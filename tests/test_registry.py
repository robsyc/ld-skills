"""Registry loading and validation tests."""

from pathlib import Path

import yaml

from ld_skills.build import load_registry

REGISTRY = Path(__file__).parent.parent / "registry" / "index.yaml"


def test_registry_loads_and_validates():
    registry, errors = load_registry(REGISTRY)
    assert errors == []
    assert len(registry.families) >= 8
    assert len(registry.specs) >= 80
    assert len(registry.namespaces) >= 8


def test_registry_entries_are_complete():
    raw = yaml.safe_load(REGISTRY.read_text())
    for family, data in raw.items():
        assert data.get("label"), f"family {family} missing label"
        for spec in data.get("specifications") or []:
            assert spec["key"] and spec["uri"].startswith("http"), family
            assert spec.get("label") and spec.get("comment"), spec["key"]
        for ns in data.get("namespaces") or []:
            assert ns["key"] and ns["uri"].startswith("http"), family


def test_registry_rejects_duplicates(tmp_path):
    bad = tmp_path / "bad.yaml"
    bad.write_text(
        """
f:
  label: F
  specifications:
    - {key: dup, label: A, comment: c, uri: "https://a.example/"}
    - {key: dup, label: B, comment: c, uri: "https://b.example/"}
"""
    )
    _, errors = load_registry(bad)
    assert any("duplicate" in e for e in errors)


def test_registry_rejects_bad_keys(tmp_path):
    bad = tmp_path / "bad.yaml"
    bad.write_text(
        """
F:
  label: F
  specifications:
    - {key: ok, label: A, comment: c, uri: "https://a.example/"}
"""
    )
    _, errors = load_registry(bad)
    assert any("dir-safe" in e for e in errors)
