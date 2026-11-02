---
title: "SPARQL 1.2 Service Description"
source: https://www.w3.org/TR/sparql12-service-description/
family: sparql
version: "1.2"
status: W3C Working Draft
spec_date: 2026-10-29
fetched: 2026-11-02
---

# SPARQL 1.2 Service Description

> Describing SPARQL services with RDF.

## Contents

- Abstract
- 1 Introduction
  - 1.1 Terminology
- 2 Namespaces
- 3 Accessing a Service Description
- 4 Service Description Vocabulary
  - 4.1 SPARQL Service Description Namespace and OWL Ontology
  - 4.2 Properties
    - 4.2.1 sd:endpoint
    - 4.2.2 sd:feature
    - 4.2.3 sd:defaultEntailmentRegime
    - 4.2.4 sd:entailmentRegime
    - 4.2.5 sd:defaultSupportedEntailmentProfile
    - 4.2.6 sd:supportedEntailmentProfile
    - 4.2.7 sd:extensionFunction
    - 4.2.8 sd:extensionAggregate
    - 4.2.9 sd:languageExtension
    - 4.2.10 sd:supportedLanguage
    - 4.2.11 sd:supportedVersion
    - 4.2.12 sd:propertyFeature
    - 4.2.13 sd:defaultDataset
    - 4.2.14 sd:availableGraphs
    - 4.2.15 sd:resultFormat
    - 4.2.16 sd:inputFormat
    - 4.2.17 sd:defaultGraph
    - 4.2.18 sd:namedGraph
    - 4.2.19 sd:name
    - 4.2.20 sd:graph
  - 4.3 Classes
    - 4.3.1 sd:Service
    - 4.3.2 sd:Feature
    - 4.3.3 sd:Language
    - 4.3.4 sd:Function
    - 4.3.5 sd:Aggregate
    - 4.3.6 sd:EntailmentRegime
    - 4.3.7 sd:EntailmentProfile
    - 4.3.8 sd:GraphCollection
    - 4.3.9 sd:Dataset
    - 4.3.10 sd:Graph
    - 4.3.11 sd:NamedGraph
  - 4.4 Instances
    - 4.4.1 sd:SPARQL10Query
    - 4.4.2 sd:SPARQL11Query
    - 4.4.3 sd:SPARQL11Update
    - 4.4.4 sd:SPARQLQuery
    - 4.4.5 sd:SPARQLUpdate
    - 4.4.6 sd:DereferencesURIs
    - 4.4.7 sd:UnionDefaultGraph
    - 4.4.8 sd:RequiresDataset
    - 4.4.9 sd:EmptyGraphs
    - 4.4.10 sd:BasicFederatedQuery
    - 4.4.11 Other Instances
- 5 Example (Informative)
  - 5.1 RDF/XML Service Description
  - 5.2 Turtle Service Description
- 6 Conformance
  - 6.1 Conformance
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

## 2. Namespaces

This specification makes use of the following namespaces:

`format`

`http://www.w3.org/ns/formats/`

`owl`

`http://www.w3.org/2002/07/owl#`

`rdfs`

`http://www.w3.org/2000/01/rdf-schema#`

`sd`

`http://www.w3.org/ns/sparql-service-description#`

`sparql`

`http://www.w3.org/ns/sparql#`

## 3. Accessing a Service Description

SPARQL services made available via the SPARQL Protocol *SHOULD* return a service description document at the service endpoint when
dereferenced using the HTTP GET operation without any query parameter strings provided. This service description *MUST* be made
available in an RDF serialization, *MAY* be embedded in (X)HTML by way of [RDFa Core 1.1 - Third Edition](https://www.w3.org/TR/rdfa-core/), and *SHOULD* use [content negotiation](https://httpwg.org/specs/rfc9110.html#content.negotiation) if available in other RDF representations.

## 4. Service Description Vocabulary

### 4.1 SPARQL Service Description Namespace and OWL Ontology

The SPARQL service description namespace IRI is:

[http://www.w3.org/ns/sparql-service-description#](https://www.w3.org/ns/sparql-service-description#)

The prefix used in this document for this namespace is `sd`.

An RDF encoding of the Service Description ontology is available by HTTP content negotiation from the [namespace IRI](https://www.w3.org/ns/sparql-service-description#).

### 4.2 Properties

#### 4.2.1 `sd:endpoint`

`sd:endpoint` is an `owl:InverseFunctionalProperty` that relates an instance of `sd:Service` (§4.3.1) to a SPARQL endpoint that implements the [SPARQL Protocol service](https://www.w3.org/TR/sparql12-protocol/#terminology) for the service. The object of the `sd:endpoint` property is an IRI.

The `rdfs:domain` of `sd:endpoint` is `sd:Service` (§4.3.1).

#### 4.2.2 `sd:feature`

`sd:feature` relates an instance of `sd:Service` (§4.3.1) with a resource representing a supported feature.

The `rdfs:domain` of `sd:feature` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:feature` is `sd:Feature` (§4.3.2).

#### 4.2.3 `sd:defaultEntailmentRegime`

`sd:defaultEntailmentRegime` relates an instance of `sd:Service` (§4.3.1) with a resource representing an entailment regime used for basic graph pattern matching. This property is
intended for use when a single entailment regime by default applies to all graphs in the default dataset of the service. In situations where a different entailment regime applies to a
specific graph in the dataset, the `sd:entailmentRegime` (§4.2.4) property should be used to indicate this fact in the description of that graph.

`sd:defaultEntailmentRegime` is a `rdfs:subPropertyOf` of `sd:feature` (§4.2.2).
The `rdfs:domain` of `sd:defaultEntailmentRegime` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:defaultEntailmentRegime` is `sd:EntailmentRegime` (§4.3.6).

#### 4.2.4 `sd:entailmentRegime`

`sd:entailmentRegime` relates a named graph description with a resource representing an entailment regime used for basic graph pattern matching over that graph.

The `rdfs:domain` of `sd:entailmentRegime` is `sd:NamedGraph` (§4.3.11).
The `rdfs:range` of `sd:entailmentRegime` is `sd:EntailmentRegime` (§4.3.6).

#### 4.2.5 `sd:defaultSupportedEntailmentProfile`

`sd:defaultSupportedEntailmentProfile` relates an instance of `sd:Service` (§4.3.1) with a resource representing a supported profile of the default entailment regime (as declared by `sd:defaultEntailmentRegime` (§4.2.3)). Entailment profiles are discussed more in [SPARQL 1.2 Entailment Regimes](https://www.w3.org/TR/sparql12-entailment/#OWL2ProfilesDS) [SPARQL12-ENTAILMENT].

Note that this specification does not make any conformance requirements on the compatibility of an advertised entailment profile with the advertised entailment regime in a service
description. Providing a reasonable combination of values to the §4.2.4 sd:entailmentRegime/§4.2.3 sd:defaultEntailmentRegime and §4.2.6 sd:supportedEntailmentProfile/§4.2.5 sd:defaultSupportedEntailmentProfile properties is up to
the creator of a service description.

`sd:defaultSupportedEntailmentProfile` is a `rdfs:subPropertyOf` of `sd:feature` (§4.2.2).
The `rdfs:domain` of `sd:defaultSupportedEntailmentProfile` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:defaultSupportedEntailmentProfile` is `sd:EntailmentProfile` (§4.3.7).

#### 4.2.6 `sd:supportedEntailmentProfile`

`sd:supportedEntailmentProfile` relates a named graph description with a resource representing a supported profile of the entailment regime (as declared by `sd:entailmentRegime` (§4.2.4)) used for basic graph pattern matching over that graph.

The `rdfs:domain` of `sd:supportedEntailmentProfile` is `sd:NamedGraph` (§4.3.11).
The `rdfs:range` of `sd:supportedEntailmentProfile` is `sd:EntailmentProfile` (§4.3.7).

#### 4.2.7 `sd:extensionFunction`

`sd:extensionFunction` relates an instance of `sd:Service` (§4.3.1) to a function that may be used in a SPARQL [SELECT expression](https://www.w3.org/TR/sparql12-query/#selectExpressions) or a [FILTER](https://www.w3.org/TR/sparql12-query/#expressions), [HAVING](https://www.w3.org/TR/sparql12-query/#having), [GROUP BY](https://www.w3.org/TR/sparql12-query/#groupby), [ORDER BY](https://www.w3.org/TR/sparql12-query/#modOrderBy), or [BIND](https://www.w3.org/TR/sparql12-query/#bind) clause.

`sd:extensionFunction` is a `rdfs:subPropertyOf` of `sd:feature` (§4.2.2).
The `rdfs:domain` of `sd:extensionFunction` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:extensionFunction` is `sd:Function` (§4.3.4).

#### 4.2.8 `sd:extensionAggregate`

`sd:extensionAggregate` relates an instance of `sd:Service` (§4.3.1) to an aggregate that may be used in a SPARQL aggregate query (for instance in a [HAVING](https://www.w3.org/TR/sparql12-query/#having) clause or [SELECT expression](https://www.w3.org/TR/sparql12-query/#selectExpressions)) besides the standard list of [supported aggregates](https://www.w3.org/TR/sparql12-query/#aggregates) COUNT, SUM, MIN, MAX, AVG, GROUP_CONCAT, and SAMPLE.

`sd:extensionAggregate` is a `rdfs:subPropertyOf` of `sd:feature` (§4.2.2).
The `rdfs:domain` of `sd:extensionAggregate` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:extensionAggregate` is `sd:Aggregate` (§4.3.5).

#### 4.2.9 `sd:languageExtension`

`sd:languageExtension` relates an instance of `sd:Service` (§4.3.1) to a resource representing an implemented extension to the SPARQL Query or Update language.

`sd:languageExtension` is a `rdfs:subPropertyOf` of `sd:feature` (§4.2.2).
The `rdfs:domain` of `sd:languageExtension` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:languageExtension` is `sd:Feature` (§4.3.2).

#### 4.2.10 `sd:supportedLanguage`

`sd:supportedLanguage` relates an instance of `sd:Service` (§4.3.1) to a SPARQL language (e.g. Query and Update) that it implements.

`sd:supportedLanguage` is a `rdfs:subPropertyOf` of `sd:feature` (§4.2.2).
The `rdfs:domain` of `sd:supportedLanguage` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:supportedLanguage` is `sd:Language` (§4.3.3).

#### 4.2.11 `sd:supportedVersion`

`sd:supportedVersion` relates an instance of `sd:Service` (§4.3.1) to a SPARQL language version that it supports.

This property is related to the `sd:supportedLanguage` property, as the combination of language and version will indicate a specific feature set supported by the service.
For example, when a service description indicates support for the `sd:SPARQLQuery` language and [`sparql:version-1.2-basic`](https://www.w3.org/ns/sparql#version-1.2-basic) version, support for SPARQL 1.2 Query [SPARQL12-QUERY] with [RDF 1.2 Basic conformance](https://www.w3.org/TR/rdf12-concepts/#dfn-basic) is indicated.

`sd:supportedVersion` is a `rdfs:subPropertyOf` of `sd:feature` (§4.2.2).
The `rdfs:domain` of `sd:supportedVersion` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:supportedVersion` is `rdfs:Resource`.

#### 4.2.12 `sd:propertyFeature`

`sd:propertyFeature` relates an instance of `sd:Service` (§4.3.1) to a resource representing an implemented feature that extends the SPARQL Query or Update language and that is
accessed by using the named property.

`sd:propertyFeature` is a `rdfs:subPropertyOf` of `sd:feature` (§4.2.2).
The `rdfs:domain` of `sd:propertyFeature` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:propertyFeature` is `sd:Feature` (§4.3.2).

#### 4.2.13 `sd:defaultDataset`

`sd:defaultDataset` is an instance of `owl:InverseFunctionalProperty` that
relates an instance of `sd:Service` (§4.3.1) to a description of the
default dataset available when no explicit dataset is specified in the query, update request, or
via protocol parameters.

The `rdfs:domain` of `sd:defaultDataset` is `sd:Service`.
The `rdfs:range` of `sd:defaultDataset` is `sd:Dataset`.

#### 4.2.14 `sd:availableGraphs`

`sd:availableGraphs` relates an instance of `sd:Service` (§4.3.1) to a description of the graphs which are allowed in the construction of a dataset via the SPARQL Protocol, with
FROM/FROM NAMED clauses in a query, or with USING/USING NAMED in an update request, if the service limits the scope of dataset construction.

The `rdfs:domain` of `sd:defaultDataset` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:defaultDataset` is `sd:GraphCollection` (§4.3.8).

#### 4.2.15 `sd:resultFormat`

`sd:resultFormat` relates an instance of `sd:Service` (§4.3.1) to a format that is supported for serializing query results.

URIs for commonly used serialization formats are defined by [Unique URIs for File Formats](https://www.w3.org/ns/formats/). For formats that do not have an
existing URI, the `<http://www.w3.org/ns/formats/media_type>` and `<http://www.w3.org/ns/formats/preferred_suffix>` properties defined in that document *SHOULD* be used to describe the format.

The `rdfs:domain` of `sd:resultFormat` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:resultFormat` is `format:Format`.

#### 4.2.16 `sd:inputFormat`

`sd:inputFormat` relates an instance of `sd:Service` (§4.3.1) to a format that is supported for parsing RDF input; for example, via a SPARQL 1.2 Update [LOAD statement](https://www.w3.org/TR/sparql12-update/#load), or when URIs are dereferenced in FROM/FROM NAMED/USING/USING NAMED clauses (see also §4.4.6 sd:DereferencesURIs below).

URIs for commonly used serialization formats are defined by [Unique URIs for File Formats](https://www.w3.org/ns/formats/). For formats that do not have an
existing URI, the `<http://www.w3.org/ns/formats/media_type>` and `<http://www.w3.org/ns/formats/preferred_suffix>` properties defined in that document *SHOULD* be used to describe the format.

The `rdfs:domain` of `sd:inputFormat` is `sd:Service` (§4.3.1).
The `rdfs:range` of `sd:inputFormat` is `format:Format`.

#### 4.2.17 `sd:defaultGraph`

`sd:defaultGraph` relates an instance of `sd:Dataset` (§4.3.9) to the description of its default graph.

The `rdfs:domain` of `sd:defaultGraph` is `sd:Dataset` (§4.3.9).
The `rdfs:range` of `sd:defaultGraph` is `sd:Graph` (§4.3.10).

#### 4.2.18 `sd:namedGraph`

`sd:namedGraph` relates an instance of `sd:GraphCollection` (§4.3.8) (or its subclass `sd:Dataset` (§4.3.9)) to the description of one of
its named graphs. The description of such a named graph *MUST* include the `sd:name` (§4.2.19) property
and *MAY* include the `sd:graph` (§4.2.20) property.

The `rdfs:domain` of `sd:namedGraph` is `sd:GraphCollection` (§4.3.8).
The `rdfs:range` of `sd:namedGraph` is `sd:NamedGraph` (§4.3.11).

#### 4.2.19 `sd:name`

`sd:name` relates a named graph to the name by which it may be referenced in a FROM/FROM NAMED clause. The object of the sd:name property is an IRI.

The `rdfs:domain` of `sd:name` is `sd:NamedGraph` (§4.3.11).

#### 4.2.20 `sd:graph`

`sd:graph` relates a named graph to its graph description.

The `rdfs:domain` of `sd:graph` is `sd:NamedGraph` (§4.3.11).
The `rdfs:range` of `sd:graph` is `sd:Graph` (§4.3.10).

### 4.3 Classes

#### 4.3.1 `sd:Service`

`sd:Service` is the `rdfs:Class` of SPARQL services made available via the SPARQL Protocol.

#### 4.3.2 `sd:Feature`

`sd:Feature` is the `rdfs:Class` of features of a SPARQL service. Specific types of features include functions (§4.3.4), aggregates (§4.3.5), languages (§4.3.3), and entailment regimes (§4.3.6) and profiles (§4.3.7).
This document defines five instances of `sd:Feature` (§4.3.2): `sd:DereferencesURIs` (§4.4.6), `sd:UnionDefaultGraph` (§4.4.7), `sd:RequiresDataset` (§4.4.8), `sd:EmptyGraphs` (§4.4.9),
and `sd:BasicFederatedQuery` (§4.4.10).

#### 4.3.3 `sd:Language`

`sd:Language` is the `rdfs:Class` of the SPARQL languages (Query or Update).
The combination of a `sd:Language` with a version indicates a specific service configuration providing particular features or extensions.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The previous version of this specification [SPARQL11-SERVICE-DESCRIPTION] defined `sd:Language` as indicating both a language *and a version*.
> This has been changed so that `sd:Language` now only represents languages. A service's supported versions of the language is now specified using the `sd:supportedVersion` (§4.2.11) property.
> The previously-defined `sd:Language` §4.4 Instances which include a version number are preserved below for backwards compatibility.

This document defines five instances of `sd:Language` (§4.3.3): `sd:SPARQL10Query` (§4.4.1), `sd:SPARQL11Query` (§4.4.2), `sd:SPARQL11Update` (§4.4.3), `sd:SPARQLQuery` (§4.4.4), and `sd:SPARQLUpdate` (§4.4.5).

`sd:Language` is a `rdfs:subClassOf` of `sd:Feature` (§4.3.2).

#### 4.3.4 `sd:Function`

`sd:Function` is the `rdfs:Class` of functions that may be used in a SPARQL [SELECT expression](https://www.w3.org/TR/sparql12-query/#selectExpressions) or a [FILTER](https://www.w3.org/TR/sparql12-query/#expressions), [HAVING](https://www.w3.org/TR/sparql12-query/#having), [GROUP BY](https://www.w3.org/TR/sparql12-query/#groupby), [ORDER BY](https://www.w3.org/TR/sparql12-query/#modOrderBy), or [BIND](https://www.w3.org/TR/sparql12-query/#bind) clause.

`sd:Function` is a `rdfs:subClassOf` of `sd:Feature` (§4.3.2).

#### 4.3.5 `sd:Aggregate`

`sd:Aggregate` is the `rdfs:Class` aggregates that may be used in a SPARQL aggregate query (for instance in a [HAVING](https://www.w3.org/TR/sparql12-query/#having) clause or [SELECT expression](https://www.w3.org/TR/sparql12-query/#selectExpressions)) besides the standard list of [supported aggregates](https://www.w3.org/TR/sparql12-query/#aggregates) COUNT, SUM, MIN, MAX, AVG, GROUP_CONCAT, and SAMPLE.

`sd:Aggregate` is a `rdfs:subClassOf` of `sd:Feature` (§4.3.2).

#### 4.3.6 `sd:EntailmentRegime`

`sd:EntailmentRegime` is the `rdfs:Class` of entailment regimes used in basic graph pattern matching (as described by [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql11-query/#sparqlBGPExtend)). URIs for commonly used entailment regimes are defined by [Unique URIs for Semantic Web Entailment Regimes](https://www.w3.org/ns/entailment/).

`sd:EntailmentRegime` is a `rdfs:subClassOf` of `sd:Feature` (§4.3.2).

#### 4.3.7 `sd:EntailmentProfile`

`sd:EntailmentProfile` is the `rdfs:Class` of profiles of an entailment regime. An entailment profile *MAY* impose restrictions on what constitutes valid RDF with respect to entailment. URIs for commonly used entailment profiles are defined by [Unique URIs for OWL 2 Profiles](https://www.w3.org/ns/owl-profile/).

`sd:EntailmentProfile` is a `rdfs:subClassOf` of `sd:Feature` (§4.3.2).

#### 4.3.8 `sd:GraphCollection`

`sd:GraphCollection` is the `rdfs:Class` of collections of zero or more named graph descriptions. Each named graph description belonging
to an `sd:GraphCollection` (§4.3.8) *MUST* be linked with the `sd:namedGraph` (§4.2.18) predicate.

#### 4.3.9 `sd:Dataset`

`sd:Dataset` is the `rdfs:Class` of [RDF Datasets](https://www.w3.org/TR/sparql12-query/#rdfDataset), comprised of a default graph and
zero or more named graphs.

The default graph of an `sd:Dataset` (§4.3.9) *MUST* be linked with the `sd:defaultGraph` (§4.2.17) predicate.

`sd:Dataset` is a `rdfs:subClassOf` of `sd:GraphCollection` (§4.3.8).

#### 4.3.10 `sd:Graph`

`sd:Graph` is the `rdfs:Class` of RDF graphs.

This document does not define properties with domain `sd:Graph` (§4.3.10). Instead, such instances may be described using other appropriate vocabularies (see example below (§5)).

#### 4.3.11 `sd:NamedGraph`

`sd:NamedGraph` is the `rdfs:Class` of graphs having a name in a `sd:Dataset` (via `sd:name` (§4.2.19)) and an optional graph
description (via `sd:graph` (§4.2.20)).

### 4.4 Instances

#### 4.4.1 `sd:SPARQL10Query`

`sd:SPARQL10Query` is a `sd:Language` (§4.3.3) representing the [SPARQL 1.0 Query Language](https://www.w3.org/TR/rdf-sparql-query/#).

#### 4.4.2 `sd:SPARQL11Query`

`sd:SPARQL11Query` is a `sd:Language` (§4.3.3) representing the [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/).

#### 4.4.3 `sd:SPARQL11Update`

`sd:SPARQL11Update` is a `sd:Language` (§4.3.3) representing the [SPARQL 1.1 Update](https://www.w3.org/TR/sparql11-update/) language.

#### 4.4.4 `sd:SPARQLQuery`

`sd:SPARQLQuery` is a `sd:Language` (§4.3.3) representing the SPARQL Query language [SPARQL12-QUERY].

Relevant supported versions (§4.2.11) are:

- `sparql:version-1.2`
- `sparql:version-1.2-basic`
- `sparql:version-1.1`
- `sparql:version-1.0`

#### 4.4.5 `sd:SPARQLUpdate`

`sd:SPARQLUpdate` is a `sd:Language` (§4.3.3) representing the SPARQL Update langauge [SPARQL12-UPDATE].

Relevant supported versions (§4.2.11) are:

- `sparql:version-1.2`
- `sparql:version-1.2-basic`
- `sparql:version-1.1`
- `sparql:version-1.0`

#### 4.4.6 `sd:DereferencesURIs`

`sd:DereferencesURIs` is a `sd:Feature` (§4.3.2) which, when used as the object of the §4.2.2 sd:feature property, indicates that a SPARQL service will [dereference](https://www.w3.org/TR/webarch/#uri-dereference) [WEBARCH] URIs used in [FROM/FROM NAMED](https://www.w3.org/TR/sparql12-query/#specifyingDataset) and [USING/USING NAMED](https://www.w3.org/TR/sparql12-update/#defUSING) clauses and use the resulting RDF in the dataset during query evaluation.

#### 4.4.7 `sd:UnionDefaultGraph`

`sd:UnionDefaultGraph` is a `sd:Feature` (§4.3.2) which, when used as the object of the §4.2.2 sd:feature property, indicates that the default graph of the dataset used during query and
update evaluation (when an explicit dataset is not specified) is comprised of the union of all the named graphs in that dataset.

#### 4.4.8 `sd:RequiresDataset`

`sd:RequiresDataset` is a `sd:Feature` (§4.3.2) which, when used as the object of the §4.2.2 sd:feature property, indicates that the SPARQL service requires an explicit dataset declaration
(based on either [FROM/FROM NAMED](https://www.w3.org/TR/sparql12-query/#specifyingDataset) clauses in a query, [USING/USING NAMED](https://www.w3.org/TR/sparql12-update/#defUSING) clauses in an update, or the [appropriate SPARQL Protocol parameters](https://www.w3.org/TR/sparql12-protocol/#dataset)).

#### 4.4.9 `sd:EmptyGraphs`

`sd:EmptyGraphs` is a `sd:Feature` (§4.3.2) which, when used as the object of the §4.2.2 sd:feature property, indicates that the underlying graph store supports empty graphs. A graph store
that supports empty graphs *MUST NOT* remove graphs that are left empty after triples are removed from them. (See [3.1 Graph Update in SPARQL 1.2 Update](https://www.w3.org/TR/sparql12-update/#graphUpdate).)

#### 4.4.10 `sd:BasicFederatedQuery`

`sd:BasicFederatedQuery` is a `sd:Feature` (§4.3.2) which, when used as the object of the §4.2.2 sd:feature property, indicates that the SPARQL service supports basic federated query using
the [SERVICE keyword](https://www.w3.org/TR/sparql12-federated-query/#service) as defined by [SPARQL 1.2 Federated Query](https://www.w3.org/TR/sparql12-federated-query/).

#### 4.4.11 Other Instances

Apart from the instances listed above, custom extensions and other documents may define further instance URIs usable within service descriptions; the following documents also list
instance URIs that may be used with some of the properties defined in the previous sections:

- [Unique URIs for Semantic Web Entailment Regimes](https://www.w3.org/ns/entailment/) (members of the class `sd:EntailmentRegime` (§4.3.6) usable with the properties `sd:defaultEntailmentRegime` (§4.2.3) and `sd:entailmentRegime` (§4.2.4))
- [Unique URIs for OWL 2 Profiles](https://www.w3.org/ns/owl-profile/) (members of the class `sd:EntailmentProfile` (§4.3.7) usable with the properties `sd:defaultSupportedEntailmentProfile` (§4.2.5) and `sd:supportedEntailmentProfile` (§4.2.6))
- [Unique URIs for File Formats](https://www.w3.org/ns/formats/) (members of the class `format:Format` usable with the properties `sd:resultFormat` (§4.2.15) and `sd:inputFormat` (§4.2.16))

## 5. Example (Informative)

The following HTTP traces illustrate the retrieval of a service description from the SPARQL endpoint `http://www.example/sparql/`.

This RDF describes a SPARQL service available at the URL `http://www.example/sparql/` that supports the SPARQL 1.2 Query language. The service will dereference URLs used in
FROM/FROM NAMED clauses, supports both the RDF/XML and Turtle serialization formats, supports the `http://example.org/Distance` extension function, and has a dataset with a default
graph and one named graph, both described using the voiD vocabulary [VOID]. The default graph contains 100 triples and supports RDFS entailment while the graph named
http://www.example/named-graph contains 2000 triples and supports OWL2 RL entailment.

### 5.1 RDF/XML Service Description

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

### 5.2 Turtle Service Description

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

## 6. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, *SHOULD*, and *SHOULD NOT* in this document
are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all
capitals, as shown here.

### 6.1 Conformance

A SPARQL service conformant with this specification:

1. *MUST* return RDF content when the service endpoint URL is accessed as described in section 2 Accessing a Service Description (§3).

2. The RDF content returned from dereferencing a service endpoint URL `<service-endpoint-URL>` *MUST* include at
   least one triple matching:

   ```
   ?service sd:endpoint <service-endpoint-URL> .
   ```

3. The RDF content returned *MUST* make use of the vocabulary defined in this document in accordance with the usage specified in
   section 3 Service Description Vocabulary (§4).

## A. Changes between SPARQL 1.1 Service Description and SPARQL 1.2 Service Description

*This section is non-normative.*

- sd:Language and sd:supportedLanguage updated to only differentiate Query and Update, leaving language versioning to the new sd:supportedVersion.
- Update fragment identifiers for references to RFC9110 in 3. Accessing a Service Description (§3)
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
  * RDF Datasets
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

[RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/). Gregg Kellogg; Andy Seaborne; Dominik Tomaszuk. W3C. 23 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-turtle/>

[RDFa-core]

[RDFa Core 1.1 - Third Edition](https://www.w3.org/TR/rdfa-core/). Ben Adida; Mark Birbeck; Shane McCarron; Ivan Herman et al. W3C. 17 March 2015. W3C Recommendation. URL: <https://www.w3.org/TR/rdfa-core/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/info/rfc2119/). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc2119/>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/info/rfc8174/). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc8174/>

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

[SPARQL 1.2 Federated Query](https://www.w3.org/TR/sparql12-federated-query/). Ruben Taelman; Gregory Williams. W3C. 23 April 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-federated-query/>

[SPARQL12-PROTOCOL]

[SPARQL 1.2 Protocol](https://www.w3.org/TR/sparql12-protocol/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 23 July 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-protocol/>

[SPARQL12-QUERY]

[SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/). Olaf Hartig; Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 25 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-query/>

[SPARQL12-UPDATE]

[SPARQL 1.2 Update](https://www.w3.org/TR/sparql12-update/). Ruben Taelman; Andy Seaborne; Thomas Pellissier Tanon. W3C. 25 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-update/>

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

[SPARQL 1.2 Graph Store Protocol](https://www.w3.org/TR/sparql12-graph-store-protocol/). Andy Seaborne; Thomas Pellissier Tanon. W3C. 24 September 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-graph-store-protocol/>

[SPARQL12-NEW]

[What’s New in SPARQL 1.2](https://w3c.github.io/sparql-new/spec/). The W3C RDF & SPARQL Working Group. W3C. W3C Editor's Draft. URL: <https://w3c.github.io/sparql-new/spec/>

[SPARQL12-RESULTS-CSV-TSV]

[SPARQL 1.2 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql12-results-csv-tsv/). Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 22 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-csv-tsv/>

[SPARQL12-RESULTS-JSON]

[SPARQL 1.2 Query Results JSON Format](https://www.w3.org/TR/sparql12-results-json/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 13 August 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-json/>

[SPARQL12-RESULTS-XML]

[SPARQL 1.2 Query Results XML Format](https://www.w3.org/TR/sparql12-results-xml/). Ruben Taelman; Dominik Tomaszuk; Thomas Pellissier Tanon. W3C. 27 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-xml/>

Permalink

**Referenced in:**

- § 4.2.11 sd:supportedVersion

Permalink

**Referenced in:**

- § 5.2 Turtle Service Description

Permalink

**Referenced in:**

- § 3. Accessing a Service Description

Permalink

**Referenced in:**

- § 4.4.1 sd:SPARQL10Query

Permalink

**Referenced in:**

- § 4.2.5 sd:defaultSupportedEntailmentProfile

Permalink

**Referenced in:**

- § 4.4.10 sd:BasicFederatedQuery

Permalink

**Referenced in:**

- § 4.4.8 sd:RequiresDataset

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 4.2.1 sd:endpoint

Permalink

**Referenced in:**

- § 4.2.7 sd:extensionFunction
- § 4.3.4 sd:Function

Permalink

**Referenced in:**

- § 4.2.7 sd:extensionFunction
- § 4.3.4 sd:Function

Permalink

**Referenced in:**

- § 4.4.6 sd:DereferencesURIs
- § 4.4.8 sd:RequiresDataset

Permalink

**Referenced in:**

- § 4.2.7 sd:extensionFunction
- § 4.3.4 sd:Function

Permalink

**Referenced in:**

- § 4.2.7 sd:extensionFunction
- § 4.2.8 sd:extensionAggregate
- § 4.3.4 sd:Function
- § 4.3.5 sd:Aggregate

Permalink

**Referenced in:**

- § 4.2.7 sd:extensionFunction
- § 4.3.4 sd:Function

Permalink

**Referenced in:**

- § 4.3.9 sd:Dataset

Permalink

**Referenced in:**

- § 4.2.7 sd:extensionFunction
- § 4.2.8 sd:extensionAggregate
- § 4.3.4 sd:Function
- § 4.3.5 sd:Aggregate

Permalink

**Referenced in:**

- § 4.2.8 sd:extensionAggregate
- § 4.3.5 sd:Aggregate

Permalink

**Referenced in:**

- § 4.4.9 sd:EmptyGraphs

Permalink

**Referenced in:**

- § 4.2.16 sd:inputFormat

Permalink

**Referenced in:**

- § 4.4.6 sd:DereferencesURIs
- § 4.4.8 sd:RequiresDataset

Permalink

**Referenced in:**

- § 4.4.6 sd:DereferencesURIs
