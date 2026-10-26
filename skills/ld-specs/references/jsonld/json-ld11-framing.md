---
title: "JSON-LD 1.1 Framing"
source: https://www.w3.org/TR/json-ld-framing/
family: jsonld
version: "1.1"
status: W3C Recommendation
spec_date: 2020-07-16
fetched: 2026-10-26
---

# JSON-LD 1.1 Framing

> Shaping JSON-LD into a desired tree structure.

## Contents

- Abstract
- 1 Introduction
  - 1.1 How to Read this Document
  - 1.2 Contributing
  - 1.3 Typographical conventions
  - 1.4 Terminology
    - Terms imported from Other Specifications
    - JSON-LD Specific Term Definitions
    - 1.4.1 Algorithm Terms
  - 1.5 Syntax Tokens and Keywords
- 2 Features
  - 2.1 Framing
    - 2.1.1 Matching on Properties
    - 2.1.2 Wildcard Matching
    - 2.1.3 Match on the Absence of a Property
    - 2.1.4 Matching on Values
    - 2.1.5 Matching on @id
    - 2.1.6 Empty Frame
  - 2.2 Default content
  - 2.3 Framing Flags
    - 2.3.1 Object Embed Flag
    - 2.3.2 Explicit inclusion flag
    - 2.3.3 Omit default flag
    - 2.3.4 Omit graph flag
    - 2.3.5 Require all flag
  - 2.4 Reverse Framing
  - 2.5 Framing Named Graphs
- 3 Conformance
- 4 Framing
  - 4.1 Framing Algorithm
    - 4.1.1 Overview
    - 4.1.2 Algorithm
  - 4.2 Frame Matching Algorithm
  - 4.3 Value Pattern Matching Algorithm
- 5 The Application Programming Interface
  - 5.1 JsonLdProcessor
  - 5.2 Error Handling
  - 5.3 Data Structures
    - 5.3.1 JsonLdContext
    - 5.3.2 JsonLdOptions
- 6 Security Considerations
- 7 Privacy Considerations
- 8 Internationalization Considerations
- A IANA Considerations
  - application/ld+json
- B IDL Index
- C Open Issues
- D Changes since 1.0 Draft of 30 August 2012
- E Changes since JSON-LD Community Group Final Report
- F Changes since Candidate Release of 12 December 2019
- G Changes since Proposed Recommendation Release of 7 May 2020
- I References
  - I.1 Normative references
  - I.2 Informative references

---

## Abstract

JSON-LD Framing allows developers to query by example and
force a specific tree layout to a JSON-LD document.

This specification describes a superset of the features defined in [JSON-LD Framing 1.0](https://json-ld.org/spec/ED/json-ld-framing/20120830/) [JSON-LD10-FRAMING]
and, except where noted,
the algorithms described in this specification are fully compatible
with documents created using the previous community standard.

## 1. Introduction

*This section is non-normative.*

JSON-LD is a lightweight syntax to serialize Linked Data [LINKED-DATA] in JSON [RFC8259].
Its design allows existing JSON to be interpreted as Linked Data with minimal changes.
As with other representations of Linked Data which describe directed graphs,
a single directed graph can have many different serializations, each expressing
exactly the same information. Developers typically work with trees, represented as [JSON objects](https://tools.ietf.org/html/rfc8259#section-4). While mapping a graph to
a tree can be done, the layout of the end result must be specified in advance.
A Frame can be used by a developer on a JSON-LD document to
specify a deterministic layout for a graph.

Using delimiters around a chunk of data is known as "framing".
JSON-LD uses JSON delimiters such as `{` and `}` to
separate statements about a particular subject. JSON-LD also allows subjects
to reference other subjects through the use of their identifiers, expressed
as strings.

However, given that JSON-LD represents one or more [graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) of information,
there is more than one way to frame the statements about several related
subjects into a whole document. In fact, a graph of information can be
thought of as a long list of independent statements (aka [triples](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple)) that are not bundled together in any way.

The JSON-LD Framing API (§5) enables a developer to specify exactly how they would like data to be framed,
such that statements about a particular subject are bundled together,
delimited via `{` and `}`, and such that the subjects
they relate to "nest" into a particular tree structure that matches what
their application expects.

### 1.1 How to Read this Document

*This section is non-normative.*

This document is a detailed specification for a serialization of Linked
Data in JSON. The document is primarily intended for the following audiences:

- Authors who want to query JSON-LD documents to create representations
  more appropriate for a given use case.
- Software developers that want to implement [processors](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor) and APIs for JSON-LD.

A companion document, the JSON-LD 1.1 specification
[JSON-LD11], specifies the grammar of JSON-LD documents.

To understand the basics in this specification you must first be familiar with [JSON](https://tools.ietf.org/html/rfc8259), which is detailed in [RFC8259].
You must also understand the JSON-LD 1.1 Syntax specification [JSON-LD11],
which is the base syntax used by all of the algorithms in this document,
and the JSON-LD 1.1 API [JSON-LD11-API].
To understand the API and how it is intended to operate in a programming environment,
it is useful to have working knowledge of
the JavaScript programming language [ECMASCRIPT]
and WebIDL [WEBIDL].
To understand how JSON-LD maps to RDF, it is helpful to be
familiar with the basic RDF concepts [RDF11-CONCEPTS].

This document can highlight changes since the [JSON-LD 1.0](https://www.w3.org/TR/2014/REC-json-ld-20140116/) version.
Select to changes.

### 1.2 Contributing

*This section is non-normative.*

There are a number of ways that one may participate in the development of
this specification:

- Technical discussion typically occurs on the public mailing list: [public-json-ld-wg@w3.org](https://lists.w3.org/Archives/Public/public-json-ld-wg/)
- The working group uses [#json-ld](http://irc.w3.org/?channels=json-ld) IRC channel is available for real-time discussion on [irc.w3.org](http://irc.w3.org).
- The [#json-ld](https://webchat.freenode.net/?channels=json-ld) IRC channel is also available for real-time discussion on irc.freenode.net.

### 1.3 Typographical conventions

*This section is non-normative.*

The following typographic conventions are used in this specification:

`markup`

Markup (elements, attributes, properties),
machine processable values (string, characters, media types),
property name,
or a file name is in red-orange monospace font.

*variable*

A variable in pseudo-code or in an algorithm description is in italics.

*definition*

A definition of a term, to be used elsewhere in this or other specifications,
is in bold and italics.

definition reference

A reference to a definition *in this document* is underlined and is also an active link to the definition itself.

`markup definition reference`

A references to a definition *in this document*,
when the reference itself is also a markup, is underlined,
red-orange monospace font, and is also an active link to the definition itself.

external definition reference

A reference to a definition *in another document* is underlined, in italics, and is also an active link to the definition itself.

` markup external definition reference`

A reference to a definition *in another document*,
when the reference itself is also a markup,
is underlined, in italics red-orange monospace font,
and is also an active link to the definition itself.

[hyperlink](https://www.w3.org/TR/json-ld-framing/)

A hyperlink is underlined and in blue.

[[reference](https://www.w3.org/TR/json-ld-framing/)]

A document reference (normative or informative) is enclosed in square brackets
and links to the references section.

Changes from Recommendation

Sections or phrases changed from the previous Recommendation
may be highlighted using a control
in § 1.1 How to Read this Document (§1.1).
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
> Examples are always informative. The content of the example is in monospace font and may be syntax colored.
>
> Examples may have tabbed navigation buttons
> to show the results of transforming an example into other representations.
> ```

### 1.4 Terminology

This document uses the following terms as defined in external specifications
and defines terms specific to JSON-LD.

#### Terms imported from Other Specifications

Terms imported from [ECMAScript Language Specification](https://tc39.es/ecma262/) [ECMASCRIPT], [The JavaScript Object Notation (JSON) Data Interchange Format](https://tools.ietf.org/html/rfc8259) [RFC8259], [Infra Standard](https://infra.spec.whatwg.org/) [INFRA], and [Web IDL](https://heycam.github.io/webidl/) [WEBIDL]

*[array](https://infra.spec.whatwg.org/#list)*

In the JSON serialization,
an [array](https://infra.spec.whatwg.org/#list) structure is represented as square brackets surrounding zero or more values.
Values are separated by commas.
In the [internal representation](https://www.w3.org/TR/json-ld11-api/#dfn-internal-representation),
a [list](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) (also called an [array](https://infra.spec.whatwg.org/#list)) is an *ordered* collection of zero or more values.
While JSON-LD uses the same array representation as JSON,
the collection is *unordered* by default.
While order is preserved in regular JSON arrays,
it is not in regular JSON-LD arrays unless specifically defined
(see the [Sets and Lists](https://www.w3.org/TR/json-ld11/#sets-and-lists) section of JSON-LD 1.1.

*[boolean](https://infra.spec.whatwg.org/#boolean)*

The values `true` and `false` that are used
to express one of two possible states.

*[JSON object](https://tools.ietf.org/html/rfc8259#section-4)*

In the JSON serialization,
an [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) structure
is represented as a pair of curly brackets surrounding zero or more name/value pairs (or members).
A name is a [string](https://infra.spec.whatwg.org/#javascript-string).
A single colon comes after each name,
separating the name from the value.
A single comma separates a value from a following name.
In JSON-LD the names in an object must be unique.

In the [internal representation](https://www.w3.org/TR/json-ld11-api/#dfn-internal-representation) a [JSON object](https://tools.ietf.org/html/rfc8259#section-4) is described as a *[map](https://infra.spec.whatwg.org/#ordered-map)* (see [INFRA]),
composed of *[entries](https://infra.spec.whatwg.org/#map-entry)* with key/value pairs.

In the [Application Programming Interface](https://www.w3.org/TR/json-ld11-api/#the-application-programming-interface),
a [map](https://infra.spec.whatwg.org/#ordered-map) is described using a [WEBIDL] [record](https://heycam.github.io/webidl/#idl-record).

*[null](https://infra.spec.whatwg.org/#nulls)*

The use of the [null](https://infra.spec.whatwg.org/#nulls) value within JSON-LD
is used to ignore or reset values.
A [map entry](https://infra.spec.whatwg.org/#map-entry) in the `@context` where the value,
or the `@id` of the value, is `null`,
explicitly decouples a term's association with an IRI.
A [map entry](https://infra.spec.whatwg.org/#map-entry) in the body of a [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) whose value is `null` has the same meaning as if the [map entry](https://infra.spec.whatwg.org/#map-entry) was not defined.
If `@value`, `@list`, or `@set` is set to `null` in expanded form,
then the entire [JSON object](https://tools.ietf.org/html/rfc8259#section-4) is ignored.

*[number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value)*

In the JSON serialization, a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) is similar to that used in most programming languages,
except that the octal and hexadecimal formats are not used and that leading zeros are not allowed.
In the [internal representation](https://www.w3.org/TR/json-ld11-api/#dfn-internal-representation),
a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) is equivalent to either a *[long](https://heycam.github.io/webidl/#idl-long)* or *[double](https://heycam.github.io/webidl/#idl-double)*,
depending on if the number has a non-zero fractional part (see [WEBIDL]).

*[scalar](https://infra.spec.whatwg.org/#primitive-data-types)*

A scalar is either a [string](https://infra.spec.whatwg.org/#javascript-string), [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value), `true`, or `false`.

*[string](https://infra.spec.whatwg.org/#javascript-string)*

A [string](https://infra.spec.whatwg.org/#javascript-string) is a sequence of zero or more Unicode (UTF-8) characters,
wrapped in double quotes, using backslash escapes (if necessary).
A character is represented as a single character string.

Terms imported from [Internationalized Resource Identifiers (IRIs)](https://tools.ietf.org/html/rfc3987) [RFC3987]

*[IRI](https://tools.ietf.org/html/rfc3987#section-2)*

The absolute form of an [IRI](https://tools.ietf.org/html/rfc3987#section-2) containing a *scheme* along with a *path* and optional *query* and *fragment* segments.

*[IRI reference](https://tools.ietf.org/html/rfc3987#section-1.3)*

Denotes the common usage of an [Internationalized Resource Identifier](https://tools.ietf.org/html/rfc3987#section-2).
An [IRI reference](https://tools.ietf.org/html/rfc3987#section-1.3) may be absolute or [relative](https://tools.ietf.org/html/rfc3987#section-6.5).
However, the "IRI" that results from such a reference only includes absolute [IRIs](https://tools.ietf.org/html/rfc3987#section-2);
any [relative IRI references](https://tools.ietf.org/html/rfc3987#section-6.5) are resolved to their absolute form.

*[relative IRI reference](https://tools.ietf.org/html/rfc3987#section-6.5)*

A relative IRI reference is an [IRI reference](https://tools.ietf.org/html/rfc3987#section-1.3) that is relative to some other [IRI](https://tools.ietf.org/html/rfc3987#section-2),
typically the [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri) of the document.
Note that [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property),
values of `@type`,
and values of [terms](https://www.w3.org/TR/json-ld11/#dfn-term) defined to be *vocabulary relative* are resolved relative to the [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping),
not the [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri).

Terms imported from [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/) [RDF11-CONCEPTS], [RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/) [RDF-SCHEMA], and [Linked Data Design Issues](https://www.w3.org/DesignIssues/LinkedData.html) [LINKED-DATA]

*[base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri)*

The [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri) is an [IRI](https://tools.ietf.org/html/rfc3987#section-2) established in the [context](https://www.w3.org/TR/json-ld11/#dfn-context),
or is based on the [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) location.
The [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri) is used to turn [relative IRI references](https://tools.ietf.org/html/rfc3987#section-6.5) into [IRIs](https://tools.ietf.org/html/rfc3987#section-2).

*[blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)*

A [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in a [graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) that is neither an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
nor a [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal).
A [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) does not contain
a de-referenceable identifier because it is either ephemeral in nature
or does not contain information that needs to be linked to from outside of the [linked data graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph).
In JSON-LD,
a blank node is assigned an identifier starting with the prefix `_:`.

*[blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier)*

A [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) is a string that can be used as an identifier for a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) within the scope of a JSON-LD document.
Blank node identifiers begin with `_:`.

*[dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset)*

A [dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) representing a collection of [RDF graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) including exactly one [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) and zero or more [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph).

*[datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri)*

A [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) is an [IRI](https://tools.ietf.org/html/rfc3987#section-2) identifying a datatype that determines how the lexical form maps to a [literal value](https://www.w3.org/TR/rdf11-concepts/#dfn-literal-value).

*[default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph)*

The [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) of a [dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) is an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) having no [name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name), which may be empty.

*[graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name)*

The [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) identifying a [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph).

*[language-tagged string](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string)*

A [language-tagged string](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string) consists of a string and a non-empty language tag
as defined by [BCP47].
The *[language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag)* must be well-formed
according to [section 2.2.9 Classes of Conformance](https://tools.ietf.org/html/bcp47#section-2.2.9) of [BCP47]. Processors may normalize [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) to lowercase.

*[Linked Data](https://www.w3.org/DesignIssues/LinkedData.html)*

A set of documents, each containing a representation of a [linked data graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) or [dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset).

*[list](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab)*

A [list](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) is an ordered sequence of [IRIs](https://tools.ietf.org/html/rfc3987#section-2), [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node), and [literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal).

*[literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal)*

An [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) expressed as a value such as a [string](https://infra.spec.whatwg.org/#javascript-string) or [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value).
Implicitly or explicitly includes a [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) and, if the datatype is `rdf:langString`, an optional [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag).

*[named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph)*

A [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph) is a [linked data graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) that is identified by an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node).

*[node](https://www.w3.org/TR/rdf11-concepts/#dfn-node)*

A [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph), either the [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) and [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) of at least one [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple).
Note that a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) can play both roles ([subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) and [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object)) in a [graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph), even in the same [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple).

*[object](https://www.w3.org/TR/rdf11-concepts/#dfn-object)*

An [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) is a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in a [linked data graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) with at least one incoming edge.

*[property](https://www.w3.org/TR/rdf11-concepts/#dfn-property)*

The name of a directed-arc in a [linked data graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph).
Every [property](https://www.w3.org/TR/rdf11-concepts/#dfn-property) is directional
and is labeled with an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
Whenever possible, a [property](https://www.w3.org/TR/rdf11-concepts/#dfn-property) should be labeled with an [IRI](https://tools.ietf.org/html/rfc3987#section-2).

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
> and may be removed in a future version of JSON-LD.

Also, see *[predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate)* in [RDF11-CONCEPTS].

*[RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph)*

A labeled directed [graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph),
i.e., a set of [nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-node) connected by directed-arcs.
Also called [linked data graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph).

*[resource](https://www.w3.org/TR/rdf11-concepts/#dfn-resource)*

A [resource](https://www.w3.org/TR/rdf11-concepts/#dfn-resource) denoted by an [IRI](https://tools.ietf.org/html/rfc3987#section-2), a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) or [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) representing something in the world (the "universe of discourse").

*[subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject)*

A [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) is a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in a [linked data graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) with at least one outgoing edge,
related to an [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) node through a [property](https://www.w3.org/TR/rdf11-concepts/#dfn-property).

*[triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple)*

A component of an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) including a [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject), [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate), and [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object), which represents
a node-arc-node segment of an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph).

#### JSON-LD Specific Term Definitions

*[active context](https://www.w3.org/TR/json-ld11/#dfn-active-context)*

A [context](https://www.w3.org/TR/json-ld11/#dfn-context) that is used to resolve [terms](https://www.w3.org/TR/json-ld11/#dfn-term) while the processing algorithm is running.

*[base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction)*

The [base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) is the direction used when a string does not have a direction associated with it directly.
It can be set in the [context](https://www.w3.org/TR/json-ld11/#dfn-context) using the `@direction` key
whose value must be one of the strings `"ltr"`, `"rtl"`, or `null`.
See the [Context Definitions](https://www.w3.org/TR/json-ld11/#context-definitions) section of JSON-LD 1.1 for a normative description.

*[context](https://www.w3.org/TR/json-ld11/#dfn-context)*

A set of rules for interpreting a [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) as described in the [The Context](https://www.w3.org/TR/json-ld11/#the-context) section of JSON-LD 1.1,
and normatively specified in the [Context Definitions](https://www.w3.org/TR/json-ld11/#context-definitions) section of JSON-LD 1.1.

*[default object](https://www.w3.org/TR/json-ld11/#dfn-default-object)*

A [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object) is a [map](https://infra.spec.whatwg.org/#ordered-map) that has a `@default` key.

*frame*

A [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document),
which describes the form for transforming another [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) using matching and embedding rules.
A frame document allows additional keywords and certain [map entries](https://infra.spec.whatwg.org/#map-entry) to describe the matching and transforming process.

*frame object*

A frame object is a [map](https://infra.spec.whatwg.org/#ordered-map) element within a frame which represents a specific portion of the frame matching either
a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) or a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) in the input.
See the [Frame Objects](https://www.w3.org/TR/json-ld11/#frame-objects) section of JSON-LD 1.1 for a normative description.

*[JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document)*

A [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) is a serialization of
an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset).
See the [JSON-LD Grammar](https://www.w3.org/TR/json-ld11/#json-ld-grammar) section in JSON-LD 1.1 for a formal description.

*[JSON-LD internal representation](https://www.w3.org/TR/json-ld11-api/#dfn-internal-representation)*

The JSON-LD internal representation
is the result of transforming a JSON syntactic structure
into the core data structures suitable for direct processing: [arrays](https://infra.spec.whatwg.org/#list), [maps](https://infra.spec.whatwg.org/#ordered-map), [strings](https://infra.spec.whatwg.org/#javascript-string), [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value), [booleans](https://infra.spec.whatwg.org/#boolean), and [null](https://infra.spec.whatwg.org/#nulls).

*[JSON-LD Processor](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor)*

A [JSON-LD Processor](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor) is a system which can perform the algorithms defined in JSON-LD 1.1 Processing Algorithms and API.
See the [Conformance](https://www.w3.org/TR/json-ld11-api/#conformance) section in JSON-LD 1.1 API for a formal description.

*[JSON-LD value](https://www.w3.org/TR/json-ld11/#dfn-json-ld-value)*

A [JSON-LD value](https://www.w3.org/TR/json-ld11/#dfn-json-ld-value) is a [string](https://infra.spec.whatwg.org/#javascript-string),
a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value), `true` or `false`,
a [typed value](https://www.w3.org/TR/json-ld11/#dfn-typed-value),
or a [language-tagged string](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string).
It represents an [RDF literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal).

*[keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword)*

A [string](https://infra.spec.whatwg.org/#javascript-string) that is specific to JSON-LD,
described in the [Syntax Tokens and Keywords](https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords) section of JSON-LD 1.1,
and normatively specified in the [Keywords](https://www.w3.org/TR/json-ld11/#keywords) section of JSON-LD 1.1,

*[node object](https://www.w3.org/TR/json-ld11/#dfn-node-object)*

A [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) represents zero or more [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in the [graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) serialized by the [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document).
A [map](https://infra.spec.whatwg.org/#ordered-map) is a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) if it exists outside of the JSON-LD [context](https://www.w3.org/TR/json-ld11/#dfn-context) and:

- it does not contain the `@value`, `@list`, or `@set` keywords, or
- it is not the top-most [map](https://infra.spec.whatwg.org/#ordered-map) in the JSON-LD document
  consisting of no other [entries](https://infra.spec.whatwg.org/#map-entry) than `@graph` and `@context`.

The [entries](https://infra.spec.whatwg.org/#map-entry) of a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) whose keys are not keywords are also called [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of the [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).
See the [Node Objects](https://www.w3.org/TR/json-ld11/#node-objects) section of JSON-LD 1.1 for a normative description.

*[node reference](https://www.w3.org/TR/json-ld11/#dfn-node-reference)*

A [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) used to reference a node having only the `@id` key.

*[processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode)*

The [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) defines how a [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) is processed.
By default, all documents are assumed to be conformant with this specification.
By defining a different version using the `@version` [entry](https://infra.spec.whatwg.org/#map-entry) in a [context](https://www.w3.org/TR/json-ld11/#dfn-context),
publishers can ensure that processors conformant with [JSON-LD 1.0](https://www.w3.org/TR/2014/REC-json-ld-20140116/) [JSON-LD10]
will not accidentally process JSON-LD 1.1 documents, possibly creating a different output.
The API provides an option for setting the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) to `json-ld-1.0`,
which will prevent JSON-LD 1.1 features from being activated,
or error if `@version` [entry](https://infra.spec.whatwg.org/#map-entry) in a [context](https://www.w3.org/TR/json-ld11/#dfn-context) is explicitly set to `1.1`.
This specification extends [JSON-LD 1.0](https://www.w3.org/TR/2014/REC-json-ld-20140116/) via the `json-ld-1.1` [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode).

*[scoped context](https://www.w3.org/TR/json-ld11/#dfn-scoped-context)*

A [scoped context](https://www.w3.org/TR/json-ld11/#dfn-scoped-context) is part of an [expanded term definition](https://www.w3.org/TR/json-ld11/#dfn-expanded-term-definition) using the `@context` [entry](https://infra.spec.whatwg.org/#map-entry). It has the same form as an [embedded context](https://www.w3.org/TR/json-ld11/#dfn-embedded-context).
When the term is used as a type, it defines a *[type-scoped context](https://www.w3.org/TR/json-ld11/#dfn-type-scoped-context)*,
when used as a property it defines a *[property-scoped context](https://www.w3.org/TR/json-ld11/#dfn-property-scoped-context)*.

*[typed value](https://www.w3.org/TR/json-ld11/#dfn-typed-value)*

A [typed value](https://www.w3.org/TR/json-ld11/#dfn-typed-value) consists of a value,
which is a [string](https://infra.spec.whatwg.org/#javascript-string),
and a type,
which is an [IRI](https://tools.ietf.org/html/rfc3987#section-2).

*[value object](https://www.w3.org/TR/json-ld11/#dfn-value-object)*

A [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) is a [map](https://infra.spec.whatwg.org/#ordered-map) that has an `@value` [entry](https://infra.spec.whatwg.org/#map-entry).
See the [Value Objects](https://www.w3.org/TR/json-ld11/#value-objects) section of JSON-LD 1.1 for a normative description.

*[vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping)*

The vocabulary mapping is set in the [context](https://www.w3.org/TR/json-ld11/#dfn-context) using the `@vocab` key
whose value must be an [IRI](https://tools.ietf.org/html/rfc3987#section-2), a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri), a [term](https://www.w3.org/TR/json-ld11/#dfn-term), or `null`.
See the [Context Definitions](https://www.w3.org/TR/json-ld11/#context-definitions) section of JSON-LD 1.1 for a normative description.

#### 1.4.1 Algorithm Terms

The Following terms are used within specific algorithms.

*[active property](https://www.w3.org/TR/json-ld11-api/#dfn-active-property)*

The currently active [property](https://www.w3.org/TR/rdf11-concepts/#dfn-property) or [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) that the processor should use when processing.
The [active property](https://www.w3.org/TR/json-ld11-api/#dfn-active-property) is represented in the original lexical form,
which is used for finding coercion mappings in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context).

*explicit inclusion flag*

A flag specifying that for [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) to be included in the output,
they must be explicitly declared in the matching frame.

*framing state*

A [map](https://infra.spec.whatwg.org/#ordered-map) containing values for
the object embed flag,
the require all flag, the embedded flag,
used internally to help determine if object embedding is appropriate, the explicit inclusion flag,
and the omit default flag.

*input frame*

The initial Frame provided to the framing algorithm.

*[IRI compacting](https://www.w3.org/TR/json-ld11-api/#dfn-iri-compacting)*

Used as a macro within various algorithms as to reduce the language used to describe
the process of compacting a [string](https://infra.spec.whatwg.org/#javascript-string) *var* representing an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) using an *active context* either specified directly, or coming from the scope of
the algorithm step using this term.
An optional *value* is used, if explicitly provided.
Unless specified, the *vocab* flag defaults to `true`,
and the *reverse* flag defaults to `false`.

1. Return the result of using the [IRI Compaction algorithm](https://www.w3.org/TR/json-ld11-api/#iri-compaction),
   passing *active context*, *var*, *value* (if supplied), *vocab*,
   and *result*.

*[JSON-LD input](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-input)*

The JSON-LD data structure that is provided as input to the algorithm.

*map of flattened subjects*

A map of subjects that is the result of the [Node Map Generation algorithm](https://www.w3.org/TR/json-ld11-api/#node-map-generation).

*object embed flag*

A flag specifying that [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) should be directly embedded in the output,
instead of being referred to by their [IRI](https://tools.ietf.org/html/rfc3987#section-2).

*omit default flag*

A flag specifying that properties that are missing from the [JSON-LD input](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-input),
but present in the input frame,
should be omitted from the output.

*omit graph flag*

A flag that determines if framing output is always contained within a `@graph` [entry](https://infra.spec.whatwg.org/#map-entry),
or only if required to represent multiple [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object).

*require all flag*

A flag specifying that all properties present in the input frame must either have a default value
or be present in the [JSON-LD input](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-input) for the frame to match.

### 1.5 Syntax Tokens and Keywords

This specification adds a number of [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) (*framing keywords*) to
the ones defined in the JSON-LD 1.1 Syntax specification [JSON-LD11]:

`@default`

Used in §2.1 Framing to set the default value for
an output property when the framed [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) does not include such a property.

`@embed`

Used in §2.1 Framing to override the
value of object embed flag within a specific frame. Valid values for `@embed` as the following:

`@always`

Always embed [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) as property values, unless this would
cause a circular reference.

`@once`

Just a single value within a given [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) should be embedded,
other values of other properties use a [node reference](https://www.w3.org/TR/json-ld11/#dfn-node-reference). This is the
default value if neither `@embed` nor object embed flag is specified.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The specific [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) chosen to embed depends on
> ordering. If the `ordered` flag is `true`,
> this will be the first [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) encountered,
> otherwise, it may be any node object.

`@never`

Always use a [node reference](https://www.w3.org/TR/json-ld11/#dfn-node-reference) when serializing matching values.

Any other value for `@embed` is invalid and indicates that an `invalid @embed value` error has been detected and processing is aborted.

`@explicit`

Used in §2.1 Framing to override the
value of explicit inclusion flag within a specific frame.

`@null`

Used in §2.1 Framing when a value of `null` should be returned, which would otherwise be removed when [Compacting](https://www.w3.org/TR/json-ld11-api/#compaction).

`@omitDefault`

Used in §2.1 Framing to override the
value of omit default flag within a specific frame.

`@requireAll`

Used in §2.1 Framing to override the
value of require all flag within a specific frame.

All JSON-LD tokens and keywords are case-sensitive.

## 2. Features

*This section is non-normative.*

JSON-LD 1.1 introduces new features that are
compatible with [JSON-LD 1.0](https://www.w3.org/TR/2014/REC-json-ld-20140116/) [JSON-LD10],
but if processed by a JSON-LD 1.0 processor may produce different results.
Processors default to `json-ld-1.1`, unless the [processingMode](https://www.w3.org/TR/json-ld11-api/#dom-jsonldoptions-processingmode) API option
is explicitly set to `json-ld-1.0`.
Publishers are encouraged to use the `@version` [map entry](https://infra.spec.whatwg.org/#map-entry) within a [context](https://www.w3.org/TR/json-ld11/#dfn-context) set to `1.1` to ensure that JSON-LD 1.0 processors will not misinterpret JSON-LD 1.1 features.

### 2.1 Framing

*This section is non-normative.*

*Framing* is used to shape the data in a [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document),
using an example frame document which is used to both match the [flattened](https://www.w3.org/TR/json-ld11-api/#dfn-flattened) data and show an example of how the resulting data should be shaped.
Matching is performed by using [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) present in in the frame to find objects in the data that share common values. Matching can be done
either using all properties present in the frame, or any property in the frame.
By chaining together objects using matched property values, objects can be embedded
within one another.

A frame also includes a [context](https://www.w3.org/TR/json-ld11/#dfn-context), which is used for compacting the resulting
framed output.

For example, assume the following JSON-LD frame:
> **Example:**
>
> Example 2: Sample library frame
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@type": "Library",
>   "contains": {
>     "@type": "Book",
>     "contains": {
>       "@type": "Chapter"
>     }
>   }
> }
> ```

This frame document describes an embedding structure that would place
objects with type *Library* at the top, with objects of
type *Book* that were linked to the library object using
the *contains* property embedded as property values. It also
places objects of type *Chapter* within the referencing *Book* object
as embedded values of the *Book* object.

When using a flattened set of objects that match the frame components:
> **Example:**
>
> Example 3: Flattened library objects
>
>
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "contains": {"@type": "@id"}
>   },
>   "@graph": [{
>     "@id": "http://example.org/library",
>     "@type": "Library",
>     "location": "Athens",
>     "contains": "http://example.org/library/the-republic"
>   }, {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": "http://example.org/library/the-republic#introduction"
>   }, {
>     "@id": "http://example.org/library/the-republic#introduction",
>     "@type": "Chapter",
>     "description": "An introductory chapter on The Republic.",
>     "title": "The Introduction"
>   }]
> }
> ```

The Frame Algorithm can create a new document which follows the structure
of the frame:
> **Example:**
>
> Example 4: Framed library objects
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22%40type%22%3A%20%22Chapter%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is not `json-ld-1.0`, or the omit graph flag is `true`,
the top-level `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) may be omitted.
> **Example:**
>
> Example 5: Framed library objects
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

The §4.1 Framing Algorithm does this by
first expanding both the input frame and document. It then creates
a map of flattened subjects. The outer-most [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) within the frame
is used to match objects in the map, in this case looking for [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) which have an `@type` of `Library`, and a `contains` property with another
frame used to match values of that property. The input document contains
exactly one such [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object). The value of contains also has
a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), which is then treated as a frame to match the set of [subjects](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) which are `contains` values of the `Library` object, and so forth.

#### 2.1.1 Matching on Properties

*This section is non-normative.*

In addition to matching on types, a frame can match on
one or more properties.

For example, the following frame selects object based on property
values, rather than `@type`.
> **Example:**
>
> Example 6: Library frame with property matching
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "location": "Athens",
>   "contains": {
>     "title": "The Republic",
>     "contains": {
>       "title": "The Introduction"
>     }
>   }
> }
> ```

This will generate the same framed results as when selecting on `@type`,
as the property values are unique to each node [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object).
> **Example:**
>
> Example 7: Framed library objects with property matching
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

See § 2.3.5 Require all flag (§2.3.5) to see how matching can be restricted to match [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) containing
all, versus any such listed property.

#### 2.1.2 Wildcard Matching

*This section is non-normative.*

The empty [map](https://infra.spec.whatwg.org/#ordered-map) (`{}`) is used as a `wildcard`, which will
match a property if it exists in a target [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), independent of any specific value.

For example, the following frame selects object based on property
wildcarding, rather than `@type`.
> **Example:**
>
> Example 8: Library frame with wildcard matching
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "location": {},
>   "contains": {
>     "creator": {},
>     "contains": {
>       "description": {}
>     }
>   }
> }
> ```

This will generate the same framed results as when selecting on `@type`,
as the matched properties are distinct to each [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).
> **Example:**
>
> Example 9: Framed library objects with wildcard matching
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22location%22%3A%20%7B%7D%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22creator%22%3A%20%7B%7D%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22description%22%3A%20%7B%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

#### 2.1.3 Match on the Absence of a Property

*This section is non-normative.*

The empty [array](https://infra.spec.whatwg.org/#list) (`[]`) is used for `match none`, which will
match a node object only if a property does not exist in a target [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).

For example, the following frame selects object based on the absence of properties,
rather than `@type`.
> **Example:**
>
> Example 10: Library frame with absent matching
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "creator": [],
>   "title": [],
>   "contains": {
>     "location": [],
>     "description": [],
>     "contains": {
>       "location": []
>     }
>   }
> }
> ```

This will generate the same framed results as when selecting on `@type`,
the property that is excluded uniquely identifies each [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).
Note that additional properties with the value `null` are added
for those properties explicitly excluded.
> **Example:**
>
> Example 11: Framed library objects with wildcard matching
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22creator%22%3A%20%5B%5D%2C%0A%20%20%22title%22%3A%20%5B%5D%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22location%22%3A%20%5B%5D%2C%0A%20%20%20%20%22description%22%3A%20%5B%5D%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22location%22%3A%20%5B%5D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "creator": null, ← This property is added
>   "title": null, ← This property is added
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "description": null, ← This property is added
>     "location": null, ← This property is added
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "location": null, ← This property is added
>       "title": "The Introduction"
>     }
>   }
> }
> ```

#### 2.1.4 Matching on Values

*This section is non-normative.*

Frames can be matched based on the presence of specific property values.
These values can themselves use `wildcards`, to match on a specific
or set of values, [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag), types, or [base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction).

For an example, we'll use an multilingual version of the library example
with more complex value representations.
> **Example:**
>
> Example 12: Multilingual library objects
>
>
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "contains": {"@type": "@id"}
>   },
>   "@graph": [{
>     "@id": "http://example.org/library",
>     "@type": "Library",
>     "location": [
>       {"@value": "Athens", "@language": "en"},
>       {"@value": "Αθήνα", "@language": "grc"},
>       {"@value": "Athína", "@language": "el-Latn"}
>     ],
>     "contains": "http://example.org/library/the-republic"
>   }, {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": [
>       {"@value": "Plato", "@language": "en"},
>       {"@value": "Πλάτων", "@language": "grc"},
>       {"@value": "Plátōn", "@language": "el-Latn"}
>     ],
>     "title": [
>       {"@value": "The Republic", "@language": "en"},
>       {"@value": "Πολιτεία", "@language": "grc"},
>       {"@value": "Res Publica", "@language": "el-Latn"}
>     ],
>     "contains": "http://example.org/library/the-republic#introduction"
>   }, {
>     "@id": "http://example.org/library/the-republic#introduction",
>     "@type": "Chapter",
>     "description": "An introductory chapter on The Republic.",
>     "title": "The Introduction"
>   }]
> }
> ```

By matching on an attribute of a value, we can match frames
having that attribute, and limit results to property values
that match. In this case, we'll frame the Library and Book objects
on values only in latinized Greek (`el-Latn`):
> **Example:**
>
> Example 13: Library frame with language matching
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "location": {"@value": {}, "@language": "el-Latn"},
>   "contains": {
>     "creator": {"@value": {}, "@language": "el-Latn"},
>     "title": {"@value": {}, "@language": "el-Latn"},
>     "contains": {
>       "title": "The Introduction"
>     }
>   }
> }
> ```

This generates the following framed results:
> **Example:**
>
> Example 14: Framed library objects with wildcard matching
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%5B%0A%20%20%20%20%20%20%7B%22%40value%22%3A%20%22Athens%22%2C%20%22%40language%22%3A%20%22en%22%7D%2C%0A%20%20%20%20%20%20%7B%22%40value%22%3A%20%22%CE%91%CE%B8%CE%AE%CE%BD%CE%B1%22%2C%20%22%40language%22%3A%20%22grc%22%7D%2C%0A%20%20%20%20%20%20%7B%22%40value%22%3A%20%22Ath%C3%ADna%22%2C%20%22%40language%22%3A%20%22el-Latn%22%7D%0A%20%20%20%20%5D%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%5B%0A%20%20%20%20%20%20%7B%22%40value%22%3A%20%22Plato%22%2C%20%22%40language%22%3A%20%22en%22%7D%2C%0A%20%20%20%20%20%20%7B%22%40value%22%3A%20%22%CE%A0%CE%BB%CE%AC%CF%84%CF%89%CE%BD%22%2C%20%22%40language%22%3A%20%22grc%22%7D%2C%0A%20%20%20%20%20%20%7B%22%40value%22%3A%20%22Pl%C3%A1t%C5%8Dn%22%2C%20%22%40language%22%3A%20%22el-Latn%22%7D%0A%20%20%20%20%5D%2C%0A%20%20%20%20%22title%22%3A%20%5B%0A%20%20%20%20%20%20%7B%22%40value%22%3A%20%22The%20Republic%22%2C%20%22%40language%22%3A%20%22en%22%7D%2C%0A%20%20%20%20%20%20%7B%22%40value%22%3A%20%22%CE%A0%CE%BF%CE%BB%CE%B9%CF%84%CE%B5%CE%AF%CE%B1%22%2C%20%22%40language%22%3A%20%22grc%22%7D%2C%0A%20%20%20%20%20%20%7B%22%40value%22%3A%20%22Res%20Publica%22%2C%20%22%40language%22%3A%20%22el-Latn%22%7D%0A%20%20%20%20%5D%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22location%22%3A%20%7B%22%40value%22%3A%20%7B%7D%2C%20%22%40language%22%3A%20%22el-Latn%22%7D%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22creator%22%3A%20%7B%22%40value%22%3A%20%7B%7D%2C%20%22%40language%22%3A%20%22el-Latn%22%7D%2C%0A%20%20%20%20%22title%22%3A%20%7B%22%40value%22%3A%20%7B%7D%2C%20%22%40language%22%3A%20%22el-Latn%22%7D%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": {"@value": "Athína", "@language": "el-Latn"},
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": {"@value": "Plátōn", "@language": "el-Latn"},
>     "title": {"@value": "Res Publica", "@language": "el-Latn"},
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

#### 2.1.5 Matching on `@id`

*This section is non-normative.*

Frames can be matched if they match a specific
identifier (`@id`). This can be illustrated with the original Flattened library objects input using a frame which matches on specific `@id` values:
> **Example:**
>
> Example 15: Library frame with @id matching
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction"
>     }
>   }
> }
> ```

This generates the following framed results:
> **Example:**
>
> Example 16: Framed library objects with @id matching
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/"
>   },
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

Frames can also be matched from an array of identifiers.
Within a frame, it is acceptable for `@id` to have an [array](https://infra.spec.whatwg.org/#list) value,
where the individual values are treated as [IRIs](https://tools.ietf.org/html/rfc3987#section-2).
> **Example:**
>
> Example 17: Library frame with array @id matching
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": ["http://example.org/home", "http://example.org/library"],
>   "contains": {
>     "@id": ["http://example.org/library/the-republic"],
>     "contains": {
>       "@id": ["http://example.org/library/the-republic#introduction"]
>     }
>   }
> }
> ```

This generates the following framed results:
> **Example:**
>
> Example 18: Framed library objects with @id matching
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40id%22%3A%20%5B%22http%3A%2F%2Fexample.org%2Fhome%22%2C%20%22http%3A%2F%2Fexample.org%2Flibrary%22%5D%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40id%22%3A%20%5B%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%5D%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22%40id%22%3A%20%5B%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%5D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

#### 2.1.6 Empty Frame

*This section is non-normative.*

An empty frame matches any node object, even if those
objects are embedded elsewhere, causing them to be serialized at the top level.
> **Example:**
>
> Example 19: Empty frame
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"}
> }
> ```

This generates the following framed results:
> **Example:**
>
> Example 20: Framed library objects with empty frame
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@graph": [{
>     "@id": "http://example.org/library",
>     "@type": "Library",
>     "location": "Athens",
>     "contains": {
>       "@id": "http://example.org/library/the-republic",
>       "@type": "Book",
>       "creator": "Plato",
>       "title": "The Republic",
>       "contains": {
>         "@id": "http://example.org/library/the-republic#introduction",
>         "@type": "Chapter",
>         "description": "An introductory chapter on The Republic.",
>         "title": "The Introduction"
>       }
>     }
>   }, {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }, {
>     "@id": "http://example.org/library/the-republic#introduction",
>     "@type": "Chapter",
>     "description": "An introductory chapter on The Republic.",
>     "title": "The Introduction"
>   }]
> }
> ```

### 2.2 Default content

*This section is non-normative.*

A frame may specify properties that don't exist in an input file. If the explicit inclusion flag is `false`, the framing algorithm
will add a property and value to the result. The `@default` property
in a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) or [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object), or as a value of `@type`,
provides a default value to use in the resulting
output document. If there is no `@default` value, the property will be output
with a `null` value. (See § 2.3.3 Omit default flag (§2.3.3) for ways to avoid this).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The value of the property in the frame is not otherwise
> used in the output document. It's purpose is for frame matching and
> finding default values. Note the *description* value for *Library* in the following example.
> **Example:**
>
> Example 21: Sample library frame with @default value
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@type": "Library",
>   "description": "A great Library.",
>   "contains": {
>     "@type": "Book",
>     "description": {"@default": "A great book."},
>     "contains": {
>       "@type": "Chapter"
>     }
>   }
> }
> ```
> **Example:**
>
> Example 22: Sample library output with @default value
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%22description%22%3A%20%22A%20great%20Library.%22%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22description%22%3A%20%7B%22%40default%22%3A%20%22A%20great%20book.%22%7D%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22%40type%22%3A%20%22Chapter%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "description": null,
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "description": "A great book.",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

Default values may also be used for `@type`, similar to other properties.
In this case, a matched [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) without an `@type` will take the
value of the [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object) from the frame.
The [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object) has a value which is a single [IRI](https://tools.ietf.org/html/rfc3987#section-2).
If multiple [IRIs](https://tools.ietf.org/html/rfc3987#section-2) are specified, only the first will be used as the default type.

The frame matches objects having specific property values,
and provides defaults for `@type` for matched objects.
> **Example:**
>
> Example 23: Sample library frame with @default type
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@type": "Library",
>   "contains": {
>     "@type": {"@default": "Book"},
>     "creator": "Plato",
>     "contains": {
>       "@type": {"@default": "Chapter"},
>       "description": "An introductory chapter on The Republic."
>     }
>   }
> }
> ```

Data missing specific values for `@type`, but which matches based on
other property values.
> **Example:**
>
> Example 24: Typeless library objects
>
>
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "contains": {"@type": "@id"}
>   },
>   "@graph": [{
>     "@id": "http://example.org/library",
>     "@type": "Library",
>     "contains": "http://example.org/library/the-republic"
>   }, {
>     "@id": "http://example.org/library/the-republic",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": "http://example.org/library/the-republic#introduction"
>   }, {
>     "@id": "http://example.org/library/the-republic#introduction",
>     "description": "An introductory chapter on The Republic.",
>     "title": "The Introduction"
>   }]
> }
> ```
> **Example:**
>
> Example 25: Sample library output with @default type
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40type%22%3A%20%7B%22%40default%22%3A%20%22Book%22%7D%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22%40type%22%3A%20%7B%22%40default%22%3A%20%22Chapter%22%7D%2C%0A%20%20%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@graph": [{
>     "@id": "http://example.org/library",
>     "@type": "Library",
>     "contains": {
>       "@id": "http://example.org/library/the-republic",
>       "@type": "Book",
>       "contains": {
>         "@id": "http://example.org/library/the-republic#introduction",
>         "@type": "Chapter",
>         "description": "An introductory chapter on The Republic.",
>         "title": "The Introduction"
>       },
>       "creator": "Plato",
>       "description": "A great book.",
>       "title": "The Republic"
>     }
>   }]
> }
> ```

### 2.3 Framing Flags

*This section is non-normative.*

Framing can be controlled using API options,
or by adding framing [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) within the frame as
described in § 1.5 Syntax Tokens and Keywords (§1.5).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Framing flags set using keywords have effect only for the
> frame in which they appear, and for implicit frames which are created
> for objects where no frame object exists.

#### 2.3.1 Object Embed Flag

*This section is non-normative.*

The object embed flag determines if a referenced [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) is embedded as a property value of a referencing
object, or kept as a [node reference](https://www.w3.org/TR/json-ld11/#dfn-node-reference).
The initial value for the object embed flag is set using the `embed` option.
Consider the following frame
based on the default `@once` value of the object embed flag:
> **Example:**
>
> Example 26: Sample library frame with implicit @embed set to @once
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@type": "Library"
> }
> ```
> **Example:**
>
> Example 27: Framed library objects with @embed set to @once
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

Because, the default for the object embed flag is `@once` (in addition to the explicit inclusion flag being `false`),
non-listed properties are added to the output, and implicitly embedded
using a default empty frame. As a result, the same output used in the Framed library objects above is generated,
assuming that the `ordered` flag is `true`.

However, if the `@embed` property is added explicitly with a
value of `@never`, the values for *Book* and *Chapter* will be excluded.
> **Example:**
>
> Example 28: Sample library frame with explicit @embed set to @never
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@type": "Library",
>   "contains": {
>     "@type": "Book",
>     "@embed": "@never"
>   }
> }
> ```
> **Example:**
>
> Example 29: Framed library objects with @embed set to @never
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22%40embed%22%3A%20%22%40never%22%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic"
>   }
> }
> ```

To illustrate the case where `@once` does not expand values,
consider an alternate library example where books are doubly indexed.
> **Example:**
>
> Example 30: Flattened library objects with double index
>
>
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "books": {"@type": "@id"},
>     "contains": {"@type": "@id"}
>   },
>   "@graph": [{
>     "@id": "http://example.org/library",
>     "@type": "Library",
>     "books": "http://example.org/library/the-republic",
>     "contains": "http://example.org/library/the-republic"
>   }, {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": "http://example.org/library/the-republic#introduction"
>   }, {
>     "@id": "http://example.org/library/the-republic#introduction",
>     "@type": "Chapter",
>     "description": "An introductory chapter on The Republic.",
>     "title": "The Introduction"
>   }]
> }
> ```
> **Example:**
>
> Example 31: Framed library objects with double index
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22books%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22books%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "contains": {"@id": "http://example.org/library/the-republic"},
>   "books": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

When framed using the same frame with the default `@embed` of `@once`,
only the *"books"* property will have content,
if the `ordered` flag is `true`,
and the *"contains"* property will use a reference.

If we use a frame using `"@embed": "@always"`,
both properties will include expanded values.
> **Example:**
>
> Example 32: Sample library frame with explicit @embed set to @always
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@type": "Library",
>   "@embed": "@always"
> }
> ```
> **Example:**
>
> Example 33: Framed library objects with double index and @always
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22books%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22books%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%22%40embed%22%3A%20%22%40always%22%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "books": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   },
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

#### 2.3.2 Explicit inclusion flag

*This section is non-normative.*

The explicit inclusion flag used to determine
properties which will be included in the output document.
The default value is `false`, which means that properties
present in an input [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) that are not in the associated frame will be
included in the output object.
If `true`, only properties present in
the input frame will be placed into the output.
The initial value for the explicit inclusion flag is set using the `explicit` option.

For example, take an expanded version of the library frame which include
some properties from the input, but omit others.
> **Example:**
>
> Example 34: Sample library frame with @explicit set to true
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@type": "Library",
>   "description": {},
>   "contains": {
>     "@type": "Book",
>     "@explicit": true,
>     "title": {},
>     "contains": {
>       "@type": "Chapter"
>     }
>   }
> }
> ```

The resulting output will exclude properties for Book which are not explicitly
listed in the frame object:
> **Example:**
>
> Example 35: Framed library objects with @explicit set to true
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%22description%22%3A%20%7B%7D%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22%40explicit%22%3A%20true%2C%0A%20%20%20%20%22title%22%3A%20%7B%7D%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22%40type%22%3A%20%22Chapter%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "description": null ← This property is explicit,
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato", ← This property is omitted
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

Note that the *Library* object contains a `null` *description* property, as it is explicitly called for in the frame
using `"description": {}`. The *creator* property does
not exist in the output, because it is not explicit.

#### 2.3.3 Omit default flag

*This section is non-normative.*

The omit default flag changes the way framing generates output when a property
described in the frame is not present in the input document.
The initial value for the omit default flag is set using the `omitDefault` option.
See § 2.2 Default content (§2.2) for a further discussion.

Consider the following input document:
> **Example:**
>
> Example 36: Sample parent/child relationship data
>
>
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "child": {"@type": "@id"}
>   },
>   "@graph": [{
>     "@id": "http://example.org#John",
>     "@type": "Person",
>     "name": "John",
>     "child": "http://example.org#Jane"
>   }, {
>     "@id": "http://example.org#Jane",
>     "@type": "Person",
>     "name": "Jane"
>   }]
> }
> ```

To illustrate where the omit default flag is useful, consider the following
frame, which does *not* use `@omitDefault`:
> **Example:**
>
> Example 37: Sample parent/child relationship frame without @omitDefault
>
>
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "child": {"@type": "@id"}
>   },
>   "@type": "Person",
>   "child": {
>     "@embed": "@always"
>   }
> }
> ```

The resulting output will include a "child" property with the value `null`, which may not always be desired:
> **Example:**
>
> Example 38: Sample parent/child relationship output without @omitDefault
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22child%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%23John%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Person%22%2C%0A%20%20%20%20%22name%22%3A%20%22John%22%2C%0A%20%20%20%20%22child%22%3A%20%22http%3A%2F%2Fexample.org%23Jane%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%23Jane%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Person%22%2C%0A%20%20%20%20%22name%22%3A%20%22Jane%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22child%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40type%22%3A%20%22Person%22%2C%0A%20%20%22child%22%3A%20%7B%0A%20%20%20%20%22%40embed%22%3A%20%22%40always%22%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "child": {"@type": "@id"}
>   },
>   "@graph": [{
>     "@id": "http://example.org#John",
>     "@type": "Person",
>     "name": "John",
>     "child": {
>       "@id": "http://example.org#Jane",
>       "@type": "Person",
>       "name": "Jane"
>     }
>   }, {
>     "@id": "http://example.org#Jane",
>     "@type": "Person",
>     "name": "Jane",
>     "child": null
>   }]
> }
> ```

Note that because the option `"@embed": "@always"` is specified in the frame
under the child property, that `"child": null` appears in the output
for matches that do not have that property, which may be undesirable.
To prevent this default `null` output from occurring,
the `@omitDefault` may be set to true like so:
> **Example:**
>
> Example 39: Sample parent/child relationship frame with @omitDefault
>
>
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "child": {"@type": "@id"}
>   },
>   "@type": "Person",
>   "child": {
>     "@embed": "@always",
>     "@omitDefault": true
>   }
> }
> ```

Which yields this (desirable) output:
> **Example:**
>
> Example 40: Sample parent/child relationship output with @omitDefault
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22child%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%23John%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Person%22%2C%0A%20%20%20%20%22name%22%3A%20%22John%22%2C%0A%20%20%20%20%22child%22%3A%20%22http%3A%2F%2Fexample.org%23Jane%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%23Jane%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Person%22%2C%0A%20%20%20%20%22name%22%3A%20%22Jane%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22child%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40type%22%3A%20%22Person%22%2C%0A%20%20%22child%22%3A%20%7B%0A%20%20%20%20%22%40embed%22%3A%20%22%40always%22%2C%0A%20%20%20%20%22%40omitDefault%22%3A%20true%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "child": {"@type": "@id"}
>   },
>   "@graph": [{
>     "@id": "http://example.org#John",
>     "@type": "Person",
>     "name": "John",
>     "child": {
>       "@id": "http://example.org#Jane",
>       "@type": "Person",
>       "name": "Jane"
>     }
>   }, {
>     "@id": "http://example.org#Jane",
>     "@type": "Person",
>     "name": "Jane"
>     ↑ Does not include "child" property
>   }]
> }
> ```

#### 2.3.4 Omit graph flag

*This section is non-normative.*

The omit graph flag determines if framed output containing a single [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) is contained within `@graph`, or not.
The initial value for the omit graph flag is set using the `omitGraph` option, or based on
the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode); if [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`, the output
always includes a `@graph` [entry](https://infra.spec.whatwg.org/#map-entry), otherwise, the `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) is used only
to describe multiple [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object), consistent with compaction.
See § 4.1 Framing Algorithm (§4.1) for a further discussion.

The result is the same as the original Flattened library objects example,
but a `@graph` at the top-level. Example 5 shows the results
with the omit graph flag set to `true`, which is the default value when
the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is set to the default `json-ld-1.1`.
The top-level object can be enclosed within `@graph` by setting the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) to `json-ld-1.0`,
or by setting the omit graph flag to `false`.
> **Example:**
>
> Example 41: Framed library objects with @omitGraph set to false
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22%40type%22%3A%20%22Chapter%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@graph": [{
>     "@id": "http://example.org/library",
>     "@type": "Library",
>     "location": "Athens",
>     "contains": {
>       "@id": "http://example.org/library/the-republic",
>       "@type": "Book",
>       "creator": "Plato",
>       "title": "The Republic",
>       "contains": {
>         "@id": "http://example.org/library/the-republic#introduction",
>         "@type": "Chapter",
>         "description": "An introductory chapter on The Republic.",
>         "title": "The Introduction"
>       }
>     }
>   }]
> }
> ```

#### 2.3.5 Require all flag

*This section is non-normative.*

The require all flag is used in frame matching to determine when a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) from an input document matches a frame. When
matching, an object may include `@type` and other
properties, a match is made when *any* property value in the
object matches the `node pattern` in the frame object if
the value of the require all flag is `false` (the
default). If the flag value is `true`, then *all* properties in the frame object must be present in the [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) for the node to match.

The following frame matches on multiple properties, including the absence of a property.
Using the Flattened library objects example,
we can match on an object containing both the title and description or title and creator
properties.
If we were to use `@requireAll` set to `false`, then we could match on the presence
of any property, not all properties.
> **Example:**
>
> Example 42: Frame with @requireAll
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@type": "Library",
>   "contains": {
>     "@requireAll": true,
>     "creator": {},
>     "title": {},
>     "contains": {
>       "@requireAll": true,
>       "description": {},
>       "title": {}
>     }
>   }
> }
> ```

This will, again, reproduce the desired framed output:
> **Example:**
>
> Example 43: Framed library objects with @requireAll set to true
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40requireAll%22%3A%20true%2C%0A%20%20%20%20%22creator%22%3A%20%7B%7D%2C%0A%20%20%20%20%22title%22%3A%20%7B%7D%2C%0A%20%20%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%20%20%22%40requireAll%22%3A%20true%2C%0A%20%20%20%20%20%20%22description%22%3A%20%7B%7D%2C%0A%20%20%20%20%20%20%22title%22%3A%20%7B%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "location": "Athens",
>   "contains": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "creator": "Plato",
>     "title": "The Republic",
>     "contains": {
>       "@id": "http://example.org/library/the-republic#introduction",
>       "@type": "Chapter",
>       "description": "An introductory chapter on The Republic.",
>       "title": "The Introduction"
>     }
>   }
> }
> ```

### 2.4 Reverse Framing

*This section is non-normative.*

A frame may include `@reverse`, or a value of a term defined using `@reverse` to invert the relationships in the output object. For example, the
Library example can be inverted using the following frame:
> **Example:**
>
> Example 44: Inverted library frame
>
>
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "within": {"@reverse": "contains"}
>   },
>   "@type": "Chapter",
>   "within": {
>     "@type": "Book",
>     "within": {
>       "@type": "Library"
>     }
>   }
> }
> ```

Using the flattened library example above, results in the following:
> **Example:**
>
> Example 45: Inverted library output
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22contains%22%3A%20%7B%22%40type%22%3A%20%22%40id%22%7D%0A%20%20%7D%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%20%20%22location%22%3A%20%22Athens%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22creator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Republic%22%2C%0A%20%20%20%20%22contains%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%20%20%22description%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22title%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%2C%0A%20%20%20%20%22within%22%3A%20%7B%22%40reverse%22%3A%20%22contains%22%7D%0A%20%20%7D%2C%0A%20%20%22%40type%22%3A%20%22Chapter%22%2C%0A%20%20%22within%22%3A%20%7B%0A%20%20%20%20%22%40type%22%3A%20%22Book%22%2C%0A%20%20%20%20%22within%22%3A%20%7B%0A%20%20%20%20%20%20%22%40type%22%3A%20%22Library%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {
>     "@vocab": "http://example.org/",
>     "within": {"@reverse": "contains"}
>   },
>   "@id": "http://example.org/library/the-republic#introduction",
>   "@type": "Chapter",
>   "description": "An introductory chapter on The Republic.",
>   "title": "The Introduction",
>   "within": {
>     "@id": "http://example.org/library/the-republic",
>     "@type": "Book",
>     "contains": {"@id": "http://example.org/library/the-republic#introduction"},
>     "creator": "Plato",
>     "title": "The Republic",
>     "within": {
>       "@id": "http://example.org/library",
>       "@type": "Library",
>       "location": "Athens",
>       "contains": {"@id": "http://example.org/library/the-republic"}
>     }
>   }
> }
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> There is an asymmetry between regular properties and reverse properties.
> Normally, when framing a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), unless the explicit inclusion flag is set,
> all properties of the node are included in the output, but reverse
> properties are not, as they are not actually properties of the node.
>
> To include reverse properties in the output, add them explicitly to the frame.
> Note that if the reverse relationship does not exist, it will simply be
> left out of the output.

### 2.5 Framing Named Graphs

*This section is non-normative.*

Frames can include `@graph`, which allows information from [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph) contained within a [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) to be exposed within it's proper
graph context. By default, framing uses a *merged graph*, composed of all
the [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) across all graphs within the input. By using `@graph` within a frame, the output document can include information specifically
from [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph) contained within the input document.

The following example uses a variation on our library theme where information
is split between the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph), and a graph named `http://example.org/graphs/books`:
> **Example:**
>
> Example 46: Frame with named graphs
>
>
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@type": "Library",
>   "contains": {
>     "@id": "http://example.org/graphs/books",
>     "@graph": {
>       "@type": "Book"
>     }
>   }
> }
> ```
> **Example:**
>
> Example 47: Flattened Input with named graphs
>
>
>
> ```
> [{
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/graphs/books",
>   "@graph": [{
>     "@id": "http://example.org/library/the-republic",
>     "@type": "http://example.org/Book",
>     "http://example.org/contains": {
>       "@id": "http://example.org/library/the-republic#introduction"
>     },
>     "http://example.org/creator": "Plato",
>     "http://example.org/title": "The Republic"
>   }, {
>     "@id": "http://example.org/library/the-republic#introduction",
>     "@type": "http://example.org/Chapter",
>     "http://example.org/description": "An introductory chapter on The Republic.",
>     "http://example.org/title": "The Introduction"
>   }]
> }, {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "http://example.org/Library",
>   "http://example.org/contains": {"@id": "http://example.org/graphs/books"},
>   "http://example.org/name": "Library"
> }]
> ```
> **Example:**
>
> Example 48: Framed output with named graphs
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-framed&json-ld=%5B%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Fgraphs%2Fbooks%22%2C%0A%20%20%22%40graph%22%3A%20%5B%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22http%3A%2F%2Fexample.org%2FBook%22%2C%0A%20%20%20%20%22http%3A%2F%2Fexample.org%2Fcontains%22%3A%20%7B%0A%20%20%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22http%3A%2F%2Fexample.org%2Fcreator%22%3A%20%22Plato%22%2C%0A%20%20%20%20%22http%3A%2F%2Fexample.org%2Ftitle%22%3A%20%22The%20Republic%22%0A%20%20%7D%2C%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%2Fthe-republic%23introduction%22%2C%0A%20%20%20%20%22%40type%22%3A%20%22http%3A%2F%2Fexample.org%2FChapter%22%2C%0A%20%20%20%20%22http%3A%2F%2Fexample.org%2Fdescription%22%3A%20%22An%20introductory%20chapter%20on%20The%20Republic.%22%2C%0A%20%20%20%20%22http%3A%2F%2Fexample.org%2Ftitle%22%3A%20%22The%20Introduction%22%0A%20%20%7D%5D%0A%7D%2C%20%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Flibrary%22%2C%0A%20%20%22%40type%22%3A%20%22http%3A%2F%2Fexample.org%2FLibrary%22%2C%0A%20%20%22http%3A%2F%2Fexample.org%2Fcontains%22%3A%20%7B%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Fgraphs%2Fbooks%22%7D%2C%0A%20%20%22http%3A%2F%2Fexample.org%2Fname%22%3A%20%22Library%22%0A%7D%5D&frame=%7B%0A%20%20%22%40context%22%3A%20%7B%22%40vocab%22%3A%20%22http%3A%2F%2Fexample.org%2F%22%7D%2C%0A%20%20%22%40type%22%3A%20%22Library%22%2C%0A%20%20%22contains%22%3A%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fexample.org%2Fgraphs%2Fbooks%22%2C%0A%20%20%20%20%22%40graph%22%3A%20%7B%0A%20%20%20%20%20%20%22%40type%22%3A%20%22Book%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {"@vocab": "http://example.org/"},
>   "@id": "http://example.org/library",
>   "@type": "Library",
>   "name": "Library",
>   "contains": {
>     "@id": "http://example.org/graphs/books",
>     "@graph": {
>       "@id": "http://example.org/library/the-republic",
>       "@type": "Book",
>       "creator": "Plato",
>       "title": "The Republic",
>       "contains": {
>         "@id": "http://example.org/library/the-republic#introduction",
>         "@type": "Chapter",
>         "description": "An introductory chapter on The Republic.",
>         "title": "The Introduction"
>       }
>     }
>   }
> }
> ```

## 3. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, *SHOULD*, and *SHOULD NOT* in this document
are to be interpreted as described in [BCP 14](https://tools.ietf.org/html/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all capitals, as shown here.

There is one class of products that can claim conformance to this
specification: [JSON-LD Processors](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor).

A conforming [JSON-LD Processor](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor) is a system which can perform the Framing (§4.1) operation in a manner consistent with
the algorithms defined in this specification.

[JSON-LD Processors](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor) *MUST NOT* attempt to correct malformed [IRIs](https://tools.ietf.org/html/rfc3987#section-2) or language tags;
however, they *MAY* issue validation warnings. IRIs are not modified other
than conversion between [relative](https://tools.ietf.org/html/rfc3987#section-6.5) and absolute [IRIs](https://tools.ietf.org/html/rfc3987#section-2).

Unless specified using [processingMode](https://www.w3.org/TR/json-ld11-api/#dom-jsonldoptions-processingmode) API option,
the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is set using the `@version` [entry](https://infra.spec.whatwg.org/#map-entry) in a local [context](https://www.w3.org/TR/json-ld11/#dfn-context) and
affects the behavior of algorithms including [expansion](https://www.w3.org/TR/json-ld11-api/#dfn-expanded) and [compaction](https://www.w3.org/TR/json-ld11-api/#dfn-compact).
Once set, it is an error to attempt to change to a different processing mode,
and processors *MUST* generate,
a [processing mode conflict](https://www.w3.org/TR/json-ld11-api/#dom-jsonlderrorcode-processing-mode-conflict) error and abort further processing.

The algorithms in this specification are generally written with more concern for clarity
than efficiency. Thus, [JSON-LD Processors](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor) *MAY* implement the algorithms given in this specification in any way desired,
so long as the end result is indistinguishable from the result that would
be obtained by the specification's algorithms.

In algorithm steps that describe operations on [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword), those steps
also apply to [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) aliases.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Implementers can partially check their level of conformance to
> this specification by successfully passing the test cases of the [JSON-LD framing test suite](https://w3c.github.io/json-ld-framing/tests/).
> Note, however, that passing all the tests in the test
> suite does not imply complete conformance to this specification. It only implies
> that the implementation conforms to aspects tested by the test suite.

## 4. Framing

The following sections describe algorithms for framing JSON-LD documents.
Framing is the process of taking a JSON-LD document, which expresses a
graph of information, and applying a specific graph layout
(called a Frame).

Framing makes use of the [Node Map Generation](https://www.w3.org/TR/json-ld11-api/#node-map-generation) algorithm
to place each object defined in the JSON-LD document into a map of flattened subjects, allowing
them to be operated upon by the §4.1 Framing Algorithm.

All algorithms described in this section are intended to operate on
language-native data structures. That is, the serialization to a text-based
JSON document isn't required as input or output to any of these algorithms.

Reference to JSON data structures are interpreted using their *internal representation* for the purpose
of describing algorithms.

### 4.1 Framing Algorithm

#### 4.1.1 Overview

A valid JSON-LD Frame is a superset of a valid [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document),
allowing additional content, which is preserved through expansion.
The [Grammar](https://www.w3.org/TR/json-ld11/#json-ld-grammar) defined in the JSON-LD 1.1 Syntax specification [JSON-LD11]
is extended as follows:

- Framing adds framing keywords which may be used as [entries](https://infra.spec.whatwg.org/#map-entry) of a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), which *MUST* be preserved when expanding.
- Values of [entries](https://infra.spec.whatwg.org/#map-entry) in a frame object that are not [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) *MAY* also include a [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object).
  Values of `@default` *MAY* include the value `@null`,
  or an [array](https://infra.spec.whatwg.org/#list) containing only `@null`, in addition to other values
  allowed in the grammar for values of [entry](https://infra.spec.whatwg.org/#map-entry) keys expanding to [IRIs](https://tools.ietf.org/html/rfc3987#section-2). [Processors](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor) *MUST* preserve this value when expanding. All other [entries](https://infra.spec.whatwg.org/#map-entry) of
  a [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object) *MUST* be ignored.
- The values of `@id` and `@type` may also be an empty [map](https://infra.spec.whatwg.org/#ordered-map), an [IRI reference](https://tools.ietf.org/html/rfc3987#section-1.3), [array](https://infra.spec.whatwg.org/#list) containing only an empty [map](https://infra.spec.whatwg.org/#ordered-map), or an array of [IRI references](https://tools.ietf.org/html/rfc3987#section-1.3). Values of `@type` *MAY* also be a [map](https://infra.spec.whatwg.org/#ordered-map) with
  a `@default` entry, whose values are restricted by be [IRIs](https://tools.ietf.org/html/rfc3987#section-2). [Processors](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor) *MUST* preserve this value when expanding.
- Framing either operates on the merged node definitions contained in
  the input document, or on the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) depending on if the
  input frame contains the `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) at the top level.
  Nodes with a [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) that is also a [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph), where
  the frame object contains `@graph`, extend framing
  to [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) from the associated [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph).

#### 4.1.2 Algorithm

The framing algorithm takes
five required input variables and one optional input variable.
The required inputs are
a framing state (*state*),
a list of *subjects* to frame,
an input frame (*expanded frame*),
a *parent* used to collect partial frame results,
and an *active property*.
The optional input variable is the `ordered` flag.

The algorithm adds elements to *parent* either by appending
the element to *parent*, if it is an [array](https://infra.spec.whatwg.org/#list), or by appending it
to an array associated with *active property* in *parent*, if it is a [map](https://infra.spec.whatwg.org/#ordered-map).
Note that if *parent* is an [array](https://infra.spec.whatwg.org/#list), *active property* *MUST* be `null`,
and if it is a [map](https://infra.spec.whatwg.org/#ordered-map), it *MUST NOT* be `null`.

1. If *frame* is an [array](https://infra.spec.whatwg.org/#list), set *frame* to the value of the [array](https://infra.spec.whatwg.org/#list), which *MUST* be a valid frame.
   If *frame* is determined to be invalid,
   an `invalid frame` error has been detected and processing is aborted.
   1. *Frame* *MUST* be a [map](https://infra.spec.whatwg.org/#ordered-map).
   2. If *frame* has an `@id` [entry](https://infra.spec.whatwg.org/#map-entry), its value *MUST* be
      either an [array](https://infra.spec.whatwg.org/#list) containing a single empty [map](https://infra.spec.whatwg.org/#ordered-map) as a value,
      a valid [IRI](https://tools.ietf.org/html/rfc3987#section-2) or an [array](https://infra.spec.whatwg.org/#list) where all values are valid [IRIs](https://tools.ietf.org/html/rfc3987#section-2).
   3. If *frame* has a `@type` [entry](https://infra.spec.whatwg.org/#map-entry), its value *MUST* be
      either an [array](https://infra.spec.whatwg.org/#list) containing a single empty [map](https://infra.spec.whatwg.org/#ordered-map) as a value,
      an [array](https://infra.spec.whatwg.org/#list) containing a [map](https://infra.spec.whatwg.org/#ordered-map) with a [entry](https://infra.spec.whatwg.org/#map-entry) whose key is `@default`,
      a valid [IRI](https://tools.ietf.org/html/rfc3987#section-2) or an [array](https://infra.spec.whatwg.org/#list) where all values are valid [IRIs](https://tools.ietf.org/html/rfc3987#section-2).
2. Initialize flags *embed*, *explicit*, and *requireAll* from object embed flag, explicit inclusion flag, and require all flag in *state* overriding from any property values
   for `@embed`, `@explicit`, and `@requireAll` in *frame*.
3. Create a list of matched subjects by filtering *subjects* against *frame* using the §4.2 Frame Matching Algorithm with *state*, *subjects*, *frame*, and *requireAll*.
4. For each *id* and associated [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) *node* from the set of matched subjects, ordered lexicographically by *id* if the optional `ordered` flag is `true`:
   1. Initialize *output* to a new [map](https://infra.spec.whatwg.org/#ordered-map) with `@id` and *id*.
   2. If the embedded flag in *state* is `false` and there is an existing embedded node in *parent* associated with *graph name* and *id* in *state*,
      do not perform additional processing for this *node*.
   3. Otherwise, if the embedded flag in *state* is `true` and either *embed* is `@never` or if a
      circular reference would be created by an embed,
      add *output* to *parent* and do not perform additional processing for this *node*.
   4. Otherwise, if the embedded flag in *state* is `true`, *embed* is `@once`,
      and there is an existing embedded node in *parent* associated with *graph name* and *id* in *state*,
      add *output* to *parent* and do not perform additional processing for this *node*.
   5. If *graph map* in *state* has an entry for *id*:
      1. If *frame* does not have a `@graph` [entry](https://infra.spec.whatwg.org/#map-entry),
         set *recurse* to `true`, unless *graph name* in *state* is `@merged` and set *subframe* to a new empty [map](https://infra.spec.whatwg.org/#ordered-map).
      2. Otherwise, set *subframe* to the first entry for `@graph` in *frame*,
         or a new empty [map](https://infra.spec.whatwg.org/#ordered-map), if it does not exist, and
         set *recurse* to `true`, unless *id* is `@merged` or `@default`.
      3. If *recurse* is `true`:
         1. Set the value of *graph name* in *state* to *id*.
         2. Set the value of embedded flag in *state* to `false`.
         3. Invoke the algorithm
            using a copy of *state* with the value of *graph name* set to *id* and the value of embedded flag set to `false`,
            the keys from the *graph map* in *state* associated with id as *subjects*, *subframe* as *frame*, *output* as *parent*, and `@graph` as *active property*.
   6. If *frame* has an `@included` [entry](https://infra.spec.whatwg.org/#map-entry),
      invoke the algorithm
      using a copy of *state* with the value of embedded flag set to `false`, *subjects*, *frame*, *output* as *parent*, and `@included` as *active property*.
   7. For each *property* and *objects* in *node*, ordered lexicographically by *property* if the optional `ordered` flag is `true`:
      1. If *property* is a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword), add *property* and *objects* to *output*.
      2. Otherwise, if *property* is not in *frame*, and *explicit* is `true`, [processors](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor) *MUST NOT* add any values for *property* to *output*, and the following
         steps are skipped.
      3. For each *item* in *objects*:
         1. If *item* is a [map](https://infra.spec.whatwg.org/#ordered-map) with the property `@list`, then each *listitem* in the list is processed in sequence and added to a new list [map](https://infra.spec.whatwg.org/#ordered-map) in output:
            1. If *listitem* is a [node reference](https://www.w3.org/TR/json-ld11/#dfn-node-reference),
               invoke the algorithm using a copy of *state* with the value of embedded flag set to `true`,
               the value of `@id` from *listitem* as the sole item in a new *subjects* [array](https://infra.spec.whatwg.org/#list),
               the first value from `@list` in *frame* as *frame*, *list* as *parent*, and `@list` as *active property*.
               If *frame* does not exist, create a new *frame* using a new [map](https://infra.spec.whatwg.org/#ordered-map) with properties for `@embed`, `@explicit` and `@requireAll` taken from *embed*, *explicit* and *requireAll*.
            2. Otherwise, append a copy of *listitem* to `@list` in *list*.
         2. If *item* is a [node reference](https://www.w3.org/TR/json-ld11/#dfn-node-reference),
            invoke the algorithm using a copy of *state* with the value of embedded flag set to `true`,
            the value of `@id` from *item* as the sole item in a new *subjects* [array](https://infra.spec.whatwg.org/#list),
            the first value from *property* in *frame* as *frame*, *output* as *parent*, and *property* as *active property*.
            If *frame* does not exist, create a new *frame* using a new [map](https://infra.spec.whatwg.org/#ordered-map) with properties for `@embed`, `@explicit` and `@requireAll` taken from *embed*, *explicit* and *requireAll*.
         3. Otherwise, append a copy of *item* to [active property](https://www.w3.org/TR/json-ld11-api/#dfn-active-property) in *output*.
      4. For each non-[keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) *property* and *objects* in *frame* (other than `@type) that is not in *output*:
         1. Let *item* be the first value in *objects*, which *MUST* be a frame object.
         2. Set *property frame* to the first value in *objects* or a newly created frame object if value is *objects*. *property frame* *MUST* be a [map](https://infra.spec.whatwg.org/#ordered-map).
         3. Skip *property* and *property frame* if *property frame* contains `@omitDefault` with a value of `true`,
            or does not contain `@omitDefault` and the value of
            the omit default flag in *state* is `true`.
         4. Add *property* to *output* with a
            new [map](https://infra.spec.whatwg.org/#ordered-map) having a property `@preserve` and
            a value that is a copy of the value of `@default` in *frame* if it exists, or the string `@null` otherwise.
      5. If *frame* has the property `@reverse`, then
         for each *reverse property* and *sub frame* that are the values of `@reverse` in *frame*:
         1. Create a `@reverse` property in *output* with a new [map](https://infra.spec.whatwg.org/#ordered-map) *reverse dict* as its value.
         2. For each *reverse id* and *node* in the map of flattened subjects that has the property *reverse property* containing a [node reference](https://www.w3.org/TR/json-ld11/#dfn-node-reference) with an `@id` of *id*:
            1. Add *reverse property* to *reverse dict* with a new empty [array](https://infra.spec.whatwg.org/#list) as its value.
            2. Invoke the algorithm using a copy of *state* with the value of embedded flag set to `true`,
               the *reverse id* as the sole item in a new *subjects* [array](https://infra.spec.whatwg.org/#list), *sub frame* as *frame*, `null` as *active property*,
               and the [array](https://infra.spec.whatwg.org/#list) value of *reverse property* in *reverse dict* as *parent*.
      6. Once output has been set are required in the previous steps,
         add *output* to *parent*.

### 4.2 Frame Matching Algorithm

The Frame Matching Algorithm is used as part of the §4.1 Framing Algorithm to determine if a particular [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) matches the criteria set in a frame.
In general, a node object matches a frame if it meets the matches on `@type`, `@id`,
or if it matches given one of several different properties.
If the require all flag is `true`, all properties must have defaults
or match for the frame to match.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> As matching is performed on expanded node objects, all values will be in the form of an array.

Node matching uses a combination of JSON constructs to match *any*, *zero*, or *some* specific values:

`[]` (`match none`)

An empty array matches no values, or a value which is, itself, an empty array.

`[frame object]` (`node pattern`)

A non-empty frame object, used to match specific values using recursive node matching.

`[IRI+]`

One or more strings in the form of an [IRI](https://tools.ietf.org/html/rfc3987#section-2), used for matching on `@type` and `@id`,
which allows a match on *any* of the listed IRIs.

`[value object]` (`value pattern`)

A [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object), used to match a specific value. Within a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object),
the values for `@value`, `@type`, and `@language` may also be an array of one or more [string](https://infra.spec.whatwg.org/#javascript-string) values, values of `@language` are compared without regard to case..

`{}` (`wildcard`)

An array containing an empty object
(after excluding any properties which are framing keywords)
matches any value that is present, and does not match if there are no values.

The frame matching algorithm takes the framing state (*state*),
a list of subjects to match from the map of flattened subjects (*subjects*),
a frame to match against (*frame*), and the *requireAll* flag
and returns a list of matched subjects by filtering each *node* in *subjects* as follows:

All properties, including `@id` and `@type`, but no other [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) are considered
when matching a frame.

1. *node* matches if frame has no properties.
2. If *requireAll* is **true**, *node* matches if all properties (*property*)
   in *frame* match any of the following conditions.
   Or, if *requireAll* is **false**, if any of the properties (*property*)
   in *frame* match any of the following conditions.
   For the *values* of each *property* from *frame* in *node*:
   1. If *property* is `@id`:

      1. *property* matches if the `@id` property in frame includes any [IRI](https://tools.ietf.org/html/rfc3987#section-2) in *values*.
      2. Otherwise, *property* matches if the `@type` property in *frame* is `wildcard` or `match none`.
      > **Note:**
      >
      > > **Note:**
      > >
      > > Note
      >
      > Framing works on map of flattened subjects,
      > and the act of flattening ensures that all subjects have an `@id` property; thus the `"@id": []` pattern would
      > never match any [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object). The `"@id": [{}]` pattern would
      > match any [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) and is equivalent to not specifying a `@id` property in *frame* at all

   2. Otherwise, if *property* is `@type`:

      1. *property* matches if the `@type` property in frame includes any [IRI](https://tools.ietf.org/html/rfc3987#section-2) in *values*.
      2. Otherwise, *property* matches if *values* is not empty and the `@type` property in *frame* is `wildcard`.
      3. Otherwise, *property* matches if *values* is empty and the `@type` property in *frame* is `match none`.
      4. Otherwise, *property* matches if the `@type` property in frame is a [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object).
      5. Otherwise, *property* does not match.

   3. If *property* is `@id` or `@type` and does not match, *node* does not match, and processing is terminated.

   4. Otherwise, the value of *property* in *frame* *MUST* be empty, or an array
      containing a valid frame.

   5. *property* matches if *values* is empty, or non existent,
      the value of *property* in *frame* is a [map](https://infra.spec.whatwg.org/#ordered-map) containing only the `@default` [entry](https://infra.spec.whatwg.org/#map-entry) with any value,
      and any other property in *node* has a non-default match.

   6. *node* does not match if *values* is not empty and the value of *property* in *frame* is `match none`, and further matching is aborted.

   7. Otherwise, *property* matches if *values* is not empty and the value of *property* in *frame* is `wildcard`.

   8. Otherwise, if the value of *property* in *frame* is a `value pattern` (*value pattern*):
      property matching is determined using the Value matching algorithm (§4.3).

   9. Otherwise, for any **node pattern** (*node pattern*) which is one of the values of *property* in *frame*:

      1. Let *value subjects* be the list of subjects from the map of flattened subjects matching the [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) values from *values*.
      2. Let *matched subjects* be the result of calling this algorithm recursively using *state*, *value subjects* for *subjects*, *node pattern* for *frame*, and the *requireAll* flag.
      3. *property* matches if *matched subjects* is not empty.

   10. Otherwise, *property* does not match.

### 4.3 Value Pattern Matching Algorithm

The Value Pattern Matching Algorithm is used as part of the Framing (§4.1) and Frame Matching (§4.2) algorithms. A value object
matches a value pattern using the `match none` and `wildcard` patterns on `@value`, `@type`, and `@language`, in addition to allowing a specific value to match a
set of values defined using the [array](https://infra.spec.whatwg.org/#list) form for each [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) property.

The algorithm takes a `value pattern` (*pattern*) and [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) (*value*) as parameters.
Value matches pattern using the following algorithm:

1. Let *v1*, *t1*, and *l1* be the values of `@value`, `@type`, and `@language` in *value*, or **null** if none exists, where values of `@language` are normalized to lower case..
2. Let *v2*, *t2*, and *l2* be the values of `@value`, `@type`, and `@language` in *value pattern*, or **null** if none exists, where string values of `@language` are normalized to lower case..
3. *Value* matches *pattern* when *pattern* is `wildcard`, or:
   1. *v1* is in *v2*, or *v1* is not **null** and *v2* is `wildcard`, and
   2. *t1* is in *t2*, or *t1* is not **null** and *t2* is `wildcard`, or **null**, or *t1* is `null` and *t2* is **null** or `match none`, and
   3. *l1* is in *l2*, or *l1* is not **null** and *l2* is `wildcard`, or **null**, or *l1* is `null` and *l2* is **null** or `match none`.

## 5. The Application Programming Interface

This API provides a clean mechanism that enables developers to convert
JSON-LD data into a variety of output formats that are easier to work with in
various programming languages. If a JSON-LD API is provided in a programming
environment, the entirety of the following API *MUST* be implemented.

The JSON-LD API uses [Promises](https://tc39.es/ecma262/#sec-promise-objects) to represent
the result of the various deferred operations. [Promises](https://tc39.es/ecma262/#sec-promise-objects) are defined in [ECMASCRIPT].
General use within specifications can be found in [promises-guide]. Implementations *MAY* chose to implement in an appropriate way for their native environments
as long as they generally use the same methods, arguments, and options
and return the same results.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Interfaces are marked `[Exposed=JsonLd]`,
> which creates a global interface.
> The use of WebIDL in JSON-LD, while appropriate for use within browsers,
> is not limited to such use.

### 5.1 JsonLdProcessor

The [JSON-LD Processor](https://www.w3.org/TR/json-ld11-api/#dfn-json-ld-processor) interface is the high-level programming structure that developers
use to access the JSON-LD transformation methods. The definition below is an experimental
extension of the interface defined in the JSON-LD 1.1 API [JSON-LD11-API].

It is important to highlight that implementations do not modify the input parameters.
If an error is detected, the [`Promise`](https://heycam.github.io/webidl/#idl-promise) is
rejected with a `JsonLdFramingError` having an appropriate `code` and processing is stopped.

```
WebIDL/*
 * The JsonLd interface is created to expose the JsonLdProcessor interface.
 */
[Global=JsonLd, Exposed=JsonLd]
interface JsonLd {};

[Exposed=JsonLd]
interface JsonLdProcessor {
  constructor();
  static Promise<JsonLdRecord> frame(
    JsonLdInput input,
    JsonLdInput frame,
    optional JsonLdOptions options = {});
};
```

The *`JsonLdProcessor`* interface *`frame()`* method Frames (§2.1) the given `input` using frame according to the steps in the §4.1 Framing Algorithm:

1. Create a new [`Promise`](https://heycam.github.io/webidl/#idl-promise) *promise* and return it. The
   following steps are then executed asynchronously.

2. If the provided input is a [RemoteDocument](https://www.w3.org/TR/json-ld11-api/#dom-remotedocument),
   initialize *remote document* to input.

3. Otherwise, if the provided input is a [string](https://infra.spec.whatwg.org/#javascript-string) representing the [IRI](https://tools.ietf.org/html/rfc3987#section-2) of a remote document, await and dereference it as *remote document* using [LoadDocumentCallback](https://www.w3.org/TR/json-ld11-api/#dom-loaddocumentcallback), passing input for *url*,
   and the [extractAllScripts](https://www.w3.org/TR/json-ld11-api/#dom-loaddocumentoptions-extractallscripts) option from options for *extractAllScripts*.

4. Set *expanded input* to the result of using the [expand](https://www.w3.org/TR/json-ld11-api/#dom-jsonldprocessor-expand) method either *remote document* or input if there is no *remote document* for [input](https://www.w3.org/TR/json-ld11-api/#dfn-jsonldprocessor-expand-input) and options with `ordered` set to `false`.

5. If the provided frame is a [RemoteDocument](https://www.w3.org/TR/json-ld11-api/#dom-remotedocument),
   initialize *remote frame* to frame.

6. Otherwise, if the provided frame is a [string](https://infra.spec.whatwg.org/#javascript-string) representing the [IRI](https://tools.ietf.org/html/rfc3987#section-2) of a remote document, await and dereference it as *remote frame* using [LoadDocumentCallback](https://www.w3.org/TR/json-ld11-api/#dom-loaddocumentcallback), passing frame for *url*,
   and the [extractAllScripts](https://www.w3.org/TR/json-ld11-api/#dom-loaddocumentoptions-extractallscripts) option from options for *extractAllScripts*.

7. Set *expanded frame* to the result of using the [expand](https://www.w3.org/TR/json-ld11-api/#dom-jsonldprocessor-expand) method either *remote frame* or frame if there is no *remote frame* for [input](https://www.w3.org/TR/json-ld11-api/#dfn-jsonldprocessor-expand-input) options the [frameExpansion](https://www.w3.org/TR/json-ld11-api/#dom-jsonldoptions-frameexpansion) option set to `true`, and the`ordered` set to `false`.

8. Set *context* to the value of `@context` from *remote frame* or frame, if it exists, or to
   a new empty [context](https://www.w3.org/TR/json-ld11/#dfn-context), otherwise.

9. Set *context base* to the [`documentUrl`](https://www.w3.org/TR/json-ld11-api/#dom-remotedocument-documenturl) from *remote frame*, if available, otherwise to the [`base`](https://www.w3.org/TR/json-ld11-api/#dom-jsonldoptions-base) option
   from options.

10. Initialize *active context* to the result of the [Context Processing algorithm](https://www.w3.org/TR/json-ld11-api/#context-processing-algorithm) passing a new empty [context](https://www.w3.org/TR/json-ld11/#dfn-context) as *active context* *context* as *local context*,
    and *context base* as *base URL*.

11. Initialize an [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) using *context*;
    the [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri) is set to
    the [base](https://www.w3.org/TR/json-ld11-api/#dom-jsonldoptions-base) option from options, if set;
    otherwise, if the [compactToRelative](https://www.w3.org/TR/json-ld11-api/#dom-jsonldoptions-compacttorelative) option is **true**, to the IRI of the currently being processed
    document, if available; otherwise to `null`.

12. Initialize *inverse context* to the result of performing the [Inverse Context Creation algorithm](https://www.w3.org/TR/json-ld11-api/#inverse-context-creation).

13. If frame has a top-level
    property which expands to `@graph` set the `frameDefault` option to options with the
    value `true`.

14. Initialize a new framing state (*state*) to an empty [map](https://infra.spec.whatwg.org/#ordered-map).

    1. Set object embed flag in *state* to `embed` with the default value `@once`.
    2. Set the *embedded flag* in *state* to `false`
    3. Set explicit inclusion flag in *state* to `explicit` with the default value `false`.
    4. Set require all flag in *state* to `requireAll` with the default value `false`.
    5. Set omit default flag in *state* to `omitDefault` with the default value `false`.
    6. Set the *graph name* in *state* to
       either `@default` if `frameDefault` is `true`,
       otherwise to `false`.
    7. Set the *graph map* in *state* to the result of performing the [Node Map Generation](https://www.w3.org/TR/json-ld11-api/#node-map-generation) algorithm on *expanded input*.
       1. If *graph name* in *state* is `@merged`,
          add en entry for `@merged` in *graph map* set
          to the result of the [Merge Node Maps](https://www.w3.org/TR/json-ld11-api/#merge-node-maps) algorithm
          passing *graph map*.
    8. Set *subject map* in *state* to the map of flattened subjects which is the value of *graph name* in *graph map*.
    9.

15. Initialize *results* as an empty [array](https://infra.spec.whatwg.org/#list).

16. Invoke the §4.1 Framing Algorithm, passing *state*,
    the keys from *subject map* in *state* for *subjects*, *expanded frame*, *results* for *parent*,
    and `null` as *active property*.

17. If the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is not `json-ld-1.0`,
    remove the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) of each [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) in *results* where the [entry](https://infra.spec.whatwg.org/#map-entry) value is a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) which appears only once
    in any property value within *results*.

18. Recursively, replace all [entries](https://infra.spec.whatwg.org/#map-entry) in *results* where the key is `@preserve` with the first value of that [entry](https://infra.spec.whatwg.org/#map-entry).
    > **Note:**
    >
    > > **Note:**
    > >
    > > Note
    >
    > The value of the entry will be an array with a single value;
    > this will effectively replace the map containing `@preserve` with that value.

19. Set *compacted results* to the result of using the `compact` method using *active context*, *inverse context*, `null` for *active property*, *results* as *element*,,
    and the [`compactArrays`](https://www.w3.org/TR/json-ld11-api/#dom-jsonldoptions-compactarrays) and `ordered` flags from options.

    1. If *compacted results* is an empty [array](https://infra.spec.whatwg.org/#list),
       replace it with a new [map](https://infra.spec.whatwg.org/#ordered-map).
    2. Otherwise, if *compacted results* is an [array](https://infra.spec.whatwg.org/#list),
       replace it with a new [map](https://infra.spec.whatwg.org/#ordered-map) with a single [entry](https://infra.spec.whatwg.org/#map-entry) whose key is the result of [IRI compacting](https://www.w3.org/TR/json-ld11-api/#dfn-iri-compacting) `@graph` and value is *compacted results*.
    3. Add an `@context` [entry](https://infra.spec.whatwg.org/#map-entry) to *compacted results* and set its value
       to the provided *context*.

20. Recursively, replace all `@null` values in *compacted results* with `null`.
    If, after replacement, an [array](https://infra.spec.whatwg.org/#list) contains only the value `null` remove that value, leaving
    an empty array.

21. If `omitGraph` is `false` and *compacted results* does not have a top-level `@graph` [entry](https://infra.spec.whatwg.org/#map-entry), or its value is
    not an [array](https://infra.spec.whatwg.org/#list), modify *compacted results* to place the non `@context` [entry](https://infra.spec.whatwg.org/#map-entry) of *compacted results* into a [map](https://infra.spec.whatwg.org/#ordered-map) contained within the [array](https://infra.spec.whatwg.org/#list) value of `@graph`. If `omitGraph` is `true`, a
    top-level `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) is used only to contain multiple [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object).

22. Resolve the *promise* with *compacted results*,
    transforming *compacted results* from the [internal representation](https://www.w3.org/TR/json-ld11-api/#dfn-internal-representation) to a JSON serialization.

*input*

The JSON-LD object or array of JSON-LD objects to perform the framing upon or an [IRI](https://tools.ietf.org/html/rfc3987#section-2) referencing the JSON-LD document to frame.

*frame*

The frame to use when re-arranging the data of `input`; either
in the form of an [map](https://infra.spec.whatwg.org/#ordered-map) or as [IRI](https://tools.ietf.org/html/rfc3987#section-2).

*options*

A set of options that *MAY* affect the framing algorithm such as, e.g., the
input document's base [IRI](https://tools.ietf.org/html/rfc3987#section-2). The `JsonLdOptions` type defines default option values.

```
WebIDLtypedef record<USVString, any> JsonLdRecord;
```

The *`JsonLdRecord`* is the definition of a [map](https://infra.spec.whatwg.org/#ordered-map) used to contain arbitrary [map entries](https://infra.spec.whatwg.org/#map-entry) which are the result of parsing a [JSON Object](https://tools.ietf.org/html/rfc8259#section-4).

```
WebIDLtypedef (JsonLdRecord or sequence<JsonLdRecord> or USVString or RemoteDocument) JsonLdInput;
```

The *`JsonLdInput`* interface is used to refer to an input value
that that may be a `JsonLdRecord`,
a `sequence` of JsonLdRecords,
a [string](https://infra.spec.whatwg.org/#javascript-string) representing an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
which can be dereferenced to retrieve a valid JSON document, or an already dereferenced [RemoteDocument](https://www.w3.org/TR/json-ld11-api/#dom-remotedocument).

When the value is a `JsonLdRecord` or sequence of JsonLdRecords,
the values are taken as their equivalent internal representation values,
where a `JsonLdRecord` is equivalent to a [map](https://infra.spec.whatwg.org/#ordered-map),
and a sequence of JsonLdRecords is equivalent to an [array](https://infra.spec.whatwg.org/#list) of [maps](https://infra.spec.whatwg.org/#ordered-map). The [map entries](https://infra.spec.whatwg.org/#map-entry) are converted to their equivalents
in [INFRA].

### 5.2 Error Handling

The *`JsonLdFramingError`* type is used to report processing errors.

```
WebIDLdictionary JsonLdFramingError {
  JsonLdFramingErrorCode code;
  USVString? message = null;
};
enum JsonLdFramingErrorCode {
  "invalid frame",
  "invalid @embed value"
};
```

JSON-LD Framing extends the error interface and codes defined in [JSON-LD 1.1 Processing Algorithms and API](https://www.w3.org/TR/json-ld11-api/#error-handling) the JSON-LD 1.1 API [JSON-LD11-API].

*`code`*

a string representing the particular error type, as described in
the various algorithms in this document.

*`message`*

an optional error message containing additional debugging information.
The specific contents of error messages are outside the scope of this
specification.

The *`JsonLdFramingErrorCode`* represents the collection of valid JSON-LD Framing error
codes.

*`invalid @embed value`*

The value for `@embed` is not one recognized for the object embed flag.

*`invalid frame`*

The frame is invalid.

### 5.3 Data Structures

This section describes datatype definitions used within the JSON-LD API.

#### 5.3.1 JsonLdContext

The [JsonLdContext](https://www.w3.org/TR/json-ld11-api/#dom-jsonldcontext) type is used to refer to a value that
that may be a [map](https://infra.spec.whatwg.org/#ordered-map), a [string](https://infra.spec.whatwg.org/#javascript-string) representing an [IRI](https://tools.ietf.org/html/rfc3987#section-2), or an array of [maps](https://infra.spec.whatwg.org/#ordered-map) and [strings](https://infra.spec.whatwg.org/#javascript-string).

See [JsonLdContext](https://www.w3.org/TR/json-ld11-api/#dom-jsonldcontext) definition in the JSON-LD 1.1 API [JSON-LD11-API].

#### 5.3.2 JsonLdOptions

The *`JsonLdOptions`* type is used to pass various options to the `JsonLdProcessor` methods.

```
WebIDLdictionary JsonLdOptions {
  (JsonLdEmbed or boolean)  embed         = "@once";
  boolean                   explicit      = false;
  boolean                   omitDefault   = false;
  boolean                   omitGraph;
  boolean                   requireAll    = false;
  boolean                   frameDefault  = false;
  boolean                   ordered       = false;
};

enum JsonLdEmbed {
  "@always",
  "@once",
  "@never"
};
```

In addition to those options defined in the JSON-LD 1.1 API [JSON-LD11-API], framing defines these
additional options:

*`embed`*

Sets the value object embed flag used in the §4.1 Framing Algorithm.
A boolean value of `true` sets the flag to `@once`, while a value of `false` sets the flag
to `@never`.

*`explicit`*

Sets the value explicit inclusion flag used in the §4.1 Framing Algorithm.

*`frameDefault`*

Instead of framing a *merged graph*, frame only the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph).

*`omitDefault`*

Sets the value omit default flag used in the §4.1 Framing Algorithm

*`omitGraph`*

Sets the value omit graph flag used in the §4.1 Framing Algorithm. If not set explicitly,
it is set to `false` if [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`, `true` otherwise.

*`ordered`*

If set to `true`, certain algorithm
processing steps where indicated are ordered lexicographically.
If `false`, order
is not considered in processing.

*`requireAll`*

Sets the value require all flag used in the §4.1 Framing Algorithm.

*`JsonLdEmbed`* enumerates the values of the `embed` option:

*`@always`*

Always embed [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) as property values, unless this would
cause a circular reference.

*`@never`*

Always use a [node reference](https://www.w3.org/TR/json-ld11/#dfn-node-reference) when serializing matching values.

*`@once`*

Only a single value within a given [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) should be embedded,
other values of other properties use a [node reference](https://www.w3.org/TR/json-ld11/#dfn-node-reference). This is the
default value if neither `@embed` nor object embed flag is specified.

See [JsonLdOptions](https://www.w3.org/TR/json-ld11-api/#dom-jsonldoptions) definition in the JSON-LD 1.1 API [JSON-LD11-API].

## 6. Security Considerations

See, Security Considerations in § A. IANA Considerations (§A).

## 7. Privacy Considerations

See, [Privacy Considerations](https://www.w3.org/TR/json-ld11/#privacy) in [JSON-LD11].

## 8. Internationalization Considerations

See, [Internationalization Considerations](https://www.w3.org/TR/json-ld11/#internationalization) in [JSON-LD11].

## A. IANA Considerations

This section is included merely for standards community review and will be
submitted to the Internet Engineering Steering Group if this specification
becomes a W3C Recommendation.

A JSON-LD Frame uses the same MIME media type described in [JSON-LD11]
along with a required `profile` parameter.

### application/ld+json

Type name:

application

Subtype name:

ld+json

Required parameters:

None

Optional parameters:

`profile`

A single URI identifying the resource as a JSON-LD Frame.
A profile does not change the semantics of the resource representation
when processed without profile knowledge, so that clients both with
and without knowledge of a profiled resource can safely use the same
representation.

`http://www.w3.org/ns/json-ld#framed`

To specify a JSON-LD Frame.

The `http://www.w3.org/ns/json-ld#framed` *SHOULD* be used when serving and requesting a JSON-LD frame document.

Encoding considerations:

See [RFC 8259, section 11](https://tools.ietf.org/html/rfc8259#section-11).

Security considerations:

See [RFC 8259, section 12](https://tools.ietf.org/html/rfc8259#section-12) [RFC8259]

Since JSON-LD is intended to be a pure data exchange format for
directed graphs, the serialization *SHOULD NOT* be passed through a
code execution mechanism such as JavaScript's `eval()` function to be parsed. An (invalid) document may contain code that,
when executed, could lead to unexpected side effects compromising
the security of a system.

When processing JSON-LD documents, links to remote contexts are
typically followed automatically, resulting in the transfer of files
without the explicit request of the user for each one. If remote
contexts are served by third parties, it may allow them to gather
usage patterns or similar information leading to privacy concerns.
Specific implementations, such as the API defined in the
JSON-LD 1.1 Processing Algorithms and API specification [JSON-LD11-API],
may provide fine-grained mechanisms to control this behavior.

JSON-LD contexts that are loaded from the Web over non-secure connections,
such as HTTP, run the risk of being altered by an attacker such that
they may modify the JSON-LD [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) in a way that
could compromise security. It is advised that any application that
depends on a remote context for mission critical purposes vet and
cache the remote context before allowing the system to use it.

Given that JSON-LD allows the substitution of long IRIs with short terms,
JSON-LD documents may expand considerably when processed and, in the worst case,
the resulting data might consume all of the recipient's resources. Applications
should treat any data with due skepticism.

As JSON-LD places no limits on the IRI schemes that may be used,
and vocabulary-relative IRIs use string concatenation rather than IRI resolution, it is possible to construct IRIs that may be
used maliciously, if dereferenced.

Interoperability considerations:

Not Applicable

Published specification:

https://www.w3.org/TR/json-ld11-framing

Applications that use this media type:

Any programming environment that requires the exchange of
directed graphs. Implementations of JSON-LD have been created for
JavaScript, Python, Ruby, PHP, and C++.

Additional information:

Magic number(s):

Not Applicable

File extension(s):

.jsonld

Macintosh file type code(s):

TEXT

Person & email address to contact for further information:

Ivan Herman <ivan@w3.org>

Intended usage:

Common

Restrictions on usage:

None

Author(s):

Manu Sporny, Gregg Kellogg, Markus Lanthaler, Dave Longley

Change controller:

W3C

Fragment identifiers used with application/ld+json are treated as in RDF syntaxes, as per [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/#section-fragID) [RDF11-CONCEPTS].

## B. IDL Index

*This section is non-normative.*

```
WebIDL/*
 * The JsonLd interface is created to expose the JsonLdProcessor interface.
 */
[Global=JsonLd, Exposed=JsonLd]
interface JsonLd {};

[Exposed=JsonLd]
interface JsonLdProcessor {
  constructor();
  static Promise<JsonLdRecord> frame(
    JsonLdInput input,
    JsonLdInput frame,
    optional JsonLdOptions options = {});
};

typedef record<USVString, any> JsonLdRecord;

typedef (JsonLdRecord or sequence<JsonLdRecord> or USVString or RemoteDocument) JsonLdInput;

dictionary JsonLdFramingError {
  JsonLdFramingErrorCode code;
  USVString? message = null;
};
enum JsonLdFramingErrorCode {
  "invalid frame",
  "invalid @embed value"
};

dictionary JsonLdOptions {
  (JsonLdEmbed or boolean)  embed         = "@once";
  boolean                   explicit      = false;
  boolean                   omitDefault   = false;
  boolean                   omitGraph;
  boolean                   requireAll    = false;
  boolean                   frameDefault  = false;
  boolean                   ordered       = false;
};

enum JsonLdEmbed {
  "@always",
  "@once",
  "@never"
};
```

## C. Open Issues

*This section is non-normative.*

The following is a list of issues open at the time of publication.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 29](https://github.com/w3c/json-ld-framing/issues/29): Allow class-scoped framing [defer-future-version](https://github.com/w3c/json-ld-framing/issues/?q=is%3Aissue+is%3Aopen+label%3A%22defer-future-version%22)[spec:enhancement](https://github.com/w3c/json-ld-framing/issues/?q=is%3Aissue+is%3Aopen+label%3A%22spec%3Aenhancement%22)
>
> Allow class-scoped framing.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 38](https://github.com/w3c/json-ld-framing/issues/38): Several frames in the same frame document? [defer-future-version](https://github.com/w3c/json-ld-framing/issues/?q=is%3Aissue+is%3Aopen+label%3A%22defer-future-version%22)[spec:enhancement](https://github.com/w3c/json-ld-framing/issues/?q=is%3Aissue+is%3Aopen+label%3A%22spec%3Aenhancement%22)[spec:substantive](https://github.com/w3c/json-ld-framing/issues/?q=is%3Aissue+is%3Aopen+label%3A%22spec%3Asubstantive%22)
>
> Several frames in the same frame document?
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 73](https://github.com/w3c/json-ld-framing/issues/73): Reframing Relationships [defer-future-version](https://github.com/w3c/json-ld-framing/issues/?q=is%3Aissue+is%3Aopen+label%3A%22defer-future-version%22)
>
> Reframing Relationships.

## D. Changes since 1.0 Draft of 30 August 2012

*This section is non-normative.*

- There are numerous formatting and terminology changes intended to align with
  the 1.0 Recommendations of JSON-LD and JSON-LD-API in addition to the use
  of common term definition sections.
- The object embed flag (`@embed`) can take on different
  values to better control object embedding.
- Framing supports *More specific frame matching*, where
  general `wildcard` and `match none` can be used for type and property values.
- Frame matching also supports value object matching, where
  values for `@value`, `@type`, and `@language` can use `wildcard` and `match none` and may also use a set of specific strings to match (e.g., a set of specific
  languages).
- Framing allows specific graphs to be matched, and the outer-most frame
  can either come from the merged graph or the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph).
- Framing supports `@reverse`.
- Through the use of *scoped contexts*, parts of a frame can be
  compacted using a different context than is used for the outer-most
  object.
- Frames can use one or more values for `@id` to allow for matching
  specific objects in a frame.
- If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is not `json-ld-1.0`, `@id` [entries](https://infra.spec.whatwg.org/#map-entry) with [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) used only for that `@id` are removed.
- The JSON syntax has been abstracted into an [internal representation](https://www.w3.org/TR/json-ld11-api/#dfn-internal-representation) to allow for other serialization formats that are functionally equivalent
  to JSON.
- Preserved values are compacted using the properties of the referencing term.
- Removed support for `@link` and in-memory object linking.
- Added the omit default flag, controlled via the `omitDefault` API option and/or
  the current [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode).
- The API now adds an `ordered` option, defaulting to `false` This is used in algorithms to
  control iteration of [map entry](https://infra.spec.whatwg.org/#map-entry) keys. Previously, the
  algorithms always required such an order. The instructions for
  evaluating test results have been updated accordingly.
- Frames may include reverse properties using `@reverse`, or a term
  defined with `@reverse`, which can cause nodes referencing a
  node targeted by a frame to have a reverse reference created.

## E. Changes since JSON-LD Community Group Final Report

*This section is non-normative.*

- The API now adds an `ordered` option, defaulting to `false` This is used in algorithms to
  control iteration of [map entry](https://infra.spec.whatwg.org/#map-entry) keys. Previously, the
  algorithms always required such an order. The instructions for
  evaluating test results have been updated accordingly.
- The IANA registration is changed from `application/ld-frame+json` to `application/ld+json` with a required `profile` parameter.
- The require all flag now needs all properties to be present, including `@id` and `@type`.
- Removed `@first` and `@last` values for the object embed flag in favor of `@once`.
- The [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is now implicitly `json-ld-1.1`, unless set
  explicitly to `json-ld-1.0`.
- In a frame `@type` can have a default value, which is not used for
  frame matching purposes.

## F. Changes since Candidate Release of 12 December 2019

*This section is non-normative.*

- Removed duplicate § 1.1 How to Read this Document (§1.1).
  This is in response to [Issue 92](https://github.com/w3c/json-ld-framing/issues/92).
- Improved algorithms in § 4.1 Framing Algorithm (§4.1).
- Moved non-recursive portions algorithms
  into the `JsonLdProcessor` processing steps.
- Remove the *graph stack* from framing state as being unnecessary.

## G. Changes since Proposed Recommendation Release of 7 May 2020

*This section is non-normative.*

- Changed `[Exposed=(Window,Worker)]` to `[Exposed=JsonLd]`,
  which is declared as a global interface in order to expose the `JsonLdProcessor` interface
  for non-browser usage to address review suggestions.

## I. References

### I.1 Normative references

[BCP47]

[Tags for Identifying Languages](https://tools.ietf.org/html/bcp47). A. Phillips; M. Davis. IETF. September 2009. IETF Best Current Practice. URL: <https://tools.ietf.org/html/bcp47>

[ECMASCRIPT]

[ECMAScript Language Specification](https://tc39.es/ecma262/). Ecma International. URL: <https://tc39.es/ecma262/>

[INFRA]

[Infra Standard](https://infra.spec.whatwg.org/). Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: <https://infra.spec.whatwg.org/>

[JSON-LD10]

[JSON-LD 1.0](https://www.w3.org/TR/2014/REC-json-ld-20140116/). Manu Sporny; Gregg Kellogg; Marcus Langhaler. W3C. 16 January 2014. W3C Recommendation. URL: <https://www.w3.org/TR/2014/REC-json-ld-20140116/>

[JSON-LD11]

[JSON-LD 1.1](https://www.w3.org/TR/json-ld11/). Gregg Kellogg; Pierre-Antoine Champin; Dave Longley. W3C. 7 May 2020. W3C Proposed Recommendation. URL: <https://www.w3.org/TR/json-ld11/>

[JSON-LD11-API]

[JSON-LD 1.1 Processing Algorithms and API](https://www.w3.org/TR/json-ld11-api/). Gregg Kellogg; Dave Longley; Pierre-Antoine Champin. W3C. 7 May 2020. W3C Proposed Recommendation. URL: <https://www.w3.org/TR/json-ld11-api/>

[LINKED-DATA]

[Linked Data Design Issues](https://www.w3.org/DesignIssues/LinkedData.html). Tim Berners-Lee. W3C. 27 July 2006. W3C-Internal Document. URL: <https://www.w3.org/DesignIssues/LinkedData.html>

[promises-guide]

[Writing Promise-Using Specifications](https://www.w3.org/2001/tag/doc/promises-guide). Domenic Denicola. W3C. 9 November 2018. TAG Finding. URL: <https://www.w3.org/2001/tag/doc/promises-guide>

[RDF-SCHEMA]

[RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/). Dan Brickley; Ramanathan Guha. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-schema/>

[RDF11-CONCEPTS]

[RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). Richard Cyganiak; David Wood; Markus Lanthaler. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf11-concepts/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://tools.ietf.org/html/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://tools.ietf.org/html/rfc2119>

[RFC3987]

[Internationalized Resource Identifiers (IRIs)](https://tools.ietf.org/html/rfc3987). M. Duerst; M. Suignard. IETF. January 2005. Proposed Standard. URL: <https://tools.ietf.org/html/rfc3987>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://tools.ietf.org/html/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://tools.ietf.org/html/rfc8174>

[RFC8259]

[The JavaScript Object Notation (JSON) Data Interchange Format](https://tools.ietf.org/html/rfc8259). T. Bray, Ed.. IETF. December 2017. Internet Standard. URL: <https://tools.ietf.org/html/rfc8259>

[WEBIDL]

[Web IDL](https://heycam.github.io/webidl/). Boris Zbarsky. W3C. 15 December 2016. W3C Editor's Draft. URL: <https://heycam.github.io/webidl/>

### I.2 Informative references

[JSON-LD10-FRAMING]

[JSON-LD Framing 1.0](https://json-ld.org/spec/ED/json-ld-framing/20120830/). Manu Sporny; Gregg Kellogg; David Longley; Marcus Langhaler. W3C. 30 August 2012. Unofficial Draft. URL: <https://json-ld.org/spec/ED/json-ld-framing/20120830/>
