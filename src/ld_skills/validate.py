"""Post-build sanity checks over generated markdown files.

Errors fail the build; warnings are reported but tolerated. All content
checks run outside fenced code blocks, where HTML fragments may legitimately
appear as examples.
"""

import re
from dataclasses import dataclass, field

from ld_skills.convert import _strip_code_fences

FORBIDDEN_RESIDUE = [
    (re.compile(r"<script\b", re.I), "script tag residue"),
    (re.compile(r"<div\b", re.I), "div tag residue"),
    (re.compile(r"<nav\b", re.I), "nav tag residue"),
    (re.compile(r"respec-ui", re.I), "respec UI residue"),
    (re.compile(r"javascript:", re.I), "javascript URL residue"),
    (re.compile(r"\[¶\]|\[§\]"), "permalink residue"),
    (re.compile(r"&#\d+;|&nbsp;"), "HTML entity residue"),
    # Real JS leaks look like DOM API calls; <script> tags are stripped in
    # preprocessing, so we only check for unambiguous browser API usage.
    (re.compile(r"document\.getElementById\s*\(|window\.addEventListener\s*\(|console\.log\s*\("), "JS code leak"),
]

MIN_BYTES = 1500
MIN_HEADINGS = 3


@dataclass
class ValidationResult:
    ok: bool = True
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, msg: str) -> None:
        self.ok = False
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def validate_markdown(markdown: str, key: str = "") -> ValidationResult:
    result = ValidationResult()
    prefix = f"{key}: " if key else ""

    if len(markdown.encode()) < MIN_BYTES:
        result.error(f"{prefix}output too small ({len(markdown.encode())} bytes)")
        return result

    # Check prose only: blank out fenced blocks and inline code spans, where
    # markup like <script> or <div> is legitimate example content.
    prose = re.sub(r"`[^`\n]*`", "", _strip_code_fences(markdown))

    for pattern, label in FORBIDDEN_RESIDUE:
        hits = pattern.findall(prose)
        if hits:
            result.error(f"{prefix}{label} ({len(hits)}x)")

    headings = re.findall(r"^#{1,6}\s+\S", prose, flags=re.M)
    if len(headings) < MIN_HEADINGS:
        result.error(f"{prefix}only {len(headings)} headings")

    if re.search(r"\n{4,}", markdown):
        result.warn(f"{prefix}excessive blank-line runs")

    longest = max((len(line) for line in markdown.splitlines()), default=0)
    if longest > 4000:
        result.warn(f"{prefix}very long line ({longest} chars)")

    link_count = len(re.findall(r"\]\(#", markdown))
    if link_count > 50:
        result.warn(f"{prefix}{link_count} unresolved internal links")

    return result
