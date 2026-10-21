"""Section structure: numbering, anchor resolution, and table-of-contents.

Anchors come from several places: headings with their own id, ``<section
id>`` containers (ReSpec/Bikeshed), and ``<a name>/<a id>`` inside headings
(2013-era W3C layouts). For each anchor we record a section number and title
so internal links like [text](#anchor) can be rewritten to "text (§1.1)" in
the generated markdown.

Numbering preference: if the heading text itself starts with a number or
roman numeral ("5.1 Tokenizing URIs", "II. Preface" — Bikeshed and old-W3C
docs embed them), that explicit number wins; otherwise a document-order
counter is used (ReSpec live drafts).
"""

import re
from dataclasses import dataclass

from bs4 import Tag

HEADING_TAGS = ["h1", "h2", "h3", "h4", "h5", "h6"]

_EXPLICIT_NUM_RE = re.compile(r"^((?:\d+|[A-Z]|[IVXLCDM]{1,6})(?:\.\d+)*)\.?\s+\S")
_APPENDIX_RE = re.compile(r"^Appendix\s+([A-Z](?:\.\d+)*)\.?\s+(\S.*)$")
_PART_RE = re.compile(r"^(part\s+\d+|appendices?)\b", re.I)

# Front-matter headings that never receive a number.
_UNNUMBERED_TITLES = {
    "abstract",
    "table of contents",
    "contents",
    "status of the document",
    "status of this document",
    "change log",
    "revision history",
}


@dataclass
class Section:
    anchor: str  # primary anchor (heading id or nearest ancestor id)
    anchors: list[str]  # all anchors resolving to this section
    number: str  # explicit number from heading text, else computed
    title: str  # heading text without the leading number
    level: int


def _heading_text(heading: Tag) -> str:
    return re.sub(r"\s+", " ", heading.get_text()).strip()


def _anchors_for(heading: Tag) -> list[str]:
    """All anchors that reference this heading: its own id, an id/name on a
    descendant anchor or span (old W3C: ``<h2><a name="x"/>Title</h2>``), and
    the id of the nearest ancestor element whose first heading is this one."""
    anchors: list[str] = []
    if heading.get("id"):
        anchors.append(str(heading["id"]))
    if not anchors:
        for child in heading.find_all(["a", "span"]):
            child_id = child.get("id") or child.get("name")
            if child_id:
                anchors.append(str(child_id))
                break
    for parent in heading.parents:
        pid = parent.get("id") if hasattr(parent, "get") else None
        if pid and parent.find(HEADING_TAGS) is heading:
            anchors.append(str(pid))
            break  # higher ancestors contain other headings first
    return anchors


def build_section_map(content: Tag) -> list[Section]:
    """Walk headings in document order and build the flat section list.

    Headings inside tables or pre blocks (grammar productions) are skipped.
    Front-matter headings (Abstract, ToC, status) and "Part N" dividers stay
    in the map for anchor resolution but never receive numbers. After the
    first lettered appendix, computed numbers stop (appendix zone).
    """
    sections: list[Section] = []
    counters = [0] * 7  # counters[level] for levels 1..6
    seen_letter_appendix = False

    for heading in content.find_all(HEADING_TAGS):
        if heading.find_parent(["table", "pre"]):
            continue

        level = int(heading.name[1])
        title = _heading_text(heading)
        if not title:
            continue

        anchors = _anchors_for(heading)
        if not anchors:
            # Some generators (MediaWiki-exported W3C docs) emit headings with
            # no ids at all. Synthesize one from the title so numbering and
            # the TOC still cover these sections.
            slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
            anchors = [f"x-{slug}"] if slug else []

        classes = " ".join(heading.get("class", [])).lower()
        parent_section = heading.find_parent("section")
        parent_classes = (
            " ".join(parent_section.get("class", [])).lower() if parent_section else ""
        )
        skip_number = (
            "no-num" in classes
            or "notoc" in classes
            or "no-toc" in classes
            or "introductory" in classes
            or "introductory" in parent_classes
            or title.lower() in _UNNUMBERED_TITLES
            or bool(_PART_RE.match(title))
        )

        explicit = None
        appendix_m = _APPENDIX_RE.match(title)
        if appendix_m and not skip_number:
            explicit = appendix_m.group(1)
            title = appendix_m.group(2)
        else:
            m = _EXPLICIT_NUM_RE.match(title)
            if m and not skip_number:
                explicit = m.group(1)
        if explicit:
            clean_title = re.sub(
                r"^(?:\d+|[A-Z]|[IVXLCDM]{1,6})(?:\.\d+)*\.?\s+", "", title
            )
        else:
            clean_title = title

        if explicit and explicit[0].isdigit():
            number = explicit
            # Keep computed counters in sync with explicit numbers so any
            # later computed heading continues the sequence.
            parts = [int(p) for p in explicit.split(".")]
            for i, value in enumerate(parts, start=1):
                counters[i] = value
            for deeper in range(len(parts) + 1, 7):
                counters[deeper] = 0
        elif explicit:
            # Appendix letters / roman-numeral clauses never feed counters.
            number = explicit
            seen_letter_appendix = True
        elif skip_number or seen_letter_appendix:
            number = ""
        else:
            counters[level] += 1
            for deeper in range(level + 1, 7):
                counters[deeper] = 0
            parts = [str(counters[i]) for i in range(1, level + 1)]
            # Drop leading zero components (document title is the h1, so
            # top-level sections usually live at h2).
            while parts and parts[0] == "0":
                parts.pop(0)
            # An inner zero means an unnumbered heading inside a numbered one
            # (e.g. ReSpec's media-type appendix).
            number = ".".join(parts) if parts and "0" not in parts else ""

        sections.append(
            Section(
                anchor=anchors[0],
                anchors=anchors,
                number=number,
                title=clean_title,
                level=level,
            )
        )

    return sections


def section_index(sections: list[Section]) -> dict[str, Section]:
    """Anchor -> Section map (first occurrence wins on duplicate anchors)."""
    index: dict[str, Section] = {}
    for s in sections:
        for anchor in s.anchors:
            index.setdefault(anchor, s)
    return index


def table_of_contents(sections: list[Section], max_entries: int = 200) -> str:
    """Render a compact TOC of h2-h4 sections for the file header."""
    lines: list[str] = []
    shown = 0
    for s in sections:
        if s.level > 4 or not s.title:
            continue
        indent = "  " * max(0, s.level - 2)
        number = f"{s.number} " if s.number else ""
        lines.append(f"{indent}- {number}{s.title}")
        shown += 1
        if shown >= max_entries:
            lines.append(f"{indent}- …")
            break
    return "\n".join(lines)


def parse_markdown_headings(markdown: str) -> list[tuple[int, str]]:
    """Recover (level, title) pairs from generated markdown headings (for tests)."""
    out: list[tuple[int, str]] = []
    in_fence = False
    for line in markdown.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            out.append((len(m.group(1)), m.group(2).strip()))
    return out
