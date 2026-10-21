"""Extract clean specification content and metadata from spec HTML.

Handles the three dominant spec generators plus the older W3C layouts:
  * ReSpec      (modern W3C drafts and notes, RML specs)
  * Bikeshed    (most CSS-WG and many newer Data/Semantics docs)
  * W3C "spec prod" / old-EDS (2013-era Recommendations: RDF 1.1, SPARQL 1.1, OWL 2)
  * Miscellaneous pages (rml.io and friends): strip site chrome generically
"""

import re
from dataclasses import dataclass, field
from typing import Callable, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Comment, Tag

# Elements that never carry specification content.
STRIP_TAGS = [
    "script",
    "style",
    "noscript",
    "template",
    "iframe",
    "object",
    "embed",
    "form",
    "button",
    "input",
    "select",
    "canvas",
    "audio",
    "video",
    "link",
    "meta",
]

# CSS selectors for boilerplate blocks (site chrome, TOC, editorial UI).
# Applied with soup.select() -> decompose().
STRIP_SELECTORS = [
    # W3C document header (logo, title block, status line, version list)
    "div.head",
    # Site chrome
    "header",
    "footer",
    "nav",
    # ReSpec UI + generated table of contents
    "#respec-ui",
    ".respec-header",
    ".respec-offending",
    "#toc",
    "nav#toc",
    "div.toc",
    ".toc-sidebar",
    "#issue-summary",
    # W3C "Status of the Document" block (status is captured as metadata)
    "#sotd",
    "section#sotd",
    "div#sotd",
    # Editorial chrome
    ".copyright",
    ".back-to-top",
    ".backtotoc",
    ".breadcrumb",
    ".sidebar",
    ".skip",
    "#div-quick-access",
    ".quick-access",
    # Pure-noise trailing sections
    "section#acknowledgements",
    "section#acknowledgments",
    ".acknowledgements",
    ".acknowledgments",
    "section#index-to-term-definitions",
    "section#issue-summary",
    "div.issue-summary",
    # Old-spec navigation bars
    ".navbar",
    "table.navbar",
    "hr.navbar",
]

# Headings whose text marks boilerplate sections we drop wholesale.
NOISE_HEADING_PREFIXES = (
    "acknowledg",
    "issue summary",
)

# Headings that never receive a section number (front matter, old-W3C style).
UNNUMBERED_HEADING_TITLES = {
    "abstract",
    "table of contents",
    "contents",
    "status of the document",
    "status of this document",
}


@dataclass
class SpecMetadata:
    title: str = ""
    subtitle: str = ""
    status: str = ""
    date: str = ""


@dataclass
class ExtractedDoc:
    """A cleaned spec document ready for markdown conversion."""

    metadata: SpecMetadata
    content: Tag  # the isolated main content
    soup: BeautifulSoup
    source_url: str
    warnings: list[str] = field(default_factory=list)


_TR_DATE_RE = re.compile(
    r"/(FPWD|CRD|DNOTE|REC|NOTE|PER|PR|CR|WD|DR|LC|CG)-(?:final-)?([\w-]+)-(\d{8})/"
)
_STATUS_NAMES = {
    "REC": "W3C Recommendation",
    "CR": "W3C Candidate Recommendation",
    "CRD": "W3C Candidate Recommendation Draft",
    "PR": "W3C Proposed Recommendation",
    "WD": "W3C Working Draft",
    "FPWD": "W3C First Public Working Draft",
    "NOTE": "W3C Group Note",
    "DNOTE": "W3C Draft Group Note",
    "PER": "W3C Proposed Edited Recommendation",
}


def _clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


_GENERIC_TITLES = {"", "notice", "warning", "document", "untitled", "home"}


def extract_metadata(soup: BeautifulSoup, source_url: str, final_url: str = "") -> SpecMetadata:
    """Best-effort title/subtitle/status/date extraction before boilerplate is removed."""
    meta = SpecMetadata()

    # ReSpec docs carry a respecConfig JSON blob with the real values.
    html_text = str(soup)
    m = re.search(r'"subtitle"\s*:\s*"([^"]+)"', html_text)
    if m:
        meta.subtitle = m.group(1)

    # Title: prefer the <title> tag (reliable across generators), then the
    # conventional heading locations. Reject boilerplate candidates ("Notice"
    # legal blocks on OGC pages).
    candidates: list[str] = []
    title_tag = soup.find("title")
    if title_tag:
        candidates.append(_clean_text(title_tag.get_text()))
    for el in [
        soup.select_one("h1#title"),
        soup.select_one("div.head h1"),
        soup.find("h1"),
    ]:
        if el:
            candidates.append(_clean_text(el.get_text()))

    for text in candidates:
        text = re.sub(r"\s*$", "", text)
        # ReSpec titles repeat the status in the h1 (e.g. "Turtle W3C Recommendation")
        text = re.sub(
            r"\s*(W3C (First Public )?(Working Draft|Candidate Recommendation( Draft)?|"
            r"Proposed( Edited)? Recommendation|Recommendation|Group( Draft)? Note))\s*$",
            "",
            text,
            flags=re.I,
        )
        if text and text.lower() not in _GENERIC_TITLES:
            meta.title = text
            break

    # Subtitle in the DOM: ReSpec #subtitle / .head h2 / <p class="subtitle">.
    if not meta.subtitle:
        for candidate in [
            soup.select_one("#subtitle"),
            soup.select_one("div.head h2"),
            soup.select_one("p.subtitle"),
        ]:
            if candidate:
                text = _clean_text(candidate.get_text())
                if text and text.lower() != meta.title.lower():
                    meta.subtitle = text
                break

    # Status + date: TR URLs of the form /TR/2013/REC-turtle-20130321/ are authoritative.
    for url in (final_url, source_url):
        m = _TR_DATE_RE.search(url)
        if m:
            # Status codes vary in length (REC, FPWD, DNOTE...); exact match.
            meta.status = _STATUS_NAMES.get(m.group(1).upper(), "")
            yyyymmdd = m.group(3)
            meta.date = f"{yyyymmdd[0:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:8]}"
            break

    if not meta.status:
        # Fall back to the status line in the document head region.
        head = soup.select_one("div.head") or soup.select_one("#subtitle") or soup.body or soup
        text = head.get_text(" ", strip=True)[:2000]
        for status in _STATUS_NAMES.values():
            if status.lower() in text.lower():
                meta.status = status
                break

    if not meta.date:
        # W3C docs carry <time datetime="..."> in the head/status region.
        head = soup.select_one("div.head") or soup.select_one("#sotd") or soup.body or soup
        t = head.find("time", datetime=True) if head else None
        if t:
            meta.date = t["datetime"][:10]

    if not meta.date:
        # Old W3C layouts state the date in prose: "W3C Recommendation 18 August 2009".
        # Search the header block first, then the whole body.
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
        ]
        head = soup.select_one("div.head")
        regions = [head, soup.body, soup] if head else [soup.body, soup]
        for region in regions:
            if region is None:
                continue
            text = region.get_text(" ", strip=True)[:2000]
            # Accept both "18 August 2009" and "August 18, 2009".
            m = re.search(
                r"\b(?:(\d{1,2})\s+(January|February|March|April|May|June|July|August|"
                r"September|October|November|December)|(January|February|March|April|"
                r"May|June|July|August|September|October|November|December)\s+(\d{1,2}),?)"
                r"\s+(\d{4})\b",
                text,
            )
            if m:
                year = m.group(5)
                if m.group(1):  # day-first order
                    month_name, day = m.group(2), int(m.group(1))
                else:  # month-first order
                    month_name, day = m.group(3), int(m.group(4))
                meta.date = f"{year}-{months.index(month_name) + 1:02d}-{day:02d}"
                break

    return meta


def _drop_noise_headed_sections(content: Tag, warnings: list[str]) -> None:
    """Remove trailing sections whose heading marks them as noise (acknowledgements...)."""
    for section in content.find_all("section"):
        heading = section.find(["h1", "h2", "h3", "h4", "h5", "h6"])
        if not heading:
            continue
        title = _clean_text(heading.get_text()).lower()
        if any(prefix in title for prefix in NOISE_HEADING_PREFIXES):
            section.decompose()


def _flatten_code(soup: BeautifulSoup) -> None:
    """Grammar tables wrap anchors inside one <code> element
    (``<code><a>X</a> | <a>Y</a></code>``); converting each anchor as its own
    code span yields mangled double-backtick markdown. Unwrap anchors inside
    code/pre and merge adjacent code spans within table cells so each cell
    converts to a single clean code span."""
    for scope in list(soup.find_all(["code", "pre"])):
        for a in scope.find_all(["a", "span"]):
            a.unwrap()
        for nested in scope.find_all("code"):
            if nested is not scope:
                nested.replace_with(soup.new_string(nested.get_text()))

    for cell in soup.find_all(["td", "th"]):
        codes = [c for c in cell.children if getattr(c, "name", None) == "code"]
        for i, code in enumerate(codes[1:], start=1):
            prev = code.previous_sibling
            between = prev if not getattr(prev, "name", None) else None
            if between is not None and re.fullmatch(r"[\s|]*", str(between)):
                prev.extract()
                first = codes[i - 1]
                first.append(soup.new_string(" " + code.get_text()))
                code.decompose()


def _wrap_grammar_blocks(soup: BeautifulSoup) -> None:
    """Old specs put EBNF productions in <div class="grammar"> as loose text;
    without a <pre> wrapper the line structure is lost in markdown."""
    for div in soup.find_all("div", class_="grammar"):
        pre = soup.new_tag("pre")
        for child in list(div.children):
            pre.append(child.extract())
        div.clear()
        div.append(pre)


_ARROW_GLYPHS = {"↑", "▲", "↩", "⇧", "»", "«"}


def _strip_toggle_anchors(soup: BeautifulSoup) -> None:
    """Remove "[show panel]"-style JS toggles (brackets may sit outside the
    anchor) and back-to-top arrows."""
    for a in soup.find_all("a"):
        text = _clean_text(a.get_text())
        stripped = text.strip("[]").strip()
        if re.match(r"^(show|hide)\b.{0,60}$", stripped, re.I) and "panel" in stripped.lower():
            a.decompose()
            continue
        if text in _ARROW_GLYPHS:
            a.decompose()


def _strip_permalink_anchors(soup: BeautifulSoup) -> None:
    """Remove ReSpec/Bikeshed permalink anchors (¶ / § / Ⓣ) that clutter headings."""
    for a in soup.find_all("a", class_=True):
        classes = " ".join(a.get("class", []))
        if not re.search(r"\b(permalink|self-link|marker|anchor)\b", classes):
            continue
        text = _clean_text(a.get_text())
        if not text or text in {"¶", "§", "Ⓣ", "#", "»", "¶¶"}:
            a.decompose()
            continue
        # Keep anchor text if it is real content; just unwrap the link.
        a.unwrap()


def _normalize_asides(soup: BeautifulSoup) -> None:
    """Turn note/warning/example/issue asides into blockquotes so they survive
    markdown conversion as marked-off blocks instead of loose paragraphs.
    Admonition headings (h4-h6) become bold labels to avoid double-nested
    blockquote noise."""
    for aside in soup.find_all(["aside", "div"], class_=True):
        classes = " ".join(aside.get("class", [])).lower()
        kind = next(
            (k for k in ("note", "warning", "example", "issue", "ednote", "advisement") if k in classes),
            None,
        )
        if kind is None:
            continue
        aside.name = "blockquote"
        label = aside.get("aria-label") or kind.capitalize()

        # Admonition heading -> bold label paragraph.
        heading = aside.find(["h4", "h5", "h6"])
        if heading:
            text = _clean_text(heading.get_text())
            if text:
                label = text
            heading.decompose()

        p = soup.new_tag("p")
        marker = soup.new_tag("strong")
        marker.string = f"{label}:"
        p.append(marker)
        aside.insert(0, p)


def _remove_empty_paragraphs(content: Tag) -> None:
    for p in content.find_all("p"):
        if not p.get_text(strip=True) and not p.find(["img", "table", "pre", "br"]):
            p.decompose()


def _inline_data_images(soup: BeautifulSoup) -> None:
    """Replace embedded (data-URL) images with their alt text as a caption.

    Base64 blobs are enormous token noise; the alt text carries the meaning.
    """
    for img in soup.find_all("img", src=True):
        if str(img.get("src", "")).startswith("data:"):
            alt = _clean_text(img.get("alt", "")) or "[figure]"
            caption = soup.new_tag("em")
            caption.string = alt
            img.replace_with(caption)


def _unwrap_runtime_examples(soup: BeautifulSoup) -> None:
    """ReSpec live drafts hide example code inside HTML comments and unwrap
    them at runtime (``data-transform="updateExample"``). Static converters
    drop comments, which would empty every example block — unwrap here."""
    for el in soup.find_all(attrs={"data-transform": True}):
        if el.get("data-transform") != "updateExample":
            continue
        comments = [c for c in el.find_all(string=True) if isinstance(c, Comment)]
        if not comments:
            continue
        content = "\n".join(str(c) for c in comments).strip()
        el.clear()
        el.append(soup.new_string(content))


def _resolve_runtime_includes(
    soup: BeautifulSoup, base_url: str, fetcher: Optional[Callable[[str], str]]
) -> list[str]:
    """ReSpec ``data-include`` pulls fragments at runtime (e.g. the N3
    grammar). Inline them while converting so nothing is lost."""
    warnings: list[str] = []
    if not fetcher:
        for el in soup.find_all(attrs={"data-include": True}):
            src = el["data-include"]
            warnings.append(f"runtime include not fetched: {src}")
        return warnings
    for el in list(soup.find_all(attrs={"data-include": True})):
        src = el.get("data-include", "")
        url = urljoin(base_url, src)
        try:
            fragment = fetcher(url)
        except Exception as e:  # noqa: BLE001 — keep building without the include
            warnings.append(f"data-include {src} failed: {e}")
            continue
        if el.get("data-include-format") == "text":
            el.clear()
            el.append(soup.new_string(fragment))
        else:
            included = BeautifulSoup(fragment, "html.parser")
            replace = el.get("data-include-replace") == "true"
            for attr in ("data-include", "data-include-format", "data-include-replace"):
                el.attrs.pop(attr, None)
            if replace:
                el.replace_with(*included.children)
            else:
                for child in list(included.children):
                    el.append(child.extract())
    return warnings


def extract_doc(
    html: str,
    source_url: str,
    final_url: str = "",
    include_fetcher: Optional[Callable[[str], str]] = None,
) -> ExtractedDoc:
    """Parse spec HTML and return cleaned main content plus metadata."""
    warnings: list[str] = []
    soup = BeautifulSoup(html, "html.parser")

    metadata = extract_metadata(soup, source_url, final_url)

    warnings += _resolve_runtime_includes(
        soup, final_url or source_url, include_fetcher
    )
    _unwrap_runtime_examples(soup)
    _flatten_code(soup)
    _wrap_grammar_blocks(soup)

    for tag in soup.find_all(STRIP_TAGS):
        tag.decompose()

    _inline_data_images(soup)

    for selector in STRIP_SELECTORS:
        for el in soup.select(selector):
            el.decompose()

    # Old W3C docs put "Status of This Document" as a bare h2 with sibling
    # paragraphs (no #sotd container) — remove the run up to the next heading.
    for heading in list(soup.find_all(["h1", "h2", "h3"])):
        title = _clean_text(heading.get_text()).lower().rstrip(":")
        if title not in {"status of the document", "status of this document"}:
            continue
        if heading.find_parent("section"):
            heading.find_parent("section").decompose()
            continue
        heading.decompose()
        for sibling in list(heading.find_next_siblings()):
            if sibling.name in ["h1", "h2", "h3"]:
                break
            sibling.decompose()

    # Bare "Table of Contents" headings left behind after the nav is removed.
    for heading in soup.find_all(["h1", "h2", "h3"]):
        if _clean_text(heading.get_text()).lower() in {"table of contents", "contents"}:
            heading.decompose()

    _strip_toggle_anchors(soup)
    _strip_permalink_anchors(soup)
    _normalize_asides(soup)

    # Main content: <main>, <article>, or the body itself.
    content_root = soup.find("main") or soup.find("article") or soup.body or soup
    if content_root is soup:
        warnings.append("no main/article/body container found; converting whole document")

    _drop_noise_headed_sections(content_root, warnings)
    _remove_empty_paragraphs(content_root)

    return ExtractedDoc(
        metadata=metadata,
        content=content_root,
        soup=soup,
        source_url=source_url,
        warnings=warnings,
    )
