---
title: "RDF Dataset Canonicalization"
source: https://www.w3.org/TR/rdf-canon/
family: rdf
status: W3C Recommendation
spec_date: 2024-05-21
fetched: 2026-10-21
---

# RDF Dataset Canonicalization

> A standard RDF Dataset Canonicalization Algorithm (URDNA2015, URGNA2012).

## Contents

- Abstract
- 1 Introduction
  - 1.1 Uses of Dataset Canonicalization
  - 1.2 How to Read this Document
  - 1.3 Typographical conventions
- 2 Conformance
- 3 Terminology
  - 3.1 Terms defined by this specification
  - 3.2 Terms defined by cited specifications
- 4 Canonicalization
  - 4.1 Overview
  - 4.2 Canonicalization State
  - 4.3 Blank Node Identifier Issuer State
  - 4.4 Canonicalization Algorithm
    - 4.4.1 Overview
    - 4.4.2 Examples
    - 4.4.3 Algorithm
  - 4.5 Issue Identifier Algorithm
    - 4.5.1 Overview
    - 4.5.2 Algorithm
  - 4.6 Hash First Degree Quads
    - 4.6.1 Overview
    - 4.6.2 Examples
    - 4.6.3 Algorithm
  - 4.7 Hash Related Blank Node
    - 4.7.1 Overview
    - 4.7.2 Examples
    - 4.7.3 Algorithm
  - 4.8 Hash N-Degree Quads
    - 4.8.1 Overview
    - 4.8.2 Examples
    - 4.8.3 Algorithm
- 5 Serialization
- 6 Privacy Considerations
- 7 Security Considerations
  - 7.1 Dataset Poisoning
  - 7.2 Insecure Hash Algorithms
- 8 Use Cases
- 9 Examples
  - 9.1 Duplicate Paths
  - 9.2 Double Circle
  - 9.3 Dataset with Blank Node Named Graph
- A A Canonical form of N-Quads
- B URDNA2015
- C URGNA2012
- D Index
  - D.1 Terms defined by this specification
  - D.2 Terms defined by reference
- E Changes since the First Public Working Draft of 24 November 2022
- F Changes since the Candidate Recommentation Snapshot of 31 October 2023
- H References
  - H.1 Normative references
  - H.2 Informative references

---

## Abstract

RDF [RDF11-CONCEPTS] describes a graph-based data model for making claims
about the world and provides the foundation for reasoning upon that graph
of information. At times, it becomes necessary to compare the differences
between sets of graphs, digitally sign them, or generate short identifiers
for graphs via hashing algorithms. This document outlines an algorithm for
normalizing [RDF datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) such that these operations can be
performed.

## 1. Introduction

*This section is non-normative.*

When data scientists discuss canonicalization,
they do so in the context of achieving a particular set of goals.
Since the same information may sometimes be expressed in a variety of different ways,
it often becomes necessary to transform each of these
different ways into a single, standard representation.
With a standard representation, the differences between
two different sets of data can be easily determined,
a cryptographically-strong hash identifier can be generated for a particular
set of data,
and a particular set of data may be digitally-signed for later
verification.

In particular, this specification is about normalizing [RDF datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset), which are collections of graphs. Since
a directed graph can express the same information in more than one
way, it requires canonicalization to achieve the aforementioned goals
and any others that may arise via serendipity.

Most [RDF datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) can be canonicalized fairly quickly, in terms
of algorithmic time complexity. However, those that contain nodes that do
not have globally unique identifiers pose a greater challenge. Normalizing
these datasets presents the *graph isomorphism* problem, a
problem that is believed to be difficult to solve quickly in the worst
case. Fortunately, existing real world data is rarely, if ever, modeled in
a way that manifests as the worst case and new data can be modeled to avoid
it. In fact, software systems that detect a problematic dataset
(see 7.1 Dataset Poisoning (§7.1)) can choose
to assume it's an attempted denial of service attack, rather than a
real input, and abort.

This document outlines an algorithm for generating a canonical
serialization of an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) given an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) as input.
The algorithm is called the **RDF Canonicalization algorithm version 1.0** or RDFC-1.0.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/) [RDF11-CONCEPTS] lacks clarity on the representation of [language-tagged strings](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string),
> where [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) of the form `xx-YY` are treated as being case insensitive. Implementations might represent language tags
> using all lower case in the form `xx-yy`,
> retain the original representation `xx-YY`,
> or use [BCP47] [formatting conventions](https://www.rfc-editor.org/rfc/rfc5646#section-2.1.1),
> leading to different canonical forms, and therefore, different hashed values.
>
> - The Canonicalization algorithm is based on the RDF 1.1 definition,
>   in the sense that the [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) `xx-YY` is case insensitive, which might lead to different canonicalizations if the user is not aware of this problem.
> - User communities ought to agree to use lower case [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag),
>   while being aware that some implementations might normalize language tags,
>   affecting hash values.
> - Future evolution of RDF might regulate this issue, which RDF environments might have to adapt to,
>   and this might lead to an update of RDFC-1.0.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> See B. URDNA2015 (§B) for a comparison with the version of the algorithm published
> in [RDF Dataset Canonicalization](https://www.w3.org/community/reports/credentials/CG-FINAL-rdf-dataset-canonicalization-20221009/) [CCG-RDC-FINAL].

### 1.1 Uses of Dataset Canonicalization

There are different use cases where graph or dataset canonicalization are important:

- Determining if one serialization is isomorphic to another.
- Digital signing of graphs (datasets) independent of serialization or format.
- Comparing two graphs (datasets) to find differences.
- Communicating change sets when remotely updating an [RDF source](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-source).

A canonicalization algorithm is necessary, but not necessarily sufficient, to handle many of these use cases. The use of [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) in RDF graphs and datasets has a long history and creates inevitable complexities. Blank nodes are used for different purposes:

- when a well known identifier for a node is not known, or the author of a document chooses not to unambiguously name that node,
- when a node is used to stitch together parts of a graph and the nodes themselves are not interesting (e.g., [RDF Collections](https://www.w3.org/TR/rdf11-mt/#rdf-collections) in [RDF11-MT]),
- when someone is trying to create an intentionally difficult graph topology.

Furthermore,
RDF semantics dictate that deserializing an RDF document
results in the creation of unique [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node),
unless it can be determined that on each occasion,
the [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) identifies the same resource.
This is due to the fact that [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) are an aspect of a concrete RDF syntax
and are not intended to be persistent or portable.
Within the abstract RDF model,
blank nodes do not have identifiers
(although some
RDF store
implementations may use stable identifiers and may choose to make them portable).
See [Blank Nodes](https://www.w3.org/TR/rdf11-concepts/#section-blank-nodes) in [RDF11-CONCEPTS] for more information.

RDF does have a provision for allowing blank nodes
to be published in an externally identifiable way through the use of [Skolem IRIs](https://www.w3.org/TR/rdf11-concepts/#dfn-skolem-iri),
which allow a given RDF store to replace the use of blank nodes
in a concrete syntax with [IRIs](https://www.w3.org/TR/rdf11-concepts/#dfn-iri),
which then serve to repeatably identify that blank node within that particular RDF store;
however, this is not generally useful for talking about the
same graph in different RDF stores,
or other concrete representations.
In any case, a stable [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) defined for one
RDF store or serialization is arbitrary,
and typically not relatable to the context within which it is used.

This specification defines an algorithm for creating stable [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) repeatably for different serializations
possibly using individualized [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) of the same RDF graph (dataset) by grounding each [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) through the nodes to which it is connected.
As a result, a graph signature can be obtained by hashing a canonical serialization
of the resulting canonicalized dataset,
allowing for the isomorphism and digital signing use cases.
This specification does not define such a graph signature.

As blank node identifiers can be stable even with other changes to a graph (dataset),
in some cases it is possible to compute the difference between two graphs (datasets),
for example if changes are made only to ground triples,
or if new blank nodes are introduced which do not create an automorphic confusion
with other existing blank nodes.
If any information which would change the generated blank node identifier,
a resulting diff might indicate a greater set of changes than actually exists.
Additionally, if the starting dataset is an N-Quads document,
it may be possible to correlate the original blank node identifiers
used within that N-Quads document with those issued in the canonicalized dataset.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Although alternative hash algorithms might be used
> with this specification,
> applications ought to carefully weigh the advantages
> and disadvantages of using an alternative hash function.
> This is the case, in particular, for any representation of the canonical n-quads form or issued identifiers map that does not identify the associated hash algorithm. Any use case
> that requires reproduction of the same output is expected to
> unequivocally express or communicate the internal
> hash algorithm that was used when generating
> the canonical n-quads form.

### 1.2 How to Read this Document

This document is a detailed specification for an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) canonicalization algorithm. The document is primarily intended for the
following audiences:

- Software developers that want to implement an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) canonicalization algorithm.
- Masochists.

To understand the basics in this specification you must be familiar with
basic RDF concepts [RDF11-CONCEPTS]. A working knowledge of [graph theory](https://en.wikipedia.org/wiki/Graph_theory) and [graph isomorphism](https://en.wikipedia.org/wiki/Graph_isomorphism) is also recommended.

### 1.3 Typographical conventions

*This section is non-normative.*

The following typographic conventions are used in this specification:

`markup`

Markup (elements, attributes, properties),
machine processable values (string, characters, media types),
property names,
and file names are in red-orange monospace font.

*variable*

A variable in pseudo-code or in an algorithm description is italicized.

*definition*

A definition of a term, to be used elsewhere in this or other specifications,
is italicized and in bold.

definition reference

A reference to a definition *in this document* is underlined and is also an active link to the definition itself.

`markup definition reference`

References to a definition *in this document*,
when the reference itself is also a markup, is underlined,
in a red-orange monospace font, and is also an active link to the definition itself.

external definition reference

A reference to a definition *in another document* is underlined and italicized, and is also an active link to the definition itself.

` markup external definition reference`

A reference to a definition *in another document*,
when the reference itself is also a markup,
is underlined and italicized in a red-orange monospace font,
and is also an active link to the definition itself.

[hyperlink](https://www.w3.org/TR/rdf-canon/)

A hyperlink is underlined and in blue.

[[reference](https://www.w3.org/TR/rdf-canon/)]

A document reference (normative or informative) is enclosed in square brackets
and links to the references section.

Explanation

An expandable area to find a more detailed, non-normative explanation of a
particular algorithmic step.

**Explanation**

This area would provide more information about the step involved.

Logging

An expandable area to find suggestions for implementations to log
information about processing,
which may be useful in comparing with other implementations,
or with logs provided with each test case.

**Logging**

For example, the following output snippet might
describe the operation of an implementation using the [YAML] format.

```
ca:
  ca2:
    bn_to_quads:
      e0:
        - _:e0 <http://example.com/#p1> _:e1 .
      e1:
        ...
  ca3:
  - identifier: e0
    h1dq:
      nquads:
        - _:a <http://example.com/#p1> _:z .
```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Notes are in light green boxes with a green left border and with a "Note" header in green.
> Notes are always informative.
> **Example:**
>
> Example 1
>
>
>
> ```
> Examples are in light khaki boxes, with khaki left border,
> and with a numbered "Example" header in khaki.
> Examples are always informative. The content of the example is in monospace font and may be
> syntax colored.
>
> Examples may have tabbed navigation buttons
> to show the results of transforming an example into other representations.
>
> Code examples are generally given in a Turtle or TriG format for brevity,
> where each line represents a single triple or quad.
> Additionally, have the following implied directives:
>
> BASE <http://example.com/>
> PREFIX : <#>
>
> Following the Turtle/TriG syntax rules, blank nodes always appear in the
> `_:xyz` format.
> ```

## 2. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MUST*, *MUST NOT*, and *SHOULD* in this document
are to be interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all capitals, as shown here.

A conforming processor is a system which can generate
the canonical n-quads form of an input dataset consistent with the algorithms defined in this specification.

The algorithms in this specification are normative,
because to consistently reproduce the same canonical identifiers,
implementations *MUST* strictly conform to the steps outlined in these algorithms.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Implementers can partially check their level of conformance with
> this specification by successfully passing the test cases of the [RDF Dataset Canonicalization test suite](https://w3c.github.io/rdf-canon/tests/).
> Note, however, that passing all the tests in the test
> suite does not imply complete conformance to this specification. It only implies
> that the implementation conforms to the aspects tested by the test suite.

## 3. Terminology

### 3.1 Terms defined by this specification

*canonical n-quads form*

The canonicalized representation of a quad is defined in A. A Canonical form of N-Quads (§A).
A quad in canonical n-quads form represents a [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name), if present, in the same manner as
a [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject), and each quad is terminated with a single `LF` (line feed, code point `U+000A`).

*canonicalization function*

A canonicalization function maps [RDF datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) into [isomorphic datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-dataset-isomorphism) [RDF11-CONCEPTS].
Two datasets produce the same canonical result if and only if they are [isomorphic](https://www.w3.org/TR/rdf11-concepts/#dfn-dataset-isomorphism).
The RDFC-1.0 algorithm implements a canonicalization function.
Some datasets may be constructed to prevent this algorithm from
terminating in a reasonable amount of time (see 7.1 Dataset Poisoning (§7.1)),
in which case the algorithm can be considered to be
a *partial canonicalization function*.

*canonicalized dataset*

A canonicalized dataset is the combination of the following:

- an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) —
  the input dataset,
- the input blank node identifier map —
  mapping [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) in the input dataset to [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), and
- the issued identifiers map from the canonical issuer —
  mapping identifiers in the input dataset to canonical identifiers

A concrete serialization of a canonicalized dataset *MUST* label
all [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) using the canonical [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).

*gossip path*

A particular enumeration of every incident mention emanating
from a blank node. This recursively includes transitively related mentions until any named node or blank node already labeled by
a particular identifier issuer is reached. Gossip paths are
encoded and operated on in the RDFC-1.0 algorithm as strings. (See 4.8 Hash N-Degree Quads (§4.8) for more information
on the construction of gossip paths.)

*hash*

The lowercase, hexadecimal representation of a message digest.

*hash algorithm*

The default hash algorithm used by RDFC-1.0, namely, SHA-256 [FIPS-180-4].

Implementations *MUST* support a parameter to define the hash algorithm, *MUST* support SHA-256 and SHA-384 [FIPS-180-4],
and *SHOULD* support the ability to specify other hash algorithms.
Using a different hash algorithm will generally result in different output than
using the default.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> There is no expectation that the default hash algorithm
> will also be used by any application creating a hash digest of the
> canonical N-Quads result.

*identifier issuer*

An identifier issuer is used to issue new [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier). It
maintains a §4.3 Blank Node Identifier Issuer State.

*input blank node identifier map*

Records any blank node identifiers already assigned to the input dataset.
If the input dataset is provided as an N-Quads document,
the [map](https://infra.spec.whatwg.org/#ordered-map) relates blank nodes in the abstract input dataset to the blank node identifiers used within the N-Quads document,
otherwise, identifiers are assigned arbitrarily for
each blank node in the input dataset not previously identified.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> Implementations or environments might deal with blank
> node identifiers more directly; for example, some implementations might
> retain blank node identifiers in the parsed or abstract dataset. Implementations
> are expected to reuse these to enable usable mappings between input blank node
> identifiers and output blank node identifiers outside of the algorithm.

*input dataset*

The abstract [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) that is provided as input to
the algorithm.

*mention*

A node is mentioned in a quad if it is a component of that quad,
as a [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject), [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate), [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object), or [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name).

*mention set*

The set of all quads in a [dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) that mention a node *n* is called the mention set of *n*,
denoted *Qn*.

*quad*

A tuple composed of [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject), [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate), [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object), and [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name).
This is a generalization of an [RDF triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) along with a [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name).

### 3.2 Terms defined by cited specifications

*[blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)*

A [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) as specified by [RDF11-CONCEPTS]. In short, it is a node in a graph that is
neither an [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri), nor a [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal).

*[blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier)*

A [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) as specified by [RDF11-CONCEPTS]. In short, it is a [string](https://infra.spec.whatwg.org/#string) that begins
with `_:` that is used as an identifier for a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node). [Blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) are typically implementation-specific local identifiers; this document
specifies an algorithm for deterministically specifying them.

Concrete syntaxes, like [Turtle] or [N-Quads], prepend blank node identifiers with the `_:` string
to differentiate them from other nodes in the graph. This affects the
canonicalization algorithm, which is based on calculating a hash over the representations of quads in this format.

*[default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph)*

The [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) as specified by [RDF11-CONCEPTS].

*[graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name)*

A [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name) as specified by [RDF11-CONCEPTS].

*[IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri)*

An [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) (Internationalized Resource Identifier) is a string that conforms to the syntax
defined in [RFC3987].

*[object](https://www.w3.org/TR/rdf11-concepts/#dfn-object)*

An [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) as specified by [RDF11-CONCEPTS].

*[predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate)*

A [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate) as specified by [RDF11-CONCEPTS].

*[RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset)*

A [dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) as specified by [RDF11-CONCEPTS].
For the purposes of this specification, an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) is considered to be a set of quads

*[RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph)*

An [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) as specified by [RDF11-CONCEPTS].

*[RDF triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple)*

A [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) as specified by [RDF11-CONCEPTS].

*[string](https://infra.spec.whatwg.org/#string)*

A string is a sequence of zero or more Unicode characters.

*[subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject)*

A [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) as specified by [RDF11-CONCEPTS].

`true` and `false`

Values that are used to express one of two possible [boolean](https://infra.spec.whatwg.org/#boolean) states.

*[Unicode code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation)*

This refers to determining the order of two Unicode strings (`A` and `B`),
using [Unicode Codepoint Collation](https://www.w3.org/TR/xpath-functions/#codepoint-collation),
as defined in [XPATH-FUNCTIONS],
which defines a [total ordering](https://en.wikipedia.org/wiki/Total_order) of [strings](https://infra.spec.whatwg.org/#string) comparing code points.
Note that for UTF-8 encoded strings, comparing the byte sequences gives the same result as [code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation).

## 4. Canonicalization

Canonicalization is the process of transforming an input dataset to its serialized canonical form.
That is, any two input datasets that contain the same information,
regardless of their arrangement,
will be transformed into the same serialized canonical form.
The problem requires directed
graphs to be deterministically ordered into sets of nodes and edges. This
is easy to do when all of the nodes have globally-unique identifiers, but
can be difficult to do when some of the nodes do not. Any nodes without
globally-unique identifiers must be issued deterministic identifiers.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This specification defines a canonicalized dataset to include stable identifiers for blank nodes,
> practical uses of which will always generate a canonical serialization of such a dataset.

In time, there may be more than one canonicalization algorithm and,
therefore, for identification purposes, this algorithm is named the
"RDF Canonicalization algorithm version 1.0"
(*RDFC-1.0*).

Figure 1 provides an overview of RDFC-1.0,
with steps 1 through 7 corresponding to the various steps described in 4.4.3 Algorithm (§4.4.3).

*Figure 1 An illustrated overview of the RDFC-1.0 algorithm.
Image available in [SVG](https://www.w3.org/TR/rdf-canon/ca-overview.svg "SVG image of overview") .*

### 4.1 Overview

*This section is non-normative.*

To determine a canonical labeling, RDFC-1.0 considers the
information connected to each blank node.
Nodes with unique first degree information can immediately be issued a canonical identifier
via the §4.5 Issue Identifier Algorithm.
When a node has non-unique first degree information,
it is necessary to determine all information that is transitively connected
to it throughout the entire dataset. 4.6 Hash First Degree Quads (§4.6) defines a
node’s first degree information via its first degree hash.

Hashes are computed from the information of each blank node.
These hashes encode the mentions incident to each blank node.
The hash of a string *s*, is the lower-case,
hexadecimal representation of the result of passing *s* through a cryptographic hash function.
By default, RDFC-1.0 uses the SHA-256 hash algorithm [FIPS-180-4].
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The "degree" terminology is used within this specification
> as colloquial way of describing
> the [eccentricity](https://en.wikipedia.org/wiki/Distance_(graph_theory)#Related_concepts) or [radius](https://en.wikipedia.org/wiki/Distance_(graph_theory)#Related_concepts) of any two nodes within a dataset.
> This concept is also related to "degrees of separation",
> as in, for example, "[six degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation)".
> Nodes with unique first degree information can be considered nodes with a radius of one.

### 4.2 Canonicalization State

When performing the steps required by the canonicalization algorithm,
it is helpful to track state in a data structure called the *canonicalization state*. The information contained in the canonicalization state is described below.

*blank node to quads map*

A [map](https://infra.spec.whatwg.org/#ordered-map) that relates a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to
the quads in which they appear in the input dataset.

*hash to blank nodes map*

A [map](https://infra.spec.whatwg.org/#ordered-map) that relates a hash to a [list](https://infra.spec.whatwg.org/#list) of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).

*canonical issuer*

An identifier issuer, initialized with the
prefix `c14n` (short for canonicalization), for issuing canonical [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).

> **Note:**
>
> > **Note:**
> >
> > Note
>
> Mapping all [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) to use this
> identifier spec means that an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) composed of two
> different [RDF graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) will issue different
> identifiers than that for the graphs taken independently. This may
> happen anyway, due to [automorphisms](https://en.wikipedia.org/wiki/Automorphism),
> or overlapping statements, but an identifier based on the resulting hash along with an issue sequence number specific to that hash would
> stand a better chance of surviving such minor changes, and allow the
> resulting information to be useful for [RDF Diff](https://www.w3.org/2001/sw/wiki/How_to_diff_RDF).

### 4.3 Blank Node Identifier Issuer State

The canonicalization algorithm issues identifiers to [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node).
The §4.5 Issue Identifier Algorithm uses an identifier issuer to accomplish this task.
The information an identifier issuer needs to keep track of is described
below.

*identifier prefix*

The identifier prefix is a string that is used at the beginning of an [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier). It should be initialized to a
string that is specified by the canonicalization algorithm. When
generating a new [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), the prefix
is concatenated with a identifier counter. For example, `c14n` is a proper initial value for the identifier prefix that would produce [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) like `c14n1`.

*identifier counter*

A counter that is appended to the identifier prefix to
create an [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier). It is initialized to `0`.

*issued identifiers map*

An [ordered map](https://infra.spec.whatwg.org/#ordered-map) that relates [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to issued identifiers,
to prevent issuance of more than one new identifier per existing identifier,
and to allow [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) to
be assigned identifiers some time after issuance.

### 4.4 Canonicalization Algorithm

The canonicalization algorithm converts an input dataset into a canonicalized dataset or raises an error if
the input dataset is determined to be overly complex.
This algorithm will assign
deterministic identifiers to any [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) in the input dataset.

#### 4.4.1 Overview

*This section is non-normative.*

RDFC-1.0 canonically labels an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) by assigning each [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) a canonical identifier.
In RDFC-1.0, an RDF dataset *D* is represented as a set of quads of the form `< s, p, o, g >` where the graph component `g` is empty if and only if the [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) `< s, p, o >` is in the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph).
It is expected that, for two RDF datasets, RDFC-1.0 returns the same canonically labeled list of quads
if and only if the two datasets are isomorphic (i.e., the same modulo blank node identifiers).

RDFC-1.0 consists of several sub-algorithms.
These sub-algorithms are introduced in the following sub-sections.
First, we give a high level summary of RDFC-1.0.

1. **Initialization**.
   Initialize the state needed for the rest of the algorithm
   using 4.2 Canonicalization State (§4.2).
   Also initialize the canonicalized dataset using the input dataset (which remains immutable)
   the input blank node identifier map (retaining blank node identifiers from the input if possible, otherwise assigning them arbitrarily);
   the issued identifiers map from the canonical issuer is added upon completion of the algorithm.
2. **Compute first degree hashes**.
   Compute the first degree hash for each blank node in the dataset using 4.6 Hash First Degree Quads (§4.6).
3. **Canonically label unique nodes**.
   Assign canonical identifiers via 4.5 Issue Identifier Algorithm (§4.5),
   in [Unicode code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation), to each blank node whose first degree hash is unique.
4. **Compute N-degree hashes for non-unique nodes**.
   For each repeated first degree hash (proceeding in [Unicode code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation)),
   compute the N-degree hash via 4.8 Hash N-Degree Quads (§4.8) of every unlabeled blank node that corresponds to the given repeated hash.
5. **Canonically label remaining nodes**.
   In [Unicode code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation) of the N-degree hashes,
   issue canonical identifiers to each corresponding blank node using 4.5 Issue Identifier Algorithm (§4.5).
   If more than one node produces the same N-degree hash,
   the order in which these nodes receive a canonical identifier does not matter.
6. **Finish**.
   Return the serialized canonical form of the canonicalized dataset.
   Alternatively, return the canonicalized dataset containing
   the input blank node identifier map and issued identifiers map.

#### 4.4.2 Examples

*This section is non-normative.*
> **Example:**
>
> Example 2: Unique hashes
>
> This example illustrates the Canonicalization Algorithm (§4.4.3) where all blank nodes have unique first-degree hashes.
>
> *Figure 2 An illustration of a graph resulting in unique hashes.
> Image available in [SVG](https://www.w3.org/TR/rdf-canon/unique-hashes.svg "SVG image of unique hashes") .*
>
> ```
> :p :q _:e0 .
> :p :r _:e1 .
> _:e0 :s :u .
> _:e1 :t :u .
> ```
>
> Step 2 is called twice, with each blank node (`e0` and `e1`)
> in the input dataset to populate blank node to quads map:
>
> *Table 1 Blank node to quads map for unique hashes*
>
> | *blank node* | *Q*                       |
> | ------------ | ------------------------- |
> | `e0`         | `:p :q e0 .` `e0 :s :u .` |
> | `e1`         | `:p :r e1 .` `e1 :t :u .` |
> Step 3 generates the first-degree
> hash for each blank node, which is explored further
> in Example 4:
>
> *Table 2 Hash to blank nodes map for unique hashes*
>
> | *hash*                                                             | *blank node(s)* |
> | ------------------------------------------------------------------ | --------------- |
> | `21d1dd5ba21f3dee9d76c0c00c260fa6f5d5d65315099e553026f4828d0dc77a` | `e0`            |
> | `6fa0b9bdb376852b5743ff39ca4cbf7ea14d34966b2828478fbf222e7c764473` | `e1`            |
> Step 4 creates canonical identifiers for each
> blank node which has a unique hash:
>
> *Table 3 Canonical identifiers for blank nodes with unique hashes*
>
> | *blank node* | *canonical identifier* |
> | ------------ | ---------------------- |
> | `e0`         | `c14n0`                |
> | `e1`         | `c14n1`                |
> Step 5 has no effect,
> as there are no remaining blank nodes without canonical identifiers.
>
> Step 6 generates
> the canonicalized dataset by mapping blank node identifiers in the input dataset
> with canonical identifiers:
>
> ```
> :p :q _:c14n0 .
> :p :r _:c14n1 .
> _:c14n0 :s :u .
> _:c14n1 :t :u .
> ```
> **Example:**
>
> Example 3: Shared hashes
>
> This example illustrates the Canonicalization Algorithm (§4.4.3) where hashing the statements mentioning those blank nodes have overlapping results.
>
> *Figure 3 An illustration of a graph resulting in shared hashes.
> Image available in [SVG](https://www.w3.org/TR/rdf-canon/shared-hashes.svg "SVG image of shared hashes") .*
>
> ```
> :p :q _:e0 .
> :p :q _:e1 .
> _:e0 :p _:e2 .
> _:e1 :p _:e3 .
> _:e2 :r _:e3 .
> ```
>
> Step 2 is called four times, with each blank node
> (`e0`, `e1`, `e2`, and `e3`)
> to populate blank node to quads map:
>
> *Table 4 Blank node to quads map for shared hashes*
>
> | *blank node* | *Q*                       |
> | ------------ | ------------------------- |
> | `e0`         | `:p :q e0 .` `e0 :p e2 .` |
> | `e1`         | `:p :q e1 .` `e1 :p e3 .` |
> | `e2`         | `e0 :p e2 .` `e2 :r e3 .` |
> | `e3`         | `e1 :p e3 .` `e2 :r e3 .` |
> Step 3 generates the first-degree
> hash for each blank node, which is explored further
> in Example 5 (note that the hashes for `e0` and `e1` are shared):
>
> *Table 5 Hash to blank nodes map shared hashes*
>
> | *hash*                                                             | *blank node(s)* |
> | ------------------------------------------------------------------ | --------------- |
> | `3b26142829b8887d011d779079a243bd61ab53c3990d550320a17b59ade6ba36` | `e0`, `e1`      |
> | `15973d39de079913dac841ac4fa8c4781c0febfba5e83e5c6e250869587f8659` | `e2`            |
> | `7e790a99273eed1dc57e43205d37ce232252c85b26ca4a6ff74ff3b5aea7bccd` | `e3`            |
> Step 4 creates canonical identifiers for each
> blank node which has a unique hash:
>
> *Table 6 Canonical identifiers for blank nodes with shared hashes*
>
> | *blank node* | *canonical identifier* |
> | ------------ | ---------------------- |
> | `e2`         | `c14n0`                |
> | `e3`         | `c14n1`                |
> Step 5 is run on `e0` and `e1`, separately,
> which share the same hash,
> and use separate instances of a *temporary issuer*,
> (as explored in Example 7)
> to create the *hash path list* composed of the hash result
> and temporary identifier mappings from Hash N-Degree Quads algorithm (§4.8) for each of these blank nodes:
>
> *Table 7 Result for `e0`*
>
> | *temporary issuer* mappings | *original identifier* *temporary identifier* `e0` `b0`             |
> | --------------------------- | ------------------------------------------------------------------ |
> | *hash*                      | `fbc300de5afafd97a4b9ee1e72b57754dcdcb7ebb724789ac6a94a5b82a48d30` |
>
> *Table 8 Result for `e1`*
>
> | *temporary issuer* mappings | *original identifier* *temporary identifier* `e1` `b0`             |
> | --------------------------- | ------------------------------------------------------------------ |
> | *hash*                      | `2c0b377baf86f6c18fed4b0df6741290066e73c932861749b172d1e5560f5045` |
> Step 5.3 creates
> the canonical identifiers for the temporary identifiers
> established in the previous step
> running in order of the *hash* component from each result.
> This updates the canonical issuer with the following
> mappings:
>
> *Table 9 Blank node to canonical identifiers*
>
> | *blank node* | *canonical identifier* |
> | ------------ | ---------------------- |
> | `e0`         | `c14n3`                |
> | `e1`         | `c14n2`                |
> | `e2`         | `c14n0`                |
> | `e3`         | `c14n1`                |
> Step 6 updates
> the canonicalized dataset with the canonical issuer,
> containing an issued identifiers map mapping blank node identifiers from the input dataset
> to their canonical identifiers:
>
> ```
> :p :q _:c14n2 .
> :p :q _:c14n3 .
> _:c14n0 :r _:c14n1 .
> _:c14n2 :p _:c14n1 .
> _:c14n3 :p _:c14n0 .
> ```

#### 4.4.3 Algorithm

The following algorithm will run with a minimal number of iterations in each step
for typical input datasets.
In some extreme cases, the algorithm can behave poorly, particularly in Step 5.
Implementations *MUST* defend against potential denial-of-service attacks
by raising suitable exceptions and terminating early.
See 7.1 Dataset Poisoning (§7.1) for further information.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Implementations can consider placing limits on the number of
> calls to 4.8 Hash N-Degree Quads (§4.8) based on the number
> of blank nodes in the hash to blank nodes map.
> For most typical datasets, more than a couple
> of iterations on 4.8 Hash N-Degree Quads (§4.8) per blank node would be unusual.

1. Create the canonicalization state.
   If the input dataset is an N-Quads document,
   parse that document into a dataset in the canonicalized dataset,
   retaining any blank node identifiers used within that document
   in the input blank node identifier map;
   otherwise arbitrary identifiers are assigned for each
   blank node.

   **Explanation**

   This has the effect of initializing the blank node to quads map,
   and the hash to blank nodes map,
   as well as instantiating a new canonical issuer.

   After this algorithm completes,
   the input blank node identifier map state
   and canonical issuer may be used to
   correlate blank nodes used in the input dataset with both their original identifiers,
   and associated canonical identifiers.

2. For every quad *Q* in input dataset:
   1. For each [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) that is a component of *Q*,
      add a reference to *Q* from the [map entry](https://infra.spec.whatwg.org/#map-entry) for the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) *identifier* in the blank node to quads map,
      creating a new entry if necessary,
      using the identifier for the blank node found in the input blank node identifier map.

      **Explanation**

      This establishes the blank node to quads map,
      relating each [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) with the set of quads of which it is a component,
      via the map for each blank node in the input dataset to its assigned identifier.
      > **Note:**
      >
      > > **Note:**
      > >
      > > Note
      >
      > [Literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) components of quads are not subject to any normalization.
      > As noted in [Section 3.3](https://www.w3.org/TR/rdf11-concepts/#section-Graph-Literal) of [RDF11-CONCEPTS], [literal term equality](https://www.w3.org/TR/rdf11-concepts/#dfn-literal-term-equality) is based on the [lexical form](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-form),
      > rather than the [literal value](https://www.w3.org/TR/rdf11-concepts/#dfn-literal-value),
      > so two literals `"01"^^xsd:integer` and `"1"^^xsd:integer` are treated as distinct resources.

   **Logging**

   Log the state of the blank node to quads map:

   ```
   # Blank node to quads map for unique hashes example
   ca:
     log point: Entering the canonicalization function (4.4.3).
     ca.2:
       log point: Extract quads for each bnode (4.4.3 (2)).
       Bnode to quads:
         e0:
           - <http://example.com/#p> <http://example.com/#q> _:e0 .
           - _:e0 <http://example.com/#s> <http://example.com/#u> .
         e1:
           - <http://example.com/#p> <http://example.com/#r> _:e1 .
           - _:e1 <http://example.com/#t> <http://example.com/#u> .
     ...
   ```

3. For each [key](https://infra.spec.whatwg.org/#map-key) *n* in the blank node to quads map:

   **Explanation**

   This step creates a hash for every blank node in the input document.
   Some blank nodes will lead to a unique hash,
   while other blank nodes may share a common hash.

   1. Create a hash, *hf(n)*,
      for *n* according to the Hash First Degree Quads algorithm (§4.6).
   2. Append *n* to the value associated to *hf(n)* in hash to blank nodes map,
      creating a new entry if necessary.

   **Logging**

   Log the results from the Hash First Degree Quads algorithm (§4.6.3).

   ```
   # First degree hashes for unique hashes example
   ca:
     ...
     ca.3:
       log point: Calculated first degree hashes (4.4.3 (3)).
       with:
         - identifier: e0
           h1dq:
             log point: Hash First Degree Quads function (4.6.3).
             nquads:
               - <http://example.com/#p> <http://example.com/#q> _:a .
               - _:a <http://example.com/#s> <http://example.com/#u> .
             hash: 21d1dd5ba21f3dee9d76c0c00c260fa6f5d5d65315099e553026f4828d0dc77a
         - identifier: e1
           h1dq:
             log point: Hash First Degree Quads function (4.6.3).
             nquads:
               - <http://example.com/#p> <http://example.com/#r> _:a .
               - _:a <http://example.com/#t> <http://example.com/#u> .
             hash: 6fa0b9bdb376852b5743ff39ca4cbf7ea14d34966b2828478fbf222e7c764473
     ...
   ```

4. For each *hash* to *identifier list* [map entry](https://infra.spec.whatwg.org/#map-entry) in hash to blank nodes map, [code point ordered](https://www.w3.org/TR/xpath-functions/#codepoint-collation) by *hash*:

   **Explanation**

   This step establishes the canonical identifier for blank nodes having
   a unique hash, which are recorded in the canonical issuer.

   1. If *identifier list* has more than one entry,
      continue to the next mapping.
   2. Use the §4.5 Issue Identifier Algorithm,
      passing canonical issuer and the
      single [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), *identifier* in *identifier list* to issue a
      canonical replacement identifier for *identifier*.
   3. Remove the [map entry](https://infra.spec.whatwg.org/#map-entry) for *hash* from the hash to blank nodes map.

   **Logging**

   Log the assigned canonical identifiers.

   ```
   # Assigned canonical identifiers for shared hashes example
   ca:
     ...
     ca.4:
       log point: Create canonical replacements for hashes mapping to a single node (4.4.3 (4)).
       with:
         - identifier: e2
           hash: 15973d39de079913dac841ac4fa8c4781c0febfba5e83e5c6e250869587f8659
           canonical label: c14n0
         - identifier: e3
           hash: 7e790a99273eed1dc57e43205d37ce232252c85b26ca4a6ff74ff3b5aea7bccd
           canonical label: c14n1
     ...
   ```

5. For each *hash* to *identifier list* [map entry](https://infra.spec.whatwg.org/#map-entry) in hash to blank nodes map, [code point ordered](https://www.w3.org/TR/xpath-functions/#codepoint-collation) by *hash*:

   **Explanation**

   This step establishes the canonical identifier for blank nodes having
   a shared hash.
   This is done by creating unique blank node identifiers for all
   blank nodes traversed by the Hash N-Degree Quads algorithm (§4.8),
   running through each blank node without a canonical identifier in the order
   of the hashes established in the previous step.

   **Logging**

   Log *hash* and *identifier list* for this iteration.

   ```
   # Hash and Identifier List for each iteration of step 5 using shared hashes example
   ca:
     ...
     ca.5:
       log point: Calculate hashes for identifiers with shared hashes (4.4.3 (5)).
       with:
         - hash: 3b26142829b8887d011d779079a243bd61ab53c3990d550320a17b59ade6ba36
           identifier list: [ "e0", "e1"]
       ...
     ...
   ```

   1. Create *hash path list* where each item will be a result
      of running the Hash N-Degree Quads algorithm (§4.8).

      **Explanation**

      This list will be populated in step 5.2, and will establish an order for those blank nodes
      sharing a common first-degree hash.

   2. For each [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) *n* in *identifier list*:
      1. If a canonical identifier has already been issued for *n*, continue to the next [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
      2. Create *temporary issuer*, an identifier issuer initialized with the prefix `b`.
      3. Use the §4.5 Issue Identifier Algorithm,
         passing *temporary issuer* and *n*, to
         issue a new temporary [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) *bn* to *n*.
      4. Run the Hash N-Degree Quads algorithm (§4.8),
         passing the canonicalization state, *n* for *identifier*, and *temporary issuer*,
         appending the
         result to the *hash path list*.

         **Logging**

         Include logs for each call to Hash N-Degree Quads algorithm (§4.8).

         ```
         # Logs from calls to Hash N-Degree Quads algorithm for shared hashes example
         ca:
           ...
           ca.5:
             log point: Calculate hashes for identifiers with shared hashes (4.4.3 (5)).
             with:
               - hash: 3b26142829b8887d011d779079a243bd61ab53c3990d550320a17b59ade6ba36
                 identifier list: [ "e0", "e1"]
                 ca.5.2:
                   log point: Calculate hashes for identifiers with shared hashes (4.4.3 (5.2)).
                   with:
                     - identifier: e0
                       hndq:
                         log point: Hash N-Degree Quads function (4.8.3).
                         identifier: e0
                         issuer: {e0: b0}
                         ...
                     ...
                 ...
           ...
         ```

   3. For each *result* in the *hash path list*, [code point ordered](https://www.w3.org/TR/xpath-functions/#codepoint-collation) by the *hash* in *result*:

      **Explanation**

      The previous step created temporary identifiers for the
      blank nodes sharing a common first degree hash,
      which is now used to generate their canonical identifiers.

      1. For each [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), *existing identifier*, that was issued a temporary
         identifier by *identifier issuer* in *result*,
         issue a canonical identifier,
         in the same order,
         using the §4.5 Issue Identifier Algorithm,
         passing canonical issuer and *existing identifier*.

         **Explanation**

         In Step 5.2, *hash path list* was created with an ordered
         set of results.
         Each result contained a *temporary issuer* which recorded temporary identifiers associated with
         a particular [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) in *identifier list*.
         This step processes each returned *temporary issuer*,
         in order, and allocates canonical identifiers
         to the temporary identifier mappings contained
         within each *temporary issuer*,
         creating a full order on the remaining blank nodes
         with unissued canonical identifiers.

      **Logging**

      Log newly issued canonical identifiers.

      ```
      # Newly issued canonical identifiers from step 5.3 for shared hashes example
      ca:
        ...
        ca.5:
          log point: Calculate hashes for identifiers with shared hashes (4.4.3 (5)).
          with:
            - hash: 3b26142829b8887d011d779079a243bd61ab53c3990d550320a17b59ade6ba36
              identifier list: [ "e0", "e1"]
              ...
              ca.5.3:
                log point: Canonical identifiers for temporary identifiers (4.4.3 (5.3)).
                issuer:
                    - blank node: e1
                      canonical identifier: c14n2
                    - blank node: e0
                      canonical identifier: c14n3
        ...
      ```

6. Add the issued identifiers map from the canonical issuer to the canonicalized dataset.

   **Explanation**

   This step adds the issued identifiers map from the canonical issuer to the canonicalized dataset, the [keys](https://infra.spec.whatwg.org/#map-key) in the issued identifiers map are [map entries](https://infra.spec.whatwg.org/#map-entry) in the input blank node identifier map.

   **Logging**

   Log the state of the canonical issuer at the completion of the algorithm.

   ```
   # Canonical issuer state after step 6 for shared hashes example
   ca:
     ...
     ca.6:
       log point: Issued identifiers map (4.4.3 (6)).
       issued identifiers map: {e2: c14n0, e3: c14n1, e1: c14n2, e0: c14n3}
   ```

7. Return the serialized canonical form of the canonicalized dataset.
   Upon request, alternatively (or additionally) return the canonicalized dataset itself, which includes the input blank node identifier map, and issued identifiers map from the canonical issuer.
   > **Note:**
   >
   > > **Note:**
   > >
   > > Note
   >
   > Technically speaking, one implementation
   > might return a canonicalized dataset that maps
   > particular blank nodes to different identifiers than another
   > implementation, however, this only occurs when there are
   > isomorphisms in the dataset such that a canonically serialized
   > expression of the dataset would appear the same from either
   > implementation.

   **Explanation**

   The serialized canonical form is an N-Quads
   document where the blank node identifiers are taken
   from the canonical identifiers associated with each blank node.

   The canonicalized dataset is composed of the original input dataset, the input blank node identifier map,
   containing identifiers for each blank node in the input dataset,
   and the canonical issuer,
   containing an issued identifiers map mapping the identifiers in the input blank node identifier map to their canonical identifiers.

### 4.5 Issue Identifier Algorithm

This algorithm issues a new [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) for
a given existing [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier). It also updates
state information that tracks the order in which new [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) were issued. The order of issuance is
important for canonically labeling blank nodes that are isomorphic
to others in the dataset.

#### 4.5.1 Overview

The algorithm maintains an issued identifiers map to
relate an existing [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) from the input dataset to a new [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) using a given identifier prefix (`c14n`) with new identifiers issued by appending an incrementing number.
For example, when called for a blank node identifier such as `e3`,
it might result in a issued identifier of `c14n1`.

#### 4.5.2 Algorithm

The algorithm takes an identifier issuer *I* and an *existing identifier* as inputs. The output is a new *issued identifier*. The steps of the algorithm are:

1. If there is a [map entry](https://infra.spec.whatwg.org/#map-entry) for *existing identifier* in issued identifiers map of *I*,
   return it.
2. Generate *issued identifier* by concatenating identifier prefix with the string value of identifier counter.
3. Add an [entry](https://infra.spec.whatwg.org/#map-entry) mapping *existing identifier* to *issued identifier* to the issued identifiers map of *I*.
4. Increment identifier counter.
5. Return *issued identifier*.

### 4.6 Hash First Degree Quads

This algorithm calculates a hash for a given [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) across the quads in a [dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) in which that blank node
is a component.
If the hash uniquely identifies that blank node,
no further examination is necessary.
Otherwise, a hash will be created for the blank node using
the algorithm in 4.8 Hash N-Degree Quads (§4.8) invoked via 4.4 Canonicalization Algorithm (§4.4).

#### 4.6.1 Overview

*This section is non-normative.*

To determine whether the first degree information of a node *n* is unique,
a hash is assigned to its mention set, *Qn*.
The first degree hash of a blank node *n*,
denoted *hf(n)*,
is the hash that results from 4.6 Hash First Degree Quads (§4.6) when passing *n*.
Nodes with unique first degree hashes have unique first degree information.

For consistency, [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) used in *Qn* are replaced with placeholders in a canonical n-quads serialization of that quad.
Every blank node component is replaced with either `a` or `z`,
depending on if that component is *n* or not.

The resulting serialized quads are then [code point ordered](https://www.w3.org/TR/xpath-functions/#codepoint-collation),
concatenated, and hashed.
This hash is the first degree hash of *n*, *hf(n)*.

#### 4.6.2 Examples

*This section is non-normative.*
> **Example:**
>
> Example 4: Unique hashes
>
> This example illustrates hashing quads containing
> blank nodes where hashing the statements mentioning those blank nodes generates unique results.
>
> *Figure 4 An illustration of a graph resulting in unique hashes.
> Image available in [SVG](https://www.w3.org/TR/rdf-canon/unique-hashes.svg "SVG image of unique hashes") .*
>
> ```
> :p :q _:e0 .
> :p :r _:e1 .
> _:e0 :s :u .
> _:e1 :t :u .
> ```
>
> The algorithm will be called twice, with each blank node (`e0` and `e1`).
> Running the algorithm with the reference node `e0` results in the
> following quads, after replacing blank nodes:
>
> ```
> :p :q _:a .
> _:a :s :u .
> ```
>
> These are then serialized to canonical n-quads form: `'<http://example.com/#p> <http://example.com/#q> _:a .\n_:a <http://example.com/#s> <http://example.com/#u> .\n'`,
> concatenated and hashed
> using the hash algorithm (SHA-256) resulting in `21d1dd5ba21f3dee9d76c0c00c260fa6f5d5d65315099e553026f4828d0dc77a`.
>
> The algorithm is run a second time with the reference node `e1` resulting
> in the following quads:
>
> ```
> :p :r _:a .
> _:a :t :u .
> ```
>
> These are then serialized to canonical n-quads form: `'<http://example.com/#p> <http://example.com/#r> _:a .\n_:a <http://example.com/#t> <http://example.com/#u> .\n'`,
> concatenated and hashed as before resulting in `6fa0b9bdb376852b5743ff39ca4cbf7ea14d34966b2828478fbf222e7c764473`.
>
> Thus the generated hashes each reference just a single blank node,
> allowing the canonicalization algorithm to use only the
> Hash First Degree Quads algorithm.
> **Example:**
>
> Example 5: Shared hashes
>
> This example illustrates hashing quads containing
> blank nodes where hashing the statements mentioning those blank nodes have overlapping results.
>
> *Figure 5 An illustration of a graph resulting in shared hashes.
> Image available in [SVG](https://www.w3.org/TR/rdf-canon/shared-hashes.svg "SVG image of a graph resulting in shared hashes") .*
>
> ```
> :p :q _:e0 .
> :p :q _:e1 .
> _:e0 :p _:e2 .
> _:e1 :p _:e3 .
> _:e2 :r _:e3 .
> ```
>
> The algorithm will be called four times, with each blank node
> (`e0`, `e1`, `e2`, and `e3`).
> Running the algorithm with the reference node `e0` results in the
> following quads, after replacing blank nodes:
>
> ```
> :p :q _:a .
> _:a :p _:z .
> ```
>
> Which hashes to: `3b26142829b8887d011d779079a243bd61ab53c3990d550320a17b59ade6ba36`.
>
> Note that using reference node `e1` results in the same quads,
> and thus results in the same hash.
>
> Using the reference node `e2` results in the following quads:
>
> ```
> _:z :p _:a .
> _:a :r _:z .
> ```
>
> Which hashes to: `15973d39de079913dac841ac4fa8c4781c0febfba5e83e5c6e250869587f8659`.
>
> Lastly, using the reference node `e3` results in the following quads:
>
> ```
> _:z :p _:a .
> _:z :r _:a .
> ```
>
> Which hashes to: `7e790a99273eed1dc57e43205d37ce232252c85b26ca4a6ff74ff3b5aea7bccd`.
>
> The hashes for `e2` and `e3` are unique, but `e0`,
> and `e1` share a common hash,
> which will require the use of the Hash N-Degree Quads Algorithm (§4.8.3),
> as it is necessary to consider quads further removed from the direct mentions to determine a unique hash.

#### 4.6.3 Algorithm

This algorithm takes the canonicalization state and a *reference blank node identifier* as inputs.

1. Initialize *nquads* to an empty [list](https://infra.spec.whatwg.org/#list).
   It will be used to store quads in canonical n-quads form.
2. Get the [list](https://infra.spec.whatwg.org/#list) of quads *quads* from the [map entry](https://infra.spec.whatwg.org/#map-entry) for reference blank node identifier in the blank node to quads map.
3. For each quad *quad* in *quads*:
   1. Serialize the quad in canonical n-quads form with the
      following special rule:
      1. If any component in *quad* is an [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node), then serialize it using a
         special identifier as follows:
         1. If the [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)'s existing [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) matches the reference blank node identifier then use the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) `a`,
            otherwise, use the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) `z`.
4. Sort nquads in [Unicode code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation).
5. Return the hash that results from passing the sorted
   and concatenated nquads through the hash algorithm.

   **Logging**

   Log the inputs and result of running this algorithm.

   ```
   # Inputs and hash result for the Hash First Degree Hash algorithm for unique hashes example
   h1dq:
     log point: Hash First Degree Quads function (4.6.3).
     nquads:
       - <http://example.com/#p> <http://example.com/#q> _:a .
       - _:a <http://example.com/#s> <http://example.com/#u> .
     hash: 21d1dd5ba21f3dee9d76c0c00c260fa6f5d5d65315099e553026f4828d0dc77a
   ```

### 4.7 Hash Related Blank Node

This algorithm generates a hash for some [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) component of a quad,
considering its position within that quad.
This is used as part of the Hash N-Degree Quads algorithm (§4.8.3) to characterize the blank nodes related to some particular blank node
within their mention sets.

#### 4.7.1 Overview

*This section is non-normative.*

An *identifier* for a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node), *related*,
which is a component of some quad, is used along
with information describing its position within the quad to create
a representation of that blank node within the quad,
which is then hashed.
The identifier is first found from the following:

1. An issued identifier from canonical issuer in the canonicalization state,
2. An issued identifier from *issuer*, or
3. the result of the Hash N-Degree Quads algorithm (§4.8.3) for *related*.

#### 4.7.2 Examples

*This section is non-normative.*
> **Example:**
>
> Example 6: With assigned canonical identifier
>
> This example illustrates generating the related hash
> for a blank node component of a quad, where the component
> is in the [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) position and has already had
> an assigned canonical identifier from the canonical issuer.
>
> Given the predicate `:p`, *related* [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) `e2` (already assigned the canonical [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) `c14n0`),
> an *input* is created as `o<http://example.com/#p>_:c14n0`,
> which hashes to `29cf7e22790bc2ed395b81b3933e5329fc7b25390486085cac31ce7252ca60fa`.
>
> If such an identifier had not yet been established,
> it would instead use the results of the Hash First Degree Quads algorithm (§4.6),
> without the leading `_:`.

#### 4.7.3 Algorithm

This algorithm creates a hash to identify how one [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) is related to another. It takes the canonicalization state, a *related* [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), a *quad*, an identifier issuer, *issuer*, and a [string](https://infra.spec.whatwg.org/#string) *position* as inputs.

1. Initialize a [string](https://infra.spec.whatwg.org/#string) *input* to the value of *position*.
2. If *position* is not `g`, append `<`, the value of the [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate) in *quad*, and `>` to *input*.
3. If there is a canonical identifier for *related*,
   or an identifier issued by *issuer*,
   append the string `_:`, followed by that identifier (using the canonical
   identifier if present, otherwise the one issued by *issuer*) to *input*.

   **Explanation**

   If a canonical identifier was already issued for *related*,
   it will be in the canonical issuer contained within canonicalization state.
   Otherwise, the temporary *issuer* instance may already
   have a mapping for *related*.

4. Otherwise,
   append the result of the Hash First Degree Quads algorithm (§4.6),
   passing *related* to *input*.

   **Explanation**

   If no identifier, canonical or temporary, has already been issued,
   a new identifier is created using the Hash First Degree Quads algorithm (§4.6).

   Note that Hash First Degree Quads algorithm (§4.6) has already been called on all blank nodes in step 3 of the §4.4 Canonicalization Algorithm.
   Implementations should consider reusing a previously determined result rather than execute the Hash First Degree Quads algorithm (§4.6) again.

5. Return the hash that results from passing *input* through the hash algorithm.

   **Explanation**

   This resulting string is used to generate a hash; in this respect, it is similar to
   the Hash First Degree Quads algorithm (§4.6) which
   uses the serialization of quads in nquads for hashing. For the sake of consistency, the nquad representation of *identifier* is used in this step, hence the
   appearance of the `_:` string.

   **Logging**

   Log the inputs and result of running this algorithm.

   ```
   # Inputs and hash result for the Hash Related Blank algorithm for shared hashes example
   hndq3.1:
     log point: Hash related bnode component (4.8.3 (3.1))
     with:
       - position: o
         related: e2
         input: "o<http://example.com/#p>_:c14n0"
         hash: 29cf7e22790bc2ed395b81b3933e5329fc7b25390486085cac31ce7252ca60fa
   ```

### 4.8 Hash N-Degree Quads

This algorithm calculates a hash for a given [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) across the quads in a [dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) in which that blank node
is a component for which the hash does not uniquely identify that blank node.
This is done by expanding the search from quads directly referencing that
blank node (the mention set), to those quads
which contain nodes which are also components of quads in the mention set,
called the gossip path.
This process proceeds in every greater degrees of indirection until
a unique hash is obtained.

#### 4.8.1 Overview

*This section is non-normative.*

Usually, when trying to determine if two nodes in a graph are
equivalent, you simply compare their identifiers. However, what if the
nodes don't have identifiers? Then you must determine if the two nodes
have equivalent connections to equivalent nodes all throughout the
whole graph. This is called the graph isomorphism problem. This
algorithm approaches this problem by considering how one might draw
a graph on paper. You can test to see if two nodes are equivalent
by drawing the graph twice. The first time you draw the graph the
first node is drawn in the center of the page. If you can draw the
graph a second time such that it looks just like the first, except
the second node is in the center of the page, then the nodes are
equivalent. This algorithm essentially defines a deterministic way to
draw a graph where, if you begin with a particular node, the graph
will always be drawn the same way. If two graphs are drawn the same way
with two different nodes, then the nodes are equivalent. A hash is used to indicate a particular way that the graph
has been drawn and can be used to compare nodes.

When two blank nodes have the same first degree hash,
extra steps must be taken to detect global,
or *N*-degree, distinctions.
All information that is in any way connected to the blank node *n* through other blank nodes, even transitively, must be considered.

To consider all transitive information,
the algorithm traverses and encodes all possible paths of incident mentions emanating from *n*, called gossip paths,
that reach every unlabeled blank node connected to *n*.
Each unlabeled blank node is assigned a temporary identifier
in the order in which it is reached in the
gossip path being explored.
The mentions that are traversed to reach
connected blank nodes are encoded in these paths via related hashes.
This provides a deterministic way to order all paths coming from *n* that
reach all blank nodes connected to n without relying on input blank
node identifiers.

This algorithm works in concert with the main canonicalization algorithm
to produce a unique, deterministic identifier for a particular blank
node. This hash incorporates all of the information that
is connected to the blank node as well as how it is connected. It does
this by creating deterministic paths that emanate out from the blank
node through any other adjacent blank nodes.

Ultimately, the algorithm selects the shortest gossip path (based on its encoding as a string), distributing canonical
identifiers to the unlabeled blank nodes in the order in which they
appear in this path.
The hash of this encoded shortest path,
called the N-degree hash of *n*,
distinguishes *n* from other blank nodes in the dataset.

For clarity, we consider a gossip path encoded via the string *s* to be shortest provided that:

1. The length of *s* is less than or equal to the length
   of any other gossip path string *s′*.
2. If *s* and *s′* have the same length (as strings),
   then *s* is [code point ordered](https://www.w3.org/TR/xpath-functions/#codepoint-collation) less than or equal to *s′*.

For example, *abc* is shorter than *bbc*,
whereas *abcd* is longer than *bcd*.

The following provides a high level outline for how the N-degree hash of *n* is computed along the shortest gossip path.
Note that the full algorithm considers all gossip paths,
ultimately returning the hash of the shortest encoded path.

1. **Compute related hashes**.
   Compute the related hash *Hn* set for *n*,
   i.e., all first degree mentions between *n* and another blank node.
   Note that this includes both unlabeled blank nodes and those
   already issued a canonical identifier (labeled blank nodes).
2. **Explore mentions**.
   Given the related hash *x* in *Hn*,
   record *x* in the data to hash *Dn*.
   Determine whether each blank node reachable via the mention with related hash *x* has already received an identifier.
   1. **Record the identifiers of labeled nodes**.
      If a blank node already has an identifier,
      record its identifier in *Dn* once for every mention with related hash *x*.
      Skip to the next related hash in *Hn* and repeat step 2.
   2. **Distribute and record temporary identifiers to unlabeled nodes**.
      For each unlabeled blank node,
      assign it a temporary identifier according to the order in which it is reached in the gossip path,
      recording its given identifier in *Dn* (including repetitions).
      Add each unlabeled node to the recursion list *Rn(x)* in this same order (omitting repetitions).
   3. **Recurse on newly labeled nodes**.
      For each *ni* in *Rn(x)*
      1. Record its identifier in *Dn*
      2. Append < *r(i)* > to *Dn* where *r(i)* is the data to hash that results from returning to step 1,
         replacing *n* with *ni*.
3. **Compute the *N*-degree hash of n**.
   Hash *Dn* to return the *N*-degree hash of *n*,
   namely *hN(n)*.
   Return the updated issuer *In* that has now distributed temporary identifiers to all unlabeled blank nodes connected to *n*.

As described above in step 2.3, *HN* recurses on each unlabeled blank node
when it is first reached along the gossip path being explored.
This recursion can be visualized as moving along the path from *n* to the blank node *ni* that is receiving a temporary identifier.
If, when recursing on *ni*,
another unlabeled blank node *nj* is discovered,
the algorithm again recurses.
Such a recursion traces out the gossip path from *n* to *nj* via *ni*.

The recursive hash *r(i)* is the hash returned from
the completed recursion on the node *ni* when computing *hN(n)*.
Just as *hN(n)* is the hash of *Dn*,
we denote the data to hash in the recursion on *ni* as *Di*.
So, *r(i)* = *h(Di)*.
For each related hash *x* ∈ *Hn*, *Rn(x)* is called the *recursion list* on
which the algorithm recurses.

#### 4.8.2 Examples

*This section is non-normative.*
> **Example:**
>
> Example 7: Shared hashes
>
> This example revisits Example 3 to illustrate the operation of the Hash N-Degree Quads Algorithm (§4.8.3) on the blank nodes (`e0` and `e1`) which resulted in a shared result from the Hash First Degree Quads Algorithm (§4.6.3).
> The other blank nodes (`e2` and `e3`) had unique
> hashes when processed by the Hash N-Degree Quads Algorithm (§4.6.3),
> so that canonical identifiers have already been issued,
> as recorded in the identifier issuer instance.
>
> *Table 10 Established canonical identifiers from canonical issuer*
>
> | *blank node* | *canonical identifier* |
> | ------------ | ---------------------- |
> | `e2`         | `c14n0`                |
> | `e3`         | `c14n1`                |
>
>
> *Figure 6 An illustration of a graph resulting in shared hashes.
> Image available in [SVG](https://www.w3.org/TR/rdf-canon/shared-hashes.svg "SVG image of a graph resulting in shared hashes") .*
>
> ```
> :p :q _:e0 .
> :p :q _:e1 .
> _:e0 :p _:e2 .
> _:e1 :p _:e3 .
> _:e2 :r _:e3 .
> ```
>
> The algorithm will be called twice, with each blank node
> which did not result in a unique hash
> from the Hash First Degree Quads Algorithm (§4.6.3) (`e0` and `e1`).
> The [map entry](https://infra.spec.whatwg.org/#map-entry) for `e0` in the blank node to quads map results in the
> following quads:
>
> ```
> :p :q _:e0 .
> _:e0 :p _:e2 .
> ```
>
> When called, the *temporary issuer* has the following mappings:
>
> *Table 11 Initial mappings in *temporary issuer* for `e0`*
>
> | *blank node* | *temporary identifier* |
> | ------------ | ---------------------- |
> | `e0`         | `b0`                   |
> Step 3 iterates over each of these quads
> to find [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) *components* to populate *Hn* with the result of running the Hash Related Blank Node algorithm (§4.7) using the *position* of that *component* within the quad.
>
> *Table 12 Hash for `e2` related to `e0`*
>
> | *related* | *quad*       | *position* | *hash*                    |
> | --------- | ------------ | ---------- | ------------------------- |
> | `e2`      | `e0 :p e2 .` | `o`        | `29cf7e2279...7252ca60fa` |
> which results in the following *Hn*:
>
> *Table 13 Blank node list for hash*
>
> | *related hash*                                                     | *blank node list* |
> | ------------------------------------------------------------------ | ----------------- |
> | `29cf7e22790bc2ed395b81b3933e5329fc7b25390486085cac31ce7252ca60fa` | `[ e2 ]`          |
> Step 5 iterates over each *related hash* which is a key in *Hn*,
> which can have one or more related blank nodes,
> which determines the shortest gossip path between
> the two nodes (`e0` and `e2`).
> In this case, the hash maps to just `e2`,
> for which a canonical identifier has already been chosen (`c14n0`),
> so there is a single permutation
> resulting in one candidate path.
> The resulting *chosen path* is `_:c14n0`.
>
> The string *data to hash* is composed
> of the single *related hash* and the *chosen path*: `29cf7e22790bc2ed395b81b3933e5329fc7b25390486085cac31ce7252ca60fa_:c14n0`,
> which hashes to `fbc300de5afafd97a4b9ee1e72b57754dcdcb7ebb724789ac6a94a5b82a48d30`,
> which, along with the *temporary issuer* used to traverse
> these paths, is the result of the algorithm:
>
> *Table 14 Result for `e0`*
>
> | *temporary issuer* mappings | *original identifier* *temporary identifier* `e0` `b0`             |
> | --------------------------- | ------------------------------------------------------------------ |
> | *hash*                      | `fbc300de5afafd97a4b9ee1e72b57754dcdcb7ebb724789ac6a94a5b82a48d30` |
> The algorithm is called again for `e1`.
>
> *Table 15 Initial mappings in *temporary issuer* for `e1`*
>
> | *blank node* | *temporary identifier* |
> | ------------ | ---------------------- |
> | `e1`         | `b0`                   |
> The [map entry](https://infra.spec.whatwg.org/#map-entry) for `e1` in the blank node to quads map results in the
> following quads:
>
> ```
> :p :q _:e1 .
> _:e1 :p _:e3 .
> ```
>
> Step 3 again calculates [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) *components* using Hash Related Blank Node algorithm (§4.7).
>
> *Table 16 Hash for `e3` related to `e1`*
>
> | *related* | *quad*       | *position* | *hash*                    |
> | --------- | ------------ | ---------- | ------------------------- |
> | `e3`      | `e1 :p e3 .` | `o`        | `b7956ea1d6...ff6b098216` |
> which results in the following *Hn*:
>
> *Table 17 Blank node list for hash*
>
> | *related hash*                                                     | *blank node list* |
> | ------------------------------------------------------------------ | ----------------- |
> | `b7956ea1d654d5824496eb439a1f2b79478bd7d02d4a115f4c97cbff6b098216` | `[ e3 ]`          |
> Step 5 runs in essentially the same manner, mapping just `e3` having the canonical identifier `c14n1`,
> so there is again a single permutation
> resulting in one candidate path.
> The resulting *chosen path* is `_:c14n1`.
>
> The string *data to hash* is composed
> of the single *related hash* and the *chosen path*: `af54b9512b1ef069205e8e41bc5a96e86a108b0389caa5029f2c3fd0bc465246_:c14n1`,
> which hashes to `767a5e66f509221f45003a16c12a89d4d9675cfa51ffa80459b63606bdfc2ada`.
>
> The string *data to hash* is composed
> of the single *related hash* and the *chosen path*: `b7956ea1d654d5824496eb439a1f2b79478bd7d02d4a115f4c97cbff6b098216_:c14n1`,
> which hashes to `fbc300de5afafd97a4b9ee1e72b57754dcdcb7ebb724789ac6a94a5b82a48d30`,
> which, along with the *temporary issuer* used to traverse
> these paths, is the result of the algorithm:
>
> *Table 18 Result for `e1`*
>
> | *temporary issuer* mappings | *original identifier* *temporary identifier* `e1` `b0`             |
> | --------------------------- | ------------------------------------------------------------------ |
> | *hash*                      | `2c0b377baf86f6c18fed4b0df6741290066e73c932861749b172d1e5560f5045` |

#### 4.8.3 Algorithm

The inputs to this algorithm are the canonicalization state,
the *identifier* for the [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) to
recursively hash quads for, and path identifier *issuer* which is
an identifier issuer that issues temporary [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier)s. The output from this algorithm
will be a hash and the identifier issuer used
to help generate it.

**Logging**

Log the inputs to the algorithm.

```
# Inputs for the Hash N-Degree Quads algorithm for double circle example
hndq:
  log point: Hash N-Degree Quads function (4.8.3).
  identifier: e0
  issuer: {e0: b0}
  ...
```

1. Create a new [map](https://infra.spec.whatwg.org/#ordered-map) *Hn* for relating hashes to related [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node).
2. Get a reference, *quads*, to the list of quads from the [map entry](https://infra.spec.whatwg.org/#map-entry) for *identifier* in the blank node to quads map.

   **Explanation**

   *quads* is the mention set of *identifier*.

   **Logging**

   Log the quads from the mention set of *identifier*.

   ```
   # Inputs for the Hash N-Degree Quads algorithm for double circle example
   hndq:
     identifier: e0
     log point: Hash N-Degree Quads function (4.8.3).
     issuer: {e0: b0}
     hndq.2:
       log point: Quads for identifier (4.8.3 (2)).
       quads:
       - _:e0 <http://example.org/vocab#next> _:e1 .
       - _:e0 <http://example.org/vocab#prev> _:e1 .
       - _:e1 <http://example.org/vocab#next> _:e0 .
       - _:e1 <http://example.org/vocab#prev> _:e0 .
     ...
   ```

3. For each *quad* in *quads*:

   **Explanation**

   This loop calculates the related hash *Hn* for other blank nodes within the mention set of *identifier*.

   1. For each *component* in *quad*, where *component* is the [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject), [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object), or [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name), and it is a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) that is not identified by *identifier*:
      1. Set *hash* to the result of the Hash Related Blank Node algorithm (§4.7),
         passing the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) for *component* as *related*, *quad*, *issuer*, and *position* as either `s`, `o`, or `g` based on whether *component* is a [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject), [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object), [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name), respectively.
      2. Add a mapping of *hash* to the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) for *component* to *Hn*, adding an entry
         as necessary.

   **Logging**

   Include the logs for each iteration of the Hash Related Blank Node algorithm (§4.7) and the resulting *Hn*.

   ```
   # Step 3 of Hash N-Degree Quads using double circle example
   hndq:
     identifier: e0
     log point: Hash N-Degree Quads function (4.8.3).
     issuer: {e0: b0}
     ...
   hndq.3:
     log point: Hash N-Degree Quads function (4.8.3 (3)).
     with:
       - quad: _:e0 <http://example.org/vocab#next> _:e1 .
         hndq.3.1:
           log point: Hash related bnode component (4.8.3 (3.1))
           with:
             - position: o
               related: e1
               h1dq:
                 log point: Hash First Degree Quads function (4.6.3).
                 nquads:
                   - _:z <http://example.org/vocab#next> _:a .
                   - _:z <http://example.org/vocab#prev> _:a .
                   - _:a <http://example.org/vocab#next> _:z .
                   - _:a <http://example.org/vocab#prev> _:z .
                 hash: 60dc8fc7b5481014b6ea38efb05455676d1e93e19b99119ab294941dacc16b3b
               input: "o<http://example.org/vocab#next>60dc8fc7b5481014b6ea38efb05455676d1e93e19b99119ab294941dacc16b3b"
               hash: 20bb08971220a5382a9a06ba2977c5fb859e63192e0b2015a378af89e453f25e
       - quad: _:e0 <http://example.org/vocab#prev> _:e1 .
         ...
     Hash to bnodes:
         20bb08971220a5382a9a06ba2977c5fb859e63192e0b2015a378af89e453f25e:
           - e1
         1e4e55ba02b8b0b527c32e2343fbcfee2e2bd9c1972c67cc01f85fabde7bc42d:
           - e1
         56d0774755aaf8d9cf4da8af3728e5589f94e5cd7d9aee86f0c5a7bc1d71c7ca:
           - e1
         2a5dd448b9467a08479008a5350829441868b7f913343cd500fe8619e047cff4:
           - e1
   ...
   ```

4. Create an empty string, *data to hash*.
5. For each *related hash* to *blank node list* mapping in *Hn*, [code point ordered](https://www.w3.org/TR/xpath-functions/#codepoint-collation) by *related hash*:

   **Explanation**

   This loop explores the gossip paths for each
   related blank node sharing a common hash to *identifier* finding the shortest such path (*chosen path*).
   This determines how canonical identifiers for
   otherwise commonly hashed blank nodes are chosen.

   Each path is represented by the concatenation of the
   identifiers for each related blank node
   — either the issued identifier,
   or a temporary identifier created using a copy of *issuer*.
   Those for which temporary identifiers were issued are later
   recursed over using this algorithm.

   **Logging**

   Log the value of *related hash* and state of *data to hash*.

   ```
   # Log related hash and data to hash in each iteration of step 5 for double circle example.
   hndq:
     log point: Hash N-Degree Quads function (4.8.3).
     identifier: e0
     issuer: {e0: b0}
     ...
     hndq.5:
       log point: Hash N-Degree Quads function (4.8.3 (5)), entering loop.
       with:
       - related_hash: 1e4e55ba02b8b0b527c32e2343fbcfee2e2bd9c1972c67cc01f85fabde7bc42d
         data_to_hash: ""
         ...
   ```

   1. Append the *related hash* to the *data to hash*.
   2. Create a [string](https://infra.spec.whatwg.org/#string) *chosen path*.
   3. Create an unset *chosen issuer* variable.
   4. For each [permutation](https://en.wikipedia.org/wiki/Permutation) *p* of *blank node list*:

      **Logging**

      Log each [permutation](https://en.wikipedia.org/wiki/Permutation) *p*.

      ```
      # Log each permutation of step 5.4 using double circle example.
      hndq:
        log point: Hash N-Degree Quads function (4.8.3).
        identifier: e0
        issuer: {e0: b0}
        ...
        hndq.5:
          log point: Hash N-Degree Quads function (4.8.3 (5)), entering loop.
          with:
          - related_hash: 1e4e55ba02b8b0b527c32e2343fbcfee2e2bd9c1972c67cc01f85fabde7bc42d
            data_to_hash: ""
            hndq.5.4:
              log point: Hash N-Degree Quads function (4.8.3 (5.4)), entering loop.
              with:
              - perm: [ "e1"]
                ...
      ```

      1. Create a copy of *issuer*, *issuer copy*.
      2. Create a [string](https://infra.spec.whatwg.org/#string) *path*.
      3. Create a *recursion list*, to store [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) that must be
         recursively processed by this algorithm.
      4. For each *related* in *p*:
         1. If a canonical identifier has been issued for *related* by canonical issuer, append the string `_:`, followed by
            the canonical identifier for *related*, to *path*.

            **Explanation**

            A canonical identifier may have been generated before calling this algorithm,
            if it was issued from an earlier call to Hash First Degree Quads algorithm (§4.6).
            There is no reason to recurse and apply the algorithm to any related blank node that has already been assigned a canonical identifier.
            Furthermore, using the canonical identifier also further distinguishes it from any temporary identifier, allowing for even greater efficiency in finding the chosen path.

         2. Otherwise:
            1. If *issuer copy* has not issued
               an identifier for *related*, append *related* to *recursion list*.

               **Explanation**

               Temporarily labeled nodes have identifiers recorded
               in *issuer copy*,
               which is later used to recursively call this algorithm,
               so that eventually all nodes are given canonical identifiers.

            2. Use the §4.5 Issue Identifier Algorithm,
               passing *issuer copy* and the *related*, and
               append the string `_:`, followed by the result, to *path*.
         3. If *chosen path* is not empty and the length
            of *path* is greater than or equal to the length
            of *chosen path* and *path* is
            greater than *chosen path* when
            considering [code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation),
            then skip to the next [permutation](https://en.wikipedia.org/wiki/Permutation) *p*.

            **Explanation**

            If *path* is already longer than
            the prospective *chosen path*,
            we can terminate this iteration early.

         **Explanation**

         *path* is used to generate a hash at a later step; in this respect, it is similar to
         the Hash First Degree Quads algorithm (§4.6) which
         uses the serialization of quads in nquads for hashing. For the sake of consistency, the nquad representation of blank node identifiers is used in these steps, hence the
         usage of the `_:` string.

         **Logging**

         Log *related* and *path*.

         ```
         # Log related and path of step 5.4.4 using double circle example.
         hndq:
           log point: Hash N-Degree Quads function (4.8.3).
           identifier: e0
           issuer: {e0: b0}
           ...
           hndq.5:
             log point: Hash N-Degree Quads function (4.8.3 (5)), entering loop.
             with:
             - related_hash: 1e4e55ba02b8b0b527c32e2343fbcfee2e2bd9c1972c67cc01f85fabde7bc42d
               data_to_hash: ""
               hndq.5.4:
                 log point: Hash N-Degree Quads function (4.8.3 (5.4)), entering loop.
                 with:
                 - perm: [ "e1"]
                   hndq.5.4.4:
                     log point: Hash N-Degree Quads function (4.8.3 (5.4.4)), entering loop.
                     with:
                       - related: e1
                         path: ""
                   ...
         ```

      5. For each *related* in *recursion list*:

         **Explanation**

         The prospective *path* is extended with
         the hash resulting from recursively calling this algorithm
         on each related blank node issued a temporary identifier.

         **Logging**

         Log *recursion list* and *path*.

         ```
         # Log related and path of step 5.4.5 using double circle example.
         hndq:
           log point: Hash N-Degree Quads function (4.8.3).
           identifier: e0
           issuer: {e0: b0}
           ...
           hndq.5:
             log point: Hash N-Degree Quads function (4.8.3 (5)), entering loop.
             with:
             - related_hash: 1e4e55ba02b8b0b527c32e2343fbcfee2e2bd9c1972c67cc01f85fabde7bc42d
               data_to_hash: ""
               hndq.5.4:
                 log point: Hash N-Degree Quads function (4.8.3 (5.4)), entering loop.
                 with:
                 - perm: [ "e1"]
                   ...
                   hndq.5.4.5:
                     log point: Hash N-Degree Quads function (4.8.3 (5.4.5)), before possible recursion.
                     recursion list: [ "e1"]
                     path: "_:b1"
                   ...
         ```

         1. Set *result* to the result of recursively executing
            the Hash N-Degree Quads algorithm (§4.8),
            passing the canonicalization state, *related* for *identifier*, and *issuer copy* for *path identifier issuer*.

            **Logging**

            Log *related* and
            include logs for each recursive call to Hash N-Degree Quads algorithm (§4.8).

            ```
            # Log related and path of step 5.4.5.1 using double circle example.
            hndq:
              log point: Hash N-Degree Quads function (4.8.3).
              identifier: e0
              issuer: {e0: b0}
              ...
              hndq.5:
                log point: Hash N-Degree Quads function (4.8.3 (5)), entering loop.
                with:
                - related_hash: 1e4e55ba02b8b0b527c32e2343fbcfee2e2bd9c1972c67cc01f85fabde7bc42d
                  data_to_hash: ""
                  hndq.5.4:
                    log point: Hash N-Degree Quads function (4.8.3 (5.4)), entering loop.
                    with:
                    - perm: [ "e1"]
                      ...
                      hndq.5.4.5:
                        log point: Hash N-Degree Quads function (4.8.3 (5.4.5)), before possible recursion.
                        recursion list: [ "e1"]
                        path: "_:b1"
                        with:
                          - related: e1
                            hndq:
                              ...
            ```

         2. Use the §4.5 Issue Identifier Algorithm,
            passing *issuer copy* and *related*; append the string `_:`, followed by
            the result, to *path*.
         3. Append `<`, the hash in *result*, and `>` to *path*.
         4. Set *issuer copy* to the identifier issuer in result.
         5. If *chosen path* is not empty and the length
            of *path* is greater than or equal to the length
            of *chosen path* and *path* is
            greater than *chosen path* when considering [code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation),
            then skip to the next *p*.

            **Explanation**

            If *path* is already longer than
            the prospective *chosen path*,
            we can terminate this iteration early.

      6. If *chosen path* is empty or *path* is
         less than *chosen path* when considering [code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation),
         set *chosen path* to *path* and *chosen issuer* to *issuer copy*.
   5. Append *chosen path* to *data to hash*.

      **Logging**

      Log *chosen path* and *data to hash*.

      ```
      # Log chosen path and data to hash logs of step 5.5 using double circle example.
      hndq:
        log point: Hash N-Degree Quads function (4.8.3).
        identifier: e0
        issuer: {e0: b0}
        ...
        hndq.5:
          log point: Hash N-Degree Quads function (4.8.3 (5)), entering loop.
          with:
          - related_hash: 1e4e55ba02b8b0b527c32e2343fbcfee2e2bd9c1972c67cc01f85fabde7bc42d
            data_to_hash: ""
            ...
            hndq.5.5:
              log point: Hash N-Degree Quads function (4.8.3 (5.5). End of current loop with Hn hashes.
              chosen path: "_:b1_:b1<1ae899f76e760eb7caf6656437aaef845b50887aff7baeb3531add85ec02ed35>"
              data to hash: "1e4e55ba02b8b0b527c32e2343fbcfee2e2bd9c1972c67cc01f85fabde7bc42d_:b1_:b1<1ae899f76e760eb7caf6656437aaef845b50887aff7baeb3531add85ec02ed35>"
            ...
      ```

   6. Replace *issuer*, by reference, with*chosen issuer*.
6. Return *issuer* and the hash that results from
   passing *data to hash* through the hash algorithm.

   **Logging**

   Log *issuer* and results from passing *data to hash* through the hash algorithm.

   ```
   # Log issuer and resulting hash of step 6 using double circle example.
   hndq:
     log point: Hash N-Degree Quads function (4.8.3).
     identifier: e0
     issuer: {e0: b0}
     ...
     hndq.6:
       log point: Leaving Hash N-Degree Quads function (4.8.3).
       hash: e332b4b59e1c4794ee72a4df0f63723326ffb6d6a5c0d0cb4d2dd8d8d5ebf5a4
       issuer: {e0: b0, e1: b1}
   ```

## 5. Serialization

This section describes the process of creating a serialized [N-Quads] representation
of a canonicalized dataset.

The *serialized canonical form* of a canonicalized dataset is an N-Quads document [N-QUADS]
created by representing each quad from the canonicalized dataset in canonical n-quads form,
sorting them into [code point order](https://www.w3.org/TR/xpath-functions/#codepoint-collation),
and concatenating them. (Note that each canonical N-Quads statement ends with a new line,
so no additional separators are needed in the concatenation.)
The resulting document has a media type of `application/n-quads`,
as described in [C. N-Quads Internet Media Type, File Extension and Macintosh File Type](https://www.w3.org/TR/n-quads/#sec-mediaReg) of [N-QUADS].

When serializing quads in canonical n-quads form,
components which are [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) *MUST* be serialized using the
canonical label associated with each [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) from the issued identifiers map component of the canonicalized dataset.
> **Example:**
>
> Example 8: Canonical N-Quads representation of Unique Hashes
>
> This example illustrates the result of serializing
> the canonicalized dataset described in Example 2.
>
> ```
> <http://example.com/p> <http://example.com/q> _:c14n0 .
> <http://example.com/p> <http://example.com/r> _:c14n1 .
> _:c14n0 <http://example.com/s> <http://example.com/u> .
> _:c14n1 <http://example.com/t> <http://example.com/u> .
> ```

## 6. Privacy Considerations

*This section is non-normative.*

The nature of the canonicalization algorithm inherently correlates its output,
i.e., the canonical labels and the sorted order of quads, with the input dataset.
This could pose issues, particularly when dealing with datasets containing personal information.
For example, even if certain information is removed from the canonicalized dataset for some privacy-respecting reason, there remains the possibility that a third party
could infer the omitted data by analyzing the canonicalized dataset.
If it is necessary to decouple the canonicalization algorithm's input and output,
some suitable post-processing methods for the output of the canonicalization should be performed.
This specification has been designed to help make additional processing easier, but
other specifications that build on top of this one are responsible for providing any
specific details.
See [Selective Disclosure](https://www.w3.org/TR/vc-data-integrity/#selective-disclosure) in [Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/) [VC-DATA-INTEGRITY] for more details about such
post-processing methods.

## 7. Security Considerations

*This section is non-normative.*

### 7.1 Dataset Poisoning

*This section is non-normative.*

The canonicalization algorithm examines every difference in the
information connected to blank nodes in order to ensure that each will
properly receive its own canonical identifier. This process can be
exploited by attackers to construct datasets which are known to take
large amounts of computing time to canonicalize, but that do not express
useful information or express it using unnecessary complexity.
Implementers of the algorithm are expected to add mitigations that will,
by default, abort canonicalizing problematic inputs.

Suggested mitigations include, but are not limited to:

- providing a configurable timeout with a default value applicable to
  an implementation's common use
- providing a configurable limit on the number of iterations of steps
  performed in the algorithm, particularly recursive steps
  and permutations of long lists

Additionally, software that uses implementations of the algorithm can
employ best-practice schema validation to reject data that does not meet
application requirements, thereby preventing useless poison datasets from
being processed. However, such mitigations are application specific and
not directly applicable to implementers of the canonicalization algorithm
itself.

### 7.2 Insecure Hash Algorithms

*This section is non-normative.*

It is possible that the default hash algorithm used by RDFC-1.0 might become
insecure at some point in the future. To mitigate this, this algorithm
and implementations of it can be parameterized to use a different
hash function, without the need to make any changes to the
canonicalization algorithm itself.
However, using a different hash algorithm will generally lead to different results;
applications making use of this specification should carefully weigh the advantages
and disadvantages of using an alternative hash function.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The possible implications of the default hash algorithm
> becoming insecure are mitigated by that fact that no internal hash
> values are revealed, and the canonicalization algorithm is designed to cope
> with first-degree hash collisions.

## 8. Use Cases

*This section is non-normative.*

The use cases that have driven the development of the RDF Dataset Canonicalization algorithm are documented in a separate document. It includes further background and explanations for the design decisions taken [RCH-EXPLAINER].

## 9. Examples

*This section is non-normative.*

### 9.1 Duplicate Paths

This example illustrates a more complicated example where the same paths
through blank nodes are duplicated in a graph, but use different [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).

*Figure 7 An illustration of a graph with duplicated paths.
Image available in [SVG](https://www.w3.org/TR/rdf-canon/duplicate-paths.svg "SVG image of duplicated paths") .*

```
_:e0 :p1 _:e1 .
_:e1 :p2 "Foo" .
_:e2 :p1 _:e3 .
_:e3 :p2 "Foo" .
```

The following is a summary of the more detailed execution log
found [here](https://www.w3.org/TR/rdf-canon/duplicate-paths.yml).
> **Example:**
>
> Example 9: Duplicate Paths
>
> Step 2 of the Canonicalization Algorithm (§4.4.3) is called four times, with each blank node
> (`e0`, `e1`, `e2`, and `e3`)
> to populate blank node to quads map:
>
> *Table 19 Blank node to quads map for duplicate paths*
>
> | *blank node* | *Q*                                |
> | ------------ | ---------------------------------- |
> | `e0`         | `_:e0 :p1 _:e1 .`                  |
> | `e1`         | `_:e0 :p1 _:e1 . _:e1 :p2 "Foo" .` |
> | `e2`         | `_:e2 :p1 _:e3 .`                  |
> | `e3`         | `_:e2 :p1 _:e3 . _:e3 :p2 "Foo" .` |
> Step 3 generates the first-degree
> hash for each blank node.
>
> For `e0`, the Hash First Degree Quads algorithm uses the nquad `_:a :p1 _:z .` to calculate the hash `24da9a4406b4e66dffa10ad3d4d6dddc388fbf193bb124e865158ef419893957`.
>
> For `e1`, the Hash First Degree Quads algorithm uses the nquads `_:z :p1 _:a .` and `_:a :p2 "Foo" .` to calculate the hash `a994e40b576809985bc0f389308cd9d552fd7c89d028c163848a6b2d33a8583a`.
>
> For `e2`, the Hash First Degree Quads algorithm uses the nquad `_:a :p1 _:z .` to calculate the hash `24da9a4406b4e66dffa10ad3d4d6dddc388fbf193bb124e865158ef419893957`.
>
> For `e3`, the Hash First Degree Quads algorithm uses the nquads `_:z :p1 _:a .` and `_:a :p2 "Foo" .` to calculate the hash `a994e40b576809985bc0f389308cd9d552fd7c89d028c163848a6b2d33a8583a`.
>
> *Table 20 Hash to blank nodes map shared hashes*
>
> | *hash*                                                             | *blank node(s)* |
> | ------------------------------------------------------------------ | --------------- |
> | `24da9a4406b4e66dffa10ad3d4d6dddc388fbf193bb124e865158ef419893957` | `e0` and `e2`   |
> | `a994e40b576809985bc0f389308cd9d552fd7c89d028c163848a6b2d33a8583a` | `e1` and `e3`   |
> Step 4 would create canonical identifiers for each
> blank node which has a unique hash, but no blank node has a unique hash.
>
> Step 5 is run on `e0`, `e1`, `e2`, and `e3`, separately,
> which share hash values.
> each use separate instances of a *temporary issuer*,
> to create the *hash path list* composed of the hash result
> and temporary identifier mappings from Hash N-Degree Quads algorithm (§4.8) for each of these blank nodes/
>
> The Hash N-Degree Quads algorithm (§4.8) is first
> called for hash `24da9a4406b4e66dffa10ad3d4d6dddc388fbf193bb124e865158ef419893957` and blank node `e0` related to
> the nquad `_:e0 :p1 _:e1 .`.
>
> | *blank node* | *temporary identifier* |
> | ------------ | ---------------------- |
> | `e0`         | `b0`                   |
> Step 3 calls the Hash Related Blank Node algorithm (§4.7) for each position in this quad:
>
> *Table 21 Hash for `e2` related to `e0`*
>
> | *related* | *quads*                     | *position* | *hash*                    |
> | --------- | --------------------------- | ---------- | ------------------------- |
> | `e3`      | `z :p1 a .` `a :p2 "Foo" .` | `o`        | `a994e40b57...2d33a8583a` |
> which results in the following *Hn*:
>
> *Table 22 Blank node list for hash*
>
> | *related hash*                                                     | *blank node list* |
> | ------------------------------------------------------------------ | ----------------- |
> | `a994e40b576809985bc0f389308cd9d552fd7c89d028c163848a6b2d33a8583a` | `[ e3 ]`          |
> Step 5 iterates over each *related hash* which is a key in *Hn*,
> which can have one or more related blank nodes.
>
> At Step 5.4.5, the *recursion list* is `[ e3 ]`,
> so the Hash N-Degree Quads algorithm (§4.8) is
> called recursively resulting in the following:
>
> *Table 23 Result for `e3`*
>
> | *temporary issuer* mappings | *original identifier* *temporary identifier* `e2` `b0` `e3` `b1`   |
> | --------------------------- | ------------------------------------------------------------------ |
> | *hash*                      | `c484f98e6cbf9e21f287433c8b1caa7f1486fd61d84ab220a494bf8184751b8c` |
> Back in step 5.4.5.4, the *path* and *issuer copy* are: `_:b1_:b1<c484f98e6cbf9e21f287433c8b1caa7f1486fd61d84ab220a494bf8184751b8c>` and `{e2: b0, e3: b1}`.
>
> This results in the *chosen path* `_:b1_:b1<c484f98e6cbf9e21f287433c8b1caa7f1486fd61d84ab220a494bf8184751b8c>` and *data to hash* `3d96946f27fc34a78e8d067135a1cb1b77083aebc4b2c6cbdc536f067242686c_:b1_:b1<c484f98e6cbf9e21f287433c8b1caa7f1486fd61d84ab220a494bf8184751b8c>`
>
> *Table 24 Result for `e2`*
>
> | *temporary issuer* mappings | *original identifier* *temporary identifier* `e2` `b0` `e3` `b1`   |
> | --------------------------- | ------------------------------------------------------------------ |
> | *hash*                      | `39d609fcd8236b74c70744f492cd2baaf0a55765b380ff9e0811ce23e2f409d7` |
> The Hash N-Degree Quads algorithm (§4.8) is next
> called for the same hash `24da9a4406b4e66dffa10ad3d4d6dddc388fbf193bb124e865158ef419893957` but this time with blank node `e2` related to
> the nquad `_:e2 :p1 _:e3 .`.
>
> | *blank node* | *temporary identifier* |
> | ------------ | ---------------------- |
> | `e2`         | `b0`                   |
> Step 3 calls the Hash Related Blank Node algorithm (§4.7) for each position in this quad:
>
> *Table 25 Hash for `e2` related to `e0`*
>
> | *related* | *quads*                     | *position* | *hash*                   |
> | --------- | --------------------------- | ---------- | ------------------------ |
> | `e3`      | `z :p1 a .` `a :p2 "Foo" .` | `o`        | `3d96946f27...184751b8c` |
> which results in the following *Hn*:
>
> *Table 26 Blank node list for hash*
>
> | *related hash*                                                     | *blank node list* |
> | ------------------------------------------------------------------ | ----------------- |
> | `3d96946f27fc34a78e8d067135a1cb1b77083aebc4b2c6cbdc536f067242686c` | `[ e3 ]`          |
> Step 5 iterates over each *related hash* which is a key in *Hn*,
> which can have one or more related blank nodes.
>
> *Table 27 Result for `e0`*
>
> | *temporary issuer* mappings | *original identifier* *temporary identifier* `e0` `b0`             |
> | --------------------------- | ------------------------------------------------------------------ |
> | *hash*                      | `fbc300de5afafd97a4b9ee1e72b57754dcdcb7ebb724789ac6a94a5b82a48d30` |
> Step 5.3 back in the Canonicalization Algorithm (§4.4.3) creates canonical identifiers for the temporary identifiers just issued:
>
> | *blank node* | *canonical identifier* |
> | ------------ | ---------------------- |
> | `e0`         | `c14n0`                |
> | `e1`         | `c14n1`                |
> | `e2`         | `c14n2`                |
> | `e3`         | `c14n3`                |
> Next, back in step 5.1,
> now using hash `a994e40b576809985bc0f389308cd9d552fd7c89d028c163848a6b2d33a8583a`,
> canonical identifiers have already been created for the
> two blank nodes `e1` and `e3`,
> so no further processing is necessary.
>
> Step 6 ends with the issued identifiers map containing the following mappings:
>
> | *blank node* | *canonical identifier* |
> | ------------ | ---------------------- |
> | `e0`         | `c14n0`                |
> | `e1`         | `c14n1`                |
> | `e2`         | `c14n2`                |
> | `e3`         | `c14n3`                |

### 9.2 Double Circle

This example illustrates another complicated example of
nodes that are doubly connected in opposite directions.

*Figure 8 An illustration of a graph back and forth links to nodes.
Image available in [SVG](https://www.w3.org/TR/rdf-canon/double-circle.svg "SVG image of double circle") .*

```
_:e0 :next _:e1 .
_:e0 :prev _:e1 .
_:e1 :next _:e0 .
_:e1 :prev _:e0 .
```

The example is not explored in detail, but the
execution log found [here](https://www.w3.org/TR/rdf-canon/double-circle.yml) shows examples of more complicated
pathways through the algorithm

### 9.3 Dataset with Blank Node Named Graph

This example illustrates an example of a [dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset),
where one graph is named using a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node),
which is also the object of a triple in the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph).

*Figure 9 An illustration of a dataset containing a graph named with a blank node.
Image available in [SVG](https://www.w3.org/TR/rdf-canon/dataset-bn-graph.svg "SVG image of dataset containg a graph named with a blank node") .*

```
_:e0 :p1 _:e1 .
_:e1 :p2 "Foo" .
_:e1 :p3 _:g0 .
_:e0 :p1 _:e1 _:g0 .
_:e1 :p2 "Bar" _:g0 .
```

The following is a summary of the more detailed execution log
found [here](https://www.w3.org/TR/rdf-canon/dataset-bn-graph.yml).
> **Example:**
>
> Example 10: Dataset Blank Node Graph
>
> Step 2 of the Canonicalization Algorithm (§4.4.3) is called three times, with each blank node
> (`e0`, `e1`, and `g0`)
> to populate blank node to quads map:
>
> *Table 28 Blank node to quads map for dataset with blank node named graph*
>
> | *blank node* | *Q*                                    |
> | ------------ | -------------------------------------- |
> | `e0`         | `_:e0 :p1 _:e1 . _:e0 :p1 _:e1 _:g0 .` |
> | `e1`         | `_:e0 :p1 _:e1 . _:e1 :p2 "Foo" .`     |
> | `g0`         | `_:e1 :p3 _:g0 . _:e0 :p1 _:e1 _:g0 .` |
> Step 3 generates the first-degree
> hash for each blank node.
>
> For `e0`, the Hash First Degree Quads algorithm uses the nquads `_:a :p1 _:z .` and `_:a :p1 _:z _:z .`to calculate the hash `39fa92e7a9ea0b32e3e08aedebc1cbbcd9ba9945a18f2594677598fcfb517345`.
>
> For `e1`, the Hash First Degree Quads algorithm uses the nquads `_:z :p1 _:a .`, `_:a :p2 "Foo" .`, `_:a :p3 _:z .`, `_:z :p1 _:a _:z .`, and `_:a :p2 "Bar" _:z .` to calculate the hash `5274652aa97d22f9f2998d1837ffaf9ad820fb813574adc4a403f105021e48bf`.
>
> For `g0`, the Hash First Degree Quads algorithm uses the nquads `_:z :p3 _:a .`, `_:z :p1 _:z _:a .`, and `_:z :p2 "Bar" _:a .` to calculate the hash `efb0096125247801199082c6f213cda5377d8ddac20a83eaf6c7d88335c12bf4`.
>
> *Table 29 Hash to blank nodes map shared hashes*
>
> | *hash*                                                             | *blank node(s)* |
> | ------------------------------------------------------------------ | --------------- |
> | `39fa92e7a9ea0b32e3e08aedebc1cbbcd9ba9945a18f2594677598fcfb517345` | `e0`            |
> | `5274652aa97d22f9f2998d1837ffaf9ad820fb813574adc4a403f105021e48bf` | `e1`            |
> | `efb0096125247801199082c6f213cda5377d8ddac20a83eaf6c7d88335c12bf4` | `g0`            |
> Step 4 creates canonical identifiers for each
> blank node which has a unique hash:
>
> *Table 30 Canonical identifiers for dataset with blank node named graph*
>
> | *blank node* | *canonical identifier* |
> | ------------ | ---------------------- |
> | `e0`         | `c14n0`                |
> | `e1`         | `c14n1`                |
> | `g0`         | `c14n2`                |
> Step 5 has no effect,
> as there are no remaining blank nodes without canonical identifiers.
>
> Step 6 ends with the canonical issuers containing the following mappings:
>
> | *blank node* | *canonical identifier* |
> | ------------ | ---------------------- |
> | `e0`         | `c14n0`                |
> | `e1`         | `c14n1`                |
> | `g0`         | `c14n2`                |

## A. A Canonical form of N-Quads

This section defines a canonical form of N-Quads which has
a completely specified layout.
The grammar for the language remains unchanged.

Canonical N-Quads updates and extends [Canonical N-Triples](https://www.w3.org/TR/n-triples/#canonical-ntriples) in [N-TRIPLES]
to include `graphLabel`.

While the N-Quads syntax [N-QUADS] allows choices for the representation and layout of RDF data,
the canonical form of N-Quads provides a unique syntactic representation of any quad.
Each code point
can be represented by only one of `UCHAR`, `ECHAR`,
or unencoded character,
where the relevant production allows for a choice in representation.
Each quad is represented entirely on a single line with specified white space.

Canonical N-Quads has the following additional constraints on layout:

- White space *MUST NOT* be used except after `subject`, `predicate`, `object`,
  and `graphLabel`,
  each of which *MUST* be a single space (code point `U+0020`).
- [Literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) with the
  datatype `http://www.w3.org/2001/XMLSchema#string` *MUST NOT* use the datatype IRI part of the [literal](https://www.w3.org/TR/n-quads/#grammar-production-literal),
  and are represented using only [STRING_LITERAL_QUOTE](https://www.w3.org/TR/n-quads/#grammar-production-STRING_LITERAL_QUOTE).
- `HEX` *MUST* use only digits (`[0-9]`) and uppercase letters (`[A-F]`).
- Within [STRING_LITERAL_QUOTE](https://www.w3.org/TR/n-quads/#grammar-production-STRING_LITERAL_QUOTE):
  * Characters `BS` (backspace, code point `U+0008`), `HT` (horizontal tab, code point `U+0009`), `LF` (line feed, code point `U+000A`), `FF` (form feed, code point `U+000C`), `CR` (carriage return, code point `U+000D`), `"` (quotation mark, code point `U+0022`), and `\` (backslash, code point `U+005C`) *MUST* be encoded using `ECHAR`.
  * Characters in the range from `U+0000` to `U+0007`, `VT` (vertical tab, code point `U+000B`),
    characters in the range from `U+000E` to `U+001F`, `DEL` (delete, code point `U+007F`),
    and characters not matching the [Char](https://www.w3.org/TR/xml11/#charsets) production from [XML11] *MUST* be represented by `UCHAR` using a lowercase `\u` with 4 `HEX`es.
  * All characters not required to be represented by `ECHAR` or `UCHAR` *MUST* be represented by their native [UNICODE] representation.
- The token `EOL` *MUST* be a single `LF` (line feed, code point `U+000A`).
- The final `EOL` *MUST* be provided.

## B. URDNA2015

*This section is non-normative.*

[RDF Dataset Canonicalization](https://www.w3.org/community/reports/credentials/CG-FINAL-rdf-dataset-canonicalization-20221009/) [CCG-RDC-FINAL] describes
"Universal RDF Dataset Normalization Algorithm 2015"
(*URDNA2015*),
essentially the same algorithm
as RDFC-1.0, and generally implementations implementing URDNA2015 should be compatible with this specification.
The minor change is in the canonical n-quads form where
some control characters were previously represented without escaping.
The version of the algorithm defined in A. A Canonical form of N-Quads (§A) clarifies the representation of [simple literals](https://www.w3.org/TR/rdf11-concepts/#dfn-simple-literal) and the characters
within [STRING_LITERAL_QUOTE](https://www.w3.org/TR/n-quads/#grammar-production-STRING_LITERAL_QUOTE) that are encoded using `ECHAR`.

## C. URGNA2012

*This section is non-normative.*

A previous version of this algorithm has light deployment. For purposes of identification,
the algorithm is called the
"Universal RDF Graph Canonicalization Algorithm 2012"
(*URGNA2012*),
and differs from the stated algorithm in the following ways:

- In 4.6 Hash First Degree Quads (§4.6), if any blank node was used in the [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name) position in the quad, then the value was serialized using
  the special [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), `g`, instead of `z`.
- In 4.7 Hash Related Blank Node (§4.7), value of the [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate) was not delimited by `<` and `>`; there
  were no delimiters.
- In 4.8 Hash N-Degree Quads (§4.8), the *position* parameter passed to
  the Hash Related Blank Node algorithm (§4.7) was instead modeled as a *direction* parameter, where it could have
  the value `p`, for property, when the related blank node was a [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) and the value `r`, for reverse or reference, when
  the related blank node was an [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object). Since URGNA2012 only canonicalized
  graphs, not datasets, there was no use of the [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name) position.
- In 4.8 Hash N-Degree Quads (§4.8), building the *Hn* was done as follows:
  1. For each *quad* in *quads*:
     1. If the *quad*'s [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) is a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) that does not
        match *identifier*, set *hash* to the result of the Hash Related Blank Node algorithm (§4.7),
        passing the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) for [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) as *related*, *quad*, *issuer*, and `p` as *position*.
     2. Otherwise, if *quad*'s [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) is a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) that does
        not match *identifier*, set *hash* to the result of the Hash Related Blank Node algorithm (§4.7),
        passing the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) for [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) as *related*, *quad*, *issuer*, and `r` as *position*.
     3. Otherwise, continue to the next quad.
     4. Add a mapping of *hash* to the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) for the component
        that matched ([subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) or [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object)) to *Hn*, adding an entry
        as necessary.

## D. Index

### D.1 Terms defined by this specification

- blank node to quads map §4.2
- canonical issuer §4.2
- canonical n-quads form §3.1
- canonicalization function §3.1
- canonicalization state §4.2
- canonicalized dataset §3.1
- definition §1.3
- gossip path §3.1
- graph isomorphism §1.
- hash §3.1
- hash algorithm §3.1
- hash to blank nodes map §4.2
- identifier counter §4.3
- identifier issuer §3.1
- identifier prefix §4.3
- input blank node identifier map §3.1
- input dataset §3.1
- issued identifiers map §4.3
- mention §3.1
- mention set §3.1
- nquads §4.6.3
- partial canonicalization function §3.1
- quad §3.1
- RDFC-1.0 §4.
- reference blank node identifier §4.6.3
- serialized canonical form §5.
- URDNA2015 §B.
- URGNA2012 §C.

### D.2 Terms defined by reference

- [BCP47] defines the following:
  * formatting conventions
- [INFRA] defines the following:
  * boolean type
  * entry (for `map`)
  * key (for `map`)
  * list
  * map
  * string
- [N-QUADS] defines the following:
  * C. N-Quads Internet Media Type, File Extension and Macintosh File Type
  * ECHAR
  * EOL
  * graphLabel
  * HEX
  * literal
  * STRING_LITERAL_QUOTE
  * UCHAR
- [N-TRIPLES] defines the following:
  * Canonical N-Triples
- [RDF11-CONCEPTS] defines the following:
  * blank node identifiers
  * blank nodes
  * Blank Nodes
  * default graph
  * graph name
  * IRIs
  * isomorphic datasets
  * language tags
  * language-tagged strings
  * lexical form
  * literal
  * literal term equality
  * literal value
  * object type
  * predicate
  * RDF datasets
  * RDF graph
  * RDF source
  * RDF triple
  * Section 3.3
  * simple literals
  * Skolem IRIs
  * subject
- [RDF11-MT] defines the following:
  * RDF Collections
- [VC-DATA-INTEGRITY] defines the following:
  * Selective Disclosure
- [XML11] defines the following:
  * Char
- [XPATH-FUNCTIONS] defines the following:
  * Unicode code point order

## E. Changes since the First Public Working Draft of 24 November 2022

*This section is non-normative.*

- The algorithm, and the examples, have been changed to systematically
  use the `xyz` format for blank node identifiers, instead of `_:xyz`. See [Issue 46](https://github.com/w3c/rdf-canon/issues/46) for the discussion.
- 4.6 Hash First Degree Quads (§4.6) was simplified to remove the `simple` flag,
  which was unused in existing implementations.
  The original design of the algorithm was to use the
  assigned canonical [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier),
  if available, instead of `_:a` or `_:z`,
  similar to how it is used in
  the related hash algorithm, but this text never made it into the spec
  before implementations moved forward.
  Therefore, the hashes never change,
  making the loop based on the `simple` flag that calls this algorithm unnecessary.
  See [Issue 23](https://github.com/w3c/rdf-canon/issues/23) for the discussion.
- Add definition for canonical n-quads form. Eventually, this should
  be a citation from [N-Quads], when it is updated. Canonical n-quads form is used in 4.6 Hash First Degree Quads (§4.6).
- Removed issue marker for [Issue 15](https://github.com/w3c/rdf-canon/issues/15) in 4.4 Canonicalization Algorithm (§4.4),
  adding a note that [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) components of quads are not normalized,
  and two literals with different syntactic representations
  remain distinct resources.
- Changed the way Blank Node identifiers are described
  (see [Issue 46](https://github.com/w3c/rdf-canon/issues/46)),
  generally omitting the leading `_:` which is a serialization artifact.
  This is still required in the algorithms, but the distinction
  between what is an identifier, and the serialization form
  is clarified.
- Changed the name of the algorithm from URDNA2015 to RDFC-1.0.
- Changed the term **normalized dataset** to canonicalized dataset,
  which is composed of the input dataset, input blank node identifier map, and issued identifiers map.

## F. Changes since the Candidate Recommentation Snapshot of 31 October 2023

*This section is non-normative.*

- Clarified that detecting a poison dataset will result in an exception and early
  termination of the Canonicalization Algorithm (§4.4.3).

## H. References

### H.1 Normative references

[FIPS-180-4]

[FIPS PUB 180-4: Secure Hash Standard (SHS)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf). U.S. Department of Commerce/National Institute of Standards and Technology. August 2015. National Standard. URL: <https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf>

[INFRA]

[Infra Standard](https://infra.spec.whatwg.org/). Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: <https://infra.spec.whatwg.org/>

[N-Quads]

[RDF 1.1 N-Quads](https://www.w3.org/TR/n-quads/). Gavin Carothers. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/n-quads/>

[N-TRIPLES]

[RDF 1.1 N-Triples](https://www.w3.org/TR/n-triples/). Gavin Carothers; Andy Seaborne. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/n-triples/>

[RDF11-CONCEPTS]

[RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). Richard Cyganiak; David Wood; Markus Lanthaler. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf11-concepts/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

[RFC3987]

[Internationalized Resource Identifiers (IRIs)](https://www.rfc-editor.org/rfc/rfc3987). M. Duerst; M. Suignard. IETF. January 2005. Proposed Standard. URL: <https://www.rfc-editor.org/rfc/rfc3987>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

[Turtle]

[RDF 1.1 Turtle](https://www.w3.org/TR/turtle/). Eric Prud'hommeaux; Gavin Carothers. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/turtle/>

[UNICODE]

[The Unicode Standard](https://www.unicode.org/versions/latest/). Unicode Consortium. URL: <https://www.unicode.org/versions/latest/>

[XML11]

[Extensible Markup Language (XML) 1.1 (Second Edition)](https://www.w3.org/TR/xml11/). Tim Bray; Jean Paoli; Michael Sperberg-McQueen; Eve Maler; François Yergeau; John Cowan et al. W3C. 16 August 2006. W3C Recommendation. URL: <https://www.w3.org/TR/xml11/>

[XPATH-FUNCTIONS]

[XQuery 1.0 and XPath 2.0 Functions and Operators (Second Edition)](https://www.w3.org/TR/xpath-functions/). Ashok Malhotra; Jim Melton; Norman Walsh; Michael Kay. W3C. 14 December 2010. W3C Recommendation. URL: <https://www.w3.org/TR/xpath-functions/>

### H.2 Informative references

[BCP47]

[Tags for Identifying Languages](https://www.rfc-editor.org/rfc/rfc5646). A. Phillips, Ed.; M. Davis, Ed.. IETF. September 2009. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc5646>

[CCG-RDC-FINAL]

[RDF Dataset Canonicalization](https://www.w3.org/community/reports/credentials/CG-FINAL-rdf-dataset-canonicalization-20221009/). Dave Longley. W3C. October 9, 2022. CG-FINAL. URL: <https://www.w3.org/community/reports/credentials/CG-FINAL-rdf-dataset-canonicalization-20221009/>

[DesignIssues-Diff]

[Delta: an ontology for the distribution of differences between RDF graphs](https://www.w3.org/DesignIssues/Diff). Tim Berners-Leee. W3C. September 25, 2015. unofficial. URL: <https://www.w3.org/DesignIssues/Diff>

[eswc2014Kasten]

[A Framework for Iterative Signing of Graph Data on the Web](https://doi.org/10.1007/978-3-319-07443-6_11). Andreas Kasten; Ansgar Scherp; Peter Schauß . ISWC 2014. 2014. unofficial. URL: <https://doi.org/10.1007/978-3-319-07443-6_11>

[Hogan-Canonical-RDF]

[Canonical Forms for Isomorphic and Equivalent RDF Graphs: Algorithms for Leaning and Labelling Blank Nodes](https://aidanhogan.com/docs/rdf-canonicalisation.pdf). Aiden Hogan. ACM. November 2017. ACM Trans. Web 11, 4, Article 22. URL: <https://aidanhogan.com/docs/rdf-canonicalisation.pdf>

[HPL-2003-142]

[Signing RDF Graphs](https://web.archive.org/web/20230129125726/https://www.hpl.hp.com/techreports/2003/HPL-2003-142.pdf). Jeremy J. Carroll. HP Laboratories Bristol. July 23, 2003. unofficial. URL: <https://web.archive.org/web/20230129125726/https://www.hpl.hp.com/techreports/2003/HPL-2003-142.pdf>

[RCH-EXPLAINER]

[RDF Dataset Canonicalization and Hash Working Group — Explainer and Use Cases](https://www.w3.org/TR/rch-explainer/). Phil Archer. W3C. 19 October 2023. W3C Working Group Note. URL: <https://www.w3.org/TR/rch-explainer/>

[RDF11-MT]

[RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/). Patrick Hayes; Peter Patel-Schneider. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf11-mt/>

[VC-DATA-INTEGRITY]

[Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/). Manu Sporny; Dave Longley; Greg Bernstein; Dmitri Zagidulin; Sebastian Crane. W3C. 28 April 2024. W3C Candidate Recommendation. URL: <https://www.w3.org/TR/vc-data-integrity/>

[YAML]

[YAML Ain’t Markup Language (YAML™) Version 1.2](http://yaml.org/spec/1.2/spec.html). Oren Ben-Kiki; Clark Evans; Ingy döt Net. 1 October 2009. URL: <http://yaml.org/spec/1.2/spec.html>

Permalink

**Referenced in:**

- § 4.8.1 Overview

Permalink

**Referenced in:**

- § 1.3 Typographical conventions (2)

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization (2)
- § 2. Conformance
- § 3.1 Terms defined by this specification
- § 4.6.1 Overview
- § 4.6.2 Examples (2)
- § 4.6.3 Algorithm (2)
- § 5. Serialization (2)
- § B. URDNA2015
- § E. Changes since the First Public Working Draft of 24 November 2022 (2)

Permalink exported

**Referenced in:**

- § 3.1 Terms defined by this specification (2)

Permalink exported

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization (2)
- § 3.1 Terms defined by this specification (2)
- § 4. Canonicalization
- § 4.4 Canonicalization Algorithm
- § 4.4.1 Overview (2) (3)
- § 4.4.2 Examples
- § 4.4.3 Algorithm (2) (3) (4) (5) (6) (7)
- § 5. Serialization (2) (3) (4) (5)
- § 6. Privacy Considerations
- § E. Changes since the First Public Working Draft of 24 November 2022

Permalink

**Referenced in:**

- § 4.8 Hash N-Degree Quads
- § 4.8.1 Overview (2) (3) (4) (5) (6)
- § 4.8.2 Examples
- § 4.8.3 Algorithm

Permalink

**Referenced in:**

- § 4.1 Overview
- § 4.2 Canonicalization State (2) (3)
- § 4.4.3 Algorithm
- § 4.6 Hash First Degree Quads
- § 4.6.1 Overview
- § 4.6.3 Algorithm
- § 4.7 Hash Related Blank Node
- § 4.7.3 Algorithm (2)
- § 4.8 Hash N-Degree Quads
- § 4.8.1 Overview (2) (3) (4)
- § 4.8.3 Algorithm (2) (3)

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization
- § 3.1 Terms defined by this specification
- § 4.6.2 Examples
- § 4.6.3 Algorithm
- § 4.7.3 Algorithm
- § 4.8.3 Algorithm (2)
- § 7.2 Insecure Hash Algorithms

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification
- § 4.2 Canonicalization State
- § 4.3 Blank Node Identifier Issuer State (2)
- § 4.4.3 Algorithm
- § 4.5.2 Algorithm
- § 4.7.3 Algorithm
- § 4.8.2 Examples
- § 4.8.3 Algorithm (2) (3)

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification
- § 4.4.1 Overview (2)
- § 4.4.3 Algorithm (2) (3) (4) (5) (6) (7)
- § E. Changes since the First Public Working Draft of 24 November 2022

Permalink

**Referenced in:**

- § 2. Conformance
- § 3.1 Terms defined by this specification (2) (3) (4)
- § 4. Canonicalization (2)
- § 4.2 Canonicalization State
- § 4.4 Canonicalization Algorithm (2)
- § 4.4.1 Overview
- § 4.4.2 Examples
- § 4.4.3 Algorithm (2) (3) (4) (5) (6)
- § 4.5.1 Overview
- § E. Changes since the First Public Working Draft of 24 November 2022

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification (2) (3)
- § 4.1 Overview
- § 4.4.2 Examples
- § 4.6.2 Examples (2) (3)
- § 4.8.1 Overview (2) (3) (4)

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification
- § 4.6.1 Overview
- § 4.7 Hash Related Blank Node
- § 4.8 Hash N-Degree Quads
- § 4.8.3 Algorithm (2) (3)

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification (2)
- § 3.2 Terms defined by cited specifications (2)
- § 4.2 Canonicalization State
- § 4.4.1 Overview
- § 4.4.3 Algorithm (2) (3)
- § 4.6 Hash First Degree Quads
- § 4.6.3 Algorithm (2) (3)
- § 4.7 Hash Related Blank Node
- § 4.7.1 Overview
- § 4.7.3 Algorithm
- § 4.8 Hash N-Degree Quads
- § 4.8.3 Algorithm (2)
- § 5. Serialization
- § C. URGNA2012
- § E. Changes since the First Public Working Draft of 24 November 2022

Permalink exported

**Referenced in:**

- § Status of This Document
- § 1. Introduction (2)
- § 3.1 Terms defined by this specification (2) (3)
- § 4. Canonicalization (2) (3)
- § 4.1 Overview (2)
- § 4.4.1 Overview (2) (3)
- § B. URDNA2015
- § E. Changes since the First Public Working Draft of 24 November 2022
- § G. Acknowledgements

Permalink

**Referenced in:**

- § 4.2 Canonicalization State
- § 4.4.3 Algorithm (2)
- § 4.6.3 Algorithm
- § 4.7.1 Overview
- § 4.7.3 Algorithm (2)
- § 4.8.3 Algorithm (2)

Permalink

**Referenced in:**

- § 4.4.2 Examples (2)
- § 4.4.3 Algorithm (2) (3) (4) (5)
- § 4.6.3 Algorithm
- § 4.8.2 Examples (2)
- § 4.8.3 Algorithm
- § 9.1 Duplicate Paths
- § 9.3 Dataset with Blank Node Named Graph

Permalink

**Referenced in:**

- § 4.4.3 Algorithm (2) (3) (4) (5) (6)

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification
- § 4.4.1 Overview
- § 4.4.2 Examples (2)
- § 4.4.3 Algorithm (2) (3) (4) (5) (6) (7) (8) (9) (10)
- § 4.7.1 Overview
- § 4.7.2 Examples
- § 4.7.3 Algorithm
- § 4.8.2 Examples
- § 4.8.3 Algorithm

Permalink

**Referenced in:**

- § 4.3 Blank Node Identifier Issuer State (2)
- § 4.5.1 Overview
- § 4.5.2 Algorithm

Permalink

**Referenced in:**

- § 4.3 Blank Node Identifier Issuer State
- § 4.5.2 Algorithm (2)

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization
- § 3.1 Terms defined by this specification
- § 4.4.1 Overview (2)
- § 4.4.2 Examples
- § 4.4.3 Algorithm (2) (3) (4) (5)
- § 4.5.1 Overview
- § 4.5.2 Algorithm (2)
- § 5. Serialization
- § E. Changes since the First Public Working Draft of 24 November 2022

Permalink

**Referenced in:**

- § 4.6.3 Algorithm (2)

Permalink

**Referenced in:**

- § 4.6.3 Algorithm (2)
- § 4.7.3 Algorithm (2)
- § 4.8.3 Algorithm (2)

Permalink

**Referenced in:**

- § 4. Canonicalization (2)
- § 4.4.1 Overview
- § 4.4.3 Algorithm (2)

Permalink exported

**Referenced in:**

- Not referenced in this document.

Permalink exported

**Referenced in:**

- § C. URGNA2012

Permalink

**Referenced in:**

- § 1. Introduction

Permalink

**Referenced in:**

- § 3.2 Terms defined by cited specifications

Permalink

**Referenced in:**

- § 4.4.3 Algorithm (2) (3) (4) (5)
- § 4.5.2 Algorithm (2)
- § 4.6.3 Algorithm
- § 4.8.2 Examples (2)
- § 4.8.3 Algorithm

Permalink

**Referenced in:**

- § 4.4.3 Algorithm (2)

Permalink

**Referenced in:**

- § 4.2 Canonicalization State
- § 4.6.3 Algorithm (2)

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification
- § 4.2 Canonicalization State (2)
- § 4.3 Blank Node Identifier Issuer State
- § 4.8.3 Algorithm

Permalink

**Referenced in:**

- § 3.2 Terms defined by cited specifications (2) (3)
- § 4.7.3 Algorithm (2)
- § 4.8.3 Algorithm (2)

Permalink

**Referenced in:**

- § 5. Serialization

Permalink

**Referenced in:**

- § A. A Canonical form of N-Quads (2) (3)
- § B. URDNA2015

Permalink

**Referenced in:**

- § A. A Canonical form of N-Quads (2)

Permalink

**Referenced in:**

- § A. A Canonical form of N-Quads

Permalink

**Referenced in:**

- § A. A Canonical form of N-Quads (2)

Permalink

**Referenced in:**

- § A. A Canonical form of N-Quads

Permalink

**Referenced in:**

- § A. A Canonical form of N-Quads (2)
- § B. URDNA2015

Permalink

**Referenced in:**

- § A. A Canonical form of N-Quads (2) (3)

Permalink

**Referenced in:**

- § A. A Canonical form of N-Quads

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization (2) (3) (4)
- § 3.1 Terms defined by this specification (2) (3)
- § 3.2 Terms defined by cited specifications (2) (3)
- § 4.2 Canonicalization State (2) (3)
- § 4.3 Blank Node Identifier Issuer State (2) (3) (4) (5)
- § 4.4.3 Algorithm (2) (3) (4) (5) (6) (7)
- § 4.5 Issue Identifier Algorithm (2) (3)
- § 4.5.1 Overview (2)
- § 4.6.1 Overview
- § 4.6.3 Algorithm (2) (3)
- § 4.7.2 Examples
- § 4.7.3 Algorithm
- § 4.8.3 Algorithm (2) (3) (4)
- § 9.1 Duplicate Paths
- § C. URGNA2012 (2) (3) (4)
- § E. Changes since the First Public Working Draft of 24 November 2022

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization (2) (3) (4)
- § 3.1 Terms defined by this specification (2)
- § 3.2 Terms defined by cited specifications (2) (3)
- § 4.2 Canonicalization State
- § 4.3 Blank Node Identifier Issuer State (2)
- § 4.4 Canonicalization Algorithm
- § 4.4.1 Overview
- § 4.4.3 Algorithm (2)
- § 4.6 Hash First Degree Quads
- § 4.6.3 Algorithm (2)
- § 4.7 Hash Related Blank Node
- § 4.7.1 Overview
- § 4.7.2 Examples
- § 4.7.3 Algorithm
- § 4.8 Hash N-Degree Quads
- § 4.8.2 Examples (2)
- § 4.8.3 Algorithm (2) (3)
- § 5. Serialization (2)
- § 9.3 Dataset with Blank Node Named Graph
- § C. URGNA2012 (2)

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization

Permalink

**Referenced in:**

- § 3.2 Terms defined by cited specifications (2)
- § 4.4.1 Overview
- § 9.3 Dataset with Blank Node Named Graph

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification (2) (3) (4)
- § 3.2 Terms defined by cited specifications (2)
- § 4.8.3 Algorithm (2)
- § C. URGNA2012 (2)

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization
- § 3.2 Terms defined by cited specifications (2) (3)

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification (2)

Permalink

**Referenced in:**

- § 1. Introduction (2) (3)

Permalink

**Referenced in:**

- § 1. Introduction

Permalink

**Referenced in:**

- § 4.4.3 Algorithm

Permalink

**Referenced in:**

- § 3.2 Terms defined by cited specifications
- § 4.4.3 Algorithm
- § A. A Canonical form of N-Quads
- § E. Changes since the First Public Working Draft of 24 November 2022

Permalink

**Referenced in:**

- § 4.4.3 Algorithm

Permalink

**Referenced in:**

- § 4.4.3 Algorithm

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification (2)
- § 3.2 Terms defined by cited specifications (2)
- § 4.7.2 Examples
- § 4.8.3 Algorithm (2)
- § C. URGNA2012 (2) (3) (4)

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification (2)
- § 3.2 Terms defined by cited specifications (2)
- § 4.7.3 Algorithm
- § C. URGNA2012

Permalink

**Referenced in:**

- § Abstract
- § Status of This Document
- § 1. Introduction (2) (3) (4)
- § 1.2 How to Read this Document (2)
- § 3.1 Terms defined by this specification (2) (3) (4)
- § 3.2 Terms defined by cited specifications (2) (3)
- § 4.2 Canonicalization State
- § 4.4.1 Overview
- § 4.6 Hash First Degree Quads
- § 4.8 Hash N-Degree Quads
- § 9.3 Dataset with Blank Node Named Graph

Permalink

**Referenced in:**

- § 3.2 Terms defined by cited specifications (2)
- § 4.2 Canonicalization State

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification
- § 3.2 Terms defined by cited specifications (2)
- § 4.4.1 Overview

Permalink

**Referenced in:**

- § 4.4.3 Algorithm

Permalink

**Referenced in:**

- § B. URDNA2015

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization

Permalink

**Referenced in:**

- § 3.1 Terms defined by this specification (2) (3)
- § 3.2 Terms defined by cited specifications (2)
- § 4.8.3 Algorithm (2)
- § C. URGNA2012 (2) (3) (4)

Permalink

**Referenced in:**

- § 1.1 Uses of Dataset Canonicalization

Permalink

**Referenced in:**

- § 6. Privacy Considerations

Permalink

**Referenced in:**

- § A. A Canonical form of N-Quads

Permalink

**Referenced in:**

- § 3.2 Terms defined by cited specifications (2) (3)
- § 4.4.1 Overview (2) (3)
- § 4.4.3 Algorithm (2) (3)
- § 4.6.1 Overview
- § 4.6.3 Algorithm
- § 4.8.1 Overview
- § 4.8.3 Algorithm (2) (3) (4)
- § 5. Serialization
