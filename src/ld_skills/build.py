"""Build the ld-specs skill: fetch specs from the registry, convert them to
markdown, and assemble the skill's references/ tree.

Usage:
    ld-skills build [--registry PATH] [--out DIR] [--cache DIR]
                    [--refresh] [--only KEY ...] [--no-namespaces]
    ld-skills check   # validate the registry without fetching
"""

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from ld_skills.convert import assemble_document, convert_spec
from ld_skills.fetch import fetch_html
from ld_skills.namespaces import extract_resources, fetch_namespace_graph, serialize_namespace
from ld_skills.validate import validate_markdown

DEFAULT_REGISTRY = Path(__file__).parent.parent.parent / "registry" / "index.yaml"
DEFAULT_OUT = Path(__file__).parent.parent.parent / "skills" / "ld-specs" / "references"

_DIR_SAFE_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
_URL_RE = re.compile(r"^https?://\S+$")


@dataclass
class SpecEntry:
    key: str
    label: str
    comment: str
    uri: str
    version: str


@dataclass
class NamespaceEntry:
    key: str
    label: str
    comment: str
    uri: str
    version: str


@dataclass
class Family:
    key: str
    label: str
    comment: str
    specifications: list[SpecEntry]
    namespaces: list[NamespaceEntry]


@dataclass
class Registry:
    families: list[Family]

    @property
    def specs(self) -> list[tuple[Family, SpecEntry]]:
        return [(f, s) for f in self.families for s in f.specifications]

    @property
    def namespaces(self) -> list[tuple[Family, NamespaceEntry]]:
        return [(f, n) for f in self.families for n in f.namespaces]


@dataclass
class BuildReport:
    ok: list[str] = field(default_factory=list)
    failed: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def success(self) -> bool:
        return not self.failed


def load_registry(path: Path) -> tuple[Registry, list[str]]:
    """Load and structurally validate the registry; returns (registry, errors)."""
    errors: list[str] = []
    raw = yaml.safe_load(path.read_text()) or {}

    families: list[Family] = []
    seen_specs: set[str] = set()
    seen_ns: set[str] = set()

    for family_key, data in raw.items():
        if not _DIR_SAFE_RE.match(str(family_key)):
            errors.append(f"family key '{family_key}' must be lowercase/dir-safe")
            continue
        specs = []
        for s in data.get("specifications") or []:
            key = s.get("key")
            if not key or not _DIR_SAFE_RE.match(str(key)):
                errors.append(f"invalid spec key {key!r} in family '{family_key}'")
                continue
            if key in seen_specs:
                errors.append(f"duplicate spec key '{key}'")
                continue
            if not _URL_RE.match(s.get("uri", "")):
                errors.append(f"spec '{key}': invalid uri {s.get('uri')!r}")
                continue
            seen_specs.add(key)
            specs.append(
                SpecEntry(
                    key=key,
                    label=s.get("label", key),
                    comment=s.get("comment", ""),
                    uri=s["uri"],
                    version=str(s.get("version", "")),
                )
            )

        nss = []
        for n in data.get("namespaces") or []:
            key = n.get("key")
            if not key or not _DIR_SAFE_RE.match(str(key)):
                errors.append(f"invalid namespace key {key!r} in family '{family_key}'")
                continue
            if key in seen_ns:
                errors.append(f"duplicate namespace key '{key}'")
                continue
            if not _URL_RE.match(n.get("uri", "")):
                errors.append(f"namespace '{key}': invalid uri {n.get('uri')!r}")
                continue
            seen_ns.add(key)
            nss.append(
                NamespaceEntry(
                    key=key,
                    label=n.get("label", key),
                    comment=n.get("comment", ""),
                    uri=n["uri"],
                    version=str(n.get("version", "")),
                )
            )

        families.append(
            Family(
                key=str(family_key),
                label=data.get("label", str(family_key)),
                comment=data.get("comment", ""),
                specifications=specs,
                namespaces=nss,
            )
        )

    return Registry(families), errors


def spec_path(out_dir: Path, family_key: str, spec_key: str) -> Path:
    return out_dir / family_key / f"{spec_key}.md"


def namespace_path(out_dir: Path, ns_key: str) -> Path:
    return out_dir / "_namespaces" / f"{ns_key}.ttl"


def build_spec(
    family: Family, spec: SpecEntry, out_dir: Path, cache_dir: Path, refresh: bool, fetched: str
) -> tuple[bool, list[str]]:
    """Fetch, convert, validate, and write one spec. Returns (ok, messages)."""
    messages: list[str] = []
    try:
        result = fetch_html(spec.uri, cache_dir=cache_dir, refresh=refresh)
    except Exception as e:  # noqa: BLE001 — report and continue with other specs
        return False, [f"fetch failed: {e}"]

    def include_fetcher(url: str) -> str:
        return fetch_html(url, cache_dir=cache_dir, refresh=refresh).html

    converted = convert_spec(
        result.html, spec.uri, final_url=result.final_url, include_fetcher=include_fetcher
    )
    document = assemble_document(
        converted,
        source_url=spec.uri,
        fetched=fetched,
        family=family.key,
        label=spec.label,
        version=spec.version,
        description=spec.comment,
    )

    validation = validate_markdown(document, key=spec.key)
    for warning in converted.warnings:
        validation.warn(f"{spec.key}: {warning}")
    messages.extend(validation.errors + validation.warnings)

    if not validation.ok:
        return False, messages

    target = spec_path(out_dir, family.key, spec.key)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(document)
    return True, messages


def build_namespace(
    ns: NamespaceEntry, out_dir: Path, fetched: str
) -> tuple[bool, list[str]]:
    """Fetch, serialize, and write one namespace snapshot."""
    try:
        graph = fetch_namespace_graph(ns.uri)
    except Exception as e:  # noqa: BLE001
        return False, [f"{ns.key}: namespace fetch/parse failed: {e}"]

    resources = extract_resources(graph, ns.uri)
    if not resources:
        return False, [f"{ns.key}: no resources found in namespace"]

    turtle = serialize_namespace(graph, ns.uri, comment=ns.comment)
    turtle += f"# fetched: {fetched}, resources: {len(resources)}\n"

    target = namespace_path(out_dir, ns.key)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(turtle)
    return True, [f"{ns.key}: {len(graph)} triples, {len(resources)} resources"]


def write_index(registry: Registry, out_dir: Path, fetched: str) -> None:
    """Write the references/index.md catalog."""
    lines = [
        "<!-- AUTO-GENERATED by ld-skills build — do not edit by hand -->",
        "",
        "# Specification catalog",
        "",
        f"Snapshots built {fetched}. Each entry is a single markdown file:",
        "open it and search (case-insensitive) for the term you need.",
        "",
    ]

    for family in registry.families:
        if not family.specifications and not family.namespaces:
            continue
        lines.append(f"## {family.label or family.key}")
        lines.append("")
        if family.comment:
            lines.append(f"*{family.comment}*")
            lines.append("")
        for spec in family.specifications:
            comment = f" — {spec.comment}" if spec.comment else ""
            lines.append(f"- [{spec.label}]({family.key}/{spec.key}.md){comment}")
        if family.namespaces:
            for ns in family.namespaces:
                comment = f" — {ns.comment}" if ns.comment else ""
                lines.append(f"- [{ns.label} vocabulary](_namespaces/{ns.key}.ttl){comment}")
        lines.append("")

    lines += [
        "---",
        "",
        "## Namespace snapshots",
        "",
        "Turtle files in `_namespaces/` hold the term definitions (classes and",
        "properties) of the core vocabularies, ready to read or load into rdflib.",
        "",
    ]

    (out_dir / "index.md").write_text("\n".join(lines))


def prune_orphans(out_dir: Path, registry: Registry) -> list[str]:
    """Remove files in out_dir that no longer correspond to a registry entry."""
    keep: set[Path] = {out_dir / "index.md"}
    for family, spec in registry.specs:
        keep.add(spec_path(out_dir, family.key, spec.key))
    for _, ns in registry.namespaces:
        keep.add(namespace_path(out_dir, ns.key))

    removed: list[str] = []
    if not out_dir.exists():
        return removed
    for path in sorted(out_dir.rglob("*")):
        if path.is_file() and path not in keep:
            removed.append(str(path.relative_to(out_dir)))
            path.unlink()
    # Clean up directories left empty.
    for path in sorted(out_dir.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()
    return removed


def run_build(args: argparse.Namespace) -> int:
    registry_path = Path(args.registry)
    registry, errors = load_registry(registry_path)
    if errors:
        for error in errors:
            print(f"registry error: {error}", file=sys.stderr)
        return 2

    out_dir = Path(args.out)
    cache_dir = Path(args.cache)
    fetched = dt.date.today().isoformat()

    only = set(args.only or [])
    report = BuildReport()

    for family, spec in registry.specs:
        if only and spec.key not in only:
            continue
        ok, messages = build_spec(family, spec, out_dir, cache_dir, args.refresh, fetched)
        status = "ok " if ok else "FAIL"
        size = ""
        target = spec_path(out_dir, family.key, spec.key)
        if target.exists():
            size = f" ({target.stat().st_size // 1024} kB)"
        print(f"[{status}] {spec.key}{size}")
        for message in messages:
            print(f"       {message}")
        (report.ok if ok else report.failed).append(spec.key)
        report.warnings.extend(m for m in messages if "FAIL" not in m)

    if not args.no_namespaces:
        for _, ns in registry.namespaces:
            if only and ns.key not in only:
                continue
            ok, messages = build_namespace(ns, out_dir, fetched)
            print(f"[{'ok ' if ok else 'FAIL'}] ns:{ns.key}")
            for message in messages:
                print(f"       {message}")
            (report.ok if ok else report.failed).append(f"ns:{ns.key}")

    if not only:
        write_index(registry, out_dir, fetched)
        for removed in prune_orphans(out_dir, registry):
            print(f"[pruned] {removed}")

    print(
        f"\n{len(report.ok)} succeeded, {len(report.failed)} failed"
        + (f": {', '.join(report.failed)}" if report.failed else "")
    )
    return 0 if report.success else 1


def run_check(args: argparse.Namespace) -> int:
    registry, errors = load_registry(Path(args.registry))
    for error in errors:
        print(f"registry error: {error}", file=sys.stderr)
    n_specs = len(registry.specs)
    n_ns = len(registry.namespaces)
    print(f"registry ok: {len(registry.families)} families, {n_specs} specs, {n_ns} namespaces")
    return 1 if errors else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ld-skills", description=__doc__)
    sub = parser.add_subparsers(dest="command")

    p_build = sub.add_parser("build", help="build the skill references tree")
    p_build.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    p_build.add_argument("--out", default=str(DEFAULT_OUT))
    p_build.add_argument("--cache", default=".cache")
    p_build.add_argument("--refresh", action="store_true", help="bypass the fetch cache")
    p_build.add_argument("--only", nargs="*", help="build only these spec/namespace keys")
    p_build.add_argument("--no-namespaces", action="store_true")
    p_build.set_defaults(func=run_build)

    p_check = sub.add_parser("check", help="validate the registry")
    p_check.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    p_check.set_defaults(func=run_check)

    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 2
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
