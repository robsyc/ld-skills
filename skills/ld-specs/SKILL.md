---
name: ld-specs
description: Offline reference library of RDF / Linked Data specifications for answering precise syntax, semantics, and vocabulary questions. Use when working with RDF (1.2), Turtle, TriG, N-Triples, N-Quads, JSON-LD, RDF/XML, Notation3, SPARQL, SHACL, OWL, SKOS, PROV, DCAT, SSN/SOSA, GeoSPARQL, OWL-Time, vCard, VoID, RDF data cubes, LDP, RDFa, R2RML, or RML/YARRRML.
---

# Linked Data Specifications

Full-text snapshots of the official RDF / Linked Data specifications, converted
to clean markdown. Use these instead of guessing syntax or recalling from
memory — they are the normative source of truth.

## How to use

1. Read `references/index.md` to find the right file. Files are organized as
   `references/<family>/<spec>.md` (e.g. `references/rdf/rdf12-turtle.md`).
2. Open the spec file. The `## Contents` block near the top lists all
   sections; jump by searching for a section number or heading text.
3. Search within a spec file (case-insensitively) for the term you need —
   keyword names (`sh:minCount`, `rml:logicalSource`, `@context`), grammar
   productions (`IRIREF`, `PropertyPath`), or section titles.
4. Read only the relevant section: files are large, so use search + a window
   of surrounding lines rather than reading whole files.
5. For term definitions of the core vocabularies (rdf, rdfs, owl, sh, skos,
   prov, time, dcat, qb, sosa, rml), the Turtle snapshots in
   `references/_namespaces/*.ttl` give the exact classes and properties —
   load them into rdflib or read them directly.

## Gotchas

- Snapshots may lag behind the live spec. Check the `source` URL in a file's
  frontmatter when currency is critical (drafts like SPARQL 1.2 and RML move
  often; undated W3C `/TR/` URLs always serve the latest edition).
- Version pairing matters: RDF 1.2 / SPARQL 1.2 / SHACL 1.2 documents
  reference each other. Don't mix 1.1 and 1.2 statements when answering
  normative questions.
- RDF-star (quoted/annotated triples) was folded into RDF 1.2 as *triple
  terms* (`<< ... >>`, `rdf:reifies`). The 2021 RDF-star CG report is kept for
  the SPARQL-star syntax, but RDF 1.2 documents are authoritative.
- Section links in the text were rewritten to `§N.M` references; `#fragment`
  links do not resolve — use the Contents list or search instead.
- Normative keywords (MUST, SHOULD, MAY) and "This section is non-normative"
  markers are preserved verbatim — respect them when citing rules.
