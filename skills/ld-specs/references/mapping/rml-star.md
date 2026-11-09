---
title: "RML-star"
source: https://w3id.org/rml/star/spec
family: mapping
spec_date: 2023-05-10
fetched: 2026-11-09
---

# RML-star

> Generating RDF-star quoted triples (W3C CG draft).

## Contents

- Abstract
- 1 Conformance
- 2 Introduction
  - 2.1 Overview
  - 2.2 Conventions
- 3 The RML-star vocabulary
  - 3.1 Overview of RML-star terms
- 4 Generating quoted triples with RML-star
- 5 Generating quoted triples from multiple sources
  - 5.1 Using star map together with referencing object maps
- 6 Generating deeply nested quoted triples
- A References
  - A.1 Normative references

---

## Abstract

This document describes the [RML] vocabulary and approach to generate RDF-star [RDF-star].

## 1. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

## 2. Introduction

*This section is non-normative.*

### 2.1 Overview

RDF-star [RDF-star] is an extension of the Resource Description Framework (RDF) [RDF11-Concepts] that introduces a new kind of term, the [quoted triple](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted), which can be referred from the subjects or objects of other triples. Triples that include a quoted triple are known as [RDF-star triples](https://w3c.github.io/rdf-star/cg-spec/editors_draft.html#dfn-triple).

```
# The triple ( :Alice a :Person ) is 80% likely to be true
<< :Alice a :Person >> :confidence 0.8 .
```

In RDF 1.1, an [asserted triple](https://www.w3.org/2021/12/rdf-star.html#dfn-asserted) is an element of the set of triples that compose an [RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph). In RDF-star, a quoted triple can be asserted, if it is also included in the RDF graph, or not, if it only occurs as a quoted triple.

```
# The triple ( :Alice a :Person ) is asserted and quoted
< :Alice a :Person > .
<< :Alice a :Person >> :confidence 0.8 .
```

The RDF Mapping Language (RML) [RML] is a language for expressing mappings between heterogeneous data and RDF. In RML, rules can be expressed to iterate over a data source and refer to specific data within an iteration. Using these iterators and references, RML rules define how to express data in the data source in RDF. RML is based on and extends R2RML [R2RML]. R2RML is defined to express customized mappings only from relational databases to RDF datasets.

This document describes RML-star: an extension of RML that enables the generation of RDF-star graphs with RML.

### 2.2 Conventions

This document assumes that the reader is familiar with RDF, RML and RDF-star concepts.

In this document, examples assume that the following prefixes have been declared to represent the IRIs shown with them:

| Prefix | Namespace                           |
| ------ | ----------------------------------- |
| `rml:` | <http://w3id.org/rml/>              |
| `xsd:` | <http://www.w3.org/2001/XMLSchema#> |
| `ex:`  | <http://example.org/>               |
| `:`    | <http://example.org/>               |

The examples are contained in color-coded boxes. We use the Turtle syntax [Turtle] to write RDF and the N-Triples-star syntax [RDF-star] to write RDF-star.

```
# This box contains an example input
```

```
# This box contains an example mapping
```

```
# This box contains the example output
```

## 3. The RML-star vocabulary

An *RML-star mapping* defines a mapping from any data in a structured source format to RDF-star. It consists of one or more [Triples Maps](https://w3id.org/core/spec/#triples-map) that can in turn contain Triples Maps within the subject or object. A Triples Map can be Asserted or Non Asserted, depending on whether the triples that they generate should be included in the output graph.

The input to an RML-star mapping is called input data source. The output of an RML-star mapping is called output dataset.

The output dataset of an RML-star mapping is an RDF-star dataset that contains the generated [RDF-star triples](https://www.w3.org/2021/12/rdf-star.html#dfn-triple) for each of the [Triples Maps](https://w3id.org/core/spec/#triples-map) in the RML-star mapping. An RML-star processor may provide additional triples or graphs.

As in RML, conforming *RML-star processors* may rename blank nodes when providing access to the output dataset.

An RML-star processor has access to one of the followings:

- an execution environment consisting of an SQL connection and an input database (as stated by the [R2RML] specification).
- an input data source (as stated by the [RML] specification).

A *base IRI* is used in resolving relative IRIs produced by the RML-star mappings. According to the [R2RML] specification, the base IRI must be a valid [IRI]. It should not contain question mark (“?”) or hash (“#”) characters and should end in a slash (“/”) character.

The RML-star vocabulary consists of the RML-star specific defined classes but also includes some [RML] classes.

- `rml:TriplesMap` is the class of Triples Maps as defined by RML-core.
- `rml:AssertedTriplesMap` is the class of Triples Maps that are asserted.
- `rml:NonAssertedTriplesMap` is the class of Triples Maps that are not asserted, but only quoted.
- `rml:LogicalSource` is the class of logical sources as defined by RML-core.
- `rml:TermMap` is the class of Term Maps, as defined by RML-core. It has the following subclasses:
  * `rml:SubjectMap` is the class of Subject Maps.
  * `rml:PredicateMap` is the class of Predicate Maps.
  * `rml:ObjectMap` is the class of Object Maps.
  * `rml:GraphMap` is the class of graph maps.
  * `rml:LanguageMap` is the class of language maps as defined by RML-core.
  * `rml:DatatypeMap` is the class of datatype maps as defined by RML-core.
- `rml:StarMap` is the class of RDF-star Term Maps.
- `rml:PredicateObjectMap` is the class of Predicate-Object Maps.
- `rml:RefObjectMap` is the class of referencing Object Maps.
- `rml:Join` is the class of join conditions.
- `rml:ReferenceFormulation` is the class of supported reference formulations as defined by RML.

### 3.1 Overview of RML-star terms

The RML-star terms are summarized in the following tables.
This vocabulary involves three classes (`rml:StarMap`, `rml:AssertedTriplesMap` and `rml:NonAssertedTriplesMap`), and one object property (`rml:quotedTriplesMap`).

| Property               | Domain        | Range                                                 |
| ---------------------- | ------------- | ----------------------------------------------------- |
| `rml:quotedTriplesMap` | `rml:StarMap` | `rml:AssertedTriplesMap or rml:NonAssertedTriplesMap` |

| Class                       | Superclass       |
| --------------------------- | ---------------- |
| `rml:StarMap`               | `owl:Thing`      |
| `rml:AssertedTriplesMap`    | `rml:TriplesMap` |
| `rml:NonAssertedTriplesMap` | `rml:TriplesMap` |

All RML-star additions and changes to RML are shown in Figure 1:

![Target structure](https://kg-construct.github.io/rml-star/spec/docs/resources/images/rml-star_diagram.png)

*Figure 1 To enable the generation of RDF-star graphs, RML-star adds three classes and one object property to the RML ontology.*

## 4. Generating quoted triples with RML-star

A *Star Map* (`rml:StarMap`) is similar to a [term map](https://w3id.org/core/spec/#term-map) that generates [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted).
It can be used within Subject or Object Maps.
A Star Map is linked to a [Triples Map](https://w3id.org/core/spec/#triples-map) by the *quoted Triples Map* property (`rml:quotedTriplesMap`).
The [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) generated by a Star Map are exactly those triples generated by its quoted Triples Map.
If a Star Map has the same [logical source](https://w3id.org/core/spec/#logical-source) as its quoted Triples Map, then for each [logical iteration](https://w3id.org/core/spec/#iterator), the [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) generated by a Star Map are those triples generated by its quoted Triples Map *for the same logical iteration*.
If a Star Map has a different logical source than its quoted Triples Map then a join is used, as described in the next section (§5).

In the following example, for each logical iteration (i.e., each CSV row) a "type" triple is generated by `<#innerTriplesMap>` that occurs
in the resulting graph both as an asserted and as a quoted triple:

```
# Contents of the ex:ConfidenceSource logical source
entity , class  , confidence
Alice  , Person , 0.8
Bobby  , Dog    , 0.6
```

```
# Triples Map that generates "type" triples that are asserted and quoted
<#innerTriplesMap>
    a rml:AssertedTriplesMap;
    rml:logicalSource ex:ConfidenceSource;
    rml:subjectMap [
        rml:template "http://example.com/{entity}"
    ];
    rml:predicateObjectMap [
        rml:predicate rdf:type;
        rml:objectMap [ rml:template "http://example.com/{class}" ];
    ].

# Triples Map that generates "confidence" triples
<#outerTriplesMap>
    a rml:AssertedTriplesMap;
    rml:logicalSource ex:ConfidenceSource;
    rml:subjectMap [
        rml:quotedTriplesMap <#innerTriplesMap>;
    ];
    rml:predicateObjectMap [
        rml:predicate ex:confidence;
        rml:objectMap [ rml:reference "confidence" ];
    ].
```

```
# Triples generated by <#innerTriplesMap>
ex:Alice a ex:Person .
ex:Bobby a ex:Dog .

# Triples generated by <#outerTriplesMap>
<< ex:Alice a ex:Person >> ex:confidence 0.8 .
<< ex:Bobby a ex:Dog >> ex:confidence 0.6 .
```

The previous example shows a [quoted triple](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) within a Subject Map.
Since [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) can be both subjects or objects, Star Maps can also
be used in the position of Object Maps, as shown in the following example:

```
# Contents of the ex:ConfidenceSource logical source
entity , pet     , class
Alice  , Bobby   , Dog
Steve  , Pumpkin , Cat
```

```
# Triples Map that generates "type" triples that are asserted and quoted
<#innerTriplesMap>
    a rml:AssertedTriplesMap;
    rml:logicalSource ex:ConfidenceSource;
    rml:subjectMap [
        rml:template "http://example.com/{pet}"
    ];
    rml:predicateObjectMap [
        rml:predicate rdf:type;
        rml:objectMap [ rml:template "http://example.com/{class}" ];
    ].

# Triples Map that generates "has pet" triples
<#outerTriplesMap>
    a rml:AssertedTriplesMap;
    rml:logicalSource ex:ConfidenceSource;
    rml:subjectMap [
        rml:template "http://example.com/{entity}";
    ];
    rml:predicateObjectMap [
        rml:predicate ex:has_pet;
        rml:objectMap [ rml:quotedTriplesMap <#innerTriplesMap> ];
    ].
```

```
# Triples generated by <#innerTriplesMap>
ex:Bobby a ex:Dog .
ex:Pumpkin a ex:Cat .

# Triples generated by <#outerTriplesMap>
ex:Alice ex:has_pet << ex:Bobby a ex:Dog >> .
ex:Steve ex:has_pet << ex:Pumpkin a ex:Cat >> .
```

Asserted Triples Map generate [asserted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-asserted).
If an Asserted Triples Map is also used in a Star Map, the triples it generates *also* occur in the resulting graph as [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted), by the process explained above.
To generate [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) without assering them, Non Asserted Triples Maps are used instead.
A Triples Map of subclass non-asserted Triples Map does not generate [asserted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-asserted),
but might generate [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) if it is used in a Star Map.

The following example is different than the previous in that `<#innerTriplesMap>` is declared to be an instance of `rml:NonAssertedTriplesMap`, with the effect that the generated "type" triples are only present in the resulting graph as [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted), not as [asserted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-asserted):

```
# Contents of the ex:ConfidenceSource logical source
entity , class  , confidence
Alice  , Person , 0.8
Bobby  , Dog    , 0.6
```

```
# Triples Map that generates "type" triples that are only quoted, not asserted
<#innerTriplesMap>
    a rml:NonAssertedTriplesMap;
    rml:logicalSource ex:ConfidenceSource;
    rml:subjectMap [
        rml:template "http://example.com/{entity}";
    ];
    rml:predicateObjectMap [
        rml:predicate rdf:type;
        rml:objectMap [ rml:template "http://example.com/{class}" ];
    ].

# Triples Map that generates "confidence" triples
<#outerTriplesMap>
    a rml:AssertedTriplesMap;
    rml:logicalSource ex:ConfidenceSource;
    rml:subjectMap [
        rml:quotedTriplesMap <#innerTriplesMap>;
    ];
    rml:predicateObjectMap [
        rml:predicate ex:confidence;
        rml:objectMap [ rml:reference "confidence" ];
    ].
```

```
<< ex:Alice a ex:Person >> ex:confidence 0.8 .
<< ex:Bobby a ex:Dog >> ex:confidence 0.6 .
```

A summary of how to generate triples in any combination of [asserted](https://www.w3.org/2021/12/rdf-star.html#dfn-asserted) and/or [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) is given in the following table:

|                  | Quoted                                         | Not quoted                                     |
| ---------------- | ---------------------------------------------- | ---------------------------------------------- |
| **Asserted**     | `rml:AssertedTriplesMap rml:StarMap` *with*    | `rml:AssertedTriplesMap rml:StarMap` *without* |
| **Not asserted** | `rml:NonAssertedTriplesMap rml:StarMap` *with* | -                                              |

It should be noted that Non Asserted Triples Maps that are not quoted do not generate any triple. For this reason, the use of `rml:NonAssertedTriplesMap` **without** `rml:StarMap` **is not allowed**. `rml:NonAssertedTriplesMap` must always be called with `rml:quotedTriplesMap`.

## 5. Generating quoted triples from multiple sources

RML-star can create RDF-star triples from multiple [logical sources](https://w3id.org/core/spec/#logical-source).
When creating RDF-star triples from multiple [logical sources](https://w3id.org/core/spec/#logical-source), [join conditions](https://w3id.org/core/spec/#join-condition) are used, just like when using [referencing object maps](https://w3id.org/core/spec/#referencing-object-map) in RML.

If a star map has a [join condition](https://w3id.org/core/spec/#join-condition), it generates [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) as follows. Each combination of iterations, i.e., the [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product), from the *child source* and the *parent source* is looked at. Here, we consider as child source the [logical source](https://w3id.org/core/spec/#logical-source) of the [Triples Map](https://w3id.org/core/spec/#triples-map) in which the star map occurs, and as parent source the logical source of the star map's Quoted Triples Map. A star map only generates quoted triples for combinations in which the join condition holds true. As is the case when [join conditions are used in in referencing object maps](https://w3id.org/core/spec/#logical-join), a join condition checks for equality of the [reference values](https://w3id.org/core/spec/#reference-value) of the [child](https://w3id.org/core/spec/#child-reference)/[parent reference](https://w3id.org/core/spec/#parent-reference) between iterations of the child/parent source.

If the [logical source](https://w3id.org/core/spec/#logical-source) of Triples Map in which a star map occurs and the logical source of star map's Quoted Triples Map are not identical, then the star map must have at least one [join condition](https://w3id.org/core/spec/#join-condition).

```
# Contents of logical source ex:ClassesSource
entity , class
Alice  , Person
Bobby  , Dog
```

```
# Contents of logical source ex:ConfidencesSource
entity , confidence
Alice  , 0.8
Bobby  , 0.6
```

```
# Triples Map that generates "type" triples
<#innerTriplesMap>
    a rml:NonAssertedTriplesMap ;
    rml:logicalSource ex:ClassesSource ;
    rml:subjectMap [
        rml:template "http://example.com/{entity}"
    ];
    rml:predicateObjectMap [
        rml:predicate rdf:type ;
        rml:objectMap [ rml:template "http://example.com/{class}" ]
    ].

# Triples Map that generates "confidence" triples
<#outerTriplesMap>
    a rml:AssertedTriplesMap;
    rml:logicalSource ex:ConfidencesSource;
    rml:subjectMap [
        rml:quotedTriplesMap <#innerTriplesMap>
        rml:joinCondition [
            rml:parent "entity";
            rml:child "entity";
        ];
    ];
    rml:predicateObjectMap [
        rml:predicate ex:confidence;
        rml:objectMap [ rml:reference "confidence" ];
    ].
```

```
<< ex:Alice a ex:Person >> ex:confidence 0.8 .
<< ex:Bobby a ex:Dog >> ex:confidence 0.6 .
```

### 5.1 Using star map together with referencing object maps

It is also possible to generate [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) which themselves are built from multiple sources.
This is done by using a Quoted Triples Map which contains a [referencing object map](https://w3id.org/core/spec/#referencing-object-map).

Note: this process for generating [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) with a [referencing object map](https://w3id.org/core/spec/#referencing-object-map) is not different from the general process to create quoted triples described earlier (§4), but we include this section for clarity.

```
# Contents of logical source ex:ClassesSource
entity , class
Alice  , Person
Bobby  , Dog
```

```
# Contents of logical source ex:ConfidencesSource
entity , confidence
Alice  , 0.8
Bobby  , 0.6
```

```
# Triples Map that generates objects of "type" triples
<#classTriplesMap>
    a rml:AssertedTriplesMap;
    rml:logicalSource ex:ClassesSource;
    rml:subjectMap [
        rml:template "http://example.com/{class}";
    ].

# Triples Map that generates "type" triples using a join
<#innerTriplesMap>
    a rml:NonAssertedTriplesMap;
    rml:logicalSource ex:ConfidencesSource;
    rml:subjectMap [
        rml:template "http://example.com/{entity}";
    ];
    rml:predicateObjectMap [
        rml:predicate rdf:type ;
        rml:objectMap [
            rml:parentTriplesMap <#classTriplesMap> ;
            rml:joinCondition [
                rml:parent "entity" ;
                rml:child "entity" ;
            ];
        ];
    ].

# Triples Map that generates "confidence" triples
<#outerTriplesMap>
    a rml:AssertedTriplesMap;
    rml:logicalSource ex:ConfidencesSource;
    rml:subjectMap [
        rml:quotedTriplesMap <#innerTriplesMap>;
    ];
    rml:predicateObjectMap [
        rml:predicate ex:confidence;
        rml:objectMap [ rml:reference "confidence" ];
    ].
```

```
<< ex:Alice a ex:Person >> ex:confidence 0.8 .
<< ex:Bobby a ex:Dog >> ex:confidence 0.6 .
```

## 6. Generating deeply nested quoted triples

It is possible to create more deeply nested RDF-star by using a Quoted Triples Map that on its own turn also uses a Quoted Triples Map.

Note: this process for generating deeply nested [quoted triples](https://www.w3.org/2021/12/rdf-star.html#dfn-quoted) is not different from the general process to create quoted triples described earlier (§4), but we include this section for clarity.

```
# Contents of Logical Source ex:PredictionsSource
entity , class   , confidence , predictor
Alice  , Person  , 0.8        , alpha
Alice  , Giraffe , 1.0        , alpha
Bobby  , Dog     , 0.6        , alpha
Bobby  , Giraffe , 1.0        , beta
```

```
# Triples Map that generates "type" triples
<#innerTriplesMap>
    a rml:NonAssertedTriplesMap;
    rml:logicalSource ex:PredictionsSource;
    rml:subjectMap [
        rml:template "http://example.com/{entity}";
    ];
    rml:predicateObjectMap [
        rml:predicate rdf:type;
        rml:objectMap [ rml:template "http://example.com/{class}" ];
    ].

# Triples Map that generates "confidence" triples
<#middleTriplesMap>
    a rml:NonAssertedTriplesMap;
    rml:logicalSource ex:PredictionsSource;
    rml:subjectMap [
        rml:quotedTriplesMap <#innerTriplesMap>;
    ];
    rml:predicateObjectMap [
        rml:predicate ex:confidence;
        rml:objectMap [ rml:reference "confidence" ];
    ].

# Triples Map that generates "predicted by" triples
<#outerTriplesMap>
    a rml:AssertedTriplesMap;
    rml:logicalSource ex:PredictionsSource;
    rml:subjectMap [
        rml:quotedTriplesMap <#middleTriplesMap>;
    ];
    rml:predicateObjectMap [
        rml:predicate ex:predictedBy;
        rml:objectMap [ rml:template "http://example.com/{predictor}" ];
    ].
```

```
<< << ex:Alice a ex:Person >> ex:confidence 0.8 >> ex:predictedBy ex:alpha .
<< << ex:Alice a ex:Giraffe >> ex:confidence 1.0 >> ex:predictedBy ex:beta .
<< << ex:Bobby a ex:Dog >> ex:confidence 0.6 >> ex:predictedBy ex:alpha .
<< << ex:Bobby a ex:Giraffe >> ex:confidence 1.0 >> ex:predictedBy ex:beta .
```

## A. References

### A.1 Normative references

[IRI]

[Internationalized Resource Identifiers (IRIs)](https://www.rfc-editor.org/rfc/rfc3987). M. Duerst; M. Suignard. IETF. January 2005. Proposed Standard. URL: <https://www.rfc-editor.org/rfc/rfc3987>

[R2RML]

[R2RML: RDB to RDF Mapping Language](https://www.w3.org/TR/r2rml/). W3C. 27 September 2012. W3C Recommendation. URL: <https://www.w3.org/TR/r2rml/>

[RDF-star]

[RDF-star and SPARQL-star](https://www.w3.org/2021/12/rdf-star.html). W3C. 17 December 2021. Final Community Group Report. URL: <https://www.w3.org/2021/12/rdf-star.html>

[RDF11-Concepts]

[RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf11-concepts/>

[RML]

[RDF Mapping Language - Core](https://w3id.org/core/spec/). https://www.w3.org/community/kg-construct/. 30 June 2023. Draft Community Group Report. URL: <https://w3id.org/core/spec/>

[Turtle]

[RDF 1.1 Turtle](https://www.w3.org/TR/turtle/). W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/turtle/>

Permalink

**Referenced in:**

- § 3. The RML-star vocabulary

Permalink

**Referenced in:**

- § 3. The RML-star vocabulary (2)

Permalink

**Referenced in:**

- § 3. The RML-star vocabulary

Permalink

**Referenced in:**

- § 4. Generating quoted triples with RML-star (2) (3) (4)
- § 5. Generating quoted triples from multiple sources (2)

Permalink

**Referenced in:**

- § 4. Generating quoted triples with RML-star (2) (3)
- § 5. Generating quoted triples from multiple sources (2)
- § 5.1 Using star map together with referencing object maps
- § 6. Generating deeply nested quoted triples
