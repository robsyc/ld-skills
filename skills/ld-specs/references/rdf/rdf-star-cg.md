---
title: "RDF-star and SPARQL-star"
source: https://www.w3.org/2021/12/rdf-star.html
family: rdf
spec_date: 2021-12-17
fetched: 2026-10-26
---

# RDF-star and SPARQL-star

> Final CG report on statement-level metadata; folded into RDF 1.2 as triple terms.

## Contents

- Abstract
- 1 Introduction
  - 1.1 Background and Motivation
  - 1.2 Overview
  - 1.3 Common misconceptions
  - 1.4 Conventions
  - 1.5 Structure of this document
  - 1.6 Conformance
- 2 Concepts and Abstract Syntax
  - 2.1 Quoted and Asserted Triples
  - 2.2 RDF-star Graph Examples
  - 2.3 Triples and occurrences
- 3 Concrete Syntaxes
  - 3.1 Annotation Syntax
  - 3.2 Turtle-star
    - 3.2.1 Grammar
    - 3.2.2 Parsing
  - 3.3 TriG-star
    - 3.3.1 Grammar
    - 3.3.2 Parsing
    - 3.3.3 Discussion
  - 3.4 N-Triples-star
    - 3.4.1 Grammar
    - 3.4.2 Parsing
  - 3.5 N-Quads-star
  - 3.6 Other Concrete Syntaxes
- 4 SPARQL-star Query Language
  - 4.1 Initial Definitions
  - 4.2 Grammar
  - 4.3 Translation to the Algebra
    - 4.3.1 Variable Scope
    - 4.3.2 Expand Syntax Forms
    - 4.3.3 Translate Property Path Patterns
    - 4.3.4 Translate Basic Graph Patterns
  - 4.4 Function and Operator Definitions
    - 4.4.1 TRIPLE
    - 4.4.2 SUBJECT
    - 4.4.3 PREDICATE
    - 4.4.4 OBJECT
    - 4.4.5 isTRIPLE
    - 4.4.6 Quoted Triple Expression
    - 4.4.7 sameTerm
    - 4.4.8 sparql-compare
    - 4.4.9 RDFterm-equal
    - 4.4.10 Operator Mappings
    - 4.4.11 Triple terms with ORDER BY
  - 4.5 Examples and Discussion
  - 4.6 Evaluation Semantics
  - 4.7 Query Result Formats
    - 4.7.1 SPARQL-star Query Results JSON Format
    - 4.7.2 SPARQL-star Query Results XML Format
- 5 SPARQL-star Update
  - 5.1 Informal Description
    - 5.1.1 INSERT DATA
    - 5.1.2 DELETE DATA
    - 5.1.3 DELETE/INSERT
  - 5.2 Grammar
  - 5.3 Semantics
- 6 RDF-star Semantics
  - 6.1 Mapping RDF-star abstract syntax to RDF
  - 6.2 Entailment of RDF-star graphs
  - 6.3 Merging RDF-star graphs
  - 6.4 Remarks
    - 6.4.1 Implementing the RDF-star semantics
    - 6.4.2 Combining RDF-star graphs
    - 6.4.3 Other uses of the unstar mapping
    - 6.4.4 Referential opacity
    - 6.4.5 Selective referential transparency
    - 6.4.6 Other alternatives to referential opacity
- 7 RDF-star vocabulary
  - 7.1 Core vocabulary
  - 7.2 Extended vocabulary
  - 7.3 Vocabulary semantics
- A IANA Considerations
- B Historical remarks
  - B.1 SA-mode and PG-mode
  - B.2 The seminal example
- C Complete EBNF Grammars
  - C.1 Turtle-Star EBNF Grammar
  - C.2 TriG-Star EBNF Grammar
  - C.3 N-Triples-Star EBNF Grammar
  - C.4 N-Quads-Star EBNF Grammar
  - C.5 SPARQL-Star EBNF Grammar
- E References
  - E.1 Normative references
  - E.2 Informative references

---

## Abstract

The Resource Description Framework (RDF) is a general-purpose framework for representing information on the Web. RDF-star extends RDF with a convenient way to make statements about other statements. This specification defines the abstract syntax of RDF-star as an extension of RDF's. It extends a number of RDF concrete syntaxes to support the new abstract syntax. It also extends RDF's formal semantics. Finally, this specification extends the SPARQL language to allow querying and updating of RDF-star data.

## 1. Introduction

### 1.1 Background and Motivation

*This section is non-normative.*

The RDF data model lets you state facts in three-part subject-predicate-object statements known as triples. For example, with a single RDF triple, you can say that employee38 has a familyName of "Smith". A triple's predicate is a property specified with an IRI (an Internationalized version of a URI), identifying that property in a globally unambiguous way. A triple's subject and object can each be an IRI referencing any entity, and the object can also be a literal value such as "Smith" or data of other types such as dates, numbers, or Boolean values.

Sometimes, we want the subject or object of a triple to refer to another triple. For example, the statement "according to employee22, employee38 has a jobTitle of 'Assistant Designer'" can be modeled as a triple with "according to" as its predicate, employee22 as its object, and another triple as its subject, namely the triple "employee38 has a jobTitle of 'Assistant Designer'". This use of a triple as the subject or object resource of another triple so that we can say things about that triple is known as [reification](https://www.w3.org/TR/rdf11-mt/#reification).
The concept of reification has always been part of RDF, but expressing it in most RDF concrete syntaxes such as Turtle and N-Triples, as well as processing or querying it with SPARQL, has been verbose and cumbersome [RDF-STAR-FOUNDATION].

### 1.2 Overview

*This section is non-normative.*

This specification describes RDF-star, an extension of RDF's conceptual data model and concrete syntaxes, which provides a compact alternative to [standard RDF reification](https://www.w3.org/TR/rdf11-mt/#reification). This model and its syntaxes enable the creation of concise triples that reference other triples as subject and object resources.
Triples that include a triple as a subject or an object are known as RDF-star triples. The following dataset shows the example RDF-star triples from above using the §3.2 Turtle-star syntax, which uses double angle brackets to enclose a triple serving as a subject or object resource:
> **Example:**
>
> Example 1
>
>
>
> ```
> PREFIX :    <http://www.example.org/>
>
> :employee38 :familyName "Smith" .
> << :employee38 :jobTitle "Assistant Designer" >> :accordingTo :employee22 .
> ```

After declaring a prefix so that IRIs can be abbreviated, the first triple in this example asserts that employee38 has a familyName of "Smith". Note that this dataset does not assert that employee38 has a jobTitle of "Assistant Designer"; it says that employee22 has made that claim. In other words, the triple "employee38 has a jobTitle of 'Assistant Designer'" is not what we call an asserted triple, like "employee38 has a familyName of 'Smith'" above; rather, it is known as a quoted triple.

If we added the triple `:employee38 :jobTitle "Assistant Designer"` to the example above, then this triple about employee38's jobTitle would be both a quoted and an asserted triple.
This pattern is quite common, so Turtle-star offers a dedicated syntax for it, called the annotation syntax, illustrated in Example 2 below. Note that this construct is purely syntactic sugar, as it can be expanded using only the double angle brackets.
> **Example:**
>
> Example 2
>
>
>
> ```
> PREFIX :    <http://www.example.org/>
>
> :employee38
>     :familyName "Smith" ;
>     :jobTitle "Assistant Designer" {| :accordingTo :employee22 |} .
>
> # this is equivalent to:
> #
> # :employee38 :familyName "Smith" .
> # :employee38 :jobTitle "Assistant Designer" .
> # << :employee38 :jobTitle "Assistant Designer" >> :accordingTo :employee22 .
> ```

This specification also describes an extension to the SPARQL Protocol and Query Language known as SPARQL-star (§4) for the querying of RDF-star triples. For example, the following SPARQL-star query asks "who has made any claims about employee38?"
> **Example:**
>
> Example 3
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> SELECT ?claimer WHERE {
>    << :employee38 ?property ?value >> :accordingTo ?claimer
> }
> ```

SPARQL can also be used to update RDF data, and SPARQL-star also extends that part. For example, the following SPARQL-star adds all the statements made by employee22 about employee38 as asserted triples, annotating them as "confirmed".
> **Example:**
>
> Example 4
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> INSERT {
>   :employee38 ?p ?o {| :status "confirmed" |}
> } WHERE {
>    << :employee38 ?p ?o >> :accordingTo :employee22
> }
> ```

### 1.3 Common misconceptions

People coming to RDF-star may have wrong ideas about what it is or how to use it. The purpose of this section is to dispel the most common misconceptions.

RDF-star is *not* syntactic sugar for [standard reification](https://www.w3.org/TR/rdf11-mt/#reification). While the latter is a vocabulary that fits into the standard RDF model (abstract syntax), RDF-star extends that model (see § 2. Concepts and Abstract Syntax (§2)) with a new construct, namely quoted triples. Note also that the two are not mutually exclusive: standard reification can be used in conjunction with RDF-star.

Unlike reified statements, RDF-star quoted triples are unique: wherever `<< :employee38 :jobTitle "Assistant Designer" >>` appears, it always denotes one and the same thing. This impacts the modeling choices one has to make when using RDF-star; this is further discussed in § 2.3 Triples and occurrences (§2.3).

Finally, quoted triples are referentially opaque. This means that two quoted triples containing distinct but equivalent terms (i.e., coreferences, known to denote the same thing) are nonetheless considered to be different triples. § 6.4.4 Referential opacity (§6.4.4) and the following sections discuss the rationale for this design, and how some form of referential transparency can still be added to RDF-star if and when needed.

### 1.4 Conventions

For the remainder of this document, examples will assume that the following prefixes have been declared to represent the IRIs shown with them here:

| `:`         | `<http://www.example.org/>`                     |
| ----------- | ----------------------------------------------- |
| `rdf:`      | `<http://www.w3.org/1999/02/22-rdf-syntax-ns#>` |
| `rdfs:`     | `<http://www.w3.org/2000/01/rdf-schema#>`       |
| `owl:`      | `<http://www.w3.org/2002/07/owl#>`              |
| `prov:`     | `<http://www.w3.org/ns/prov#>`                  |
| `dbo:`      | `<http://dbpedia.org/ontology/>`                |
| `dbr:`      | `<http://dbpedia.org/resource/>`                |
| `dc:`       | `<http://purl.org/dc/elements/1.1/>`            |
| `dct:`      | `<http://purl.org/dc/terms/>`                   |
| `rdf-star:` | `<http://www.w3.org/ns/rdf-star#>`              |

### 1.5 Structure of this document

This specification covers many aspects of RDF-star, and not all sections will be of interest to all readers.

Section 2 (§2) first defines the concepts and the abstract syntax of RDF-star, to which all following sections refer.
The next three sections focus on how users will interact with the abstract syntax, defining the §3 Concrete Syntaxes, the query language SPARQL-star (§4) and its counterpart for updates (§5). Section 6 (§6) then defines RDF-star's formal semantics, which lays the foundation for reasoning with RDF-star data. Finally, Section 7 (§7) defines an RDF vocabulary capturing the main concepts of RDF-star.

|                                                                                                            | § 2. Concepts and Abstract Syntax (§2) **can be...**      |                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| *... serialized with* § 3. Concrete Syntaxes (§3) |                                                                                                           | *... represented by* § 7. RDF-star vocabulary (§7)    |
| *... queried with* § 4. SPARQL-star Query Language (§4) | *... updated with* § 5. SPARQL-star Update (§5) | *... interpreted through* § 6. RDF-star Semantics (§6) |

*Figure 1 A visual map of the sections of this document*

### 1.6 Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, and *OPTIONAL* in this document
are to be interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all capitals, as shown here.

A system supports RDF-star for input if it supports an input syntax for
an RDF 1.1 standard syntax that has additional syntax for quoted triples.
Such input syntaxes include those in the [RDF-star test suite](https://w3c.github.io/rdf-star/tests/) ([N-Triples-star syntax tests](https://w3c.github.io/rdf-star/tests/nt/syntax/), [Turtle-star syntax tests](https://w3c.github.io/rdf-star/tests/turtle/syntax/),
or [TriG-star syntax tests](https://w3c.github.io/rdf-star/tests/trig/syntax/)).

A system supports RDF-star for output if it supports an output syntax for
an RDF 1.1 standard syntax that has additional syntax for quoted triples.
Such output syntaxes include those in the [RDF-star test suite](https://w3c.github.io/rdf-star/tests/) ([N-Triples-star syntax tests](https://w3c.github.io/rdf-star/tests/nt/syntax/), [Turtle-star syntax tests](https://w3c.github.io/rdf-star/tests/turtle/syntax/),
or [TriG-star syntax tests](https://w3c.github.io/rdf-star/tests/trig/syntax/)).

A system supports SPARQL-star if it passes
the [SPARQL-star syntax](https://w3c.github.io/rdf-star/tests/sparql/syntax/) test suite
and the [SPARQL-star evaluation](https://w3c.github.io/rdf-star/tests/sparql/eval/) test suites.

## 2. Concepts and Abstract Syntax

In the following, we introduce a number of definitions specific to SPARQL-star, which rely on the following notions (extending some of them) defined in [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/) [RDF11-CONCEPTS]: *[blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)*, *[default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph)*, *[graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name)*, *[IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri)*, *[literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal)*, *[named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph)*, *[subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject)*, *[predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate)*, *[object](https://www.w3.org/TR/rdf11-concepts/#dfn-object)*, *[RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset)*, *[RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph)*, *[RDF triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple)*,
and *[RDF term](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term)*.

An *RDF-star graph* is a set of RDF-star triples.

An *RDF-star triple* is a 3-tuple defined recursively as follows:

- any [RDF triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple) is an RDF-star triple;
- if *t* and *t'* are RDF-star triples, *s* is an [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) or a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node), *p* is an [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri), *o* is an [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri), a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) or a [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal), then (*t*, *p*, *o*), (*s*, *p*, *t*) and (*t*, *p*, *t'*) are RDF-star triples.

As for [RDF triples](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple), we call the 3 components of an RDF-star triple its [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject), [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate) and [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object), respectively. From the definitions above, it follows that any [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) is also an RDF-star graph. Note also that, by definition, an RDF-star triple cannot contain itself and cannot be nested infinitely.

[IRIs](https://www.w3.org/TR/rdf11-concepts/#dfn-iri), [literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal), [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) and RDF-star triples are collectively known as *RDF-star terms*.

For every RDF-star triple *t*, we define its *constituent terms* (or simply constituents) as the set containing its [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject), its [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate), its [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object), plus all the constituent terms of its [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) and/or its [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) if they are themselves RDF-star triples. By extension, we define the constituent terms of an RDF-star graph to be the union set of the constituent terms of all its triples.
> **Example:**
>
> Consider the following RDF-star triple (represented in Turtle-star):
>
> > **Example:**
> >
> > Example 5
> >
> >
> >
> > ```
> > << _:a :name "Alice" >> :statedBy :bob.
> > ```
>
> Its set of constituent terms comprises the [IRIs](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) `:name`, `:statedBy`, `:bob`, the [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) `_:a`, the [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) `"Alice"`, and the triple `<< _:a :name "Alice" >>`.

An RDF-star triple used as the [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) or [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) of another RDF-star triple is called a *quoted triple*. An RDF-star triple that is an element of an RDF-star graph is called an *asserted triple*. Note that, in a given RDF-star graph, the same triple *MAY* be both quoted and asserted.

An *RDF-star dataset* is a collection of RDF-star graphs, and comprises:

- Exactly one [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph), being an RDF-star graph. The [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) does not have a name and *MAY* be empty.
- Zero or more [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph). Each [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph) is a pair consisting of either an [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) or a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) (called the [graph name](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name)), and an RDF-star graph. [Graph names](https://www.w3.org/TR/rdf11-concepts/#dfn-graph-name) are unique within an RDF-star dataset.

Again, this definition is an extension of the notion of [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset), hence it follows that any [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) is also an RDF-star dataset.

### 2.1 Quoted and Asserted Triples

*This section is non-normative.*

A triple in RDF is a tuple of three components: subject, predicate, and object. These are
collectively known as [RDF Terms](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term) as defined in [RDF11-CONCEPTS].

RDF-star introduces quoted triple, which is a new kind of RDF term.
A *quoted triple* is a triple used as the subject or object of another triple. Quoted
triples can also be called "embedded triples".

in RDF 1.1, an asserted triple is an element of the set of triples that
make up an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph). RDF-star does not change this except that an RDF-star
triple can contain quoted triples. A triple can be used as an *asserted
triple*, a *quoted triple*, or both, in a given graph.

A quoted triple is written in Turtle-star and related syntaxes using delimiters `<<` and `>>`.

`           << :a :name "Alice" >>         `

The definition of quoted triple is recursive. That is, a quoted triple can itself have a
subject or object component which is another quoted triple. Cycles of quoted
triples can not be created. In the next example, there is a quoted triple with
property `:reportedBy`, whose subject is another quoted triple, `:a :name         "Alice"`.

`           << << :a :name "Alice" >>  :reportedBy :charlie >>         `
> **Note:**
>
> > **Note:**
> >
> > Note
>
> It may be apt to draw a parallel between "quoted" triples and
> quoted expressions in the *programming language Lisp*.
> Expressions in Lisp (called "s-expressions") are interpreted
> through a process called "evaluation", and as a result they
> have a value. A quoted expression evaluates to the expression itself -
> you can imagine that quoting prevents the expression from being
> evaluated. In RDF (as well as in RDF-star), *asserting* a triple
> (i.e., considering it to be "true") serves as the analogue of
> evaluation. Triples are asserted, unless (in RDF-star) they are quoted
> which, effectively, prevents the triple from being asserted - thus a
> quoted triple stands by itself and we assign no truth value to it.
>
> Obviously this way of thinking is helpful only if you understand how Lisp works.

### 2.2 RDF-star Graph Examples

In the example below, there is a quoted triple, `:a :name "Alice"`, which is used
as the subject for an asserted triple:
> **Example:**
>
> Example 6
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> :bob :name "Bob" .
> << :a :name "Alice" >> :statedBy :bob .
> ```

The graph of this example has two asserted triples:

1. `:bob :name "Bob" .`
2. `<< :a :name "Alice" >> :statedBy :bob .`

This graph does not have an asserted triple, `:a :name "Alice"`, because
that triple is not an element of the set of triples.

On the other hand, the graph in the example below contains three asserted triples:
the same two as the previous example, and `:a :name "Alice"`. The latter is used
both as an asserted triple and a quoted triple in this graph.
> **Example:**
>
> Example 7
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> :bob :name "Bob" .
> :a :name "Alice" .
> << :a :name "Alice" >> :statedBy :bob .
> ```

### 2.3 Triples and occurrences

*This section is non-normative.*

According to the definitions above, an RDF-star triple is an abstract entity whose identity is entirely defined by its subject, predicate, and object. Conversely, given three RDF-star terms *s*, *p*, and *o*, there is exactly and only one RDF-star triple with subject *s*, predicate *p*, and object *o*. This unique triple (*s*, *p*, *o*) can be quoted as the subject or object of multiple other triples, but must be assumed to represent the *same thing* everywhere it occurs, just like the same [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) *p* is assumed to represent the same thing everywhere it occurs.

In some situations, however, it might be necessary to distinguish the *occurrences* of a triple in different graphs. Consider the following sentence: "The triple `<http://example.org/s> <http://example.org/p> <http://example.org/o>` in (the graph represented by) file1.ttl was added by Alice, and the same triple in file2.ttl was added by Bob." Note that the words "same triple" in this sentence may be confusing, because although the triple (as an abstract entity) is the same, its respective occurrences are different things, each within a different file and with a different author (this is known, in philosophy and linguistics, as the [type-token distinction](https://en.wikipedia.org/wiki/Type%E2%80%93token_distinction)). As the quoted triple represents a unique thing, adequately conveying the meaning of the sentence above requires additional nodes for representing the two distinct occurrences. One possible solution is illustrated in the following example (using the Turtle-star concrete syntax described in the next section (§3.2)).
> **Example:**
>
> Example 8
>
>
>
> ```
> _:a :occurrenceOf << :s :p :o >> ;
>     :in <file1.ttl> ;
>     dct:creator :alice.
> _:b :occurrenceOf << :s :p :o >> ;
>     :in <file2.ttl> ;
>     dct:creator :bob.
> ```

## 3. Concrete Syntaxes

This section defines the following concrete syntaxes:

- § 3.2 Turtle-star (§3.2)
- § 3.3 TriG-star (§3.3)
- § 3.4 N-Triples-star (§3.4)
- § 3.5 N-Quads-star (§3.5)
- § 3.6 Other Concrete Syntaxes (§3.6)

Changes for SPARQL-star are given in § 4.2 Grammar (§4.2) and the changes for the result set formats in § 4.7 Query Result Formats (§4.7).

### 3.1 Annotation Syntax

There are syntax additions for quoted triples and also for *annotation syntax* which provides a convenient shortcut in Turtle-star and
TriG-star syntaxes. It is used to both assert a triple and have that triple be the
subject of further triples. It uses delimiters `{|` and `|}` following an asserted
triple to make that triple, as a quoted triple, the subject of the
RDF-star triples formed by combining it with the enclosed RDF predicate(s) and object(s).

Annotation syntax does not appear in the RDF-star abstract data model. It is
only a syntactic short cut and the RDF-star abstract data model does not
distinguished how the triples were written.
> **Example:**
>
> Example 9
>
>
>
> ```
> :a :name "Alice" {| :statedBy :bob ; :recorded "2021-07-07"^^xsd:date |} .
> ```

is the same set of triples as:
> **Example:**
>
> Example 10
>
>
>
> ```
> << :a :name "Alice" >> :statedBy :bob .
> << :a :name "Alice" >> :recorded "2021-07-07"^^xsd:date .
> :a :name "Alice"
> ```

and RDF-star graph contains three asserted triples.

### 3.2 Turtle-star

In this section, we present Turtle-star,
an extension of the Turtle format [TURTLE]
allowing the representation of RDF-star graphs.
For the sake of conciseness,
we only describe here the differences between Turtle-star and Turtle.

#### 3.2.1 Grammar

Turtle-star is defined to follow the [same grammar](https://www.w3.org/TR/turtle/#h3_sec-grammar-grammar) as Turtle, *except* for the [EBNF productions](https://www.w3.org/TR/xml/#sec-notation) specified below,
which replace the productions having the same number (if any) in the original grammar.

| [8]   | `objectList`   | ::= | object annotation`? (` object annotation`? )*` |
| ----- | -------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [10]  | `subject`      | ::= | [iri](https://www.w3.org/TR/turtle/#grammar-production-iri) `\| \|` [BlankNode](https://www.w3.org/TR/turtle/#grammar-production-BlankNode) [collection](https://www.w3.org/TR/turtle/#grammar-production-collection) quotedTriple |
| [12]  | `object`       | ::= | [iri](https://www.w3.org/TR/turtle/#grammar-production-iri) `\| \|` [BlankNode](https://www.w3.org/TR/turtle/#grammar-production-BlankNode) [collection](https://www.w3.org/TR/turtle/#grammar-production-collection) [blankNodePropertyList](https://www.w3.org/TR/turtle/#grammar-production-blankNodePropertyList) [literal](https://www.w3.org/TR/turtle/#grammar-production-literal) quotedTriple |
| [27t] | `quotedTriple` | ::= | `'<<' '>>'` qtSubject [verb](https://www.w3.org/TR/turtle/#grammar-production-verb) qtObject |
| [28t] | `qtSubject`    | ::= | [iri](https://www.w3.org/TR/turtle/#grammar-production-iri) `\| \|` [BlankNode](https://www.w3.org/TR/turtle/#grammar-production-BlankNode) quotedTriple |
| [29t] | `qtObject`     | ::= | [iri](https://www.w3.org/TR/turtle/#grammar-production-iri) `\| \|` [BlankNode](https://www.w3.org/TR/turtle/#grammar-production-BlankNode) [literal](https://www.w3.org/TR/turtle/#grammar-production-literal) quotedTriple |
| [30t] | `annotation`   | ::= | `'{\|' '\|}'` [predicateObjectList](https://www.w3.org/TR/turtle/#grammar-production-predicateObjectList)                                                                                                |

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The complete grammar may be found in § C.1 Turtle-Star EBNF Grammar (§C.1).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The changes are that `subject` and `object` productions
> have been extended to accept quoted triples,
> which are described by the new productions 27t to 30t.
> Note that quoted triples accept a more restricted range of [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) and [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) expressions
> than asserted triples.
> Additionally, the `objectList` production
> now accepts an optional annotation after each [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object).

#### 3.2.2 Parsing

A Turtle-star parser is similar to a Turtle parser
as defined in [Section 7 of the Turtle specification](https://www.w3.org/TR/turtle/#h2_sec-parsing) [TURTLE],
with an additional item in its state :

- RDF-star Term *curObject* —
  The *curObject* is bound to the `qtObject` production.

Additionally, the [*curSubject*](https://www.w3.org/TR/turtle/#curSubject) can be bound to any RDF-star term (including a quoted triple).

A *Turtle-star document* defines an RDF-star graph composed of a set of RDF-star triples.
The `subject` and `qtSubject` productions set the *curSubject*.
The [`verb`](https://www.w3.org/TR/turtle/#grammar-production-verb) production
sets the [*curPredicate*](https://www.w3.org/TR/turtle/#curPredicate).
The `object` and `qtObject` productions
set the *curObject*.
Finishing the `object` production,
an RDF-star triple *curSubject* *curPredicate* *curObject* is produced
(added to the RDF-star graph).

Beginning the `quotedTriple` production
records the *curSubject* and *curPredicate*.
Finishing the `quotedTriple` production
yields the RDF-star triple *curSubject* *curPredicate* *curObject* and restores the recorded values of *curSubject* and *curPredicate*.

Beginning the `annotation` production
records the *curSubject* and *curPredicate*,
and sets the *curSubject* to the RDF-star triple *curSubject* *curPredicate* *curObject*.
Finishing the `annotation` production
restores the recorded values of *curSubject* and *curPredicate*.

All other productions *MUST* be handled as specified
by [Section 7 of the Turtle specification](https://www.w3.org/TR/turtle/#h2_sec-parsing) [TURTLE],
while still applying the changes above recursively.

##### 3.2.2.1 Discussion

*This section is non-normative.*

This section describes parser behavior when parsing
a Turtle-star document that contains quoted triples and annotations.

Consider a Turtle-star document that describes an RDF triple,
and also uses that triple as a quoted triple as the subject of another RDF-star triple:
> **Example:**
>
> Example 11: Turtle-star quoted triples
>
>
>
> ```
> BASE <http://example.org/>
> PREFIX : <#>
> _:a :name "Alice" .
> << _:a :name "Alice" >> :statedBy :bob .
> ```

The usual process of parsing a Turtle document
applies with the addition of matching the quoted triple `<< _:a :name "Alice" >>` as part of the `subject` production.
The resulting RDF-star graph consists of two RDF-star triples:

1. (*b*, `http://example.org/#name`, `"Alice"`),
   where *b* is a blank node
2. ((*b*, `http://example.org/#name`, `"Alice"`), `http://example.org/#statedBy`, `http://example.org/#bob/`),
   where *b* is the same blank node

Because the above example includes the triple (*b*, `http://example.org/#name`, `"Alice"`)
as an asserted triple,
the same RDF-star graph may also be represented
by using the Turtle-star annotation syntax as follows:
> **Example:**
>
> Example 12: Turtle-star annotated triples
>
>
>
> ```
> BASE <http://example.org/>
> PREFIX : <#>
> _:a :name "Alice" {| :statedBy :bob |} .
> ```

In this case, the `objectList` production
matches the `annotation` production on `{| :source :bob |}` after parsing the `object` production on `"Alice"`.
At this point, the *curSubject*, *curPredicate*, and *curObject* are saved,
and a new RDF-star triple `_:a :name "Alice"` is created
and used as *curSubject* while processing
the `annotation` production.

### 3.3 TriG-star

This section describes TriG-star,
a minimal extension of the TriG format [TRIG]
using the same production updates described in § 3.2 Turtle-star (§3.2).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> RDF-star describes quoted triples,
> which are not necessarily present in any [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph),
> or within the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph).

A *TriG-star document* defines an RDF-star dataset, composed of
a single [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) and zero or more [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph),
all of which are RDF-star graphs.

#### 3.3.1 Grammar

TriG-star is defined to follow the [same grammar](https://www.w3.org/TR/trig/#grammar-ebnf) as TriG, *except* for the [EBNF productions](https://www.w3.org/TR/xml/#sec-notation) specified below,
which replace the productions having the same number (if any) in the original grammar.

The TriG-star grammar contains exactly the same production updates
described in § 3.2.1 Grammar (§3.2.1) with an additional change to the triplesOrGraph production.

| [3g]  | `triplesOrGraph` | ::= | [labelOrSubject](https://www.w3.org/TR/trig/#grammar-production-labelOrSubject) `( \|` [wrappedGraph](https://www.w3.org/TR/trig/#grammar-production-wrappedGraph) [predicateObjectList](https://www.w3.org/TR/trig/#grammar-production-predicateObjectList) `\|` quotedTriple [predicateObjectList](https://www.w3.org/TR/trig/#grammar-production-predicateObjectList) `'.'` |
| ----- | ---------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [8]   | `objectList`     | ::= | object annotation`? (` object annotation`? )*` |
| [10]  | `subject`        | ::= | [iri](https://www.w3.org/TR/trig/#grammar-production-iri) `\| \|` [BlankNode](https://www.w3.org/TR/trig/#grammar-production-BlankNode) [collection](https://www.w3.org/TR/trig/#grammar-production-collection) quotedTriple |
| [12]  | `object`         | ::= | [iri](https://www.w3.org/TR/trig/#grammar-production-iri) `\| \|` [BlankNode](https://www.w3.org/TR/trig/#grammar-production-BlankNode) [collection](https://www.w3.org/TR/trig/#grammar-production-collection) [blankNodePropertyList](https://www.w3.org/TR/trig/#grammar-production-blankNodePropertyList) [literal](https://www.w3.org/TR/trig/#grammar-production-literal) quotedTriple |
| [27t] | `quotedTriple`   | ::= | `'<<' '>>'` qtSubject [verb](https://www.w3.org/TR/turtle/#grammar-production-verb) qtObject |
| [28t] | `qtSubject`      | ::= | [iri](https://www.w3.org/TR/trig/#grammar-production-iri) `\| \|` [BlankNode](https://www.w3.org/TR/trig/#grammar-production-BlankNode) quotedTriple |
| [29t] | `qtObject`       | ::= | [iri](https://www.w3.org/TR/trig/#grammar-production-iri) `\| \|` [BlankNode](https://www.w3.org/TR/trig/#grammar-production-BlankNode) [literal](https://www.w3.org/TR/trig/#grammar-production-literal) quotedTriple |
| [30t] | `annotation`     | ::= | `'{\|' '\|}'` [predicateObjectList](https://www.w3.org/TR/trig/#grammar-production-predicateObjectList)                                                                                                  |

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The complete grammar may be found in § C.2 TriG-Star EBNF Grammar (§C.2).

#### 3.3.2 Parsing

TriG-star parsing uses the same updates described
in § 3.2.2 Parsing (§3.2.2) as applied to [Section 5 of the TriG specification](https://www.w3.org/TR/trig/#sec-parsing) [TRIG].
> **Note:**
>
> > **Note:**
> >
> > Note
>
> As with Turtle-star,
> the `quotedTriple` and `annotation` are used to set either the *curSubject* or *curObject*,
> and do not directly add the associated quoted triple to *curGraph*.
> Subsequent productions which use either *curSubject* or *curObject* may result in adding triples to *curGraph*.

A conforming TriG-star parser *MUST* parse any
valid **TriG document** and any
valid Turtle-star document in addition
to the Turtle-star grammar (§3.2.1) productions contained within a [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph).

#### 3.3.3 Discussion

*This section is non-normative.*

TriG-star allows the same expressivity as Turtle-star
with the addition of allowing quoted triples and annotations within named graphs.
> **Example:**
>
> Example 13: TriG-star annotated triples
>
>
>
> ```
> BASE <http://example.org/>
> PREFIX : <#>
> :G {
>   _:a :name "Alice" {| :statedBy :bob |} .
> }
> ```

The resulting RDF-star dataset consists of
an empty default graph, and a graph named `http://example.org/#G` with two RDF-star triples:

1. (*b*, `http://example.org/#name`, `"Alice"`),
   where *b* is a blank node
2. ((*b*, `http://example.org/#name`, `"Alice"`), `http://example.org/#statedBy`, `http://example.org/#bob/`),
   where *b* is the same blank node

### 3.4 N-Triples-star

This section describes N-Triples-star,
a minimal extension of the N-Triples format [N-TRIPLES]
allowing a [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) or an [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) of an RDF-star triple to be a quoted triple.

#### 3.4.1 Grammar

N-Triples-star is defined to follow the same grammar as
the [N-Triples Grammar](https://www.w3.org/TR/n-triples/#n-triples-grammar),
except for the [EBNF productions](https://www.w3.org/TR/xml/#sec-notation) specified below,
which replace the productions having the same number
(if any) in the original grammar.

| [3]  | `subject`      | ::= | [IRIREF](https://www.w3.org/TR/n-triples/#grammar-production-IRIREF) `\| \|` [BLANK_NODE_LABEL](https://www.w3.org/TR/n-triples/#grammar-production-BLANK_NODE_LABEL) quotedTriple |
| ---- | -------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [5]  | `object`       | ::= | [IRIREF](https://www.w3.org/TR/n-triples/#grammar-production-IRIREF) `\| \|` [BLANK_NODE_LABEL](https://www.w3.org/TR/n-triples/#grammar-production-BLANK_NODE_LABEL) [literal](https://www.w3.org/TR/n-triples/#grammar-production-literal) quotedTriple |
| [7t] | `quotedTriple` | ::= | "<<" subject [predicate](https://www.w3.org/TR/n-triples/#grammar-production-predicate) object ">>" |

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The complete grammar may be found in § C.3 N-Triples-Star EBNF Grammar (§C.3).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The changes are that `subject` and `object` productions
> have been extended to accept quoted triples,
> which are described by the new production 7.

#### 3.4.2 Parsing

In contrast to [N-TRIPLES],
N-Triples-star allows recursion on the `subject` and `object` productions.

An *N-Triples-star document* defines an RDF-star graph composed of a set of RDF-star triples.
The [`triple`](https://www.w3.org/TR/n-triples/#grammar-production-triple) production
produces an RDF-star triple composed of a `subject`, [`predicate`](https://www.w3.org/TR/n-triples/#grammar-production-predicate),
and `object`.

In addition to the [Term Constructors](https://www.w3.org/TR/n-triples/#sec-parsing-terms) defined in [N-TRIPLES],
an additional constructor is defined for `quotedTriple` of type RDF-star triple defined by the terms constructed
for `subject`, [`predicate`](https://www.w3.org/TR/n-triples/#grammar-production-predicate),
and `object`.

All other productions *MUST* be handled as specified by [Section 8.1 of the N-Triples specification](https://www.w3.org/TR/n-triples/#sec-parsing-terms) [N-TRIPLES],
while still applying the changes above recursively.

### 3.5 N-Quads-star

The [N-QUADS] format is extended to describe the
N-Quads-star format using the same production updates described in the N-Triples-star Grammar (§3.4.1).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The complete grammar may be found in § C.4 N-Quads-Star EBNF Grammar (§C.4).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> As RDF-star describes quoted triples and not quoted quads,
> the [`graphLabel`](https://www.w3.org/TR/n-quads/#grammar-production-graphLabel) component of an N-Quads [`statement`](https://www.w3.org/TR/n-quads/#grammar-production-statement) does not apply to the `quotedTriple` component.

An *N-Quads-star document* defines an RDF-star dataset,
composed of a single [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) and zero or more [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph),
all of which are RDF-star graphs.

A conforming N-Quads-star parser *MUST* parse any valid **N-Quads document** and additionally parse the `subject` and `object` productions
from N-Triples-star to generate RDF-star triples which are
added to either the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) or associated [named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph), as appropriate.

### 3.6 Other Concrete Syntaxes

*This section is non-normative.*

While this document specifies a small number of concrete syntaxes,
nothing prevents other concrete syntaxes of RDF-star from being proposed. In particular, syntaxes such as
RDF/XML [RDF-SYNTAX-GRAMMAR],
and JSON-LD [JSON-LD],
could be extended to support RDF-star.

## 4. SPARQL-star Query Language

This Section introduces SPARQL-star, which is an RDF-star-aware extension of the RDF query language SPARQL [SPARQL11-QUERY]; i.e., SPARQL-star can be used to query RDF-star graphs.

### 4.1 Initial Definitions

In the following, we introduce a number of SPARQL-star-specific definitions, which rely on the following notions, defined in [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/) [SPARQL11-QUERY]: *[query variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable)*, *[triple pattern](https://www.w3.org/TR/sparql11-query/#defn_TriplePattern)*, *[property path pattern](https://www.w3.org/TR/sparql11-query/#defn_PropertyPathPattern)*, *[property path expression](https://www.w3.org/TR/sparql11-query/#defn_PropertyPathExpr)*,
and *[solution mapping](https://www.w3.org/TR/sparql11-query/#defn_sparqlSolutionMapping)*.

A *SPARQL-star triple pattern* is a 3-tuple that is defined recursively as follows:

1. Every SPARQL [triple pattern](https://www.w3.org/TR/sparql11-query/#defn_TriplePattern) is a SPARQL-star triple pattern;
2. If *t* and *t'* are SPARQL-star triple patterns, *x* is an [RDF term](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term) or a [query variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable), and *p* is an [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) or a [query variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable), then (*t*, *p*, *x*), (*x*, *p*, *t*), and (*t*, *p*, *t'*) are SPARQL-star triple patterns.

As for RDF-star triples, a SPARQL-star triple pattern *MUST NOT* contain itself.

A *SPARQL-star basic graph pattern* (BGP-star) is a set of SPARQL-star triple patterns.

A *SPARQL-star property path pattern* is a 3-tuple (*s*,*p*,*o*) where

- *s* is either an [RDF term](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term), a [query variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable), or a SPARQL-star triple pattern,
- *p* is a [property path expression](https://www.w3.org/TR/sparql11-query/#defn_PropertyPathExpr), and
- *o* is either an [RDF term](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term), a [query variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable), or a SPARQL-star triple pattern.

A *SPARQL-star solution mapping* μ is a partial function from the set of all [query variables](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable) to the set of all RDF-star terms.
The domain of μ, denoted by dom(μ), is the set of [query variables](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable) for which μ is defined.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The notion of a SPARQL-star solution mapping extends the notion of a standard SPARQL [solution mapping](https://www.w3.org/TR/sparql11-query/#defn_sparqlSolutionMapping); that is, every SPARQL [solution mapping](https://www.w3.org/TR/sparql11-query/#defn_sparqlSolutionMapping) is a SPARQL-star solution mapping. However, in contrast to SPARQL [solution mappings](https://www.w3.org/TR/sparql11-query/#defn_sparqlSolutionMapping), SPARQL-star solution mappings may map [variables](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable) also to RDF-star triples.

All notions related to SPARQL solution mappings carry over naturally to SPARQL-star solution mappings. In particular, the definition of *[compatibility](https://www.w3.org/TR/sparql11-query/#defn_algCompatibleMapping)* extends naturally to SPARQL-star solution mappings: two SPARQL-star solution mappings μ1 and μ2 are compatible if, for every variable v that is both in dom(μ1) and in dom(μ2), μ1(v) and μ2(v) are the same RDF-star term.
In this case, μ1 ∪ μ2 is also a SPARQL-star solution mapping.
Moreover, for any SPARQL-star solution mapping μ we write card[Ω](μ) to denote the cardinality of μ in a multiset Ω of such mappings.
Finally, given a BGP-star *B* and a SPARQL-star solution mapping μ, we write μ(*B*) to denote the result of replacing every variable *v* in *B* for which μ is defined with μ(v).

Next, we aim to carry over the notion of [solutions for BGPs](https://www.w3.org/TR/sparql11-query/#BGPsparql) to BGP-star. To this end, we first define an auxiliary concept that carries over the notion of an [RDF instance mapping](https://www.w3.org/TR/rdf11-mt/#dfn-instance) [RDF11-MT] to RDF-star.

An *RDF-star instance mapping* σ is a partial function from the set of all [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) to the set of all RDF-star terms.
The domain of σ, denoted by dom(σ), is the set of [blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) for which σ is defined.

Similar to the corresponding notation for solution mappings, for an RDF-star instance mapping σ and a BGP-star *B* we write σ(*B*) to denote the result of replacing every blank node *b* in *B* for which σ is defined with σ(b).

Now we are ready to define the notion of solution for BGP-star.

Given a BGP-star *B* and an RDF-star graph *G*, a SPARQL-star solution mapping μ is a *solution for the BGP-star* *B* **over** *G* if it has the following two properties

- dom(μ) is equivalent to the set of query variables in *B*, and
- there exists an RDF-star instance mapping σ such that dom(σ) is equivalent to the set of blank nodes in *B* and μ(σ(*B*)) is a subgraph of *G*.

### 4.2 Grammar

SPARQL-star is defined to follow the [same grammar](https://www.w3.org/TR/sparql11-query/#sparqlGrammar) as SPARQL 1.1, *except* for the [EBNF productions](https://www.w3.org/TR/xml/#sec-notation) specified below, which replace the productions having the same number (if any) in the original grammar. The parts in which these productions differ from the corresponding productions in the original grammar are marked in bold font. Productions [174](https://www.w3.org/2021/12/rdf-star.html#rQuotedTP) and following have been added and have no counterpart in the original grammar.

| [65]  | `DataBlockValue`         | ::= | QuotedTriple `\|` [iri](https://www.w3.org/TR/sparql11-query/#riri) `\| \|` [RDFLiteral](https://www.w3.org/TR/sparql11-query/#rRDFLiteral) [NumericLiteral](https://www.w3.org/TR/sparql11-query/#rNumericLiteral) [BooleanLiteral](https://www.w3.org/TR/sparql11-query/#rBooleanLiteral) |
| ----- | ------------------------ | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [75]  | `TriplesSameSubject`     | ::= | VarOrTermOrQuotedTP [PropertyListNotEmpty](https://www.w3.org/TR/sparql11-query/#rPropertyListNotEmpty) `\|` [TriplesNode](https://www.w3.org/TR/sparql11-query/#rTriplesNode) [PropertyList](https://www.w3.org/TR/sparql11-query/#rPropertyList) |
| [80]  | `Object`                 | ::= | [GraphNode](https://www.w3.org/TR/sparql11-query/#rGraphNode) AnnotationPattern`?`                                                        |
| [81]  | `TriplesSameSubjectPath` | ::= | VarOrTermOrQuotedTP [PropertyListPathNotEmpty](https://www.w3.org/TR/sparql11-query/#rPropertyListPathNotEmpty) `\|` [TriplesNode](https://www.w3.org/TR/sparql11-query/#rTriplesNode) [PropertyListPath](https://www.w3.org/TR/sparql11-query/#rPropertyListPath) |
| [87]  | `ObjectPath`             | ::= | GraphNodePath AnnotationPatternPath`?`                                     |
| [104] | `GraphNode`              | ::= | VarOrTermOrQuotedTP `\|` [TriplesNode](https://www.w3.org/TR/sparql11-query/#rTriplesNodePath)                                          |
| [105] | `GraphNodePath`          | ::= | VarOrTermOrQuotedTP `\|` [TriplesNodePath](https://www.w3.org/TR/sparql11-query/#rTriplesNodePath)                                      |
| [119] | `PrimaryExpression`      | ::= | [BrackettedExpression](https://www.w3.org/TR/sparql11-query/#rBrackettedExpression) `\| \|` [BuiltInCall](https://www.w3.org/TR/sparql11-query/#rBuiltInCall) [iriOrFunction](https://www.w3.org/TR/sparql11-query/#ririOrFunction) [RDFLiteral](https://www.w3.org/TR/sparql11-query/#rRDFLiteral) [NumericLiteral](https://www.w3.org/TR/sparql11-query/#rNumericLiteral) [BooleanLiteral](https://www.w3.org/TR/sparql11-query/#rBooleanLiteral) [Var](https://www.w3.org/TR/sparql11-query/#rVar) `\|` ExprQuotedTP |
| [121] | `BuiltInCall`            | ::= | [Aggregate](https://www.w3.org/TR/sparql11-query/#rAggregate) `\|` `'STR'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'LANG'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'LANGMATCHES'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'DATATYPE'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'BOUND'` `'('` [Var](https://www.w3.org/TR/sparql11-query/#rVar) `')'` `\|` `'IRI'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'URI'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'BNODE'` `(` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` [NIL](https://www.w3.org/TR/sparql11-query/#rNIL) `)` `\|` `'RAND'` [NIL](https://www.w3.org/TR/sparql11-query/#rNIL) `\|` `'ABS'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'CEIL'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'FLOOR'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'ROUND'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'CONCAT'` [ExpressionList](https://www.w3.org/TR/sparql11-query/#rExpressionList) `\|` [SubstringExpression](https://www.w3.org/TR/sparql11-query/#rSubstringExpression) `\|` `'STRLEN'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` [StrReplaceExpression](https://www.w3.org/TR/sparql11-query/#rStrReplaceExpression) `\|` `'UCASE'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'LCASE'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'ENCODE_FOR_URI'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'CONTAINS'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'STRSTARTS'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'STRENDS'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'STRBEFORE'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'STRAFTER'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'YEAR'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'MONTH'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'DAY'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'HOURS'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'MINUTES'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'SECONDS'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'TIMEZONE'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'TZ'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'NOW'` [NIL](https://www.w3.org/TR/sparql11-query/#rNIL) `\|` `'UUID'` [NIL](https://www.w3.org/TR/sparql11-query/#rNIL) `\|` `'STRUUID'` [NIL](https://www.w3.org/TR/sparql11-query/#rNIL) `\|` `'MD5'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'SHA1'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'SHA256'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'SHA384'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'SHA512'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'COALESCE'` [ExpressionList](https://www.w3.org/TR/sparql11-query/#rExpressionList) `\|` `'IF'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'STRLANG'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'STRDT'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'sameTerm'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'isIRI'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'isURI'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'isBLANK'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'isLITERAL'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'isNUMERIC'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` [RegexExpression](https://www.w3.org/TR/sparql11-query/#rRegexExpression) `\|` [ExistsFunc](https://www.w3.org/TR/sparql11-query/#rExistsFunc) `\|` [NotExistsFunc](https://www.w3.org/TR/sparql11-query/#rNotExistsFunc) `\|` `'TRIPLE'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `','` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'SUBJECT'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'PREDICATE'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'OBJECT'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` `\|` `'isTRIPLE'` `'('` [Expression](https://www.w3.org/TR/sparql11-query/#rExpression) `')'` |
| [174] | `QuotedTP`               | ::= | `'<<' '>>'` qtSubjectOrObject [Verb](https://www.w3.org/TR/sparql11-query/#rVerb) qtSubjectOrObject |
| [175] | `QuotedTriple`           | ::= | `'<<' (` DataValueTerm [iri](https://www.w3.org/TR/sparql11-query/#riri) DataValueTerm |
| [176] | `qtSubjectOrObject`      | ::= | [Var](https://www.w3.org/TR/sparql11-query/#rVar) `\| \|` [BlankNode](https://www.w3.org/TR/sparql11-query/#rBlankNode) [iri](https://www.w3.org/TR/sparql11-query/#riri) [RDFLiteral](https://www.w3.org/TR/sparql11-query/#rRDFLiteral) [NumericLiteral](https://www.w3.org/TR/sparql11-query/#rNumericLiteral) [BooleanLiteral](https://www.w3.org/TR/sparql11-query/#rBooleanLiteral) QuotedTP |
| [177] | `DataValueTerm`          | ::= | [iri](https://www.w3.org/TR/sparql11-query/#riri) `\| \|` [RDFLiteral](https://www.w3.org/TR/sparql11-query/#rRDFLiteral) [NumericLiteral](https://www.w3.org/TR/sparql11-query/#rNumericLiteral) [BooleanLiteral](https://www.w3.org/TR/sparql11-query/#rBooleanLiteral) QuotedTriple |
| [178] | `VarOrTermOrQuotedTP`    | ::= | [Var](https://www.w3.org/TR/sparql11-query/#rVar) `\| \|` [GraphTerm](https://www.w3.org/TR/sparql11-query/#rGraphTerm) QuotedTP                   |
| [179] | `AnnotationPattern`      | ::= | `'{\|' '\|}'` [PropertyListNotEmpty](https://www.w3.org/TR/sparql11-query/#rPropertyListNotEmpty)                                                                                                        |
| [180] | `AnnotationPatternPath`  | ::= | `'{\|' '\|}'` [PropertyListPathNotEmpty](https://www.w3.org/TR/sparql11-query/#rPropertyListPathNotEmpty)                                                                                                |
| [181] | `ExprQuotedTP`           | ::= | `'<<' '>>'` ExprVarOrTerm [Verb](https://www.w3.org/TR/sparql11-query/#rVerb) ExprVarOrTerm |
| [182] | `ExprVarOrTerm`          | ::= | [iri](https://www.w3.org/TR/sparql11-query/#riri) `\| \|` [RDFLiteral](https://www.w3.org/TR/sparql11-query/#rRDFLiteral) [NumericLiteral](https://www.w3.org/TR/sparql11-query/#rNumericLiteral) [BooleanLiteral](https://www.w3.org/TR/sparql11-query/#rBooleanLiteral) [Var](https://www.w3.org/TR/sparql11-query/#rVar) ExprQuotedTP |

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The complete grammar may be found in § C.5 SPARQL-Star EBNF Grammar (§C.5).

This introduces a notation for *quoted triple patterns* (production [174](https://www.w3.org/2021/12/rdf-star.html#rQuotedTP)),
which is similar to the one defined for quoted triples in § 3.2 Turtle-star (§3.2),
but accepting also [variables](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable).
These quoted triple patterns are allowed in both the subject position ([75](https://www.w3.org/2021/12/rdf-star.html#rTriplesSameSubject), [81](https://www.w3.org/2021/12/rdf-star.html#rTriplesSameSubjectPath)) and the object position ([80](https://www.w3.org/2021/12/rdf-star.html#rObject), [87](https://www.w3.org/2021/12/rdf-star.html#rObjectPath))
of SPARQL-star triple patterns, as well as in [the short-hand notation for querying collections](https://www.w3.org/TR/sparql11-query/#collections) ([102](https://www.w3.org/TR/sparql11-query/#rCollection), [103](https://www.w3.org/TR/sparql11-query/#rCollectionPath)).

Additionally, production [65](https://www.w3.org/2021/12/rdf-star.html#rDataBlockValue) for values that can be used in the [VALUES clause](https://www.w3.org/TR/sparql11-query/#inline-data) is extended to permit RDF-star triples as possible values, and the set of available built-in functions is extended with the five functions TRIPLE, SUBJECT, PREDICATE, OBJECT, and isTRIPLE ([121](https://www.w3.org/2021/12/rdf-star.html#rBuiltInCall)) that are defined in § 4.4 Function and Operator Definitions (§4.4).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> [As defined for all keywords in SPARQL](https://www.w3.org/TR/sparql11-query/#sparqlGrammar), the names of the five new built-in functions added by SPARQL-star are matched in a case-insensitive manner.

Yet another extension is that both the Object and the ObjectPath productions now accept an optional *annotation pattern* after each object. The purpose of this feature is to enable users to use the same kind of annotation syntax that is supported in Turtle-star. As in the case of Turtle-star, the annotation syntax in SPARQL-star is purely syntactic sugar that has to be processed in accordance to the first expansion rule in § 4.3.2 Expand Syntax Forms (§4.3.2).

A **restriction** to the use of the annotation syntax in SPARQL-star exists that is not captured by the grammar as defined above: An AnnotationPatternPath may be added only to SPARQL-star property path patterns in which the [property path expression](https://www.w3.org/TR/sparql11-query/#defn_PropertyPathExpr) is a [PredicatePath](https://www.w3.org/TR/sparql11-query/#pp-language) (i.e., a single IRI) or the keyword `a` (as a [short form for the IRI `rdf:type`](https://www.w3.org/TR/sparql11-query/#abbrevRdfType)). Hence, a query such as the following violates this restriction and, thus, is *invalid*.
> **Example:**
>
> Example 14
>
>
>
> ```
> SELECT * WHERE {
>     ?s :p/:q ?o {| ?pp ?oo |}.
> }
> ```

While annotation patterns must not be added to property path patterns other than the ones permitted by the restriction above, it is possible to use property path expressions within annotation patterns (but without violating the restriction in the case of nested annotation patterns). For instance, the following query is valid.
> **Example:**
>
> Example 15
>
>
>
> ```
> SELECT * WHERE {
>     ?s ?p ?o {| :p/:q ?oo |}.
> }
> ```

### 4.3 Translation to the Algebra

Based on the SPARQL grammar, the SPARQL specification "defines the process of converting graph patterns and solution modifiers in a SPARQL query string into a SPARQL algebra expression" [[SPARQL11-QUERY, Section 18.2](https://www.w3.org/TR/sparql11-query/#sparqlQuery)]. This process must be adjusted to consider the extended grammar introduced above (§4.2). In the following, any step of the conversion process that requires adjustment is discussed.

#### 4.3.1 Variable Scope

As a basis of the translation, the SPARQL specification introduces a notion of [in-scope variables](https://www.w3.org/TR/sparql11-query/#variableScope). To cover the new syntax elements introduced in § 4.2 Grammar (§4.2) this notion *MUST* be extended as follows.

- A [variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable) is in-scope of a BGP-star *B* if the [variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable) occurs in *B*, which includes an occurrence in any quoted triple pattern in *B* (independent of the level of nesting).
- A [variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable) is in-scope of a [property path pattern](https://www.w3.org/TR/sparql11-query/#defn_PropertyPathPattern) if the variable occurs in that pattern, which includes an occurrence in any quoted triple pattern in the pattern (independent of the level of nesting).

#### 4.3.2 Expand Syntax Forms

The translation process starts with expanding "abbreviations for IRIs and triple patterns" [[SPARQL11-QUERY, Section 18.2.2.1](https://www.w3.org/TR/sparql11-query/#sparqlExpandForms)]. This step *MUST* be extended in three ways:

1. Annotation patterns *MUST* be replaced by additional SPARQL-star triple patterns that have the annotated triple pattern as a quoted triple pattern in their subject position.
   > **Example:**
   >
   > Example 16: Expanding annotations to quoted triple patterns
   >
   > For instance, the following syntax expression:
   >
   > ```
   > ?x :p :o1 {| :ap1 ?y;
   >              :ap2 ?z |} ,
   >       :o2 {| :ap3 ?z |} .
   >
   > ?x :p :o3 {| :ap4/:ap5 ?w } .
   > ```
   >
   > must be replaced by
   >
   > ```
   > ?x :p :o1, o2 .
   > <<?x :p :o1>> :ap1 ?y ;
   >               :ap2 ?z .
   > <<?x :p :o2>> :ap3 ?z .
   >
   > ?x :p :o3 .
   > <<?x :p :o3>> :ap4/:ap5 ?w .
   > ```

2. Abbreviations for [triple patterns](https://www.w3.org/TR/sparql11-query/#defn_TriplePattern) with quoted triple patterns *MUST* be expanded as if each quoted triple pattern was a [variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable) (or an [RDF term](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term)).
   > **Example:**
   >
   > Example 17: Expanding abbreviations for triple patterns with quoted triple patterns
   >
   > For instance, the following syntax expression:
   >
   > ```
   > <<?c a owl:Class>> dct:source ?src ;
   >     :entailing <<?c a rdfs:Class>> .
   > ```
   >
   > must be expanded to
   >
   > ```
   > <<?c a owl:Class>> dct:source ?src .
   > <<?c a owl:Class>> :entailing <<?c a rdfs:Class>> .
   > ```

3. Abbreviations for IRIs in all quoted triple patterns *MUST* be expanded.
   > **Example:**
   >
   > Example 18: Expanding IRI abbreviations
   >
   > For instance, the quoted triple pattern
   >
   > ```
   > <<?c a rdfs:Class>>
   > ```
   >
   > must be expanded to
   >
   > ```
   > << ?c <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2000/01/rdf-schema#Class>>>
   > ```

#### 4.3.3 Translate Property Path Patterns

The [translation of property path patterns](https://www.w3.org/TR/sparql11-query/#sparqlTranslatePathPatterns) has to be adjusted because the extended grammar allows for SPARQL-star property path patterns whose subject or object is a SPARQL-star triple pattern.

The translation as specified in the W3C specification distinguishes four cases. The first three of these cases do not require adjustment because they are taken care of either by recursion or by the adjusted translation of basic graph patterns (as defined in § 4.3.4 Translate Basic Graph Patterns (§4.3.4) below). However, the fourth case *MUST* be adjusted as follows.

Let *X* *P* *Y* be a string that corresponds to the fourth case in [[SPARQL11-QUERY, Section 18.2.2.4](https://www.w3.org/TR/sparql11-query/#sparqlTranslatePathPatterns)]. Given the grammar introduced in § 4.2 Grammar (§4.2), *X* and *Y* may be an [RDF term](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term), a [variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable), or a quoted triple pattern, respectively (and *P* is a [property path expression](https://www.w3.org/TR/sparql11-query/#defn_PropertyPathExpr)). The string *X* *P* *Y* is translated to the algebra expression `Path`(*X’*,*P*,*Y’*) where *X’* and *Y’* are the result of calling a function named `Lift` for *X* and *Y*, respectively. For some input string *Z* (such as *X* or *Y*) that can be an [RDF term](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term), a [variable](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable), or a quoted triple pattern, the function `Lift` is defined recursively as follows:

1. If *Z* is a quoted triple pattern <<*S*,*P*,*O*>> then return the SPARQL-star triple pattern (`Lift`(*S*), *P*, `Lift`(*O*));
2. Otherwise, return *Z*.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The purpose of this translation step is to convert any property path pattern as can be written based on the extended grammar for SPARQL-star (cf. § 4.2 Grammar (§4.2)) into a SPARQL-star property path pattern as considered in the algebra. To this end, the function `Lift` translates every quoted triple pattern as can be written in the SPARQL-star syntax into a SPARQL-star triple pattern.

#### 4.3.4 Translate Basic Graph Patterns

After translating [property path patterns](https://www.w3.org/TR/sparql11-query/#defn_PropertyPathPattern), the translation process collects "any adjacent triple patterns [...] to form a basic graph pattern" [[SPARQL11-QUERY, Section 18.2.2.5](https://www.w3.org/TR/sparql11-query/#sparqlTranslateBasicGraphPatterns)]. This step has to be adjusted because [triple patterns](https://www.w3.org/TR/sparql11-query/#defn_TriplePattern) in the extended syntax may have a quoted triple pattern in their subject position or in their object position (or in both). To ensure that every result of this step is a BGP-star, before adding a [triple pattern](https://www.w3.org/TR/sparql11-query/#defn_TriplePattern) to its corresponding collection, its subject and object *MUST* be replaced by the result of calling function `Lift` for the subject and the object, respectively.

### 4.4 Function and Operator Definitions

SPARQL introduces operators and functions that can be used in an expression of a FILTER clause, a BIND clause, or a SELECT clause (see [Section 17.3](https://www.w3.org/TR/sparql11-query/#OperatorMapping) and [Section 17.4](https://www.w3.org/TR/sparql11-query/#SparqlOps) in [SPARQL11-QUERY]). While these operators and functions are defined to operate on [RDF terms](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term) and [query variables](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable), for SPARQL-star they have to be defined to operate on RDF-star terms and [query variables](https://www.w3.org/TR/sparql11-query/#defn_QueryVariable). To this end, when using these operators and functions in the context of SPARQL-star, their definitions as given in [Section 17.4](https://www.w3.org/TR/sparql11-query/#SparqlOps) of [SPARQL11-QUERY] are extended by assuming that any mention of `RDF term` as a data type for operands is understood to be the type of all RDF-star terms.

SPARQL-star introduces five new functions that are defined as follows (where the data types `RDF-star term` and `RDF-star triple` capture all RDF-star terms and all RDF-star triples,
respectively).

The modifications to functions and operators for triple terms are:

- Modified `sameTerm` function (§4.4.7) (SPARQL 1.1 [Section 17.4.1.8](https://www.w3.org/TR/sparql11-query/#func-sameTerm))
- New function `sparql-compare` (§4.4.8) for the `=` operator and other comparison mappings
- Modified `RDFterm-equal` (§4.4.9) (SPARQL 1.1 [Section 17.4.1.7](https://www.w3.org/TR/sparql11-query/#func-RDFterm-equal))
- Operator mapping for `=` and other operators (§4.4.10) (SPARQL 1.1 [Section 17.3](https://www.w3.org/TR/sparql11-query/#OperatorMapping))
- Modified `ORDER BY` (§4.4.11) (SPARQL 1.1 [Section 15.1](https://www.w3.org/TR/sparql11-query/#modOrderBy))

#### 4.4.1 TRIPLE

`RDF-star triple` `TRIPLE` ( `RDF-star term ` `term1`, `RDF-star term ` `term2`, `RDF-star term ` `term3` )

If the 3-tuple (`term1`, `term2`, `term3`) is an RDF-star triple, the function returns this triple. If the 3-tuple is not an RDF-star triple, then the function raises an error.

#### 4.4.2 SUBJECT

`RDF-star term` `SUBJECT` ( `RDF-star triple ` `triple` )

If `triple` is an RDF-star triple, the function returns the subject of this triple. Passing anything other than an RDF-star triple is an error.

#### 4.4.3 PREDICATE

`RDF-star term` `PREDICATE` ( `RDF-star triple ` `triple` )

If `triple` is an RDF-star triple, the function returns the predicate of this triple. Passing anything other than an RDF-star triple is an error.

#### 4.4.4 OBJECT

`RDF-star term` `OBJECT` ( `RDF-star triple ` `triple` )

If `triple` is an RDF-star triple, the function returns the object of this triple. Passing anything other than an RDF-star triple is an error.

#### 4.4.5 isTRIPLE

`xsd:boolean` `isTRIPLE` ( `RDF-star term ` `term` )

Returns `true` if `term` is an RDF-star triple. Returns `false` otherwise.

#### 4.4.6 Quoted Triple Expression

`RDF-star triple` `<<` `RDF-star term` `term1`, `RDF-star term` `term2`, `RDF-star term` `term3` `>>`

A Quoted Triple Expression `<<S P O>>`, where `S`, `P` and `O` conform to ExprVarOrTerm,
is evaluated as `TRIPLE(S, P, O)`.

#### 4.4.7 sameTerm

`xsd:boolean` `sameTerm` (`term`, `term`)

The function `sameTerm` is extended to support term comparison for
RDF-star triple terms by defining:

**Extended Definition: *`sameTerm`***

If both arguments are RDF-star triple terms:

`sameTerm(<<S1 P1 O1>>,               <<S2 P2 O2>>)`

is evaluated as

`sameTerm(S1, S2) && sameTerm(P1, P2) && sameTerm(O1, O2)`

This is applied recursively.

If one argument is an RDF-star triple term and the other argument is not,
the result is `false`.

#### 4.4.8 sparql-compare

The function `sparql-compare` is defined to support value-comparison
operators such as `=` and `ORDER BY`.

`xsd:boolean` `sparql-compare` (`RDF-star term`, `RDF-star term`)

The function `sparql-compare` returns `-1`, `0`, `1`, or throws an
error, based on the comparison of two RDF-star terms.
When comparing two RDF-star triple terms, comparison is
by pairwise comparison of subject, then predicate, then object.

**Definition: *`sparql-compare`***

- If neither A nor B is an RDF-star triple term,
  compare by SPARQL 1.1 operators `<`, `=`, `>`)
  and return the comparison value (`-1`, `0`, `+1`) or throw an error
  as defined by SPARQL 1.1.
- If either A or B is an RDF-star triple term, and the other is not
  an RDF-star triple term, then error.
- If `sparql-compare(SUBJECT(A), SUBJECT(B)) != 0`,
  then return this value.
- If `sparql-compare(PREDICATE(A), PREDICATE(B)) != 0`,
  then return this value.
- Return `sparql-compare(OBJECT(A), OBJECT(B))`

#### 4.4.9 RDFterm-equal

The function `RDFterm-equal` is the default dispatch for the `=` operator.

This is extended to cover RDF-star terms so that it returns `true` if term1 and term2 are both RDF-star triple
terms and `RDFterm-equal` is `true` for pairwise comparison of the component RDF terms.

**Extended Definition: *`RDFTerm-equal`***

If exactly one of the arguments is an RDF-star triple term,
return `false`.

If both arguments are RDF-star triple terms:

`RDFterm-equal(<<S1 P1 O1>>,               <<S2 P2 O2>>)`

is evaluated as

`RDFterm-equal(S1, S2) && RDFterm-equal(P1, P2) && RDFterm-equal(O1, O2)`

It produces an error if matching RDF terms in nested RDF triple terms when
both are literals but not the same RDF term. This is the same as the existing `RDFterm-equal`. Operator mapping overrides this behavior.

The case of two RDF-star triple terms is covered by the operator dispatch mappings
and covers cases involving literals.

#### 4.4.10 Operator Mappings

New operator mappings are added for RDF-star triple terms for section
SPARQL 1.1 Query [17.3 Operator Mapping](https://www.w3.org/TR/sparql11-query/#OperatorMapping)

*SPARQL Binary Operators (SPARQL\-star)*

| Operator          | Type(A)         | Type(B)         | Evaluation                                                                                                                                                                                               | Result type |
| ----------------- | --------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SPARQL-star Tests | | | | |
| A = B             | RDF triple term | RDF triple term | [op:numeric-equal](https://www.w3.org/TR/xpath-functions/#func-numeric-equal)(sparql-compare(A, B), 0)                                   | xsd:boolean |
| A != B            | RDF triple term | RDF triple term | [fn:not](https://www.w3.org/TR/xpath-functions/#func-not)([op:numeric-equal](https://www.w3.org/TR/xpath-functions/#func-numeric-equal)(sparql-compare(A, B), 0)) | xsd:boolean |
| A < B             | RDF triple term | RDF triple term | [op:numeric-equal](https://www.w3.org/TR/xpath-functions/#func-numeric-equal)(sparql-compare(A, B), -1)                                  | xsd:boolean |
| A <= B            | RDF triple term | RDF triple term | [fn:not](https://www.w3.org/TR/xpath-functions/#func-not)([op:numeric-equal](https://www.w3.org/TR/xpath-functions/#func-numeric-equal)(sparql-compare(A, B), 1)) | xsd:boolean |
| A > B             | RDF triple term | RDF triple term | [op:numeric-equal](https://www.w3.org/TR/xpath-functions/#func-numeric-equal)(sparql-compare(A, B), 1)                                   | xsd:boolean |
| A >= B            | RDF triple term | RDF triple term | [fn:not](https://www.w3.org/TR/xpath-functions/#func-not)([op:numeric-equal](https://www.w3.org/TR/xpath-functions/#func-numeric-equal)(sparql-compare(A, B), -1)) | xsd:boolean |

#### 4.4.11 Triple terms with ORDER BY

There is an added item to the ordering of terms when they would not
otherwise be ordered. RDF-star triple terms are placed last (highest).

1. (Lowest) no value assigned to the variable
   or expression in this solution.
2. Blank nodes
3. IRIs
4. RDF literals
5. *RDF-star triple terms*

RDF-star triple terms are compared using the `<` operator.

While SPARQL-star does not define a total ordering of all possible RDF-star terms,
implementations should provide some ordering for `ORDER BY` that does not change between queries if the data has not changed.

### 4.5 Examples and Discussion

*This section is non-normative.*

By the evaluation semantics of SPARQL-star as defined in § 4.6 Evaluation Semantics (§4.6), the five new built-in functions defined above can be used in exactly the same manner as [the functions defined in the SPARQL 1.1 spec](https://www.w3.org/TR/sparql11-query/#SparqlOps). For instance, the following SPARQL-star query retrieves every asserted triple that is both contained in the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) of the queried RDF-star dataset and has a quoted triple as its [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject).
> **Example:**
>
> Example 19
>
>
>
> ```
> SELECT ?t WHERE {
>   ?s ?p ?o .
>   BIND( TRIPLE(?s,?p,?o) AS ?t )
>   FILTER( isTRIPLE(SUBJECT(?t)) )
> }
> ```

Instead of accessing the subject of the triples in the FILTER after the BIND clause, as was done in the previous query, a semantically equivalent query may apply the FILTER directly on the variable `?s`, as follows:
> **Example:**
>
> Example 20
>
>
>
> ```
> SELECT ?t WHERE {
>   ?s ?p ?o .
>   BIND( TRIPLE(?s,?p,?o) AS ?t )
>   FILTER( isTRIPLE(?s) )
> }
> ```

While the triples that the previous example queries bind to variable `?t` occur in the queried data, the TRIPLE function (§4.4.1) can be used to construct triples that may not be in the data. For instance, the following query uses the subject of each asserted triple in the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph) of the queried RDF-star dataset to construct another triple, and bind it to the variable `?t`. Notice that the result of this query contains as many SPARQL-star solution mappings as there are asserted triples in the queried graph, and there may be duplicates in the result if multiple asserted triples have the same subject.
> **Example:**
>
> Example 21
>
>
>
> ```
> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
>
> SELECT ?t WHERE {
>   ?s ?p ?o .
>   BIND( TRIPLE(?s,rdf:type,rdfs:Resource) AS ?t )
> }
> ```

There are cases where the effects of using the new TRIPLE function are not immediately obvious just from its definition, particularly when considering the interplay of this function with the [BNODE function](https://www.w3.org/TR/sparql11-query/#func-bnode) when used within [GRAPH clauses](https://www.w3.org/TR/sparql11-query/#queryDataset). Some of these cases are discussed below.

Consider the following SPARQL-star query.
> **Example:**
>
> Example 22
>
>
>
> ```
> SELECT ( COUNT(?t1) AS ?t1Count )
>        ( COUNT(?t2) AS ?t2Count )
>        ( COUNT(?t3) AS ?t3Count )
>        ( COUNT(DISTINCT ?t1) AS ?t1DistCount )
>        ( COUNT(DISTINCT ?t2) AS ?t2DistCount )
>        ( COUNT(DISTINCT ?t3) AS ?t3DistCount )
> WHERE {
>   GRAPH ?g {
>     BIND( TRIPLE(BNODE(), :p, :o) AS ?t1 )
>     BIND( TRIPLE(BNODE("id"), :p, :o) AS ?t2 )
>     BIND( TRIPLE(:s, :p, :o) AS ?t3 )
>   }
> }
> ```

When evaluated over an RDF-star dataset that contains *n* [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph), where *n*>0, the GRAPH clause results in one SPARQL-star solution mapping per named graph. The SELECT clause collapses these *n* mappings into a single mapping that is defined for the six variables introduced in the SELECT clause. (If *n*=0, the query result is the empty set.) Each of these six variables is mapped to an integer-typed literal with values as follows. For each of `?t1Count`, `?t2Count`, and `?t3Count`, the value is *n*, because the variables `?t1`, `?t2`, and `?t3` are bound in each of the *n* solution mappings produced for the GRAPH clause. For the variable `?t1DistCount`, the value is also *n*, because the BIND clauses are evaluated *n* times (once for each named graph) and the subexpression BNODE() always creates a different new blank node; thus, the triples created for variable `?t1` are all different from one another. This is also the case if the BNODE function is used with an argument; i.e., the value of `?t2DistCount` is *n* too. In contrast, the variable `?t3` is mapped to the same triple within each evaluation of the third BIND clause; thus, the value for `?t3DistCount` is 1.

Notice that the BNODE function has to be used to create a blank node; simply writing a blank node directly in an expression [is not permitted](https://www.w3.org/TR/sparql11-query/#rExpression).

Notice as well that the preceding query is special in two ways: its GRAPH clause does not actually consider the content of the named graphs; and the expressions in the BIND clauses do not contain variables. In contrast, the GRAPH clause and the BIND clauses in the following query do.
> **Example:**
>
> Example 23
>
>
>
> ```
> PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
> PREFIX rdfg: <http://www.w3.org/2004/03/trix/rdfg-1/>
>
> SELECT ( COUNT(?t1) AS ?t1Count )
>        ( COUNT(?t2) AS ?t2Count )
> WHERE {
>   GRAPH ?g {
>     ?g rdf:type rdfg:Graph .
>     BIND( TRIPLE(?g, rdf:type, rdfs:Resource) AS ?t1 )
>     BIND( TRIPLE(?x, rdf:type, rdfs:Resource) AS ?t2 )
>   }
> }
> ```

For every RDF-star dataset with *n*>0 named graphs, the result of this query consists of a single SPARQL-star solution mapping that is defined for the three variables introduced in the SELECT clause. The value of `?t1Count` is the number of named graphs in the queried dataset that contain a triple of the form (*u*, `rdf:type`, `rdfg:Graph`) such that *u* is the name of the named graph in the dataset. The value of `?t2Count` is always 0 (zero), because evaluating the expression of the second BIND clause results in an error, because the variable `?x` is not bound in the scope of this evaluation. As a side note, evaluating the expression of the first BIND clause would also result in an error, if the variable `?g` was not mentioned inside the GRAPH clause (e.g., if the given triple pattern was not there).

### 4.6 Evaluation Semantics

The SPARQL specification defines a function "eval(*D*(*G*), algebra expression) as the evaluation of an algebra expression with respect to a dataset *D* having active graph *G*" [[SPARQL11-QUERY, Section 18.6](https://www.w3.org/TR/sparql11-query/#sparqlAlgebraEval)]. Recall that the dataset *D* in the context of SPARQL-star is an RDF-star dataset and, thus, the active graph *G* is an RDF-star graph, and so is any other graph in dataset *D*. The definition of the [eval](https://www.w3.org/TR/sparql11-query/#sparqlAlgebraEval) function is recursive; the base case of this definition for SPARQL-star are given as follows:

- For every BGP-star *B*, eval(*D*(*G*), *B*) is a multiset Ω that consists of all SPARQL-star solution mappings that are a solution for the BGP-star *B* over *G*. For every such mapping μ, card[Ω](μ) is the number of distinct RDF-star instance mappings σ such that dom(σ) is equivalent to the set of blank nodes in *B* and μ(σ(*B*)) is a subgraph of *G*. (For any SPARQL-star solution mapping μ' that is *not* a solution for *B* over *G*, we have that card[Ω](μ')=0; i.e., μ' is not in Ω.)

For any other algebra expression, the SPARQL specification defines algebra operators [SPARQL11-QUERY]. These definitions can be extended naturally to operate over multisets of SPARQL-star solution mappings (instead of ordinary [solution mappings](https://www.w3.org/TR/sparql11-query/#defn_sparqlSolutionMapping)). Given this extension, the recursive steps of the definition of the [eval](https://www.w3.org/TR/sparql11-query/#sparqlAlgebraEval) function for SPARQL-star are the same as in the SPARQL specification.

### 4.7 Query Result Formats

In SPARQL, queries can take four forms: *SELECT*, *CONSTRUCT*, *DESCRIBE*, and *ASK* - see [SPARQL1.1 Query, Section 16](https://www.w3.org/TR/sparql11-query/#QueryForms) [SPARQL11-QUERY]. The first of these returns a [sequence of solution mappings](https://www.w3.org/TR/sparql11-query/#defn_sparqlSolutionSequence) that contain variable bindings. The second and third both return an RDF graph, and the last returns a boolean value.

The result of the *ASK* query form is not changed by the introduction of RDF-star, and the result of the *CONSTRUCT* and *DESCRIBE* forms can be represented by §3.2 Turtle-star. However, since the *SELECT* form deals with returning individual RDF terms, the specific serialization formats for representing such query results need to be extended so that the new quoted triple RDF term can be represented. In this section, we propose extensions for the two most common formats for this purpose: [SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/sparql11-results-json/), and [SPARQL Query Results XML Format (Second Edition)](https://www.w3.org/TR/rdf-sparql-XMLres/).

#### 4.7.1 SPARQL-star Query Results JSON Format

The result of a SPARQL SELECT query is serialized in JSON as defined in [SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/sparql11-results-json/), which specifies a JSON representation of variable bindings to RDF terms (see [[sparql11-results-json, Section 3.2](https://www.w3.org/TR/sparql11-results-json/#select-results)]). To accommodate the new RDF term for quoted triples that RDF-star introduces, the table of RDF term JSON representations in [sparql11-results-json, Section 3.2.2](https://www.w3.org/TR/sparql11-results-json/#select-encode-terms) is extended with the following entry:

A quoted triple with subject RDF term `S`, predicate RDF term `P` and object RDF term `O`

```
{
  "type": "triple",
  "value": {
     "subject": S,
     "predicate": P,
     "object": O
  }
}
```

where `S`, `P` and `O` are encoded using the same format, recursively.
> **Example:**
>
> Example 24
>
> Consider the following RDF term, a quoted triple in Turtle-star syntax:
>
> ```
> << <http://example.org/alice> <http://example.org/name> "Alice" >>
> ```
>
> This term is represented in JSON as follows:
>
> ```
> {
>   "type": "triple",
>   "value": {
>      "subject": {
>         "type": "uri",
>         "value" "http://example.org/alice"
>      },
>      "predicate": {
>         "type": "uri",
>         "value" "http://example.org/name"
>      },
>      "object": {
>         "type": "literal",
>         "value" "Alice",
>         "datatype": "http://www.w3.org/2001/XMLSchema#string"
>      },
>   }
> }
> ```

#### 4.7.2 SPARQL-star Query Results XML Format

The result of a SPARQL SELECT query is serialized in XML as defined in [SPARQL Query Results XML Format (Second Edition)](https://www.w3.org/TR/rdf-sparql-XMLres/). This format proposes an XML representation of variable bindings to RDF terms.

To accommodate the new RDF term for quoted triples that RDF-star introduces, the list of RDF terms and their XML representations in [[RDF-SPARQL-XMLRES Section 2.3.1](https://www.w3.org/TR/rdf-sparql-XMLres/#results)] is extended as follows:

A quoted triple with subject term `S`, predicate term `P`, and object term `O`

```
<binding>
  <triple>
    <subject>S</subject>
    <predicate>P</predicate>
    <object>O</object>
  </triple>
</binding>
```

where `S`, `P` and `O` are encoded recursively, using the same format, without the enclosing `<binding>` tag.
> **Example:**
>
> Example 25
>
> Consider the following RDF term, a quoted triple in Turtle-star syntax:
>
> ```
> << <http://example.org/alice> <http://example.org/name> "Alice" >>
> ```
>
> This term is represented in XML as follows:
>
> ```
> <triple>
>     <subject>
>         <uri>http://example.org/alice</uri>
>     </subject>
>     <predicate>
>         <uri>http://example.org/name</uri>
>     </predicate>
>     <object>
>         <literal datatype='http://www.w3.org/2001/XMLSchema#string'>Alice</literal>
>     </object>
> </triple>
> ```

## 5. SPARQL-star Update

This section specifies SPARQL-star Update, an update language for RDF-star. This language extends SPARQL Update [SPARQL11-UPDATE], the update language for RDF, by adding RDF-star-specific features and semantics.

### 5.1 Informal Description

*This section is non-normative.*

While SPARQL Update operates over a [graph store](https://www.w3.org/TR/sparql11-update/#graphStore) that consists of RDF graphs, SPARQL-star Update extends the notion of graph store to contain RDF-star graphs instead of RDF graphs. That is, a [graph store](https://www.w3.org/TR/sparql11-update/#defn_graphStore) in the context of SPARQL-star Update contains one (unnamed) slot holding an RDF-star graph, referred to as the default graph, and zero or more named slots holding other RDF-star graphs, referred to as named graphs. Then, all [graph management operations](https://www.w3.org/TR/sparql11-update/#graphManagement) in SPARQL Update ([CREATE](https://www.w3.org/TR/sparql11-update/#create), [DROP](https://www.w3.org/TR/sparql11-update/#drop), [COPY](https://www.w3.org/TR/sparql11-update/#copy), [MOVE](https://www.w3.org/TR/sparql11-update/#move), [ADD](https://www.w3.org/TR/sparql11-update/#add)) carry over directly to SPARQL-star Update with the only difference being that in SPARQL-star Update these operations manage RDF-star graphs. For instance, the [CREATE](https://www.w3.org/TR/sparql11-update/#create) operation in SPARQL-star Update creates an RDF-star graph rather than a pure RDF graph. Similarly, the [graph update operations](https://www.w3.org/TR/sparql11-update/#graphUpdate) [LOAD](https://www.w3.org/TR/sparql11-update/#load) and [CLEAR](https://www.w3.org/TR/sparql11-update/#clear) in SPARQL-star Update operate with RDF-star graphs in the same way as their SPARQL Update counterparts operate with RDF graphs.

The only operations that SPARQL-star Update actually extends are the graph update operations [INSERT DATA](https://www.w3.org/TR/sparql11-update/#insertData), [DELETE DATA](https://www.w3.org/TR/sparql11-update/#deleteData), and [DELETE/INSERT](https://www.w3.org/TR/sparql11-update/#deleteInsert). This section describes these extensions informally. While this description focuses mainly on updates to the default graph, the operations can also be applied to the named graphs.

#### 5.1.1 INSERT DATA

The [INSERT DATA](https://www.w3.org/TR/sparql11-update/#insertData) operation can be used to add a given set of triples into the graph store. In the context of SPARQL-star Update, these triples may be RDF-star triples. As an example, consider the following INSERT DATA operation.
> **Example:**
>
> Example 26
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> INSERT DATA {
>   :alice :claims << :bob :age 23 >> .
> }
> ```

Suppose this INSERT DATA operation is executed over a graph store with an empty default graph. After executing this operation, the default graph contains the given (nested) RDF-star triple. Now, it is possible to query for this triple. For instance, the following SPARQL-star query returns a single solution mapping in which the variables ?p and ?a are mapped to the IRI `:alice` and the literal `23`, respectively.
> **Example:**
>
> Example 27
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> SELECT ?p ?a WHERE {
>   ?p :claims << :bob :age ?a >> .
> }
> ```

Notice that inserting a nested triple does not automatically also insert its quoted triple(s) as asserted triple(s) into the graph. Hence, in the previous example, after executing the given INSERT DATA operation, the default graph does *not* contain the triple `:bob :age 23`. In other words, a query such as the following would have an empty result.
> **Example:**
>
> Example 28
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> SELECT ?a WHERE {
>   :bob :age ?a .
> }
> ```

For a quoted triple to be present in the graph as an asserted triple, it needs to be inserted as such. For instance, the INSERT DATA operation in the example above may be modified as follows in order to insert not only the nested triple but also the triple `:bob :age 23`.
> **Example:**
>
> Example 29
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> INSERT DATA {
>   :bob :age 23 .
>   :alice :claims << :bob :age 23 >> .
> }
> ```

#### 5.1.2 DELETE DATA

The [DELETE DATA](https://www.w3.org/TR/sparql11-update/#deleteData) operation can be used to remove a given set of triples from the graph store. In the context of SPARQL-star Update, this may include removing nested RDF-star triples as demonstrated in the following example.
> **Example:**
>
> Example 30
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> DELETE DATA {
>   :alice :claims << :bob :age 23 >> .
> }
> ```

After executing this DELETE DATA operation over a graph store with a default graph that contains the given nested triple, the graph will not contain this triple any longer. If the graph did not contain that nested triple in the first place, the graph will remain unchanged by the given DELETE DATA operation.

Notice that deleting triples by using the DELETE DATA operation does not affect any other triples in the corresponding graphs. For instance, for a default graph that contains the triple `:bob :age 23` as an asserted triple, the DELETE DATA operation given above does *not* delete this asserted triple. In contrast, the following operation would delete this asserted triple but it would *not* delete any nested triple that contains the given triple as a quoted triple.
> **Example:**
>
> Example 31
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> DELETE DATA {
>   :bob :age 23 .
> }
> ```

#### 5.1.3 DELETE/INSERT

The [DELETE/INSERT](https://www.w3.org/TR/sparql11-update/#deleteInsert) operation can be used to remove or add triples based on variable bindings obtained by evaluating a given WHERE clause. As an example, the following DELETE/INSERT operation replaces all nested triples in which `:alice` is the subject by nested triples in which `:carol` is the subject.
> **Example:**
>
> Example 32
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> DELETE { :alice ?pp <<?s ?p ?o>> . }
> INSERT { :carol ?pp <<?s ?p ?o>> . }
> WHERE {  :alice ?pp <<?s ?p ?o>> . }
> ```

As in SPARQL Update, in SPARQL-star Update it is possible to use variations of the DELETE/INSERT operations in which either the DELETE clause or the INSERT clause are omitted.

When removing triples via the DELETE clause (irrespective of whether the INSERT clause is omitted or not), the effects with respect to nested triples must be the same as described above for the DELETE DATA operation; i.e., only the triples that are explicitly identified to be deleted are deleted. Similarly, inserting triples via the INSERT clause has the same effects as described above for the INSERT DATA operation; i.e., inserting nested triples does not automatically also insert their quoted triples as asserted triples into the graph. Of course, it is possible to request such inserts explicitly as demonstrated in the following example.
> **Example:**
>
> Example 33
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> DELETE { :alice ?pp <<?s ?p ?o>> . }
> INSERT { :carol ?pp <<?s ?p ?o>> .  ?s ?p ?o .}
> WHERE {  :alice ?pp <<?s ?p ?o>> . }
> ```

While all SPARQL-star Update examples above focus only on the default graph of a graph store, SPARQL-star Update can also be used to update the named graphs of a graph store, which works in exactly the same way as in SPARQL Update. As a possible example consider the following INSERT operation which retrieves all quoted triples found in nested triples in the default graph and inserts them as asserted triples into the named graph with IRI `:graph2`.
> **Example:**
>
> Example 34
>
>
>
> ```
> PREFIX : <http://www.example.org/>
>
> INSERT {
>   GRAPH :graph2 { ?s ?p ?o }
> }
> WHERE {
>   { <<?s ?p ?o>> ?pp ?oo }
>   UNION
>   { ?ss ?pp <<?s ?p ?o>> }
> }
> ```

### 5.2 Grammar

SPARQL-star Update is an extension of the SPARQL Update language [SPARQL11-UPDATE]. As mentioned in [SPARQL 1.1 Update, Appendix C](https://www.w3.org/TR/sparql11-update/#grammar) [SPARQL11-UPDATE], the grammar of the latter is provided as part of the [SPARQL 1.1 Query grammar](https://www.w3.org/TR/sparql11-query/#sparqlGrammar). Similarly, the grammar of SPARQL-star Update is provided as part of the grammar of the SPARQL-star query language, which is defined by the SPARQL 1.1 Query grammar with the extensions specified in § 4.2 Grammar (§4.2). As a result of these extensions, the production rules [QuadData](https://www.w3.org/TR/sparql11-query/#rQuadData) and [QuadPattern](https://www.w3.org/TR/sparql11-query/#rQuadPattern), which are used in the definition of SPARQL Update [SPARQL11-UPDATE], are extended to capture nested triples and nested triple patterns as demonstrated in the examples above.

### 5.3 Semantics

The semantics of SPARQL-star Update operations can also be defined by a simple extension of [the formalization of SPARQL Update](https://www.w3.org/TR/sparql11-update/#formalModel) [SPARQL11-UPDATE]. This extension assumes that any mention of "RDF triple" or "triple" in the formalization of SPARQL Update is understood as an RDF-star triple. Similarly, "RDF graph" and "solution mapping" are understood as RDF-star graph and SPARQL-star solution mapping, respectively. Any mention of the "evaluation function eval()" is understood as the eval function for SPARQL-star as defined in § 4.6 Evaluation Semantics (§4.6).

## 6. RDF-star Semantics

In this section, we provide a model-theoretic semantics for RDF-star, based on the one defined in [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/) [RDF11-MT]. More precisely, we define a mapping from RDF-star's abstract syntax into standard RDF's abstract syntax, and define the semantics of RDF-star graphs in terms of the semantics of the mapped [RDF graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph).

In the following, we will use abbreviated [IRIs](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) using the prefix `unstar:` which is an alias for the namespace `https://w3c.github.io/rdf-star/unstar#`.

We also introduce a number of definitions specific to RDF-star, which rely on the following notions, defined in [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/) [RDF11-CONCEPTS] and [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/) [RDF11-MT]: *[datatype](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype)*, *[lexical form](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-form)*, *[ill-typed](https://www.w3.org/TR/rdf11-mt/#dfn-ill-typed)*, *[merging](https://www.w3.org/TR/rdf11-mt/#dfn-merging)*, *[satisfiability](https://www.w3.org/TR/rdf11-mt/#dfn-satisfiable)*, *[unsatisfiability](https://www.w3.org/TR/rdf11-mt/#dfn-unsatisfiable)*, *[entailment](https://www.w3.org/TR/rdf11-mt/#dfn-entail)*,
and *[equivalence](https://www.w3.org/TR/rdf11-mt/#dfn-equivalent)*.

### 6.1 Mapping RDF-star abstract syntax to RDF

We define a mapping *L* that maps any [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) or [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) *t* to a literal with:

- `xsd:string` as its [datatype](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype), and
- the [canonical N-Triples](https://www.w3.org/TR/n-triples/#canonical-ntriples) representation of *t* as its [lexical form](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-form) [N-TRIPLES]. If *t* is itself a literal with the `xsd:string` [datatype](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype), the representation *MUST* simply match the [`STRING_LITERAL_QUOTE`](https://www.w3.org/TR/n-triples/#grammar-production-STRING_LITERAL_QUOTE) production (i.e., without an explicit [datatype](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype) [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri)).

Given an RDF-star graph *G*, the following steps define the *unstar mapping*, which transform *G* into an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) that we call unstar(*G*).

1. For each [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) *i* in the constituents of *G* starting with `https://w3c.github.io/rdf-star/unstar#`:
   1. Mint a new [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) *j* by appending an underscore (`_`) to *i*.
   2. Replace with *j* all occurrences of *i* in the [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject), [predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate), or [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) position of an asserted or quoted triple of *G*.
2. While *G* contains quoted triples:
   1. Pick an RDF-star triple (*s*, *p*, *o*) in the constituents of *G* such that neither *s* nor *o* is a quoted triple.
   2. Mint a fresh blank node *b* (i.e., such that *b* is not in the constituents of *G*).
   3. Replace with *b* all occurrences of (*s*, *p*, *o*) in the [subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject) or [object](https://www.w3.org/TR/rdf11-concepts/#dfn-object) position of an asserted or quoted triple of *G*.
   4. Add the following asserted triples to *G*:
      - (*b*, `unstar:subject`,` `*s*)
      - (*b*, `unstar:predicate`,` `*p*)
      - (*b*, `unstar:object`,` `*o*) unless *o* is an [ill-typed](https://www.w3.org/TR/rdf11-mt/#dfn-ill-typed) literal
      - (*b*, `unstar:subjectLexical`,` `*L*(*s*)) unless *s* is a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)
      - (*b*, `unstar:predicateLexical`,` `*L*(*p*))
      - (*b*, `unstar:objectLexical`,` `*L*(*o*)) unless *o* is a [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)

After these steps, unstar(*G*) is an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph), as it contains no quoted triples. Note that if *G* contains no quoted triple and no [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) in the `unstar:` namespace, then unstar(*G*) = *G*.

### 6.2 Entailment of RDF-star graphs

Following [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/), we define the notions of [satisfiability](https://www.w3.org/TR/rdf11-mt/#dfn-satisfiable) and [entailment](https://www.w3.org/TR/rdf11-mt/#dfn-entail) for RDF-star graphs. Given two RDF-star graphs *G* and *H*:

- We say that *G* is star-[satisfiable](https://www.w3.org/TR/rdf11-mt/#dfn-satisfiable) (resp. star-[unsatisfiable](https://www.w3.org/TR/rdf11-mt/#dfn-unsatisfiable)) if and only if unstar(*G*) is simply [satisfiable](https://www.w3.org/TR/rdf11-mt/#dfn-satisfiable) (resp. simply [unsatisfiable](https://www.w3.org/TR/rdf11-mt/#dfn-unsatisfiable)).
- We say that *H* is star-[entailed](https://www.w3.org/TR/rdf11-mt/#dfn-entail) by (resp. star-[equivalent](https://www.w3.org/TR/rdf11-mt/#dfn-equivalent) to) *G* if and only if unstar(*H*) is simply [entailed](https://www.w3.org/TR/rdf11-mt/#dfn-entail) by (resp. simply [equivalent](https://www.w3.org/TR/rdf11-mt/#dfn-equivalent) to) unstar(*G*).

It is easy to see that, in the special case of [RDF graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) *G* and *H* (i.e. RDF-star graphs containing no quoted triple), *G* is star-[satisfiable](https://www.w3.org/TR/rdf11-mt/#dfn-satisfiable) if and only if *G* is simply [satisfiable](https://www.w3.org/TR/rdf11-mt/#dfn-satisfiable), and *G* star-[entails](https://www.w3.org/TR/rdf11-mt/#dfn-entail) *H* if and only if *G* simply [entails](https://www.w3.org/TR/rdf11-mt/#dfn-entail) *H*. This is trivially true if *G* and *H* do not contain any `unstar:` [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) (in which case they are left unchanged by the unstar mapping). But this is also true if they do contain such [IRIs](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) (as the renaming performed by the unstar mapping has no significant impact on the semantic relationships between the two graphs). Star-[entailment](https://www.w3.org/TR/rdf11-mt/#dfn-entail) can therefore be considered as a natural *extension* of simple [entailment](https://www.w3.org/TR/rdf11-mt/#dfn-entail) to RDF-star graphs.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Other notions of [satisfiability](https://www.w3.org/TR/rdf11-mt/#dfn-satisfiable) and [entailment](https://www.w3.org/TR/rdf11-mt/#dfn-entail), such as [RDF entailment](https://www.w3.org/TR/rdf11-mt/#rdf-entailment) or [RDFS entailment](https://www.w3.org/TR/rdf11-mt/#rdfs-entailment), can be extended in the same way for RDF-star graphs.

### 6.3 Merging RDF-star graphs

[RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/) [RDF11-MT] defines the [merging](https://www.w3.org/TR/rdf11-mt/#dfn-merging) of two or more [RDF graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) as "[taking their] union after forcing any shared blank nodes, which occur in more than one graph, to be distinct in each graph." Note that, in the case of RDF-star graphs, any [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) in the constituent terms of that graph is governed by the definition above, *not* only those in the subject or object position of some asserted triple.
> **Example:**
>
> Example 35
>
>
>
> ```
> #### graph #1
> :alice :says
>   << _:x :name "bob" >>,
>   << _:x :likes :alice >>.
>
> #### graph #2
> :bob :says
>   << :alice :hates _:x >>.
>
> #### Merge of graphs #1 and #2 →
> :alice :says
>   << _:y :name "bob" >>,
>   << _:y :likes :alice >>.
> :bob :says
>   << :alice :hates _:z >>.
> ```

### 6.4 Remarks

*This section is non-normative.*

#### 6.4.1 Implementing the RDF-star semantics

It is important to notice that the definitions given above (§6.2) for [satisfiability](https://www.w3.org/TR/rdf11-mt/#dfn-satisfiable) and [entailment](https://www.w3.org/TR/rdf11-mt/#dfn-entail) of RDF-star graphs do not mandate that implementations actually transform RDF-star graphs using the unstar mapping defined above. It should be possible to implement the semantics by directly handling RDF-star's abstract syntax (§2).

#### 6.4.2 Combining RDF-star graphs

Care must be taken when implementations that rely on the unstar mapping combine the resulting [RDF graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) through union or [merge](https://www.w3.org/TR/rdf11-mt/#dfn-merging). Given two RDF-star graphs *G* and *H*, it may be the case that unstar(*G* ∪ *H*) ≠ unstar(*G*) ∪ unstar(*H*).

In particular, if *G* and *H* contain the same quoted triple, this triple will be mapped to a single blank node in unstar(*G* ∪ *H*), but in two potentially different blank nodes in unstar(*G*) ∪ unstar(*H*). These blank nodes will need to be unified in order to reconstruct unstar(*G* ∪ *H*).

Conversely, nothing in the definition of the unstar mapping prevents it from generating the same blank node *b* for a quoted triple of *G*, and for a *different* quoted triple of *H* (provided that *b* is not present in either *G* nor *H*). In that case, not only would unstar(*G*) ∪ unstar(*H*) be different from unstar(*G* ∪ *H*), but it would lose some information by mixing the descriptions of the two quoted triples.

#### 6.4.3 Other uses of the unstar mapping

Since the unstar mapping transforms any RDF-star graph into a standard ("non-star") [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph), it might be tempting to use this mapping for conveying RDF-star graphs to legacy RDF systems. However, this has a number of caveats.

First, the unstar mapping alters the semantics of the graph: in general, a graph *G* is *not* [equivalent](https://www.w3.org/TR/rdf11-mt/#dfn-equivalent) to its "unstarred" version unstar(*G*), even if *G* is a standard [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) containing no quoted triples. (More precisely, they are equivalent only if *G* contains no quoted triples and no IRIs from the `unstar:` namespace.)

Second, when a legacy RDF system communicates an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph) to an RDF-star-aware system, there is no means by which the latter can determine with certainty whether the graph is the result of applying the unstar mapping, and thus needs to be transformed back. (The presence of `unstar:` IRIs in the graph can be used as a hint, but such IRIs can also be used independently of the mapping.) Additional metadata should therefore be attached to unstarred graphs, so that RDF-star systems know whether or not they need to apply the inverse transformation of unstar.

Finally, legacy RDF systems may alter unstarred graphs in ways that prevent their transformation back to the original RDF-star graph. For example, it has been pointed out above (§6.4.2) how combining several unstarred graphs may not yield the expected result. Another example is the removal of some arcs, such that a quoted triple is not completely described anymore, and can not be reconstructed.

#### 6.4.4 Referential opacity

The way the unstar mapping is defined, the denotation of a quoted triple does not only depend on the denotation of its component terms, but also on their syntactical form (for IRIs and literals). This behavior is referred to as [referential opacity](https://en.wikipedia.org/wiki/Opaque_context). A consequence is that two different triples, that would be semantically equivalent if asserted, are not automatically considered to denote the same thing when quoted. In the example below, assuming [D-entailment](https://www.w3.org/TR/rdf11-mt/#datatype-entailment): while `"104232"^^xsd:nonNegativeInteger` and `"000104232"^^xsd:nonNegativeInteger` denote the same thing (namely, the number 104232), the two quoted triples are allowed to have different denotations, and so the entailment does not hold.
> **Example:**
>
> Example 36
>
>
>
> ```
> #### under D-entailment
>
> << dbr:Linköping dbo:populationTotal "104232"^^xsd::nonNegativeInteger >>
>     :source <https://dbpedia.org/data/Linköping>.
>
> #### does NOT entail
>
> << dbr:Linköping dbo:populationTotal "000104232"^^xsd::nonNegativeInteger >>
>     :source <https://dbpedia.org/data/Linköping>.
>
> # (notice the leading zeros in the literal)
> ```

Similarly, in the example below and under [OWL entailment](https://www.w3.org/TR/owl2-overview/) [OWL2-Overview], while `:superman` and `:clark` are inferred to denote one and the same person (because of the `owl:sameAs` relationship between them), the two quoted triples are not automatically considered to denote the same thing.
> **Example:**
>
> Example 37
>
>
>
> ```
> #### under OWL-entailment
>
> :superman owl:sameAs :clark.
> << :superman :can :fly >> :reportedBy :clark.
>
> #### does NOT entail
>
> << :clark :can :fly >> :reportedBy :clark.
> ```

Note that this may lead to counter-intuitive results when the §3.1 Annotation Syntax is used, as illustrated in the example below.
> **Example:**
>
> Example 38
>
>
>
> ```
> #### under D-entailment
>
> dbr:Linköping dbo:populationTotal "104232"^^xsd::nonNegativeInteger
>     {| :source <https://dbpedia.org/data/Linköping> |}.
>
> #### does NOT entail
>
> dbr:Linköping dbo:populationTotal "000104232"^^xsd::nonNegativeInteger
>     {| :source <https://dbpedia.org/data/Linköping> |}.
>
> # (notice the leading zeros in the literal)
>
> #### more precisely, it DOES entail
>
> dbr:Linköping dbo:populationTotal "000104232"^^xsd::nonNegativeInteger.
>
> #### but it does NOT entail
>
> << dbr:Linköping dbo:populationTotal "000104232"^^xsd::nonNegativeInteger >>
>     :source <https://dbpedia.org/data/Linköping>.
> ```

#### 6.4.5 Selective referential transparency

Referencial opacity is well suited for use-cases where the syntactical form of the annotated statements may be significant (like [annotating statements from other graphs](https://w3c.github.io/rdf-star/UCR/rdf-star-ucr.html#annotate-statements-from-other-named-graphs-and-datasets) or [annotating commit deltas](https://w3c.github.io/rdf-star/UCR/rdf-star-ucr.html#annotate-commit-deltas)). On the other hand, other use-cases would expect some degree of referential transparency. Consider the case of [attributed/evidenced triples](https://w3c.github.io/rdf-star/UCR/rdf-star-ucr.html#meta-properties-over-properties). The annotation is understood to be about the fact asserted by the triple rather than the triple itself. In this use case, one might then expect more inferences than provided by the base semantics. Consider the following example.
> **Example:**
>
> Example 39
>
>
>
> ```
> << dbr:Linköping dbo:populationTotal "104232"^^xsd::nonNegativeInteger >>
>   :measuredOn "2010-12-31"^^xsd:date ;
>   :source <https://dbpedia.org/data/Linköping.ttl> .
>
> ### Candidate entailment #1
>
> << dbr:Linköping dbo:populationTotal "000104232"^^xsd::nonNegativeInteger >>
>   :measuredOn "2010-12-31"^^xsd:date .
>
> ### Candidate entailment #2
>
> << dbr:Linköping dbo:populationTotal "000104232"^^xsd::nonNegativeInteger >>
>   :source <https://dbpedia.org/data/Linköping.ttl> .
>
> # (notice the leading zeros in the literal in both candidate entailments)
> ```

One could argue that the candidate entailment #1 is desirable because the property `:measuredOn` is understood to be about the *statement* made by the subject triple (that statement was true on the given date, regardless of its RDF expression, in this case using an object value equivalent to `104232`). On the other hand, the candidate entailment #2 may be considered not desirable because the predicate `:source` is about the triple itself (that specific triple was parsed from the given Turtle file).

In Section § 7. RDF-star vocabulary (§7), we introduce the notion of *transparency-enabling property (TEP)*, for selectively enabling this kind of entailment on specific properties. The basis of the idea is that each such property *p* is identified by adding to the RDF-star graph a triple of the form (*p*, `rdf:type`, `rdf-star:TransparencyEnablingProperty`); i.e., for the previous example, this triple would be (`:measuredOn`, `rdf:type`, `rdf-star:TransparencyEnablingProperty`).
This would make candidate entailment #1 above valid. The semantics of such TEPs is formally defined in Section § 7.3 Vocabulary semantics (§7.3).

Notice that enabling referential transparency based on such TEPs is only local to the RDF-star graph(s) in which the property is stated to be a TEP (or where this statement can be inferred as per the entailment regime considered). In other words, for every graph *G* in which a property is *not* stated to be transparency enabling, all quoted triples appearing in *G* as subject or object of that property are stilled considered as referentially opaque, even if there may exist some other graph in which the property is stated to be transparency enabling.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This proposal for TEPs makes no distinction regarding the position (subject or object) of the quoted triples. The group did consider a finer-grained alternative, where selective transparency could also be enabled only for the subjects (resp. objects) of the TEP. This was however ruled out as overly complex for a limited added value.

#### 6.4.6 Other alternatives to referential opacity

Given the potential drawbacks of the referential opacity provided by the current semantics, as described in the beginning of Section § 6.4.5 Selective referential transparency (§6.4.5) above, the group has considered other alternative semantics. No clear consensus was reached, however, to decide whether these alternatives should be used as a replacement, or as a [semantic extension](https://www.w3.org/TR/rdf11-mt/#dfn-semantic-extension), of the current semantics.

A fully referentially transparent semantics can be achieved by changing the step 2.4 of the unstar mapping algorithm as follows:

- Add the following asserted triples to *G*:
  * (*b*, `unstar:subject`,` `*s*)
  * (*b*, `unstar:predicate`,` `*p*)
  * (*b*, `unstar:object`,` `*o*)

In the examples above (Example 36, Example 37, Example 38, Example 39), all the entailments would now hold automatically. This could be a problem in some use-cases, as such inferences could then not be cancelled, given the [monotonic semantics](https://www.w3.org/TR/rdf11-mt/#dfn-monotonic) of RDF.

An intermediate alternative would be to make quoted triples referentially opaque for IRIs only, keeping it transparent for literals (and for blank nodes, as is already the case). This can be achieved by changing the step 2.4 of the unstar mapping algorithm as follows:

- Add the following asserted triples to *G*:
  * (*b*, `unstar:subject`,` `*s*)
  * (*b*, `unstar:predicate`,` `*p*)
  * (*b*, `unstar:object`,` `*o*)
  * (*b*, `unstar:subjectLexical`,` `*L*(*s*)) if *s* is an [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri)
  * (*b*, `unstar:predicateLexical`,` `*L*(*p*))
  * (*b*, `unstar:objectLexical`,` `*L*(*o*)) if *o* is an [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri)

> **Note:**
>
> > **Note:**
> >
> > Note
>
> Other design choices for the semantics have also been discussed by the community group; these have been [summarized in a Github issue](https://github.com/w3c/rdf-star/issues/95).

## 7. RDF-star vocabulary

*This section is non-normative.*

In this section, we propose a minimal vocabulary that can be useful when working with RDF-star, especially when describing other vocabularies meant to be used with RDF-star triples and graphs.

### 7.1 Core vocabulary

In this section we define IRIs for the concepts defined in other normative parts of this document.

`rdf-star:Triple`

This term identifies the class of all RDF-star triples. It is expected to serve, among other things, as the `rdfs:domain` or `rdfs:range` of properties meant to apply to quoted triples.

`rdf-star:Graph`

This term identifies the class of all RDF-star graphs.

`rdf-star:Source`

This term identifies the class of all RDF-star sources, an extension of the notion of *[RDF source](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-source)*: a persistent yet mutable source or container of RDF-star graphs.

`rdf-star:SPARQLStarQuery`

This term identifies the extension of the SPARQL query language defined in Section § 4. SPARQL-star Query Language (§4). It is expected to serve as the value of `sd:supportedLanguage` in SPARQL service descriptions [SPARQL11-SERVICE-DESCRIPTION].

`rdf-star:SPARQLStarUpdate`

This term identifies the extension of the SPARQL update language defined in Section § 5. SPARQL-star Update (§5). It is expected to value as the domain of `sd:supportedLanguage` in SPARQL service descriptions [SPARQL11-SERVICE-DESCRIPTION].

Below is a Turtle description of that vocabulary.

```
## RDF-star core vocabulary
PREFIX rdf:       <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:      <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf-star:  <http://www.w3.org/ns/rdf-star#>
PREFIX sd:        <http://www.w3.org/ns/sparql-service-description#>

rdf-star:Triple      a rdfs:Class ;
    rdfs:isDefinedBy   <http://www.w3.org/ns/rdf-star#> ;
    rdfs:label         "RDF-star Triple" ;
    rdfs:comment       "The class of RDF-star triples." ;
    rdfs:subClassOf    rdfs:Resource .

rdf-star:Graph       a rdfs:Class ;
    rdfs:isDefinedBy   <http://www.w3.org/ns/rdf-star#> ;
    rdfs:label         "RDF-star Graph" ;
    rdfs:comment       "The class of RDF-star graphs." ;
    rdfs:subClassOf    rdfs:Resource .

rdf-star:Source      a rdfs:Class ;
    rdfs:isDefinedBy   <http://www.w3.org/ns/rdf-star#> ;
    rdfs:label         "RDF-star Source" ;
    rdfs:seeAlso       <https://www.w3.org/TR/rdf11-concepts/#h3_change-over-time> ;
    rdfs:comment       "The class of RDF-star sources." ;
    rdfs:subClassOf    rdfs:Resource .

rdf-star:SPARQLStarQuery a sd:Language ;
    rdfs:isDefinedBy   <http://www.w3.org/ns/rdf-star#> ;
    rdfs:label         "SPARQL-star" ;
    rdfs:comment       "The SPARQL-star query language" .

rdf-star:SPARQLStarUpdate a sd:Language ;
    rdfs:isDefinedBy   <http://www.w3.org/ns/rdf-star#> ;
    rdfs:label         "SPARQL-star Update" ;
    rdfs:comment       "The SPARQL-star update language" .
```

### 7.2 Extended vocabulary

In this section we define IRIs for the concepts defined in other non-normative parts of this document.

`rdf-star:TransparencyEnablingProperty`

A special kind of property that, when applied to a quoted triple, also holds for any semantically equivalent triple, as discussed in § 6.4.5 Selective referential transparency (§6.4.5).

Below is a Turtle description of that vocabulary.

```
## RDF-star extended vocabulary
PREFIX rdf:       <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:      <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf-star:  <http://www.w3.org/ns/rdf-star#>

rdf-star:TransparencyEnablingProperty a rdfs:Class ;
    rdfs:isDefinedBy   <http://www.w3.org/ns/rdf-star#> ;
    rdfs:label         "RDF-star Source" ;
    rdfs:comment       "The class of transparency-enabling properties." ;
    rdfs:subClassOf    rdf:Property .
```

### 7.3 Vocabulary semantics

We now describe a [semantic extension](https://www.w3.org/TR/rdf11-mt/#dfn-semantic-extension) of RDF-star, embedding the inherent semantics of the RDF-star vocabulary (RSV) described above (core and extended). A *simple RSV-interpretation* is a [simple interpretation](https://www.w3.org/TR/rdf11-mt/#simple-interpretations) *I* that satisfies the following additional conditions:

1. *Ensure that all quoted triples in this interpretations are instances of `rdf-star:Triple`.*
   - For all *t*, *x* in the domain IR such that either
     * (*t*, *x*) ∈ IEXT(IS(`unstar:subject`)),
     * (*t*, *x*) ∈ IEXT(IS(`unstar:predicate`)),
     * (*t*, *x*) ∈ IEXT(IS(`unstar:object`)),
     * (*t*, *x*) ∈ IEXT(IS(`unstar:subjectLexical`)),
     * (*t*, *x*) ∈ IEXT(IS(`unstar:predicateLexical`)),
     * (*t*, *x*) ∈ IEXT(IS(`unstar:objectLexical`)),
   - then (*t*, IS(`rdf-star:Triple`)) must be an element of IEXT(IS(`rdf:type`)).
2. *Ensure that, for all quoted triples in this interpretation, all "equivalent" triples also exist in the interpretation.*
   - For all *t*, *s*, *p*, *o* in the domain IR such that
     * (*t*, *s*) ∈ IEXT(IS(`unstar:subject`)),
     * (*t*, *p*) ∈ IEXT(IS(`unstar:predicate`)),
     * (*t*, *o*) ∈ IEXT(IS(`unstar:object`)),
   - and for all terms *s*', *p*', and *o*' such that
     * *I*(*s*') = *s*,
     * *I*(*p*') = *p*,
     * *I*(*o*') = *o*,
   - there must exist *t*' in IR such that
     * (*t*', *s*) ∈ IEXT(IS(`unstar:subject`)),
     * (*t*', *p*) ∈ IEXT(IS(`unstar:predicate`)),
     * (*t*', *o*) ∈ IEXT(IS(`unstar:object`)),
     * (*t*', *I*(L(*s*'))) ∈ IEXT(IS(`unstar:subjectLexical`)),
     * (*t*', *I*(L(*p*'))) ∈ IEXT(IS(`unstar:predicateLexical`)), and
     * (*t*', *I*(L(*o*'))) ∈ IEXT(IS(`unstar:objectLexical`)).
3. *Ensure that TEPs that hold for a triple also hold for all "equivalent" triples.*
   - For all *p* such that (*p*,IS(`rdf-star:TransparencyEnablingProperty`)) ∈ IEXT(IS(`rdf:type`))
   - then *p* must be an element of IP, and
     * For all *t*, *u*, *s*', *p*', *o*', *t*' in IR such that
       + (*t*, *u*) ∈ IEXT(`p`)
       + (*t*, *s*') ∈ IEXT(IS(`unstar:subject`)),
       + (*t*, *p*') ∈ IEXT(IS(`unstar:predicate`)),
       + (*t*, *o*') ∈ IEXT(IS(`unstar:object`)),
       + (*t*', *s*') ∈ IEXT(IS(`unstar:subject`)),
       + (*t*', *p*') ∈ IEXT(IS(`unstar:predicate`)),
       + (*t*', *o*') ∈ IEXT(IS(`unstar:object`))

       then (*t*', *u*) must also be an element of IEXT(*p*).
     * For all *t*, *u*, *s*', *p*', *o*', *t*' in IR such that
       + (*u*, *t*) ∈ IEXT(`p`)
       + (*t*, *s*') ∈ IEXT(IS(`unstar:subject`)),
       + (*t*, *p*') ∈ IEXT(IS(`unstar:predicate`)),
       + (*t*, *o*') ∈ IEXT(IS(`unstar:object`)),
       + (*t*', *s*') ∈ IEXT(IS(`unstar:subject`)),
       + (*t*', *p*') ∈ IEXT(IS(`unstar:predicate`)),
       + (*t*', *o*') ∈ IEXT(IS(`unstar:object`))

       then (*u*, *t*') must also be an element of IEXT(*p*).

Given two RDF-star graphs *G* and *H*, and following standard terminology, we say that a simple RSV-interpretation *I* satisfies *G* if *I*(*G*) = true, and that *G* is (simply) RSV-satisfiable if a simple RSV-interpretation exists that satisfies *G*; otherwise, *G* is (simply) RSV-unsatisfiable. We say that *G* simply RSV-entails *H* if every simple RSV-interpretation that satisfies *G* also satisfies *H*. If *G* and *H* each RSV-entail the other, they are RSV-equivalent.

RSV-entailment is defined here as an extension of [simple entailment](https://www.w3.org/TR/rdf11-mt/#simpleentailment), but other entailment regimes (such as [RDF entailment](https://www.w3.org/TR/rdf11-mt/#rdf-entailment) or [RDFS entailment](https://www.w3.org/TR/rdf11-mt/#rdfs-entailment)) can be extended in the exact same way (i.e., by extending their respective notion of interpretation with the aforementioned conditions).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Some terms of the RDF-star vocabulary have no associated constraint in RSV-interpretations (for instance, `rdf-star:Graph`). The reason is that the intended meaning of these terms leads to no particular inference *with this vocabulary*.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 169](https://github.com/w3c/rdf-star/issues/169): Occurrences vocabulary [later](https://github.com/w3c/rdf-star/issues/?q=is%3Aissue+is%3Aopen+label%3A%22later%22)[vocabulary](https://github.com/w3c/rdf-star/issues/?q=is%3Aissue+is%3Aopen+label%3A%22vocabulary%22)
>
> This issue discusses the relevance of introducing a standard property to link a quoted triple to its occurrences (as illustrated in Example 8), as well as other related properties and classes.

## A. IANA Considerations

*This section is non-normative.*

In § 3. Concrete Syntaxes (§3), we have proposed extensions to four existing media types, namely `text/turtle` [TURTLE], `application/trig` [TRIG], `application/n-triples` [N-TRIPLES] and `application/n-quads` [N-QUADS]. In § 4. SPARQL-star Query Language (§4), we have proposed extensions to three more existing media types, namely `application/sparql-query` [SPARQL11-QUERY], `application/sparql-results+json` [SPARQL11-RESULTS-JSON], and `application/sparql-result+xml` [RDF-SPARQL-XMLRES]. While the [RDF-DEV Community Group](https://www.w3.org/community/rdf-dev/) has no authority to officially update these media-types, we hope that a future working group with such authority will consider doing so, and include extensions proposed in this report.

In the meantime, implementers of RDF-star are faced with a dilemma: use the standard media-type identifiers as if their definition had been already updated (optimistic approach); or make it explicit that they are prone to produce or consume quoted triples (pessimistic approach), perhaps by using a different temporary media-type, or custom HTTP headers.

The optimistic approach raises the risk of breaking the expectations of other applications that are not RDF-star-aware. For example, if a SPARQL-star endpoint responds to a CONSTRUCT query with the `text/turtle` media-type, and includes a quoted triple in the response, a legacy client will fail to parse that response. On the other hand, if the same server applies the pessimistic approach, it may simply reject any query requiring `text/turtle`, *just in case* the result contain quoted triples. Note that it is not always feasible for the server to decide beforehand whether the result is plain Turtle or Turtle-star, because the result is often produced in a streamed manner, after the headers containing the media-type have been sent to the client.

Another problem with the pessimistic approach is that "temporary" media-types are known to actually become permanent. Old applications keep using them long after their intended expiration date. This a burden on all other implementations, which must handle the "temporary" media-types along the permanent one, as aliases, in order to maintain backward compatibility.

The W3C Recommendation [Content Negotiation by Profile](https://www.w3.org/TR/dx-prof-conneg/#introduction) [DX-PROF-CONNEG] describes a mechanism that separates content-type
negotiation from requesting a response conforming to a specific information model,
whether that model is a specific standard, specification or profile.
The [operations of the abstract model](https://www.w3.org/TR/dx-prof-conneg/#requestsandresonses) are "list profiles" and "get resource by profile".
The "get resource" operation can provide the profile requests with HTTP
header `Accept-Profile` and responses use `Content-Profile`, or
alternatively the request can use HTTP Query String parameters.

This may be useful when the information is available in RDF-star or in non-RDF-star
RDF 1.1 form, whether using reification, or by omitting information expressed with
the RDF-star data model and responding with a restricted response. By lifting the
issue up to the information model, away from being purely about syntax, restricted
responses can be requested and returned which do not use RDF-star features.
However, it assumes both requestor and receiver adhere to the defined profile
negotiation and therefore does not address the dilemma of optimistic or pessimistic
approaches.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 43](https://github.com/w3c/rdf-star/issues/43): New mime types for RDF-star serializations (inc. SPARQL results) [sparql-star](https://github.com/w3c/rdf-star/issues/?q=is%3Aissue+is%3Aopen+label%3A%22sparql-star%22)[concrete-syntax](https://github.com/w3c/rdf-star/issues/?q=is%3Aissue+is%3Aopen+label%3A%22concrete-syntax%22)[later](https://github.com/w3c/rdf-star/issues/?q=is%3Aissue+is%3Aopen+label%3A%22later%22)
>
> Although the examples in this document, and the tests in [the test suite](https://w3c.github.io/rdf-star/tests/), adopt the optimistic approach, it should be noted that no clear consensus emerged from the group on which approach is the best.

## B. Historical remarks

*This section is non-normative.*

### B.1 SA-mode and PG-mode

A lot of discussions on the [RDF-star mailing list](https://lists.w3.org/Archives/Public/public-rdf-star/) and [GitHub repository](https://github.com/w3c/rdf-star) refer to SA-mode and PG-mode. Those abbreviations stand for "Separate Assertion mode" and "Property Graph mode". They originate in the fact that different versions of RDF-star have been published over the years, with different designs. In PG-mode, any quoted triple was also considered asserted. SA-mode, on the other hand, allowed the use of quoted triples without those triples being automatically asserted, requiring that they be asserted separately when that was intended. SA-mode was more flexible, but induced redundancy in the use-cases that PG-mode was designed to address.

The notion of annotations in the §3.2 Turtle-star syntax was introduced to remove the need for different modes. Rather than interpret the same syntax differently in each mode, which would have caused interoperability problems and required a switch for those modes, it was decided to provide a different syntax for each use case.

- The `<< ... >>` syntax represents a triple that is quoted without being asserted, satisfying the need formerly filled by SA-mode.
- The `:a :b :c {| :p :o ... |}` annotation syntax creates triples where the subject is a quoted version of the triple asserted just before the annotation (here, `:a :b :c`), without the need to repeat it, satisfying the need formerly filled by PG-mode.

### B.2 The seminal example

The motivating example in the original RDF-star paper [RDF-STAR-FOUNDATION] was on a provenance use-case, and is repeated below.
> **Example:**
>
> Example 40
>
>
>
> ```
> # the controversial seminal example
> :bob foaf:name "Bob".
> <<:bob foaf:age 23>> dct:creator <http://example.com/crawlers#c1> ;
>                      dct:source <http://example.net/listing.html> .
> ```

This example was further debated on the [RDF-star mailing list](https://lists.w3.org/Archives/Public/public-rdf-star/), as it appears to have set wrong expectations about what quoted triples represent. More precisely, from this example, one may wrongly assume that `<<:bob foaf:age 23>>` represents the *occurrence* of the given triple at the address `http://example.net/listing.html` (see § 2.3 Triples and occurrences (§2.3)). This impression may be reinforced by the use of `dct:creator`: arguably, a triple (as a unique abstract entity) is not "created" by anyone, while an occurrence thereof can be said to be created or authored.

The problem with this interpretation is that it will break as soon as other creators and sources are added for the triple: one could not tell which source corresponds to which creator. Correctly capturing this information would require additional nodes to explicitly represent triple occurrences, as in Example 8. In summary, although RDF-star can be used for provenance, the seminal example does not work as stated and can lead to the fundamentally incorrect interpretation that RDF-star can represent multiple distinct quoted triples with the same subject, predicate, and object.

## C. Complete EBNF Grammars

### C.1 Turtle-Star EBNF Grammar

*This section is non-normative.*

The following is a complete grammar for Turtle-Star.
The EBNF used here is defined in XML 1.0 [EBNF-NOTATION].

| [1]        | `turtleDoc`                        | ::= | statement`*`                                                                                                                 |
| ---------- | ---------------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [2]        | `statement`                        | ::= | directive `\| (` triples "`.`"`)`                  |
| [3]        | `directive`                        | ::= | prefixID `\| \|` base sparqlPrefix sparqlBase |
| [4]        | `prefixID`                         | ::= | "@prefix" PNAME_NS IRIREF "`.`"`?`                   |
| [5]        | `base`                             | ::= | "@base" IRIREF "`.`"`?`                                                                                                         |
| [5s]       | `sparqlPrefix`                     | ::= | "PREFIX" PNAME_NS IRIREF                             |
| [6s]       | `sparqlBase`                       | ::= | "BASE" IRIREF                                                                                                                   |
| [6]        | `triples`                          | ::= | `(` subject predicateObjectList`) \|` blankNodePropertyList predicateObjectList`? )` |
| [7]        | `predicateObjectList`              | ::= | verb objectList `(` "`;`" `(` verb objectList`) ?` |
| [8]        | `objectList`                       | ::= | object annotation`? (` "`,`" object annotation`? )` |
| [9]        | `verb`                             | ::= | predicate `\|` "`a`"                                                                                                         |
| [10]       | `subject`                          | ::= | iri `\| \|` BlankNode collection quotedTriple |
| [11]       | `predicate`                        | ::= | iri                                                                                                                                |
| [12]       | `object`                           | ::= | iri `\| \|` BlankNode collection blankNodePropertyList literal quotedTriple |
| [13]       | `literal`                          | ::= | RDFLiteral `\| \|` NumericLiteral BooleanLiteral |
| [14]       | `blankNodePropertyList`            | ::= | "`[`" predicateObjectList "`]`"                                                                                    |
| [15]       | `collection`                       | ::= | "`(`" object`*` "`)`"                                                                                                           |
| [16]       | `NumericLiteral`                   | ::= | INTEGER `\| \|` DECIMAL DOUBLE |
| [128s]     | `RDFLiteral`                       | ::= | String `( \|` LANGTAG "^^" iri`) )` |
| [133s]     | `BooleanLiteral`                   | ::= | "true" `\|` "false"                                                                                                                                                                                      |
| [17]       | `String`                           | ::= | STRING_LITERAL_QUOTE `\| \|` STRING_LITERAL_SINGLE_QUOTE STRING_LITERAL_LONG_SINGLE_QUOTE STRING_LITERAL_LONG_QUOTE |
| [135s]     | `iri`                              | ::= | IRIREF `\|` PrefixedName                         |
| [136s]     | `PrefixedName`                     | ::= | PNAME_LN `\|` PNAME_NS                             |
| [137s]     | `BlankNode`                        | ::= | BLANK_NODE_LABEL `\|` ANON                     |
| [27]       | `quotedTriple`                     | ::= | "<<" qtSubject predicate qtObject ">>" |
| [28]       | `qtSubject`                        | ::= | iri `\| \|` BlankNode quotedTriple |
| [29]       | `qtObject`                         | ::= | iri `\| \|` BlankNode literal quotedTriple |
| [30]       | `annotation`                       | ::= | "{\|" predicateObjectList "\|}"                                                                                    |
| @terminals | |     | **# Productions for terminals**                                                                                                                                                                          |
| [18]       | `IRIREF`                           | ::= | "`<`" `( [#x00-#x20```<>"{}\|^`\```] \|` UCHAR`) *` "`>`"                                                                        |
| [139s]     | `PNAME_NS`                         | ::= | PN_PREFIX`?` "`:`"                                                                                                           |
| [140s]     | `PNAME_LN`                         | ::= | PNAME_NS PN_LOCAL                                  |
| [141s]     | `BLANK_NODE_LABEL`                 | ::= | "_:" `( \|` PN_CHARS_U`] )` PN_CHARS "`.`"`) *` PN_CHARS`) ?` |
| [144s]     | `LANGTAG`                          | ::= | "`@`" `[ a-zA-Z] +` "`-`" `[ a-zA-Z0-9] +`                                                                                                                                                               |
| [19]       | `INTEGER`                          | ::= | `[ +-] ?] +`                                                                                                                                                                                             |
| [20]       | `DECIMAL`                          | ::= | `[ +-] ?] *` "`.`" `[ 0-9] +`                                                                                                                                                                            |
| [21]       | `DOUBLE`                           | ::= | `[ +-] ?] +` "`.`" `[ 0-9] *` EXPONENT`) \|` "`.`" `[ 0-9] +` EXPONENT`) \|] +` EXPONENT`) )` |
| [154s]     | `EXPONENT`                         | ::= | `[ eE] [] ?] +`                                                                                                                                                                                          |
| [22]       | `STRING_LITERAL_QUOTE`             | ::= | '`"`' `( [>"#x5C#x0A#x0D] \|` ECHAR UCHAR`) *` '`"`'     |
| [23]       | `STRING_LITERAL_SINGLE_QUOTE`      | ::= | "`'`" `( [#x27#x5C#x0A#x0D] \|` ECHAR UCHAR`) *` "`'`"   |
| [24]       | `STRING_LITERAL_LONG_SINGLE_QUOTE` | ::= | "'''" `( (` "`'`" `\|` "''"`) ?] \|` ECHAR UCHAR`) )` "'''" |
| [25]       | `STRING_LITERAL_LONG_QUOTE`        | ::= | '"""' `( (` '`"`' `\|` '""'`) ?] \|` ECHAR UCHAR`) )` '"""' |
| [26]       | `UCHAR`                            | ::= | `(` "\u" HEX HEX HEX HEX`) \|` "\U" HEX HEX HEX HEX HEX HEX HEX HEX`)` |
| [159s]     | `ECHAR`                            | ::= | "`\`" `[ tbnrf\"']`                                                                                                                                                                                      |
| [161s]     | `WS`                               | ::= | `#x20 \|`                                                                                                                                                                                                |
| [162s]     | `ANON`                             | ::= | "`[`" WS`*` "`]`"                                                                                                                   |
| [163s]     | `PN_CHARS_BASE`                    | ::= | `[ A-Z]`                                                                                                                                                                                                 |
|            | | \|  | `[ a-z]`                                                                                                                                                                                                 |
|            | | \|  | `[ #xC0-#xD6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xD8-#xF6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xF8-#x02FF]`                                                                                                                                                                                         |
|            | | \|  | `[ #x0370-#x037D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x037F-#x1FFF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x200C-#x200D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2070-#x218F]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2C00-#x2FEF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x3001-#xD7FF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xF900-#xFDCF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xFDF0-#xFFFD]`                                                                                                                                                                                       |
|            | | \|  | `[ #x00010000-#x000EFFFF]`                                                                                                                                                                               |
| [164s]     | `PN_CHARS_U`                       | ::= | PN_CHARS_BASE `\|` "`_`"                                                                                                 |
| [166s]     | `PN_CHARS`                         | ::= | PN_CHARS_U `\|` "`-`" `\| [] \|-#x036F] \|-#x2040]`                                                                         |
| [167s]     | `PN_PREFIX`                        | ::= | PN_CHARS_BASE `( (` PN_CHARS "`.`"`) *` PN_CHARS`) ?` |
| [168s]     | `PN_LOCAL`                         | ::= | `( \|` PN_CHARS_U "`:`" `\| [] \|` PLX`) (` PN_CHARS "`.`" `\|` "`:`" `\|` PLX`) *` PN_CHARS "`:`" `\|` PLX`) )` |
| [169s]     | `PLX`                              | ::= | PERCENT `\|` PN_LOCAL_ESC                       |
| [170s]     | `PERCENT`                          | ::= | "`%`" HEX HEX                                                |
| [171s]     | `HEX`                              | ::= | `[ 0-9] \|] \|]`                                                                                                                                                                                         |
| [172s]     | `PN_LOCAL_ESC`                     | ::= | "`\`" `(` "`_`" `\|` "`~`" `\|` "`.`" `\|` "`-`" `\|` "`!`" `\|` "`$`" `\|` "`&`" `\|` "`'`" `\|` "`(`" `\|` "`)`" `\|` "`*`" `\|` "`+`" `\|` "`,`" `\|` "`;`" `\|` "`=`" `\|` "`/`" `\|` "`?`" `\|` "`#`" `\|` "`@`" `\|` "`%`"`)` |

### C.2 TriG-Star EBNF Grammar

*This section is non-normative.*

The following is a complete grammar for TriG-Star.
The EBNF used here is defined in XML 1.0 [EBNF-NOTATION].

| [1g]       | `trigDoc`                          | ::= | `( \|` directive block`) *`                          |
| ---------- | ---------------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [2g]       | `block`                            | ::= | triplesOrGraph `\| \|` wrappedGraph triples2 "GRAPH" labelOrSubject wrappedGraph`)` |
| [3g]       | `triplesOrGraph`                   | ::= | `( (` labelOrSubject wrappedGraph predicateObjectList "`.`"`) )` quotedTriple predicateObjectList "`.`"`)` |
| [4g]       | `triples2`                         | ::= | `(` blankNodePropertyList predicateObjectList`?` "`.`"`) \|` collection predicateObjectList "`.`"`)` |
| [5g]       | `wrappedGraph`                     | ::= | "`{`" triplesBlock`?` "`}`"                                                                                               |
| [6g]       | `triplesBlock`                     | ::= | triples `(` "`.`" triplesBlock`? )`             |
| [7g]       | `labelOrSubject`                   | ::= | iri `\|` BlankNode                                     |
| [3]        | `directive`                        | ::= | prefixID `\| \|` base sparqlPrefix sparqlBase |
| [4]        | `prefixID`                         | ::= | "@prefix" PNAME_NS IRIREF "`.`"`?`                   |
| [5]        | `base`                             | ::= | "@base" IRIREF "`.`"`?`                                                                                                         |
| [5s]       | `sparqlPrefix`                     | ::= | "PREFIX" PNAME_NS IRIREF                             |
| [6s]       | `sparqlBase`                       | ::= | "BASE" IRIREF                                                                                                                   |
| [6]        | `triples`                          | ::= | `(` subject predicateObjectList`) \|` blankNodePropertyList predicateObjectList`? )` |
| [7]        | `predicateObjectList`              | ::= | verb objectList `(` "`;`" `(` verb objectList`) ?` |
| [8]        | `objectList`                       | ::= | object annotation`? (` "`,`" object annotation`? )` |
| [9]        | `verb`                             | ::= | predicate `\|` "`a`"                                                                                                         |
| [10]       | `subject`                          | ::= | iri `\| \|` blank quotedTriple |
| [11]       | `predicate`                        | ::= | iri                                                                                                                                |
| [12]       | `object`                           | ::= | iri `\| \|` blank blankNodePropertyList literal quotedTriple |
| [13]       | `literal`                          | ::= | RDFLiteral `\| \|` NumericLiteral BooleanLiteral |
| [14]       | `blank`                            | ::= | BlankNode `\|` collection                       |
| [15]       | `blankNodePropertyList`            | ::= | "`[`" predicateObjectList "`]`"                                                                                    |
| [16]       | `collection`                       | ::= | "`(`" object`*` "`)`"                                                                                                           |
| [17]       | `NumericLiteral`                   | ::= | INTEGER `\| \|` DECIMAL DOUBLE |
| [128s]     | `RDFLiteral`                       | ::= | String `( \|` LANGTAG "^^" iri`) )` |
| [133s]     | `BooleanLiteral`                   | ::= | "true" `\|` "false"                                                                                                                                                                                      |
| [18]       | `String`                           | ::= | STRING_LITERAL_QUOTE `\| \|` STRING_LITERAL_SINGLE_QUOTE STRING_LITERAL_LONG_SINGLE_QUOTE STRING_LITERAL_LONG_QUOTE |
| [135s]     | `iri`                              | ::= | IRIREF `\|` PrefixedName                         |
| [136s]     | `PrefixedName`                     | ::= | PNAME_LN `\|` PNAME_NS                             |
| [137s]     | `BlankNode`                        | ::= | BLANK_NODE_LABEL `\|` ANON                     |
| [27]       | `quotedTriple`                     | ::= | "<<" qtSubject predicate qtObject ">>" |
| [28]       | `qtSubject`                        | ::= | iri `\| \|` BlankNode quotedTriple |
| [29]       | `qtObject`                         | ::= | iri `\| \|` BlankNode literal quotedTriple |
| [30]       | `annotation`                       | ::= | "{\|" predicateObjectList "\|}"                                                                                    |
| @terminals | |     | **# Productions for terminals**                                                                                                                                                                          |
| [19]       | `IRIREF`                           | ::= | "`<`" `( [#x00-#x20```<>"{}\|^`\```] \|` UCHAR`) *` "`>`"                                                                        |
| [139s]     | `PNAME_NS`                         | ::= | PN_PREFIX`?` "`:`"                                                                                                           |
| [140s]     | `PNAME_LN`                         | ::= | PNAME_NS PN_LOCAL                                  |
| [141s]     | `BLANK_NODE_LABEL`                 | ::= | "_:" `( \|` PN_CHARS_U`] )` PN_CHARS "`.`"`) *` PN_CHARS`) ?` |
| [144s]     | `LANGTAG`                          | ::= | "`@`" `[ a-zA-Z] +` "`-`" `[ a-zA-Z0-9] +`                                                                                                                                                               |
| [20]       | `INTEGER`                          | ::= | `[ +-] ?] +`                                                                                                                                                                                             |
| [21]       | `DECIMAL`                          | ::= | `[ +-] ?] *` "`.`" `[ 0-9] +`                                                                                                                                                                            |
| [22]       | `DOUBLE`                           | ::= | `[ +-] ?] +` "`.`" `[ 0-9] *` EXPONENT`) \|` "`.`" `[ 0-9] +` EXPONENT`) \|] +` EXPONENT`) )` |
| [154s]     | `EXPONENT`                         | ::= | `[ eE] [] ?] +`                                                                                                                                                                                          |
| [23]       | `STRING_LITERAL_QUOTE`             | ::= | '`"`' `( [>"#x5C#x0A#x0D] \|` ECHAR UCHAR`) *` '`"`'     |
| [24]       | `STRING_LITERAL_SINGLE_QUOTE`      | ::= | "`'`" `( [#x27#x5C#x0A#x0D] \|` ECHAR UCHAR`) *` "`'`"   |
| [25]       | `STRING_LITERAL_LONG_SINGLE_QUOTE` | ::= | "'''" `( (` "`'`" `\|` "''"`) ?] \|` ECHAR UCHAR`) )` "'''" |
| [26]       | `STRING_LITERAL_LONG_QUOTE`        | ::= | '"""' `( (` '`"`' `\|` '""'`) ?] \|` ECHAR UCHAR`) )` '"""' |
| [27]       | `UCHAR`                            | ::= | `(` "\u" HEX HEX HEX HEX`) \|` "\U" HEX HEX HEX HEX HEX HEX HEX HEX`)` |
| [159s]     | `ECHAR`                            | ::= | "`\`" `[ tbnrf\"']`                                                                                                                                                                                      |
| [160s]     | `NIL`                              | ::= | "`(`" WS`*` "`)`"                                                                                                                   |
| [161s]     | `WS`                               | ::= | `#x20 \|`                                                                                                                                                                                                |
| [162s]     | `ANON`                             | ::= | "`[`" WS`*` "`]`"                                                                                                                   |
| [163s]     | `PN_CHARS_BASE`                    | ::= | `[ A-Z]`                                                                                                                                                                                                 |
|            | | \|  | `[ a-z]`                                                                                                                                                                                                 |
|            | | \|  | `[ #xC0-#xD6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xD8-#xF6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xF8-#x02FF]`                                                                                                                                                                                         |
|            | | \|  | `[ #x0370-#x037D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x037F-#x1FFF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x200C-#x200D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2070-#x218F]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2C00-#x2FEF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x3001-#xD7FF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xF900-#xFDCF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xFDF0-#xFFFD]`                                                                                                                                                                                       |
|            | | \|  | `[ #x00010000-#x000EFFFF]`                                                                                                                                                                               |
| [164s]     | `PN_CHARS_U`                       | ::= | PN_CHARS_BASE `\|` "`_`"                                                                                                 |
| [166s]     | `PN_CHARS`                         | ::= | PN_CHARS_U `\|` "`-`" `\| [] \|-#x036F] \|-#x2040]`                                                                         |
| [167s]     | `PN_PREFIX`                        | ::= | PN_CHARS_BASE `( (` PN_CHARS "`.`"`) *` PN_CHARS`) ?` |
| [168s]     | `PN_LOCAL`                         | ::= | `( \|` PN_CHARS_U "`:`" `\| [] \|` PLX`) (` PN_CHARS "`.`" `\|` "`:`" `\|` PLX`) *` PN_CHARS "`:`" `\|` PLX`) )` |
| [169s]     | `PLX`                              | ::= | PERCENT `\|` PN_LOCAL_ESC                       |
| [170s]     | `PERCENT`                          | ::= | "`%`" HEX HEX                                                |
| [171s]     | `HEX`                              | ::= | `[ 0-9] \|] \|]`                                                                                                                                                                                         |
| [172s]     | `PN_LOCAL_ESC`                     | ::= | "`\`" `(` "`_`" `\|` "`~`" `\|` "`.`" `\|` "`-`" `\|` "`!`" `\|` "`$`" `\|` "`&`" `\|` "`'`" `\|` "`(`" `\|` "`)`" `\|` "`*`" `\|` "`+`" `\|` "`,`" `\|` "`;`" `\|` "`=`" `\|` "`/`" `\|` "`?`" `\|` "`#`" `\|` "`@`" `\|` "`%`"`)` |

### C.3 N-Triples-Star EBNF Grammar

*This section is non-normative.*

The following is a complete grammar for N-Triples-Star.
The EBNF used here is defined in XML 1.0 [EBNF-NOTATION].

| [1]        | `ntriplesDoc`          | ::= | triple`? (` EOL triple`) *` EOL`?` |
| ---------- | ---------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [2]        | `triple`               | ::= | subject predicate object "`.`" |
| [3]        | `subject`              | ::= | IRIREF `\| \|` BLANK_NODE_LABEL quotedTriple |
| [4]        | `predicate`            | ::= | IRIREF                                                                                                                          |
| [5]        | `object`               | ::= | IRIREF `\| \|` BLANK_NODE_LABEL literal quotedTriple |
| [6]        | `literal`              | ::= | STRING_LITERAL_QUOTE `( (` "^^" IRIREF`) \|` LANGTAG`) ?` |
| [7t]       | `quotedTriple`         | ::= | "<<" subject predicate object ">>" |
| @terminals | |     | **# Productions for terminals**                                                                                                                                                                          |
| [144s]     | `LANGTAG`              | ::= | "`@`" `[ a-zA-Z] +` "`-`" `[ a-zA-Z0-9] +`                                                                                                                                                               |
| [7]        | `EOL`                  | ::= | `[ #x0D#x0A] +`                                                                                                                                                                                          |
| [8]        | `IRIREF`               | ::= | "`<`" `( [#x00-#x20```<>"{}\|^`\```] \|` UCHAR`) *` "`>`"                                                                        |
| [9]        | `STRING_LITERAL_QUOTE` | ::= | '`"`' `( [>"#x5C#x0A#x0D] \|` ECHAR UCHAR`) *` '`"`'     |
| [141s]     | `BLANK_NODE_LABEL`     | ::= | "_:" `( \|` PN_CHARS_U`] )` PN_CHARS "`.`"`) *` PN_CHARS`) ?` |
| [10]       | `UCHAR`                | ::= | `(` "\u" HEX HEX HEX HEX`) \|` "\U" HEX HEX HEX HEX HEX HEX HEX HEX`)` |
| [153s]     | `ECHAR`                | ::= | "`\`" `[ tbnrf"'\``]`                                                                                                                                                                                    |
| [157s]     | `PN_CHARS_BASE`        | ::= | `[ A-Z]`                                                                                                                                                                                                 |
|            | | \|  | `[ a-z]`                                                                                                                                                                                                 |
|            | | \|  | `[ #xC0-#xD6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xD8-#xF6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xF8-#x02FF]`                                                                                                                                                                                         |
|            | | \|  | `[ #x0370-#x037D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x037F-#x1FFF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x200C-#x200D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2070-#x218F]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2C00-#x2FEF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x3001-#xD7FF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xF900-#xFDCF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xFDF0-#xFFFD]`                                                                                                                                                                                       |
|            | | \|  | `[ #x00010000-#x000EFFFF]`                                                                                                                                                                               |
| [158s]     | `PN_CHARS_U`           | ::= | PN_CHARS_BASE `\|` "`_`" `\|` "`:`"                                                                                      |
| [160s]     | `PN_CHARS`             | ::= | PN_CHARS_U `\|` "`-`" `\| [] \|-#x036F] \|-#x2040]`                                                                         |
| [162s]     | `HEX`                  | ::= | `[ 0-9] \|] \|]`                                                                                                                                                                                         |

### C.4 N-Quads-Star EBNF Grammar

*This section is non-normative.*

The following is a complete grammar for N-Quads-Star.
The EBNF used here is defined in XML 1.0 [EBNF-NOTATION].

| [1]        | `nquadsDoc`            | ::= | statement`? (` EOL statement`) *` EOL`?` |
| ---------- | ---------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [2]        | `statement`            | ::= | subject predicate object graphLabel "`.`" |
| [3]        | `subject`              | ::= | IRIREF `\| \|` BLANK_NODE_LABEL quotedTriple |
| [4]        | `predicate`            | ::= | IRIREF                                                                                                                          |
| [5]        | `object`               | ::= | IRIREF `\| \|` BLANK_NODE_LABEL literal quotedTriple |
| [6]        | `graphLabel`           | ::= | IRIREF `\|` BLANK_NODE_LABEL                 |
| [7]        | `literal`              | ::= | STRING_LITERAL_QUOTE `( (` "^^" IRIREF`) \|` LANGTAG`) ?` |
| [7t]       | `quotedTriple`         | ::= | "<<" subject predicate object ">>" |
| @terminals | |     | **# Productions for terminals**                                                                                                                                                                          |
| [144s]     | `LANGTAG`              | ::= | "`@`" `[ a-zA-Z] +` "`-`" `[ a-zA-Z0-9] +`                                                                                                                                                               |
| [8]        | `EOL`                  | ::= | `[ #x0D#x0A] +`                                                                                                                                                                                          |
| [10]       | `IRIREF`               | ::= | "`<`" `( [#x00-#x20```<>"{}\|^`\```] \|` UCHAR`) *` "`>`"                                                                        |
| [11]       | `STRING_LITERAL_QUOTE` | ::= | '`"`' `( [>"#x5C#x0A#x0D] \|` ECHAR UCHAR`) *` '`"`'     |
| [141s]     | `BLANK_NODE_LABEL`     | ::= | "_:" `( \|` PN_CHARS_U`] )` PN_CHARS "`.`"`) *` PN_CHARS`) ?` |
| [12]       | `UCHAR`                | ::= | `(` "\u" HEX HEX HEX HEX`) \|` "\U" HEX HEX HEX HEX HEX HEX HEX HEX`)` |
| [153s]     | `ECHAR`                | ::= | "`\`" `[ tbnrf"'\``]`                                                                                                                                                                                    |
| [157s]     | `PN_CHARS_BASE`        | ::= | `[ A-Z]`                                                                                                                                                                                                 |
|            | | \|  | `[ a-z]`                                                                                                                                                                                                 |
|            | | \|  | `[ #xC0-#xD6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xD8-#xF6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xF8-#x02FF]`                                                                                                                                                                                         |
|            | | \|  | `[ #x0370-#x037D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x037F-#x1FFF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x200C-#x200D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2070-#x218F]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2C00-#x2FEF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x3001-#xD7FF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xF900-#xFDCF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xFDF0-#xFFFD]`                                                                                                                                                                                       |
|            | | \|  | `[ #x00010000-#x000EFFFF]`                                                                                                                                                                               |
| [158s]     | `PN_CHARS_U`           | ::= | PN_CHARS_BASE `\|` "`_`" `\|` "`:`"                                                                                      |
| [160s]     | `PN_CHARS`             | ::= | PN_CHARS_U `\|` "`-`" `\| [] \|-#x036F] \|-#x2040]`                                                                         |
| [162s]     | `HEX`                  | ::= | `[ 0-9] \|] \|]`                                                                                                                                                                                         |

### C.5 SPARQL-Star EBNF Grammar

*This section is non-normative.*

The following is a complete grammar for SPARQL-Star.
The EBNF used here is defined in XML 1.0 [EBNF-NOTATION].

| [1]        | `QueryUnit`                 | ::= | Query                                                                                                                            |
| ---------- | --------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [2]        | `Query`                     | ::= | Prologue `( \|` SelectQuery ConstructQuery DescribeQuery AskQuery`)` ValuesClause |
| [3]        | `UpdateUnit`                | ::= | Update                                                                                                                          |
| [4]        | `Prologue`                  | ::= | `( \|` BaseDecl PrefixDecl`) *`                  |
| [5]        | `BaseDecl`                  | ::= | "BASE" IRIREF                                                                                                                   |
| [6]        | `PrefixDecl`                | ::= | "PREFIX" PNAME_NS IRIREF                             |
| [7]        | `SelectQuery`               | ::= | SelectClause DatasetClause`*` WhereClause SolutionModifier |
| [8]        | `SubSelect`                 | ::= | SelectClause WhereClause SolutionModifier ValuesClause |
| [9]        | `SelectClause`              | ::= | "SELECT" `(` "DISTINCT" `\|` "REDUCED"`) ?` Var "`(`" Expression "AS" Var "`)`"`) )` "`*`"`)` |
| [10]       | `ConstructQuery`            | ::= | "CONSTRUCT"                                                                                                                                                                                              |
|            | |     | `( (` ConstructTemplate DatasetClause`*` WhereClause SolutionModifier`)(` DatasetClause`*` "WHERE" "`{`" TriplesTemplate`?` "`}`" SolutionModifier`) )` |
| [11]       | `DescribeQuery`             | ::= | "DESCRIBE" `(` VarOrIri`+ \|` "`*`"`)` DatasetClause`*` WhereClause`?` SolutionModifier |
| [12]       | `AskQuery`                  | ::= | "ASK" DatasetClause`*` WhereClause ValuesClause |
| [13]       | `DatasetClause`             | ::= | "FROM" `( \|` DefaultGraphClause NamedGraphClause`)` |
| [14]       | `DefaultGraphClause`        | ::= | SourceSelector                                                                                                          |
| [15]       | `NamedGraphClause`          | ::= | "NAMED" SourceSelector                                                                                                  |
| [16]       | `SourceSelector`            | ::= | iri                                                                                                                                |
| [17]       | `WhereClause`               | ::= | "WHERE"`?` GroupGraphPattern                                                                                         |
| [18]       | `SolutionModifier`          | ::= | GroupClause`?` HavingClause`?` OrderClause`?` LimitOffsetClauses`?` |
| [19]       | `GroupClause`               | ::= | "GROUP" "BY" GroupCondition`+`                                                                                          |
| [20]       | `GroupCondition`            | ::= | BuiltInCall `\| \|` FunctionCall "`( (`" Expression "AS" Var`) ?` "`)`"`) \|` Var |
| [21]       | `HavingClause`              | ::= | "HAVING" HavingCondition`+`                                                                                            |
| [22]       | `HavingCondition`           | ::= | Constraint                                                                                                                  |
| [23]       | `OrderClause`               | ::= | "ORDER" "BY" OrderCondition`+`                                                                                          |
| [24]       | `OrderCondition`            | ::= | `( (` "ASC" `\|` "DESC"`)` BrackettedExpression`) \|` Constraint Var`)` |
| [25]       | `LimitOffsetClauses`        | ::= | `(` LimitClause OffsetClause`? )` OffsetClause LimitClause`? )` |
| [26]       | `LimitClause`               | ::= | "LIMIT" INTEGER                                                                                                                |
| [27]       | `OffsetClause`              | ::= | "OFFSET" INTEGER                                                                                                               |
| [28]       | `ValuesClause`              | ::= | `(` "VALUES" DataBlock`) ?`                                                                                                  |
| [29]       | `Update`                    | ::= | Prologue `( (` Update1 "`;`" Update`) ?` |
| [30]       | `Update1`                   | ::= | Load `\| \|` Clear Drop Add Move Copy Create InsertData DeleteData DeleteWhere Modify |
| [31]       | `Load`                      | ::= | "LOAD" "SILENT"`? (` iri "INTO" GraphRef`) ?`           |
| [32]       | `Clear`                     | ::= | "CLEAR" "SILENT"`?` GraphRefAll                                                                                            |
| [33]       | `Drop`                      | ::= | "DROP" "SILENT"`?` GraphRefAll                                                                                             |
| [34]       | `Create`                    | ::= | "CREATE" "SILENT"`?` GraphRef                                                                                                 |
| [35]       | `Add`                       | ::= | "ADD" "SILENT"`?` GraphOrDefault "TO" GraphOrDefault |
| [36]       | `Move`                      | ::= | "MOVE" "SILENT"`?` GraphOrDefault "TO" GraphOrDefault |
| [37]       | `Copy`                      | ::= | "COPY" "SILENT"`?` GraphOrDefault "TO" GraphOrDefault |
| [38]       | `InsertData`                | ::= | "INSERT DATA" QuadData                                                                                                        |
| [39]       | `DeleteData`                | ::= | "DELETE DATA" QuadData                                                                                                        |
| [40]       | `DeleteWhere`               | ::= | "DELETE WHERE" QuadPattern                                                                                                 |
| [41]       | `Modify`                    | ::= | `(` "WITH" iri`) ?` DeleteClause InsertClause`? )` InsertClause`)` UsingClause`*` "WHERE" GroupGraphPattern |
| [42]       | `DeleteClause`              | ::= | "DELETE" QuadPattern                                                                                                       |
| [43]       | `InsertClause`              | ::= | "INSERT" QuadPattern                                                                                                       |
| [44]       | `UsingClause`               | ::= | "USING" `( \|` iri "NAMED" iri`) )`                          |
| [45]       | `GraphOrDefault`            | ::= | "DEFAULT" `\| (` "GRAPH"`?` iri`)`                                                                                                 |
| [46]       | `GraphRef`                  | ::= | "GRAPH" iri                                                                                                                        |
| [47]       | `GraphRefAll`               | ::= | GraphRef `\|` "DEFAULT" `\|` "NAMED" `\|` "ALL"                                                                               |
| [48]       | `QuadPattern`               | ::= | "`{`" Quads "`}`"                                                                                                                |
| [49]       | `QuadData`                  | ::= | "`{`" Quads "`}`"                                                                                                                |
| [50]       | `Quads`                     | ::= | TriplesTemplate`? (` QuadsNotTriples "`.`"`?` TriplesTemplate`? )` |
| [51]       | `QuadsNotTriples`           | ::= | "GRAPH" VarOrIri "`{`" TriplesTemplate`?` "`}`" |
| [52]       | `TriplesTemplate`           | ::= | TriplesSameSubject `(` "`.`" TriplesTemplate`? )` |
| [53]       | `GroupGraphPattern`         | ::= | "`{`" `( \|` SubSelect GroupGraphPatternSub`)` "`}`" |
| [54]       | `GroupGraphPatternSub`      | ::= | TriplesBlock`? (` GraphPatternNotTriples "`.`"`?` TriplesBlock`? )` |
| [55]       | `TriplesBlock`              | ::= | TriplesSameSubjectPath `(` "`.`" TriplesBlock`? )` |
| [56]       | `GraphPatternNotTriples`    | ::= | GroupOrUnionGraphPattern `\| \|` OptionalGraphPattern MinusGraphPattern GraphGraphPattern ServiceGraphPattern Filter Bind InlineData |
| [57]       | `OptionalGraphPattern`      | ::= | "*OPTIONAL*" GroupGraphPattern                                                                                       |
| [58]       | `GraphGraphPattern`         | ::= | "GRAPH" VarOrIri GroupGraphPattern        |
| [59]       | `ServiceGraphPattern`       | ::= | "SERVICE" "SILENT"`?` VarOrIri GroupGraphPattern |
| [60]       | `Bind`                      | ::= | "BIND" "`(`" Expression "AS" Var "`)`"                |
| [61]       | `InlineData`                | ::= | "VALUES" DataBlock                                                                                                           |
| [62]       | `DataBlock`                 | ::= | InlineDataOneVar `\|` InlineDataFull |
| [63]       | `InlineDataOneVar`          | ::= | Var "`{`" DataBlockValue`*` "`}`"                 |
| [64]       | `InlineDataFull`            | ::= | `( \|` NIL "`(`" Var`*` "`)`"`) )` "`{`" `( (` "`(`" DataBlockValue`*` "`)`"`) \|` NIL`) *` "`}`" |
| [65]       | `DataBlockValue`            | ::= | QuotedTriple `\| \|` iri RDFLiteral NumericLiteral BooleanLiteral "UNDEF" |
| [66]       | `MinusGraphPattern`         | ::= | "MINUS" GroupGraphPattern                                                                                            |
| [67]       | `GroupOrUnionGraphPattern`  | ::= | GroupGraphPattern `(` "UNION" GroupGraphPattern`) *` |
| [68]       | `Filter`                    | ::= | "FILTER" Constraint                                                                                                         |
| [69]       | `Constraint`                | ::= | BrackettedExpression `\| \|` BuiltInCall FunctionCall |
| [70]       | `FunctionCall`              | ::= | iri ArgList                                              |
| [71]       | `ArgList`                   | ::= | NIL `\| (` "`(`" "DISTINCT"`? (` Expression "`,`" Expression`) *` "`)`"`)` |
| [72]       | `ExpressionList`            | ::= | NIL `\| (` "`( (`" Expression "`,`" Expression`) *` "`)`"`)` |
| [73]       | `ConstructTemplate`         | ::= | "`{`" ConstructTriples`?` "`}`"                                                                                       |
| [74]       | `ConstructTriples`          | ::= | TriplesSameSubject `(` "`.`" ConstructTriples`? )` |
| [75]       | `TriplesSameSubject`        | ::= | `(` VarOrTermOrQuotedTP PropertyListNotEmpty`) \|` TriplesNode PropertyList`)` |
| [76]       | `PropertyList`              | ::= | PropertyListNotEmpty`?`                                                                                           |
| [77]       | `PropertyListNotEmpty`      | ::= | Verb ObjectList `(` "`;`" `(` Verb ObjectList`) ?` |
| [78]       | `Verb`                      | ::= | VarOrIri `\|` "`a`"                                                                                                           |
| [79]       | `ObjectList`                | ::= | Object `(` "`,`" Object`) *`                           |
| [80]       | `Object`                    | ::= | GraphNode AnnotationPattern`?`           |
| [81]       | `TriplesSameSubjectPath`    | ::= | `(` VarOrTermOrQuotedTP PropertyListPathNotEmpty`) \|` TriplesNodePath PropertyListPath`)` |
| [82]       | `PropertyListPath`          | ::= | PropertyListPathNotEmpty`?`                                                                                   |
| [83]       | `PropertyListPathNotEmpty`  | ::= | `( \|` VerbPath VerbSimple`) (` ObjectListPath "`;`" `( (` VerbPath VerbSimple`)` ObjectList`) ?` |
| [84]       | `VerbPath`                  | ::= | Path                                                                                                                              |
| [85]       | `VerbSimple`                | ::= | Var                                                                                                                                |
| [86]       | `ObjectListPath`            | ::= | ObjectPath `(` "`,`" ObjectPath`) *`           |
| [87]       | `ObjectPath`                | ::= | GraphNodePath AnnotationPatternPath`?` |
| [88]       | `Path`                      | ::= | PathAlternative                                                                                                        |
| [89]       | `PathAlternative`           | ::= | PathSequence `(` "`\|`" PathSequence`) *`  |
| [90]       | `PathSequence`              | ::= | PathEltOrInverse `(` "`/`" PathEltOrInverse`) *` |
| [91]       | `PathElt`                   | ::= | PathPrimary PathMod`?`                           |
| [92]       | `PathEltOrInverse`          | ::= | PathElt `\| (` "`^`" PathElt`)`                      |
| [93]       | `PathMod`                   | ::= | "`*`" `\|` "`?`" `\|` "`+`"                                                                                                                                                                              |
| [94]       | `PathPrimary`               | ::= | iri `\|` "`a`" `\| (` "`!`" PathNegatedPropertySet`) \|` "`(`" Path "`)`"`)` |
| [95]       | `PathNegatedPropertySet`    | ::= | PathOneInPropertySet `\| (` "`(`" `( (` PathOneInPropertySet "`\|`" PathOneInPropertySet`) *` "`)`"`)` |
| [96]       | `PathOneInPropertySet`      | ::= | iri `\|` "`a`" `\| (` "`^`" `( \|` iri "`a`"`) )`            |
| [97]       | `Integer`                   | ::= | INTEGER                                                                                                                        |
| [98]       | `TriplesNode`               | ::= | Collection `\|` BlankNodePropertyList |
| [99]       | `BlankNodePropertyList`     | ::= | "`[`" PropertyListNotEmpty "`]`"                                                                                  |
| [100]      | `TriplesNodePath`           | ::= | CollectionPath `\|` BlankNodePropertyListPath |
| [101]      | `BlankNodePropertyListPath` | ::= | "`[`" PropertyListPathNotEmpty "`]`"                                                                          |
| [102]      | `Collection`                | ::= | "`(`" GraphNode`+` "`)`"                                                                                                     |
| [103]      | `CollectionPath`            | ::= | "`(`" GraphNodePath`+` "`)`"                                                                                             |
| [104]      | `GraphNode`                 | ::= | VarOrTermOrQuotedTP `\|` TriplesNode |
| [105]      | `GraphNodePath`             | ::= | VarOrTermOrQuotedTP `\|` TriplesNodePath |
| [106]      | `VarOrTerm`                 | ::= | Var `\|` GraphTerm                                     |
| [107]      | `VarOrIri`                  | ::= | Var `\|` iri                                                 |
| [108]      | `Var`                       | ::= | VAR1 `\|` VAR2                                             |
| [109]      | `GraphTerm`                 | ::= | iri `\| \|` RDFLiteral NumericLiteral BooleanLiteral BlankNode NIL |
| [110]      | `Expression`                | ::= | ConditionalOrExpression                                                                                        |
| [111]      | `ConditionalOrExpression`   | ::= | ConditionalAndExpression `(` "\|\|" ConditionalAndExpression`) *` |
| [112]      | `ConditionalAndExpression`  | ::= | ValueLogical `(` "&&" ValueLogical`) *`    |
| [113]      | `ValueLogical`              | ::= | RelationalExpression                                                                                              |
| [114]      | `RelationalExpression`      | ::= | NumericExpression                                                                                                    |
|            | |     | `( (` "`=`" NumericExpression`)(` "!=" NumericExpression`) \|` "`<`" NumericExpression`) \|` "`>`" NumericExpression`) \|` "<=" NumericExpression`) \|` ">=" NumericExpression`) \|` "IN" ExpressionList`) \|` "NOT" "IN" ExpressionList`) )` |
| [115]      | `NumericExpression`         | ::= | AdditiveExpression                                                                                                  |
| [116]      | `AdditiveExpression`        | ::= | MultiplicativeExpression                                                                                      |
|            | |     | `( (` "`+`" MultiplicativeExpression`)(` "`-`" MultiplicativeExpression`) \|` NumericLiteralPositive NumericLiteralNegative`) (` "`*`" UnaryExpression`) \|` "`/`" UnaryExpression`) )` |
| [117]      | `MultiplicativeExpression`  | ::= | UnaryExpression `( (` "`*`" UnaryExpression`) \|` "`/`" UnaryExpression`) )` |
| [118]      | `UnaryExpression`           | ::= | `(` "`!`" PrimaryExpression`) \|` "`+`" PrimaryExpression`) \|` "`-`" PrimaryExpression`) \|` PrimaryExpression |
| [119]      | `PrimaryExpression`         | ::= | BrackettedExpression `\| \|` BuiltInCall iriOrFunction RDFLiteral NumericLiteral BooleanLiteral Var ExprQuotedTP |
| [120]      | `BrackettedExpression`      | ::= | "`(`" Expression "`)`"                                                                                                      |
| [121]      | `BuiltInCall`               | ::= | Aggregate                                                                                                                    |
|            | | \|  | `(` "STR" "`(`" Expression "`)`"`)`                                                                                         |
|            | | \|  | `(` "LANG" "`(`" Expression "`)`"`)`                                                                                        |
|            | | \|  | `(` "LANGMATCHES" "`(`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "DATATYPE" "`(`" Expression "`)`"`)`                                                                                    |
|            | | \|  | `(` "BOUND" "`(`" Var "`)`"`)`                                                                                                     |
|            | | \|  | `(` "IRI" "`(`" Expression "`)`"`)`                                                                                         |
|            | | \|  | `(` "URI" "`(`" Expression "`)`"`)`                                                                                         |
|            | | \|  | `(` "BNODE" `( (` "`(`" Expression "`)`"`) \|` NIL`) )` |
|            | | \|  | `(` "RAND" NIL`)`                                                                                                                  |
|            | | \|  | `(` "ABS" "`(`" Expression "`)`"`)`                                                                                         |
|            | | \|  | `(` "CEIL" "`(`" Expression "`)`"`)`                                                                                        |
|            | | \|  | `(` "FLOOR" "`(`" Expression "`)`"`)`                                                                                       |
|            | | \|  | `(` "ROUND" "`(`" Expression "`)`"`)`                                                                                       |
|            | | \|  | `(` "CONCAT" ExpressionList`)`                                                                                          |
|            | | \|  | SubstringExpression                                                                                                |
|            | | \|  | `(` "STRLEN" "`(`" Expression "`)`"`)`                                                                                      |
|            | | \|  | StrReplaceExpression                                                                                              |
|            | | \|  | `(` "UCASE" "`(`" Expression "`)`"`)`                                                                                       |
|            | | \|  | `(` "LCASE" "`(`" Expression "`)`"`)`                                                                                       |
|            | | \|  | `(` "ENCODE_FOR_URI" "`(`" Expression "`)`"`)`                                                                              |
|            | | \|  | `(` "CONTAINS" "`(`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "STRSTARTS" "`(`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "STRENDS" "`(`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "STRBEFORE" "`(`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "STRAFTER" "`(`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "YEAR" "`(`" Expression "`)`"`)`                                                                                        |
|            | | \|  | `(` "MONTH" "`(`" Expression "`)`"`)`                                                                                       |
|            | | \|  | `(` "DAY" "`(`" Expression "`)`"`)`                                                                                         |
|            | | \|  | `(` "HOURS" "`(`" Expression "`)`"`)`                                                                                       |
|            | | \|  | `(` "MINUTES" "`(`" Expression "`)`"`)`                                                                                     |
|            | | \|  | `(` "SECONDS" "`(`" Expression "`)`"`)`                                                                                     |
|            | | \|  | `(` "TIMEZONE" "`(`" Expression "`)`"`)`                                                                                    |
|            | | \|  | `(` "TZ" "`(`" Expression "`)`"`)`                                                                                          |
|            | | \|  | `(` "NOW" NIL`)`                                                                                                                   |
|            | | \|  | `(` "UUID" NIL`)`                                                                                                                  |
|            | | \|  | `(` "STRUUID" NIL`)`                                                                                                               |
|            | | \|  | `(` "MD5" "`(`" Expression "`)`"`)`                                                                                         |
|            | | \|  | `(` "SHA1" "`(`" Expression "`)`"`)`                                                                                        |
|            | | \|  | `(` "SHA224" "`(`" Expression "`)`"`)`                                                                                      |
|            | | \|  | `(` "SHA256" "`(`" Expression "`)`"`)`                                                                                      |
|            | | \|  | `(` "SHA384" "`(`" Expression "`)`"`)`                                                                                      |
|            | | \|  | `(` "SHA512" "`(`" Expression "`)`"`)`                                                                                      |
|            | | \|  | `(` "COALESCE" ExpressionList`)`                                                                                        |
|            | | \|  | `(` "IF" "`(`" Expression "`,`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "STRLANG" "`(`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "STRDT" "`(`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "sameTerm" "`(`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "isIRI" "`(`" Expression "`)`"`)`                                                                                       |
|            | | \|  | `(` "isURI" "`(`" Expression "`)`"`)`                                                                                       |
|            | | \|  | `(` "isBLANK" "`(`" Expression "`)`"`)`                                                                                     |
|            | | \|  | `(` "isLITERAL" "`(`" Expression "`)`"`)`                                                                                   |
|            | | \|  | `(` "isNUMERIC" "`(`" Expression "`)`"`)`                                                                                   |
|            | | \|  | `(` "TRIPLE" "`(`" Expression "`,`" Expression "`,`" Expression "`)`"`)` |
|            | | \|  | `(` "SUBJECT" "`(`" Expression "`)`"`)`                                                                                     |
|            | | \|  | `(` "PREDICATE" "`(`" Expression "`)`"`)`                                                                                   |
|            | | \|  | `(` "OBJECT" "`(`" Expression "`)`"`)`                                                                                      |
|            | | \|  | `(` "isTRIPLE" "`(`" Expression "`)`"`)`                                                                                    |
|            | | \|  | RegexExpression                                                                                                        |
|            | | \|  | ExistsFunc                                                                                                                  |
|            | | \|  | NotExistsFunc                                                                                                            |
| [122]      | `RegexExpression`           | ::= | "REGEX" "`(`" Expression "`, (`" Expression "`,`" Expression`) ?` "`)`" |
| [123]      | `SubstringExpression`       | ::= | "SUBSTR" "`(`" Expression "`, (`" Expression "`,`" Expression`) ?` "`)`" |
| [124]      | `StrReplaceExpression`      | ::= | "REPLACE" "`(`" Expression "`,`" Expression "`, (`" Expression "`,`" Expression`) ?` "`)`" |
| [125]      | `ExistsFunc`                | ::= | "EXISTS" GroupGraphPattern                                                                                           |
| [126]      | `NotExistsFunc`             | ::= | "NOT" "EXISTS" GroupGraphPattern                                                                                     |
| [127]      | `Aggregate`                 | ::= | `(` "COUNT" "`(`" "DISTINCT"`? (` "`*`"Expression`)` "`)`"`)`                                                               |
|            | | \|  | `(` "SUM" "`(`" "DISTINCT"`?` Expression "`)`"`)`                                                                           |
|            | | \|  | `(` "MIN" "`(`" "DISTINCT"`?` Expression "`)`"`)`                                                                           |
|            | | \|  | `(` "MAX" "`(`" "DISTINCT"`?` Expression "`)`"`)`                                                                           |
|            | | \|  | `(` "AVG" "`(`" "DISTINCT"`?` Expression "`)`"`)`                                                                           |
|            | | \|  | `(` "SAMPLE" "`(`" "DISTINCT"`?` Expression "`)`"`)`                                                                        |
|            | | \|  | `(` "GROUP_CONCAT" "`(`" "DISTINCT"`? (` Expression "`;`" "SEPARATOR" "`=`" String`) ?` "`)`"`)` |
| [128]      | `iriOrFunction`             | ::= | iri ArgList`?`                                           |
| [129]      | `RDFLiteral`                | ::= | String `( \|` LANGTAG "^^" iri`) )` |
| [130]      | `NumericLiteral`            | ::= | NumericLiteralUnsigned `\| \|` NumericLiteralPositive NumericLiteralNegative |
| [131]      | `NumericLiteralUnsigned`    | ::= | INTEGER `\| \|` DECIMAL DOUBLE |
| [132]      | `NumericLiteralPositive`    | ::= | INTEGER_POSITIVE `\| \|` DECIMAL_POSITIVE DOUBLE_POSITIVE |
| [133]      | `NumericLiteralNegative`    | ::= | INTEGER_NEGATIVE `\| \|` DECIMAL_NEGATIVE DOUBLE_NEGATIVE |
| [134]      | `BooleanLiteral`            | ::= | "true" `\|` "false"                                                                                                                                                                                      |
| [135]      | `String`                    | ::= | STRING_LITERAL1 `\| \|` STRING_LITERAL2 STRING_LITERAL_LONG1 STRING_LITERAL_LONG2 |
| [136]      | `iri`                       | ::= | IRIREF `\|` PrefixedName                         |
| [137]      | `PrefixedName`              | ::= | PNAME_LN `\|` PNAME_NS                             |
| [138]      | `BlankNode`                 | ::= | BLANK_NODE_LABEL `\|` ANON                     |
| [174]      | `QuotedTP`                  | ::= | "<<" qtSubjectOrObject Verb qtSubjectOrObject ">>" |
| [175]      | `QuotedTriple`              | ::= | "<<" DataValueTerm `( \|` iri "`a`"`)` DataValueTerm ">>" |
| [176]      | `qtSubjectOrObject`         | ::= | Var `\| \|` BlankNode iri RDFLiteral NumericLiteral BooleanLiteral QuotedTP |
| [177]      | `DataValueTerm`             | ::= | iri `\| \|` RDFLiteral NumericLiteral BooleanLiteral QuotedTriple |
| [178]      | `VarOrTermOrQuotedTP`       | ::= | Var `\| \|` GraphTerm QuotedTP |
| [179]      | `AnnotationPattern`         | ::= | "{\|" PropertyListNotEmpty "\|}"                                                                                  |
| [180]      | `AnnotationPatternPath`     | ::= | "{\|" PropertyListPathNotEmpty "\|}"                                                                          |
| [181]      | `ExprQuotedTP`              | ::= | "<<" ExprVarOrTerm Verb ExprVarOrTerm ">>" |
| [182]      | `ExprVarOrTerm`             | ::= | iri `\| \|` RDFLiteral NumericLiteral BooleanLiteral Var ExprQuotedTP |
| @terminals | |     | **# Productions for terminals**                                                                                                                                                                          |
| [139]      | `IRIREF`                    | ::= | "`<`" `( [] --#x20] )` "`>`"                                                                                                                                                                             |
| [140]      | `PNAME_NS`                  | ::= | PN_PREFIX`?` "`:`"                                                                                                           |
| [141]      | `PNAME_LN`                  | ::= | PNAME_NS PN_LOCAL                                  |
| [142]      | `BLANK_NODE_LABEL`          | ::= | "_:" `( \|` PN_CHARS_U`] )` PN_CHARS "`.`"`) *` PN_CHARS`) ?` |
| [143]      | `VAR1`                      | ::= | "`?`" VARNAME                                                                                                                  |
| [144]      | `VAR2`                      | ::= | "`$`" VARNAME                                                                                                                  |
| [145]      | `LANGTAG`                   | ::= | "`@`" `[ a-zA-Z] +` "`-`" `[ a-zA-Z0-9] +`                                                                                                                                                               |
| [146]      | `INTEGER`                   | ::= | `[ 0-9] +`                                                                                                                                                                                               |
| [147]      | `DECIMAL`                   | ::= | `[ 0-9] *` "`.`" `[ 0-9] +`                                                                                                                                                                              |
| [148]      | `DOUBLE`                    | ::= | `( [] +` "`.`" `[ 0-9] *` EXPONENT`) \|` "`.`" `[ 0-9] +` EXPONENT`) \|] +` EXPONENT`)` |
| [149]      | `INTEGER_POSITIVE`          | ::= | "`+`" INTEGER                                                                                                                  |
| [150]      | `DECIMAL_POSITIVE`          | ::= | "`+`" DECIMAL                                                                                                                  |
| [151]      | `DOUBLE_POSITIVE`           | ::= | "`+`" DOUBLE                                                                                                                    |
| [152]      | `INTEGER_NEGATIVE`          | ::= | "`-`" INTEGER                                                                                                                  |
| [153]      | `DECIMAL_NEGATIVE`          | ::= | "`-`" DECIMAL                                                                                                                  |
| [154]      | `DOUBLE_NEGATIVE`           | ::= | "`-`" DOUBLE                                                                                                                    |
| [155]      | `EXPONENT`                  | ::= | `[ eE] [] ?] +`                                                                                                                                                                                          |
| [156]      | `STRING_LITERAL1`           | ::= | "`'`" `( [#x27#x5C#x0A#x0D] \|` ECHAR`) *` "`'`"                                                                                 |
| [157]      | `STRING_LITERAL2`           | ::= | '`"`' `( [>"#x5C#x0A#x0D] \|` ECHAR`) *` '`"`'                                                                                   |
| [158]      | `STRING_LITERAL_LONG1`      | ::= | "'''" `( (` "`'`" `\|` "''"`) ?] \|` ECHAR`) )` "'''"                                                                            |
| [159]      | `STRING_LITERAL_LONG2`      | ::= | '"""' `( (` '`"`' `\|` '""'`) ?] \|` ECHAR`) )` '"""'                                                                            |
| [160]      | `ECHAR`                     | ::= | "`\`" `[ tbnrf\"']`                                                                                                                                                                                      |
| [161]      | `NIL`                       | ::= | "`(`" WS`*` "`)`"                                                                                                                   |
| [162]      | `WS`                        | ::= | `#x20 \|`                                                                                                                                                                                                |
| [163]      | `ANON`                      | ::= | "`[`" WS`*` "`]`"                                                                                                                   |
| [164]      | `PN_CHARS_BASE`             | ::= | `[ A-Z]`                                                                                                                                                                                                 |
|            | | \|  | `[ a-z]`                                                                                                                                                                                                 |
|            | | \|  | `[ #xC0-#xD6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xD8-#xF6]`                                                                                                                                                                                           |
|            | | \|  | `[ #xF8-#x02FF]`                                                                                                                                                                                         |
|            | | \|  | `[ #x0370-#x037D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x037F-#x1FFF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x200C-#x200D]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2070-#x218F]`                                                                                                                                                                                       |
|            | | \|  | `[ #x2C00-#x2FEF]`                                                                                                                                                                                       |
|            | | \|  | `[ #x3001-#xD7FF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xF900-#xFDCF]`                                                                                                                                                                                       |
|            | | \|  | `[ #xFDF0-#xFFFD]`                                                                                                                                                                                       |
|            | | \|  | `[ #x00010000-#x000EFFFF]`                                                                                                                                                                               |
| [165]      | `PN_CHARS_U`                | ::= | PN_CHARS_BASE `\|` "`_`"                                                                                                 |
| [166]      | `VARNAME`                   | ::= | `( \|` PN_CHARS_U`] )` PN_CHARS_U`] \|-#x036F] \|-#x2040] )` |
| [167]      | `PN_CHARS`                  | ::= | PN_CHARS_U `\|` "`-`" `\| [] \|-#x036F] \|-#x2040]`                                                                         |
| [168]      | `PN_PREFIX`                 | ::= | PN_CHARS_BASE `( (` PN_CHARS "`.`"`) *` PN_CHARS`) ?` |
| [169]      | `PN_LOCAL`                  | ::= | `( \|` PN_CHARS_U`] )` PN_CHARS "`.`"`) *` PN_CHARS`) ?` |
| [170]      | `PLX`                       | ::= | PERCENT `\|` PN_LOCAL_ESC                       |
| [171]      | `PERCENT`                   | ::= | "`%`" HEX HEX                                                |
| [172]      | `HEX`                       | ::= | `[ 0-9] \|] \|]`                                                                                                                                                                                         |
| [173]      | `PN_LOCAL_ESC`              | ::= | "`\`" `(` "`_`" `\|` "`~`" `\|` "`.`" `\|` "`-`" `\|` "`!`" `\|` "`$`" `\|` "`&`" `\|` "`'`" `\|` "`(`" `\|` "`)`" `\|` "`*`" `\|` "`+`" `\|` "`,`" `\|` "`;`" `\|` "`=`" `\|` "`/`" `\|` "`?`" `\|` "`#`" `\|` "`@`" `\|` "`%`"`)` |

## E. References

### E.1 Normative references

[N-QUADS]

[RDF 1.1 N-Quads](https://www.w3.org/TR/n-quads/). Gavin Carothers. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/n-quads/>

[N-TRIPLES]

[RDF 1.1 N-Triples](https://www.w3.org/TR/n-triples/). Gavin Carothers; Andy Seaborne. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/n-triples/>

[RDF-SPARQL-XMLRES]

[SPARQL Query Results XML Format (Second Edition)](https://www.w3.org/TR/rdf-sparql-XMLres/). Dave Beckett; Jeen Broekstra. W3C. 21 March 2013. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-sparql-XMLres/>

[RDF11-CONCEPTS]

[RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). Richard Cyganiak; David Wood; Markus Lanthaler. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf11-concepts/>

[RDF11-MT]

[RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/). Patrick Hayes; Peter Patel-Schneider. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf11-mt/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

[SPARQL11-QUERY]

[SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/). Steven Harris; Andy Seaborne. W3C. 21 March 2013. W3C Recommendation. URL: <https://www.w3.org/TR/sparql11-query/>

[SPARQL11-RESULTS-JSON]

[SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/sparql11-results-json/). Andy Seaborne. W3C. 21 March 2013. W3C Recommendation. URL: <https://www.w3.org/TR/sparql11-results-json/>

[SPARQL11-UPDATE]

[SPARQL 1.1 Update](https://www.w3.org/TR/sparql11-update/). Paula Gearon; Alexandre Passant; Axel Polleres. W3C. 21 March 2013. W3C Recommendation. URL: <https://www.w3.org/TR/sparql11-update/>

[TRIG]

[RDF 1.1 TriG](https://www.w3.org/TR/trig/). Gavin Carothers; Andy Seaborne. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/trig/>

[TURTLE]

[RDF 1.1 Turtle](https://www.w3.org/TR/turtle/). Eric Prud'hommeaux; Gavin Carothers. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/turtle/>

[XML]

[Extensible Markup Language (XML) 1.0 (Fifth Edition)](https://www.w3.org/TR/xml/). Tim Bray; Jean Paoli; Michael Sperberg-McQueen; Eve Maler; François Yergeau et al. W3C. 26 November 2008. W3C Recommendation. URL: <https://www.w3.org/TR/xml/>

[XPATH-FUNCTIONS]

[XQuery 1.0 and XPath 2.0 Functions and Operators (Second Edition)](https://www.w3.org/TR/xpath-functions/). Ashok Malhotra; Jim Melton; Norman Walsh; Michael Kay. W3C. 14 December 2010. W3C Recommendation. URL: <https://www.w3.org/TR/xpath-functions/>

### E.2 Informative references

[DX-PROF-CONNEG]

[Content Negotiation by Profile](https://www.w3.org/TR/dx-prof-conneg/). Lars G. Svensson; Nicholas Car. W3C. 26 November 2019. W3C Working Draft. URL: <https://www.w3.org/TR/dx-prof-conneg/>

[EBNF-NOTATION]

[EBNF NOTATION](https://www.w3.org/TR/REC-xml/#sec-notation). Tim Bray; Jean Paoli; C. M. Sperberg-McQueen; Eve Maler; François Yergeau. W3C. 26 November 2008. W3C Recommendation. URL: [http://www.w3.org/TR/REC-xml/#sec-notation](https://www.w3.org/TR/REC-xml/#sec-notation)

[JSON-LD]

[JSON-LD 1.0](https://www.w3.org/TR/json-ld/). Manu Sporny; Gregg Kellogg; Markus Lanthaler. W3C. 3 November 2020. W3C Recommendation. URL: <https://www.w3.org/TR/json-ld/>

[OWL2-Overview]

[OWL 2 Web Ontology Language Document Overview (Second Edition)](https://www.w3.org/TR/owl2-overview/). W3C OWL Working Group. W3C. 11 December 2012. W3C Recommendation. URL: <https://www.w3.org/TR/owl2-overview/>

[RDF-STAR-FOUNDATION]

[Foundations of RDF* and SPARQL* - An Alternative Approach to Statement-Level Metadata in RDF.](http://ceur-ws.org/Vol-1912/paper12.pdf). Olaf Hartig. In Proceedings of the 11th Alberto Mendelzon International Workshop on Foundations of Data Management (AMW), Montevideo, Uruguay. June 2017. URL: <http://ceur-ws.org/Vol-1912/paper12.pdf>

[RDF-SYNTAX-GRAMMAR]

[RDF 1.1 XML Syntax](https://www.w3.org/TR/rdf-syntax-grammar/). Fabien Gandon; Guus Schreiber. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-syntax-grammar/>

[SPARQL11-SERVICE-DESCRIPTION]

[SPARQL 1.1 Service Description](https://www.w3.org/TR/sparql11-service-description/). Gregory Williams. W3C. 21 March 2013. W3C Recommendation. URL: <https://www.w3.org/TR/sparql11-service-description/>

Permalink

**Referenced in:**

- § 2. Concepts and Abstract Syntax (2) (3) (4) (5) (6) (7)
- § 3.1 Annotation Syntax
- § 3.2 Turtle-star
- § 3.2.2 Parsing (2)
- § 3.3 TriG-star
- § 3.4.2 Parsing
- § 3.5 N-Quads-star
- § 4.1 Initial Definitions
- § 4.6 Evaluation Semantics
- § 5.3 Semantics
- § 6. RDF-star Semantics
- § 6.1 Mapping RDF-star abstract syntax to RDF
- § 6.2 Entailment of RDF-star graphs (2) (3) (4) (5) (6)
- § 6.3 Merging RDF-star graphs
- § 6.4.1 Implementing the RDF-star semantics (2)
- § 6.4.2 Combining RDF-star graphs
- § 6.4.3 Other uses of the unstar mapping (2) (3)
- § 7.1 Core vocabulary (2)
- § 7.3 Vocabulary semantics

Permalink

**Referenced in:**

- § 1.2 Overview
- § 2. Concepts and Abstract Syntax (2) (3) (4) (5) (6) (7) (8) (9) (10) (11) (12) (13) (14)
- § 2.3 Triples and occurrences (2)
- § 3.2.2 Parsing (2) (3) (4)
- § 3.4 N-Triples-star
- § 3.4.2 Parsing (2) (3)
- § 3.5 N-Quads-star
- § 4.1 Initial Definitions (2)
- § 4.2 Grammar
- § 4.4 Function and Operator Definitions
- § 4.4.1 TRIPLE
- § 4.4.2 SUBJECT
- § 4.4.3 PREDICATE
- § 4.4.4 OBJECT
- § 4.4.5 isTRIPLE
- § 5.1.1 INSERT DATA
- § 5.3 Semantics
- § 6.1 Mapping RDF-star abstract syntax to RDF
- § 7.1 Core vocabulary

Permalink

**Referenced in:**

- § 2.3 Triples and occurrences
- § 3.2.2 Parsing (2)
- § 4.1 Initial Definitions (2) (3)
- § 4.4 Function and Operator Definitions (2) (3)
- § 4.4.8 sparql-compare

Permalink

**Referenced in:**

- § 2. Concepts and Abstract Syntax (2) (3) (4)
- § 6.1 Mapping RDF-star abstract syntax to RDF (2) (3)
- § 6.3 Merging RDF-star graphs

Permalink

**Referenced in:**

- § 1.2 Overview (2)
- § 1.3 Common misconceptions (2) (3) (4)
- § 1.6 Conformance (2)
- § 2. Concepts and Abstract Syntax
- § 2.1 Quoted and Asserted Triples (2)
- § 2.2 RDF-star Graph Examples
- § 2.3 Triples and occurrences (2)
- § 3.1 Annotation Syntax (2)
- § 3.2.1 Grammar (2)
- § 3.2.2 Parsing
- § 3.2.2.1 Discussion (2) (3)
- § 3.3 TriG-star
- § 3.3.2 Parsing
- § 3.3.3 Discussion
- § 3.4 N-Triples-star
- § 3.4.1 Grammar
- § 3.5 N-Quads-star
- § 4.2 Grammar
- § 4.5 Examples and Discussion
- § 4.7 Query Result Formats
- § 4.7.1 SPARQL-star Query Results JSON Format (2) (3)
- § 4.7.2 SPARQL-star Query Results XML Format (2) (3)
- § 5.1.1 INSERT DATA (2)
- § 5.1.2 DELETE DATA
- § 5.1.3 DELETE/INSERT (2)
- § 6.1 Mapping RDF-star abstract syntax to RDF (2) (3) (4) (5) (6)
- § 6.2 Entailment of RDF-star graphs
- § 6.4.2 Combining RDF-star graphs (2) (3) (4)
- § 6.4.3 Other uses of the unstar mapping (2) (3)
- § 6.4.4 Referential opacity (2) (3) (4)
- § 6.4.5 Selective referential transparency
- § 6.4.6 Other alternatives to referential opacity
- § 7.1 Core vocabulary
- § 7.2 Extended vocabulary
- § 7. RDF-star vocabulary
- § A. IANA Considerations (2) (3)
- § B.1 SA-mode and PG-mode (2) (3) (4)
- § B.2 The seminal example (2)

Permalink

**Referenced in:**

- § 1.2 Overview (2) (3)
- § 2. Concepts and Abstract Syntax
- § 2.1 Quoted and Asserted Triples
- § 2.2 RDF-star Graph Examples
- § 3.2.1 Grammar
- § 3.2.2.1 Discussion
- § 4.5 Examples and Discussion (2) (3) (4)
- § 5.1.1 INSERT DATA (2)
- § 5.1.2 DELETE DATA (2) (3)
- § 5.1.3 DELETE/INSERT (2)
- § 6.1 Mapping RDF-star abstract syntax to RDF (2) (3)
- § 6.3 Merging RDF-star graphs
- § 6.4.6 Other alternatives to referential opacity (2)
- § B.1 SA-mode and PG-mode (2) (3) (4) (5)

Permalink

**Referenced in:**

- § 2. Concepts and Abstract Syntax (2)
- § 3.3 TriG-star
- § 3.5 N-Quads-star
- § 4.5 Examples and Discussion (2) (3)
- § 4.6 Evaluation Semantics

Permalink

**Referenced in:**

- § 1.2 Overview
- § 3.2.2.1 Discussion

Permalink

**Referenced in:**

- § 3.2.2.1 Discussion
- § 3.3.2 Parsing

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 4.1 Initial Definitions (2) (3) (4)
- § 4.2 Grammar
- § 4.3.2 Expand Syntax Forms
- § 4.3.3 Translate Property Path Patterns (2) (3)

Permalink

**Referenced in:**

- § 4.1 Initial Definitions (2) (3)
- § 4.3.1 Variable Scope
- § 4.3.4 Translate Basic Graph Patterns
- § 4.6 Evaluation Semantics

Permalink

**Referenced in:**

- § 4.2 Grammar
- § 4.3.3 Translate Property Path Patterns (2)

Permalink

**Referenced in:**

- § 4.1 Initial Definitions (2) (3) (4) (5)
- § 4.5 Examples and Discussion (2)
- § 4.6 Evaluation Semantics (2)
- § 5.3 Semantics

Permalink

**Referenced in:**

- § 4.1 Initial Definitions
- § 4.6 Evaluation Semantics

Permalink

**Referenced in:**

- § 4.6 Evaluation Semantics

Permalink

**Referenced in:**

- § 4.3.1 Variable Scope
- § 4.3.2 Expand Syntax Forms (2) (3) (4)
- § 4.3.3 Translate Property Path Patterns (2) (3) (4)
- § 4.3.4 Translate Basic Graph Patterns

Permalink

**Referenced in:**

- § 4.3.2 Expand Syntax Forms

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 4.4.10 Operator Mappings (2) (3) (4) (5) (6)

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 6.1 Mapping RDF-star abstract syntax to RDF (2) (3)
- § 6.2 Entailment of RDF-star graphs (2) (3) (4) (5)
- § 6.4.1 Implementing the RDF-star semantics
- § 6.4.2 Combining RDF-star graphs (2) (3) (4) (5) (6) (7) (8) (9) (10) (11) (12)
- § 6.4.3 Other uses of the unstar mapping (2) (3) (4) (5) (6)
- § 6.4.4 Referential opacity
- § 6.4.6 Other alternatives to referential opacity (2)

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 7.3 Vocabulary semantics
