---
title: "JSON-LD 1.1 Processing Algorithms and API"
source: https://www.w3.org/TR/json-ld-api/
family: jsonld
version: "1.1"
status: W3C Recommendation
spec_date: 2020-07-16
fetched: 2026-11-09
---

# JSON-LD 1.1 Processing Algorithms and API

> Expansion, compaction, flattening algorithms.

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
    - 1.4.2 Syntax Tokens and Keywords
  - 1.5 Example Conventions
- 2 Features
  - 2.1 Expansion
  - 2.2 Compaction
  - 2.3 Flattening
  - 2.4 RDF Serialization/Deserialization
- 3 Conformance
- 4 Context Processing Algorithms
  - 4.1 Context Processing Algorithm
    - 4.1.1 Overview
    - 4.1.2 Algorithm
  - 4.2 Create Term Definition
    - 4.2.1 Overview
    - 4.2.2 Algorithm
  - 4.3 Inverse Context Creation
    - 4.3.1 Overview
    - 4.3.2 Algorithm
  - 4.4 Term Selection
    - 4.4.1 Overview
    - 4.4.2 Algorithm
    - 4.4.3 Examples
- 5 Expansion Algorithms
  - 5.1 Expansion Algorithm
    - 5.1.1 Overview
    - 5.1.2 Algorithm
  - 5.2 IRI Expansion
    - 5.2.1 Overview
    - 5.2.2 Algorithm
  - 5.3 Value Expansion
    - 5.3.1 Overview
    - 5.3.2 Algorithm
- 6 Compaction Algorithms
  - 6.1 Compaction Algorithm
    - 6.1.1 Overview
    - 6.1.2 Algorithm
  - 6.2 IRI Compaction
    - 6.2.1 Overview
    - 6.2.2 Algorithm
  - 6.3 Value Compaction
    - 6.3.1 Overview
    - 6.3.2 Algorithm
- 7 Flattening Algorithms
  - 7.1 Flattening Algorithm
    - 7.1.1 Overview
    - 7.1.2 Algorithm
  - 7.2 Node Map Generation
    - 7.2.1 Overview
    - 7.2.2 Algorithm
  - 7.3 Merge Node Maps
  - 7.4 Generate Blank Node Identifier
    - 7.4.1 Overview
    - 7.4.2 Algorithm
- 8 RDF Serialization/Deserialization Algorithms
  - 8.1 Deserialize JSON-LD to RDF Algorithm
    - 8.1.1 Overview
    - 8.1.2 Algorithm
  - 8.2 Object to RDF Conversion
    - 8.2.1 Overview
    - 8.2.2 Algorithm
  - 8.3 List to RDF Conversion
    - 8.3.1 Overview
    - 8.3.2 Algorithm
  - 8.4 Serialize RDF as JSON-LD Algorithm
    - 8.4.1 Overview
    - 8.4.2 Algorithm
  - 8.5 RDF to Object Conversion
    - 8.5.1 Overview
    - 8.5.2 Algorithm
  - 8.6 Data Round Tripping
- 9 The Application Programming Interface
  - 9.1 The JsonLdProcessor Interface
  - 9.2 RDF Dataset Interfaces
  - 9.3 The JsonLdOptions Type
  - 9.4 Remote Document and Context Retrieval
    - 9.4.1 LoadDocumentCallback
    - 9.4.2 LoadDocumentOptions
    - 9.4.3 RemoteDocument
  - 9.5 HTML Content Algorithms
    - 9.5.1 Process HTML
    - 9.5.2 Extract Script Content Algorithm
  - 9.6 Error Handling
    - 9.6.1 JsonLdError
    - 9.6.2 JsonLdErrorCode
- 10 Security Considerations
- 11 Privacy Considerations
- 12 Internationalization Considerations
- A IDL Index
- B Open Issues
- C Changes since 1.0 Recommendation of 16 January 2014
- D Changes since JSON-LD Community Group Final Report
- E Changes since Candidate Release of 12 December 2019
- F Changes since Candidate Release of 05 March 2020
- G Changes since Proposed Recommendation Release of 7 May 2020
- I References
  - I.1 Normative references
  - I.2 Informative references

---

## Abstract

This specification defines a set of algorithms for programmatic transformations
of JSON-LD documents. Restructuring data according to the defined transformations
often dramatically simplifies its usage. Furthermore, this document proposes
an Application Programming Interface (API) for developers implementing the
specified algorithms.

This specification describes a superset of the features defined in [JSON-LD 1.0 Processing Algorithms And API](https://www.w3.org/TR/2014/REC-json-ld-api-20140116/) [JSON-LD10-API]
and, except where noted,
the algorithms described in this specification are fully compatible
with documents created using [JSON-LD 1.0](https://www.w3.org/TR/2014/REC-json-ld-20140116/) [JSON-LD10].

## 1. Introduction

*This section is non-normative.*

This document is a detailed specification of the JSON-LD processing algorithms.
The document is primarily intended for the following audiences:

- Software developers who want to implement the algorithms to transform
  JSON-LD documents.
- Web authors and developers who want a very detailed view of how
  a JSON-LD Processor operates.
- Developers who want an overview of the proposed JSON-LD API.

To understand the basics in this specification you must first be familiar with [JSON](https://tools.ietf.org/html/rfc8259), which is detailed in [RFC8259]. You must also understand the
JSON-LD syntax defined in the [JSON-LD 1.1 Syntax specification](https://www.w3.org/TR/json-ld11/) [JSON-LD11], which is the base syntax used by all
of the algorithms in this document. To understand the API and how it is
intended to operate in a programming environment, it is useful to have working
knowledge of the JavaScript programming language [ECMASCRIPT] and
WebIDL [WEBIDL]. To understand how JSON-LD maps to RDF, it is helpful to be
familiar with the basic RDF concepts [RDF11-CONCEPTS].

### 1.1 How to Read this Document

*This section is non-normative.*

This document is a detailed specification for a serialization of Linked
Data in JSON. The document is primarily intended for the following audiences:

- Software developers who want to implement processors and APIs for
  JSON-LD

A companion document, the JSON-LD 1.1 specification
[JSON-LD11], specifies the grammar of JSON-LD documents.

To understand the basics in this specification you must first be familiar with [JSON](https://tools.ietf.org/html/rfc8259), which is detailed in [RFC8259].

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

[hyperlink](https://www.w3.org/TR/json-ld-api/)

A hyperlink is underlined and in blue.

[[reference](https://www.w3.org/TR/json-ld-api/)]

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
In the internal representation,
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

In the internal representation a [JSON object](https://tools.ietf.org/html/rfc8259#section-4) is described as a *[map](https://infra.spec.whatwg.org/#ordered-map)* (see [INFRA]),
composed of *[entries](https://infra.spec.whatwg.org/#map-entry)* with key/value pairs.

In the Application Programming Interface (§9),
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
In the internal representation,
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

*[compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri)*

A compact IRI has the form of [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix):*suffix* and is used as a way of expressing an [IRI](https://tools.ietf.org/html/rfc3987#section-2) without needing to define separate [term](https://www.w3.org/TR/json-ld11/#dfn-term) definitions
for each IRI contained within a common vocabulary identified by [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix).

*[context](https://www.w3.org/TR/json-ld11/#dfn-context)*

A set of rules for interpreting a [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) as described in the [The Context](https://www.w3.org/TR/json-ld11/#the-context) section of JSON-LD 1.1,
and normatively specified in the [Context Definitions](https://www.w3.org/TR/json-ld11/#context-definitions) section of JSON-LD 1.1.

*[default language](https://www.w3.org/TR/json-ld11/#dfn-default-language)*

The [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) is the language used when a string does not have a language associated with it directly.
It can be set in the [context](https://www.w3.org/TR/json-ld11/#dfn-context) using the `@language` key
whose value must be a [string](https://infra.spec.whatwg.org/#javascript-string) representing a [BCP47] language code or `null`.
See the [Context Definitions](https://www.w3.org/TR/json-ld11/#context-definitions) section of JSON-LD 1.1 for a normative description.

*[default object](https://www.w3.org/TR/json-ld11/#dfn-default-object)*

A [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object) is a [map](https://infra.spec.whatwg.org/#ordered-map) that has a `@default` key.

*[expanded term definition](https://www.w3.org/TR/json-ld11/#dfn-expanded-term-definition)*

An expanded term definition is a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) where the value is a [map](https://infra.spec.whatwg.org/#ordered-map) containing one or more [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) keys to define the associated [IRI](https://tools.ietf.org/html/rfc3987#section-2),
if this is a reverse property,
the type associated with string values, and a container mapping.
See the [Expanded Term Definition](https://www.w3.org/TR/json-ld11/#expanded-term-definition) section of JSON-LD 1.1 for a normative description.

*[frame](https://www.w3.org/TR/json-ld11-framing/#dfn-frame)*

A [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document),
which describes the form for transforming another [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) using matching and embedding rules.
A frame document allows additional keywords and certain [map entries](https://infra.spec.whatwg.org/#map-entry) to describe the matching and transforming process.

*[graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object)*

A [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object) represents a [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph) as the value of a [map entry](https://infra.spec.whatwg.org/#map-entry) within a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).
When expanded, a graph object must have an `@graph` [entry](https://infra.spec.whatwg.org/#map-entry),
and may also have `@id`, and `@index` [entries](https://infra.spec.whatwg.org/#map-entry).
A *[simple graph object](https://www.w3.org/TR/json-ld11/#dfn-simple-graph-object)* is a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object) which does not have an `@id` [entry](https://infra.spec.whatwg.org/#map-entry).
Note that [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) may have a `@graph` [entry](https://infra.spec.whatwg.org/#map-entry),
but are not considered [graph objects](https://www.w3.org/TR/json-ld11/#dfn-graph-object) if they include any other [entries](https://infra.spec.whatwg.org/#map-entry).
A top-level object consisting of `@graph` is also not a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object).
Note that a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) may also represent a [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph) it it includes other properties.
See the [Graph Objects](https://www.w3.org/TR/json-ld11/#graph-objects) section of JSON-LD 1.1 for a normative description.

*[id map](https://www.w3.org/TR/json-ld11/#dfn-id-map)*

An [id map](https://www.w3.org/TR/json-ld11/#dfn-id-map) is a [map](https://infra.spec.whatwg.org/#ordered-map) value of a [term](https://www.w3.org/TR/json-ld11/#dfn-term) defined with `@container` set to `@id`.
The values of the [id map](https://www.w3.org/TR/json-ld11/#dfn-id-map) must be [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object),
and its keys are interpreted as [IRIs](https://tools.ietf.org/html/rfc3987#section-2) representing
the `@id` of the associated [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).
If a value in the [id map](https://www.w3.org/TR/json-ld11/#dfn-id-map) contains a key expanding to `@id`,
its value must be equivalent to the referencing key in the [id map](https://www.w3.org/TR/json-ld11/#dfn-id-map).
See the [Id Maps](https://www.w3.org/TR/json-ld11/#id-maps) section of JSON-LD 1.1 for a normative description.

*[included block](https://www.w3.org/TR/json-ld11/#dfn-included-block)*

An [included block](https://www.w3.org/TR/json-ld11/#dfn-included-block) is an [entry](https://infra.spec.whatwg.org/#map-entry) in a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) where the key is either `@included` or an alias of `@included` and the value is one or more [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object).
See the [Included Blocks](https://www.w3.org/TR/json-ld11/#included-blocks) section of JSON-LD 1.1 for a normative description.

*[index map](https://www.w3.org/TR/json-ld11/#dfn-index-map)*

An [index map](https://www.w3.org/TR/json-ld11/#dfn-index-map) is a [map](https://infra.spec.whatwg.org/#ordered-map) value of a [term](https://www.w3.org/TR/json-ld11/#dfn-term) defined with `@container` set to `@index`,
whose values must be any of the following types: [string](https://infra.spec.whatwg.org/#javascript-string), [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value), `true`, `false`, [null](https://infra.spec.whatwg.org/#nulls), [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object), [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object), [set object](https://www.w3.org/TR/json-ld11/#dfn-set-object), or
an [array](https://infra.spec.whatwg.org/#list) of zero or more of the above possibilities.
See the [Index Maps](https://www.w3.org/TR/json-ld11/#index-maps) section in JSON-LD 1.1 for a formal description.

*[JSON literal](https://www.w3.org/TR/json-ld11/#dfn-json-literal)*

A [JSON literal](https://www.w3.org/TR/json-ld11/#dfn-json-literal) is a [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) where the associated [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) is `rdf:JSON`.
In the [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) representation, the value of `@type` is `@json`.
JSON literals represent values which are valid JSON [RFC8259].
See the [The `rdf:JSON` Datatype](https://www.w3.org/TR/json-ld11/#the-rdf-json-datatype) section in JSON-LD 1.1 for a normative description.

*[JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document)*

A [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) is a serialization of
an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset).
See the [JSON-LD Grammar](https://www.w3.org/TR/json-ld11/#json-ld-grammar) section in JSON-LD 1.1 for a formal description.

*JSON-LD internal representation*

The JSON-LD internal representation
is the result of transforming a JSON syntactic structure
into the core data structures suitable for direct processing: [arrays](https://infra.spec.whatwg.org/#list), [maps](https://infra.spec.whatwg.org/#ordered-map), [strings](https://infra.spec.whatwg.org/#javascript-string), [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value), [booleans](https://infra.spec.whatwg.org/#boolean), and [null](https://infra.spec.whatwg.org/#nulls).

*JSON-LD Processor*

A JSON-LD Processor is a system which can perform the algorithms defined in JSON-LD 1.1 Processing Algorithms and API.
See the §3 Conformance section in JSON-LD 1.1 API for a formal description.

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

*[language map](https://www.w3.org/TR/json-ld11/#dfn-language-map)*

An [language map](https://www.w3.org/TR/json-ld11/#dfn-language-map) is a [map](https://infra.spec.whatwg.org/#ordered-map) value of a [term](https://www.w3.org/TR/json-ld11/#dfn-term) defined with `@container` set to `@language`,
whose keys must be [strings](https://infra.spec.whatwg.org/#javascript-string) representing [BCP47] language codes
and the values must be any of the following types: [null](https://infra.spec.whatwg.org/#nulls), [string](https://infra.spec.whatwg.org/#javascript-string), or
an [array](https://infra.spec.whatwg.org/#list) of zero or more of the above possibilities.
See the [Language Maps](https://www.w3.org/TR/json-ld11/#language-maps) section of JSON-LD 1.1 for a normative description.

*[list object](https://www.w3.org/TR/json-ld11/#dfn-list-object)*

A [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object) is a [map](https://infra.spec.whatwg.org/#ordered-map) that has a `@list` key.
It may also have an `@index` key, but no other [entries](https://infra.spec.whatwg.org/#map-entry).
See the [Lists and Sets](https://www.w3.org/TR/json-ld11/#lists-and-sets) section of JSON-LD 1.1 for a normative description.

*[local context](https://www.w3.org/TR/json-ld11/#dfn-local-context)*

A [context](https://www.w3.org/TR/json-ld11/#dfn-context) that is specified with a [map](https://infra.spec.whatwg.org/#ordered-map),
specified via the `@context` [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword).

*[node object](https://www.w3.org/TR/json-ld11/#dfn-node-object)*

A [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) represents zero or more [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in the [graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) serialized by the [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document).
A [map](https://infra.spec.whatwg.org/#ordered-map) is a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) if it exists outside of the JSON-LD [context](https://www.w3.org/TR/json-ld11/#dfn-context) and:

- it does not contain the `@value`, `@list`, or `@set` keywords, or
- it is not the top-most [map](https://infra.spec.whatwg.org/#ordered-map) in the JSON-LD document
  consisting of no other [entries](https://infra.spec.whatwg.org/#map-entry) than `@graph` and `@context`.

The [entries](https://infra.spec.whatwg.org/#map-entry) of a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) whose keys are not keywords are also called [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of the [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).
See the [Node Objects](https://www.w3.org/TR/json-ld11/#node-objects) section of JSON-LD 1.1 for a normative description.

*[prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix)*

A [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix) is the first component of a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) which comes from a [term](https://www.w3.org/TR/json-ld11/#dfn-term) that maps to a string that,
when prepended to the suffix of the [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri),
results in an [IRI](https://tools.ietf.org/html/rfc3987#section-2).

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

*[set object](https://www.w3.org/TR/json-ld11/#dfn-set-object)*

A [set object](https://www.w3.org/TR/json-ld11/#dfn-set-object) is a [map](https://infra.spec.whatwg.org/#ordered-map) that has an `@set` [entry](https://infra.spec.whatwg.org/#map-entry).
It may also have an `@index` key, but no other [entries](https://infra.spec.whatwg.org/#map-entry).
See the [Lists and Sets](https://www.w3.org/TR/json-ld11/#lists-and-sets) section of JSON-LD 1.1 for a normative description.

*[term](https://www.w3.org/TR/json-ld11/#dfn-term)*

A [term](https://www.w3.org/TR/json-ld11/#dfn-term) is a short word defined in a [context](https://www.w3.org/TR/json-ld11/#dfn-context) that may be expanded to an [IRI](https://tools.ietf.org/html/rfc3987#section-2).
See the [Terms](https://www.w3.org/TR/json-ld11/#terms) section of JSON-LD 1.1 for a normative description.

*[term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition)*

A term definition is an entry in a [context](https://www.w3.org/TR/json-ld11/#dfn-context),
where the key defines a [term](https://www.w3.org/TR/json-ld11/#dfn-term) which may be used within a [map](https://infra.spec.whatwg.org/#ordered-map) as a key, type, or elsewhere that a string is interpreted as a vocabulary item.
Its value is either a string (*[simple term definition](https://www.w3.org/TR/json-ld11/#dfn-simple-term-definition)*),
expanding to an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
or a map ([expanded term definition](https://www.w3.org/TR/json-ld11/#dfn-expanded-term-definition)).

*[type map](https://www.w3.org/TR/json-ld11/#dfn-type-map)*

A [type map](https://www.w3.org/TR/json-ld11/#dfn-type-map) is a [map](https://infra.spec.whatwg.org/#ordered-map) value of a [term](https://www.w3.org/TR/json-ld11/#dfn-term) defined with `@container` set to `@type`,
whose keys are interpreted as [IRIs](https://tools.ietf.org/html/rfc3987#section-2) representing the `@type` of the associated [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object);
the value must be a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), or [array](https://infra.spec.whatwg.org/#list) of node objects.
If the value contains a [term](https://www.w3.org/TR/json-ld11/#dfn-term) expanding to `@type`,
its values are merged with the map value when expanding.
See the [Type Maps](https://www.w3.org/TR/json-ld11/#type-maps) section of JSON-LD 1.1 for a normative description.

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

*active graph*

The name of the currently active graph that the processor should use when processing.

*active property*

The currently active [property](https://www.w3.org/TR/rdf11-concepts/#dfn-property) or [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) that the processor should use when processing.
The active property is represented in the original lexical form,
which is used for finding coercion mappings in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context).

*add value*

Used as a macro within various algorithms as a way to add a *value* to an [entry](https://infra.spec.whatwg.org/#map-entry) in a [map](https://infra.spec.whatwg.org/#ordered-map) (*object*) using a specified *key*.
The invocation may include an *as array* flag defaulting to `false`.

1. If *as array* is `true` and the value of *key* in *object* does not exist
   or is not an [array](https://infra.spec.whatwg.org/#list), set it to a new [array](https://infra.spec.whatwg.org/#list) containing any original value.
2. If *value* is an [array](https://infra.spec.whatwg.org/#list),
   then for each element *v* in *value*,
   use add value recursively to add *v* to *key* in *entry*.
3. Otherwise:
   1. If *key* is not an entry in *object*,
      add *value* as the value of *key* in *object*.
   2. Otherwise
      1. If the value of the *key* [entry](https://infra.spec.whatwg.org/#map-entry) in *object* is not an [array](https://infra.spec.whatwg.org/#list),
         set it to a new [array](https://infra.spec.whatwg.org/#list) containing the original value.
      2. Append *value* to the value of the *key* [entry](https://infra.spec.whatwg.org/#map-entry) in *object*.

*IRI compacting*

Used as a macro within various algorithms as to reduce the language used to describe
the process of compacting a [string](https://infra.spec.whatwg.org/#javascript-string) *var* representing an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) using an *active context* either specified directly, or coming from the scope of
the algorithm step using this term.
An optional *value* is used, if explicitly provided.
Unless specified, the *vocab* flag defaults to `true`,
and the *reverse* flag defaults to `false`.

1. Return the result of using the IRI Compaction algorithm (§6.2),
   passing *active context*, *var*, *value* (if supplied), *vocab*,
   and *result*.

*IRI expanding*

Used as a macro within various algorithms as to reduce the language used to describe
the process of expanding a [string](https://infra.spec.whatwg.org/#javascript-string) *value* representing an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) using an *active context* either specified directly, or coming from the scope of
the algorithm step using this term.
Optional *defined* and *local context* arguments are used, if explicitly provided.
Unless specified,
the *document relative* flag defaults to `false`,
and the *vocab* flag defaults to `true`.

1. Return the result of using the IRI Expansion algorithm (§5.2),
   passing *active context*, *value*, *local context* (if supplied), *defined* (if supplied), *document relative*,
   and *vocab*.

*JSON-LD input*

The JSON-LD data structure that is provided as input to the algorithm.

#### 1.4.2 Syntax Tokens and Keywords

In addition to the [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) defined in the JSON-LD 1.1 Syntax specification [JSON-LD11],
this specification adds an additional [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) to support [JSON-LD 1.1 Framing](https://www.w3.org/TR/json-ld11-framing/) [JSON-LD11-FRAMING]:

`@preserve`

Used in an expanded document created as the result of the [Framing algorithm](https://www.w3.org/TR/json-ld11-framing/#framing-algorithm) to represent values that might otherwise be removed as part of the §5.1 Expansion Algorithm.

### 1.5 Example Conventions

*This section is non-normative.*

Note that in the examples used in this document, output
is of necessity shown in serialized form as JSON. While the algorithms
describe operations on the JSON-LD internal representation, when
they as displayed as examples, the JSON serialization is used. In particular,
the internal representation use of [maps](https://infra.spec.whatwg.org/#ordered-map) are represented using [JSON objects](https://tools.ietf.org/html/rfc8259#section-4).
> **Example:**
>
> Example 2: Sample JSON-LD document
>
>
>
> ```
> {
>   "@context": {
>     "name": "http://xmlns.com/foaf/0.1/name",
>     "knows": "http://xmlns.com/foaf/0.1/knows"
>   },
>   "@id": "http://me.markus-lanthaler.com/",
>   "name": "Markus Lanthaler",
>   "knows": [
>     {
>       "name": "Dave Longley"
>     }
>   ]
> }
> ```

In the internal representation, the example above would be of a [map](https://infra.spec.whatwg.org/#ordered-map) containing `@context`, `@id`, `name`, and `knows` [entries](https://infra.spec.whatwg.org/#map-entry),
with either [maps](https://infra.spec.whatwg.org/#ordered-map), [strings](https://infra.spec.whatwg.org/#javascript-string), or [arrays](https://infra.spec.whatwg.org/#list) of
maps or strings values. In the JSON serialization, [JSON objects](https://tools.ietf.org/html/rfc8259#section-4) are used
for maps, while arrays and strings are serialized using a
convention common to many programming languages.

## 2. Features

*This section is non-normative.*

The JSON-LD 1.1 Syntax specification [JSON-LD11] defines a syntax to
express Linked Data in JSON. Because there is more than one way to
express Linked Data using this syntax, it is often useful to be able to
transform JSON-LD documents so that they may be more easily consumed by
specific applications.

To allow these algorithms to be adapted for syntaxes
other than JSON, the algorithms operate on the JSON-LD internal representation,
which uses the generic
concepts of [arrays](https://infra.spec.whatwg.org/#list), [maps](https://infra.spec.whatwg.org/#ordered-map), [strings](https://infra.spec.whatwg.org/#javascript-string), [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value), [booleans](https://infra.spec.whatwg.org/#boolean), and [null](https://infra.spec.whatwg.org/#nulls) to describe
the data represented by a JSON document. Algorithms act on this internal representation with API entry points responsible for
transforming between the concrete and internal representations.

JSON-LD uses [contexts](https://www.w3.org/TR/json-ld11/#dfn-context) to allow Linked Data
to be expressed in a way that is specifically tailored to a particular
person or application. By providing a [context](https://www.w3.org/TR/json-ld11/#dfn-context),
JSON data can be expressed in a way that is a natural fit for a particular
person or application whilst also indicating how the data should be
understood at a global scale. In order for people or applications to
share data that was created using a [context](https://www.w3.org/TR/json-ld11/#dfn-context) that is different
from their own, a JSON-LD processor must be able to transform a document
from one [context](https://www.w3.org/TR/json-ld11/#dfn-context) to another. Instead of requiring JSON-LD
processors to write specific code for every imaginable [context](https://www.w3.org/TR/json-ld11/#dfn-context) switching scenario, it is much easier to specify a
single algorithm that can remove any [context](https://www.w3.org/TR/json-ld11/#dfn-context). Similarly,
another algorithm can be specified to subsequently apply any [context](https://www.w3.org/TR/json-ld11/#dfn-context). These two algorithms represent the most basic
transformations of JSON-LD documents. They are referred to as expansion and compaction, respectively.

JSON-LD 1.1 introduces new features that are
compatible with [JSON-LD 1.0](https://www.w3.org/TR/2014/REC-json-ld-20140116/) [JSON-LD10],
but if processed by a JSON-LD 1.0 processor may produce different results.
Processors default to `json-ld-1.1`, unless the `processingMode` API option
is explicitly set to `json-ld-1.0`.
Publishers are encouraged to use the `@version` [map entry](https://infra.spec.whatwg.org/#map-entry) within a [context](https://www.w3.org/TR/json-ld11/#dfn-context) set to `1.1` to ensure that JSON-LD 1.0 processors will not misinterpret JSON-LD 1.1 features.

There are four major types of transformation that are discussed in this
document: expansion, compaction, flattening, and RDF serialization/deserialization.

### 2.1 Expansion

*This section is non-normative.*

The algorithm that removes [context](https://www.w3.org/TR/json-ld11/#dfn-context) is
called *expansion*. Before performing any other
transformations on a JSON-LD document, it is easiest to
remove any [context](https://www.w3.org/TR/json-ld11/#dfn-context) from it and to make data structures
more regular.

To get an idea of how context and data structuring affects the same data,
here is an example of JSON-LD that uses only [terms](https://www.w3.org/TR/json-ld11/#dfn-term) and is fairly compact:
> **Example:**
>
> Example 3: JSON-LD document using only terms
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-expand&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22name%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fname%22%2C%0A%20%20%20%20%22homepage%22%3A%20%7B%0A%20%20%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fhomepage%22%2C%0A%20%20%20%20%20%20%22%40type%22%3A%20%22%40id%22%0A%20%20%20%20%7D%0A%20%20%7D%2C%0A%20%20%22%40id%22%3A%20%22http%3A%2F%2Fme.markus-lanthaler.com%2F%22%2C%0A%20%20%22name%22%3A%20%22Markus%20Lanthaler%22%2C%0A%20%20%22homepage%22%3A%20%22http%3A%2F%2Fwww.markus-lanthaler.com%2F%22%0A%7D)
>
> ```
> {
>   "@context": {
>     "name": "http://xmlns.com/foaf/0.1/name",
>     "homepage": {
>       "@id": "http://xmlns.com/foaf/0.1/homepage",
>       "@type": "@id"
>     }
>   },
>   "@id": "http://me.markus-lanthaler.com/",
>   "name": "Markus Lanthaler",
>   "homepage": "http://www.markus-lanthaler.com/"
> }
> ```
>
> ```
> [{
>   "@id": "http://me.markus-lanthaler.com/",
>   "http://xmlns.com/foaf/0.1/name": [
>     {"@value": "Markus Lanthaler"}
>   ],
>   "http://xmlns.com/foaf/0.1/homepage": [
>     {"@id": "http://www.markus-lanthaler.com/"}
>   ]
> }]
> ```
>
> | Subject                         | Property                           | Value                            |
> | ------------------------------- | ---------------------------------- | -------------------------------- |
> | http://me.markus-lanthaler.com/ | foaf:name                          | Markus Lanthaler                 |
> | http://me.markus-lanthaler.com/ | http://xmlns.com/foaf/0.1/homepage | http://www.markus-lanthaler.com/ |
>
> ```
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
>
> <http://me.markus-lanthaler.com/> foaf:name "Markus Lanthaler";
>   foaf:homepage <http://www.markus-lanthaler.com/> .
> ```

The next input example uses one [IRI](https://tools.ietf.org/html/rfc3987#section-2) to express a [property](https://www.w3.org/TR/rdf11-concepts/#dfn-property) and a [map](https://infra.spec.whatwg.org/#ordered-map) to encapsulate a value, but
leaves the rest of the information untouched.
> **Example:**
>
> Example 4: Sample JSON-LD document using an IRI instead of a term to express a property
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-expand&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22website%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fhomepage%22%0A%20%20%7D%2C%0A%20%20%22%40id%22%3A%20%22http%3A%2F%2Fme.markus-lanthaler.com%2F%22%2C%0A%20%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fname%22%3A%20%22Markus%20Lanthaler%22%2C%0A%20%20%22website%22%3A%20%7B%20%22%40id%22%3A%20%22http%3A%2F%2Fwww.markus-lanthaler.com%2F%22%20%7D%0A%7D)
>
> ```
> {
>   "@context": {
>     "website": "http://xmlns.com/foaf/0.1/homepage"
>   },
>   "@id": "http://me.markus-lanthaler.com/",
>   "http://xmlns.com/foaf/0.1/name": "Markus Lanthaler",
>   "website": { "@id": "http://www.markus-lanthaler.com/" }
> }
> ```
>
> ```
> [{
>   "@id": "http://me.markus-lanthaler.com/",
>   "http://xmlns.com/foaf/0.1/name": [
>     {"@value": "Markus Lanthaler"}
>   ],
>   "http://xmlns.com/foaf/0.1/homepage": [
>     {"@id": "http://www.markus-lanthaler.com/"}
>   ]
> }]
> ```
>
> | Subject                         | Property                           | Value                            |
> | ------------------------------- | ---------------------------------- | -------------------------------- |
> | http://me.markus-lanthaler.com/ | foaf:name                          | Markus Lanthaler                 |
> | http://me.markus-lanthaler.com/ | http://xmlns.com/foaf/0.1/homepage | http://www.markus-lanthaler.com/ |
>
> ```
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
>
> <http://me.markus-lanthaler.com/> foaf:name "Markus Lanthaler";
>   foaf:homepage <http://www.markus-lanthaler.com/> .
> ```

Note that both inputs are valid JSON-LD and both represent the same
information. The difference is in their [context](https://www.w3.org/TR/json-ld11/#dfn-context) information
and in the data structures used. A JSON-LD processor can remove [context](https://www.w3.org/TR/json-ld11/#dfn-context) and ensure that the data is more regular by employing expansion.

Expansion has two important goals: removing any contextual
information from the document, and ensuring all values are represented
in a regular form. These goals are accomplished by expanding all [entry](https://infra.spec.whatwg.org/#map-entry) keys
to [IRIs](https://tools.ietf.org/html/rfc3987#section-2) and by expressing all
values in [arrays](https://infra.spec.whatwg.org/#list) in expanded form. Expanded form is the most verbose
and regular way of expressing of values in JSON-LD; all contextual
information from the document is instead stored locally with each value.
Running the §5.1 Expansion Algorithm (`expand()`)
operation) against the above examples results in the following output:
> **Example:**
>
> Example 5: Expanded JSON-LD document using an IRI
>
>
>
> ```
> [
>   {
>     "@id": "http://me.markus-lanthaler.com/",
>     "http://xmlns.com/foaf/0.1/name": [
>       { "@value": "Markus Lanthaler" }
>     ],
>     "http://xmlns.com/foaf/0.1/homepage": [
>       { "@id": "http://www.markus-lanthaler.com/" }
>     ]
>   }
> ]
> ```

The example above is the JSON-LD serialization of the output of the §5.1 Expansion Algorithm,
where the algorithm's use of [maps](https://infra.spec.whatwg.org/#ordered-map) are replaced with [JSON objects](https://tools.ietf.org/html/rfc8259#section-4).

Note that in the output above all [context](https://www.w3.org/TR/json-ld11/#dfn-context) definitions have
been removed, all [terms](https://www.w3.org/TR/json-ld11/#dfn-term) and [compact IRIs](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) have been expanded to absolute [IRIs](https://tools.ietf.org/html/rfc3987#section-2), and all [JSON-LD values](https://www.w3.org/TR/json-ld11/#dfn-json-ld-value) are expressed in [arrays](https://infra.spec.whatwg.org/#list) in expanded form. While the
output is more verbose and difficult for a human to read, it establishes a
baseline that makes JSON-LD processing easier because of its very regular
structure.

### 2.2 Compaction

*This section is non-normative.*

While expansion removes [context](https://www.w3.org/TR/json-ld11/#dfn-context) from a given
input, *compaction*'s primary function is to
perform the opposite operation: to express a given input according to
a particular [context](https://www.w3.org/TR/json-ld11/#dfn-context). Compaction applies a [context](https://www.w3.org/TR/json-ld11/#dfn-context) that specifically tailors the way information is
expressed for a particular person or application. This simplifies applications
that consume JSON or JSON-LD by expressing the data in application-specific
terms, and it makes the data easier to read by humans.

Compaction uses a developer-supplied [context](https://www.w3.org/TR/json-ld11/#dfn-context) to
shorten [IRIs](https://tools.ietf.org/html/rfc3987#section-2) to [terms](https://www.w3.org/TR/json-ld11/#dfn-term) or [compact IRIs](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) and [JSON-LD values](https://www.w3.org/TR/json-ld11/#dfn-json-ld-value) expressed in expanded form to simple values such as [strings](https://infra.spec.whatwg.org/#javascript-string) or [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value).

For example, assume the following expanded JSON-LD input document:
> **Example:**
>
> Example 6: Expanded sample document
>
>
>
> ```
> [
>   {
>     "@id": "http://me.markus-lanthaler.com/",
>     "http://xmlns.com/foaf/0.1/name": [
>       { "@value": "Markus Lanthaler" }
>     ],
>     "http://xmlns.com/foaf/0.1/homepage": [
>       { "@id": "http://www.markus-lanthaler.com/" }
>     ]
>   }
> ]
> ```

Additionally, assume the following developer-supplied JSON-LD [context](https://www.w3.org/TR/json-ld11/#dfn-context):
> **Example:**
>
> Example 7: JSON-LD context
>
>
>
> ```
> {
>   "@context": {
>     "name": "http://xmlns.com/foaf/0.1/name",
>     "homepage": {
>       "@id": "http://xmlns.com/foaf/0.1/homepage",
>       "@type": "@id"
>     }
>   }
> }
> ```

Running the §6.1 Compaction Algorithm (`compact()`)
operation) given the context supplied above against the JSON-LD input
document provided above would result in the following output:
> **Example:**
>
> Example 8: Compacted sample document
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-compacted&json-ld=%5B%0A%20%20%7B%0A%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fme.markus-lanthaler.com%2F%22%2C%0A%20%20%20%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fname%22%3A%20%5B%0A%20%20%20%20%20%20%7B%20%22%40value%22%3A%20%22Markus%20Lanthaler%22%20%7D%0A%20%20%20%20%5D%2C%0A%20%20%20%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fhomepage%22%3A%20%5B%0A%20%20%20%20%20%20%7B%20%22%40id%22%3A%20%22http%3A%2F%2Fwww.markus-lanthaler.com%2F%22%20%7D%0A%20%20%20%20%5D%0A%20%20%7D%0A%5D&context=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22name%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fname%22%2C%0A%20%20%20%20%22homepage%22%3A%20%7B%0A%20%20%20%20%20%20%22%40id%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fhomepage%22%2C%0A%20%20%20%20%20%20%22%40type%22%3A%20%22%40id%22%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
>
> ```
> {
>   "@context": {
>     "name": "http://xmlns.com/foaf/0.1/name",
>     "homepage": {
>       "@id": "http://xmlns.com/foaf/0.1/homepage",
>       "@type": "@id"
>     }
>   },
>   "@id": "http://me.markus-lanthaler.com/",
>   "name": "Markus Lanthaler",
>   "homepage": "http://www.markus-lanthaler.com/"
> }
> ```

The example above is the JSON-LD serialization of the output of the §6.1 Compaction Algorithm,
where the algorithm's use of [maps](https://infra.spec.whatwg.org/#ordered-map) are replaced with [JSON objects](https://tools.ietf.org/html/rfc8259#section-4).

Note that all [IRIs](https://tools.ietf.org/html/rfc3987#section-2) have been compacted to [terms](https://www.w3.org/TR/json-ld11/#dfn-term) as specified in the [context](https://www.w3.org/TR/json-ld11/#dfn-context),
which has been injected into the output. While compacted output is
useful to humans, it is also used to generate structures that are easy to
program against. Compaction enables developers to map any expanded document
into an application-specific compacted document. While the context provided
above mapped `http://xmlns.com/foaf/0.1/name` to `name`, it
could also have been mapped to any other term provided by the developer.

### 2.3 Flattening

*This section is non-normative.*

While expansion ensures that a document is in a uniform structure, *flattening* goes a step further to ensure that the shape of the data
is deterministic. In expanded documents, the [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of a single [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) may be spread across a number of different [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object). By flattening a
document, all [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) are collected in a single [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) and all [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) are labeled with a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier). This may drastically
simplify the code required to process JSON-LD data in certain applications.

For example, assume the following JSON-LD input document:
> **Example:**
>
> Example 9: JSON-LD document in compact form
>
>
>
> ```
> {
>   "@context": {
>     "name": "http://xmlns.com/foaf/0.1/name",
>     "knows": "http://xmlns.com/foaf/0.1/knows"
>   },
>   "@id": "http://me.markus-lanthaler.com/",
>   "name": "Markus Lanthaler",
>   "knows": [
>     {"name": "Dave Longley"}
>   ]
> }
> ```

Running the §7.1 Flattening Algorithm (`flatten()`)
operation) with a context set to [null](https://infra.spec.whatwg.org/#nulls) to prevent compaction
returns the following document:
> **Example:**
>
> Example 10: Flattened sample document
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-flattened&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22name%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fname%22%2C%0A%20%20%20%20%22knows%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fknows%22%0A%20%20%7D%2C%0A%20%20%22%40id%22%3A%20%22http%3A%2F%2Fme.markus-lanthaler.com%2F%22%2C%0A%20%20%22name%22%3A%20%22Markus%20Lanthaler%22%2C%0A%20%20%22knows%22%3A%20%5B%0A%20%20%20%20%7B%22name%22%3A%20%22Dave%20Longley%22%7D%0A%20%20%5D%0A%7D&context=%7B%7D)
>
> ```
> [{
>   "@id": "http://me.markus-lanthaler.com/",
>   "http://xmlns.com/foaf/0.1/name": [
>     { "@value": "Markus Lanthaler" }
>   ],
>   "http://xmlns.com/foaf/0.1/knows": [
>     { "@id": "_:b0" }
>   ]
> }, {
>   "@id": "_:b0",
>   "http://xmlns.com/foaf/0.1/name": [
>     { "@value": "Dave Longley" }
>   ]
> }]
> ```

The example above is the JSON-LD serialization of the output of the §7.1 Flattening Algorithm,
where the algorithm's use of [maps](https://infra.spec.whatwg.org/#ordered-map) are replaced with [JSON objects](https://tools.ietf.org/html/rfc8259#section-4).

Note how in the output above all [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) are collected in a
single [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) and how the [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) representing
"Dave Longley" has been assigned the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) `_:b0`.

To make it easier for humans to read or for certain applications to
process it, a flattened document can be compacted by passing a [context](https://www.w3.org/TR/json-ld11/#dfn-context). Using
the same context as the input document, the flattened and compacted document
looks as follows:
> **Example:**
>
> Example 11: Flattened and compacted sample document
>
> [Open in playground](https://json-ld.org/playground/#startTab=tab-flattened&json-ld=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22name%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fname%22%2C%0A%20%20%20%20%22knows%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fknows%22%0A%20%20%7D%2C%0A%20%20%22%40id%22%3A%20%22http%3A%2F%2Fme.markus-lanthaler.com%2F%22%2C%0A%20%20%22name%22%3A%20%22Markus%20Lanthaler%22%2C%0A%20%20%22knows%22%3A%20%5B%0A%20%20%20%20%7B%22name%22%3A%20%22Dave%20Longley%22%7D%0A%20%20%5D%0A%7D&context=%7B%0A%20%20%22%40context%22%3A%20%7B%0A%20%20%20%20%22name%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fname%22%2C%0A%20%20%20%20%22knows%22%3A%20%22http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Fknows%22%0A%20%20%7D%2C%0A%20%20%22%40id%22%3A%20%22http%3A%2F%2Fme.markus-lanthaler.com%2F%22%2C%0A%20%20%22name%22%3A%20%22Markus%20Lanthaler%22%2C%0A%20%20%22knows%22%3A%20%5B%0A%20%20%20%20%7B%22name%22%3A%20%22Dave%20Longley%22%7D%0A%20%20%5D%0A%7D)
>
> ```
> {
>   "@context": {
>     "name": "http://xmlns.com/foaf/0.1/name",
>     "knows": "http://xmlns.com/foaf/0.1/knows"
>   },
>   "@graph": [{
>     "@id": "http://me.markus-lanthaler.com/",
>     "name": "Markus Lanthaler",
>     "knows": { "@id": "_:b0" }
>   }, {
>     "@id": "_:b0",
>     "name": "Dave Longley"
>   }]
> }
> ```

Please note that the result of flattening and compacting a document
is always a [map](https://infra.spec.whatwg.org/#ordered-map), (represented as a [JSON object](https://tools.ietf.org/html/rfc8259#section-4) when serialized),
which contains an `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) that represents the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph).

### 2.4 RDF Serialization/Deserialization

*This section is non-normative.*

JSON-LD can be used to serialize RDF data as described in
[RDF11-CONCEPTS]. This ensures that data can be round-tripped to and from
any RDF syntax without any loss in fidelity.

For example, assume the following RDF input serialized in Turtle [TURTLE]:
> **Example:**
>
> Example 12: Sample Turtle document
>
>
>
> ```
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
>
> <http://me.markus-lanthaler.com/>
>   foaf:name "Markus Lanthaler" ;
>   foaf:homepage <http://www.markus-lanthaler.com/> .
> ```

Using the §8.4 Serialize RDF as JSON-LD Algorithm a developer could transform this document into expanded JSON-LD:
> **Example:**
>
> Example 13: Sample Turtle document converted to JSON-LD
>
>
>
> ```
> [
>   {
>     "@id": "http://me.markus-lanthaler.com/",
>     "http://xmlns.com/foaf/0.1/name": [
>       { "@value": "Markus Lanthaler" }
>     ],
>     "http://xmlns.com/foaf/0.1/homepage": [
>       { "@id": "http://www.markus-lanthaler.com/" }
>     ]
>   }
> ]
> ```

The example above is the JSON-LD serialization of the output of the §8.4 Serialize RDF as JSON-LD Algorithm,
where the algorithm's use of [maps](https://infra.spec.whatwg.org/#ordered-map) are replaced with [JSON objects](https://tools.ietf.org/html/rfc8259#section-4).

Note that the output above could easily be compacted using the technique outlined
in the previous section. It is also possible to deserialize the JSON-LD document back
to RDF using the §8.1 Deserialize JSON-LD to RDF Algorithm.

## 3. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, and *SHOULD* in this document
are to be interpreted as described in [BCP 14](https://tools.ietf.org/html/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all capitals, as shown here.

There are two classes of products that can claim conformance to this
specification: JSON-LD Processors,
and RDF Serializers/Deserializers.

A conforming JSON-LD Processor is a system which can perform the Expansion (§5.1), Compaction (§6.1),
and Flattening (§7.1) operations in a manner consistent with
the algorithms defined in this specification.

JSON-LD Processors *MUST NOT* attempt to correct malformed [IRIs](https://tools.ietf.org/html/rfc3987#section-2) or [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag);
however, they *SHOULD* issue validation warnings.
IRIs are not modified other than conversion between [relative](https://tools.ietf.org/html/rfc3987#section-6.5) and absolute [IRIs](https://tools.ietf.org/html/rfc3987#section-2).

A conforming *RDF Serializer/Deserializer* is a system that can deserialize JSON-LD to RDF (§8.1) and serialize RDF as JSON-LD (§8.4) as
defined in this specification.

Unless specified using `processingMode` API option,
the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is set using the `@version` [entry](https://infra.spec.whatwg.org/#map-entry) in a local [context](https://www.w3.org/TR/json-ld11/#dfn-context) and
affects the behavior of algorithms including expansion and compaction.
Once set, it is an error to attempt to change to a different processing mode,
and processors *MUST* generate,
a `processing mode conflict` error and abort further processing.

The algorithms in this specification are generally written with more concern for clarity
than efficiency. Thus, JSON-LD Processors may
implement the algorithms given in this specification in any way desired,
so long as the end result is indistinguishable from the result that would
be obtained by the specification's algorithms.

In algorithm steps that describe operations on [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword), those steps
also apply to keyword aliases.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Implementers can partially check their level of conformance to
> this specification by successfully passing the test cases of the [JSON-LD test suite](https://w3c.github.io/json-ld-api/tests/).
> Note, however, that passing all the tests in the test
> suite does not imply complete conformance to this specification. It only implies
> that the implementation conforms to aspects tested by the test suite.

This specification makes use of the following namespace prefixes:

| Prefix | IRI                                         |
| ------ | ------------------------------------------- |
| rdf    | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| xsd    | http://www.w3.org/2001/XMLSchema#           |

## 4. Context Processing Algorithms

The following sections describe algorithms for processing a JSON-LD context.

### 4.1 Context Processing Algorithm

When processing a JSON-LD data structure, each processing rule is applied
using information provided by the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context). This
section describes how to produce an [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context).

The [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) consists of:

- the active [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition) which specify how
  keys and values have to be interpreted ([array](https://infra.spec.whatwg.org/#list) of [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition)),
- the current *base IRI* ([IRI](https://tools.ietf.org/html/rfc3987#section-2)),
- the *original base URL* ([IRI](https://tools.ietf.org/html/rfc3987#section-2)),
- an *inverse context* (inverse context),
- an optional [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping) ([IRI](https://tools.ietf.org/html/rfc3987#section-2)),
- an optional [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) ([string](https://infra.spec.whatwg.org/#javascript-string)),
- an optional [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) (`"ltr"` or `"rtl"`),
- and an optional *previous context* ([context](https://www.w3.org/TR/json-ld11/#dfn-context)),
  used when a non-propagated [context](https://www.w3.org/TR/json-ld11/#dfn-context) is defined.

Each [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) consists of:

- an *IRI mapping* ([IRI](https://tools.ietf.org/html/rfc3987#section-2)),
- a *prefix flag* ([boolean](https://infra.spec.whatwg.org/#boolean)),
- a *protected* flag ([boolean](https://infra.spec.whatwg.org/#boolean)),
- a *reverse property* flag ([boolean](https://infra.spec.whatwg.org/#boolean)),
- an optional *base URL* ([IRI](https://tools.ietf.org/html/rfc3987#section-2)),
- an optional [context](https://www.w3.org/TR/json-ld11/#dfn-context) ([context](https://www.w3.org/TR/json-ld11/#dfn-context)),
- an optional *container mapping* ([array](https://infra.spec.whatwg.org/#list) of [strings](https://infra.spec.whatwg.org/#javascript-string)),
- an optional *direction mapping* (`"ltr"` or `"rtl"`),
- an optional *index mapping* ([string](https://infra.spec.whatwg.org/#javascript-string)),
- an optional *language mapping* ([string](https://infra.spec.whatwg.org/#javascript-string)),
- an optional *nest value* ([string](https://infra.spec.whatwg.org/#javascript-string)),
- and an optional *type mapping* ([IRI](https://tools.ietf.org/html/rfc3987#section-2)).

A [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) can not only be used to map a [term](https://www.w3.org/TR/json-ld11/#dfn-term) to an IRI, but also to map a [term](https://www.w3.org/TR/json-ld11/#dfn-term) to a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword),
in which case it is referred to as a *keyword alias*.

When processing, *active context* is initialized with a `null` inverse context, without any [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition), [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping), [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction), or [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language).
If a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) is encountered during processing, a new *active context* is created by cloning the existing *active context*. Then the information from the [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) is merged into the new *active context*.
Given that [local contexts](https://www.w3.org/TR/json-ld11/#dfn-local-context) may contain
references to remote contexts, this includes their retrieval.

#### 4.1.1 Overview

*This section is non-normative.*

First we prepare a new [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) *result* by cloning
the current [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context). Then we normalize the form of the original [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) to an [array](https://infra.spec.whatwg.org/#list). [Local contexts](https://www.w3.org/TR/json-ld11/#dfn-local-context) may be in the form of a [map](https://infra.spec.whatwg.org/#ordered-map), a [string](https://infra.spec.whatwg.org/#javascript-string), or an [array](https://infra.spec.whatwg.org/#list) containing
a combination of the two. Finally we process each [context](https://www.w3.org/TR/json-ld11/#dfn-context) contained
in the [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) [array](https://infra.spec.whatwg.org/#list) as follows.

If [context](https://www.w3.org/TR/json-ld11/#dfn-context) is a [string](https://infra.spec.whatwg.org/#javascript-string), it represents a reference to
a remote context. We dereference the remote context and replace [context](https://www.w3.org/TR/json-ld11/#dfn-context) with the value of the `@context` [entry](https://infra.spec.whatwg.org/#map-entry) of the top-level object in the
retrieved JSON-LD document.
If there's no such [entry](https://infra.spec.whatwg.org/#map-entry), an `invalid remote context` has been detected. Otherwise, we process [context](https://www.w3.org/TR/json-ld11/#dfn-context) by recursively using
this algorithm ensuring that there is no cyclical reference.

If [context](https://www.w3.org/TR/json-ld11/#dfn-context) is a [map](https://infra.spec.whatwg.org/#ordered-map),
it is a [context definition](https://www.w3.org/TR/json-ld11/#dfn-context-definition).
We first update
the base IRI, the [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction),
the [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language), context propagation, the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode),
and the [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping) by processing six specific keywords: `@base`, `@direction`, `@language`, `@propagate`, `@version`,
and `@vocab`.
These are handled before any other [entries](https://infra.spec.whatwg.org/#map-entry) in the [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) because
they affect how the other [entries](https://infra.spec.whatwg.org/#map-entry) are processed. If [context](https://www.w3.org/TR/json-ld11/#dfn-context) contains `@import`, it is retrieved and is reverse-merged
into the containing context, allowing JSON-LD 1.0 contexts to be upgraded to JSON-LD 1.1. Please note that `@base` is ignored when processing remote contexts.

If [context](https://www.w3.org/TR/json-ld11/#dfn-context) is not to be propagated,
a reference to the previous context is retained so that
it may be rolled back when a new [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) is entered.
By default, all contexts are propagated, other than [type-scoped contexts](https://www.w3.org/TR/json-ld11/#dfn-type-scoped-context).

When an [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) is initialized, the value
of the original base URL is initialized from the original `documentUrl` of the document containing the initial [context](https://www.w3.org/TR/json-ld11/#dfn-context), if available,
otherwise from the `base` API option.
This is necessary when resetting the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) by setting it to `null` to retain the original default base IRI.

When initialized, or when any entry of
an [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) is changed,
or any associated [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) is added, changed, or removed,
the inverse context field
in [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) is set to `null`.

Then, for every other [entry](https://infra.spec.whatwg.org/#map-entry) in [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context), we update
the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in *result*. Since [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) may themselves contain [terms](https://www.w3.org/TR/json-ld11/#dfn-term) or [compact IRIs](https://www.w3.org/TR/json-ld11/#dfn-compact-iri), we may need to recurse.
When doing so, we must ensure that there is no cyclical dependency,
which is an error. After we have processed any [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) dependencies,
we update the current [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition),
which may be a keyword alias.

Finally, we return *result* as the new [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context).

#### 4.1.2 Algorithm

This algorithm specifies how a new [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) is updated
with a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context). The algorithm takes three required and four optional input variables.
The required inputs are
an *active context*,
a *local context*, and a *base URL* used when resolving relative context URLs.
The optional inputs are
an [array](https://infra.spec.whatwg.org/#list) *remote contexts*,
defaulting to a new empty [array](https://infra.spec.whatwg.org/#list), which is used to detect cyclical context inclusions, *override protected*, defaulting to `false`,
which is used to allow changes to protected terms, *propagate*, defaulting to `true` to mark [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition) associated with non-propagated [contexts](https://www.w3.org/TR/json-ld11/#dfn-context),
and *validate scoped context* defaulting to `true`,
which is used to limit recursion when validating possibly recursive [scoped contexts](https://www.w3.org/TR/json-ld11/#dfn-scoped-context)..

1. Initialize *result* to the result of cloning *active context*, with inverse context set to `null`..

2. If *local context* is an object containing the member `@propagate`,
   its value *MUST* be [boolean](https://infra.spec.whatwg.org/#boolean) `true` or `false`,
   set *propagate* to that value.
   > **Note:**
   >
   > > **Note:**
   > >
   > > Note
   >
   > Error handling is performed in step 5.11.

3. If *propagate* is `false`, and *result* does not have a previous context, set previous context in *result* to *active context*.

4. If *local context* is not an [array](https://infra.spec.whatwg.org/#list),
   set *local context* to an [array](https://infra.spec.whatwg.org/#list) containing only *local context*.

5. For each item *context* in *local context*:

   1. If *context* is `null`:

      1. If *override protected* is `false` and *active context* contains any protected [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition),
         an `invalid context nullification` has been detected and processing is aborted.
      2. Initialize *result* as a
         newly-initialized [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context), setting both base IRI and original base URL to the value of original base URL in *active context*,
         and, if *propagate* is `false`, previous context in *result* to the previous value of *result*.
      3. Continue with the next *context*.

   2. If *context* is a [string](https://infra.spec.whatwg.org/#javascript-string),

      1. Initialize *context* to the result of resolving *context* against *base URL*. If *base URL* is not a valid [IRI](https://tools.ietf.org/html/rfc3987#section-2),
         then *context* *MUST* be a valid [IRI](https://tools.ietf.org/html/rfc3987#section-2), otherwise
         a `loading document failed` error
         has been detected and processing is aborted.
         > **Note:**
         >
         > > **Note:**
         > >
         > > Note
         >
         > *base URL* is often not the same as `base` or the base IRI of the *active context*.

      2. If *validate scoped context* is `false`,
         and *remote contexts* already includes *context* do not process *context* further and continue to any next *context* in *local context*.

      3. If the number of entries in the *remote contexts* array
         exceeds a processor defined limit, a `context overflow` error has been detected and processing is aborted;
         otherwise, add *context* to *remote contexts*.

      4. If *context* was previously dereferenced,
         then the processor *MUST NOT* do a further dereference, and [context](https://www.w3.org/TR/json-ld11/#dfn-context) is set to the
         previously established internal representation:
         set *context document* to the previously dereferenced document,
         and set *loaded context* to the value of the `@context` [entry](https://infra.spec.whatwg.org/#map-entry) from the document in *context document*.
         > **Note:**
         >
         > > **Note:**
         > >
         > > Note
         >
         > Only the `@context` [entry](https://infra.spec.whatwg.org/#map-entry) need be retained.

      5. Otherwise, set *context document* to the `RemoteDocument` obtained
         by dereferencing *context* using
         the `LoadDocumentCallback`, passing *context* for url,
         and `http://www.w3.org/ns/json-ld#context` for `profile` and for `requestProfile`.

         1. If *context* cannot be dereferenced, or the `document` from *context document* cannot be transformed into the internal representation ,
            a `loading remote context failed` error has been detected and processing is aborted.
         2. If the `document` has no
            top-level [map](https://infra.spec.whatwg.org/#ordered-map) with an `@context` [entry](https://infra.spec.whatwg.org/#map-entry), an `invalid remote context` has been detected and processing is aborted.
         3. Set *loaded context* to the value of that [entry](https://infra.spec.whatwg.org/#map-entry).

      6. Set *result* to the result of recursively calling this algorithm,
         passing *result* for *active context*, *loaded context* for *local context*, the `documentUrl` of *context document* for *base URL*, a copy of *remote contexts*, and *validate scoped context*.
         > **Note:**
         >
         > > **Note:**
         > >
         > > Note
         >
         > If *context* was previously dereferenced, processors *MUST* make provisions for retaining the *base URL* of that [context](https://www.w3.org/TR/json-ld11/#dfn-context) for this step to enable the resolution of any
         > relative context URLs that may be encountered during processing.

      7. Continue with the next *context*.

   3. If *context* is not a [map](https://infra.spec.whatwg.org/#ordered-map), an `invalid local context` error has been detected and processing is aborted.

   4. Otherwise, *context* is a [context definition](https://www.w3.org/TR/json-ld11/#dfn-context-definition).

   5. If *context* has an `@version` [entry](https://infra.spec.whatwg.org/#map-entry):

      1. If the associated value is not `1.1`,
         an `invalid @version value` has been detected, and processing is aborted.
         > **Note:**
         >
         > > **Note:**
         > >
         > > Note
         >
         > The use of `1.1` for the value of `@version` is intended to
         > cause a JSON-LD 1.0 processor to stop processing.
         > Although it is clearly meant to be related to JSON-LD 1.1, it does not
         > otherwise adhere to the requirements for [Semantic Versioning](https://semver.org/).
         > Implementations may require [special consideration](https://en.wikipedia.org/wiki/Floating-point_arithmetic#Minimizing_the_effect_of_accuracy_problems) when comparing the values of [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) with a non-zero fractional part.

      2. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is set to `json-ld-1.0`,
         a `processing mode conflict` error has been detected and processing is aborted.

   6. If *context* has an `@import` [entry](https://infra.spec.whatwg.org/#map-entry):

      1. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`,
         an `invalid context entry` error has been detected and processing is aborted.
      2. Otherwise, if the value of `@import` is not a [string](https://infra.spec.whatwg.org/#javascript-string),
         an `invalid @import value` error has been detected and processing is aborted.
      3. Initialize *import* to the result of resolving the value of `@import` against *base URL*.
      4. Dereference *import* using
         the `LoadDocumentCallback`, passing *import* for url,
         and `http://www.w3.org/ns/json-ld#context` for `profile` and for `requestProfile`.
      5. If *import* cannot be dereferenced, or cannot be transformed into the internal representation,
         a `loading remote context failed` error has been detected and processing is aborted.
      6. If the dereferenced document has no
         top-level [map](https://infra.spec.whatwg.org/#ordered-map) with an `@context` [entry](https://infra.spec.whatwg.org/#map-entry),
         or if the value of `@context` is not a [context definition](https://www.w3.org/TR/json-ld11/#dfn-context-definition) (i.e., it is not an [map](https://infra.spec.whatwg.org/#ordered-map)),
         an `invalid remote context` has been detected and processing is aborted; otherwise,
         set *import context* to the value of that [entry](https://infra.spec.whatwg.org/#map-entry).
      7. If *import context* has a `@import` [entry](https://infra.spec.whatwg.org/#map-entry),
         an `invalid context entry` error has been detected and processing is aborted.
      8. Set *context* to the result of merging *context* into *import context*, replacing common entries
         with those from *context*.

   7. If *context* has an `@base` [entry](https://infra.spec.whatwg.org/#map-entry) and *remote contexts* is empty, i.e., the currently
      being processed context is not a remote context:

      1. Initialize *value* to the value associated with the `@base` [entry](https://infra.spec.whatwg.org/#map-entry).
      2. If *value* is `null`, remove the base IRI of *result*.
      3. Otherwise, if *value* is an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
         the base IRI of *result* is set to *value*.
      4. Otherwise, if *value* is a [relative IRI reference](https://tools.ietf.org/html/rfc3987#section-6.5) and
         the base IRI of *result* is not `null`,
         set the base IRI of *result* to the result of
         resolving *value* against the current base IRI of *result*.
      5. Otherwise, an `invalid base IRI` error has been detected and processing is aborted.

   8. If *context* has an `@vocab` [entry](https://infra.spec.whatwg.org/#map-entry):

      1. Initialize *value* to the value associated with the `@vocab` [entry](https://infra.spec.whatwg.org/#map-entry).
      2. If *value* is [null](https://infra.spec.whatwg.org/#nulls), remove
         any [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping) from *result*.
      3. Otherwise, if *value* is
         an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), the [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping) of *result* is set to the result of IRI expanding *value* using `true` for *document relative* .
         If it is not an [IRI](https://tools.ietf.org/html/rfc3987#section-2), or a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), an `invalid vocab mapping` error has been detected and processing is aborted.
         > **Note:**
         >
         > > **Note:**
         > >
         > > Note
         >
         > The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to value for `@vocab` is obsolete,
         > and may be removed in a future version of JSON-LD.

   9. If *context* has an `@language` [entry](https://infra.spec.whatwg.org/#map-entry):

      1. Initialize *value* to the value associated with the `@language` [entry](https://infra.spec.whatwg.org/#map-entry).
      2. If *value* is `null`, remove
         any [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) from *result*.
      3. Otherwise, if *value* is a [string](https://infra.spec.whatwg.org/#javascript-string), the [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) of *result* is set to *value*.
         If it is not a [string](https://infra.spec.whatwg.org/#javascript-string), an `invalid default language` error has been detected and processing is aborted. If *value* is not well-formed according to [section 2.2.9](https://tools.ietf.org/html/bcp47#section-2.2.9) of [BCP47],
         processors *SHOULD* issue a warning.
         > **Note:**
         >
         > > **Note:**
         > >
         > > Note
         >
         > Processors *MAY* normalize [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) to lower case.

   10. If *context* has an `@direction` [entry](https://infra.spec.whatwg.org/#map-entry):

       1. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`,
          an `invalid context entry` error has been detected and processing is aborted.
       2. Initialize *value* to the value associated with the `@direction` [entry](https://infra.spec.whatwg.org/#map-entry).
       3. If *value* is `null`, remove
          any [base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) from *result*.
       4. Otherwise, if *value* is a [string](https://infra.spec.whatwg.org/#javascript-string), the [base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) of *result* is set to *value*. If it is not `null`, `"ltr"`, or `"rtl"`, an `invalid base direction` error has been detected and processing is aborted.

   11. If *context* has an `@propagate` [entry](https://infra.spec.whatwg.org/#map-entry):

       1. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`,
          an `invalid context entry` error has been detected and processing is aborted.
       2. Otherwise, if the value of `@propagate` is not [boolean](https://infra.spec.whatwg.org/#boolean) `true` or `false`,
          an `invalid @propagate value` error has been detected and processing is aborted.
          > **Note:**
          >
          > > **Note:**
          > >
          > > Note
          >
          > The previous context is actually set earlier in this algorithm;
          > the previous two steps exist for error checking only.

   12. Create a [map](https://infra.spec.whatwg.org/#ordered-map) *defined* to keep
       track of whether or not a [term](https://www.w3.org/TR/json-ld11/#dfn-term) has already been defined
       or is currently being defined during recursion.

   13. For each *key*-*value* pair in *context* where *key* is not `@base`, `@direction`, `@import`, `@language`, `@propagate`, `@protected`, `@version`, or `@vocab`,
       invoke the Create Term Definition algorithm (§4.2),
       passing *result* for *active context*, *context* for *local context*, *key*, *defined*, *base URL*,
       the value of the `@protected` entry from *context*, if any, for *protected*, *override protected*,
       and a copy of *remote contexts*.

6. Return *result*.

### 4.2 Create Term Definition

This algorithm is called from the §4.1 Context Processing Algorithm to create a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) for a [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed in a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context).

#### 4.2.1 Overview

*This section is non-normative.*

[Term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition) are created by
parsing the information in the given [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) for the
given [term](https://www.w3.org/TR/json-ld11/#dfn-term). If the given [term](https://www.w3.org/TR/json-ld11/#dfn-term) is a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri), it may omit an IRI mapping by
depending on its [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix) having its own [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition). If the [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix) is
an [entry](https://infra.spec.whatwg.org/#map-entry) in the [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context), then its [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) must first be created, through recursion, before continuing. Because a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) can depend on other [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition), a mechanism must
be used to detect cyclical dependencies. The solution employed here
uses a map, *defined*, that keeps track of whether or not a [term](https://www.w3.org/TR/json-ld11/#dfn-term) has been defined or is currently in the process of
being defined. This map is checked before any recursion is attempted.

After all dependencies for a [term](https://www.w3.org/TR/json-ld11/#dfn-term) have been defined, the rest of
the information in the [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) for the given [term](https://www.w3.org/TR/json-ld11/#dfn-term) is taken into account, creating the appropriate IRI mapping, container mapping, and type mapping, language mapping, or direction mapping for the [term](https://www.w3.org/TR/json-ld11/#dfn-term).

#### 4.2.2 Algorithm

The algorithm has four required and five optional inputs.
The required inputs are
an *active context*,
a *local context*,
a *term*,
and a map *defined*. The optional inputs are *base URL* defaulting to `null`, *protected* which defaults to `false`,
and *override protected*, defaulting to `false`,
which is used to allow changes to protected terms,
an [array](https://infra.spec.whatwg.org/#list) *remote contexts*,
defaulting to a new empty [array](https://infra.spec.whatwg.org/#list), which is used to detect cyclical context inclusions,
and *validate scoped context* defaulting to `true`,
which is used to limit recursion when validating possibly recursive [scoped contexts](https://www.w3.org/TR/json-ld11/#dfn-scoped-context)..

1. If *defined* contains the [entry](https://infra.spec.whatwg.org/#map-entry) *term* and the associated
   value is `true` (indicating that the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) has already been created), return. Otherwise,
   if the value is `false`, a `cyclic IRI mapping` error has been detected and processing is aborted.

2. If *term* is the empty string (`""`),
   an `invalid term definition` error has been detected and processing is aborted.
   Otherwise, set the value associated with *defined*'s *term* [entry](https://infra.spec.whatwg.org/#map-entry) to `false`. This indicates that the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) is now being created but is not yet complete.

3. Initialize *value* to a copy of the value associated with the [entry](https://infra.spec.whatwg.org/#map-entry) *term* in *local context*.

4. If *term* is `@type`,
   and [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`,
   a `keyword redefinition` error has
   been detected and processing is aborted.
   At this point, *value* *MUST* be a [map](https://infra.spec.whatwg.org/#ordered-map) with only either or both of the following [entries](https://infra.spec.whatwg.org/#map-entry):

   - An entry for `@container` with value `@set`.
   - An entry for `@protected`.

   Any other value means that a `keyword redefinition` error has
   been detected and processing is aborted.

5. Otherwise, since [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) cannot be overridden, *term* *MUST NOT* be a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) and a `keyword redefinition` error has been detected and processing is aborted.
   If *term* has the form of a keyword
   (i.e., it matches the ABNF rule `"@"1*ALPHA` from [RFC5234]),
   return; processors *SHOULD* generate a warning.

6. Initialize *previous definition* to any existing [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *term* in *active context*,
   removing that [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) from *active context*.

7. If *value* is `null`,
   convert it to a [map](https://infra.spec.whatwg.org/#ordered-map) consisting of a single [entry](https://infra.spec.whatwg.org/#map-entry) whose
   key is `@id` and whose value is `null`.

8. Otherwise, if *value* is a [string](https://infra.spec.whatwg.org/#javascript-string), convert it
   to a [map](https://infra.spec.whatwg.org/#ordered-map) consisting of a single [entry](https://infra.spec.whatwg.org/#map-entry) whose
   key is `@id` and whose value is *value*. Set *simple term* to `true`.

9. Otherwise, *value* *MUST* be a [map](https://infra.spec.whatwg.org/#ordered-map), if not, an `invalid term definition` error has been detected and processing is aborted. Set *simple term* to `false`.

10. Create a new [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition), *definition*, initializing prefix flag to `false`, protected to *protected*,
    and reverse property to `false`.

11. If *value* has an `@protected` entry,
    set the protected flag in *definition* to the value of this entry.
    If the value of `@protected` is not a [boolean](https://infra.spec.whatwg.org/#boolean),
    an `invalid @protected value` error has been detected and processing is aborted.
    If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`,
    an `invalid term definition` has been detected and processing is aborted.

12. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@type`:

    1. Initialize *type* to the value associated with the `@type` [entry](https://infra.spec.whatwg.org/#map-entry), which *MUST* be a [string](https://infra.spec.whatwg.org/#javascript-string). Otherwise, an `invalid type mapping` error has been detected and processing is aborted.
    2. Set *type* to the result of IRI expanding *type*,
       using *local context*, and *defined*.
    3. If the expanded *type* is `@json` or `@none`, and [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`,
       an `invalid type mapping` error has been detected and processing is aborted.
    4. Otherwise, if the expanded *type* is
       neither `@id`, nor `@json`,
       nor `@none`,
       nor `@vocab`,
       nor an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
       an `invalid type mapping` error has been detected and processing is aborted.
    5. Set the type mapping for *definition* to *type*.

13. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@reverse`:

    1. If *value* contains `@id` or `@nest`, [entries](https://infra.spec.whatwg.org/#map-entry), an `invalid reverse property` error has been detected and processing is aborted.
    2. If the value associated with the `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry) is not a [string](https://infra.spec.whatwg.org/#javascript-string), an `invalid IRI mapping` error has been detected and processing is aborted.
    3. If the value associated with the `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry) is a string
       having the form of a keyword
       (i.e., it matches the ABNF rule `"@"1*ALPHA` from [RFC5234]),
       return; processors *SHOULD* generate a warning.
    4. Otherwise, set the IRI mapping of *definition* to the
       result of IRI expanding the value associated with the `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry),
       using *local context*, and *defined*.
       If the result does not have the [form](https://tools.ietf.org/html/rfc3987#section-2.2) of an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier),
       an `invalid IRI mapping` error has been detected and processing is aborted.
    5. If *value* contains an `@container` [entry](https://infra.spec.whatwg.org/#map-entry),
       set the container mapping of *definition* to an [array](https://infra.spec.whatwg.org/#list) containing its value;
       if its value is neither `@set`, nor `@index`, nor `null`, an `invalid reverse property` error has been detected (reverse properties only support set- and
       index-containers) and processing is aborted.
    6. Set the reverse property flag of *definition* to `true`.
    7. Set the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) of *term* in *active context* to *definition* and the
       value associated with *defined*'s [entry](https://infra.spec.whatwg.org/#map-entry) *term* to `true` and return.

14. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@id` and its value
    does not equal *term*:

    1. If the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) of *value* is `null`, the term is not used for IRI expansion, but is
       retained to be able to detect future redefinitions of this term.
    2. Otherwise:
       1. If the value associated with the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) is not a [string](https://infra.spec.whatwg.org/#javascript-string), an `invalid IRI mapping` error has been detected and processing is aborted.
       2. If the value associated with the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) is not a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword), but
          has the form of a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) (i.e., it matches the ABNF rule `"@"1*ALPHA` from [RFC5234]),
          return; processors *SHOULD* generate a warning.
       3. Otherwise, set the IRI mapping of *definition* to the
          result of IRI expanding the value associated with the `@id` [entry](https://infra.spec.whatwg.org/#map-entry),
          using *local context*, and *defined*.
          If the resulting IRI mapping is neither a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword), nor an [IRI](https://tools.ietf.org/html/rfc3987#section-2), nor a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), an `invalid IRI mapping` error has been detected and processing is aborted; if it equals `@context`, an `invalid keyword alias` error has been detected and processing is aborted.
       4. If the *term* contains a colon (`:`)
          anywhere but as the first or last character of *term*,
          or if it contains a slash (`/`) anywhere:
          1. Set the value associated with *defined*'s *term* [entry](https://infra.spec.whatwg.org/#map-entry) to `true`.
          2. If the result of IRI expanding *term* using *local context*, and *defined*,
             is not the same as the IRI mapping of *definition*,
             an `invalid IRI mapping` error has been detected and processing is aborted.
       5. If *term* contains neither a colon (`:`) nor a slash (`/`), *simple term* is `true`,
          and if the IRI mapping of *definition* is either an [IRI](https://tools.ietf.org/html/rfc3987#section-2) ending with a [gen-delim](https://tools.ietf.org/html/rfc3986#section-2.2) character,
          or a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier),
          set the prefix flag in *definition* to `true`.

15. Otherwise if the *term* contains a colon (`:`) anywhere after the first character:

    1. If *term* is a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) with a [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix) that is an [entry](https://infra.spec.whatwg.org/#map-entry) in *local context* a dependency has been found. Use this algorithm recursively passing *active context*, *local context*, the [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix) as *term*, and *defined*.
    2. If *term*'s [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix) has a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in *active context*, set
       the IRI mapping of *definition* to the result of
       concatenating the value associated with the [prefix's](https://www.w3.org/TR/json-ld11/#dfn-prefix) IRI mapping and the *term*'s *suffix*.
    3. Otherwise, *term* is an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier). Set the IRI mapping of *definition* to *term*.

16. Otherwise if the *term* contains a slash (`/`):

    1. *Term* is a [relative IRI reference](https://tools.ietf.org/html/rfc3987#section-6.5).
    2. Set the IRI mapping of *definition* to the
       result of IRI expanding *term*.
       If the resulting IRI mapping is not an [IRI](https://tools.ietf.org/html/rfc3987#section-2), an `invalid IRI mapping` error has been detected and processing is aborted.

17. Otherwise, if term is `@type`, set the IRI mapping of *definition* to `@type`.

18. Otherwise, if *active context* has a [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping), the IRI mapping of *definition* is set to the result of concatenating the value
    associated with the [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping) and *term*.
    If it does not have a [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping), an `invalid IRI mapping` error been detected and processing is aborted.

19. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@container`:

    1. Initialize *container* to the value associated with the `@container` [entry](https://infra.spec.whatwg.org/#map-entry), which *MUST* be either `@graph`, `@id`, `@index`, `@language`, `@list`, `@set`, `@type`, or an [array](https://infra.spec.whatwg.org/#list) containing exactly any one of those keywords,
       an [array](https://infra.spec.whatwg.org/#list) containing `@graph` and
       either `@id` or `@index` optionally
       including `@set`,
       or an [array](https://infra.spec.whatwg.org/#list) containing a combination of `@set` and any of `@index`, `@graph`, `@id`, `@type`, `@language` in any order .
       Otherwise, an `invalid container mapping` has been detected and processing is aborted.
    2. If the container value
       is `@graph`, `@id`, or `@type`, or is otherwise not a [string](https://infra.spec.whatwg.org/#javascript-string),
       generate an `invalid container mapping` error and abort processing if [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`.
    3. Set the container mapping of *definition* to *container* coercing to an [array](https://infra.spec.whatwg.org/#list), if necessary.
    4. If the container mapping of *definition* includes `@type`:
       1. If *type mapping* in *definition* is undefined, set it to `@id`.
       2. If *type mapping* in *definition* is neither `@id` nor `@vocab`,
          an `invalid type mapping` error has been detected and processing is aborted.

20. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@index`:

    1. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0` or container mapping does not include `@index`,
       an `invalid term definition` has been detected and processing is aborted.
    2. Initialize *index* to the value associated with the `@index` [entry](https://infra.spec.whatwg.org/#map-entry).
       If the result of IRI expanding that value is not an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
       an `invalid term definition` has been detected and processing is aborted.
    3. Set the index mapping of *definition* to *index*

21. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@context`:

    1. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`, an `invalid term definition` has been detected and processing is aborted.

    2. Initialize *context* to the value associated with the `@context` [entry](https://infra.spec.whatwg.org/#map-entry), which is treated as a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context).

    3. Invoke the §4.1 Context Processing Algorithm using the *active context*, *context* as *local context*, *base URL*, `true` for *override protected*, a copy of *remote contexts*,
       and `false` for *validate scoped context*.
       If any error is detected, an `invalid scoped context` error
       has been detected and processing is aborted.
       > **Note:**
       >
       > > **Note:**
       > >
       > > Note
       >
       > The result of the §4.1 Context Processing Algorithm is discarded; it is called to detect errors at definition time.
       > If used, the context will be re-processed and applied to the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) as part of expansion or compaction.

    4. Set the [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) of *definition* to *context*,
       and base URL to *base URL*.

22. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@language` and
    does not contain the [entry](https://infra.spec.whatwg.org/#map-entry) `@type`:

    1. Initialize *language* to the value associated with the `@language` [entry](https://infra.spec.whatwg.org/#map-entry), which *MUST* be either `null` or a [string](https://infra.spec.whatwg.org/#javascript-string). If *language* is not well-formed according to [section 2.2.9](https://tools.ietf.org/html/bcp47#section-2.2.9) of [BCP47],
       processors *SHOULD* issue a warning. Otherwise, an `invalid language mapping` error has been detected and processing is aborted.
    2. Set the language mapping of *definition* to *language*.
       > **Note:**
       >
       > > **Note:**
       > >
       > > Note
       >
       > Processors *MAY* normalize [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) to lower case.

23. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@direction` and
    does not contain the [entry](https://infra.spec.whatwg.org/#map-entry) `@type`:

    1. Initialize *direction* to the value associated with the `@direction` [entry](https://infra.spec.whatwg.org/#map-entry), which *MUST* be either `null`, `"ltr"`, or `"rtl"`. Otherwise, an `invalid base direction` error has been detected and processing is aborted.
    2. Set the direction mapping of *definition* to *direction*.

24. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@nest`:

    1. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`, an `invalid term definition` has been detected and processing is aborted.
    2. Initialize nest value in *definition* to the value associated with the `@nest` [entry](https://infra.spec.whatwg.org/#map-entry), which *MUST* be a [string](https://infra.spec.whatwg.org/#javascript-string) and *MUST NOT* be a keyword other than `@nest`. Otherwise, an `invalid @nest value` error has been detected and processing is aborted.

25. If *value* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@prefix`:

    1. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`, or if *term* contains a colon (`:`) or slash (`/`), an `invalid term definition` has been detected and processing is aborted.
    2. Set the prefix flag to the value associated with the `@prefix` [entry](https://infra.spec.whatwg.org/#map-entry), which *MUST* be a [boolean](https://infra.spec.whatwg.org/#boolean). Otherwise, an `invalid @prefix value` error has been detected and processing is aborted.
    3. If the prefix flag of *definition* is set to `true`,
       and its IRI mapping is a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword),
       an `invalid term definition` has been detected and processing is aborted.

26. If *value* contains any [entry](https://infra.spec.whatwg.org/#map-entry) other than `@id`, `@reverse`, `@container`, `@context`, `@direction`, `@index`, `@language`, `@nest`, `@prefix`, `@protected`,
    or `@type`,
    an `invalid term definition` error has
    been detected and processing is aborted.

27. If *override protected* is `false` and *previous definition* exists and is protected;

    1. If *definition* is not the same as *previous definition* (other than the value of protected),
       a `protected term redefinition` error has been detected,
       and processing is aborted.
    2. Set *definition* to *previous definition* to retain the value
       of protected.

28. Set the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) of *term* in *active context* to *definition* and set the value
    associated with *defined*'s [entry](https://infra.spec.whatwg.org/#map-entry) *term* to `true`.

### 4.3 Inverse Context Creation

When there is more than one [term](https://www.w3.org/TR/json-ld11/#dfn-term) that could be chosen
to compact an [IRI](https://tools.ietf.org/html/rfc3987#section-2), it has to be ensured that the [term](https://www.w3.org/TR/json-ld11/#dfn-term) selection is both deterministic and represents the most context-appropriate
choice whilst taking into consideration algorithmic complexity.

In order to make [term](https://www.w3.org/TR/json-ld11/#dfn-term) selections, the concept of an inverse context is introduced. An *inverse context* is essentially a reverse lookup table that maps container mapping, type mappings, and language mappings to a simple [term](https://www.w3.org/TR/json-ld11/#dfn-term) for a given [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context). A inverse context only needs to be generated for an [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) if it is being used for compaction.

To make use of an inverse context, a list of preferred container mapping and the type mapping or language mapping are gathered
for a particular value associated with an [IRI](https://tools.ietf.org/html/rfc3987#section-2). These parameters
are then fed to the Term Selection algorithm (§4.4),
which will find the [term](https://www.w3.org/TR/json-ld11/#dfn-term) that most appropriately
matches the value's mappings.

#### 4.3.1 Overview

*This section is non-normative.*

To create an inverse context for a given [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context), each [term](https://www.w3.org/TR/json-ld11/#dfn-term) in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) is visited, ordered by length, shortest
first (ties are broken by choosing the lexicographically least [term](https://www.w3.org/TR/json-ld11/#dfn-term)). For each [term](https://www.w3.org/TR/json-ld11/#dfn-term), an entry is added to
the inverse context for each possible combination of container mapping and type mapping or language mapping that would legally match the [term](https://www.w3.org/TR/json-ld11/#dfn-term). Illegal matches include differences between a
value's type mapping or language mapping and
that of the [term](https://www.w3.org/TR/json-ld11/#dfn-term). If a [term](https://www.w3.org/TR/json-ld11/#dfn-term) has no container mapping, type mapping, or language mapping (or some combination of these), then it
will have an entry in the inverse context using the special
key `@none`. This allows the Term Selection algorithm (§4.4) to fall back
to choosing more generic [terms](https://www.w3.org/TR/json-ld11/#dfn-term) when a more
specifically-matching [term](https://www.w3.org/TR/json-ld11/#dfn-term) is not available for a particular [IRI](https://tools.ietf.org/html/rfc3987#section-2) and value combination.

Although normalizing [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) is optional,
the inverse context creates entries based on normalized [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag), so that the proper term can be selected
regardless of representation.

#### 4.3.2 Algorithm

The algorithm takes one required input: the *active context* that
the inverse context is being created for.

1. Initialize *result* to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
2. Initialize *default language* to `@none`.
   If the *active context* has a [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language),
   set *default language* to the [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) from the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) normalized to lower case.
3. For each key [term](https://www.w3.org/TR/json-ld11/#dfn-term) and value [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in
   the *active context*, ordered by shortest [term](https://www.w3.org/TR/json-ld11/#dfn-term) first (breaking ties by choosing the lexicographically least [term](https://www.w3.org/TR/json-ld11/#dfn-term)):
   1. If the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) is `null`, [term](https://www.w3.org/TR/json-ld11/#dfn-term) cannot be selected during compaction,
      so continue to the next [term](https://www.w3.org/TR/json-ld11/#dfn-term).
   2. Initialize *container* to `@none`. If the container mapping is not empty, set *container* to the concatenation of all values of the container mapping in lexicographical order .
   3. Initialize *var* to the value of the IRI mapping for the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition).
   4. If *var* is not an [entry](https://infra.spec.whatwg.org/#map-entry) of *result*, add
      an [entry](https://infra.spec.whatwg.org/#map-entry) where the key is *var* and the value
      is an empty [map](https://infra.spec.whatwg.org/#ordered-map) to *result*.
   5. Reference the value associated with the *var* [entry](https://infra.spec.whatwg.org/#map-entry) in *result* using the variable *container map*.
   6. If *container map* has no *container* [entry](https://infra.spec.whatwg.org/#map-entry),
      create one and set its value to a new [map](https://infra.spec.whatwg.org/#ordered-map) with three [entries](https://infra.spec.whatwg.org/#map-entry).
      The first [entry](https://infra.spec.whatwg.org/#map-entry) is `@language` and its value is a new empty [map](https://infra.spec.whatwg.org/#ordered-map), the second [entry](https://infra.spec.whatwg.org/#map-entry) is `@type` and its value is a new empty [map](https://infra.spec.whatwg.org/#ordered-map), and the third [entry](https://infra.spec.whatwg.org/#map-entry) is `@any` and its value is a new [map](https://infra.spec.whatwg.org/#ordered-map) with the [entry](https://infra.spec.whatwg.org/#map-entry) `@none` set to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
   7. Reference the value associated with the *container* [entry](https://infra.spec.whatwg.org/#map-entry) in *container map* using the variable *type/language map*.
   8. Reference the value associated with the `@type` [entry](https://infra.spec.whatwg.org/#map-entry) in *type/language map* using the variable *type map*.
   9. Reference the value associated with the `@language` [entry](https://infra.spec.whatwg.org/#map-entry) in *type/language map* using the variable *language map*.
   10. If the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) indicates that the [term](https://www.w3.org/TR/json-ld11/#dfn-term) represents a reverse property:
       1. If *type map* does not have an `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry), create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
   11. Otherwise, if [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) has a type mapping which is `@none`:
       1. If *language map* does not have an `@any` [entry](https://infra.spec.whatwg.org/#map-entry), create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
       2. If *type map* does not have an `@any` [entry](https://infra.spec.whatwg.org/#map-entry), create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
   12. Otherwise, if [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) has a type mapping:
       1. If *type map* does not have an [entry](https://infra.spec.whatwg.org/#map-entry) corresponding
          to the type mapping in [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition),
          create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
   13. Otherwise, if [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) has both
       a language mapping and a direction mapping:
       1. Create a new variable *lang dir*.
       2. If neither the language mapping nor the direction mapping are `null`, set *lang dir* to the concatenation
          of language mapping and direction mapping separated by an underscore (`"_"`)
          normalized to lower case.
       3. Otherwise, if language mapping is not `null`,
          set *lang dir* to the language mapping,
          normalized to lower case.
       4. Otherwise, if direction mapping is not `null`,
          set *lang dir* to direction mapping preceded by an underscore (`"_"`).
       5. Otherwise, set *lang dir* to `@null`.
       6. If *language map* does not have a *lang dir* [entry](https://infra.spec.whatwg.org/#map-entry), create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
   14. Otherwise, if [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) has a language mapping (might be `null`):
       1. If the language mapping equals `null`,
          set *language* to `@null`; otherwise
          to the language mapping, normalized to lower case.
       2. If *language map* does not have a *language* [entry](https://infra.spec.whatwg.org/#map-entry),
          create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
   15. Otherwise, if [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) has a direction mapping (might be `null`):
       1. If the direction mapping equals `null`,
          set *direction* to `@none`; otherwise
          to direction mapping preceded by an underscore (`"_"`).
       2. If *language map* does not have a *direction* [entry](https://infra.spec.whatwg.org/#map-entry),
          create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
   16. Otherwise, if *active context* has a [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction):
       1. Initialize a variable *lang dir* with the concatenation of [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) and [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction),
          separate by an underscore (`"_"`),
          normalized to lower case.
       2. If *language map* does not have a *lang dir* [entry](https://infra.spec.whatwg.org/#map-entry),
          create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
       3. If *language map* does not have an `@none` [entry](https://infra.spec.whatwg.org/#map-entry),
          create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
       4. If *type map* does not have an `@none` [entry](https://infra.spec.whatwg.org/#map-entry),
          create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
   17. Otherwise:
       1. If *language map* does not have a *default language* [entry](https://infra.spec.whatwg.org/#map-entry) (after being normalized to lower case),
          create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
       2. If *language map* does not have an `@none` [entry](https://infra.spec.whatwg.org/#map-entry), create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
       3. If *type map* does not have an `@none` [entry](https://infra.spec.whatwg.org/#map-entry), create one and set its value to the [term](https://www.w3.org/TR/json-ld11/#dfn-term) being processed.
4. Return *result*.

### 4.4 Term Selection

This algorithm, invoked via the IRI Compaction algorithm (§6.2),
makes use of an [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) inverse context to find the [term](https://www.w3.org/TR/json-ld11/#dfn-term) that is best
used to compact an [IRI](https://tools.ietf.org/html/rfc3987#section-2). Other
information about a value associated with the [IRI](https://tools.ietf.org/html/rfc3987#section-2) is given,
including which container mapping and which type mapping or language mapping would
be best used to express the value.

#### 4.4.1 Overview

*This section is non-normative.*

The inverse context's entry for
the [IRI](https://tools.ietf.org/html/rfc3987#section-2) will be first searched according to the preferred container mapping, in the order
that they are given. Amongst [terms](https://www.w3.org/TR/json-ld11/#dfn-term) with a matching container mapping, preference will be given to those
with a matching type mapping or language mapping,
over those without a type mapping or language mapping. If there is no [term](https://www.w3.org/TR/json-ld11/#dfn-term) with a matching container mapping then the [term](https://www.w3.org/TR/json-ld11/#dfn-term) without a container mapping that matches the given type mapping or language mapping is selected. If
there is still no selected [term](https://www.w3.org/TR/json-ld11/#dfn-term), then a [term](https://www.w3.org/TR/json-ld11/#dfn-term) with no type mapping or language mapping will
be selected if available. No [term](https://www.w3.org/TR/json-ld11/#dfn-term) will be selected that
has a conflicting type mapping or language mapping.
Ties between [terms](https://www.w3.org/TR/json-ld11/#dfn-term) that have the same
mappings are resolved by first choosing the shortest terms, and then by
choosing the lexicographically least term. Note that these ties are
resolved automatically because they were previously resolved when the Inverse Context Creation algorithm (§4.3) was used to create the inverse context.

#### 4.4.2 Algorithm

This algorithm has five required inputs. They are:
an *active context*,
a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) or [IRI](https://tools.ietf.org/html/rfc3987#section-2) *var*,
an [array](https://infra.spec.whatwg.org/#list) *containers* that represents an
ordered list of preferred container mapping,
a [string](https://infra.spec.whatwg.org/#javascript-string) *type/language* that indicates whether
to look for a [term](https://www.w3.org/TR/json-ld11/#dfn-term) with a matching type mapping or language mapping,
and an [array](https://infra.spec.whatwg.org/#list) representing an ordered list of *preferred values* for the type mapping or language mapping to look for.

1. If the *active context* has a `null` inverse context,
   set inverse context in *active context* to the result of calling the Inverse Context Creation algorithm (§4.3) using *active context*.
2. Initialize *inverse context* to the value of inverse context in *active context*.
3. Initialize *container map* to the value associated with *var* in the *inverse context*.
4. For each item *container* in *containers*:
   1. If *container* is not an [entry](https://infra.spec.whatwg.org/#map-entry) of *container map*, then
      there is no [term](https://www.w3.org/TR/json-ld11/#dfn-term) with a matching container mapping for it, so continue to the next *container*.
   2. Initialize *type/language map* to the value associated
      with the *container* [entry](https://infra.spec.whatwg.org/#map-entry) in *container map*.
   3. Initialize *value map* to the value associated
      with *type/language* [entry](https://infra.spec.whatwg.org/#map-entry) in *type/language map*.
   4. For each *item* in *preferred values*:
      1. If *item* is not an [entry](https://infra.spec.whatwg.org/#map-entry) of *value map*,
         then there is no [term](https://www.w3.org/TR/json-ld11/#dfn-term) with a matching type mapping or language mapping,
         so continue to the next *item*.
      2. Otherwise, a matching term has been found, return the value
         associated with the *item* [entry](https://infra.spec.whatwg.org/#map-entry) in *value map*.
5. No matching term has been found. Return `null`.

#### 4.4.3 Examples

*This section is non-normative.*

The following examples are intended to illustrate how the term selection algorithm
behaves for different term definitions and values. It is not comprehensive, but
intended to illustrate different parts of the algorithm.

##### Language Map Term

If the term definition has `"@container": "@language"`, it will only match a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) having no `@type`.
> **Example:**
>
> Example 14: Term definition with language map
>
> ```
> {
>   "@context": {"t": {"@id": "http://example.org/t", "@container": "@language"}}
> }
> ```
>
> The inverse context will contain the following:
>
> ```
> {
>   "@language": {
>     "@language": {"@none": "t"},
>     "@type": {"@none": "t"},
>     "@any": {"@none": "t"}
>   }
> }
> ```
> **Example:**
>
> Example 15: Language map term with language value
>
> Given the [entry](https://infra.spec.whatwg.org/#map-entry) `{"http://example.org/t": {"@value": "foo", "@type": "http:/example.org/type"}}`,
> The algorithm will be invoked as follows:
>
> *containers*
>
> `["@language", "@language@set", "@set", "@none", "@index", "@index@set"]`
>
> *type/language*
>
> `@language`
>
> *preferred values*
>
> `["en", "@none"]`
>
> The *value map* will be set to `{"@none": "t"}`,
> as *preferred values* contains `"@none"`,
> the algorithm returns `"t"` as the term to use for compaction.

##### Datatyped Term

If the term definition has a datatype, it will only match a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) having a matching datatype.
> **Example:**
>
> Example 16: Term definition with datatype
>
> ```
> {
>   "@context": {"t": {"@id": "http://example.org/t", "@type": "http:/example.org/type"}}
> }
> ```
>
> The inverse context will contain the following:
>
> ```
> {
>   "@none": {
>     "@language": {},
>     "@type": {"http:/example.org/type": "t"},
>     "@any": {"@none": "t"}
>   }
> }
> ```
> **Example:**
>
> Example 17: Datatyped term with datatyped value
>
> Given the [entry](https://infra.spec.whatwg.org/#map-entry) `{"http://example.org/t": {"@value": "foo", "@type": "http:/example.org/type"}}`,
> The algorithm will be invoked as follows:
>
> *containers*
>
> `["@set", "@none", "@index", "@index@set"]`
>
> *type/language*
>
> `@type`
>
> *preferred values*
>
> `["http:/example.org/type", "@none"]`
>
> The *value map* will be set to `{"http:/example.org/type": "t"}`,
> as *preferred values* contains `"http:/example.org/type"`,
> the algorithm returns `"t"` as the term to use for compaction.
> **Example:**
>
> Example 18: Datatyped term with simple value
>
> Given the [entry](https://infra.spec.whatwg.org/#map-entry) `{"http://example.org/t": {"@value": "foo"}}`,
> The algorithm will be invoked as follows:
>
> *containers*
>
> `["@set", "@none", "@index", "@index@set", "@language", "@language@set"]`
>
> *type/language*
>
> `@language`
>
> *preferred values*
>
> `["@null", "@none"]`
>
> The *value map* will be set to `{"@none": "t"}`,
> as no key in *preferred values* matches a key in *value map*,
> the algorithm returns `null` and no term is found.
> **Example:**
>
> Example 19: Datatyped term with object value
>
> Given the [entry](https://infra.spec.whatwg.org/#map-entry) `{"http://example.org/t": {"@id": "http://example.org/id"}}`,
> The algorithm will be invoked as follows:
>
> *containers*
>
> `["@id", "@id@set", "@type", "@set@type", "@set", "@none", "@index", "@index@set"]`
>
> *type/language*
>
> `@type`
>
> *preferred values*
>
> `["@id", "@vocab", "@none"]`
>
> The *value map* will be set to `{"http:/example.org/type": "t"}`,
> as no key in *preferred values* matches a key in *value map*,
> the algorithm returns `null` and no term is found.

## 5. Expansion Algorithms

The following sections describe algorithms for expanding JSON-LD
documents, IRIs and values.

### 5.1 Expansion Algorithm

This algorithm expands a JSON-LD document, such that all [context](https://www.w3.org/TR/json-ld11/#dfn-context) definitions are removed, all [terms](https://www.w3.org/TR/json-ld11/#dfn-term) and [compact IRIs](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) are expanded to [IRIs](https://tools.ietf.org/html/rfc3987#section-2), [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), or [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) and all [JSON-LD values](https://www.w3.org/TR/json-ld11/#dfn-json-ld-value) are expressed in [arrays](https://infra.spec.whatwg.org/#list) in expanded form.

#### 5.1.1 Overview

*This section is non-normative.*

Starting with its root *element*, we can process the
JSON-LD document recursively, until we have a fully expanded *result*. When expanding an *element*, we can treat
each one differently according to its type, in order to break down the
problem:

1. If the *element* is `null`, there is nothing
   to expand.
2. Otherwise, if *element* is a [scalar](https://infra.spec.whatwg.org/#primitive-data-types), we expand it
   according to the Value Expansion algorithm (§5.3).
3. Otherwise, if the *element* is an [array](https://infra.spec.whatwg.org/#list), then we expand
   each of its items recursively and return them in a new [array](https://infra.spec.whatwg.org/#list).
4. Otherwise, *element* is a [map](https://infra.spec.whatwg.org/#ordered-map). We expand
   each of its [entries](https://infra.spec.whatwg.org/#map-entry), adding them to our *result*, and then we expand
   each value for each [entry](https://infra.spec.whatwg.org/#map-entry) recursively. Some of the [entry](https://infra.spec.whatwg.org/#map-entry) keys will be [terms](https://www.w3.org/TR/json-ld11/#dfn-term) or [compact IRIs](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) and others will be [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) or simply ignored because
   they do not have definitions in the [context](https://www.w3.org/TR/json-ld11/#dfn-context). Any [IRIs](https://tools.ietf.org/html/rfc3987#section-2) will be expanded using the IRI Expansion algorithm (§5.2).

Finally, after ensuring *result* is in an [array](https://infra.spec.whatwg.org/#list),
we return *result*.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Although the [data model](https://www.w3.org/TR/json-ld11/#data-model),
> based on [RDF11-CONCEPTS], does not support multiple unordered property values,
> this algorithm does not remove duplicates that
> may be found during expansion within an unordered [array](https://infra.spec.whatwg.org/#list).
> Other algorithms, such as § 6.1 Compaction Algorithm (§6.1),
> and § 7.1 Flattening Algorithm (§7.1), do eliminate
> duplicate values from unordered arrays.
> A future version of this specification may be updated to remove duplicate
> array values when the form a set.

#### 5.1.2 Algorithm

The algorithm takes four required and three optional input variables.
The required inputs are an *active context*,
an *active property*, an *element* to be expanded, and a *base URL* associated with the `documentUrl` of the original
document to expand. The optional inputs are the `frameExpansion` flag allowing special forms of input used for [frame expansion](https://www.w3.org/TR/json-ld11-framing/#dfn-framing),
the `ordered` flag, used to order [map entry](https://infra.spec.whatwg.org/#map-entry) keys lexicographically, where noted,
and the *from map* flag, used to control reverting
previous [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) associated with non-propagated [contexts](https://www.w3.org/TR/json-ld11/#dfn-context).
If not passed, the optional flags are set to `false`.

The algorithm also performs processing steps specific to expanding
a [JSON-LD Frame](https://www.w3.org/TR/json-ld11-framing/#dfn-frame). For a [frame](https://www.w3.org/TR/json-ld11-framing/#dfn-frame), the `@id` and `@type` [entries](https://infra.spec.whatwg.org/#map-entry) can accept an array of [IRIs](https://tools.ietf.org/html/rfc3987#section-2) or
an empty [map](https://infra.spec.whatwg.org/#ordered-map). The [entries](https://infra.spec.whatwg.org/#map-entry) of a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) can also
accept an [array](https://infra.spec.whatwg.org/#list) of [strings](https://infra.spec.whatwg.org/#javascript-string), or an empty [map](https://infra.spec.whatwg.org/#ordered-map).
Framing also uses additional keyword [entries](https://infra.spec.whatwg.org/#map-entry):
(`@explicit`, `@default`, `@embed`, `@explicit`, `@omitDefault`, or `@requireAll`) which are preserved through expansion.
Special processing for a [JSON-LD Frame](https://www.w3.org/TR/json-ld11-framing/#dfn-frame) is invoked when the `frameExpansion` flag is set to `true`.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> As mentioned in [Terms](https://www.w3.org/TR/json-ld11/#terms) [JSON-LD11],
> to avoid forward-compatibility issues, [terms](https://www.w3.org/TR/json-ld11/#dfn-term) should not start with an `@` character as future versions of JSON-LD may introduce
> additional [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword).
> This algorithm will treat such terms like any other term, i.e., they are ignored unless mapped to an [IRI](https://tools.ietf.org/html/rfc3987#section-2).
> Implementations of this algorithm may consider providing a
> runtime flag to show a warning if such terms are encountered.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The use of empty [terms](https://www.w3.org/TR/json-ld11/#dfn-term) (`""`) is not
> allowed as not all programming languages are able to handle empty JSON keys.
> Implementations of this algorithm may consider providing a
> runtime flag to show a warning if such terms are encountered.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
> and may be removed in a future version of JSON-LD.
> Implementations of this algorithm may consider providing a
> runtime flag to show a warning if such terms are encountered.

1. If *element* is `null`, return `null`.
2. If *active property* is `@default`,
   initialize the `frameExpansion` flag to `false`.
3. If *active property* has a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in *active context* with a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context), initialize *property-scoped context* to that [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context).
4. If *element* is a [scalar](https://infra.spec.whatwg.org/#primitive-data-types),
   1. If *active property* is `null` or `@graph`,
      drop the free-floating [scalar](https://infra.spec.whatwg.org/#primitive-data-types) by returning `null`.
   2. If *property-scoped context* is defined,
      set *active context* to the result of the §4.1 Context Processing Algorithm,
      passing *active context*, *property-scoped context* as *local context*,
      and *base URL* from the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *active property* in *active context*.
   3. Return the result of the Value Expansion algorithm (§5.3), passing the *active context*, *active property*, and *element* as *value*.
5. If *element* is an [array](https://infra.spec.whatwg.org/#list),
   1. Initialize an empty array, *result*.
   2. For each *item* in *element*:
      1. Initialize *expanded item* to the result of using this
         algorithm recursively, passing *active context*, *active property*, *item* as *element*, *base URL*, the `frameExpansion` `ordered`,
         and *from map* flags.
      2. If the container mapping of *active property* includes `@list`,
         and *expanded item* is an [array](https://infra.spec.whatwg.org/#list), set *expanded item* to a new [map](https://infra.spec.whatwg.org/#ordered-map) containing the [entry](https://infra.spec.whatwg.org/#map-entry) `@list` where the value is the original *expanded item*.
      3. If *expanded item* is an [array](https://infra.spec.whatwg.org/#list), append each
         of its items to *result*. Otherwise, if *expanded item* is not null, append it to *result*.
   3. Return *result*.
6. Otherwise *element* is a [map](https://infra.spec.whatwg.org/#ordered-map).
7. If *active context* has a previous context,
   the *active context* is not propagated.
   If *from map* is undefined or `false`,
   and *element* does not contain an [entry](https://infra.spec.whatwg.org/#map-entry) expanding to `@value`,
   and *element* does not consist of a single [entry](https://infra.spec.whatwg.org/#map-entry) expanding to `@id` (where [entries](https://infra.spec.whatwg.org/#map-entry) are IRI expanded,
   set *active context* to previous context from *active context*,
   as the scope of a term-scoped [context](https://www.w3.org/TR/json-ld11/#dfn-context) does not apply when processing new [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object).
8. If *property-scoped context* is defined,
   set *active context* to the result of the §4.1 Context Processing Algorithm,
   passing *active context*, *property-scoped context* as *local context*, *base URL* from the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *active property*,
   in *active context* and `true` for *override protected*.
9. If *element* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@context`, set *active context* to the result of the §4.1 Context Processing Algorithm,
   passing *active context*, the value of the `@context` [entry](https://infra.spec.whatwg.org/#map-entry) as *local context* and *base URL*.
10. Initialize *type-scoped context* to *active context*.
    This is used for expanding values that may be relevant to any previous [type-scoped context](https://www.w3.org/TR/json-ld11/#dfn-type-scoped-context).
11. For each *key* and *value* in *element* ordered lexicographically by *key* where *key* IRI expands to `@type`:
    1. Convert *value* into an [array](https://infra.spec.whatwg.org/#list), if necessary.
    2. For each *term* which is a value of *value* ordered lexicographically,
       if *term* is a [string](https://infra.spec.whatwg.org/#javascript-string),
       and *term*'s [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in *type-scoped context* has a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context), set *active context* to the result §4.1 Context Processing Algorithm,
       passing *active context*,
       the value of the *term*'s [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) as *local context*, *base URL* from the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *value* in *active context*,
       and `false` for *propagate*.
12. Initialize two empty [maps](https://infra.spec.whatwg.org/#ordered-map), *result* and *nests*.
    Initialize *input type* to expansion of the last value of the first [entry](https://infra.spec.whatwg.org/#map-entry) in *element* expanding to `@type` (if any), ordering [entries](https://infra.spec.whatwg.org/#map-entry) lexicographically by key.
    Both the key and value of the matched entry are IRI expanded.
13. For each *key* and *value* in *element*,
    ordered lexicographically by *key* if `ordered` is `true`:
    1. If *key* is `@context`, continue to
       the next *key*.
    2. Initialize *expanded property* to the result of IRI expanding *key*.
    3. If *expanded property* is `null` or it neither
       contains a colon (`:`) nor it is a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword),
       drop *key* by continuing to the next *key*.
    4. If *expanded property* is a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword):
       1. If *active property* equals `@reverse`, an `invalid reverse property map` error has been detected and processing is aborted.
       2. If *result* already has an *expanded property* [entry](https://infra.spec.whatwg.org/#map-entry), other than `@included` or `@type` (unless [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`),
          a `colliding keywords` error has been detected and processing is aborted.
       3. If *expanded property* is `@id`:
          1. If *value* is not a [string](https://infra.spec.whatwg.org/#javascript-string), an `invalid @id value` error has been detected and processing is aborted. When the `frameExpansion` flag is set, *value* *MAY* be an empty [map](https://infra.spec.whatwg.org/#ordered-map), or an [array](https://infra.spec.whatwg.org/#list) of one
             or more [strings](https://infra.spec.whatwg.org/#javascript-string).
          2. Otherwise,
             set *expanded value* to the result of IRI expanding *value* using `true` for *document relative* and `false` for *vocab*. When the `frameExpansion` flag is set, *expanded value* will be
             an [array](https://infra.spec.whatwg.org/#list) of one or more of the values, with [string](https://infra.spec.whatwg.org/#javascript-string) values expanded using the IRI Expansion algorithm (§5.2) as above.
       4. If *expanded property* is `@type`:
          1. If *value* is neither a [string](https://infra.spec.whatwg.org/#javascript-string) nor an [array](https://infra.spec.whatwg.org/#list) of [strings](https://infra.spec.whatwg.org/#javascript-string), an `invalid type value` error has been detected and processing is aborted. When the `frameExpansion` flag is set, *value* *MAY* be an empty [map](https://infra.spec.whatwg.org/#ordered-map), or a [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object) where the value of `@default` is restricted to be
             an [IRI](https://tools.ietf.org/html/rfc3987#section-2).
             All other values mean that `invalid type value` error has been detected and processing is aborted.
          2. If *value* is an empty [map](https://infra.spec.whatwg.org/#ordered-map), set *expanded value* to *value*.
          3. Otherwise, if *value* is a [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object), set *expanded value* to
             a new [default object](https://www.w3.org/TR/json-ld11/#dfn-default-object) with the value of `@default` set
             to the result of IRI expanding *value* using *type-scoped context* for *active context*,
             and `true` for *document relative*.
          4. Otherwise,
             set *expanded value* to the result of IRI expanding each of its values
             using *type-scoped context* for *active context*,
             and `true` for *document relative*.
          5. If *result* already has an entry for `@type`,
             prepend the value of `@type` in *result* to *expanded value*,
             transforming it into an [array](https://infra.spec.whatwg.org/#list), if necessary.
             > **Note:**
             >
             > > **Note:**
             > >
             > > Note
             >
             > No transformation from a [string](https://infra.spec.whatwg.org/#javascript-string) *value* to an [array](https://infra.spec.whatwg.org/#list) *expanded value* is implied, and the form or *value* should be preserved in *expanded value*.

       5. If *expanded property* is `@graph`, set *expanded value* to the result of using this algorithm
          recursively passing *active context*, `@graph` for *active property*, *value* for *element*, *base URL*, and the `frameExpansion` and `ordered` flags, ensuring that *expanded value* is an [array](https://infra.spec.whatwg.org/#list) of one or more [maps](https://infra.spec.whatwg.org/#ordered-map).
       6. If *expanded property* is `@included`:
          1. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`,
             continue with the next *key* from *element*.
          2. Set *expanded value* to the result of using
             this algorithm recursively passing *active context*, `null` for *active property*, *value* for *element*, *base URL*,
             and the `frameExpansion` and `ordered` flags,
             ensuring that the result is an [array](https://infra.spec.whatwg.org/#list).
          3. If any element of *expanded value* is not a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object),
             an `invalid @included value` error has been detected and processing is aborted.
          4. If *result* already has an entry for `@included`,
             prepend the value of `@included` in *result* to *expanded value*.
       7. If *expanded property* is `@value`:
          1. If *input type* is `@json`,
             set *expanded value* to *value*.
             If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`,
             an `invalid value object value` error has been detected and processing is aborted.
          2. Otherwise, if *value* is not a [scalar](https://infra.spec.whatwg.org/#primitive-data-types) or `null`,
             an `invalid value object value` error has been detected and processing is aborted. When the `frameExpansion` flag is set, *value* *MAY* be an empty [map](https://infra.spec.whatwg.org/#ordered-map) or an array of [scalar](https://infra.spec.whatwg.org/#primitive-data-types) values.
          3. Otherwise, set *expanded value* to *value*. When the `frameExpansion` flag is set, *expanded value* will be an [array](https://infra.spec.whatwg.org/#list) of one or more [string](https://infra.spec.whatwg.org/#javascript-string) values
             or an [array](https://infra.spec.whatwg.org/#list) containing an empty [map](https://infra.spec.whatwg.org/#ordered-map).
          4. If *expanded value* is `null`, set the `@value` [entry](https://infra.spec.whatwg.org/#map-entry) of *result* to `null` and continue with the
             next *key* from *element*. Null values need to be preserved
             in this case as the meaning of an `@type` [entry](https://infra.spec.whatwg.org/#map-entry) depends
             on the existence of an `@value` [entry](https://infra.spec.whatwg.org/#map-entry).
       8. If *expanded property* is `@language`:
          1. If *value* is not a [string](https://infra.spec.whatwg.org/#javascript-string), an `invalid language-tagged string` error has been detected and processing is aborted. When the `frameExpansion` flag is set, *value* *MAY* be an empty [map](https://infra.spec.whatwg.org/#ordered-map) or an array of zero or more [strings](https://infra.spec.whatwg.org/#javascript-string).
          2. Otherwise, set *expanded value* to *value*.
             If *value* is not well-formed according to [section 2.2.9](https://tools.ietf.org/html/bcp47#section-2.2.9) of [BCP47],
             processors *SHOULD* issue a warning.
             When the `frameExpansion` flag is set, *expanded value* will be an [array](https://infra.spec.whatwg.org/#list) of one or more [string](https://infra.spec.whatwg.org/#javascript-string) values
             or an [array](https://infra.spec.whatwg.org/#list) containing an empty [map](https://infra.spec.whatwg.org/#ordered-map).
             > **Note:**
             >
             > > **Note:**
             > >
             > > Note
             >
             > Processors *MAY* normalize [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) to lower case.

       9. If *expanded property* is `@direction`:
          1. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.0`,
             continue with the next *key* from *element*.
          2. If *value* is neither `"ltr"` nor `"rtl"`, an `invalid base direction` error has been detected and processing is aborted.
             When the `frameExpansion` flag is set, *value* *MAY* be an empty [map](https://infra.spec.whatwg.org/#ordered-map) or an array of zero or more [strings](https://infra.spec.whatwg.org/#javascript-string).
          3. Otherwise, set *expanded value* to *value*.
             When the `frameExpansion` flag is set, *expanded value* will be an [array](https://infra.spec.whatwg.org/#list) of one or more [string](https://infra.spec.whatwg.org/#javascript-string) values
             or an [array](https://infra.spec.whatwg.org/#list) containing an empty [map](https://infra.spec.whatwg.org/#ordered-map).
       10. If *expanded property* is `@index`:
           1. If *value* is not a [string](https://infra.spec.whatwg.org/#javascript-string), an `invalid @index value` error has been detected and processing is aborted.
           2. Otherwise,
              set *expanded value* to *value*.
       11. If *expanded property* is `@list`:
           1. If *active property* is `null` or `@graph`, continue with the next *key* from *element* to remove the free-floating list.
           2. Otherwise, initialize *expanded value* to the result of using
              this algorithm recursively passing *active context*, *active property*, *value* for *element*, *base URL*, and the `frameExpansion` and `ordered` flags,
              ensuring that the result is an [array](https://infra.spec.whatwg.org/#list)..
       12. If *expanded property* is `@set`, set *expanded value* to the result of using this algorithm
           recursively, passing *active context*, *active property*, *value* for *element*, *base URL*, and the `frameExpansion` and `ordered` flags.
       13. If *expanded property* is `@reverse`:
           1. If *value* is not a [map](https://infra.spec.whatwg.org/#ordered-map), an `invalid @reverse value` error has been detected and processing is aborted.
           2. Otherwise initialize *expanded value* to the result of using this
              algorithm recursively, passing *active context*, `@reverse` as *active property*, *value* as *element*, *base URL*, and the `frameExpansion` and `ordered` flags.
           3. If *expanded value* contains an `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry),
              i.e., [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) that are reversed twice, execute for each of its *property* and *item* the following steps:
              1. Use add value to add *item* to the *property* [entry](https://infra.spec.whatwg.org/#map-entry) in *result* using `true` for *as array*.
           4. If *expanded value* contains an [entry](https://infra.spec.whatwg.org/#map-entry) other than `@reverse`:
              1. Set *reverse map* to the value
                 of the `@reverse` entry in *result*,
                 initializing it to an empty [map](https://infra.spec.whatwg.org/#ordered-map), if necessary.
              2. For each *property* and *items* in *expanded value* other than `@reverse`:
                 1. For each *item* in *items*:
                    1. If *item* is a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) or [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object), an `invalid reverse property value` has been detected and processing is aborted.
                    2. Use add value to add *item* to the *property* [entry](https://infra.spec.whatwg.org/#map-entry) in *reverse map* using `true` for *as array*.
           5. Continue with the next *key* from *element*.
       14. If *expanded property* is `@nest`,
           add *key* to *nests*, initializing it to an empty [array](https://infra.spec.whatwg.org/#list),
           if necessary.
           Continue with the next *key* from *element*.
       15. When the `frameExpansion` flag is set,
           if *expanded property* is any other
           framing keyword (`@default`, `@embed`, `@explicit`, `@omitDefault`, or `@requireAll`),
           set *expanded value* to the result of performing the §5.1 Expansion Algorithm recursively, passing *active context*, *active property*, *value* for *element*, *base URL*, and the `frameExpansion` and `ordered` flags.
       16. Unless *expanded value* is `null`, *expanded property* is `@value`,
           and *input type* is not `@json`, set the *expanded property* [entry](https://infra.spec.whatwg.org/#map-entry) of *result* to *expanded value*.
       17. Continue with the next *key* from *element*.
    5. Initialize *container mapping* to *key*'s container mapping in *active context*.
    6. If *key*'s [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in *active context* has a type mapping of `@json`,
       set *expanded value* to a new [map](https://infra.spec.whatwg.org/#ordered-map), set the [entry](https://infra.spec.whatwg.org/#map-entry) `@value` to *value*, and set the entry `@type` to `@json`.
    7. Otherwise, if *container mapping* includes `@language` and *value* is a [map](https://infra.spec.whatwg.org/#ordered-map) then *value* is expanded from a [language map](https://www.w3.org/TR/json-ld11/#dfn-language-map) as follows:
       1. Initialize *expanded value* to an empty [array](https://infra.spec.whatwg.org/#list).
       2. Initialize *direction* to the [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) from *active context*.
       3. If *key*'s [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) has a direction mapping,
          update *direction* with that value.
       4. For each key-value pair *language*-*language value* in *value*, ordered lexicographically by *language* if `ordered` is `true`:
          1. If *language value* is not an [array](https://infra.spec.whatwg.org/#list) set *language value* to an [array](https://infra.spec.whatwg.org/#list) containing only *language value*.
          2. For each *item* in *language value*:
             1. If *item* is `null`,
                continue to the next entry in *language value*.

             2. *item* must be a [string](https://infra.spec.whatwg.org/#javascript-string),
                otherwise an `invalid language map value` error has been detected and processing is aborted.

             3. Initialize a new [map](https://infra.spec.whatwg.org/#ordered-map) *v* consisting of two
                key-value pairs: (`@value`-*item*)
                and (`@language`-*language*). If *item* is neither `@none` nor well-formed according to [section 2.2.9](https://tools.ietf.org/html/bcp47#section-2.2.9) of [BCP47],
                processors *SHOULD* issue a warning.
                > **Note:**
                >
                > > **Note:**
                > >
                > > Note
                >
                > Processors *MAY* normalize [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) to lower case.

             4. If *language* is `@none`,
                or expands to `@none`, remove `@language` from *v*.

             5. If *direction* is not `null`,
                add an [entry](https://infra.spec.whatwg.org/#map-entry) for `@direction` to *v* with *direction*.

             6. Append *v* to *expanded value*.

    8. Otherwise, if *container mapping* includes `@index`, `@type`, or `@id` and *value* is a [map](https://infra.spec.whatwg.org/#ordered-map) then *value* is expanded from an map as follows:
       1. Initialize *expanded value* to an empty [array](https://infra.spec.whatwg.org/#list).
       2. Initialize *index key* to
          the *key*'s index mapping in [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context),
          or `@index`, if it does not exist.
       3. For each key-value pair *index*-*index value* in *value*, ordered lexicographically by *index* if `ordered` is `true`:
          1. If *container mapping* includes `@id` or `@type`,
             initialize *map context* to the previous context from *active context* if it exists,
             otherwise, set *map context* to *active context*.
          2. If *container mapping* includes `@type` and *index*'s [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in *map context* has a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context), update *map context* to the result of the §4.1 Context Processing Algorithm,
             passing *map context* as *active context* the value of the *index*'s [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) as *local context* and *base URL* from the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *index* in *map context*.
          3. Otherwise, set *map context* to *active context*.
          4. Initialize *expanded index* to the result of IRI expanding *index*.
          5. If *index value* is not an [array](https://infra.spec.whatwg.org/#list) set *index value* to an [array](https://infra.spec.whatwg.org/#list) containing only *index value*.
          6. Initialize *index value* to the result of
             using this algorithm recursively, passing *map context* as *active context*, *key* as *active property*, *index value* as *element*, *base URL*, `true` for *from map*,
             and the `frameExpansion` and `ordered` flags.
          7. For each *item* in *index value*:
             1. If *container mapping* includes `@graph`, and *item* is not a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object), set *item* to a new [map](https://infra.spec.whatwg.org/#ordered-map) containing the key-value pair `@graph`-*item*,
                ensuring that the value is represented using an [array](https://infra.spec.whatwg.org/#list).
             2. If *container mapping* includes `@index`, *index key* is not `@index`,
                and *expanded index* is not `@none`:
                1. Initialize *re-expanded index* to the result of calling
                   the Value Expansion algorithm (§5.3),
                   passing the *active context*, *index key* as *active property*,
                   and *index* as *value*.
                2. Initialize *expanded index key* to the result of IRI expanding *index key*.
                3. Initialize *index property values* to
                   an [array](https://infra.spec.whatwg.org/#list) consisting of *re-expanded index* followed
                   by the existing values of
                   the concatenation of *expanded index key* in *item*,
                   if any.
                4. Add the key-value pair (*expanded index key*-*index property values*)
                   to *item*.
                5. If *item* is a value object,
                   it *MUST NOT* contain any extra properties;
                   an `invalid value object` error has been detected and processing is aborted.
             3. Otherwise, if *container mapping* includes `@index`, *item* does not have an [entry](https://infra.spec.whatwg.org/#map-entry) `@index`,
                and *expanded index* is not `@none`,
                add the key-value pair (`@index`-*index*) to *item*.
             4. Otherwise, if *container mapping* includes `@id` *item* does not have the [entry](https://infra.spec.whatwg.org/#map-entry) `@id`,
                and *expanded index* is not `@none`,
                add the key-value pair (`@id`-*expanded index*) to *item*,
                where *expanded index* is set to the result of IRI expanding*index* using `true` for *document relative* and `false` for *vocab*.
             5. Otherwise, if *container mapping* includes `@type` and *expanded index* is not `@none`,
                initialize *types* to a new [array](https://infra.spec.whatwg.org/#list) consisting of *expanded index* followed by any existing
                values of `@type` in *item*.
                Add the key-value pair (`@type`-*types*) to *item*.
             6. Append *item* to *expanded value*.
    9. Otherwise, initialize *expanded value* to the result of
       using this algorithm recursively, passing *active context*, *key* for *active property*, *value* for *element*, *base URL*, and the `frameExpansion` and `ordered` flags.
    10. If *expanded value* is `null`, ignore *key* by continuing to the next *key* from *element*.
    11. If *container mapping* includes `@list` and *expanded value* is not already a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object),
        convert *expanded value* to a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object) by first setting it to an [array](https://infra.spec.whatwg.org/#list) containing only *expanded value* if it is not already an [array](https://infra.spec.whatwg.org/#list),
        and then by setting it to a [map](https://infra.spec.whatwg.org/#ordered-map) containing
        the key-value pair `@list`-*expanded value*.
    12. If *container mapping* includes `@graph`,
        and includes neither `@id` nor `@index`,
        convert *expanded value* into an [array](https://infra.spec.whatwg.org/#list), if necessary,
        then convert each value *ev* in *expanded value* into a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object):
        1. Convert *ev* into
           a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object) by creating a [map](https://infra.spec.whatwg.org/#ordered-map) containing the key-value
           pair `@graph`-*ev* where *ev* is represented as an [array](https://infra.spec.whatwg.org/#list).
           > **Note:**
           >
           > > **Note:**
           > >
           > > Note
           >
           > This may lead to a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object) including another [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object),
           > if *ev* was already in the form of a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object).

    13. If the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) associated to *key* indicates that it is a reverse property
        1. If *result* has no `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry), create
           one and initialize its value to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
        2. Reference the value of the `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry) in *result* using the variable *reverse map*.
        3. If *expanded value* is not an [array](https://infra.spec.whatwg.org/#list), set
           it to an [array](https://infra.spec.whatwg.org/#list) containing *expanded value*.
        4. For each *item* in *expanded value*
           1. If *item* is a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) or [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object), an `invalid reverse property value` has been detected and processing is aborted.
           2. If *reverse map* has no *expanded property* [entry](https://infra.spec.whatwg.org/#map-entry),
              create one and initialize its value to an empty [array](https://infra.spec.whatwg.org/#list).
           3. Use add value to add *item* to the *expanded property* [entry](https://infra.spec.whatwg.org/#map-entry) in *reverse map* using `true` for *as array*.
    14. Otherwise, *key* is not a reverse property use add value to add *expanded value* to the *expanded property* [entry](https://infra.spec.whatwg.org/#map-entry) in *result* using `true` for *as array*.
14. For each key *nesting-key* in *nests*,
    ordered lexicographically if `ordered` is `true`:
    1. Initialize *nested values* to the value of *nesting-key* in *element*, ensuring that it is an [array](https://infra.spec.whatwg.org/#list).
    2. For each *nested value* in *nested values*:
       1. If *nested value* is not a [map](https://infra.spec.whatwg.org/#ordered-map), or any key within *nested value* expands to `@value`, an `invalid @nest value` error
          has been detected and processing is aborted.
       2. Recursively repeat steps 13 and 14 using *nested value* for *element*.
          > **Note:**
          >
          > > **Note:**
          > >
          > > Note
          >
          > By invoking steps 13 and 14 on *nested value* we are able to unfold arbitrary levels of nesting, with results being merged into *result*.
          > Step 13 iterates through each
          > entry in *nested value* and expands it, while collecting new *nested values* found at each level, until all nesting has been extracted.

15. If *result* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@value`:
    1. The *result* must not contain any [entries](https://infra.spec.whatwg.org/#map-entry) other than `@direction`, `@index`, `@language`, `@type`,
       and `@value`.
       It must not contain an `@type` [entry](https://infra.spec.whatwg.org/#map-entry) if it contains either `@language` or `@direction` [entries](https://infra.spec.whatwg.org/#map-entry).
       Otherwise, an `invalid value object` error has been detected and processing is aborted.
    2. If the *result*'s `@type` [entry](https://infra.spec.whatwg.org/#map-entry) is `@json`, then the `@value` [entry](https://infra.spec.whatwg.org/#map-entry) may
       contain any value, and is treated as a [JSON literal](https://www.w3.org/TR/json-ld11/#dfn-json-literal).
    3. Otherwise, if the value of *result*'s `@value` [entry](https://infra.spec.whatwg.org/#map-entry) is `null`, or an empty [array](https://infra.spec.whatwg.org/#list), return `null`.
    4. Otherwise, if the value of *result*'s `@value` [entry](https://infra.spec.whatwg.org/#map-entry) is not a [string](https://infra.spec.whatwg.org/#javascript-string) and *result* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@language`, an `invalid language-tagged value` error has been detected (only [strings](https://infra.spec.whatwg.org/#javascript-string) can be language-tagged) and processing is aborted.
    5. Otherwise, if the *result* has an `@type` [entry](https://infra.spec.whatwg.org/#map-entry) and its value is not an [IRI](https://tools.ietf.org/html/rfc3987#section-2), an `invalid typed value` error has been detected and processing is aborted.
16. Otherwise, if *result* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@type` and its associated value is not an [array](https://infra.spec.whatwg.org/#list), set it to
    an [array](https://infra.spec.whatwg.org/#list) containing only the associated value.
17. Otherwise, if *result* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@set` or `@list`:
    1. The *result* must contain at most one other [entry](https://infra.spec.whatwg.org/#map-entry) which must be `@index`. Otherwise, an `invalid set or list object` error has been detected and processing is aborted.
    2. If *result* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@set`, then
       set *result* to the [entry's](https://infra.spec.whatwg.org/#map-entry) associated value.
18. If *result* is a [map](https://infra.spec.whatwg.org/#ordered-map) that contains only the [entry](https://infra.spec.whatwg.org/#map-entry) `@language`, return `null`.
19. If *active property* is `null` or `@graph`,
    drop free-floating values as follows:
    1. If *result* is a [map](https://infra.spec.whatwg.org/#ordered-map) which is empty,
       or contains only the [entries](https://infra.spec.whatwg.org/#map-entry) `@value` or `@list`,
       set *result* to `null`.
    2. Otherwise, if *result* is a [map](https://infra.spec.whatwg.org/#ordered-map) whose only [entry](https://infra.spec.whatwg.org/#map-entry) is `@id`, set *result* to `null`. When the `frameExpansion` flag is set, a [map](https://infra.spec.whatwg.org/#ordered-map) containing only the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) is retained.
20. Return *result*.

### 5.2 IRI Expansion

In JSON-LD documents, some keys and values may represent [IRIs](https://tools.ietf.org/html/rfc3987#section-2). This section defines an algorithm for
transforming a [string](https://infra.spec.whatwg.org/#javascript-string) that represents an [IRI](https://tools.ietf.org/html/rfc3987#section-2) into
an absolute [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
It also covers transforming keyword aliases into [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword).

[IRI](https://tools.ietf.org/html/rfc3987#section-2) expansion may occur during context processing or during
any of the other JSON-LD algorithms. If IRI expansion occurs during context
processing, then the [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) and its related *defined* map from the §4.1 Context Processing Algorithm are passed to this algorithm. This allows for [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) dependencies to be processed via the Create Term Definition algorithm (§4.2).

#### 5.2.1 Overview

*This section is non-normative.*

In order to expand *value* to an [IRI](https://tools.ietf.org/html/rfc3987#section-2), we must
first determine if it is `null`, a [term](https://www.w3.org/TR/json-ld11/#dfn-term), a keyword alias, or some form of [IRI](https://tools.ietf.org/html/rfc3987#section-2). Based on what
we find, we handle the specific kind of expansion; for example, we expand
a keyword alias to a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) and a [term](https://www.w3.org/TR/json-ld11/#dfn-term) to an [IRI](https://tools.ietf.org/html/rfc3987#section-2) according to its IRI mapping in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context). While inspecting *value* we
may also find that we need to create [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) dependencies because we're running this algorithm during context processing.
We can tell whether or not we're running during context processing by
checking [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) against `null`.
We know we need to create a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) when *value* is
an [entry](https://infra.spec.whatwg.org/#map-entry) in the [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) and the *defined* map
does not have an [entry](https://infra.spec.whatwg.org/#map-entry) for *value* with an associated value of `true`. The *defined* map is used during Context Processing (§4.1) to keep track of
which [terms](https://www.w3.org/TR/json-ld11/#dfn-term) have already been defined or are
in the process of being defined. We create a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) by using the Create Term Definition algorithm (§4.2).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Values that have the form of a keyword,
> but are not keywords (i.e., they begin with `"@"`) do not
> map to any value, as they are reserved for future use.
> The algorithm returns `null`, so that they will be ignored when encountered.

#### 5.2.2 Algorithm

The algorithm takes two required and four optional input variables. The
required inputs are an *active context* and a *value* to be expanded. The optional inputs are two flags, *document relative* and *vocab*, that specifying
whether *value* can be interpreted as a [relative IRI reference](https://tools.ietf.org/html/rfc3987#section-6.5) against the document's base [IRI](https://tools.ietf.org/html/rfc3987#section-2) or the [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping), respectively, and
a *local context* and a map *defined* to be used when
this algorithm is used during Context Processing (§4.1).
If not passed, the two flags are set to `false` and *local context* and *defined* are initialized to `null`.

1. If *value* is a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) or `null`,
   return *value* as is.
2. If *value* has the form of a keyword
   (i.e., it matches the ABNF rule `"@"1*ALPHA` from [RFC5234]),
   a processor *SHOULD* generate a warning and return `null`.
3. If *local context* is not `null`, it contains
   an [entry](https://infra.spec.whatwg.org/#map-entry) with a key that equals *value*, and the value of the [entry](https://infra.spec.whatwg.org/#map-entry) for *value* in *defined* is not `true`,
   invoke the Create Term Definition algorithm (§4.2),
   passing *active context*, *local context*, *value* as *term*, and *defined*. This will ensure that
   a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) is created for *value* in *active context* during Context Processing (§4.1).
4. If *active context* has a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *value*, and the associated IRI mapping is a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword),
   return that [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword).
5. If *vocab* is `true` and the *active context* has a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *value*, return the associated IRI mapping.
6. If *value* contains a colon (`:`) anywhere after the first character,
   it is either
   an [IRI](https://tools.ietf.org/html/rfc3987#section-2), a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri), or a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier):
   1. Split *value* into a *prefix* and *suffix* at the first occurrence of a colon (`:`).
   2. If *prefix* is underscore (`_`)
      or *suffix* begins with double-forward-slash
      (`//`), return *value* as it is already an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
   3. If *local context* is not `null`, it
      contains a *prefix* [entry](https://infra.spec.whatwg.org/#map-entry), and the value
      of the *prefix* [entry](https://infra.spec.whatwg.org/#map-entry) in *defined* is not `true`, invoke the Create Term Definition algorithm (§4.2),
      passing *active context*, *local context*, *prefix* as *term*,
      and *defined*. This will ensure that a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) is created for [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix) in *active context* during Context Processing (§4.1).
   4. If *active context* contains a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *prefix* having a non-`null` IRI mapping and the prefix flag of the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) is `true`,
      return the result of concatenating the IRI mapping associated with *prefix* and *suffix*.
   5. If *value* has the [form](https://tools.ietf.org/html/rfc3987#section-2.2) of an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
      return *value*.
7. If *vocab* is `true`, and *active context* has a [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping),
   return the result of concatenating the [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping) with *value*.
8. Otherwise, if *document relative* is `true` set *value* to the result of resolving *value* against
   the base IRI from *active context*. Only the basic algorithm in [section 5.2](https://tools.ietf.org/html/rfc3986#section-5.2) of [RFC3986] is used; neither [Syntax-Based Normalization](https://tools.ietf.org/html/rfc3986#section-6.2.2) nor [Scheme-Based Normalization](https://tools.ietf.org/html/rfc3986#section-6.2.3) are performed. Characters additionally allowed in IRI references are treated
   in the same way that unreserved characters are treated in URI references, per [section 6.5](https://tools.ietf.org/html/rfc3987#section-6.5) of [RFC3987].
9. Return *value* as is.

### 5.3 Value Expansion

Some values in JSON-LD can be expressed in a compact form. These values are required
to be expanded at times when processing
JSON-LD documents. A value is said to be in *expanded form* after the application of this algorithm.

#### 5.3.1 Overview

*This section is non-normative.*

If active property has a type mapping in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) set to `@id` or `@vocab`, and the value is a [string](https://infra.spec.whatwg.org/#javascript-string), a [map](https://infra.spec.whatwg.org/#ordered-map) with a single [entry](https://infra.spec.whatwg.org/#map-entry) `@id` whose
value is the result of using the IRI Expansion algorithm (§5.2) on *value* is returned.

Otherwise, the result will be a [map](https://infra.spec.whatwg.org/#ordered-map) containing
an `@value` [entry](https://infra.spec.whatwg.org/#map-entry) whose value is the passed *value*.
Additionally, an `@type` [entry](https://infra.spec.whatwg.org/#map-entry) will be included if there is a type mapping associated with the active property or an `@language` [entry](https://infra.spec.whatwg.org/#map-entry) if *value* is a [string](https://infra.spec.whatwg.org/#javascript-string) and there is language mapping associated
with the active property.

Note that values interpreted as [IRIs](https://tools.ietf.org/html/rfc3987#section-2) fall into two categories:
those that are *document relative*, and those that are *vocabulary relative*. [Properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) and values of `@type`,
along with terms marked as `"@type": "@vocab"` are *vocabulary relative*, meaning that they need to be either
a defined [term](https://www.w3.org/TR/json-ld11/#dfn-term), a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) where the [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix) is a [term](https://www.w3.org/TR/json-ld11/#dfn-term),
or a string which is turned into an [IRI](https://tools.ietf.org/html/rfc3987#section-2) using
the [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping).

#### 5.3.2 Algorithm

The algorithm takes three required inputs: an *active context*,
an *active property*, and a *value* to expand.

1. If the *active property* has a type mapping in *active context* that is `@id`, and the *value* is a [string](https://infra.spec.whatwg.org/#javascript-string), return a new [map](https://infra.spec.whatwg.org/#ordered-map) containing a single [entry](https://infra.spec.whatwg.org/#map-entry) where the
   key is `@id` and the value is the result IRI expanding *value* using `true` for *document relative* and `false` for *vocab*.
2. If *active property* has a type mapping in *active context* that is `@vocab`, and the *value* is a [string](https://infra.spec.whatwg.org/#javascript-string), return a new [map](https://infra.spec.whatwg.org/#ordered-map) containing a single [entry](https://infra.spec.whatwg.org/#map-entry) where the
   key is `@id` and the value is the result of IRI expanding *value* using `true` for *document relative*.
3. Otherwise, initialize *result* to a [map](https://infra.spec.whatwg.org/#ordered-map) with an `@value` [entry](https://infra.spec.whatwg.org/#map-entry) whose value is set to *value*.
4. If *active property* has a type mapping in *active context*, other than `@id`, `@vocab`, or `@none`, add `@type` to *result* and set its value to the value associated with the type mapping.
5. Otherwise, if *value* is a [string](https://infra.spec.whatwg.org/#javascript-string):
   1. Initialize *language* to the language mapping for *active property* in *active context*, if any, otherwise to the [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) of *active context*.
   2. Initialize *direction* to the direction mapping for *active property* in *active context*, if any, otherwise to the [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) of *active context*.
   3. If *language* is not `null`,
      add `@language` to *result* with the value *language*.
   4. If *direction* is not `null`,
      add `@direction` to *result* with the value *direction*.
6. Return *result*.

## 6. Compaction Algorithms

The following sections describe algorithms for compacting JSON-LD
documents, IRIs and values.

### 6.1 Compaction Algorithm

This algorithm compacts a JSON-LD document, such that the given [context](https://www.w3.org/TR/json-ld11/#dfn-context) is applied. This must result in shortening
any applicable [IRIs](https://tools.ietf.org/html/rfc3987#section-2) to [terms](https://www.w3.org/TR/json-ld11/#dfn-term) or [compact IRIs](https://www.w3.org/TR/json-ld11/#dfn-compact-iri), any applicable [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) to keyword aliases, and
any applicable [JSON-LD values](https://www.w3.org/TR/json-ld11/#dfn-json-ld-value) expressed in expanded form to simple values such as [strings](https://infra.spec.whatwg.org/#javascript-string) or [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value).

#### 6.1.1 Overview

*This section is non-normative.*

Starting with its root *element*, we can process the
JSON-LD document recursively, until we have a fully compacted *result*. When compacting an *element*, we can treat
each one differently according to its type, in order to break down the
problem:

1. If the *element* is a [scalar](https://infra.spec.whatwg.org/#primitive-data-types), it is
   already in compacted form, so we simply return it.
2. If the *element* is an [array](https://infra.spec.whatwg.org/#list), we compact
   each of its items recursively and return them in a new [array](https://infra.spec.whatwg.org/#list).
3. Otherwise *element* is a [map](https://infra.spec.whatwg.org/#ordered-map). The value
   of each [entry](https://infra.spec.whatwg.org/#map-entry) in element is compacted recursively. Some of the [entry](https://infra.spec.whatwg.org/#map-entry) keys will be
   compacted, using the IRI Compaction algorithm (§6.2),
   to [terms](https://www.w3.org/TR/json-ld11/#dfn-term) or [compact IRIs](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) and others will be compacted from [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) to keyword aliases or simply left
   unchanged because they do not have definitions in the [context](https://www.w3.org/TR/json-ld11/#dfn-context).
   Values will be converted to compacted form via the Value Compaction algorithm (§6.3). Some data
   will be reshaped based on container mapping specified in the context such as `@index` or `@language` maps.

#### 6.1.2 Algorithm

The algorithm takes three required and two optional input variables.
The required inputs are an *active context*,
an *active property*,
and an *element* to be compacted. The optional inputs are the `compactArrays` flag
and the `ordered` flag, used to order [map entry](https://infra.spec.whatwg.org/#map-entry) keys lexicographically, where noted.
If not passed, both flags are set to `false`.

1. Initialize *type-scoped context* to *active context*.
   This is used for compacting values that may be relevant to any previous [type-scoped context](https://www.w3.org/TR/json-ld11/#dfn-type-scoped-context).
2. If *element* is a [scalar](https://infra.spec.whatwg.org/#primitive-data-types), it is already in its most
   compact form, so simply return *element*.
3. If *element* is an [array](https://infra.spec.whatwg.org/#list):
   1. Initialize *result* to an empty [array](https://infra.spec.whatwg.org/#list).
   2. For each *item* in *element*:
      1. Initialize *compacted item* to the result of using this
         algorithm recursively, passing *active context*, *active property*, *item* for *element*, and the `compactArrays` and `ordered` flags.
      2. If *compacted item* is not `null`, then append
         it to *result*.
   3. If *result* is empty or contains more than one value,
      or `compactArrays` is `false`, or *active property* is either `@graph` or `@set`,
      or container mapping for *active property* in *active context* includes either `@list` or `@set`, return *result*.
   4. Otherwise, return the value in *result*.
4. Otherwise *element* is a [map](https://infra.spec.whatwg.org/#ordered-map).
5. If *active context* has a previous context,
   the *active context* is not propagated.
   If *element* does not contain an `@value` [entry](https://infra.spec.whatwg.org/#map-entry),
   and *element* does not consist of a single `@id` entry,
   set *active context* to previous context from *active context*,
   as the scope of a term-scoped [context](https://www.w3.org/TR/json-ld11/#dfn-context) does not apply when processing new [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object).
6. If the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *active property* in *active context* has a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context):
   1. Set *active context* to the result of the §4.1 Context Processing Algorithm,
      passing *active context*,
      the value of the *active property*'s [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) as *local context*, *base URL* from the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *active property* in *active context*,
      and `true` for *override protected*.
7. If *element* has an `@value` or `@id` [entry](https://infra.spec.whatwg.org/#map-entry) and the result of using the Value Compaction algorithm (§6.3),
   passing *active context*, *active property*, and *element* as *value* is
   a [scalar](https://infra.spec.whatwg.org/#primitive-data-types), or the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *active property* has a type mapping of `@json`, return that result.
8. If *element* is a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object), and the container mapping for *active property* in *active context* includes `@list`,
   return the result of using this algorithm recursively, passing *active context*, *active property*, value of `@list` in *element* for *element*, and the `compactArrays` and `ordered` flags.
9. Initialize *inside reverse* to `true` if *active property* equals `@reverse`,
   otherwise to `false`.
10. Initialize *result* to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
11. If *element* has an `@type` [entry](https://infra.spec.whatwg.org/#map-entry),
    create a new array *compacted types* initialized
    by transforming each *expanded type* of that [entry](https://infra.spec.whatwg.org/#map-entry) into its compacted form by IRI compacting *expanded type*.
    Then, for each *term* in *compacted types* ordered lexicographically:
    1. If the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *term* in *type-scoped context* has a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) set *active context* to the result of the §4.1 Context Processing Algorithm,
       passing *active context* and the value of *term*'s [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) in *type-scoped context* as *local context* *base URL* from the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *term* in *type-scoped context*,
       and `false` for *propagate*.
12. For each key *expanded property* and value *expanded value* in *element*, ordered lexicographically by *expanded property* if `ordered` is `true`:
    1. If *expanded property* is `@id`:
       1. If *expanded value* is a [string](https://infra.spec.whatwg.org/#javascript-string),
          then initialize *compacted value* by IRI compacting *expanded value* with *vocab* set to `false`.
       2. Initialize *alias* by IRI compacting *expanded property*.
       3. Add an [entry](https://infra.spec.whatwg.org/#map-entry) *alias* to *result* whose value is
          set to *compacted value* and continue to the next *expanded property*.
    2. If *expanded property* is `@type`:
       1. If *expanded value* is a [string](https://infra.spec.whatwg.org/#javascript-string),
          then initialize *compacted value* by IRI compacting *expanded value* using *type-scoped context* for *active context*.
       2. Otherwise, *expanded value* must be a `@type` [array](https://infra.spec.whatwg.org/#list):
          1. Initialize *compacted value* to an empty [array](https://infra.spec.whatwg.org/#list).
          2. For each item *expanded type* in *expanded value*:
             1. Set *term* by IRI compacting *expanded type* using *type-scoped context* for *active context*.
             2. Append *term*, to *compacted value*.
       3. Initialize *alias* by IRI compacting *expanded property*.
       4. Initialize *as array* to `true` if [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is `json-ld-1.1` and
          the container mapping for *alias* in the *active context* includes `@set`,
          otherwise to the negation of `compactArrays`.
       5. Use add value to add *compacted value* to the *alias* [entry](https://infra.spec.whatwg.org/#map-entry) in *result* using *as array*.
       6. Continue to the next *expanded property*.
    3. If *expanded property* is `@reverse`:
       1. Initialize *compacted value* to the result of using this
          algorithm recursively, passing *active context*, `@reverse` for *active property*, *expanded value* for *element*, and the `compactArrays` and `ordered` flags.
       2. For each *property* and *value* in *compacted value*:
          1. If the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *property* in the *active context* indicates that *property* is
             a reverse property
             1. Initialize *as array* to `true` if the container mapping for *property* in the *active context* includes `@set`,
                otherwise the negation of `compactArrays`.
             2. Use add value to add *value* to the *property* [entry](https://infra.spec.whatwg.org/#map-entry) in *result* using *as array*.
             3. Remove the *property* [entry](https://infra.spec.whatwg.org/#map-entry) from *compacted value*.
       3. If *compacted value* has some remaining [map entries](https://infra.spec.whatwg.org/#map-entry), i.e.,
          it is not an empty [map](https://infra.spec.whatwg.org/#ordered-map):
          1. Initialize *alias* by IRI compacting `@reverse`.
          2. Set the value of the *alias* [entry](https://infra.spec.whatwg.org/#map-entry) of *result* to *compacted value*.
       4. Continue with the next *expanded property* from *element*.
    4. If *expanded property* is `@preserve` then:
       1. Initialize *compacted value* to the result of using this
          algorithm recursively, passing *active context*, *active property*, *expanded value* for *element*, and the `compactArrays` and `ordered` flags.
       2. Add *compacted value* as the value of `@preserve` in *result* unless *expanded value* is an empty [array](https://infra.spec.whatwg.org/#list).
    5. If *expanded property* is `@index` and *active property* has a container mapping in *active context* that includes `@index`,
       then the compacted result will be inside of an `@index` container, drop the `@index` [entry](https://infra.spec.whatwg.org/#map-entry) by continuing
       to the next *expanded property*.
    6. Otherwise, if *expanded property* is `@direction`, `@index`, `@language`,
       or `@value`:
       1. Initialize *alias* by IRI compacting *expanded property*.
       2. Add an [entry](https://infra.spec.whatwg.org/#map-entry) *alias* to *result* whose value is
          set to *expanded value* and continue with the next *expanded property*.
    7. If *expanded value* is an empty [array](https://infra.spec.whatwg.org/#list):
       1. Initialize *item active property* by IRI compacting *expanded property* using *expanded value* for *value* and *inside reverse* for *reverse*.
       2. If the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *item active property* in the *active context* has a nest value [entry](https://infra.spec.whatwg.org/#map-entry) (*nest term*):
          1. If *nest term* is not `@nest`,
             or a [term](https://www.w3.org/TR/json-ld11/#dfn-term) in the *active context* that expands to `@nest`,
             an `invalid @nest value` error has been detected, and processing is aborted.
          2. If *result* does not have a *nest term* [entry](https://infra.spec.whatwg.org/#map-entry),
             initialize it to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
          3. Initialize *nest result* to the value of *nest term* in *result*.
       3. Otherwise, initialize *nest result* to *result*.
       4. Use add value to add an empty [array](https://infra.spec.whatwg.org/#list) to the *item active property* [entry](https://infra.spec.whatwg.org/#map-entry) in *nest result* using `true` for *as array*.
    8. At this point, *expanded value* must be an [array](https://infra.spec.whatwg.org/#list) due to the §5.1 Expansion Algorithm.
       For each item *expanded item* in *expanded value*:
       1. Initialize *item active property* by IRI compacting *expanded property* using *expanded item* for *value* and *inside reverse* for *reverse*.
       2. If the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) for *item active property* in the *active context* has a nest value [entry](https://infra.spec.whatwg.org/#map-entry) (*nest term*):
          1. If *nest term* is not `@nest`,
             or a [term](https://www.w3.org/TR/json-ld11/#dfn-term) in the *active context* that expands to `@nest`,
             an `invalid @nest value` error has been detected, and processing is aborted.
          2. If *result* does not have a *nest term* [entry](https://infra.spec.whatwg.org/#map-entry),
             initialize it to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
          3. Initialize *nest result* to the value of *nest term* in *result*.
       3. Otherwise, initialize *nest result* to *result*.
       4. Initialize *container* to container mapping for *item active property* in *active context*,
          or to a new empty [array](https://infra.spec.whatwg.org/#list), if there is no such container mapping.
       5. Initialize *as array* to `true` if *container* includes `@set`,
          or if *item active property* is `@graph` or `@list`,
          otherwise the negation of `compactArrays`.
       6. Initialize *compacted item* to the result of using
          this algorithm recursively, passing *active context*, *item active property* for *active property*, *expanded item* for *element*, along with the `compactArrays` and `ordered` flags.
          If *expanded item* is a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object) or a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object),
          use the value of the `@list` or `@graph` entries,
          respectively, for *element* instead of *expanded item*.
       7. If *expanded item* is a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object):
          1. If *compacted item* is not an [array](https://infra.spec.whatwg.org/#list),
             then set *compacted item* to an [array](https://infra.spec.whatwg.org/#list) containing only *compacted item*.
          2. If *container* does not include `@list`:
             1. Convert *compacted item* to a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object) by setting it to a [map](https://infra.spec.whatwg.org/#ordered-map) containing an [entry](https://infra.spec.whatwg.org/#map-entry) where the key is the result of IRI compacting `@list` and the value is the original *compacted item*.
             2. If *expanded item* contains the [entry](https://infra.spec.whatwg.org/#map-entry) `@index`-*value*, then add an [entry](https://infra.spec.whatwg.org/#map-entry) to *compacted item* where the key is the
                result of IRI compacting `@index` and value is *value*.
             3. Use add value to add *compacted item* to the *item active property* [entry](https://infra.spec.whatwg.org/#map-entry) in *nest result* using *as array*.
          3. Otherwise, set the value of the *item active property* entry
             in *nest result* to *compacted item*.
       8. If *expanded item* is a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object):
          1. If *container* includes `@graph` and `@id`:
             1. Initialize *map object* to the value of *item active property* in *nest result*,
                initializing it to a new empty [map](https://infra.spec.whatwg.org/#ordered-map), if necessary.
             2. Initialize *map key* by IRI compacting the value of `@id` in *expanded item* or `@none` if no such value exists
                with *vocab* set to `false` if there is an `@id` [entry](https://infra.spec.whatwg.org/#map-entry) in *expanded item*.
             3. Use add value to add *compacted item* to the *map key* entry in *map object* using *as array*.
          2. Otherwise, if *container* includes `@graph` and `@index` and *expanded item* is a [simple graph object](https://www.w3.org/TR/json-ld11/#dfn-simple-graph-object):
             1. Initialize *map object* to the value of *item active property* in *nest result*,
                initializing it to a new empty [map](https://infra.spec.whatwg.org/#ordered-map), if necessary.
             2. Initialize *map key* the value of `@index` in *expanded item* or `@none`, if no such
                value exists.
             3. Use add value to add *compacted item* to the *map key* entry in *map object* using *as array*.
          3. Otherwise, if *container* includes `@graph` and *expanded item* is a [simple graph object](https://www.w3.org/TR/json-ld11/#dfn-simple-graph-object) the value cannot be represented as a map object.
             1. If *compacted item* is an [array](https://infra.spec.whatwg.org/#list) with more than one value, it cannot be directly represented,
                as multiple objects would be interpreted as different named graphs.
                Set *compacted item* to a new [map](https://infra.spec.whatwg.org/#ordered-map),
                containing the key
                from IRI compacting `@included` and the original *compacted item* as the value.
             2. Use add value to add *compacted item* to the *item active property* entry in *nest result* using *as array*.
          4. Otherwise, *container* does not include `@graph` or otherwise does not match one of the previous cases.
             1. Set *compacted item* to a new map containing
                the key
                from IRI compacting `@graph` using the original *compacted item* as a value.
             2. If expanded item contains an `@id` [entry](https://infra.spec.whatwg.org/#map-entry),
                add an entry in *compacted item* using the key
                from IRI compacting `@id` using the value
                of IRI compacting the value of `@id` in *expanded item* using `false` for *vocab*.
             3. If expanded item contains an `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
                add an entry in *compacted item* using the key
                from IRI compacting `@index` and the value of `@index` in *expanded item*.
             4. Use add value to add *compacted item* to the *item active property* entry in *nest result* using *as array*.
       9. Otherwise, if *container* includes `@language`, `@index`, `@id`,
          or `@type` and *container* does not include `@graph`:
          1. Initialize *map object* to the value of *item active property* in *nest result*,
             initializing it to a new empty [map](https://infra.spec.whatwg.org/#ordered-map), if necessary.
          2. Initialize *container key* by IRI compacting either `@language`, `@index`, `@id`, or `@type` based on the contents of *container*.
          3. Initialize *index key* to the value of index mapping in
             the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) associated with *item active property* in *active context*,
             or `@index`, if no such value exists.
          4. If *container* includes `@language` and *expanded item* contains a `@value` [entry](https://infra.spec.whatwg.org/#map-entry), then set *compacted item* to the value associated with its `@value` [entry](https://infra.spec.whatwg.org/#map-entry).
             Set *map key* to the value of `@language` in *expanded item*, if any.
          5. Otherwise, if *container* includes `@index` and *index key* is `@index`,
             set *map key* to the value of `@index` in *expanded item*, if any.
          6. Otherwise, if *container* includes `@index` and *index key* is not `@index`:
             1. Reinitialize *container key* by IRI compacting *index key*.
             2. Set *map key* to the first value of *container key* in *compacted item*, if any.
             3. If there are remaining values in *compacted item* for *container key*, use add value to
                add those remaining values to the *container key* in *compacted item*.
                Otherwise, remove that [entry](https://infra.spec.whatwg.org/#map-entry) from *compacted item*.
          7. Otherwise, if *container* includes `@id`, set *map key* to the value of *container key* in *compacted item* and remove *container key* from *compacted item*.
          8. Otherwise, if *container* includes `@type`:
             1. Set *map key* to the first value of *container key* in *compacted item*, if any.
             2. If there are remaining values in *compacted item* for *container key*, use add value to
                add those remaining values to the *container key* in *compacted item*.
             3. Otherwise, remove that [entry](https://infra.spec.whatwg.org/#map-entry) from *compacted item*.
             4. If *compacted item* contains a single [entry](https://infra.spec.whatwg.org/#map-entry) with a key expanding
                to `@id`, set *compacted item* to the result of using
                this algorithm recursively, passing *active context*, *item active property* for *active property*,
                and a [map](https://infra.spec.whatwg.org/#ordered-map) composed of the single [entry](https://infra.spec.whatwg.org/#map-entry) for `@id` from *expanded item* for *element*.
          9. If *map key* is `null`,
             set it to the result of IRI compacting `@none`.
          10. Use add value to add *compacted item* to the *map key* entry in *map object* using *as array*.
       10. Otherwise, use add value to add *compacted item* to the *item active property* entry in *nest result* using *as array*.
13. Return *result*.

### 6.2 IRI Compaction

This algorithm compacts an [IRI](https://tools.ietf.org/html/rfc3987#section-2) to a [term](https://www.w3.org/TR/json-ld11/#dfn-term) or [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri), or a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) to a keyword alias. A value that is associated with the [IRI](https://tools.ietf.org/html/rfc3987#section-2) may be passed in order to assist in selecting the most
context-appropriate [term](https://www.w3.org/TR/json-ld11/#dfn-term).

#### 6.2.1 Overview

*This section is non-normative.*

If the passed [IRI](https://tools.ietf.org/html/rfc3987#section-2) is `null`,
we simply return `null`.
Otherwise, we first try to find a [term](https://www.w3.org/TR/json-ld11/#dfn-term) that the [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) can be compacted to if it is relative to [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping).
In order to select the most appropriate [term](https://www.w3.org/TR/json-ld11/#dfn-term),
we may have to collect information about the passed *value*.
This information includes determining the preferred container mapping, type mapping or language mapping for expressing the *value*.
For [JSON-LD lists](https://www.w3.org/TR/json-ld11/#dfn-list-object), the type mapping or language mapping will be chosen based on the most
specific values that work for all items in the list.
Once this information is gathered,
it is passed to the Term Selection algorithm (§4.4),
which will return the most appropriate [term](https://www.w3.org/TR/json-ld11/#dfn-term).

If no [term](https://www.w3.org/TR/json-ld11/#dfn-term) was found that could be used to compact the [IRI](https://tools.ietf.org/html/rfc3987#section-2),
an attempt is made to compact the [IRI](https://tools.ietf.org/html/rfc3987#section-2) using the [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping),
if there is one.
If the [IRI](https://tools.ietf.org/html/rfc3987#section-2) could not be compacted,
an attempt is made to find a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri). A term will be used to create a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) only if the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) contains the prefix flag with the value `true`. If there is no appropriate [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri), and the `compactToRelative` option is `true`,
the [IRI](https://tools.ietf.org/html/rfc3987#section-2) is transformed to a [relative IRI reference](https://tools.ietf.org/html/rfc3987#section-6.5) using the document's [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri).
Finally, if the [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) still could not be compacted,
it is returned as is.

When considering language mapping,
the direction mapping is also considered, either with, or without,
a language mapping,
and the language mapping is normalized to lower case.

In the case were this algorithm would return the input [IRI](https://tools.ietf.org/html/rfc3987#section-2) as is,
and that [IRI](https://tools.ietf.org/html/rfc3987#section-2) can be mistaken for a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context),
this algorithm will raise an error,
because it has no way to return an unambiguous representation of the original [IRI](https://tools.ietf.org/html/rfc3987#section-2).

#### 6.2.2 Algorithm

This algorithm takes two required inputs and three optional inputs.
The required inputs are an *active context*,
and the *var* to be compacted.
The optional inputs are a *value* associated with the *var*,
a *vocab* flag which specifies whether the passed *var* should be compacted using the [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping),
and a *reverse* flag which specifies whether a reverse property is being compacted.
If not passed, *value* is set to `null` and both *vocab* and *reverse* are both set to `false`.

1. If *var* is `null`, return `null`.

2. If the *active context* has a `null` inverse context,
   set inverse context in *active context* to the result of calling the Inverse Context Creation algorithm (§4.3) using *active context*.

3. Initialize *inverse context* to the value of inverse context in *active context*.

4. If *vocab* is `true` and *var* is an [entry](https://infra.spec.whatwg.org/#map-entry) of *inverse context*:

   1. Initialize *default language* based on the [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language), normalized to lower case and [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction):

      1. If the [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) is not `null`, to the concatenation of
         the [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) and [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction), separated by an underscore (`"_"`),
         normalized to lower case.
      2. Otherwise, to the [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language),
         if it has one,
         normalized to lower case,
         otherwise to `@none`.

   2. If *value* is a [map](https://infra.spec.whatwg.org/#ordered-map) containing an `@preserve` [entry](https://infra.spec.whatwg.org/#map-entry),
      use the first element from the value of `@preserve` as *value*.

   3. Initialize *containers* to an empty [array](https://infra.spec.whatwg.org/#list). This [array](https://infra.spec.whatwg.org/#list) will be used to keep track of an ordered list of
      preferred container mapping for a [term](https://www.w3.org/TR/json-ld11/#dfn-term),
      based on what is compatible with *value*.
      > **Note:**
      >
      > > **Note:**
      > >
      > > Note
      >
      > Algorithm steps may append the same value to *containers*,
      > but the order in which they are added is significant for choosing the most appropriate term.

   4. Initialize *type/language* to `@language`,
      and *type/language value* to `@null`. These two
      variables will keep track of the preferred type mapping or language mapping for
      a [term](https://www.w3.org/TR/json-ld11/#dfn-term), based on what is compatible with *value*.

   5. If *value* is a [map](https://infra.spec.whatwg.org/#ordered-map) containing an `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
      and *value* is not a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object) then append the values `@index` and `@index@set` to *containers*.

   6. If *reverse* is `true`, set *type/language* to `@type`, *type/language value* to `@reverse`, and append `@set` to *containers*.

   7. Otherwise, if *value* is a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object), then set *type/language* and *type/language value* to the most specific values that work for all items in
      the list as follows:

      1. If `@index` is not an [entry](https://infra.spec.whatwg.org/#map-entry) in *value*, then
         append `@list` to *containers*.
      2. Initialize *list* to the [array](https://infra.spec.whatwg.org/#list) associated
         with the `@list` [entry](https://infra.spec.whatwg.org/#map-entry) in *value*.
      3. Initialize *common type* and *common language* to `null`. If *list* is empty, set *common language* to *default language*.
      4. For each *item* in *list*:
         1. Initialize *item language* to `@none` and *item type* to `@none`.
         2. If *item* contains an `@value` [entry](https://infra.spec.whatwg.org/#map-entry):
            1. If *item* contains an `@direction` [entry](https://infra.spec.whatwg.org/#map-entry),
               then set *item language* to the concatenation of
               the *item*'s `@language` entry (if any)
               the *item*'s `@direction`, separated by an underscore (`"_"`),
               normalized to lower case.
            2. Otherwise, if *item* contains an `@language` [entry](https://infra.spec.whatwg.org/#map-entry),
               then set *item language* to its associated value,
               normalized to lower case.
            3. Otherwise, if *item* contains a `@type` [entry](https://infra.spec.whatwg.org/#map-entry), set *item type* to its
               associated value.
            4. Otherwise, set *item language* to `@null`.
         3. Otherwise, set *item type* to `@id`.
         4. If *common language* is `null`,
            set *common language* to *item language*.
         5. Otherwise, if *item language* does not equal *common language* and *item* contains a `@value` [entry](https://infra.spec.whatwg.org/#map-entry), then set *common language* to `@none` because list items have conflicting
            languages.
         6. If *common type* is `null`,
            set *common type* to *item type*.
         7. Otherwise, if *item type* does not equal *common type*, then set *common type* to `@none` because list items have conflicting
            types.
         8. If *common language* is `@none` and *common type* is `@none`, then
            stop processing items in the list because it has been
            detected that there is no common language or type amongst
            the items.
      5. If *common language* is `null`,
         set *common language* to `@none`.
      6. If *common type* is `null`,
         set *common type* to `@none`.
      7. If *common type* is not `@none` then set *type/language* to `@type` and *type/language value* to *common type*.
      8. Otherwise, set *type/language value* to *common language*.

   8. Otherwise, if *value* is a [graph object](https://www.w3.org/TR/json-ld11/#dfn-graph-object),
      prefer a mapping most appropriate for the particular value.

      1. If *value* contains an `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
         append the values `@graph@index` and `@graph@index@set` to *containers*.
      2. If *value* contains an `@id` [entry](https://infra.spec.whatwg.org/#map-entry),
         append the values `@graph@id` and `@graph@id@set` to *containers*.
      3. Append the values `@graph` `@graph@set`,
         and `@set` to *containers*.
      4. If *value* does not contain an `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
         append the values `@graph@index` and `@graph@index@set` to *containers*.
      5. If the *value* does not contain an `@id` [entry](https://infra.spec.whatwg.org/#map-entry),
         append the values `@graph@id` and `@graph@id@set` to *containers*.
      6. Append the values `@index` and `@index@set` to *containers*.
      7. Set *type/language* to `@type` and set *type/language value* to `@id`.

   9. Otherwise:

      1. If *value* is a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object):
         1. If *value* contains an `@direction` [entry](https://infra.spec.whatwg.org/#map-entry) and does not contain an `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
            then set *type/language value* to the concatenation of
            the *value*'s `@language` [entry](https://infra.spec.whatwg.org/#map-entry) (if any)
            and the *value*'s `@direction` [entry](https://infra.spec.whatwg.org/#map-entry), separated by an underscore (`"_"`),
            normalized to lower case.
            Append `@language` and `@language@set` to *containers*.
         2. Otherwise, if *value* contains an `@language` [entry](https://infra.spec.whatwg.org/#map-entry) and does not contain an `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
            then set *type/language value* to
            the value of `@language` normalized to lower case,
            and append `@language`, and `@language@set` to *containers*.
         3. Otherwise, if *value* contains an `@type` [entry](https://infra.spec.whatwg.org/#map-entry), then set *type/language value* to
            its associated value and set *type/language* to `@type`.
      2. Otherwise, set *type/language* to `@type` and set *type/language value* to `@id`, and append `@id`, `@id@set`, `@type`, and `@set@type`,
         to *containers*.
      3. Append `@set` to *containers*.

   10. Append `@none` to *containers*. This represents
       the non-existence of a container mapping, and it will
       be the last container mapping value to be checked as it
       is the most generic.

   11. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is not `json-ld-1.0` and *value* is not a [map](https://infra.spec.whatwg.org/#ordered-map) or does not contain an `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
       append `@index` and `@index@set` to *containers*.

   12. If [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is not `json-ld-1.0` and *value* is a [map](https://infra.spec.whatwg.org/#ordered-map) containing only an `@value` [entry](https://infra.spec.whatwg.org/#map-entry),
       append `@language` and `@language@set` to *containers*.

   13. If *type/language value* is `null`,
       set *type/language value* to `@null`.
       This is the key under which `null` values
       are stored in the *inverse context* *entry*.

   14. Initialize *preferred values* to an empty [array](https://infra.spec.whatwg.org/#list).
       This [array](https://infra.spec.whatwg.org/#list) will indicate, in order, the preferred values for
       a [term's](https://www.w3.org/TR/json-ld11/#dfn-term) type mapping or language mapping.

   15. If *type/language value* is `@reverse`, append `@reverse` to *preferred values*.

   16. If *type/language value* is `@id` or `@reverse` and *value* is a [map](https://infra.spec.whatwg.org/#ordered-map) containing an `@id` [entry](https://infra.spec.whatwg.org/#map-entry):

       1. If the result of IRI compacting the value of the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) in *value* has a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in the *active context* with an IRI mapping that equals the value of the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) in *value*,
          then append `@vocab`, `@id`, and `@none`, in that order, to *preferred values*.
       2. Otherwise, append `@id`, `@vocab`, and `@none`, in that order, to *preferred values*.

   17. Otherwise, append *type/language value* and `@none`, in
       that order, to *preferred values*. If *value* is a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object) with an empty *array* as the value of `@list`,
       set *type/language* to `@any`.

   18. Append `@any` to *preferred values*.

   19. If *preferred values* contains any entry having an underscore (`"_"`),
       append the substring of that entry from the underscore to the end of the string
       to *preferred values*.

   20. Initialize *term* to the result of the Term Selection algorithm (§4.4), passing *var*, *containers*, *type/language*, and *preferred values*.

   21. If *term* is not `null`, return *term*.

5. At this point, there is no simple [term](https://www.w3.org/TR/json-ld11/#dfn-term) that *var* can be compacted to. If *vocab* is `true` and *active context* has a [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping):

   1. If *var* begins with the [vocabulary mapping's](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping) value
      but is longer, then initialize *suffix* to the substring
      of *var* that does not match. If *suffix* does not
      have a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in *active context*,
      then return *suffix*.

6. The *var* could not be compacted using the [active context's](https://www.w3.org/TR/json-ld11/#dfn-active-context) [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping).
   Try to create a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri), starting by initializing *compact IRI* to `null`. This variable will be used to
   store the created [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri), if any.

7. For each [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) *definition* in *active context*:

   1. If the IRI mapping of *definition* is `null`,
      its IRI mapping equals *var*,
      its IRI mapping is not a substring at the beginning of *var*, or *definition* does not have
      a `true` prefix flag, *definition*'s key cannot be used as a [prefix](https://www.w3.org/TR/json-ld11/#dfn-prefix).
      Continue with the next *definition*.
   2. Initialize *candidate* by concatenating *definition* key,
      a colon (`:`), and the substring of *var* that follows after the value of the *definition*'s IRI mapping.
   3. If either *compact IRI* is `null`, *candidate* is
      shorter or the same length but lexicographically less than *compact IRI* and *candidate* does not have a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in *active context*, or if that [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) has an IRI mapping that equals *var* and *value* is `null`,
      set *compact IRI* to *candidate*.

8. If *compact IRI* is not `null`, return *compact IRI*.

9. To ensure that the [IRI](https://tools.ietf.org/html/rfc3987#section-2) *var* is
   not confused with a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri),
   if the [IRI scheme](https://tools.ietf.org/html/rfc3986#section-3.1) of *var* matches any term in [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) with prefix flag set to `true`,
   and *var* has no [IRI authority](https://tools.ietf.org/html/rfc3986#section-3.2) (preceded by double-forward-slash (`//`),
   an `IRI confused with prefix` error has been detected,
   and processing is aborted.

10. If *vocab* is `false`,
    transform *var* to a [relative IRI reference](https://tools.ietf.org/html/rfc3987#section-6.5) using
    the base IRI from *active context*, if it exists.

11. Finally, return *var* as is.

### 6.3 Value Compaction

Expansion transforms all values into expanded form in JSON-LD. This algorithm performs the opposite operation, transforming
a value into *compacted form*. This algorithm compacts a
value according to the [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) in the given [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) that is associated with the value's associated active property.

#### 6.3.1 Overview

*This section is non-normative.*

The *value* to compact has either an `@id` or an `@value` [entry](https://infra.spec.whatwg.org/#map-entry).

For the former case, if the type mapping of active property is set to `@id` or `@vocab` and *value* consists of only an `@id` [entry](https://infra.spec.whatwg.org/#map-entry) and, if
the container mapping of active property includes `@index`, an `@index` [entry](https://infra.spec.whatwg.org/#map-entry), *value* can be compacted to a [string](https://infra.spec.whatwg.org/#javascript-string) by returning the result of
using the IRI Compaction algorithm (§6.2) to compact the value associated with the `@id` [entry](https://infra.spec.whatwg.org/#map-entry).
Otherwise, *value* cannot be compacted and is returned as is.

For the latter case, it might be possible to compact *value* just into the value associated with the `@value` [entry](https://infra.spec.whatwg.org/#map-entry).
This can be done if the active property has a matching type mapping or language mapping and there
is either no `@index` [entry](https://infra.spec.whatwg.org/#map-entry) or the container mapping of active property includes `@index`. It can
also be done if `@value` is the only [entry](https://infra.spec.whatwg.org/#map-entry) in *value* (apart an `@index` [entry](https://infra.spec.whatwg.org/#map-entry) in case the container mapping of active property includes `@index`) and
either its associated value is not a [string](https://infra.spec.whatwg.org/#javascript-string), there is
no [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language), or there is an explicit `null` language mapping for the active property.

#### 6.3.2 Algorithm

This algorithm has three required inputs: an *active context*,
an *active property*, and a *value* to be compacted.

1. Initialize *result* to a copy of *value*.
2. If the *active context* has a `null` inverse context,
   set inverse context in *active context* to the result of calling the Inverse Context Creation algorithm (§4.3) using *active context*.
3. Initialize *inverse context* to the value of inverse context in *active context*.
4. Initialize *language* to the language mapping for *active property* in *active context*, if any, otherwise to the [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) of *active context*.
5. Initialize *direction* to the direction mapping for *active property* in *active context*, if any, otherwise to the [default base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) of *active context*.
6. If *value* has an `@id` [entry](https://infra.spec.whatwg.org/#map-entry) and has no other [entries](https://infra.spec.whatwg.org/#map-entry) other than `@index`:
   1. If the type mapping of *active property* is set to `@id`, set *result* to the result of IRI compacting the value associated with the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) using `false` for *vocab*.
   2. Otherwise, if the type mapping of *active property* is set to `@vocab`, set *result* to the result of IRI compacting the value associated with the `@id` [entry](https://infra.spec.whatwg.org/#map-entry).
7. Otherwise, if *value* has an `@type` [entry](https://infra.spec.whatwg.org/#map-entry) whose
   value matches the type mapping of *active property*,
   set *result* to the value associated with the `@value` [entry](https://infra.spec.whatwg.org/#map-entry) of *value*.
8. Otherwise, if the type mapping of *active property* is `@none`,
   or *value* has an `@type` [entry](https://infra.spec.whatwg.org/#map-entry),
   and the value of `@type` in *value* does not match the type mapping of *active property*,
   leave *value* as is, as value compaction is disabled.
   1. Replace any value of `@type` in *result* with the result of IRI compacting the value of the `@type` [entry](https://infra.spec.whatwg.org/#map-entry).
9. Otherwise, if the value of the `@value` [entry](https://infra.spec.whatwg.org/#map-entry) is not a [string](https://infra.spec.whatwg.org/#javascript-string):
   1. If *value* has an `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
      and the container mapping associated to *active property* includes `@index`,
      or if *value* has no `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
      set *result* to the value associated with the `@value` [entry](https://infra.spec.whatwg.org/#map-entry).
10. Otherwise, if *value* has an `@language` [entry](https://infra.spec.whatwg.org/#map-entry) whose value exactly matches *language*, using a case-insensitive comparison if it is not `null`, or is not present, if *language* is `null`, and the *value* has an `@direction` [entry](https://infra.spec.whatwg.org/#map-entry) whose value exactly matches *direction*,
    if it is not `null`, or is not present, if *direction* is `null`:
    1. If *value* has an `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
       and the container mapping associated to *active property* includes `@index`,
       or *value* has no `@index` [entry](https://infra.spec.whatwg.org/#map-entry),
       set *result* to the value associated with the `@value` [entry](https://infra.spec.whatwg.org/#map-entry).
11. If *result* is a *map*,
    replace each key in *result* with the result of IRI compacting that key.
12. Return *result*.

## 7. Flattening Algorithms

The following sections describe algorithms for flattening JSON-LD documents,
creating node maps, and generating blank nodes.

### 7.1 Flattening Algorithm

This algorithm flattens an expanded JSON-LD document by collecting all [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in a single [map](https://infra.spec.whatwg.org/#ordered-map) and labeling all [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) with [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
This resulting uniform shape of the document, may drastically simplify
the code required to process JSON-LD data in certain applications.

#### 7.1.1 Overview

*This section is non-normative.*

First, a *node map* is generated using the Node Map Generation algorithm (§7.2) which collects all [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in a single [map](https://infra.spec.whatwg.org/#ordered-map). In the next step, the *node map* is
converted to a JSON-LD document in [flattened document form](https://www.w3.org/TR/json-ld11/#flattened-document-form).

#### 7.1.2 Algorithm

The algorithm takes one required and one optional input variables.
The required input is an *element* to flatten. The optional input is
the `ordered` flag, used to order [map entry](https://infra.spec.whatwg.org/#map-entry) keys lexicographically, where noted.
If not passed, the `ordered` flag is set to `false`.

This algorithm uses the Generate Blank Node Identifier algorithm (§7.4) to generate new [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) and relabel existing [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
The Generate Blank Node Identifier algorithm (§7.4) maintains an *identifier map* to ensure that blank node identifiers in the source
document are consistently remapped to new blank node identifiers
avoiding collisions. Thus, before this algorithm is run, the *identifier map* is reset.

1. Initialize *node map* to a [map](https://infra.spec.whatwg.org/#ordered-map) consisting of
   a single [entry](https://infra.spec.whatwg.org/#map-entry) whose key is `@default` and whose value is
   an empty [map](https://infra.spec.whatwg.org/#ordered-map).
2. Perform the Node Map Generation algorithm (§7.2), passing *element* and *node map*.
3. Initialize *default graph* to the value of the `@default` [entry](https://infra.spec.whatwg.org/#map-entry) of *node map*, which is a [map](https://infra.spec.whatwg.org/#ordered-map) representing
   the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph).
4. For each key-value pair *graph name*-*graph* in *node map* where *graph name* is not `@default`, ordered lexicographically by *graph name* if `ordered` is `true`,
   perform the following steps:
   1. If *default graph* does not have a *graph name* [entry](https://infra.spec.whatwg.org/#map-entry), create
      one and initialize its value to a [map](https://infra.spec.whatwg.org/#ordered-map) consisting of an `@id` [entry](https://infra.spec.whatwg.org/#map-entry) whose value is set to *graph name*.
   2. Reference the value associated with the *graph name* [entry](https://infra.spec.whatwg.org/#map-entry) in *default graph* using the variable *entry*.
   3. Add an `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) to *entry* and set it to an
      empty [array](https://infra.spec.whatwg.org/#list).
   4. For each *id*-*node* pair in *graph* ordered lexicographically by *id* if `ordered` is `true`,
      add *node* to the `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) of *entry*,
      unless the only [entry](https://infra.spec.whatwg.org/#map-entry) of *node* is `@id`.
5. Initialize an empty [array](https://infra.spec.whatwg.org/#list) *flattened*.
6. For each *id*-*node* pair in *default graph* ordered lexicographically by *id* if `ordered` is `true`,
   add *node* to *flattened*,
   unless the only [entry](https://infra.spec.whatwg.org/#map-entry) of *node* is `@id`.
7. Return *flattened*.

### 7.2 Node Map Generation

This algorithm creates a [map](https://infra.spec.whatwg.org/#ordered-map) *node map* holding an indexed
representation of the [graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) and [nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-node) represented in the passed expanded document. All [nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-node) that are not
uniquely identified by an IRI get assigned a (new) [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
The resulting *node map* will have an [map entry](https://infra.spec.whatwg.org/#map-entry) for every graph in the document whose
value is another object with an [entry](https://infra.spec.whatwg.org/#map-entry) for every [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) represented in the document.
The default graph is stored under the `@default` [entry](https://infra.spec.whatwg.org/#map-entry), all other graphs are
stored under their [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name).

#### 7.2.1 Overview

*This section is non-normative.*

The algorithm recursively runs over an expanded JSON-LD document to
collect all [entries](https://infra.spec.whatwg.org/#map-entry) of a [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in a single [map](https://infra.spec.whatwg.org/#ordered-map). The algorithm updates a [map](https://infra.spec.whatwg.org/#ordered-map) *node map* whose keys represent the [graph names](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name) used in the document
(the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) is stored under the `@default` [entry](https://infra.spec.whatwg.org/#map-entry))
and whose associated values are [maps](https://infra.spec.whatwg.org/#ordered-map) which index the [nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-node) in the [graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph). If a [entry's](https://infra.spec.whatwg.org/#map-entry) value is a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object),
it is replaced by a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) consisting of only an `@id` [entry](https://infra.spec.whatwg.org/#map-entry). If a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) has no `@id` [entry](https://infra.spec.whatwg.org/#map-entry) or it is identified by a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier),
a new [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) is generated. This relabeling
of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) is
also done for [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) and values of `@type`.

#### 7.2.2 Algorithm

The algorithm takes as input an expanded JSON-LD document *element* and a reference to
a [map](https://infra.spec.whatwg.org/#ordered-map) *node map*. Furthermore it has the optional parameters *active graph* (which defaults to `@default`), an *active subject*, *active property*, and a reference to a [map](https://infra.spec.whatwg.org/#ordered-map) *list*. If
not passed, *active subject*, *active property*, and *list* are
set to `null`.

1. If *element* is an array, process each *item* in *element* as follows and then return:
   1. Run this algorithm recursively by passing *item* for *element*, *node map*, *active graph*, *active subject*, *active property*, and *list*.
2. Otherwise *element* is a [map](https://infra.spec.whatwg.org/#ordered-map). Reference the [map](https://infra.spec.whatwg.org/#ordered-map) which is the value of the active graph [entry](https://infra.spec.whatwg.org/#map-entry) of *node map* using the variable *graph*. If the *active subject* is `null`, set *node* to `null` otherwise reference the *active subject* [entry](https://infra.spec.whatwg.org/#map-entry) of *graph* using the
   variable *subject node*.
3. For each *item* in the `@type` [entry](https://infra.spec.whatwg.org/#map-entry) of *element*,
   if any, or for the value of `@type`, if the value of `@type` exists and is not an [array](https://infra.spec.whatwg.org/#list):
   1. If *item* is a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), replace it with a newly generated blank node identifier (§7.4) passing *item* for *identifier*.
4. If *element* has an `@value` [entry](https://infra.spec.whatwg.org/#map-entry), perform the following steps:
   1. If *list* is `null`:
      1. If *subject node* does not have an *active property* [entry](https://infra.spec.whatwg.org/#map-entry),
         create one and initialize its value to an [array](https://infra.spec.whatwg.org/#list) containing *element*.
      2. Otherwise, compare *element* against every item in the [array](https://infra.spec.whatwg.org/#list) associated with the *active property* [entry](https://infra.spec.whatwg.org/#map-entry) of *subject node*. If there is no item equivalent to *element*,
         append *element* to the [array](https://infra.spec.whatwg.org/#list). Two [maps](https://infra.spec.whatwg.org/#ordered-map) are considered
         equal if they have equivalent [map entries](https://infra.spec.whatwg.org/#map-entry).
   2. Otherwise, append *element* to the `@list` [entry](https://infra.spec.whatwg.org/#map-entry) of *list*.
5. Otherwise, if *element* has an `@list` [entry](https://infra.spec.whatwg.org/#map-entry), perform
   the following steps:
   1. Initialize a new [map](https://infra.spec.whatwg.org/#ordered-map) *result* consisting of a single [entry](https://infra.spec.whatwg.org/#map-entry) `@list` whose value is initialized to an empty [array](https://infra.spec.whatwg.org/#list).
   2. Recursively call this algorithm passing the value of *element*'s `@list` [entry](https://infra.spec.whatwg.org/#map-entry) for *element*, *node map*, *active graph*, *active subject*, *active property*, and *result* for *list*.
   3. If *list* is `null`,
      append *result* to the value of the *active property* [entry](https://infra.spec.whatwg.org/#map-entry) of *subject node*.
   4. Otherwise, append *result* to the `@list` [entry](https://infra.spec.whatwg.org/#map-entry) of *list*.
6. Otherwise *element* is a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), perform
   the following steps:
   1. If *element* has an `@id` [entry](https://infra.spec.whatwg.org/#map-entry), set *id* to its value and remove the [entry](https://infra.spec.whatwg.org/#map-entry) from *element*. If *id* is a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), replace it with a newly generated blank node identifier (§7.4) passing *id* for *identifier*.
   2. Otherwise, set *id* to the result of the Generate Blank Node Identifier algorithm (§7.4) passing `null` for *identifier*.
   3. If *graph* does not contain an [entry](https://infra.spec.whatwg.org/#map-entry) *id*, create one and initialize
      its value to a [map](https://infra.spec.whatwg.org/#ordered-map) consisting of a single [entry](https://infra.spec.whatwg.org/#map-entry) `@id` whose
      value is *id*.
   4. Reference the value of the *id* [entry](https://infra.spec.whatwg.org/#map-entry) of *graph* using the
      variable *node*.
   5. If *active subject* is a [map](https://infra.spec.whatwg.org/#ordered-map), a reverse property relationship
      is being processed. Perform the following steps:
      1. If *node* does not have a *active property* [entry](https://infra.spec.whatwg.org/#map-entry),
         create one and initialize its value to an [array](https://infra.spec.whatwg.org/#list) containing *active subject*.
      2. Otherwise, compare *active subject* against every item in the [array](https://infra.spec.whatwg.org/#list) associated with the *active property* [entry](https://infra.spec.whatwg.org/#map-entry) of *node*. If there is no item equivalent to *active subject*,
         append *active subject* to the [array](https://infra.spec.whatwg.org/#list). Two [maps](https://infra.spec.whatwg.org/#ordered-map) are considered
         equal if they have equivalent [map entries](https://infra.spec.whatwg.org/#map-entry).
   6. Otherwise, if *active property* is not `null`, perform the following steps:
      1. Create a new [map](https://infra.spec.whatwg.org/#ordered-map) *reference* consisting of a single [entry](https://infra.spec.whatwg.org/#map-entry) `@id` whose value is *id*.
      2. If *list* is `null`:
         1. If *subject node* does not have an *active property* [entry](https://infra.spec.whatwg.org/#map-entry),
            create one and initialize its value to an [array](https://infra.spec.whatwg.org/#list) containing *reference*.
         2. Otherwise, compare *reference* against every item in the [array](https://infra.spec.whatwg.org/#list) associated with the *active property* [entry](https://infra.spec.whatwg.org/#map-entry) of *subject node*. If there is no item equivalent to *reference*,
            append *reference* to the [array](https://infra.spec.whatwg.org/#list). Two [maps](https://infra.spec.whatwg.org/#ordered-map) are considered
            equal if they have equivalent [map entries](https://infra.spec.whatwg.org/#map-entry).
      3. Otherwise, append *reference* to the `@list` [entry](https://infra.spec.whatwg.org/#map-entry) of *list*.
   7. If *element* has an `@type` [entry](https://infra.spec.whatwg.org/#map-entry), append
      each item of its associated [array](https://infra.spec.whatwg.org/#list) to the [array](https://infra.spec.whatwg.org/#list) associated with the `@type` [entry](https://infra.spec.whatwg.org/#map-entry) of *node* unless it is already in that [array](https://infra.spec.whatwg.org/#list). Finally
      remove the `@type` [entry](https://infra.spec.whatwg.org/#map-entry) from *element*.
   8. If *element* has an `@index` [entry](https://infra.spec.whatwg.org/#map-entry), set the `@index` [entry](https://infra.spec.whatwg.org/#map-entry) of *node* to its value. If [node](https://www.w3.org/TR/rdf11-concepts/#dfn-node) already has an `@index` [entry](https://infra.spec.whatwg.org/#map-entry) with a different value, a `conflicting indexes` error has been detected and processing is aborted. Otherwise, continue by
      removing the `@index` [entry](https://infra.spec.whatwg.org/#map-entry) from *element*.
   9. If *element* has an `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry):
      1. Create a [map](https://infra.spec.whatwg.org/#ordered-map) *referenced node* with a single [entry](https://infra.spec.whatwg.org/#map-entry) `@id` whose
         value is *id*.
      2. Initialize *reverse map* to the value of the `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry) of *element*.
      3. For each key-value pair *property*-*values* in *reverse map*:
         1. For each *value* of *values*:
            1. Recursively invoke this algorithm passing *value* for *element*, *node map*, *active graph*, *referenced node* for *active subject*, and *property* for *active property*. Passing a [map](https://infra.spec.whatwg.org/#ordered-map) for *active subject* indicates to the
               algorithm that a reverse property relationship is being processed.
      4. Remove the `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry) from *element*.
   10. If *element* has an `@graph` [entry](https://infra.spec.whatwg.org/#map-entry), recursively invoke this
       algorithm passing the value of the `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) for *element*, *node map*, and *id* for *active graph* before removing
       the `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) from *element*.
   11. If *element* has an `@included` [entry](https://infra.spec.whatwg.org/#map-entry),
       recursively invoke this algorithm passing the value of the `@included` [entry](https://infra.spec.whatwg.org/#map-entry) for *element*, *node map*, and *active graph* before removing the `@included` [entry](https://infra.spec.whatwg.org/#map-entry) from *element*.
   12. Finally, for each key-value pair *property*-*value* in *element* ordered by *property* perform the following steps:
       1. If *property* is a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), replace it with a newly generated blank node identifier (§7.4) passing *property* for *identifier*.
          > **Note:**
          >
          > > **Note:**
          > >
          > > Note
          >
          > The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
          > and may be removed in a future version of JSON-LD.

       2. If *node* does not have a *property* [entry](https://infra.spec.whatwg.org/#map-entry), create one and initialize
          its value to an empty [array](https://infra.spec.whatwg.org/#list).

       3. Recursively invoke this algorithm passing *value* for *element*, *node map*, *active graph*, *id* for *active subject*,
          and *property* for *active property*.

### 7.3 Merge Node Maps

This algorithm creates a new map of [subjects](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) to [nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-node) using all graphs
contained in the *graph map* created using the Node Map Generation algorithm (§7.2) to create merged [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) containing information defined for a given [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) in each graph contained in the *node map*.

1. Create *result* as an empty [map](https://infra.spec.whatwg.org/#ordered-map)
2. For each *graph name* and *node map* in *graph map* and for each *id* and *node* in *node map*:
   1. Initialize *merged node* to the value for *id* in *result*, initializing it
      with a new [map](https://infra.spec.whatwg.org/#ordered-map) consisting of a single [entry](https://infra.spec.whatwg.org/#map-entry) `@id` whose value is *id*, if it does not exist.
   2. For each *property* and *values* in *node*:
      1. If *property* is a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) other than `@type`, add *property* and values to *merged node*.
      2. Otherwise, merge each element from *values* into the values for *property* in *merged node*, initializing it to an empty [array](https://infra.spec.whatwg.org/#list) if necessary.
3. Return *result*.

### 7.4 Generate Blank Node Identifier

This algorithm is used to generate new [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) or to
relabel an existing [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to avoid collision
by the introduction of new ones.

#### 7.4.1 Overview

*This section is non-normative.*

The simplest case is if there exists already a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) in the *identifier map* for the passed *identifier*, in which
case it is simply returned. Otherwise, a new [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) is generated. If the passed *identifier* is not `null`,
an entry is created in the *identifier map* associating the *identifier* with the [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).

#### 7.4.2 Algorithm

The algorithm takes a single input variable *identifier* which may
be `null`. The algorithm
maintains an *identifier map* to relabel existing [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to new [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), which is reset when the invoking algorithm is initialized.

1. If *identifier* is not `null` and has an entry in the *identifier map*, return the mapped identifier.
2. Otherwise, generate a new unique [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
3. If *identifier* is not `null`, create a new entry
   for *identifier* in *identifier map* and set its value
   to the new [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
4. Return the new [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).

> **Note:**
>
> > **Note:**
> >
> > Note
>
> One way of generating new [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) is to maintain a counter
> and increment it when generating a new identifier and appending it to
> a string such as `_:b`.

## 8. RDF Serialization/Deserialization Algorithms

This section describes algorithms to deserialize a JSON-LD document to an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) and vice versa. The algorithms are designed for in-memory
implementations with random access to [map](https://infra.spec.whatwg.org/#ordered-map) elements.

### 8.1 Deserialize JSON-LD to RDF Algorithm

This algorithm deserializes a JSON-LD document to an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset).
Please note that RDF does not allow a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) to be used
as a [property](https://www.w3.org/TR/rdf11-concepts/#dfn-property), while JSON-LD does. Therefore, by default [triples](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) that would have contained blank nodes as [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) are
discarded when interpreting JSON-LD as RDF.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
> and may be removed in a future version of JSON-LD.

If the `rdfDirection` option is not `null`, then special processing is used to
convert from an `i18n-datatype` or `compound-literal` form.

Implementations *MUST* generate only *well-formed* [triples](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) and [graph names](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name):

- An [IRI](https://tools.ietf.org/html/rfc3987#section-2) is well-formed if it matches the [ABNF for **IRI**](https://tools.ietf.org/html/rfc3987#section-2.2) as
  described in [RFC3987].

- A [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) is well-formed if it matches the [EBNF for **BLANK_NODE_LABEL**](https://www.w3.org/TR/turtle/#sec-grammar-grammar) as described in [Turtle].
  > **Note:**
  >
  > > **Note:**
  > >
  > > Note
  >
  > When following the algorithm described here,
  > all blank node identifiers will be normalized using the Generate Blank Node Identifier algorithm (§7.4) and automatically adhere to this form.

- A [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) is well-formed if it has the lexical form of a [string](https://infra.spec.whatwg.org/#javascript-string), any [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) is well-formed, and any [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) is well-formed according to [section 2.2.9](https://tools.ietf.org/html/bcp47#section-2.2.9) of
  [BCP47].

#### 8.1.1 Overview

*This section is non-normative.*

The JSON-LD document is expanded and converted to a *node map* using the Node Map Generation algorithm (§7.2).
This allows each graph represented within the document to be
extracted and flattened, making it easier to process each [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).
Each graph from the *node map* is processed to extract [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple),
to which any (non-default) graph name is applied to create an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset).
Each [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) in the *node map* has an `@id` [entry](https://infra.spec.whatwg.org/#map-entry) which corresponds to the [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject),
the other [entries](https://infra.spec.whatwg.org/#map-entry) represent [predicates](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate).
Each [entry](https://infra.spec.whatwg.org/#map-entry) value is either an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) or can be transformed to an[RDF literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) to generate an [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple). [Lists](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) are transformed into an [RDF collection](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) using the List to RDF Conversion algorithm. (§8.3)

#### 8.1.2 Algorithm

The algorithm takes a [map](https://infra.spec.whatwg.org/#ordered-map) *node map*, which
is the result of the Node Map Generation algorithm (§7.2) and
an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) *dataset* into which new [graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) and [triples](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) are added.
It also takes two optional input variables `produceGeneralizedRdf` and `rdfDirection`.
Unless the `produceGeneralizedRdf` option
is set to `true`, [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) containing a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate) are excluded from output.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
> and may be removed in a future version of JSON-LD,
> as is the support for [generalized RDF Datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-generalized-rdf-dataset) and thus the `produceGeneralizedRdf` option may be also be removed.

1. For each *graph name* and *graph* in *node map* ordered by *graph name*:
   1. If *graph name* is not well-formed, continue
      with the next *graph name*-*graph* pair.
   2. If *graph name* is `@default`,
      initialize *triples* to the value of the `defaultGraph` attribute of *dataset*.
      Otherwise, initialize *triples* as an empty `RdfGraph` and add to *dataset* using its `add` method along with *graph name* for `graphName`.
   3. For each *subject* and *node* in *graph* ordered
      by *subject*:
      1. If *subject* is not well-formed, continue
         with the next *subject*-*node* pair.
      2. For each *property* and *values* in *node* ordered by *property*:
         1. If *property* is `@type`, then for each *type* in *values*,
            create a new `RdfTriple` composed of *subject*, `rdf:type` for `predicate`,
            and *type* for `object` and add to *triples* using its `add` method,
            unless *type* is not well-formed.

         2. Otherwise, if *property* is a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) continue with the next *property*-*values* pair.

         3. Otherwise, if *property* is a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) and
            the `produceGeneralizedRdf` option is not `true`,
            continue with the next *property*-*values* pair.
            > **Note:**
            >
            > > **Note:**
            > >
            > > Note
            >
            > The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
            > and may be removed in a future version of JSON-LD,
            > as is the support for [generalized RDF Datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-generalized-rdf-dataset) and thus the `produceGeneralizedRdf` option may be also be removed.

         4. Otherwise, if *property* is not well-formed,
            continue with the next *property*-*values* pair.

         5. Otherwise, *property* is an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier). For each *item* in *values*:

            1. Initialize *list triples* as an empty [array](https://infra.spec.whatwg.org/#list).
               > **Note:**
               >
               > > **Note:**
               > >
               > > Note
               >
               > *item* is a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object), [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object),
               > or a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).

            2. Add a [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) composed of *subject*, *property*, and
               the result of using the Object to RDF Conversion algorithm (§8.2) passing *item* and *list triples* to *triples* using its `add` method,
               unless the result is `null`,
               indicating a non-well-formed [resource](https://www.w3.org/TR/rdf11-concepts/#dfn-resource) that has to be ignored.

            3. Add all `RdfTriple` instances from *list triples* to *triples* using
               its `add` method.

### 8.2 Object to RDF Conversion

This algorithm takes a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object), or [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) and transforms it into an [resource](https://www.w3.org/TR/rdf11-concepts/#dfn-resource) to be used as the [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) of an [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple).
If a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) containing a [relative IRI reference](https://tools.ietf.org/html/rfc3987#section-6.5) is passed to
the algorithm, `null` is returned which then causes the resulting [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) to be ignored. If the input is a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object), it will also
return the triples created from that input.

#### 8.2.1 Overview

*This section is non-normative.*

[Value objects](https://www.w3.org/TR/json-ld11/#dfn-value-object) are transformed to [RDF literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) as described in § 8.6 Data Round Tripping (§8.6) whereas [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) are transformed
to [IRIs](https://tools.ietf.org/html/rfc3987#section-2), [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier),
or `null`.

#### 8.2.2 Algorithm

The algorithm takes as two arguments *item* which *MUST* be
either a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object), [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object), or [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) and *list triples*, which is an empty array.

1. If *item* is a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) and the value of
   its `@id` [entry](https://infra.spec.whatwg.org/#map-entry) is not well-formed, return `null`.

2. If *item* is a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), return the [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) associated
   with its `@id` [entry](https://infra.spec.whatwg.org/#map-entry).

3. If *item* is a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object) return the result of the List Conversion algorithm (§8.3), passing
   the value associated with the `@list` [entry](https://infra.spec.whatwg.org/#map-entry) from *item* and *list triples*.

4. Otherwise, *item* is a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object). Initialize *value* to the value associated with the `@value` [entry](https://infra.spec.whatwg.org/#map-entry) in *item*.

5. Initialize *datatype* to the value associated with the `@type` [entry](https://infra.spec.whatwg.org/#map-entry) of *item* or `null` if *item* does not have such an [entry](https://infra.spec.whatwg.org/#map-entry).

6. If *datatype* is not `null` and neither a well-formed [IRI](https://tools.ietf.org/html/rfc3987#section-2) nor `@json`,
   return `null`.

7. If *item* has an `@language` [entry](https://infra.spec.whatwg.org/#map-entry) which is not well-formed, return `null`.

8. If *datatype* is `@json`,
   convert *value* to the canonical lexical form using the result of transforming the internal representation of *value* to JSON and set *datatype* to `rdf:JSON`.
   > **Issue:**
   >
   > > **Issue:**
   > >
   > > Issue
   >
   > The JSON Canonicalization Scheme (JCS) [RFC8785]
   > is an emerging standard for JSON canonicalization.
   > This specification will likely be updated to require such a canonical representation.
   > Users are cautioned from depending on the [JSON literal](https://www.w3.org/TR/json-ld11/#dfn-json-literal) lexical representation as an [RDF literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal),
   > as the specifics of serialization may change in a future revision of this document.

9. If *value* is `true` or `false`, set *value* to the [string](https://infra.spec.whatwg.org/#javascript-string) `true` or `false` which is the canonical lexical form as described in § 8.6 Data Round Tripping (§8.6) If *datatype* is `null`,
   set *datatype* to `xsd:boolean`.

10. Otherwise, if *value* is a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) with a non-zero fractional
    part (the result of a modulo‑1 operation) or an absolute value greater or equal to 1021,
    or *value* is a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) and *datatype* equals `xsd:double`, convert *value* to a [string](https://infra.spec.whatwg.org/#javascript-string) in canonical lexical form of
    an [`xsd:double`](https://www.w3.org/TR/xmlschema11-2/#double) as defined in [XMLSCHEMA11-2]
    and described in § 8.6 Data Round Tripping (§8.6).
    If *datatype* is `null`,
    set *datatype* to `xsd:double`.

11. Otherwise, if *value* is a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value),
    convert it to a [string](https://infra.spec.whatwg.org/#javascript-string) in canonical lexical form of
    an [`xsd:integer`](https://www.w3.org/TR/xmlschema11-2/#integer) as defined in [XMLSCHEMA11-2]
    and described in § 8.6 Data Round Tripping (§8.6).
    If *datatype* is `null`,
    set *datatype* to `xsd:integer`.
    > **Note:**
    >
    > > **Note:**
    > >
    > > Note
    >
    > It follows from the previous step that *value* has no non-zero fractional part.

12. Otherwise, if *datatype* is `null`,
    set *datatype* to `xsd:string` or `rdf:langString`,
    depending on if item has an `@language` [entry](https://infra.spec.whatwg.org/#map-entry).

13. If *item* contains an `@direction` [entry](https://infra.spec.whatwg.org/#map-entry) and `rdfDirection` is not `null`, *item* is a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) which is serialized using special rules.

    1. Initialize *language* to the value of `@language` in *item* normalized to lower case,
       or the empty string (`""`) if there is no such entry.
       > **Note:**
       >
       > > **Note:**
       > >
       > > Note
       >
       > Generally, language tags are not normalized,
       > but when creating an `i18n-datatype` or `compound-literal` values are normalized to lower case for improved interoperability.

    2. If `rdfDirection` is `i18n-datatype`,
       set *datatype* to the result of appending *language* and the value of `@direction` in *item* separated by an underscore (`"_"`)
       to `https://www.w3.org/ns/i18n#`.
       Initialize *literal* as an [RDF literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) using *value* and *datatype*.
       > **Note:**
       >
       > > **Note:**
       > >
       > > Note
       >
       > Processors *MAY* normalize [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) to lower case.
       > **Note:**
       >
       > > **Note:**
       > >
       > > Note
       >
       > As `@direction` may be used without `@language`,
       > it is possible, and legitimate, to create a datatype IRI such as `http://w3.org/ns/i18n#_ltr`, which does not encode a language tag.

    3. Otherwise, if `rdfDirection` is `compound-literal`:

       1. Initialize *literal* as a new [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node).
       2. Create a new triple using *literal* as the subject, `rdf:value` as the predicate, and the value of `@value` in *item* as the object, and add it to *list triples*.
       3. If the *item* has an entry for `@language`,
          create a new triple using *literal* as the subject, `rdf:language` as the predicate, and *language* as the object, and add it to *list triples*.
       4. Create a new triple using *literal* as the subject, `rdf:direction` as the predicate, and the value of `@direction` in *item* as the object, and add it to *list triples*.

14. Otherwise, initialize *literal* as an [RDF literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) using *value* and *datatype*. If *item* has an `@language` [entry](https://infra.spec.whatwg.org/#map-entry), add the value associated with the `@language` [entry](https://infra.spec.whatwg.org/#map-entry) as the [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) of *literal*.

15. Return *literal*.

### 8.3 List to RDF Conversion

List Conversion is the process of taking a [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object) and transforming it into an [RDF collection](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) as defined in RDF Semantics [RDF11-MT].

#### 8.3.1 Overview

*This section is non-normative.*

For each element of the [list](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) a new [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) is allocated which is used to generate `rdf:first` and `rdf:rest`. The
algorithm returns the list head, which is either the first allocated [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) or `rdf:nil` if the [list](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) is empty. If a list element represents an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
the corresponding `rdf:first` triple is omitted.

#### 8.3.2 Algorithm

The algorithm takes two inputs: an [array](https://infra.spec.whatwg.org/#list) *list* and an empty [array](https://infra.spec.whatwg.org/#list) *list triples* used for returning
the generated [triples](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple).

1. If *list* is empty, return `rdf:nil`.
2. Otherwise, create an [array](https://infra.spec.whatwg.org/#list) *bnodes* composed of a newly generated blank node identifier (§7.4) for each entry in *list*.
3. For each pair of *subject* from *bnodes* and *item* from *list*:
   1. Initialize *embedded triples* to a new empty array.
   2. Initialize *object* to the result of using the Object to RDF Conversion algorithm (§8.2) passing *item* and *embedded triples* for *list triples*.
   3. Unless *object* is `null`, append a [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) composed of *subject*, `rdf:first`, and *object* to *list triples*.
   4. Initialize *rest* as the next entry in *bnodes*, or if that
      does not exist, `rdf:nil`. Append a [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) composed of *subject*, `rdf:rest`, and *rest* to *list triples*.
   5. Append all values from *embedded triples* to *list triples*
4. Return the first [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) from *bnodes* or `rdf:nil` if *bnodes* is empty.

### 8.4 Serialize RDF as JSON-LD Algorithm

This algorithm serializes an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) consisting of a [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) and zero or more [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph) into a JSON-LD document.

In the RDF abstract syntax, [RDF literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) have a [*lexical form*](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-form), as defined
in [RDF11-CONCEPTS]. The form of these literals is used when creating [JSON-LD values](https://www.w3.org/TR/json-ld11/#dfn-json-ld-value) based on these literals.

#### 8.4.1 Overview

*This section is non-normative.*

Iterate through each graph in the dataset, converting each [RDF collection](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) into a [list](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) and generating a JSON-LD document in expanded form for all [RDF literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal), [IRIs](https://tools.ietf.org/html/rfc3987#section-2) and [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).
If the `useNativeTypes` flag is set to `true`, [RDF literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) with a [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) that equals `xsd:integer` or `xsd:double` are converted
to a [JSON numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) and [RDF literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) with a [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) that equals `xsd:boolean` are converted to `true` or `false` based on their lexical form as described in § 8.6 Data Round Tripping (§8.6).
Unless the `useRdfType` flag is set to true, `rdf:type` predicates will be serialized as `@type` as long as the associated object is
either an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).

If the `rdfDirection` option is not `null`, then special processing is used to
convert from an `i18n-datatype` or `compound-literal` form.

#### 8.4.2 Algorithm

The algorithm takes one required and four optional inputs:
an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) *dataset* and the four optional arguments are
the `ordered` flag, defaulting to `false`, used to order [map entry](https://infra.spec.whatwg.org/#map-entry) keys lexicographically, where noted, `rdfDirection` defaulting to `null`,
the `useNativeTypes` flag, defaulting to `false`,
and the `useRdfType` flag, defaulting to `false`.

The *dataset* is `iterable` to iterate over [graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) and [graph names](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name) contained within the `RdfDataset`. Each [graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) is also `iterable` for iterating over [triples](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) contained within the `RdfGraph`.

1. Initialize *default graph* to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
2. Initialize *graph map* to a [map](https://infra.spec.whatwg.org/#ordered-map) consisting
   of a single [entry](https://infra.spec.whatwg.org/#map-entry) `@default` whose value references *default graph*.
3. Initialize *referenced once* to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
4. Initialize *compound literal subjects* to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
5. For each *graph* in *dataset*:
   1. If *graph* is the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph),
      initialize *name* to `@default`, otherwise to the [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name) associated with *graph*.
   2. If *graph map* has no *name* [entry](https://infra.spec.whatwg.org/#map-entry), create one and set
      its value to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
   3. If *compound literal subjects* has no *name* [entry](https://infra.spec.whatwg.org/#map-entry), create one and set
      its value to an empty [map](https://infra.spec.whatwg.org/#ordered-map).
   4. If *graph* is not the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) and *default graph* does not have a *name* [entry](https://infra.spec.whatwg.org/#map-entry),
      create such an [entry](https://infra.spec.whatwg.org/#map-entry) and initialize its value to a new [map](https://infra.spec.whatwg.org/#ordered-map) with a single [entry](https://infra.spec.whatwg.org/#map-entry) `@id` whose value is *name*.
   5. Reference the value of the *name* [entry](https://infra.spec.whatwg.org/#map-entry) in *graph map* using the variable *node map*.
   6. Reference the value of the *name* [entry](https://infra.spec.whatwg.org/#map-entry) in *compound literal subjects* using the variable *compound map*.
   7. For each [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) in *graph* consisting of *subject*, *predicate*, and *object*:
      1. If *node map* does not have a *subject* [entry](https://infra.spec.whatwg.org/#map-entry),
         create one and initialize its value to a new [map](https://infra.spec.whatwg.org/#ordered-map) consisting of a single [entry](https://infra.spec.whatwg.org/#map-entry) `@id` whose value is
         set to *subject*.
      2. Reference the value of the *subject* [entry](https://infra.spec.whatwg.org/#map-entry) in *node map* using the variable *node*.
      3. If the `rdfDirection` option
         is `compound-literal` and *predicate* is `rdf:direction`,
         add an entry in *compound map* for *subject* with the value `true`.
      4. If *object* is an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier),
         and *node map* does not have an *object* [entry](https://infra.spec.whatwg.org/#map-entry),
         create one and initialize its value to a new [map](https://infra.spec.whatwg.org/#ordered-map) consisting of a single [entry](https://infra.spec.whatwg.org/#map-entry) `@id` whose value is
         set to *object*.
      5. If *predicate* equals `rdf:type`, the `useRdfType` flag is not `true`, and *object* is an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier),
         append *object* to the value of the `@type` [entry](https://infra.spec.whatwg.org/#map-entry) of *node*; unless such an item already exists.
         If no such [entry](https://infra.spec.whatwg.org/#map-entry) exists, create one
         and initialize it to an [array](https://infra.spec.whatwg.org/#list) whose only item is *object*. Finally, continue to the next [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple).
      6. Initialize *value* to the result of using the RDF to Object Conversion algorithm (§8.5),
         passing *object*, `rdfDirection`,
         and `useNativeTypes`.
      7. If *node* does not have a *predicate* [entry](https://infra.spec.whatwg.org/#map-entry), create one
         and initialize its value to an empty [array](https://infra.spec.whatwg.org/#list).
      8. If there is no item equivalent to *value* in the [array](https://infra.spec.whatwg.org/#list) associated with the *predicate* [entry](https://infra.spec.whatwg.org/#map-entry) of *node*, append a
         reference to *value* to the [array](https://infra.spec.whatwg.org/#list). Two [maps](https://infra.spec.whatwg.org/#ordered-map) are considered equal if they have equivalent [map entries](https://infra.spec.whatwg.org/#map-entry).
      9. If *object* is `rdf:nil`, it represents
         the termination of an [RDF collection](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab):
         1. Reference the `usages` [entry](https://infra.spec.whatwg.org/#map-entry) of the *object* [entry](https://infra.spec.whatwg.org/#map-entry) of *node map* using the variable *usages*.
         2. Append a new [map](https://infra.spec.whatwg.org/#ordered-map) consisting of three [entries](https://infra.spec.whatwg.org/#map-entry), `node`, `property`, and `value` to the *usages* [array](https://infra.spec.whatwg.org/#list). The `node` [entry](https://infra.spec.whatwg.org/#map-entry) is set to a reference to *node*, `property` to *predicate*,
            and `value` to a reference to *value*.
      10. Otherwise, if *referenced once* has an entry for *object*,
          set the *object* [entry](https://infra.spec.whatwg.org/#map-entry) of *referenced once* to `false`.
      11. Otherwise, if *object* is a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier),
          it might represent a list node:
          1. Set the *object* [entry](https://infra.spec.whatwg.org/#map-entry) of *referenced once* to a new [map](https://infra.spec.whatwg.org/#ordered-map) consisting of three [entries](https://infra.spec.whatwg.org/#map-entry), `node`, `property`, and `value` to the *usages* [array](https://infra.spec.whatwg.org/#list). The `node` [entry](https://infra.spec.whatwg.org/#map-entry) is set to a reference to *node*, `property` to *predicate*,
             and `value` to a reference to *value*.
6. For each *name* and *graph object* in *graph map*:
   1. If *compound literal subjects* has an entry for *name*, then for each *cl* which is a key in that entry:
      1. Initialize *cl entry* to the value of *cl* in *referenced once*,
         continuing to the next *cl* if *cl entry* is not a [map](https://infra.spec.whatwg.org/#ordered-map).
      2. Initialize *node* to the value of `node` in *cl entry*.
      3. Initialize *property* to value of `property` in *cl entry*.
      4. Initialize *value* to value of `value` in *cl entry*.
      5. Initialize *cl node* to the value of *cl* in *graph object*, and remove that [entry](https://infra.spec.whatwg.org/#map-entry) from *graph object*,
         continuing to the next *cl* if *cl node* is not a [map](https://infra.spec.whatwg.org/#ordered-map).
      6. For each *cl reference* in the value of *property* in *node* where the value of `@id` in *cl reference* is *cl*:
         1. Delete the `@id` entry in *cl reference*.
         2. Add an [entry](https://infra.spec.whatwg.org/#map-entry) to *cl reference* for `@value` with the value taken
            from the `rdf:value` entry in *cl node*.
         3. Add an [entry](https://infra.spec.whatwg.org/#map-entry) to *cl reference* for `@language` with the value taken
            from the `rdf:language` entry in *cl node*, if any.
            If that value is not well-formed according to [section 2.2.9](https://tools.ietf.org/html/bcp47#section-2.2.9) of [BCP47],
            an `invalid language-tagged string` error has been detected and processing is aborted.
         4. Add an [entry](https://infra.spec.whatwg.org/#map-entry) to *cl reference* for `@direction` with the value taken
            from the `rdf:direction` entry in *cl node*, if any.
            If that value is not `"ltr"` or `"rtl"`, an `invalid base direction` error has been detected and processing is aborted.
   2. If *graph object* has no `rdf:nil` [entry](https://infra.spec.whatwg.org/#map-entry), continue
      with the next *name*-*graph object* pair as the graph does
      not contain any lists that need to be converted.
   3. Initialize *nil* to the value of the `rdf:nil` [entry](https://infra.spec.whatwg.org/#map-entry) of *graph object*.
   4. For each item *usage* in the `usages` [entry](https://infra.spec.whatwg.org/#map-entry) of *nil*, perform the following steps:
      1. Initialize *node* to the value of the value of the `node` [entry](https://infra.spec.whatwg.org/#map-entry) of *usage*, *property* to
         the value of the `property` [entry](https://infra.spec.whatwg.org/#map-entry) of *usage*,
         and *head* to the value of the `value` [entry](https://infra.spec.whatwg.org/#map-entry) of *usage*.
      2. Initialize two empty [arrays](https://infra.spec.whatwg.org/#list) *list* and *list nodes*.
      3. While *property* equals `rdf:rest`, the value of the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) of *node* is a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), the value of the [entry](https://infra.spec.whatwg.org/#map-entry) of *referenced once* associated with the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) of `node` is a [map](https://infra.spec.whatwg.org/#ordered-map), *node* has `rdf:first` and `rdf:rest` [entries](https://infra.spec.whatwg.org/#map-entry),
         both of which have as value an [array](https://infra.spec.whatwg.org/#list) consisting of a single element,
         and *node* has no other [entries](https://infra.spec.whatwg.org/#map-entry) apart from an optional `@type` [entry](https://infra.spec.whatwg.org/#map-entry) whose value is an array with a single item equal to `rdf:List`, *node* represents a well-formed list node.
         Perform the following steps to traverse the list backwards towards its head:
         1. Append the only item of `rdf:first` [entry](https://infra.spec.whatwg.org/#map-entry) of *node* to the *list* [array](https://infra.spec.whatwg.org/#list).
         2. Append the value of the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) of *node* to the *list nodes* [array](https://infra.spec.whatwg.org/#list).
         3. Initialize *node usage* to the value of the [entry](https://infra.spec.whatwg.org/#map-entry) of *referenced once* associated with the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) of `node`.
         4. Set *node* to the value of the `node` [entry](https://infra.spec.whatwg.org/#map-entry) of *node usage*, *property* to the value of the `property` [entry](https://infra.spec.whatwg.org/#map-entry) of *node usage*, and *head* to the value of the `value` [entry](https://infra.spec.whatwg.org/#map-entry) of *node usage*.
         5. If the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) of *node* is an [IRI](https://tools.ietf.org/html/rfc3987#section-2) instead of a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier),
            exit the while loop.
      4. Remove the `@id` [entry](https://infra.spec.whatwg.org/#map-entry) from *head*.
      5. Reverse the order of the *list* [array](https://infra.spec.whatwg.org/#list).
      6. Add an `@list` [entry](https://infra.spec.whatwg.org/#map-entry) to *head* and initialize
         its value to the *list* [array](https://infra.spec.whatwg.org/#list).
      7. For each item *node id* in *list nodes*, remove the *node id* [entry](https://infra.spec.whatwg.org/#map-entry) from *graph object*.
7. Initialize an empty [array](https://infra.spec.whatwg.org/#list) *result*.
8. For each *subject* and *node* in *default graph* ordered lexicographically by *subject* if `ordered` is `true`:
   1. If *graph map* has a *subject* [entry](https://infra.spec.whatwg.org/#map-entry):
      1. Add an `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) to *node* and initialize
         its value to an empty [array](https://infra.spec.whatwg.org/#list).
      2. For each key-value pair *s*-*n* in the *subject* [entry](https://infra.spec.whatwg.org/#map-entry) of *graph map* ordered lexicographically by *s* if `ordered` is `true`,
         append *n* to the `@graph` [entry](https://infra.spec.whatwg.org/#map-entry) of *node* after
         removing its `usages` [entry](https://infra.spec.whatwg.org/#map-entry), unless the only
         remaining [entry](https://infra.spec.whatwg.org/#map-entry) of *n* is `@id`.
   2. Append *node* to *result* after removing its `usages` [entry](https://infra.spec.whatwg.org/#map-entry), unless the only remaining [entry](https://infra.spec.whatwg.org/#map-entry) of *node* is `@id`.
9. Return *result*.

### 8.5 RDF to Object Conversion

This algorithm transforms an RDF literal to a JSON-LD [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) and a RDF [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) or [IRI](https://tools.ietf.org/html/rfc3987#section-2) to an JSON-LD [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).

#### 8.5.1 Overview

*This section is non-normative.*

[RDF literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) are transformed to [value objects](https://www.w3.org/TR/json-ld11/#dfn-value-object) whereas [IRIs](https://tools.ietf.org/html/rfc3987#section-2) and [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) are
transformed to [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object).

Literals with datatype `rdf:JSON` are transformed into a value object using the internal representation
based on the lexical-to-value mapping defined in [JSON datatype](https://www.w3.org/TR/json-ld11/#the-rdf-json-datatype) in [JSON-LD11],
and `@type` of `@json`.

With the `rdfDirection` option set to `i18n-datatype`,
literals with datatype starting with `https://www.w3.org/ns/i18n#` are transformed into a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) by decoding
the [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) and [base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) from the datatype.

With the `rdfDirection` option set to `compound-literal`,
blank node objects using `rdf:direction` are
are transformed into a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) by decoding
the `rdf:value`, `rdf:language`, and `rdf:direction` properties.

If the `useNativeTypes` flag is set to `true`, [RDF literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) with a [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) that equals `xsd:integer` or `xsd:double` are converted
to a [JSON numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) and [RDF literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) with a [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) that equals `xsd:boolean` are converted to `true` or `false` based on their lexical form as described in § 8.6 Data Round Tripping (§8.6).

#### 8.5.2 Algorithm

This algorithm takes three required inputs:
a *value* to be converted to a [map](https://infra.spec.whatwg.org/#ordered-map), `rdfDirection`,
and a flag `useNativeTypes`.

1. If *value* is an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), return a new [map](https://infra.spec.whatwg.org/#ordered-map) consisting of a single [entry](https://infra.spec.whatwg.org/#map-entry) `@id` whose value is set to *value*.
2. Otherwise *value* is an [RDF literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal):
   1. Initialize a new empty [map](https://infra.spec.whatwg.org/#ordered-map) result.

   2. Initialize *converted value* to *value*.

   3. Initialize *type* to `null`

   4. If `useNativeTypes` is `true`

      1. If the [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) of *value* equals `xsd:string`, set *converted value* to the lexical form of *value*.
      2. Otherwise, if the [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) of *value* equals `xsd:boolean`, set *converted value* to `true` if the lexical form of *value* matches `true`, or `false` if it matches `false`. If it matches neither,
         set *type* to `xsd:boolean`.
      3. Otherwise, if the [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) of *value* equals `xsd:integer` or `xsd:double` and its lexical form is a valid `xsd:integer` or `xsd:double` according [XMLSCHEMA11-2], set *converted value* to the result of converting the lexical form to a JSON [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value).

   5. Otherwise, if [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is not `json-ld-1.0`,
      and *value* is a [JSON literal](https://www.w3.org/TR/json-ld11/#dfn-json-literal),
      set *converted value* to the result of
      turning the lexical value of *value* into the JSON-LD internal representation, and set *type* to `@json`.
      If the lexical value of *value* is not valid JSON according to
      the [JSON Grammar](https://tools.ietf.org/html/rfc8259#section-2) [RFC8259],
      an `invalid JSON literal` error has been detected and processing is aborted.

   6. Otherwise, if the [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) of *value* starts with `https://www.w3.org/ns/i18n#`,
      and `rdfDirection` is `i18n-datatype`:

      1. Set *converted value* to the lexical form of *value*.

      2. If the string prefix of the [fragment identifier](https://tools.ietf.org/html/rfc3986#section-3.5) of the [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) up until the underscore (`"_"`) is not empty,
         add an [entry](https://infra.spec.whatwg.org/#map-entry) `@language` to *result* and set its value to that prefix.
         > **Note:**
         >
         > > **Note:**
         > >
         > > Note
         >
         > As `@direction` may be used without `@language`,
         > it is possible, and legitimate, to create a datatype IRI such as `http://w3.org/ns/i18n#_ltr`, which does not encode a language tag.

      3. Add an [entry](https://infra.spec.whatwg.org/#map-entry) `@direction` to *result* and set its value to the substring of the [fragment identifier](https://tools.ietf.org/html/rfc3986#section-3.5) following
         the underscore (`"_"`).

   7. Otherwise, if *value* is a [language-tagged string](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string) add an [entry](https://infra.spec.whatwg.org/#map-entry) `@language` to *result* and set its value to the [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) of *value*.

   8. Otherwise, set *type* to the [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) of *value*, unless it equals `xsd:string` which is ignored.

   9. Add an [entry](https://infra.spec.whatwg.org/#map-entry) `@value` to *result* whose value
      is set to *converted value*.

   10. If *type* is not `null`, add an [entry](https://infra.spec.whatwg.org/#map-entry) `@type` to *result* whose value is set to *type*.

   11. Return *result*.

### 8.6 Data Round Tripping

When deserializing JSON-LD to RDF (§8.1) JSON-native [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) are automatically
type-coerced to `xsd:integer` or `xsd:double` depending on whether the [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) has a non-zero fractional part
or not (the result of a modulo‑1 operation), the boolean values `true` and `false` are coerced to `xsd:boolean`,
and [strings](https://infra.spec.whatwg.org/#javascript-string) are coerced to `xsd:string`.
The JSON, numeric, or boolean values themselves are converted to *canonical lexical form*, i.e., a deterministic string
representation as defined in [XMLSCHEMA11-2].

The canonical lexical form of an *integer*, i.e., a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) with no non-zero fractional part and an absolute value less than 1021, or a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) coerced to `xsd:integer`,
is a finite-length sequence of decimal
digits (`0-9`) with an optional leading minus sign; leading
zeros are prohibited. In JavaScript, implementers can use the following
snippet of code to convert an integer to canonical lexical form:
> **Example:**
>
> Example 20: Sample integer serialization implementation in JavaScript
>
>
>
> ```
> (value).toFixed(0).toString()
> ```

The canonical lexical form of a *double*, i.e., a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) with a non-zero fractional part or an absolute value greater or equal to 1021,
or a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) coerced to `xsd:double`, consists of a mantissa followed by the
character `E`, followed by an exponent. The mantissa is a
decimal number and the exponent is an integer. Leading zeros and a
preceding plus sign (`+`) are prohibited in the exponent.
If the exponent is zero, it is indicated by `E0`. For the
mantissa, the preceding optional plus sign is prohibited and the
decimal point is required. Leading and trailing zeros are prohibited
subject to the following: number representations must be normalized
such that there is a single digit which is non-zero to the left of
the decimal point and at least a single digit to the right of the
decimal point unless the value being represented is zero. The
canonical representation for zero is `0.0E0`. `xsd:double`'s value space is defined by the IEEE
double-precision 64-bit floating point type [IEEE-754-2008] whereas
the value space of JSON [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) is not
specified; when deserializing JSON-LD to RDF the mantissa is rounded to
15 digits after the decimal point. In JavaScript, implementers
can use the following snippet of code to convert a double to canonical lexical form:
> **Example:**
>
> Example 21: Sample floating point number serialization implementation in JavaScript
>
>
>
> ```
> (value).toExponential(15).replace(/(\d)0*e\+?/,'$1E')
> ```

The canonical lexical form of the *boolean* values `true` and `false` are the strings `true` and `false`.

The canonical lexical form of a [JSON literal](https://www.w3.org/TR/json-ld11/#dfn-json-literal) is the result of serializing the internal representation into the JSON format [RFC8259] in compliance with the constraints of the **value space** description within [The `rdf:JSON` Datatype](https://www.w3.org/TR/json-ld11/#the-rdf-json-datatype) of [JSON-LD11].
> **Example:**
>
> Example 22: Canonicalized JSON literal
>
> ```
> {
>   "@context": {
>     "@version": 1.1,
>     "e": {"@id": "http://example.org/vocab#json", "@type": "@json"}
>   },
>   "e": [
>     56.0,
>     {
>       "d": true,
>       "10": null,
>       "1": [ ]
>     }
>   ]
> }
> ```
>
> The example shows the value of "e" as a native JSON array including
> unnecessary whitespace, a number and an object. The result
> eliminates the whitespace, uses a canonical number representation,
> and reorders the [map entries](https://infra.spec.whatwg.org/#map-entry) lexicographically:
>
> ```
> @prefix ex: <http://example.org/vocab#> .
> @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> [ex:json """[56,{"1":[],"10":null,"d":true}]"""^^rdf:JSON] .
> ```

When JSON-native [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) are deserialized
to RDF, lossless data round-tripping cannot be guaranteed, as rounding
errors might occur. When serializing RDF as JSON-LD (§8.4),
similar rounding errors might occur. Furthermore, the datatype or the lexical
representation might be lost. An `xsd:double` with a value
of `2.0` will, e.g., result in an `xsd:integer` with a value of `2` in canonical lexical form when converted from RDF to JSON-LD and back to RDF. It is important
to highlight that in practice it might be impossible to losslessly
convert an `xsd:integer` to a [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) because
its value space is not limited. While the JSON specification [RFC8259]
does not limit the value space of [numbers](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value) either, concrete implementations typically do have a limited value
space.

To ensure lossless round-tripping the §8.4 Serialize RDF as JSON-LD Algorithm specifies a `useNativeTypes` flag which controls whether [RDF literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) with a [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) equal to `xsd:integer`, `xsd:double`, or `xsd:boolean` are converted to their JSON-native
counterparts. If the `useNativeTypes` flag is set to `false`, all literals remain in their original string
representation.

Some JSON serializers, such as PHP's native implementation in some versions,
backslash-escape the forward slash character. For example, the value `http://example.com/` would be serialized as `http:\/\/example.com\/`.
This is problematic as other JSON parsers might not understand those escaping characters.
There is no need to backslash-escape forward slashes in JSON-LD. To aid
interoperability between JSON-LD processors, forward slashes *MUST NOT* be
backslash-escaped.

## 9. The Application Programming Interface

This API provides a clean mechanism that enables developers to convert
JSON-LD data into a variety of output formats that are often easier to
work with.

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

### 9.1 The *`JsonLdProcessor`* Interface

The `JsonLdProcessor` interface is the high-level programming structure
that developers use to access the JSON-LD transformation methods.

It is important to highlight that implementations do not modify the input parameters.
If an error is detected, the [`Promise`](https://heycam.github.io/webidl/#idl-promise) is
rejected with a `JsonLdError` having an appropriate `code` and processing is stopped.

If the `documentLoader` option is specified, it is used to dereference remote documents and contexts.
The `documentUrl` in the returned `RemoteDocument` is used as [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri) and the `contextUrl` is used instead of looking at the HTTP Link Header directly. For the sake of simplicity, none of the algorithms
in this document mention this directly.

```
WebIDL/*
 * The JsonLd interface is created to expose the JsonLdProcessor interface.
 */
[Global=JsonLd, Exposed=JsonLd]
interface JsonLd {};

[Exposed=JsonLd]
interface JsonLdProcessor {
  constructor();
  static Promise<JsonLdRecord> compact(
    JsonLdInput input,
    optional JsonLdContext context = null,
    optional JsonLdOptions options = {});
  static Promise<sequence<JsonLdRecord>> expand(
    JsonLdInput input,
    optional JsonLdOptions options = {});
  static Promise<JsonLdRecord> flatten(
    JsonLdInput input,
    optional JsonLdContext context = null,
    optional JsonLdOptions options = {});
  static Promise<sequence<JsonLdRecord>> fromRdf(
    RdfDataset input,
    optional JsonLdOptions options = {});
  static Promise<RdfDataset> toRdf(
    JsonLdInput input,
    optional JsonLdOptions options = {});
};
```

*`compact()`*

Compacts the given input using the *context* according to the steps in the §6.1 Compaction Algorithm:

The final output is a [map](https://infra.spec.whatwg.org/#ordered-map) derived from *compacted output*.
If *compacted output* is an [array](https://infra.spec.whatwg.org/#list), it is
included with an entry of (a possibly aliased) `@graph` with the value of *compacted output*,
otherwise *compacted output* is used as the [map](https://infra.spec.whatwg.org/#ordered-map) result.
If context not `null`,
an `@context` entry is added to the [map](https://infra.spec.whatwg.org/#ordered-map) result.

1. Create a new [`Promise`](https://heycam.github.io/webidl/#idl-promise) *promise* and return it.
   The following steps are then deferred.
2. If the provided input is a `RemoteDocument`,
   initialize *remote document* to input.
3. Otherwise, if the provided input is a [string](https://infra.spec.whatwg.org/#javascript-string) representing the [IRI](https://tools.ietf.org/html/rfc3987#section-2) of a remote document, await and dereference it as *remote document* using `LoadDocumentCallback`, passing input for url,
   and the `extractAllScripts` option from options for `extractAllScripts`.
4. Set *expanded input* to the result of
   using the `expand()` method
   using either *remote document* or input if there is no *remote document* for input,
   and options, with `ordered` set to `false`, and `extractAllScripts` defaulting to `false`.
5. Set *context base* to the `documentUrl` from *remote document*, if available, otherwise to the `base` option
   from options.
6. If context is a [map](https://infra.spec.whatwg.org/#ordered-map) having an `@context` [entry](https://infra.spec.whatwg.org/#map-entry),
   set *context* to that [entry's](https://infra.spec.whatwg.org/#map-entry) value,
   otherwise to context.
7. Initialize *active context* to the result of the §4.1 Context Processing Algorithm passing a new empty [context](https://www.w3.org/TR/json-ld11/#dfn-context) as *active context* *context* as *local context*,
   and *context base* as *base URL*.
8. Set base IRI in *active context* to the `base` option from options, if set;
   otherwise, if the `compactToRelative` option is **true**,
   to the IRI of the currently being processed document, if available;
   otherwise to `null`.
9. Set *compacted output* to the result of using the §6.1 Compaction Algorithm,
   using [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context), `null` for *active property*, *expanded input* as *element*,
   and the `compactArrays` and `ordered` flags from options.
   1. If *compacted output* is an empty [array](https://infra.spec.whatwg.org/#list),
      replace it with a new [map](https://infra.spec.whatwg.org/#ordered-map).
   2. Otherwise, if *compacted output* is an [array](https://infra.spec.whatwg.org/#list),
      replace it with a new [map](https://infra.spec.whatwg.org/#ordered-map) with a single [entry](https://infra.spec.whatwg.org/#map-entry) whose key is the result of IRI compacting `@graph` and value is *compacted output*.
   3. If context was not `null`,
      add an `@context` [entry](https://infra.spec.whatwg.org/#map-entry) to *compacted output* and set its value
      to the provided *context*.
10. Resolve the *promise* with *compacted output* transforming *compacted output* from the internal representation to a JSON serialization.

*input*

The [map](https://infra.spec.whatwg.org/#ordered-map),
array of [maps](https://infra.spec.whatwg.org/#ordered-map) to perform the compaction upon,
or an [IRI](https://tools.ietf.org/html/rfc3987#section-2) referencing the JSON-LD document to compact.

*context*

The context to use when compacting the input;
it can be specified by using a [map](https://infra.spec.whatwg.org/#ordered-map),
an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
or an array consisting of [maps](https://infra.spec.whatwg.org/#ordered-map) and [IRI](https://tools.ietf.org/html/rfc3987#section-2)s.

*options*

A set of options to configure the algorithms.
This allows, e.g., to set the input document's base [IRI](https://tools.ietf.org/html/rfc3987#section-2). The `JsonLdOptions` type defines default option values.

*`expand()`*

Expands (§2.1) the given input according to the steps in the §5.1 Expansion Algorithm:

1. Create a new [`Promise`](https://heycam.github.io/webidl/#idl-promise) *promise* and return it.
   The following steps are then deferred.

2. If the provided input is a `RemoteDocument`,
   initialize *remote document* to input.

3. Otherwise, if the provided input is a [string](https://infra.spec.whatwg.org/#javascript-string) representing the [IRI](https://tools.ietf.org/html/rfc3987#section-2) of a remote document, await and dereference it as *remote document* using `LoadDocumentCallback`, passing input for url,
   the `extractAllScripts` option from options for `extractAllScripts`.

4. If `document` from *remote document* is a [string](https://infra.spec.whatwg.org/#javascript-string), transform into the internal representation.
   If `document` cannot be transformed to the internal representation,
   reject *promise* passing a `loading document failed` error.

5. Initialize a new empty *active context*.
   The base IRI and original base URL of the *active context* is set to the `documentUrl` from *remote document*, if available;
   otherwise to the `base` option from options.
   If set, the `base` option from options overrides the base IRI.

6. If the `expandContext` option in options is set,
   update the *active context* using the §4.1 Context Processing Algorithm,
   passing the `expandContext` as *local context* and the original base URL from *active context* as *base URL*.
   If `expandContext` is a [map](https://infra.spec.whatwg.org/#ordered-map) having an `@context` [entry](https://infra.spec.whatwg.org/#map-entry),
   pass that [entry's](https://infra.spec.whatwg.org/#map-entry) value instead for *local context*.

7. If *remote document* has a `contextUrl`,
   update the *active context* using the §4.1 Context Processing Algorithm,
   passing the `contextUrl` as *local context*,
   and `contextUrl` as *base URL*.

8. Set *expanded output* to the result of using the §5.1 Expansion Algorithm,
   passing the *active context*, `document` from *remote document* or input if there is no *remote document* as *element*, `null` as *active property*, `documentUrl` as *base URL*, if available,
   otherwise to the `base` option
   from options,
   and the `frameExpansion` and and `ordered` flags from options.
   > **Note:**
   >
   > > **Note:**
   > >
   > > Note
   >
   > If there is no *remote document*,
   > then input is
   > a `JsonLdRecord` or a `sequence` of JsonLdRecords, which are implicitly already in the internal representation.

   1. If *expanded output* is a [map](https://infra.spec.whatwg.org/#ordered-map) that contains only an `@graph` [entry](https://infra.spec.whatwg.org/#map-entry),
      set *expanded output* that value.
   2. If *expanded output* is `null`,
      set *expanded output* to an empty [array](https://infra.spec.whatwg.org/#list).
   3. If *expanded output* is not an [array](https://infra.spec.whatwg.org/#list),
      set *expanded output* to an [array](https://infra.spec.whatwg.org/#list) containing only *expanded output*.

9. Resolve the *promise* with *expanded output* transforming *expanded output* from the internal representation to a JSON serialization.

*input*

The [map](https://infra.spec.whatwg.org/#ordered-map),
or array of [maps](https://infra.spec.whatwg.org/#ordered-map) to perform the expansion upon,
or an [IRI](https://tools.ietf.org/html/rfc3987#section-2) referencing the [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) to expand.

*options*

A set of options to configure the used algorithms.
This allows, e.g., to set the input document's [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri). The `JsonLdOptions` type defines default option values.

*`flatten()`*

Flattens (§2.3) the given input and optionally compacts it using the provided context according to the steps in the §7.1 Flattening Algorithm:

1. Create a new [`Promise`](https://heycam.github.io/webidl/#idl-promise) *promise* and return it.
   The following steps are then deferred.
2. If the provided input is a `RemoteDocument`,
   initialize *remote document* to input.
3. Otherwise, if the provided input is a [string](https://infra.spec.whatwg.org/#javascript-string) representing the [IRI](https://tools.ietf.org/html/rfc3987#section-2) of a remote document, await and dereference it as *remote document* using `LoadDocumentCallback`, passing input for url,
   and the `extractAllScripts` option from options for `extractAllScripts`.
4. Set *expanded input* to the result of
   using the `expand()` method
   using either *remote document* or input if there is no *remote document* for input,
   and options with `ordered` set to `false`.
5. Initialize an empty *identifier map*.
6. Set *flattened output* to the result of using the §7.1 Flattening Algorithm,
   passing *expanded input* as *element*, and the `ordered` flag
   from options.
   1. If context is not `null`,
      set *flattened output* to the result of
      using the `compact()` method
      using *flattened output* for input, context,
      and options.
      Set the base IRI in *active context* to the `base` option
      from options, if set;
      otherwise, if the `compactToRelative` option is **true**,
      to the IRI of the currently being processed document, if available;
      otherwise to `null`.
7. Resolve the *promise* with *flattened output* transforming *flattened output* from the internal representation to a JSON serialization,
   if necessary.

*input*

The [map](https://infra.spec.whatwg.org/#ordered-map),
or array of [maps](https://infra.spec.whatwg.org/#ordered-map),
or an [IRI](https://tools.ietf.org/html/rfc3987#section-2) referencing the JSON-LD document to flatten.

*context*

The context to use when compacting the flattened *expanded input*;
it can be specified by using a [map](https://infra.spec.whatwg.org/#ordered-map),
an [IRI](https://tools.ietf.org/html/rfc3987#section-2), or an array consisting of [maps](https://infra.spec.whatwg.org/#ordered-map) and [IRI](https://tools.ietf.org/html/rfc3987#section-2)s.
If `null`, the result will not be compacted but kept in expanded form.

*options*

A set of options to configure the used algorithms.
This allows, e.g., to set the input document's [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri). The `JsonLdOptions` type defines default option values.

*`fromRdf()`*

Transforms the given input into a [JSON-LD document](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document) in expanded form according to the steps in the §8.4 Serialize RDF as JSON-LD Algorithm:
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This interface does not define a means of creating an `RdfDataset` from an arbitrary input, other than the `toRdf()` method.

1. Create a new [`Promise`](https://heycam.github.io/webidl/#idl-promise) *promise* and return it.
   The following steps are then deferred.
2. Set *expanded result* to the result of invoking the §8.4 Serialize RDF as JSON-LD Algorithm method
   using dataset and options.
3. Resolve the *promise* with *expanded result* transforming *expanded result* from the internal representation to a JSON serialization.

*input*

The [map](https://infra.spec.whatwg.org/#ordered-map),
or array of [maps](https://infra.spec.whatwg.org/#ordered-map),
or an [IRI](https://tools.ietf.org/html/rfc3987#section-2) referencing the JSON-LD document to flatten.

*options*

A set of options to configure the used algorithms.
This allows, e.g., to set the input document's [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri). The `JsonLdOptions` type defines default option values.

*`toRdf()`*

Transforms the given input into an `RdfDataset` according to the steps in the §8.1 Deserialize JSON-LD to RDF Algorithm:

1. Create a new [`Promise`](https://heycam.github.io/webidl/#idl-promise) *promise* and return it.
   The following steps are then deferred.

2. Set *expanded input* to the result of using the `expand()` method
   using input and options with `ordered` set to `false`.

3. Create a new `RdfDataset` *dataset*.

4. Create a new [map](https://infra.spec.whatwg.org/#ordered-map) *node map*.

5. Invoke the Node Map Generation algorithm (§7.2),
   passing *expanded input* as *element* and *node map*.

6. Invoke the §8.1 Deserialize JSON-LD to RDF Algorithm passing *node map*, *dataset*,
   and the `produceGeneralizedRdf` flag from options.
   > **Note:**
   >
   > > **Note:**
   > >
   > > Note
   >
   > The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
   > and may be removed in a future version of JSON-LD,
   > as is the support for [generalized RDF Datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-generalized-rdf-dataset) and thus the `produceGeneralizedRdf` option may be also be removed.

7. Resolve the *promise* with *dataset*.

*input*

The [map](https://infra.spec.whatwg.org/#ordered-map),
or array of [maps](https://infra.spec.whatwg.org/#ordered-map),
or an [IRI](https://tools.ietf.org/html/rfc3987#section-2) referencing the JSON-LD document to flatten.

*options*

A set of options to configure the used algorithms.
This allows, e.g., to set the input document's [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri). The `JsonLdOptions` type defines default option values.

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
which can be dereferenced to retrieve a valid JSON document, or an already dereferenced `RemoteDocument`.

When the value is a `JsonLdRecord` or sequence of JsonLdRecords,
the values are taken as their equivalent internal representation values,
where a `JsonLdRecord` is equivalent to a [map](https://infra.spec.whatwg.org/#ordered-map),
and a sequence of JsonLdRecords is equivalent to an [array](https://infra.spec.whatwg.org/#list) of [maps](https://infra.spec.whatwg.org/#ordered-map). The [map entries](https://infra.spec.whatwg.org/#map-entry) are converted to their equivalents
in [INFRA].

```
WebIDLtypedef (JsonLdRecord or sequence<(JsonLdRecord or USVString)> or USVString) JsonLdContext;
```

The *`JsonLdContext`* interface is used to refer to a value
that may be a `JsonLdRecord`,
a `sequence` of JsonLdRecords,
or a [string](https://infra.spec.whatwg.org/#javascript-string) representing an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
which can be dereferenced to retrieve a valid JSON document.

When the value is a `JsonLdRecord` or sequence of JsonLdRecords,
the values are taken as their equivalent internal representation values,
where a `JsonLdRecord` is equivalent to a [map](https://infra.spec.whatwg.org/#ordered-map),
and a sequence of JsonLdRecords is equivalent to an [array](https://infra.spec.whatwg.org/#list) of [maps](https://infra.spec.whatwg.org/#ordered-map). The [map entries](https://infra.spec.whatwg.org/#map-entry) are converted to their equivalents
in [INFRA].

### 9.2 RDF Dataset Interfaces

The *`RdfDataset`* interface describes operations on an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) used by the `fromRdf()` and `toRdf()` methods
in the `JsonLdProcessor` interface.
The interface may be used for constructing a new [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset),
which has a [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) accessible via the `defaultGraph` attribute.

```
WebIDL[Exposed=JsonLd]
interface RdfDataset {
  constructor();
  readonly attribute RdfGraph defaultGraph;
  void add(USVString graphName, RdfGraph graph);
  iterable<USVString?, RdfGraph>;
};
```

*`add()`*

Adds an `RdfGraph` and its associated [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name) to the `RdfDataset`.
Used by the §8.1 Deserialize JSON-LD to RDF Algorithm.

*graphName*

The [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name) associated with [graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph). `graphName` *MUST* be a well-formed [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).

*graph*

The `RdfGraph` to add to the `RdfDataset`.

*`defaultGraph`*

Provides access to the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) associated with the [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset).

*`iterable`*

The [value pairs to iterate over](https://heycam.github.io/webidl/#dfn-value-pairs-to-iterate-over) are the list of *graph name*-*graph* pairs,
with the *graph name* being `null` (for the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph)),
an [IRI](https://tools.ietf.org/html/rfc3987#section-2),
or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) and graph an `RdfGraph` instance.

The *`RdfGraph`* interface describes operations on an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) used by the `fromRdf()` and `toRdf()` methods
in the `JsonLdProcessor` interface.
The interface may be used for constructing a new [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph),
which is composed of zero or more `RdfTriple` instances.

```
WebIDL[Exposed=JsonLd]
interface RdfGraph {
  constructor();
  void add(RdfTriple triple);
  iterable<RdfTriple>;
};
```

*`add()`*

Adds an `RdfTriple` to the `RdfGraph`.
Used by the §8.1 Deserialize JSON-LD to RDF Algorithm.

*triple*

The `RdfTriple` to add to the `RdfGraph`.

*`iterable`*

A [value iterator](https://heycam.github.io/webidl/#dfn-value-iterator) over the `RdfTriple` instances associated with the graph.
Note that a given `RdfTriple` instance may appear in more than one graph
within a particular `RdfDataset` instance.

The *`RdfTriple`* interface describes an [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple).

```
WebIDL[Exposed=JsonLd]
interface RdfTriple {
  constructor();
  readonly attribute USVString subject;
  readonly attribute USVString predicate;
  readonly attribute (USVString or RdfLiteral) _object;
};
```

*`subject`*

An absolute [IRI](https://tools.ietf.org/html/rfc3987#section-2) or [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) denoting the [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) of the [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple).

*`predicate`*

An absolute [IRI](https://tools.ietf.org/html/rfc3987#section-2) denoting the [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate) of the [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple).
If used to represent a [Generalized RDF Dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-generalized-rdf-dataset),
it may also be a [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier).

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
> and may be removed in a future version of JSON-LD, as is the support for [generalized RDF Datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-generalized-rdf-dataset).

*`object`*

An absolute [IRI](https://tools.ietf.org/html/rfc3987#section-2), [blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier), or [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) denoting the [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) of the [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple).

The *`RdfLiteral`* interface describes an [RDF Literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal).

```
WebIDL[Exposed=JsonLd]
interface RdfLiteral {
  constructor();
  readonly attribute USVString value;
  readonly attribute USVString datatype;
  readonly attribute USVString? language;
};
```

*`value`*

The lexical value of the [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal).

*`datatype`*

An absolute [IRI](https://tools.ietf.org/html/rfc3987#section-2) denoting the [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri) of the [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal).
If the value is `rdf:langString`, `language` *MUST* be specified.

*`language`*

An optional [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) as defined by [BCP47].
If this value is specified, `datatype` *MUST* be `rdf:langString`.

### 9.3 The JsonLdOptions Type

The *`JsonLdOptions`* type is used to pass various options to the `JsonLdProcessor` methods.

```
WebIDLdictionary JsonLdOptions {
  USVString?             base = null;
  boolean                compactArrays = true;
  boolean                compactToRelative = true;
  LoadDocumentCallback?  documentLoader = null;
  (JsonLdRecord? or USVString) expandContext = null;
  boolean                extractAllScripts = false;
  boolean                frameExpansion = false;
  boolean                ordered = false;
  USVString              processingMode = "json-ld-1.1";
  boolean                produceGeneralizedRdf = true;
  USVString?             rdfDirection = null;
  boolean                useNativeTypes = false;
  boolean                useRdfType = false;
};
```

*`base`*

The base IRI to use when expanding or compacting the document.
If set, this overrides the input document's IRI.

*`compactArrays`*

If set to `true`, the JSON-LD processor replaces arrays
with just one element with that element during compaction.
If set to `false`,
all arrays will remain arrays even if they have just one element.

*`compactToRelative`*

Determines if IRIs are compacted
relative to the `base` option
or document location when compacting.

*`documentLoader`*

The callback of the loader to be used to retrieve remote documents and contexts,
implementing the `LoadDocumentCallback`.
If specified, it is used to retrieve remote documents and contexts;
otherwise, if not specified, the processor's built-in loader is used.

*`expandContext`*

A context that is used to initialize the active context when expanding a document.

*`extractAllScripts`*

If set to `true`,
when extracting JSON-LD script elements from HTML,
unless a specific [fragment identifier](https://tools.ietf.org/html/rfc3986#section-3.5) is targeted,
extracts all encountered JSON-LD script elements using an [array](https://infra.spec.whatwg.org/#list) form, if necessary.

*`frameExpansion`*

Enables special frame processing rules for the §5.1 Expansion Algorithm.

Enables special rules for the §8.4 Serialize RDF as JSON-LD Algorithm to use JSON-LD native types as values, where possible.

*`ordered`*

If set to `true`,
certain algorithm processing steps where indicated are ordered lexicographically.
If `false`, order is not considered in processing.

*`processingMode`*

Sets the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode).
If set to `json-ld-1.0` or `json-ld-1.1`,
the implementation must produce exactly the same results as the
algorithms defined in this specification.
If set to another value,
the JSON-LD processor is allowed to extend or modify the algorithms defined in this specification
to enable application-specific optimizations.
The definition of such optimizations is beyond the scope of this specification
and thus not defined.
Consequently, different implementations may implement different optimizations.
Developers must not define modes beginning with `json-ld` as they are reserved for future versions of this specification.

*`produceGeneralizedRdf`*

If set to `true`, the JSON-LD processor may emit [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) for [triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) [predicates](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate),
otherwise they will be omitted. *[Generalized RDF Datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-generalized-rdf-dataset)* are defined in [RDF11-CONCEPTS].

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
> and may be removed in a future version of JSON-LD,
> as is the support for [generalized RDF Datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-generalized-rdf-dataset) and thus the `produceGeneralizedRdf` option may be also be removed.

*`rdfDirection`*

Determines how [value objects](https://www.w3.org/TR/json-ld11/#dfn-value-object) containing a [base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) are transformed to and from RDF.

- If set to `i18n-datatype`, an [RDF literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) is generated using a datatype IRI based on `https://www.w3.org/ns/i18n#` with both the [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) (if present)
  and [base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) encoded.
  When transforming from RDF, this datatype is decoded to create a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) containing `@language` (if present) and `@direction`.
- If set to `compound-literal`, a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) is emitted instead of a [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal),
  where the blank node is the subject of `rdf:value`, `rdf:direction`, and `rdf:language` (if present)
  properties.
  When transforming from RDF, this object is decoded to create a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) containing `@language` (if present) and `@direction`.

*`useNativeTypes`*

Causes the §8.4 Serialize RDF as JSON-LD Algorithm to use native JSON values in [value objects](https://www.w3.org/TR/json-ld11/#dfn-value-object) avoiding the need for an explicitly `@type`.

*`useRdfType`*

Enables special rules for the §8.4 Serialize RDF as JSON-LD Algorithm causing `rdf:type` properties to be kept as [IRIs](https://tools.ietf.org/html/rfc3987#section-2) in the output, rather than use `@type`.

### 9.4 Remote Document and Context Retrieval

Users of an API implementation can utilize a callback to control how
remote documents and contexts are retrieved.
This section details the parameters of that callback
and the data structure used to return the retrieved context.

#### 9.4.1 LoadDocumentCallback

The *`LoadDocumentCallback`* defines a callback that custom document loaders
have to implement to be used to retrieve remote documents and contexts.
The callback returns a [`Promise`](https://heycam.github.io/webidl/#idl-promise) resolving to a `RemoteDocument`.
On failure, the [`Promise`](https://heycam.github.io/webidl/#idl-promise) with a `JsonLdError` having an appropriate error `code`.

```
WebIDLcallback LoadDocumentCallback = Promise<RemoteDocument> (
  USVString url,
  optional LoadDocumentOptions? options
);
```

*url*

The URL of the remote document or context to load.

*options*

A set of options to determine
the behavior of the callback. See § 9.4.2 LoadDocumentOptions (§9.4.2).

The following algorithm describes the default callback and places
requirements on implementations of the callback.

1. Create a new [`Promise`](https://heycam.github.io/webidl/#idl-promise) *promise* and return it.
   The following steps are then deferred.

2. Set *document* to the body retrieved from
   the resource identified by url,
   or by otherwise locating a resource associated with url.
   When requesting remote documents the request *MUST* prefer [Content-Type](https://tools.ietf.org/html/rfc2045#section-5) `application/ld+json` followed by `application/json`.

   If `requestProfile` is set,
   it *MUST* be added as a profile on `application/ld+json`.

   Processors *MAY* include other media types using a `+json` suffix as defined in [RFC6839].

3. Set *documentUrl* to the location of the retrieved resource
   considering redirections (exclusive of HTTP status `303` "See Other" redirects
   as discussed in [cooluris]).

4. If the retrieved resource's [Content-Type](https://tools.ietf.org/html/rfc2045#section-5) is not `application/json` nor any media type with a `+json` suffix as defined in [RFC6839],
   and the response has an HTTP Link Header [RFC8288] using the `alternate` link relation
   with type `application/ld+json`,
   set *url* to the associated `href` relative to the previous *url* and restart the algorithm from step 2.

5. If the retrieved resource's [Content-Type](https://tools.ietf.org/html/rfc2045#section-5) is `application/json` or any media type with a `+json` suffix as defined in [RFC6839]
   except `application/ld+json`,
   and the response has an HTTP Link Header [RFC8288] using the `http://www.w3.org/ns/json-ld#context` link relation,
   set *contextUrl* to the associated `href`.

   If multiple HTTP Link Headers using the `http://www.w3.org/ns/json-ld#context` link relation are found,
   the *promise* is rejected with a `JsonLdError` whose `code` is set to `multiple context link headers` and processing is terminated.

   Processors *MAY* transform *document* to the internal representation.
   > **Note:**
   >
   > > **Note:**
   > >
   > > Note
   >
   > The HTTP Link Header is ignored for documents served as `application/ld+json`, `text/html`, or `application/xhtml+xml`.

6. Otherwise, the retrieved document's [Content-Type](https://tools.ietf.org/html/rfc2045#section-5) is neither `application/json`, `application/ld+json`,
   nor any other media type using a `+json` suffix as defined in [RFC6839].
   Reject the *promise* passing a `loading document failed` error.

7. Create a new `RemoteDocument` *remote document* using *url* as `documentUrl`, *document* as `document`,
   the returned [Content-Type](https://tools.ietf.org/html/rfc2045#section-5) (without parameters) as `contentType`,
   any returned `profile` parameter, or `null` as `profile`,
   and *contextUrl*, or `null` as `contextUrl`.

8. Resolve the *promise* with *remote document*.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> A custom `LoadDocumentCallback` set via the `documentLoader` option might be used
> to maintain a local cache of well-known context documents or to implement
> application-specific URL protocols.

#### 9.4.2 LoadDocumentOptions

The *`LoadDocumentOptions`* type is used to pass various options
to the `LoadDocumentCallback`.

```
WebIDLdictionary LoadDocumentOptions {
  boolean  extractAllScripts = false;
  USVString profile = null;
  (USVString or sequence<USVString>) requestProfile = null;
};
```

*`extractAllScripts`*

If set to `true`,
when extracting JSON-LD script elements from HTML,
unless a specific [fragment identifier](https://tools.ietf.org/html/rfc3986#section-3.5) is targeted,
extracts all encountered JSON-LD script elements using an [array](https://infra.spec.whatwg.org/#list) form, if necessary.

*`profile`*

When the resulting `contentType` is `text/html` or `application/xhtml+xml`,
this option determines the profile to use for selecting JSON-LD script elements.

*`requestProfile`*

One or more IRIs to use in the request as a `profile` parameter.
(See [IANA Considerations](https://www.w3.org/TR/json-ld11/#iana-considerations) in [JSON-LD11]).

#### 9.4.3 RemoteDocument

The *`RemoteDocument`* type is used by a `LoadDocumentCallback` to return information about a remote document or context.

```
WebIDL[Exposed=JsonLd]
interface RemoteDocument {
  constructor();
  readonly attribute USVString contentType;
  readonly attribute USVString contextUrl;
  attribute any document;
  readonly attribute USVString documentUrl;
  readonly attribute USVString profile;
};
```

*`contentType`*

The *[Content-Type](https://tools.ietf.org/html/rfc2045#section-5)* of the loaded document, exclusive of any optional parameters.

*`contextUrl`*

If available, the value of the HTTP Link Header [RFC8288]
using the `http://www.w3.org/ns/json-ld#context` link relation
in the response.
If the response's [Content-Type](https://tools.ietf.org/html/rfc2045#section-5) is `application/ld+json`,
the HTTP Link Header is ignored.
If multiple HTTP Link Headers using the `http://www.w3.org/ns/json-ld#context` link relation are found,
the [`Promise`](https://heycam.github.io/webidl/#idl-promise) of the `LoadDocumentCallback` is rejected
with a `JsonLdError` whose `code` is set to `multiple context link headers`.

*`document`*

The retrieved document.
This can either be the raw payload or the already parsed document.

*`documentUrl`*

The final URL of the loaded document.
This is important to handle HTTP redirects properly.

*`profile`*

The value of any `profile` parameter
retrieved as part of the original `contentType`.

### 9.5 HTML Content Algorithms
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This section describes optional features available
> with a `documentLoader` supporting HTML script extraction.

Implementations of a `documentLoader` *MAY* support extracting JSON-LD from [script elements](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element) contained within an HTML [HTML] document.
This section describes the normative behavior of such processors.
Such a processor supports *HTML script extraction*.

#### 9.5.1 Process HTML

This sections describe an extension to the algorithm specified
in `LoadDocumentCallback` to support extracting JSON-LD from HTML.

Step 2 is updated to add the following: A processor supporting HTML script extraction *MUST* include `text/html` at any preference level
and *MAY* include `application/xhtml+xml` at any preference level,
unless `requestProfile` is `http://www.w3.org/ns/json-ld#context`.

After step 5, add the following processing step:
Otherwise, if the retrieved resource's [Content-Type](https://tools.ietf.org/html/rfc2045#section-5) is either `text/html` or `application/xhtml+xml`:

1. Set *documentUrl* to the [Document Base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-url) of url, as defined in [HTML],
   using the existing *documentUrl* as the document's URL.

2. If the url parameter
   contains a [fragment identifier](https://tools.ietf.org/html/rfc3986#section-3.5),
   set *source* to the [textContent](https://dom.spec.whatwg.org/#dom-node-textcontent) of the [script element](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element) in *document* having an [id attribute](https://html.spec.whatwg.org/multipage/dom.html#the-id-attribute) that matches the fragment identifier, after decoding [percent encoded sequences](https://tools.ietf.org/html/rfc3986#section-2.1).

   If no such element is found,
   or the located element is not a JSON-LD script element,
   the *promise* is rejected with a `JsonLdError` whose `code` is set to `loading document failed` and processing is terminated.

3. Otherwise, if the `profile` option is specified,
   set *source* to the result of transforming the [textContent](https://dom.spec.whatwg.org/#dom-node-textcontent) of the first [script element](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element) in *document* having an [type attribute](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-type) of `application/ld+json` along with the value of the `profile` option, if found.

4. If *source* is still undefined and the `extractAllScripts` option is not present, or `false`,
   set *source* to the [textContent](https://dom.spec.whatwg.org/#dom-node-textcontent) of the first JSON-LD script element in *document*.

   If no such element is found,
   or the located element is not a JSON-LD script element,
   the *promise* is rejected with a `JsonLdError` whose `code` is set to `loading document failed` and processing is terminated.

5. If *source* is defined,
   set *document* to the result of the §9.5.2 Extract Script Content Algorithm,
   using *source*, rejecting *promise* with a `JsonLdError` whose code set from the result, if an error is detected
   and processing is terminated.

6. Otherwise, *source* is undefined.

   1. If the `extractAllScripts` option is not present, or `false`,
      the *promise* is rejected with a `JsonLdError` whose `code` is set to `loading document failed` and processing is terminated.
   2. Otherwise, the `extractAllScripts` option is `true`.
      Set *document* to a new empty [array](https://infra.spec.whatwg.org/#list).
      For each JSON-LD script element in *input*:
      1. Set *source* to its [textContent](https://dom.spec.whatwg.org/#dom-node-textcontent).
      2. Set *script content* to the result of the §9.5.2 Extract Script Content Algorithm,
         using *source*, rejecting *promise* with a `JsonLdError` whose code set from the result, if an error is detected
         and processing is terminated.
      3. If *script content* is an [array](https://infra.spec.whatwg.org/#list), merge it to the end of *document*.
      4. Otherwise, append *script content* to *document*.

#### 9.5.2 Extract Script Content Algorithm

The algorithm extracts the text content a JSON-LD script element into a [map](https://infra.spec.whatwg.org/#ordered-map) or [array](https://infra.spec.whatwg.org/#list) of [maps](https://infra.spec.whatwg.org/#ordered-map).
A *JSON-LD script element* is a [script element](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element) within an HTML [HTML] document with the [type attribute](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-type) set to `application/ld+json`.

The algorithm takes a single required input variable: *source*,
the [textContent](https://dom.spec.whatwg.org/#dom-node-textcontent) of an HTML [script element](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element).

1. If *source* is not a valid JSON document,
   an `invalid script element` has been detected, and processing is aborted.
2. Return the result of transforming *source* into the internal representation.

### 9.6 Error Handling

This section describes the datatype definitions
used within the JSON-LD API for error handling.

#### 9.6.1 JsonLdError

The *`JsonLdError`* type is used to report processing errors.

```
WebIDLdictionary JsonLdError {
  JsonLdErrorCode code;
  USVString?      message = null;
};
```

*`code`*

A string representing the particular error type,
as described in the various algorithms in this document.

*`message`*

An optional error message containing additional debugging information.
The specific contents of error messages are outside the scope of this specification.

#### 9.6.2 JsonLdErrorCode

The *`JsonLdErrorCode`* represents the collection of valid JSON-LD error codes.

```
WebIDLenum JsonLdErrorCode {
    "colliding keywords",
    "conflicting indexes",
    "context overflow",
    "cyclic IRI mapping",
    "invalid @id value",
    "invalid @import value",
    "invalid @included value",
    "invalid @index value",
    "invalid @nest value",
    "invalid @prefix value",
    "invalid @propagate value",
    "invalid @protected value",
    "invalid @reverse value",
    "invalid @version value",
    "invalid base direction",
    "invalid base IRI",
    "invalid container mapping",
    "invalid context entry",
    "invalid context nullification",
    "invalid default language",
    "invalid IRI mapping",
    "invalid JSON literal",
    "invalid keyword alias",
    "invalid language map value",
    "invalid language mapping",
    "invalid language-tagged string",
    "invalid language-tagged value",
    "invalid local context",
    "invalid remote context",
    "invalid reverse property map",
    "invalid reverse property value",
    "invalid reverse property",
    "invalid scoped context",
    "invalid script element",
    "invalid set or list object",
    "invalid term definition",
    "invalid type mapping",
    "invalid type value",
    "invalid typed value",
    "invalid value object value",
    "invalid value object",
    "invalid vocab mapping",
    "IRI confused with prefix",
    "keyword redefinition",
    "loading document failed",
    "loading remote context failed",
    "multiple context link headers",
    "processing mode conflict",
    "protected term redefinition"
};
```

*`colliding keywords`*

Two [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) which expand to the same keyword have been detected.
This might occur if a [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) and an alias thereof
are used at the same time.

*`conflicting indexes`*

Multiple conflicting indexes have been found for the same node.

*`context overflow`*

Maximum number of `@context` URLs exceeded.

*`cyclic IRI mapping`*

A cycle in IRI mappings has been detected.

*`invalid @id value`*

An `@id` [entry](https://infra.spec.whatwg.org/#map-entry) was encountered whose value was not a [string](https://infra.spec.whatwg.org/#javascript-string).

*`invalid @import value`*

An invalid value for `@import` has been found.

*`invalid @included value`*

An [included block](https://www.w3.org/TR/json-ld11/#dfn-included-block) contains an invalid value.

*`invalid @index value`*

An `@index` [entry](https://infra.spec.whatwg.org/#map-entry) was encountered whose value was not a [string](https://infra.spec.whatwg.org/#javascript-string).

*`invalid @nest value`*

An invalid value for `@nest` has been found.

*`invalid @prefix value`*

An invalid value for `@prefix` has been found.

*`invalid @propagate value`*

An invalid value for `@propagate` has been found.

*`invalid @protected value`*

An invalid value for `@protected` has been found.

*`invalid @reverse value`*

An invalid value for an `@reverse` [entry](https://infra.spec.whatwg.org/#map-entry) has been detected,
i.e., the value was not a [map](https://infra.spec.whatwg.org/#ordered-map).

*`invalid @version value`*

The `@version` [entry](https://infra.spec.whatwg.org/#map-entry) was used in a [context](https://www.w3.org/TR/json-ld11/#dfn-context) with an out of range value.

*`invalid base direction`*

The value of `@direction` is not `"ltr"`, `"rtl"`,
or `null` and thus invalid.

*`invalid base IRI`*

An invalid [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri) has been detected, i.e.,
it is neither an [IRI](https://tools.ietf.org/html/rfc3987#section-2) nor `null`.

*`invalid container mapping`*

An `@container` [entry](https://infra.spec.whatwg.org/#map-entry) was encountered
whose value was not one of the following [strings](https://infra.spec.whatwg.org/#javascript-string): `@list`, `@set`, `@language`, `@index`, `@id`, `@graph`, or `@type`.

*`invalid context entry`*

An [entry](https://infra.spec.whatwg.org/#map-entry) in a context is invalid due to processing mode incompatibility.

*`invalid context nullification`*

An attempt was made to nullify a context
containing protected [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition).

*`invalid default language`*

The value of the [default language](https://www.w3.org/TR/json-ld11/#dfn-default-language) is not a [string](https://infra.spec.whatwg.org/#javascript-string) or `null` and thus invalid.

*`invalid IRI mapping`*

A [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) contains a [term](https://www.w3.org/TR/json-ld11/#dfn-term) that has an invalid or missing IRI mapping.

*`invalid JSON literal`*

An invalid JSON literal was detected.

*`invalid keyword alias`*

An invalid [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) alias definition has been encountered.

*`invalid language map value`*

An invalid value in a [language map](https://www.w3.org/TR/json-ld11/#dfn-language-map) has been detected.
It *MUST* be a [string](https://infra.spec.whatwg.org/#javascript-string) or an [array](https://infra.spec.whatwg.org/#list) of [strings](https://infra.spec.whatwg.org/#javascript-string).

*`invalid language mapping`*

An `@language` [entry](https://infra.spec.whatwg.org/#map-entry) in a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) was encountered whose value was neither a [string](https://infra.spec.whatwg.org/#javascript-string) nor `null` and thus invalid.

*`invalid language-tagged string`*

A [language-tagged string](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string) with an invalid language value was detected.

*`invalid language-tagged value`*

A [number](https://tc39.es/ecma262/#sec-terms-and-definitions-number-value), `true`, or `false` with an associated [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) was detected.

*`invalid local context`*

In invalid [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) was detected.

*`invalid remote context`*

No valid context document has been found for a referenced remote context.

*`invalid reverse property`*

An invalid reverse property definition has been detected.

*`invalid reverse property map`*

An invalid reverse property map has been detected.
No [keywords](https://www.w3.org/TR/json-ld11/#dfn-keyword) apart from `@context` are allowed in reverse property maps.

*`invalid reverse property value`*

An invalid value for a reverse property has been detected.
The value of an inverse property must be a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).

*`invalid scoped context`*

The [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context) defined within a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) is invalid.

*`invalid script element`*

A [script element](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element) in HTML input
which is the target of a [fragment identifier](https://tools.ietf.org/html/rfc3986#section-3.5) does not have an appropriate [type attribute](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-type).

*`invalid set or list object`*

A [set object](https://www.w3.org/TR/json-ld11/#dfn-set-object) or [list object](https://www.w3.org/TR/json-ld11/#dfn-list-object) with disallowed [entries](https://infra.spec.whatwg.org/#map-entry) has been detected.

*`invalid term definition`*

An invalid [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) has been detected.

*`invalid type mapping`*

An `@type` [entry](https://infra.spec.whatwg.org/#map-entry) in a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) was encountered whose value could not be expanded to an [IRI](https://tools.ietf.org/html/rfc3987#section-2).

*`invalid type value`*

An invalid value for an `@type` [entry](https://infra.spec.whatwg.org/#map-entry) has been detected,
i.e., the value was neither a [string](https://infra.spec.whatwg.org/#javascript-string) nor an [array](https://infra.spec.whatwg.org/#list) of [strings](https://infra.spec.whatwg.org/#javascript-string).

*`invalid typed value`*

A [typed value](https://www.w3.org/TR/json-ld11/#dfn-typed-value) with an invalid type was detected.

*`invalid value object`*

A [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) with disallowed [entries](https://infra.spec.whatwg.org/#map-entry) has been detected.

*`invalid value object value`*

An invalid value for the `@value` [entry](https://infra.spec.whatwg.org/#map-entry) of a [value object](https://www.w3.org/TR/json-ld11/#dfn-value-object) has been detected,
i.e., it is neither a [scalar](https://infra.spec.whatwg.org/#primitive-data-types) nor `null`.

*`invalid vocab mapping`*

An invalid [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping) has been detected,
i.e., it is neither an [IRI](https://tools.ietf.org/html/rfc3987#section-2) nor `null`.

*`IRI confused with prefix`*

When compacting an [IRI](https://tools.ietf.org/html/rfc3987#section-2) would result in an [IRI](https://tools.ietf.org/html/rfc3987#section-2) which could be confused with a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) (because its [IRI scheme](https://tools.ietf.org/html/rfc3986#section-3.1) matches a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) and it has no [IRI authority](https://tools.ietf.org/html/rfc3986#section-3.1)).

*`keyword redefinition`*

A [keyword](https://www.w3.org/TR/json-ld11/#dfn-keyword) redefinition has been detected.

*`loading document failed`*

The document could not be loaded or parsed as JSON.

*`loading remote context failed`*

There was a problem encountered loading a remote context.

*`multiple context link headers`*

Multiple HTTP Link Headers [RFC8288]
using the `http://www.w3.org/ns/json-ld#context` link relation
have been detected.

*`processing mode conflict`*

An attempt was made to change the [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) which is incompatible with the previous specified version.

*`protected term redefinition`*

An attempt was made to redefine a protected term.

## 10. Security Considerations

See, [Security Considerations](https://www.w3.org/TR/json-ld11/#security) in [JSON-LD11].

## 11. Privacy Considerations

See, [Privacy Considerations](https://www.w3.org/TR/json-ld11/#privacy) in [JSON-LD11].

## 12. Internationalization Considerations

See, [Internationalization Considerations](https://www.w3.org/TR/json-ld11/#internationalization) in [JSON-LD11].

## A. IDL Index

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
  static Promise<JsonLdRecord> compact(
    JsonLdInput input,
    optional JsonLdContext context = null,
    optional JsonLdOptions options = {});
  static Promise<sequence<JsonLdRecord>> expand(
    JsonLdInput input,
    optional JsonLdOptions options = {});
  static Promise<JsonLdRecord> flatten(
    JsonLdInput input,
    optional JsonLdContext context = null,
    optional JsonLdOptions options = {});
  static Promise<sequence<JsonLdRecord>> fromRdf(
    RdfDataset input,
    optional JsonLdOptions options = {});
  static Promise<RdfDataset> toRdf(
    JsonLdInput input,
    optional JsonLdOptions options = {});
};

typedef record<USVString, any> JsonLdRecord;

typedef (JsonLdRecord or sequence<JsonLdRecord> or USVString or RemoteDocument) JsonLdInput;

typedef (JsonLdRecord or sequence<(JsonLdRecord or USVString)> or USVString) JsonLdContext;

[Exposed=JsonLd]
interface RdfDataset {
  constructor();
  readonly attribute RdfGraph defaultGraph;
  void add(USVString graphName, RdfGraph graph);
  iterable<USVString?, RdfGraph>;
};

[Exposed=JsonLd]
interface RdfGraph {
  constructor();
  void add(RdfTriple triple);
  iterable<RdfTriple>;
};

[Exposed=JsonLd]
interface RdfTriple {
  constructor();
  readonly attribute USVString subject;
  readonly attribute USVString predicate;
  readonly attribute (USVString or RdfLiteral) _object;
};

[Exposed=JsonLd]
interface RdfLiteral {
  constructor();
  readonly attribute USVString value;
  readonly attribute USVString datatype;
  readonly attribute USVString? language;
};

dictionary JsonLdOptions {
  USVString?             base = null;
  boolean                compactArrays = true;
  boolean                compactToRelative = true;
  LoadDocumentCallback?  documentLoader = null;
  (JsonLdRecord? or USVString) expandContext = null;
  boolean                extractAllScripts = false;
  boolean                frameExpansion = false;
  boolean                ordered = false;
  USVString              processingMode = "json-ld-1.1";
  boolean                produceGeneralizedRdf = true;
  USVString?             rdfDirection = null;
  boolean                useNativeTypes = false;
  boolean                useRdfType = false;
};

callback LoadDocumentCallback = Promise<RemoteDocument> (
  USVString url,
  optional LoadDocumentOptions? options
);

dictionary LoadDocumentOptions {
  boolean  extractAllScripts = false;
  USVString profile = null;
  (USVString or sequence<USVString>) requestProfile = null;
};

[Exposed=JsonLd]
interface RemoteDocument {
  constructor();
  readonly attribute USVString contentType;
  readonly attribute USVString contextUrl;
  attribute any document;
  readonly attribute USVString documentUrl;
  readonly attribute USVString profile;
};

dictionary JsonLdError {
  JsonLdErrorCode code;
  USVString?      message = null;
};

enum JsonLdErrorCode {
    "colliding keywords",
    "conflicting indexes",
    "context overflow",
    "cyclic IRI mapping",
    "invalid @id value",
    "invalid @import value",
    "invalid @included value",
    "invalid @index value",
    "invalid @nest value",
    "invalid @prefix value",
    "invalid @propagate value",
    "invalid @protected value",
    "invalid @reverse value",
    "invalid @version value",
    "invalid base direction",
    "invalid base IRI",
    "invalid container mapping",
    "invalid context entry",
    "invalid context nullification",
    "invalid default language",
    "invalid IRI mapping",
    "invalid JSON literal",
    "invalid keyword alias",
    "invalid language map value",
    "invalid language mapping",
    "invalid language-tagged string",
    "invalid language-tagged value",
    "invalid local context",
    "invalid remote context",
    "invalid reverse property map",
    "invalid reverse property value",
    "invalid reverse property",
    "invalid scoped context",
    "invalid script element",
    "invalid set or list object",
    "invalid term definition",
    "invalid type mapping",
    "invalid type value",
    "invalid typed value",
    "invalid value object value",
    "invalid value object",
    "invalid vocab mapping",
    "IRI confused with prefix",
    "keyword redefinition",
    "loading document failed",
    "loading remote context failed",
    "multiple context link headers",
    "processing mode conflict",
    "protected term redefinition"
};
```

## B. Open Issues

*This section is non-normative.*

The following is a list of issues open at the time of publication.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 76](https://github.com/w3c/json-ld-api/issues/76): More compact @prefix [defer-future-version](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22defer-future-version%22)
>
> More compact @prefix.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 94](https://github.com/w3c/json-ld-api/issues/94): Expansion concept "key's term definition" is unclear with compact IRI keys [defer-future-version](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22defer-future-version%22)
>
> Expansion concept "key's term definition" is unclear with compact IRI keys.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 166](https://github.com/w3c/json-ld-api/issues/166): Relationship to the RDF/JS Dataset interface(s) [defer-future-version](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22defer-future-version%22)
>
> Relationship to the RDF/JS Dataset interface(s).
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 380](https://github.com/w3c/json-ld-api/issues/380): Expansion does not take property-scoped contexts for nested properties into account [defer-future-version](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22defer-future-version%22)[spec:editorial](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22spec%3Aeditorial%22)[test:needs tests](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22test%3Aneeds+tests%22)[wr:spec-updated-partial](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22wr%3Aspec-updated-partial%22)
>
> Expansion does not take property-scoped contexts for nested properties into account.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 391](https://github.com/w3c/json-ld-api/issues/391): Recursively nested properties and compaction [defer-future-version](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22defer-future-version%22)
>
> Recursively nested properties and compaction.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 435](https://github.com/w3c/json-ld-api/issues/435): relative iri compaction [defer-future-version](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22defer-future-version%22)[spec:wontfix](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22spec%3Awontfix%22)[wr:pending](https://github.com/w3c/json-ld-api/issues/?q=is%3Aissue+is%3Aopen+label%3A%22wr%3Apending%22)
>
> relative iri compaction.

## C. Changes since 1.0 Recommendation of 16 January 2014

*This section is non-normative.*

- The §5.1 Expansion Algorithm has a special [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode), based on
  the `frameExpansion` flag, to enable content associated with JSON-LD
  frames, which may not otherwise be valid [JSON-LD documents](https://www.w3.org/TR/json-ld11/#dfn-json-ld-document).
- An [expanded term definition](https://www.w3.org/TR/json-ld11/#dfn-expanded-term-definition) can now have an `@context` [entry](https://infra.spec.whatwg.org/#map-entry), which defines a context used for values of
  a [property](https://www.w3.org/TR/rdf11-concepts/#dfn-property) identified with such a [term](https://www.w3.org/TR/json-ld11/#dfn-term). This context is used
  in both the §5.1 Expansion Algorithm and §6.1 Compaction Algorithm.
- A new § 7.3 Merge Node Maps (§7.3) is required
  for framing, to create a single graph from the [default](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) and [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph).
- An [expanded term definition](https://www.w3.org/TR/json-ld11/#dfn-expanded-term-definition) can now have an `@nest` [entry](https://infra.spec.whatwg.org/#map-entry), which identifies a term expanding to `@nest` which is used for containing [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) using the same `@nest` mapping. When expanding, the values of an [entry](https://infra.spec.whatwg.org/#map-entry) expanding to `@nest` are treated as if they were contained
  within the enclosing [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) directly.
- `@container` values within an [expanded term definition](https://www.w3.org/TR/json-ld11/#dfn-expanded-term-definition) may now
  include `@id` and `@type`, corresponding to [id maps](https://www.w3.org/TR/json-ld11/#dfn-id-map) and [type maps](https://www.w3.org/TR/json-ld11/#dfn-type-map).
- Both [language maps](https://www.w3.org/TR/json-ld11/#dfn-language-map) and [index maps](https://www.w3.org/TR/json-ld11/#dfn-index-map) may legitimately have an `@none` value, but
  JSON-LD 1.0 only allowed [string](https://infra.spec.whatwg.org/#javascript-string) values. This has been updated
  to allow (and ignore) `@none` values.
- The JSON syntax has been abstracted into an internal representation to allow for other serialization formats that are functionally equivalent
  to JSON.
- Preserved values are compacted using the [properties](https://www.w3.org/TR/rdf11-concepts/#dfn-property) of the referencing term.
- The value for `@container` in an [expanded term definition](https://www.w3.org/TR/json-ld11/#dfn-expanded-term-definition) can also be an [array](https://infra.spec.whatwg.org/#list) containing any appropriate container
  keyword along with `@set` (other than `@list`).
  This allows a way to ensure that such [entry](https://infra.spec.whatwg.org/#map-entry) values will always
  be expressed in [array](https://infra.spec.whatwg.org/#list) form.
- Added support for the `compactToRelative` option to allow IRI compaction (§ 6.2 IRI Compaction (§6.2))
  to document-relative IRIs to be disabled.
- In JSON-LD 1.1, terms will be used as [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) prefixes
  when compacting only if
  a [simple term definition](https://www.w3.org/TR/json-ld11/#dfn-simple-term-definition) is used where the value ends with a URI [gen-delim](https://tools.ietf.org/html/rfc3986#section-2.2) character,
  or if their [expanded term definition](https://www.w3.org/TR/json-ld11/#dfn-expanded-term-definition) contains
  an `@prefix` [entry](https://infra.spec.whatwg.org/#map-entry) with the value `true`. The 1.0 algorithm has
  been updated to only consider terms that map to a value that ends with a URI [gen-delim](https://tools.ietf.org/html/rfc3986#section-2.2) character.
- Term definitions now allow `@container` to include `@graph`,
  along with `@id`, `@index` and `@set`.
  In the §5.1 Expansion Algorithm, this is
  used to create a [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph) from either a [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object), or
  objects which are values of [entries](https://infra.spec.whatwg.org/#map-entry) in an [id map](https://www.w3.org/TR/json-ld11/#dfn-id-map) or [index map](https://www.w3.org/TR/json-ld11/#dfn-index-map).
  The §6.1 Compaction Algorithm allows
  specific forms of graph objects to be compacted back to a set of [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object),
  or maps of [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object).
- §5.3 Value Expansion will not turn native values
  into [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object).
- The Term Selection algorithm (§4.4) has been
  updated to allow uses of containers for values which would otherwise not
  match. This is used in the Compaction Algorithm (§5.1) to use the `@none` keyword, or an alias, for
  values of maps for which there is no natural index. The §5.1 Expansion Algorithm removes this indexing
  transparently.

Additionally, see § D. Changes since JSON-LD Community Group Final Report (§D).

## D. Changes since JSON-LD Community Group Final Report

*This section is non-normative.*

- [Lists](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab) may now have items which are themselves [lists](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab).
- The §8.1 Deserialize JSON-LD to RDF Algorithm has been updated to ensure that only well-formed [triples](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) are emitted; previously, it only ensured that [triples](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) containing [relative IRI references](https://tools.ietf.org/html/rfc3987#section-6.5) were excluded.
- The API now adds an `ordered` option, defaulting to `false` This is used in algorithms to
  control iteration of [map entry](https://infra.spec.whatwg.org/#map-entry) keys. Previously, the
  algorithms always required such an order. The instructions for
  evaluating test results have been updated accordingly.
- The Generate Blank Node Identifier algorithm (§7.4) has been updated to remove the specifics of how new blank node
  identifiers are created.
- Values of `@type`, or an alias of `@type`, may now have their `@container` set to `@set` to ensure that `@type` entries are always represented as an array. This
  also allows a term to be defined for `@type`, where the value *MUST* be a [map](https://infra.spec.whatwg.org/#ordered-map) with `@container` set to `@set`.
- Updated the IRI Expansion algorithm (§5.2) so that
  if *value* contains a colon (`:`), but *prefix* is not a [term](https://www.w3.org/TR/json-ld11/#dfn-term), to only return *value* if it has the [form](https://tools.ietf.org/html/rfc3987#section-2.2) of an [IRI](https://tools.ietf.org/html/rfc3987#section-2), otherwise fall through to
  the rest of the algorithm.
- The use of [blank node identifiers](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier) to label properties is obsolete,
  and may be removed in a future version of JSON-LD,
  as is the support for [generalized RDF Datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-generalized-rdf-dataset) and thus the `produceGeneralizedRdf` option may be also be removed.
- Added API steps to accept `text/html` as input,
  extracting either a specifically targeted [script element](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element),
  the first found JSON-LD script element,
  or all JSON-LD script elements.
- Added `contentType` field to `RemoteDocument`.
- Added support for protected [contexts](https://www.w3.org/TR/json-ld11/#dfn-context) and [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition).
- Because scoped contexts can lead to contexts being reloaded, replace the **recursive context inclusion** error with a `context overflow` error.
- Added support for `"@type": "@none"` in a [term definition](https://www.w3.org/TR/json-ld11/#dfn-term-definition) to prevent value compaction.
- Added support for [JSON literals](https://www.w3.org/TR/json-ld11/#dfn-json-literal).
- [Term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition) with keys which are of the [form](https://tools.ietf.org/html/rfc3987#section-2.2) of an [IRI](https://tools.ietf.org/html/rfc3987#section-2) or a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) *MUST NOT* expand to an [IRI](https://tools.ietf.org/html/rfc3987#section-2) other than the expansion of the key itself.
- Consolidate `RemoteDocument` processing into the `LoadDocumentCallback` including variations on HTML processing.
- The IRI Compaction algorithm (§6.2) may generate an error if the result is an [IRI](https://tools.ietf.org/html/rfc3987#section-2) which could be confused with a [compact IRI](https://www.w3.org/TR/json-ld11/#dfn-compact-iri) in the [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context).
- By default, all contexts are propagated when traversing [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object), other than [type-scoped contexts](https://www.w3.org/TR/json-ld11/#dfn-type-scoped-context). This can be controlled using the `@propagate` [entry](https://infra.spec.whatwg.org/#map-entry) in a [local context](https://www.w3.org/TR/json-ld11/#dfn-local-context).
- A context may contain a `@import` [entry](https://infra.spec.whatwg.org/#map-entry) used to reference a remote context
  within a context, allowing `JSON-LD 1.1` features to be added to contexts originally
  authored for `JSON-LD 1.0`.
- The `colliding keywords` error is not issued for `@type`;
  instead, previous values of `@type` are prepended to any new values, when expanding.
- A [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) may include an [included block](https://www.w3.org/TR/json-ld11/#dfn-included-block),
  which is used to contain a set of [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) which are treated
  exactly as if they were [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) defined in an [array](https://infra.spec.whatwg.org/#list) including the containing [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).
  This allows the use of the object form of a JSON-LD document when there is more
  than one [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object) being defined, and where those [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object) are not embedded as values of the containing [node object](https://www.w3.org/TR/json-ld11/#dfn-node-object).
- A [relative IRI reference](https://tools.ietf.org/html/rfc3987#section-6.5) has been added as a possible value for `@vocab` in
  a context. When this is set, vocabulary-relative IRI references, such as the [entries](https://infra.spec.whatwg.org/#map-entry) of [node objects](https://www.w3.org/TR/json-ld11/#dfn-node-object), are expanded or compacted relative
  to the [base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri) and the [vocabulary mapping](https://www.w3.org/TR/json-ld11/#dfn-vocabulary-mapping) using string concatenation.
- In the `LoadDocumentCallback`, if the retrieved content is not any JSON media type
  and there is a link header with `rel=alternate` and `type=application/ld+json`, redirect
  to that content.
- [Value objects](https://www.w3.org/TR/json-ld11/#dfn-value-object), and associated [context](https://www.w3.org/TR/json-ld11/#dfn-context) and [term definitions](https://www.w3.org/TR/json-ld11/#dfn-term-definition) have been updated to
  support `@direction` for setting the [base direction](https://www.w3.org/TR/json-ld11/#dfn-base-direction) of strings.
- It is no longer required that language tags be normalized to lower case,
  other than for testing considerations.
  Language tags that are not valid according to [BCP47] are rejected.
- The [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is now implicitly `json-ld-1.1`, unless set
  explicitly to `json-ld-1.0`.
- Improve notation using [IRI](https://tools.ietf.org/html/rfc3987#section-2), [IRI reference](https://tools.ietf.org/html/rfc3987#section-1.3), and [relative IRI reference](https://tools.ietf.org/html/rfc3987#section-6.5).
- Ignore terms and IRIs that have the form of a keyword (`"@"1*ALPHA`).

## E. Changes since Candidate Release of 12 December 2019

*This section is non-normative.*
> **Note:**
>
> > **Note:**
> >
> > Note
>
> All changes are editorial and do not affect the observable
> behavior of the API nor the expected test results.

- Add `application/xhtml+xml` as an allowed media type in § 9.5.1 Process HTML (§9.5.1),
  in the note in § 9.4.1 LoadDocumentCallback (§9.4.1),
  and as a use of the `profile` API option.
- Added add value, IRI expanding, and IRI compacting macros to reduce boilerplate in algorithmic language.
- Improved algorithms in § 4.1 Context Processing Algorithm (§4.1), § 4.2 Create Term Definition (§4.2), § 2.1 Expansion (§2.1), § 2.2 Compaction (§2.2), § 6.3 Value Compaction (§6.3), § 7.2 Node Map Generation (§7.2),
  and § 8.1 Deserialize JSON-LD to RDF Algorithm (§8.1).
- When creating an `i18n` datatype or `rdf:CompoundLiteral`, [language tags](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) are
  normalized to lower case to improve interoperability between implementations.
- Moved non-recursive portions algorithms
  into the `JsonLdProcessor` processing steps.
- Fix some `JsonLdOption` initializers where defaults are `null`.
  Set default value for `processingMode` to `json-ld-1.1`.
- Remove normative text for canonicalizing `rdf:JSON` literals and
  reference the `rdf:JSON` datatype of the syntax document
  for the conversion of the [JSON Literals](https://www.w3.org/TR/json-ld11/#dfn-json-literal) in § 8.6 Data Round Tripping (§8.6).
- Updated interfaces in § 9. The Application Programming Interface (§9) to use [record](https://heycam.github.io/webidl/#idl-record),
  instead of [dictionary](https://heycam.github.io/webidl/#dfn-dictionary),
  and to allow `RemoteDocument` to be used
  as a direct input, which resolves a [`Promise`](https://heycam.github.io/webidl/#idl-promise) boundary issue.

## F. Changes since Candidate Release of 05 March 2020

*This section is non-normative.*
> **Note:**
>
> > **Note:**
> >
> > Note
>
> All changes are editorial and do not affect the observable
> behavior of the API nor the expected test results.

- The inverse context is not passed explicitly as a parameter
  to the §4.4 Term Selection, §6.2 IRI Compaction,
  and §6.3 Value Compaction algorithms,
  but is retrieved from the inverse context field
  within an [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context), and initialized as necessary.
  This simplifies calling sequences and better represents actual implementation experience.
- Updated step 5.13 of the §4.1 Context Processing Algorithm to pass *override protected* and not pass *validate scoped context* to the Create Term Definition algorithm (§4.2).
- Move step 5.2.2 of the §4.1 Context Processing Algorithm to run before the subsequent step for checking *remote contexts*.
- Updated step 11 of the Create Term Definition algorithm (§4.2) to use any boolean value of `@protected`, not just `true`.
- Updated step 4.5 of the IRI Compaction algorithm (§6.2) to use `@index` for any value with an `@index` entry.
- Update step 13.4.6.2 of the §5.1 Expansion Algorithm to pass `null` for *active property*, as [included blocks](https://www.w3.org/TR/json-ld11/#dfn-included-block) do not define a relationship to a referencing node.
- Update step 13.8.3.6 of the §5.1 Expansion Algorithm to pass `true` for the *from map* parameter to properly manage reverting [active contexts](https://www.w3.org/TR/json-ld11/#dfn-active-context).
- Update step 11.1 of the §6.1 Compaction Algorithm to pass `false` for *propagate* when calling the §4.1 Context Processing Algorithm.
- Updated step 12.2.4 of the §6.1 Compaction Algorithm to only look for `@set` if [processing mode](https://www.w3.org/TR/json-ld11/#dfn-processing-mode) is json-ld-1.1.
- Update step 12.8.6 of the §6.1 Compaction Algorithm to clarify the value passed for *element*.
- Update steps 12.8.9.6.3 and 12.8.9.2.2 of the §6.1 Compaction Algorithm to invoke the add value macro for adding remaining values back to *compacted item*.
- Update step 12.8.10 of the §6.1 Compaction Algorithm to add values to *nest result* instead of *result* as was originally intended.
- Update step 2.2.1 of § 7.3 Merge Node Maps (§7.3) to
  exclude `@type`, leaving it to the next step.
  This could cause type values from a node to be left out of the merge.
- Added step 5.2.3 to the §4.1 Context Processing Algorithm,
  which is added *validate scoped context* as a new
  optional argument, and passed to the Create Term Definition algorithm (§4.2),
  which in turn uses it with the value `false` when recursively calling
  the §4.1 Context Processing Algorithm when validating a [scoped context](https://www.w3.org/TR/json-ld11/#dfn-scoped-context).
- Added missing values for `@container` in the description of `invalid container mapping`.
- Clarified step 3.13 in the Inverse Context Creation algorithm (§4.3) by moving the preceding step to 3.9.
- Update substeps of 6.1.6 in the §8.4 Serialize RDF as JSON-LD Algorithm to update *cl reference* and not *node*.
- Added § 1.4.2 Syntax Tokens and Keywords (§1.4.2) to describe
  the `preserve` keyword, which is only used for framing.

## G. Changes since Proposed Recommendation Release of 7 May 2020

*This section is non-normative.*

- Removed remaining "at-risk" notes.
- Update bibliographic reference for JCS to [RFC8785].
- Changed `[Exposed=(Window,Worker)]` to `[Exposed=JsonLd]`,
  which is declared as a global interface in order to expose the `JsonLdProcessor` interface
  for non-browser usage to address review suggestions.

## I. References

### I.1 Normative references

[BCP47]

[Tags for Identifying Languages](https://tools.ietf.org/html/bcp47). A. Phillips; M. Davis. IETF. September 2009. IETF Best Current Practice. URL: <https://tools.ietf.org/html/bcp47>

[DOM]

[DOM Standard](https://dom.spec.whatwg.org/). Anne van Kesteren. WHATWG. Living Standard. URL: <https://dom.spec.whatwg.org/>

[ECMASCRIPT]

[ECMAScript Language Specification](https://tc39.es/ecma262/). Ecma International. URL: <https://tc39.es/ecma262/>

[HTML]

[HTML Standard](https://html.spec.whatwg.org/multipage/). Anne van Kesteren; Domenic Denicola; Ian Hickson; Philip Jägenstedt; Simon Pieters. WHATWG. Living Standard. URL: <https://html.spec.whatwg.org/multipage/>

[IEEE-754-2008]

[IEEE 754-2008 Standard for Floating-Point Arithmetic](http://standards.ieee.org/findstds/standard/754-2008.html). Institute of Electrical and Electronics Engineers. 2008. URL: <http://standards.ieee.org/findstds/standard/754-2008.html>

[INFRA]

[Infra Standard](https://infra.spec.whatwg.org/). Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: <https://infra.spec.whatwg.org/>

[JSON-LD10]

[JSON-LD 1.0](https://www.w3.org/TR/2014/REC-json-ld-20140116/). Manu Sporny; Gregg Kellogg; Marcus Langhaler. W3C. 16 January 2014. W3C Recommendation. URL: <https://www.w3.org/TR/2014/REC-json-ld-20140116/>

[JSON-LD11]

[JSON-LD 1.1](https://www.w3.org/TR/json-ld11/). Gregg Kellogg; Pierre-Antoine Champin; Dave Longley. W3C. 7 May 2020. W3C Proposed Recommendation. URL: <https://www.w3.org/TR/json-ld11/>

[JSON-LD11-FRAMING]

[JSON-LD 1.1 Framing](https://www.w3.org/TR/json-ld11-framing/). Dave Longley; Gregg Kellogg; Pierre-Antoine Champin. W3C. 7 May 2020. W3C Proposed Recommendation. URL: <https://www.w3.org/TR/json-ld11-framing/>

[LINKED-DATA]

[Linked Data Design Issues](https://www.w3.org/DesignIssues/LinkedData.html). Tim Berners-Lee. W3C. 27 July 2006. W3C-Internal Document. URL: <https://www.w3.org/DesignIssues/LinkedData.html>

[promises-guide]

[Writing Promise-Using Specifications](https://www.w3.org/2001/tag/doc/promises-guide). Domenic Denicola. W3C. 9 November 2018. TAG Finding. URL: <https://www.w3.org/2001/tag/doc/promises-guide>

[RDF-SCHEMA]

[RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/). Dan Brickley; Ramanathan Guha. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-schema/>

[RDF11-CONCEPTS]

[RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). Richard Cyganiak; David Wood; Markus Lanthaler. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf11-concepts/>

[RDF11-MT]

[RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/). Patrick Hayes; Peter Patel-Schneider. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf11-mt/>

[RFC2045]

[Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies](https://tools.ietf.org/html/rfc2045). N. Freed; N. Borenstein. IETF. November 1996. Draft Standard. URL: <https://tools.ietf.org/html/rfc2045>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://tools.ietf.org/html/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://tools.ietf.org/html/rfc2119>

[RFC3986]

[Uniform Resource Identifier (URI): Generic Syntax](https://tools.ietf.org/html/rfc3986). T. Berners-Lee; R. Fielding; L. Masinter. IETF. January 2005. Internet Standard. URL: <https://tools.ietf.org/html/rfc3986>

[RFC3987]

[Internationalized Resource Identifiers (IRIs)](https://tools.ietf.org/html/rfc3987). M. Duerst; M. Suignard. IETF. January 2005. Proposed Standard. URL: <https://tools.ietf.org/html/rfc3987>

[RFC5234]

[Augmented BNF for Syntax Specifications: ABNF](https://tools.ietf.org/html/rfc5234). D. Crocker, Ed.; P. Overell. IETF. January 2008. Internet Standard. URL: <https://tools.ietf.org/html/rfc5234>

[RFC6839]

[Additional Media Type Structured Syntax Suffixes](https://tools.ietf.org/html/rfc6839). T. Hansen; A. Melnikov. IETF. January 2013. Informational. URL: <https://tools.ietf.org/html/rfc6839>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://tools.ietf.org/html/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://tools.ietf.org/html/rfc8174>

[RFC8259]

[The JavaScript Object Notation (JSON) Data Interchange Format](https://tools.ietf.org/html/rfc8259). T. Bray, Ed.. IETF. December 2017. Internet Standard. URL: <https://tools.ietf.org/html/rfc8259>

[RFC8288]

[Web Linking](https://tools.ietf.org/html/rfc8288). M. Nottingham. October 2017. Proposed Standard. URL: <https://tools.ietf.org/html/rfc8288>

[Turtle]

[RDF 1.1 Turtle](https://www.w3.org/TR/turtle/). Eric Prud'hommeaux; Gavin Carothers. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/turtle/>

[WEBIDL]

[Web IDL](https://heycam.github.io/webidl/). Boris Zbarsky. W3C. 15 December 2016. W3C Editor's Draft. URL: <https://heycam.github.io/webidl/>

[XMLSCHEMA11-2]

[W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/). David Peterson; Sandy Gao; Ashok Malhotra; Michael Sperberg-McQueen; Henry Thompson; Paul V. Biron et al. W3C. 5 April 2012. W3C Recommendation. URL: <https://www.w3.org/TR/xmlschema11-2/>

### I.2 Informative references

[cooluris]

[Cool URIs for the Semantic Web](https://www.w3.org/TR/cooluris/). Leo Sauermann; Richard Cyganiak. W3C. 3 December 2008. W3C Note. URL: <https://www.w3.org/TR/cooluris/>

[JSON-LD10-API]

[JSON-LD 1.0 Processing Algorithms And API](https://www.w3.org/TR/2014/REC-json-ld-api-20140116/). Marcus Langhaler; Gregg Kellogg; Manu Sporny. W3C. 16 January 2014. W3C Recommendation. URL: <https://www.w3.org/TR/2014/REC-json-ld-api-20140116/>

[RFC8785]

[JSON Canonicalization Scheme (JCS)](https://www.rfc-editor.org/rfc/rfc8785). A. Rundgren; B. Jordan; S. Erdtman. Network Working Group. June 2020. Informational. URL: <https://www.rfc-editor.org/rfc/rfc8785>
