"""Converter tests on synthetic spec fixtures (offline)."""

from ld_skills.convert import (
    _drop_link_toc_blocks,
    _postprocess,
    _rewrite_links,
    _strip_code_fences,
    assemble_document,
    convert_spec,
)
from ld_skills.validate import validate_markdown

RESPEC_FIXTURE = """<html><head><title>Test Spec W3C Working Draft</title></head>
<body>
<div class="head">
  <h1 id="title">Test Spec</h1>
  <p>W3C Working Draft, <time datetime="2026-01-01">1 January 2026</time></p>
</div>
<nav id="toc"><ol><li><a href="#intro">1. Introduction</a></li></ol></nav>
<div id="respec-ui" hidden></div>
<main>
<section id="abstract" class="introductory"><h2>Abstract</h2>
<p>A <abbr title="Resource Description Framework">RDF</abbr> test spec.</p></section>
<section id="sotd"><p>Status text that is noise.</p></section>
<section id="sec-intro"><h2 id="x1">1. Introduction <a class="self-link" href="#sec-intro">¶</a></h2>
<p>See the <a href="#terms">defined terms</a> and <a href="#unknown-frag">nowhere</a>.</p>
<aside class="note"><p>Notes matter.</p></aside>
<aside class="example"><pre>ex:a ex:b ex:c .</pre></aside>
</section>
<section id="terms"><h3 id="x1-1">1.1 Terms</h3>
<p>Definitions of <a href="#dfn-widget">widgets</a> live here.</p>
<table><tr><th>Term</th><th>Meaning</th></tr><tr><td>widget</td><td>a thing</td></tr></table>
</section>
</main>
<script>document.getElementById("x");</script>
<footer>site chrome</footer>
</body></html>"""

OLD_W3C_FIXTURE = """<html><head><title>Old Spec</title></head><body>
<div class="head">
<p><a name="spec">Old Spec</a> W3C Recommendation</p>
<dl><dt>This version:</dt><dd><a>http://www.w3.org/TR/2013/REC-old-20130101/</a></dd></dl>
</div>
<nav id="toc"><p class="toc"><a href="#intro">1. Introduction</a><br/><a href="#grammar">2. Grammar</a></p></nav>
<h2 id="intro">1. Introduction</h2>
<p>Intro text with <a href="#grammar">grammar link</a>.</p>
<h2 id="grammar">2. Grammar</h2>
<div class="grammarTable"><table>
<tr><td>[1]</td><td>Term</td><td>::=</td><td><a href="#prod-a">A</a> | <a href="#prod-b">B</a></td></tr>
</table></div>
<p class="copyright">Copyright noise.</p>
<p class="toc"><a href="#intro">1. Introduction</a><br/><a href="#grammar">2. Grammar</a></p>
</body></html>"""

OGC_FIXTURE = """<html><body>
<header>OGC site nav</header>
<h1>Geo Test</h1>
<p><img alt="overview diagram" src="data:image/png;base64,iVBORw0KGGO"/></p>
<p>Internal <a href="#clause-1">clause link</a> and <a href="https://example.org/#x">external</a>.</p>
<h2 id="clause-1">Clause 1</h2>
<p>Body text.</p>
<footer>copyright boilerplate</footer>
</body></html>"""


def test_respec_conversion_captures_and_cleans():
    result = convert_spec(RESPEC_FIXTURE, "https://example.org/spec/")
    md = result.markdown

    # Kept information
    assert "Introduction" in md
    assert "ex:a ex:b ex:c ." in md  # example survives as code
    assert "| Term" in md and "| Meaning |" in md  # table survives
    assert "**Note:**" in md or "**Note**" in md  # note labeled
    terms = [s for s in result.sections if s.title == "Terms"]
    assert terms and terms[0].number == "1.1"  # explicit numbers preserved
    assert "RDF" in md and "Resource Description Framework)" not in md  # abbr not expanded

    # Noise removed
    assert "Status text that is noise" not in md
    assert "site chrome" not in md
    assert "Table of Contents" not in md
    assert "respec" not in md.lower()
    assert "¶" not in md
    assert "getElementById" not in md

    # Links rewritten: known section keeps a § reference, unknown becomes text
    assert "](#" not in md
    assert "nowhere" in md
    assert "§" in md

    # Metadata
    assert result.title == "Test Spec"
    assert result.status == "W3C Working Draft"  # from head text (no TR-dated URL)


def test_status_from_tr_url():
    result = convert_spec(RESPEC_FIXTURE, "https://www.w3.org/TR/2013/REC-old-20130101/")
    assert result.status == "W3C Recommendation"
    assert result.date == "2013-01-01"


def test_old_w3c_layout():
    result = convert_spec(OLD_W3C_FIXTURE, "https://www.w3.org/TR/old/")
    md = result.markdown

    assert "1. Introduction" in md or "Introduction" in md
    assert "::=" in md  # grammar production survives
    assert "This version" not in md
    assert "Copyright noise" not in md
    assert "| Term |" in md or "Term" in md

    # Explicit section numbers win over computed ones
    numbers = {s.number for s in result.sections}
    assert "1" in numbers and "2" in numbers

    # TOC paragraphs of links are dropped as noise
    assert md.count("grammar link") <= 1


def test_ogc_layout_and_data_images():
    result = convert_spec(OGC_FIXTURE, "https://example.org/geo/")
    md = result.markdown

    assert "OGC site nav" not in md
    assert "copyright boilerplate" not in md
    assert "data:image/png" not in md
    assert "*overview diagram*" in md  # image becomes italic caption
    assert "external" in md  # external link kept
    assert "[clause link (§1)]" not in md  # no bracketed dead link


def test_drop_link_toc_blocks():
    md = "before\n" + "\n".join(f"[Section {i}](#s{i})" for i in range(8)) + "\nafter"
    out = _drop_link_toc_blocks(md)
    assert "Section 3" not in out
    assert "before" in out and "after" in out

    # A short run of links stays (inline references, not a TOC)
    short = "see [a](#a) and [b](#b)"
    assert _drop_link_toc_blocks(short) == short


def test_postprocess_collapses_and_strips():
    md = "para   \n\n\n\n\nnext\n\n¶\n\nBack to Contents\n"
    out = _postprocess(md)
    assert "\n\n\n" not in out
    assert "¶" not in out
    assert "Back to Contents" not in out
    assert "para" in out and "next" in out


def test_strip_code_fences_handles_blockquotes():
    md = "text\n> ```\n> <script>alert(1)</script>\n> ```\nmore <div>"
    prose = _strip_code_fences(md)
    assert "<script" not in prose
    assert "<div>" in prose


def test_validate_markdown():
    good = "# T\n\n## A\n\ntext\n\n## B\n\n" + "word " * 400
    assert validate_markdown(good).ok

    # HTML residue outside code is an error
    bad = good.replace("text", "<div>leaked</div>")
    assert not validate_markdown(bad).ok

    # Inline-code markup is example content, not residue
    inline = good.replace("text", "use `<script>` tags in HTML")
    assert validate_markdown(inline).ok

    assert not validate_markdown("too short").ok


def test_rewrite_links_is_linear_on_bracket_heavy_text():
    """Regression: an ambiguous link-text regex caused catastrophic
    backtracking (infinite-looking CPU spin) on grammar tables full of
    brackets and escaped pipes."""
    import time

    from ld_skills.structure import Section

    line = "| `[99]` | `BlankNodePropertyList` | ::= | `''` `[`PropertyListNotEmpty` `']'` `\\|` `[a-z]` "
    segment = "\n".join([line + str(i) for i in range(200)])
    anchors = {"prod": Section("prod", ["prod"], "9.9", "Productions", 2)}

    start = time.monotonic()
    out, _ = _rewrite_links(segment, anchors)
    elapsed = time.monotonic() - start

    assert elapsed < 2.0, f"regex blew up: {elapsed:.1f}s"
    assert "[99]" in out


def test_assemble_document_header():
    from ld_skills.structure import Section

    result = convert_spec(RESPEC_FIXTURE, "https://example.org/spec/")
    result.sections = [Section("a", ["a"], "1", "One", 2)]
    doc = assemble_document(
        result,
        source_url="https://example.org/spec/",
        fetched="2026-10-21",
        family="test",
        label="Test Spec",
        version="1.0",
        description="A test spec.",
    )
    assert doc.startswith("---\n")
    assert "source: https://example.org/spec/" in doc
    assert "fetched: 2026-10-21" in doc
    assert "# Test Spec" in doc
    assert "## Contents" in doc
    assert "- 1 One" in doc
