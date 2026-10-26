---
title: "SPARQL 1.2 Service Description"
source: https://www.w3.org/TR/sparql12-service-description/
family: sparql
version: "1.2"
status: W3C Working Draft
spec_date: 2026-04-23
fetched: 2026-10-26
---

# SPARQL 1.2 Service Description

> Describing SPARQL services with RDF.

## Contents

- Abstract
- 1 Introduction
  - 1.1 Terminology
- 2 Accessing a Service Description
- 3 Service Description Vocabulary
  - 3.1 SPARQL Service Description Namespace and OWL Ontology
  - 3.2 Properties
    - 3.2.1 sd:endpoint
    - 3.2.2 sd:feature
    - 3.2.3 sd:defaultEntailmentRegime
    - 3.2.4 sd:entailmentRegime
    - 3.2.5 sd:defaultSupportedEntailmentProfile
    - 3.2.6 sd:supportedEntailmentProfile
    - 3.2.7 sd:extensionFunction
    - 3.2.8 sd:extensionAggregate
    - 3.2.9 sd:languageExtension
    - 3.2.10 sd:supportedLanguage
    - 3.2.11 sd:supportedVersion
    - 3.2.12 sd:propertyFeature
    - 3.2.13 sd:defaultDataset
    - 3.2.14 sd:availableGraphs
    - 3.2.15 sd:resultFormat
    - 3.2.16 sd:inputFormat
    - 3.2.17 sd:defaultGraph
    - 3.2.18 sd:namedGraph
    - 3.2.19 sd:name
    - 3.2.20 sd:graph
  - 3.3 Classes
    - 3.3.1 sd:Service
    - 3.3.2 sd:Feature
    - 3.3.3 sd:Language
    - 3.3.4 sd:Function
    - 3.3.5 sd:Aggregate
    - 3.3.6 sd:EntailmentRegime
    - 3.3.7 sd:EntailmentProfile
    - 3.3.8 sd:GraphCollection
    - 3.3.9 sd:Dataset
    - 3.3.10 sd:Graph
    - 3.3.11 sd:NamedGraph
  - 3.4 Instances
    - 3.4.1 sd:SPARQL10Query
    - 3.4.2 sd:SPARQL11Query
    - 3.4.3 sd:SPARQL11Update
    - 3.4.4 sd:SPARQLQuery
    - 3.4.5 sd:SPARQLUpdate
    - 3.4.6 sd:DereferencesURIs
    - 3.4.7 sd:UnionDefaultGraph
    - 3.4.8 sd:RequiresDataset
    - 3.4.9 sd:EmptyGraphs
    - 3.4.10 sd:BasicFederatedQuery
    - 3.4.11 Other Instances
- 4 Example (Informative)
  - 4.1 RDF/XML Service Description
  - 4.2 Turtle Service Description
- 5 Conformance
  - 5.1 Conformance
- A Changes between SPARQL 1.1 Service Description and SPARQL 1.2 Service Description
- B Privacy Considerations
- C Security Considerations
- D Internationalization Considerations
- E Index
  - E.1 Terms defined by this specification
  - E.2 Terms defined by reference
- F References
  - F.1 Normative references
  - F.2 Informative references

---

## Abstract

This document describes SPARQL service description, a method for discovering, and vocabulary for describing SPARQL services made available via the [SPARQL 1.2 Protocol](https://www.w3.org/TR/sparql12-protocol/). These descriptions provide a mechanism by which a client or end user can discover
information about the SPARQL service such as supported extension functions and details about the available dataset.

## 1. Introduction

A SPARQL service description lists the features of a SPARQL service made available via the [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/). This document describes both a method for discovering a service description from a specific SPARQL service and an RDF schema for encoding such descriptions in RDF.

### 1.1 Terminology

When this document uses the words *MUST*, *MUST NOT*, *SHOULD*, *SHOULD NOT*,
and *MAY*, and the words appear as emphasized text, they must be
interpreted as described in [RFC2119].

The following terms are also in use throughout this document:

SPARQL Service

Any implementation conforming to the [SPARQL 1.2 Protocol](https://www.w3.org/TR/sparql12-protocol/) (this document's use of "SPARQL Service" is the same as "[SPARQL Protocol service](https://www.w3.org/TR/sparql12-protocol/#terminology)" as defined in the SPARQL 1.2 Protocol) [SPARQL12-PROTOCOL].

SPARQL endpoint

The URI at which a SPARQL Service listens for requests from clients.

## 2. Accessing a Service Description

SPARQL services made available via the SPARQL Protocol *SHOULD* return a service description document at the service endpoint when
dereferenced using the HTTP GET operation without any query parameter strings provided. This service description *MUST* be made
available in an RDF serialization, *MAY* be embedded in (X)HTML by way of [RDFa Core 1.1 - Third Edition](https://www.w3.org/TR/rdfa-core/), and *SHOULD* use [content negotiation](https://httpwg.org/specs/rfc9110.html#content.negotiation) if available in other RDF representations.

## 3. Service Description Vocabulary

### 3.1 SPARQL Service Description Namespace and OWL Ontology

The SPARQL service description namespace IRI is:

[http://www.w3.org/ns/sparql-service-description#](https://www.w3.org/ns/sparql-service-description#)

The prefix used in this document for this namespace is `sd`.

An RDF encoding of the Service Description ontology is available by HTTP content negotiation from the [namespace IRI](https://www.w3.org/ns/sparql-service-description#).

### 3.2 Properties

#### 3.2.1 sd:endpoint

Relates an instance of `sd:Service` (§3.3.1) to a SPARQL endpoint that implements the [SPARQL Protocol service](https://www.w3.org/TR/sparql12-protocol/#terminology) for the service. The object of the sd:endpoint property is an IRI.

| type:   | `owl:InverseFunctionalProperty`                                                |
| ------- | ------------------------------------------------------------------------------ |
| domain: | `sd:Service` (§3.3.1) |

#### 3.2.2 sd:feature

Relates an instance of `sd:Service` (§3.3.1) with a resource representing a supported feature.

| domain: | `sd:Service` (§3.3.1) |
| ------- | ------------------------------------------------------------------------------ |
| range:  | `sd:Feature` (§3.3.2) |

#### 3.2.3 sd:defaultEntailmentRegime

Relates an instance of `sd:Service` (§3.3.1) with a resource representing an entailment regime used for basic graph pattern matching. This property is
intended for use when a single entailment regime by default applies to all graphs in the default dataset of the service. In situations where a different entailment regime applies to a
specific graph in the dataset, the `sd:entailmentRegime` (§3.2.4) property should be used to indicate this fact in the description of that graph.

| subPropertyOf: | `sd:feature` (§3.2.2)                   |
| -------------- | ------------------------------------------------------------------------------------------------ |
| domain:        | `sd:Service` (§3.3.1)                   |
| range:         | `sd:EntailmentRegime` (§3.3.6) |

#### 3.2.4 sd:entailmentRegime

Relates a named graph description with a resource representing an entailment regime used for basic graph pattern matching over that graph.

| domain: | `sd:NamedGraph` (§3.3.11)             |
| ------- | ------------------------------------------------------------------------------------------------ |
| range:  | `sd:EntailmentRegime` (§3.3.6) |

#### 3.2.5 sd:defaultSupportedEntailmentProfile

Relates an instance of `sd:Service` (§3.3.1) with a resource representing a supported profile of the default entailment regime (as declared by `sd:defaultEntailmentRegime` (§3.2.3)). Entailment profiles are discussed more in [SPARQL 1.2 Entailment Regimes](https://www.w3.org/TR/sparql12-entailment/#OWL2ProfilesDS) [SPARQL12-ENTAILMENT].

Note that this specification does not make any conformance requirements on the compatibility of an advertised entailment profile with the advertised entailment regime in a service
description. Providing a reasonable combination of values to the §3.2.4 sd:entailmentRegime/§3.2.3 sd:defaultEntailmentRegime and §3.2.6 sd:supportedEntailmentProfile/§3.2.5 sd:defaultSupportedEntailmentProfile properties is up to
the creator of a service description.

| subPropertyOf: | `sd:feature` (§3.2.2)                     |
| -------------- | -------------------------------------------------------------------------------------------------- |
| domain:        | `sd:Service` (§3.3.1)                     |
| range:         | `sd:EntailmentProfile` (§3.3.7) |

#### 3.2.6 sd:supportedEntailmentProfile

Relates a named graph description with a resource representing a supported profile of the entailment regime (as declared by `sd:entailmentRegime` (§3.2.4)) used for basic graph pattern matching over that graph.

| domain: | `sd:NamedGraph` (§3.3.11)               |
| ------- | -------------------------------------------------------------------------------------------------- |
| range:  | `sd:EntailmentProfile` (§3.3.7) |

#### 3.2.7 sd:extensionFunction

Relates an instance of `sd:Service` (§3.3.1) to a function that may be used in a SPARQL [SELECT expression](https://www.w3.org/TR/sparql12-query/#selectExpressions) or a [FILTER](https://www.w3.org/TR/sparql12-query/#expressions), [HAVING](https://www.w3.org/TR/sparql12-query/#having), [GROUP BY](https://www.w3.org/TR/sparql12-query/#groupby), [ORDER BY](https://www.w3.org/TR/sparql12-query/#modOrderBy), or [BIND](https://www.w3.org/TR/sparql12-query/#bind) clause.

| subPropertyOf: | `sd:feature` (§3.2.2)   |
| -------------- | -------------------------------------------------------------------------------- |
| domain:        | `sd:Service` (§3.3.1)   |
| range:         | `sd:Function` (§3.3.4) |

#### 3.2.8 sd:extensionAggregate

Relates an instance of `sd:Service` (§3.3.1) to an aggregate that may be used in a SPARQL aggregate query (for instance in a [HAVING](https://www.w3.org/TR/sparql12-query/#having) clause or [SELECT expression](https://www.w3.org/TR/sparql12-query/#selectExpressions)) besides the standard list of [supported aggregates](https://www.w3.org/TR/sparql12-query/#aggregates) COUNT, SUM, MIN, MAX, AVG, GROUP_CONCAT, and SAMPLE.

| subPropertyOf: | `sd:feature` (§3.2.2)     |
| -------------- | ---------------------------------------------------------------------------------- |
| domain:        | `sd:Service` (§3.3.1)     |
| range:         | `sd:Aggregate` (§3.3.5) |

#### 3.2.9 sd:languageExtension

Relates an instance of `sd:Service` (§3.3.1) to a resource representing an implemented extension to the SPARQL Query or Update language.

| subPropertyOf: | `sd:feature` (§3.2.2) |
| -------------- | ------------------------------------------------------------------------------ |
| domain:        | `sd:Service` (§3.3.1) |
| range:         | `sd:Feature` (§3.3.2) |

#### 3.2.10 sd:supportedLanguage

Relates an instance of `sd:Service` (§3.3.1) to a SPARQL language (e.g. Query and Update) that it implements.

| subPropertyOf: | `sd:feature` (§3.2.2)   |
| -------------- | -------------------------------------------------------------------------------- |
| domain:        | `sd:Service` (§3.3.1)   |
| range:         | `sd:Language` (§3.3.3) |

#### 3.2.11 sd:supportedVersion

Relates an instance of `sd:Service` (§3.3.1) to a SPARQL language version that it supports.

This property is related to the `sd:supportedLanguage` property, as the combination of language and version will indicate a specific feature set supported by the service.
For example, when a service description indicates support for the `sd:SPARQLQuery` language and [`sparql:version-1.2-basic`](https://www.w3.org/ns/sparql#version-1.2-basic) version, support for SPARQL 1.2 Query [SPARQL12-QUERY] with [RDF 1.2 Basic conformance](https://www.w3.org/TR/rdf12-concepts/#dfn-basic) is indicated.

| subPropertyOf: | `sd:feature` (§3.2.2) |
| -------------- | ------------------------------------------------------------------------------ |
| domain:        | `sd:Service` (§3.3.1) |
| range:         | `rdfs:Resource`                                                                |

#### 3.2.12 sd:propertyFeature

Relates an instance of `sd:Service` (§3.3.1) to a resource representing an implemented feature that extends the SPARQL Query or Update language and that is
accessed by using the named property.

| subPropertyOf: | `sd:feature` (§3.2.2) |
| -------------- | ------------------------------------------------------------------------------ |
| domain:        | `sd:Service` (§3.3.1) |
| range:         | `sd:Feature` (§3.3.2) |

#### 3.2.13 sd:defaultDataset

Relates an instance of `sd:Service` (§3.3.1) to a description of the default dataset available when no explicit dataset is specified in the query, update
request or via protocol parameters.

| type:   | `owl:InverseFunctionalProperty`                                                |
| ------- | ------------------------------------------------------------------------------ |
| domain: | `sd:Service` (§3.3.1) |
| range:  | `sd:Dataset` (§3.3.9) |

#### 3.2.14 sd:availableGraphs

Relates an instance of `sd:Service` (§3.3.1) to a description of the graphs which are allowed in the construction of a dataset via the SPARQL Protocol, with
FROM/FROM NAMED clauses in a query, or with USING/USING NAMED in an update request, if the service limits the scope of dataset construction.

| domain: | `sd:Service` (§3.3.1)                 |
| ------- | ---------------------------------------------------------------------------------------------- |
| range:  | `sd:GraphCollection` (§3.3.8) |

#### 3.2.15 sd:resultFormat

Relates an instance of `sd:Service` (§3.3.1) to a format that is supported for serializing query results.

URIs for commonly used serialization formats are defined by [Unique URIs for File Formats](https://www.w3.org/ns/formats/). For formats that do not have an
existing URI, the `<http://www.w3.org/ns/formats/media_type>` and `<http://www.w3.org/ns/formats/preferred_suffix>` properties defined in that document *SHOULD* be used to describe the format.

| domain: | `sd:Service` (§3.3.1) |
| ------- | ------------------------------------------------------------------------------ |
| range:  | `<http://www.w3.org/ns/formats/Format>`                                        |

#### 3.2.16 sd:inputFormat

Relates an instance of `sd:Service` (§3.3.1) to a format that is supported for parsing RDF input; for example, via a SPARQL 1.2 Update [LOAD statement](https://www.w3.org/TR/sparql12-update/#load), or when URIs are dereferenced in FROM/FROM NAMED/USING/USING NAMED clauses (see also §3.4.6 sd:DereferencesURIs below).

URIs for commonly used serialization formats are defined by [Unique URIs for File Formats](https://www.w3.org/ns/formats/). For formats that do not have an
existing URI, the `<http://www.w3.org/ns/formats/media_type>` and `<http://www.w3.org/ns/formats/preferred_suffix>` properties defined in that document *SHOULD* be used to describe the format.

| domain: | `sd:Service` (§3.3.1) |
| ------- | ------------------------------------------------------------------------------ |
| range:  | `<http://www.w3.org/ns/formats/Format>`                                        |

#### 3.2.17 sd:defaultGraph

Relates an instance of `sd:Dataset` (§3.3.9) to the description of its default graph.

| domain: | `sd:Dataset` (§3.3.9) |
| ------- | ------------------------------------------------------------------------------ |
| range:  | `sd:Graph` (§3.3.10)     |

#### 3.2.18 sd:namedGraph

Relates an instance of `sd:GraphCollection` (§3.3.8) (or its subclass `sd:Dataset` (§3.3.9)) to the description of one of
its named graphs. The description of such a named graph *MUST* include the `sd:name` (§3.2.19) property
and *MAY* include the `sd:graph` (§3.2.20) property.

| domain: | `sd:GraphCollection` (§3.3.8) |
| ------- | ---------------------------------------------------------------------------------------------- |
| range:  | `sd:NamedGraph` (§3.3.11)           |

#### 3.2.19 sd:name

Relates a named graph to the name by which it may be referenced in a FROM/FROM NAMED clause. The object of the sd:name property is an IRI.

| domain: | `sd:NamedGraph` (§3.3.11) |
| ------- | ------------------------------------------------------------------------------------ |

#### 3.2.20 sd:graph

Relates a named graph to its graph description.

| domain: | `sd:NamedGraph` (§3.3.11) |
| ------- | ------------------------------------------------------------------------------------ |
| range:  | `sd:Graph` (§3.3.10)           |

### 3.3 Classes

#### 3.3.1 sd:Service

An instance of `sd:Service` (§3.3.1) represents a SPARQL service made available via the SPARQL Protocol.

| type: | `rdfs:Class` |
| ----- | ------------ |

#### 3.3.2 sd:Feature

An instance of `sd:Feature` (§3.3.2) represents a feature of a SPARQL service. Specific types of features include functions (§3.3.4), aggregates (§3.3.5), languages (§3.3.3), and entailment regimes (§3.3.6) and profiles (§3.3.7).
This document defines five instances of `sd:Feature` (§3.3.2): `sd:DereferencesURIs` (§3.4.6), `sd:UnionDefaultGraph` (§3.4.7), `sd:RequiresDataset` (§3.4.8), `sd:EmptyGraphs` (§3.4.9),
and `sd:BasicFederatedQuery` (§3.4.10).

| type: | `rdfs:Class` |
| ----- | ------------ |

#### 3.3.3 sd:Language

An instance of `sd:Language` (§3.3.3) represents one of the SPARQL languages (Query or Update).
The combination of a `sd:Language` with a version indicates a specific service configuration providing particular features or extensions.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The previous version of this specification [SPARQL11-SERVICE-DESCRIPTION] defined `sd:Language` as indicating both a language *and a version*.
> This has been changed so that `sd:Language` now only represents languages. A service's supported versions of the language is now specified using the `sd:supportedVersion` (§3.2.11) property.
> The previously-defined `sd:Language` §3.4 Instances which include a version number are preserved below for backwards compatibility.

This document defines five instances of `sd:Language` (§3.3.3): `sd:SPARQL10Query` (§3.4.1), `sd:SPARQL11Query` (§3.4.2), `sd:SPARQL11Update` (§3.4.3), `sd:SPARQLQuery` (§3.4.4), and `sd:SPARQLUpdate` (§3.4.5).

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.4 sd:Function

An instance of `sd:Function` (§3.3.4) represents a function that may be used in a SPARQL [SELECT expression](https://www.w3.org/TR/sparql12-query/#selectExpressions) or a [FILTER](https://www.w3.org/TR/sparql12-query/#expressions), [HAVING](https://www.w3.org/TR/sparql12-query/#having), [GROUP BY](https://www.w3.org/TR/sparql12-query/#groupby), [ORDER BY](https://www.w3.org/TR/sparql12-query/#modOrderBy), or [BIND](https://www.w3.org/TR/sparql12-query/#bind) clause.

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.5 sd:Aggregate

An instance of `sd:Aggregate` (§3.3.5) represents an aggregate that may be used in a SPARQL aggregate query (for instance in a [HAVING](https://www.w3.org/TR/sparql12-query/#having) clause or [SELECT expression](https://www.w3.org/TR/sparql12-query/#selectExpressions)) besides the standard list of [supported aggregates](https://www.w3.org/TR/sparql12-query/#aggregates) COUNT, SUM, MIN, MAX, AVG, GROUP_CONCAT, and SAMPLE.

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.6 sd:EntailmentRegime

An instance of `sd:EntailmentRegime` (§3.3.6) represents an entailment regime used in basic graph pattern matching (as described by [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql11-query/#sparqlBGPExtend)). URIs for commonly used entailment regimes are defined by [Unique URIs for Semantic Web Entailment Regimes](https://www.w3.org/ns/entailment/).

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.7 sd:EntailmentProfile

An instance of `sd:EntailmentProfile` (§3.3.7) represents a profile of an entailment regime. An entailment profile *MAY* impose restrictions on what constitutes valid RDF with respect to entailment. URIs for commonly used entailment profiles are defined by [Unique URIs for OWL 2 Profiles](https://www.w3.org/ns/owl-profile/).

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.8 sd:GraphCollection

An instance of `sd:GraphCollection` (§3.3.8) represents a collection of zero or more named graph descriptions. Each named graph description belonging
to an `sd:GraphCollection` (§3.3.8) *MUST* be linked with the `sd:namedGraph` (§3.2.18) predicate.

| type: | `rdfs:Class` |
| ----- | ------------ |

#### 3.3.9 sd:Dataset

An instance of `sd:Dataset` (§3.3.9) represents a [RDF Dataset](https://www.w3.org/TR/sparql12-query/#rdfDataset) comprised of a default graph and
zero or more named graphs.

The default graph of an `sd:Dataset` (§3.3.9) *MUST* be linked with the `sd:defaultGraph` (§3.2.17) predicate.

| type:       | `rdfs:Class`                                                                                   |
| ----------- | ---------------------------------------------------------------------------------------------- |
| subClassOf: | `sd:GraphCollection` (§3.3.8) |

#### 3.3.10 sd:Graph

An instance of `sd:Graph` (§3.3.10) represents the description of an RDF graph.

This document does not define properties with domain `sd:Graph` (§3.3.10). Instead, such instances may be described using other appropriate vocabularies (see example below (§4)).

| type: | `rdfs:Class` |
| ----- | ------------ |

#### 3.3.11 sd:NamedGraph

An instance of `sd:NamedGraph` (§3.3.11) represents a named graph having a name (via `sd:name` (§3.2.19)) and an optional graph
description (via `sd:graph` (§3.2.20)).

| type: | `rdfs:Class` |
| ----- | ------------ |

### 3.4 Instances

#### 3.4.1 sd:SPARQL10Query

`sd:SPARQL10Query` is an `sd:Language` (§3.3.3) representing the [SPARQL 1.0 Query Language](https://www.w3.org/TR/rdf-sparql-query/#).

| type: | `sd:Language` (§3.3.3) |
| ----- | -------------------------------------------------------------------------------- |

#### 3.4.2 sd:SPARQL11Query

`sd:SPARQL11Query` is an `sd:Language` (§3.3.3) representing the [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/).

| type: | `sd:Language` (§3.3.3) |
| ----- | -------------------------------------------------------------------------------- |

#### 3.4.3 sd:SPARQL11Update

`sd:SPARQL11Update` is an `sd:Language` (§3.3.3) representing the [SPARQL 1.1 Update](https://www.w3.org/TR/sparql11-update/) language.

| type: | `sd:Language` (§3.3.3) |
| ----- | -------------------------------------------------------------------------------- |

#### 3.4.4 sd:SPARQLQuery

`sd:SPARQLQuery` is an `sd:Language` (§3.3.3) representing the SPARQL Query language [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/).

Relevant supported versions (§3.2.11) are:

- `sparql:version-1.2`
- `sparql:version-1.2-basic`
- `sparql:version-1.1`
- `sparql:version-1.0`

| type: | `sd:Language` (§3.3.3) |
| ----- | -------------------------------------------------------------------------------- |

#### 3.4.5 sd:SPARQLUpdate

`sd:SPARQLUpdate` is an `sd:Language` (§3.3.3) representing the SPARQL Update langauge [SPARQL 1.2 Update](https://www.w3.org/TR/sparql12-update/) language.

Relevant supported versions (§3.2.11) are:

- `sparql:version-1.2`
- `sparql:version-1.2-basic`
- `sparql:version-1.1`
- `sparql:version-1.0`

| type: | `sd:Language` (§3.3.3) |
| ----- | -------------------------------------------------------------------------------- |

#### 3.4.6 sd:DereferencesURIs

`sd:DereferencesURIs`, when used as the object of the §3.2.2 sd:feature property, indicates that a SPARQL service will [dereference](https://www.w3.org/TR/webarch/#uri-dereference) [WEBARCH] URIs used in [FROM/FROM NAMED](https://www.w3.org/TR/sparql12-query/#specifyingDataset) and [USING/USING NAMED](https://www.w3.org/TR/sparql12-update/#defUSING) clauses and use the resulting RDF in the dataset during query evaluation.

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.7 sd:UnionDefaultGraph

`sd:UnionDefaultGraph`, when used as the object of the §3.2.2 sd:feature property, indicates that the default graph of the dataset used during query and
update evaluation (when an explicit dataset is not specified) is comprised of the union of all the named graphs in that dataset.

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.8 sd:RequiresDataset

`sd:RequiresDataset`, when used as the object of the §3.2.2 sd:feature property, indicates that the SPARQL service requires an explicit dataset declaration
(based on either [FROM/FROM NAMED](https://www.w3.org/TR/sparql12-query/#specifyingDataset) clauses in a query, [USING/USING NAMED](https://www.w3.org/TR/sparql12-update/#defUSING) clauses in an update, or the [appropriate SPARQL Protocol parameters](https://www.w3.org/TR/sparql12-protocol/#dataset)).

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.9 sd:EmptyGraphs

`sd:EmptyGraphs`, when used as the object of the §3.2.2 sd:feature property, indicates that the underlying graph store supports empty graphs. A graph store
that supports empty graphs *MUST NOT* remove graphs that are left empty after triples are removed from them. (See [3.1 Graph Update in SPARQL 1.2 Update](https://www.w3.org/TR/sparql12-update/#graphUpdate).)

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.10 sd:BasicFederatedQuery

`sd:BasicFederatedQuery`, when used as the object of the §3.2.2 sd:feature property, indicates that the SPARQL service supports basic federated query using
the [SERVICE keyword](https://www.w3.org/TR/sparql12-federated-query/#service) as defined by [SPARQL 1.2 Federated Query](https://www.w3.org/TR/sparql12-federated-query/).

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.11 Other Instances

Apart from the instances listed above, custom extensions and other documents may define further instance URIs usable within service descriptions; the following documents also list
instance URIs that may be used with some of the properties defined in the previous sections:

- [Unique URIs for Semantic Web Entailment Regimes](https://www.w3.org/ns/entailment/) (members of the class `sd:EntailmentRegime` (§3.3.6) usable with the properties `sd:defaultEntailmentRegime` (§3.2.3) and `sd:entailmentRegime` (§3.2.4))
- [Unique URIs for OWL 2 Profiles](https://www.w3.org/ns/owl-profile/) (members of the class `sd:EntailmentProfile` (§3.3.7) usable with the properties `sd:defaultSupportedEntailmentProfile` (§3.2.5) and `sd:supportedEntailmentProfile` (§3.2.6))
- [Unique URIs for File Formats](https://www.w3.org/ns/formats/) (members of the class `<http://www.w3.org/ns/formats/Format>` usable with the properties `sd:resultFormat` (§3.2.15) and `sd:inputFormat` (§3.2.16))

## 4. Example (Informative)

The following HTTP traces illustrate the retrieval of a service description from the SPARQL endpoint `http://www.example/sparql/`.

This RDF describes a SPARQL service available at the URL `http://www.example/sparql/` that supports the SPARQL 1.2 Query language. The service will dereference URLs used in
FROM/FROM NAMED clauses, supports both the RDF/XML and Turtle serialization formats, supports the `http://example.org/Distance` extension function, and has a dataset with a default
graph and one named graph, both described using the voiD vocabulary [VOID]. The default graph contains 100 triples and supports RDFS entailment while the graph named
http://www.example/named-graph contains 2000 triples and supports OWL2 RL entailment.

### 4.1 RDF/XML Service Description

Given the HTTP request:

```
GET /sparql/ HTTP/1.1
Host: www.example
```

the SPARQL service responds with an RDF/XML encoded service description (no content negotiation or RDFa encoding is used):

```
HTTP/1.1 200 OK
Date: Fri, 09 Oct 2009 17:31:12 GMT
Server: Apache/1.3.29 (Unix) PHP/4.3.4 DAV/1.0.3
Connection: close
Content-Type: application/rdf+xml

<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:sd="http://www.w3.org/ns/sparql-service-description#"
   xmlns:prof="http://www.w3.org/ns/owl-profile/"
   xmlns:void="http://rdfs.org/ns/void#">
  <sd:Service>
    <sd:endpoint rdf:resource="http://www.example/sparql/"/>
    <sd:supportedLanguage rdf:resource="http://www.w3.org/ns/sparql-service-description#SPARQLQuery"/>
    <sd:supportedVersion rdf:resource="http://www.w3.org/ns/sparql#version-1.2"/>
    <sd:supportedVersion rdf:resource="http://www.w3.org/ns/sparql#version-1.2-basic"/>
    <sd:resultFormat rdf:resource="http://www.w3.org/ns/formats/RDF_XML"/>
    <sd:resultFormat rdf:resource="http://www.w3.org/ns/formats/Turtle"/>
    <sd:feature rdf:resource="http://www.w3.org/ns/sparql-service-description#DereferencesURIs"/>
    <sd:defaultEntailmentRegime rdf:resource="http://www.w3.org/ns/entailment/RDFS"/>
    <sd:extensionFunction>
      <sd:Function rdf:about="http://example.org/Distance"/>
    </sd:extensionFunction>
    <sd:defaultDataset>
      <sd:Dataset>
        <sd:defaultGraph>
          <sd:Graph>
            <void:triples rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">100</void:triples>
          </sd:Graph>
        </sd:defaultGraph>
        <sd:namedGraph>
          <sd:NamedGraph>
            <sd:name rdf:resource="http://www.example/named-graph"/>
            <sd:entailmentRegime rdf:resource="http://www.w3.org/ns/entailment/OWL-RDF-Based"/>
            <sd:supportedEntailmentProfile rdf:resource="http://www.w3.org/ns/owl-profile/RL"/>
            <sd:graph>
              <sd:Graph>
                <void:triples rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2000</void:triples>
              </sd:Graph>
            </sd:graph>
          </sd:NamedGraph>
        </sd:namedGraph>
      </sd:Dataset>
    </sd:defaultDataset>
  </sd:Service>
</rdf:RDF>
```

### 4.2 Turtle Service Description

Given the HTTP request:

```
GET /sparql/ HTTP/1.1
Host: www.example
Accept: text/turtle
```

the SPARQL service responds with a [Turtle](https://www.w3.org/TR/rdf12-turtle/#) encoded service description:

```
HTTP/1.1 200 OK
Date: Fri, 09 Oct 2009 17:31:12 GMT
Server: Apache/1.3.29 (Unix) PHP/4.3.4 DAV/1.0.3
Connection: close
Content-Type: text/turtle

PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
PREFIX ent: <http://www.w3.org/ns/entailment/>
PREFIX prof: <http://www.w3.org/ns/owl-profile/>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX sparql: <http://www.w3.org/ns/sparql#>

[] a sd:Service ;
    sd:endpoint <http://www.example/sparql/> ;
    sd:supportedLanguage sd:SPARQLQuery ;
    sd:supportedVersion sparql:version-1.2, sparql:version-1.2-basic ;
    sd:resultFormat <http://www.w3.org/ns/formats/RDF_XML>, <http://www.w3.org/ns/formats/Turtle> ;
    sd:extensionFunction <http://example.org/Distance> ;
    sd:feature sd:DereferencesURIs ;
    sd:defaultEntailmentRegime ent:RDFS ;
    sd:defaultDataset [
        a sd:Dataset ;
        sd:defaultGraph [
            a sd:Graph ;
            void:triples 100
        ] ;
        sd:namedGraph [
            a sd:NamedGraph ;
            sd:name <http://www.example/named-graph> ;
            sd:entailmentRegime ent:OWL-RDF-Based ;
            sd:supportedEntailmentProfile prof:RL ;
            sd:graph [
                a sd:Graph ;
                void:triples 2000
            ]
        ]
    ] .

<http://example.org/Distance> a sd:Function .
```

## 5. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, *SHOULD*, and *SHOULD NOT* in this document
are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all
capitals, as shown here.

### 5.1 Conformance

A SPARQL service conformant with this specification:

1. *MUST* return RDF content when the service endpoint URL is accessed as described in section 2 Accessing a Service Description (§2).

2. The RDF content returned from dereferencing a service endpoint URL `<service-endpoint-URL>` *MUST* include at
   least one triple matching:

   ```
   ?service sd:endpoint <service-endpoint-URL> .
   ```

3. The RDF content returned *MUST* make use of the vocabulary defined in this document in accordance with the usage specified in
   section 3 Service Description Vocabulary (§3).

## A. Changes between SPARQL 1.1 Service Description and SPARQL 1.2 Service Description

*This section is non-normative.*

- sd:Language and sd:supportedLanguage updated to only differentiate Query and Update, leaving language versioning to the new sd:supportedVersion.
- Update fragment identifiers for references to RFC9110 in 2. Accessing a Service Description (§2)
- Use PREFIX instead of @prefix in all Turtle examples

## B. Privacy Considerations

TODO

## C. Security Considerations

TODO

## D. Internationalization Considerations

TODO

## E. Index

### E.1 Terms defined by this specification

### E.2 Terms defined by reference

- [RDF12-CONCEPTS] defines the following:
  * RDF 1.2 Basic conformance
- [RDF12-TURTLE] defines the following:
  * Turtle
- [RFC9110] defines the following:
  * content negotiation
- [SPARQL-QUERY] defines the following:
  * SPARQL 1.0 Query Language
- [SPARQL12-ENTAILMENT] defines the following:
  * SPARQL 1.2 Entailment Regimes
- [SPARQL12-FEDERATED-QUERY] defines the following:
  * SERVICE keyword
- [SPARQL12-PROTOCOL] defines the following:
  * appropriate SPARQL Protocol parameters
  * SPARQL Protocol service
- [SPARQL12-QUERY] defines the following:
  * BIND
  * FILTER
  * FROM/FROM NAMED
  * GROUP BY
  * HAVING
  * ORDER BY
  * RDF Dataset
  * SELECT expression
  * supported aggregates
- [SPARQL12-UPDATE] defines the following:
  * 3.1 Graph Update in SPARQL 1.2 Update
  * LOAD statement
  * USING/USING NAMED
- [WEBARCH] defines the following:
  * dereference

## F. References

### F.1 Normative references

[RDF12-CONCEPTS]

[RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/). Andy Seaborne; Gregg Kellogg; Olaf Hartig; Pierre-Antoine Champin. W3C. 7 April 2026. W3C Candidate Recommendation. URL: <https://www.w3.org/TR/rdf12-concepts/>

[RDF12-TURTLE]

[RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/). Gregg Kellogg; Dominik Tomaszuk. W3C. 21 April 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-turtle/>

[RDFa-core]

[RDFa Core 1.1 - Third Edition](https://www.w3.org/TR/rdfa-core/). Ben Adida; Mark Birbeck; Shane McCarron; Ivan Herman et al. W3C. 17 March 2015. W3C Recommendation. URL: <https://www.w3.org/TR/rdfa-core/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

[rfc9110]

[HTTP Semantics](https://httpwg.org/specs/rfc9110.html). R. Fielding, Ed.; M. Nottingham, Ed.; J. Reschke, Ed. IETF. June 2022. Internet Standard. URL: <https://httpwg.org/specs/rfc9110.html>

[SPARQL-QUERY]

[SPARQL Query Language for RDF](https://www.w3.org/TR/rdf-sparql-query/). Eric Prud'hommeaux; Andy Seaborne. W3C. 15 January 2008. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-sparql-query/>

[SPARQL11-QUERY]

[SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/). Steven Harris; Andy Seaborne. W3C. 21 March 2013. W3C Recommendation. URL: <https://www.w3.org/TR/sparql11-query/>

[SPARQL11-UPDATE]

[SPARQL 1.1 Update](https://www.w3.org/TR/sparql11-update/). Paula Gearon; Alexandre Passant; Axel Polleres. W3C. 21 March 2013. W3C Recommendation. URL: <https://www.w3.org/TR/sparql11-update/>

[SPARQL12-ENTAILMENT]

[SPARQL 1.2 Entailment Regimes](https://www.w3.org/TR/sparql12-entailment/). Peter Patel-Schneider. W3C. 9 April 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-entailment/>

[SPARQL12-FEDERATED-QUERY]

[SPARQL 1.2 Federated Query](https://www.w3.org/TR/sparql12-federated-query/). Ruben Taelman; Gregory Williams. W3C. 26 January 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-federated-query/>

[SPARQL12-PROTOCOL]

[SPARQL 1.2 Protocol](https://www.w3.org/TR/sparql12-protocol/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 14 August 2025. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-protocol/>

[SPARQL12-QUERY]

[SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/). Olaf Hartig; Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 16 April 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-query/>

[SPARQL12-UPDATE]

[SPARQL 1.2 Update](https://www.w3.org/TR/sparql12-update/). Ruben Taelman; Andy Seaborne; Thomas Pellissier Tanon. W3C. 14 August 2025. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-update/>

[VOID]

[Describing Linked Datasets with the VoID Vocabulary](https://www.w3.org/TR/void/). Keith Alexander; Richard Cyganiak; Michael Hausenblas; Jun Zhao. W3C. 3 March 2011. W3C Working Group Note. URL: <https://www.w3.org/TR/void/>

[WEBARCH]

[Architecture of the World Wide Web, Volume One](https://www.w3.org/TR/webarch/). Ian Jacobs; Norman Walsh. W3C. 15 December 2004. W3C Recommendation. URL: <https://www.w3.org/TR/webarch/>

### F.2 Informative references

[SPARQL11-SERVICE-DESCRIPTION]

[SPARQL 1.1 Service Description](https://www.w3.org/TR/sparql11-service-description/). Gregory Williams. W3C. 21 March 2013. W3C Recommendation. URL: <https://www.w3.org/TR/sparql11-service-description/>

[SPARQL12-CONCEPTS]

[SPARQL 1.2 Concepts](https://w3c.github.io/sparql-concepts/spec/). The W3C RDF & SPARQL Working Group. W3C. W3C Editor's Draft. URL: <https://w3c.github.io/sparql-concepts/spec/>

[SPARQL12-GRAPH-STORE-PROTOCOL]

[SPARQL 1.2 Graph Store Protocol](https://www.w3.org/TR/sparql12-graph-store-protocol/). Andy Seaborne; Thomas Pellissier Tanon. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-graph-store-protocol/>

[SPARQL12-NEW]

[What’s New in SPARQL 1.2](https://w3c.github.io/sparql-new/spec/). The W3C RDF & SPARQL Working Group. W3C. W3C Editor's Draft. URL: <https://w3c.github.io/sparql-new/spec/>

[SPARQL12-RESULTS-CSV-TSV]

[SPARQL 1.2 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql12-results-csv-tsv/). Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 28 March 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-csv-tsv/>

[SPARQL12-RESULTS-JSON]

[SPARQL 1.2 Query Results JSON Format](https://www.w3.org/TR/sparql12-results-json/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 28 March 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-json/>

[SPARQL12-RESULTS-XML]

[SPARQL 1.2 Query Results XML Format](https://www.w3.org/TR/sparql12-results-xml/). Ruben Taelman; Dominik Tomaszuk; Thomas Pellissier Tanon. W3C. 27 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-xml/>

Permalink

**Referenced in:**

- § 3.2.11 sd:supportedVersion

Permalink

**Referenced in:**

- § 4.2 Turtle Service Description

Permalink

**Referenced in:**

- § 2. Accessing a Service Description

Permalink

**Referenced in:**

- § 3.4.1 sd:SPARQL10Query

Permalink

**Referenced in:**

- § 3.2.5 sd:defaultSupportedEntailmentProfile

Permalink

**Referenced in:**

- § 3.4.10 sd:BasicFederatedQuery

Permalink

**Referenced in:**

- § 3.4.8 sd:RequiresDataset

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.1 sd:endpoint

Permalink

**Referenced in:**

- § 3.2.7 sd:extensionFunction
- § 3.3.4 sd:Function

Permalink

**Referenced in:**

- § 3.2.7 sd:extensionFunction
- § 3.3.4 sd:Function

Permalink

**Referenced in:**

- § 3.4.6 sd:DereferencesURIs
- § 3.4.8 sd:RequiresDataset

Permalink

**Referenced in:**

- § 3.2.7 sd:extensionFunction
- § 3.3.4 sd:Function

Permalink

**Referenced in:**

- § 3.2.7 sd:extensionFunction
- § 3.2.8 sd:extensionAggregate
- § 3.3.4 sd:Function
- § 3.3.5 sd:Aggregate

Permalink

**Referenced in:**

- § 3.2.7 sd:extensionFunction
- § 3.3.4 sd:Function

Permalink

**Referenced in:**

- § 3.3.9 sd:Dataset

Permalink

**Referenced in:**

- § 3.2.7 sd:extensionFunction
- § 3.2.8 sd:extensionAggregate
- § 3.3.4 sd:Function
- § 3.3.5 sd:Aggregate

Permalink

**Referenced in:**

- § 3.2.8 sd:extensionAggregate
- § 3.3.5 sd:Aggregate

Permalink

**Referenced in:**

- § 3.4.9 sd:EmptyGraphs

Permalink

**Referenced in:**

- § 3.2.16 sd:inputFormat

Permalink

**Referenced in:**

- § 3.4.6 sd:DereferencesURIs
- § 3.4.8 sd:RequiresDataset

Permalink

**Referenced in:**

- § 3.4.6 sd:DereferencesURIs
