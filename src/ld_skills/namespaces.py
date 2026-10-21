"""RDF namespace snapshots: fetch a namespace and emit a stable Turtle file.

Ported from ld-mcp's parsers/namespace.py, switched to synchronous use.
"""

import urllib.request

from rdflib import RDF, Graph

# Standard prefix bindings applied to every snapshot.
PREFIXES = {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "sh": "http://www.w3.org/ns/shacl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "prov": "http://www.w3.org/ns/prov#",
    "time": "http://www.w3.org/2006/time#",
    "dcterms": "http://purl.org/dc/terms/",
}

USER_AGENT = "ld-skills/0.1 (+https://github.com/robsyc/ld-skills)"


def fetch_namespace_graph(uri: str) -> Graph:
    """Fetch and parse namespace RDF with standard prefix bindings.

    rdflib cannot guess the format of raw bytes, so pick it from the
    Content-Type header and fall back to trying the common serializations.
    """
    g = Graph()
    for prefix, ns in PREFIXES.items():
        g.bind(prefix, ns)

    req = urllib.request.Request(
        uri,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/turtle, application/rdf+xml, application/ld+json, */*",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        data = response.read()
        ctype = response.headers.get("Content-Type", "").lower()

    fmt = None
    if "turtle" in ctype:
        fmt = "turtle"
    elif "rdf+xml" in ctype or "xml" in ctype:
        fmt = "xml"
    elif "ld+json" in ctype or "json" in ctype:
        fmt = "json-ld"
    elif "n3" in ctype or "notation" in ctype:
        fmt = "n3"

    attempts = [fmt] if fmt else [None]
    attempts += [f for f in ("turtle", "xml", "json-ld") if f != fmt]

    last_error: Exception | None = None
    for attempt in attempts:
        try:
            g.parse(data=data, format=attempt)
            return g
        except Exception as e:  # noqa: BLE001 — try the next serialization
            last_error = e
    raise ValueError(f"could not parse namespace {uri}: {last_error}")


def _uri_variants(ns_uri: str) -> list[str]:
    variants = [ns_uri]
    if ns_uri.startswith("https://"):
        variants.append(ns_uri.replace("https://", "http://", 1))
    elif ns_uri.startswith("http://"):
        variants.append(ns_uri.replace("http://", "https://", 1))
    return variants


def extract_resources(graph: Graph, ns_uri: str) -> list[dict]:
    """Resources defined in the namespace, sorted by local name."""
    resources = []
    for s in set(graph.subjects()):
        s_str = str(s)
        for uri in _uri_variants(ns_uri):
            if s_str.startswith(uri):
                local = s_str[len(uri):]
                if not local:
                    break
                types = [graph.qname(t) for t in graph.objects(s, RDF.type)]
                resources.append({"name": local, "a": types[0] if types else None})
                break
    return sorted(resources, key=lambda r: r["name"])


def serialize_namespace(graph: Graph, ns_uri: str, comment: str = "") -> str:
    """Serialize the whole namespace graph as Turtle with a provenance header."""
    subgraph = Graph()
    for prefix, ns in PREFIXES.items():
        subgraph.bind(prefix, ns)

    variants = _uri_variants(ns_uri)
    for s, p, o in graph:
        if any(str(s).startswith(uri) or str(p).startswith(uri) for uri in variants):
            subgraph.add((s, p, o))

    turtle = subgraph.serialize(format="turtle")
    header = f"# Namespace snapshot of <{ns_uri}>\n"
    if comment:
        header += f"# {comment}\n"
    return header + turtle
