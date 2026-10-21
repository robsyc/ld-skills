"""HTML-to-Markdown conversion pipeline for specification documents.

Goal: maximum information capture with minimal noise.

Pipeline:
  1. extract.py   — strip boilerplate (nav, TOC, UI chrome, permalinks),
                    isolate main content, normalize notes into blockquotes,
                    capture title/status/date metadata.
  2. structure.py — anchor/section map for the document.
  3. html-to-markdown (kreuzberg) — the HTML -> Markdown engine, same library
                    proven in ld-mcp, with base_url so links/images resolve.
  4. post-process — rewrite internal fragment links to section references
                    ("see <a href=#x>BLEND</a>" -> "BLEND (§18.2.1)"), drop
                    empty/anchor-only links, collapse whitespace.
  5. assemble     — YAML frontmatter + title + compact TOC + content.
"""

import re
from dataclasses import dataclass, field

from bs4 import Tag  # noqa: F401  (re-exported for typing convenience)
from html_to_markdown import (
    CodeBlockStyle,
    ConversionOptions,
    HeadingStyle,
    HiddenContent,
    convert,
)

from ld_skills.extract import ExtractedDoc, extract_doc
from ld_skills.structure import Section, build_section_map, section_index, table_of_contents


@dataclass
class ConversionResult:
    markdown: str
    title: str
    status: str
    date: str
    warnings: list[str] = field(default_factory=list)
    sections: list[Section] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Post-processing
# ---------------------------------------------------------------------------

# Markdown link with optional quoted title: [text](url "Title (with parens)").
# Link text may contain escaped brackets (\]). The text group must be
# unambiguous (escape branch owns backslashes, the class excludes them) or
# backslash/bracket-heavy grammar tables cause catastrophic backtracking.
_MD_LINK_RE = re.compile(
    r"\[((?:\\.|[^\[\]\\])*)\]\(\s*<?([^)>\s]+)>?(?:\s+\"[^\"]*\")?\s*\)"
)

_FENCE_LINE_RE = re.compile(r"^\s*(?:>\s*)*`{3,}")


def _map_outside_fences(md: str, fn) -> str:
    """Apply fn to segments of markdown outside fenced code blocks (which may
    be nested in blockquotes: "> ```")."""
    buf: list[str] = []
    final: list[str] = []
    for line in md.splitlines(keepends=True):
        if _FENCE_LINE_RE.match(line):
            if buf:
                final.append(fn("".join(buf)))
                buf = []
            final.append(line)
            continue
        buf.append(line)
    if buf:
        final.append(fn("".join(buf)))
    return "".join(final)


def _rewrite_links(md: str, anchors: dict[str, Section], base_urls: tuple[str, ...] = ()) -> tuple[str, int]:
    """Rewrite markdown links: internal fragments become section references.

    Links whose target is one of base_urls plus a fragment are treated as
    internal links too (grammar tables in SPARQL use absolute same-document
    hrefs).
    """
    rewritten = 0
    doc_prefixes: list[str] = []
    for u in base_urls:
        if u:
            doc_prefixes.append(u + "#")
            doc_prefixes.append(u.rstrip("/") + "#")
    doc_prefixes = tuple(doc_prefixes)

    def replace(match: re.Match) -> str:
        nonlocal rewritten
        text, target = match.group(1), match.group(2).strip()
        # Some generators escape characters inside URLs (\-, \_).
        target = target.replace("\\-", "-").replace("\\_", "_").replace("\\#", "#")
        if target.startswith("mailto:"):
            rewritten += 1
            return text
        if not text or text.strip() in {"¶", "§", "#", "»", "Ⓣ", "↑", "↩"}:
            rewritten += 1
            return ""
        if target.startswith("#") or (
            doc_prefixes and target.startswith(doc_prefixes)
        ):
            anchor = target.split("#", 1)[1] if "#" in target else ""
            section = anchors.get(anchor)
            title = text.strip()
            if anchor and title.replace("_", "-") == anchor.replace("_", "-"):
                # Pandoc-style wiki links: text mirrors the anchor id.
                title = title.replace("_", " ")
            if section is None:
                # Unknown fragment: keep the text, drop the dead link.
                rewritten += 1
                return title
            if section.title and title.lower() == section.title.lower():
                repl = f"§{section.number} {section.title}" if section.number else section.title
            else:
                repl = f"{title} (§{section.number})" if section.number else title
            rewritten += 1
            return repl
        return match.group(0)

    return _MD_LINK_RE.sub(replace, md), rewritten


def _postprocess(md: str) -> str:
    # Stray non-breaking spaces and zero-width joiners.
    md = md.replace("\u00a0", " ").replace("\u200b", "")

    # Trailing whitespace and 3+ blank lines.
    md = re.sub(r"[ \t]+$", "", md, flags=re.M)
    md = re.sub(r"\n{3,}", "\n\n", md)

    # Boilerplate one-liners that survive conversion on some layouts.
    md = re.sub(r"^\s*(¶|§|»|#|↑|▲|↩|\[\])\s*$", "", md, flags=re.M)
    md = re.sub(
        r"^\s*(back to (the )?(table of )?contents?|↑ back to top)\s*$",
        "",
        md,
        flags=re.M | re.I,
    )

    # ReSpec citation markers resolved at runtime in browsers: [[[KEY]]] / [[KEY]].
    md = re.sub(r"\[{2,3}([^\[\]]+)\]{2,3}", r"[\1]", md)

    # Definition labels glued to their value: **IRI:**http://… -> **IRI:** http://…
    md = re.sub(r"(\*\*[^*\n]+:\*\*)(?=[^\s*])", r"\1 ", md)

    # Separate "Example N:" captions from the preceding paragraph inside
    # blockquotes so renderers do not join them.
    md = _separate_example_captions(md)

    # Empty link/bold residue and stray footnote markers.
    md = re.sub(r"\[\]\([^)]*\)", "", md)
    md = re.sub(r"^[-=_*]{4,}\s*$", "", md, flags=re.M)

    # Table of contents that some old specs inline into the body:
    # long runs of lines that are just [text](#anchor) links.
    md = _drop_link_toc_blocks(md)

    # Duplicate horizontal rules and leading/trailing blanks.
    md = re.sub(r"(\n[-*]{3,}\s*\n)(\s*\n)+(\1)+", r"\1", md)
    return md.strip()


def _separate_example_captions(md: str) -> str:
    """Insert an empty blockquote line before '> Example N:' captions that
    directly follow prose, so they render as separate paragraphs."""
    out: list[str] = []
    lines = md.splitlines()
    for i, line in enumerate(lines):
        if (
            i > 0
            and re.match(r"^>\s*(?:\*\*)?Example \d", line)
            and lines[i - 1].strip()
            and not lines[i - 1].startswith(">")
            and not lines[i - 1].startswith("```")
        ):
            out.append("")
        out.append(line)
    return "\n".join(out)


_LINKY_LINE_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)?\s*\[[^\]]+\]\(#[^)]*\)\s*[,.]?\s*$")


def _drop_link_toc_blocks(md: str) -> str:
    """Remove blocks of 5+ consecutive lines that are only internal links."""
    lines = md.splitlines()
    out: list[str] = []
    run: list[str] = []
    for line in lines:
        if _LINKY_LINE_RE.match(line):
            run.append(line)
        else:
            if len(run) >= 5:
                out.append("")
            else:
                out.extend(run)
            run = []
            out.append(line)
    if len(run) >= 5:
        out.append("")
    else:
        out.extend(run)
    return "\n".join(out)


def _strip_code_fences(md: str) -> str:
    """Return markdown with fenced/indented code blocks blanked (for checks).

    Handles fences nested in blockquotes ("> ```") as produced for ReSpec
    examples.
    """
    fence_re = re.compile(r"^\s*(?:>\s*)*`{3,}")
    out: list[str] = []
    in_fence = False
    for line in md.splitlines():
        if fence_re.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def _demote_headings(md: str, floor_level: int = 2) -> str:
    """Shift heading levels so the shallowest content heading is at floor_level."""
    levels: list[int] = []
    in_fence = False
    for line in md.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s", line)
        if m:
            levels.append(len(m.group(1)))
    if not levels:
        return md
    shift = floor_level - min(levels)
    if shift == 0:
        return md

    def bump(match: re.Match) -> str:
        hashes = match.group(1)
        new_len = min(6, max(1, len(hashes) + shift))
        return "#" * new_len + " "

    out: list[str] = []
    in_fence = False
    for line in md.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        out.append(re.sub(r"^(#{1,6})\s", bump, line) if not in_fence else line)
    return "\n".join(out)


def _drop_duplicate_title(md: str, title: str) -> str:
    """Remove a leading content heading that just repeats the document title."""
    normalized = re.sub(r"\W+", "", title or "").lower()
    if not normalized:
        return md
    lines = md.splitlines()
    for i, line in enumerate(lines[:5]):
        m = re.match(r"^#{1,2}\s+(.*)$", line)
        if m and re.sub(r"\W+", "", m.group(1)).lower() == normalized:
            del lines[i]
            return "\n".join(lines).lstrip("\n")
    return md


def convert_spec(
    html: str,
    source_url: str,
    final_url: str = "",
    include_fetcher=None,
) -> ConversionResult:
    """Convert a specification HTML page into a complete markdown document."""
    # Non-breaking spaces trip up the converter (Rust byte-boundary panics)
    # and render as \xa0 noise in output; normalize them away up front.
    html = html.replace("\u00a0", " ").replace("&nbsp;", " ")
    doc: ExtractedDoc = extract_doc(
        html, source_url, final_url, include_fetcher=include_fetcher
    )
    sections = build_section_map(doc.content)
    anchors = section_index(sections)

    options = ConversionOptions(
        heading_style=HeadingStyle.ATX,
        code_block_style=CodeBlockStyle.BACKTICKS,
        autolinks=True,
        expand_abbreviations=False,
        hidden_content=HiddenContent.ALL,
        base_url=final_url or source_url,
    )
    md = convert(str(doc.content), options).content

    # Link rewriting must not touch fenced code blocks.
    md = _map_outside_fences(md, lambda seg: _rewrite_links(seg, anchors, (source_url, final_url))[0])
    md = _postprocess(md)
    md = _demote_headings(md, floor_level=2)
    md = _drop_duplicate_title(md, doc.metadata.title)

    warnings = list(doc.warnings)
    if not sections:
        warnings.append("no section anchors found")

    return ConversionResult(
        markdown=md,
        title=doc.metadata.title,
        status=doc.metadata.status,
        date=doc.metadata.date,
        warnings=warnings,
        sections=sections,
    )


def assemble_document(
    result: ConversionResult,
    *,
    source_url: str,
    fetched: str,
    family: str = "",
    label: str = "",
    version: str = "",
    description: str = "",
) -> str:
    """Build the final file: frontmatter, title, provenance, TOC, content."""
    meta_lines = [
        f'title: "{result.title.replace(chr(34), chr(39)) if result.title else label}"',
        f"source: {source_url}",
    ]
    if family:
        meta_lines.append(f"family: {family}")
    if version:
        meta_lines.append(f'version: "{version}"')
    if result.status:
        meta_lines.append(f"status: {result.status}")
    if result.date:
        meta_lines.append(f"spec_date: {result.date}")
    meta_lines.append(f"fetched: {fetched}")

    header = ["---", *meta_lines, "---", "", f"# {result.title or label}", ""]
    if description:
        header += [f"> {description}", ""]

    toc = table_of_contents(result.sections)
    if toc:
        header += ["## Contents", "", toc, "", "---", ""]

    return "\n".join(header) + "\n" + result.markdown + "\n"
