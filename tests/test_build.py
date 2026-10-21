"""Build-tree layout tests: written files must survive pruning."""

from pathlib import Path

from ld_skills.build import (
    Family,
    NamespaceEntry,
    Registry,
    SpecEntry,
    namespace_path,
    prune_orphans,
    spec_path,
)


def _registry() -> Registry:
    family = Family(
        key="rdf",
        label="RDF",
        comment="",
        specifications=[
            SpecEntry("rdf12-turtle", "Turtle", "", "https://example.org/t", "1.2")
        ],
        namespaces=[
            NamespaceEntry("sh", "SHACL", "", "https://example.org/sh#", "1.1")
        ],
    )
    return Registry([family])


def test_prune_keeps_written_files(tmp_path: Path):
    """Files written by build_spec/build_namespace must never be pruned."""
    registry = _registry()
    for family, spec in registry.specs:
        path = spec_path(tmp_path, family.key, spec.key)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# doc")
    for _, ns in registry.namespaces:
        path = namespace_path(tmp_path, ns.key)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# ttl")

    removed = prune_orphans(tmp_path, registry)

    assert removed == []
    assert spec_path(tmp_path, "rdf", "rdf12-turtle").exists()
    assert namespace_path(tmp_path, "sh").exists()


def test_prune_removes_stale_layouts(tmp_path: Path):
    """Legacy/renamed locations (e.g. namespaces/ vs _namespaces/) are cleaned."""
    stale = tmp_path / "namespaces" / "sh.ttl"
    stale.parent.mkdir(parents=True)
    stale.write_text("old location")
    orphan = tmp_path / "rdf" / "removed-spec.md"
    orphan.parent.mkdir(parents=True)
    orphan.write_text("gone")

    removed = prune_orphans(tmp_path, _registry())

    assert not stale.exists()
    assert not orphan.exists()
    assert sorted(removed) == ["namespaces/sh.ttl", "rdf/removed-spec.md"]
