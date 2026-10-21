# ld-skills
 
Agent skills that bundle the RDF / Linked Data specification suite as static
markdown — no MCP server, no runtime fetching. Where [ld-mcp](../ld-mcp)
served W3C specs section-by-section over MCP, this repo builds them once into
a single skill (`skills/ld-specs/`) that any agent can read offline.
 
```
skills/ld-specs/
├── SKILL.md                  # skill entry point (triggers + usage)
└── references/
    ├── index.md              # catalog: what is where
    ├── rdf/                  # one markdown file per specification
    │   ├── rdf12-turtle.md
    │   ├── rdf12-concepts.md
    │   └── …
    ├── sparql/  owl/  shacl/  jsonld/  skos/  prov/
    ├── mapping/              # RML, YARRRML, R2RML
    ├── vocabularies/         # DCAT, Data Cube, VoID, SSN/SOSA, GeoSPARQL, vCard
    ├── web/                  # LDP, RDFa, Notation3
    └── _namespaces/          # Turtle snapshots of the core vocabularies
        ├── shacl.ttl  owl.ttl  skos.ttl  rml.ttl  …
```
 
~95 specifications across 11 families, each converted from its canonical
source (W3C `/TR/`, w3id.org/kg-construct, OGC) into clean markdown:
boilerplate stripped, examples and tables preserved, internal links collapsed
to `§` section references, provenance recorded in frontmatter.
 
## Using the skill
 
Copy or symlink `skills/ld-specs/` into your agent's skills directory:
 
| Agent | Location |
|-------|----------|
| Claude Code | `.claude/skills/` or `~/.claude/skills/` (project or user scope) |
| Generic agents | `.agents/skills/` |
 
The skill triggers on RDF/SPARQL/SHACL/OWL/RML/etc. work; agents read
`references/index.md`, then the relevant spec file, searching within it for
the term they need.
 
## Updating the snapshots
 
A GitHub Actions cron job (`.github/workflows/update.yml`, Mondays 04:17 UTC)
rebuilds every snapshot and commits changes. Undated W3C `/TR/` URLs follow
the latest published edition automatically, so new Recommendations are picked
up without registry changes.
 
Locally:
 
```bash
uv sync
uv run ld-skills check            # validate registry
uv run ld-skills build            # rebuild skills/ld-specs/references
uv run ld-skills build --only rdf12-turtle rml-core   # subset (uses .cache/)
uv run ld-skills build --refresh  # bypass cache
```
 
Adding a specification: add an entry to `registry/index.yaml` (family →
specifications → key/label/comment/uri), run `uv run ld-skills build --only
<key>`, and open a PR.
 
## Conversion pipeline
 
`src/ld_skills/` (reuses [ld-mcp](https://github.com/robsyc/ld-mcp)'s
proven [html-to-markdown](https://github.com/kreuzberg-dev/html-to-markdown)
engine underneath):
 
1. **extract** — strip nav/TOC/UI chrome/status blocks/permalinks, isolate
   main content, unwrap ReSpec's runtime transforms (`updateExample` comment
   blocks, `data-include` fragments), flatten grammar-table code spans.
2. **structure** — build a section map (anchors, numbers, titles) that
   understands ReSpec `<section id>`, Bikeshed `secno`, and 2013-era
   `<a name>` headings; appendices keep their letters.
3. **convert** — HTML → markdown; internal fragment links become
   `text (§N.M)` references; citation markers, dead links, and noise lines
   are removed; example captions and notes are kept as blockquotes.
4. **validate** — every output is checked for markup residue, missing
   headings, and undersized files; the build fails loudly otherwise.
 
The converter was stress-tested by sub-agent audits against source HTML
across all generator styles (modern ReSpec, 2013-era W3C, OGC, ReSpec CG
drafts).
 
### Deliberate removals
 
Acknowledgements sections, status-of-the-document text, tables of contents
(replaced by a generated `## Contents`), and site chrome are dropped as noise.
Everything else — examples, tables, grammar productions, notes, references —
is preserved. Each file's frontmatter records `source`, `status`,
`spec_date`, and `fetched`.
 
## Development
 
```bash
uv sync --group dev
uv run pytest -v        # converter unit tests + registry validation
uv run ruff check src/ tests/
```
 
## License
 
MIT for the code. The specification snapshots remain under their respective
source licenses (W3C per-document license, OGC); each file records its source
URL — follow it for license text and the authoritative version.
