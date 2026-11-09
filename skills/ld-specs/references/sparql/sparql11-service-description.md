---
title: "SPARQL 1.1 Service Description"
source: https://www.w3.org/TR/sparql11-service-description/
family: sparql
version: "1.1"
status: W3C Recommendation
spec_date: 2013-03-21
fetched: 2026-11-09
---

# SPARQL 1.1 Service Description

> Service descriptions (1.1 Recommendation).

## Contents

- Abstract
    - 1 May Be Superseded
    - 2 Set of Documents
    - No Substantive Changes
    - Please Send Comments
    - Endorsed By W3C
    - 3 Patents
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
    - 3.2.11 sd:propertyFeature
    - 3.2.12 sd:defaultDataset
    - 3.2.13 sd:availableGraphs
    - 3.2.14 sd:resultFormat
    - 3.2.15 sd:inputFormat
    - 3.2.16 sd:defaultGraph
    - 3.2.17 sd:namedGraph
    - 3.2.18 sd:name
    - 3.2.19 sd:graph
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
    - 3.4.4 sd:DereferencesURIs
    - 3.4.5 sd:UnionDefaultGraph
    - 3.4.6 sd:RequiresDataset
    - 3.4.7 sd:EmptyGraphs
    - 3.4.8 sd:BasicFederatedQuery
    - 3.4.9 Other Instances
- 4 Example (Informative)
  - 4.1 RDF/XML Service Description
  - 4.2 Turtle Service Description
- 5 Conformance
- A References
  - A.1 Normative References
  - A.2 Other References
- Change Log
  - Changes since Proposed Recommendation
  - Changes since Last Call

---

---

## Abstract

This document describes SPARQL service description, a method for
discovering, and vocabulary for describing SPARQL services made available
via the [SPARQL 1.1 Protocol for RDF](https://www.w3.org/TR/sparql11-protocol/) [SPROT]. These descriptions
provide a mechanism by which a client or end user can discover
information about the SPARQL service such as supported
extension functions and details about the available dataset.

#### May Be Superseded

*This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at http://www.w3.org/TR/.*

#### Set of Documents

This document is one of eleven SPARQL 1.1 Recommendations produced by the [SPARQL Working Group](https://www.w3.org/2001/sw/DataAccess/):

1. [SPARQL 1.1 Overview](https://www.w3.org/TR/2013/REC-sparql11-overview-20130321)
2. [SPARQL 1.1 Query Language](https://www.w3.org/TR/2013/REC-sparql11-query-20130321)
3. [SPARQL 1.1 Update](https://www.w3.org/TR/2013/REC-sparql11-update-20130321)
4. [SPARQL1.1 Service Description](https://www.w3.org/TR/2013/REC-sparql11-service-description-20130321) (this document)
5. [SPARQL 1.1 Federated Query](https://www.w3.org/TR/2013/REC-sparql11-federated-query-20130321)
6. [SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/2013/REC-sparql11-results-json-20130321)
7. [SPARQL 1.1 Query Results CSV and TSV Formats](https://www.w3.org/TR/2013/REC-sparql11-results-csv-tsv-20130321)
8. [SPARQL Query Results XML Format (Second Edition)](https://www.w3.org/TR/2013/REC-rdf-sparql-XMLres-20130321)
9. [SPARQL 1.1 Entailment Regimes](https://www.w3.org/TR/2013/REC-sparql11-entailment-20130321)
10. [SPARQL 1.1 Protocol](https://www.w3.org/TR/2013/REC-sparql11-protocol-20130321)
11. [SPARQL 1.1 Graph Store HTTP Protocol](https://www.w3.org/TR/2013/REC-sparql11-http-rdf-update-20130321)

#### No Substantive Changes

There have been no substantive changes to this document since the [previous version](https://www.w3.org/TR/2012/PR-sparql11-service-description-20121108/). Minor editorial changes, if any, are detailed in the change log and visible in the [color-coded diff](https://www.w3.org/TR/sparql11-service-description/diff).

#### Please Send Comments

Please send any comments to <public-rdf-dawg-comments@w3.org> ([public archive](http://lists.w3.org/Archives/Public/public-rdf-dawg-comments/)). Although work on this document by the [SPARQL Working Group](https://www.w3.org/2009/sparql/) is complete, comments may be addressed in the [errata](https://www.w3.org/2013/sparql-errata) or in future revisions. Open discussion is welcome at <public-sparql-dev@w3.org> ([public archive](http://lists.w3.org/Archives/Public/public-sparql-dev/)).

#### Endorsed By W3C

*This document has been reviewed by W3C Members, by software developers, and by other W3C groups and interested parties, and is endorsed by the Director as a W3C Recommendation. It is a stable document and may be used as reference material or cited from another document. W3C's role in making the Recommendation is to draw attention to the specification and to promote its widespread deployment. This enhances the functionality and interoperability of the Web.*

#### Patents

*This document was produced by a group operating under the [5 February 2004 W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy-20040205/). W3C maintains a [public list of any patent disclosures](https://www.w3.org/2004/01/pp-impl/35463/status) made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains [Essential Claim(s)](https://www.w3.org/Consortium/Patent-Policy-20040205/#def-essential) must disclose the information in accordance with [section 6 of the W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy-20040205/#sec-Disclosure).*

---

## 1 Introduction

A SPARQL service description lists the features of a SPARQL service made available via the [SPARQL 1.1 Protocol for RDF](https://www.w3.org/TR/sparql11-protocol/) [SPROT]. This document describes both a method for discovering a service description from a specific SPARQL service and an RDF schema for encoding such descriptions in RDF.

### 1.1 Terminology

When this document uses the words *MUST*, *SHOULD* and *MAY*, and the words appear as emphasized text, they must be interpreted as described in [RFC2119].

The following terms are also in use throughout this document:

SPARQL Service

Any implementation conforming to the [SPARQL 1.1 Protocol for RDF](https://www.w3.org/TR/sparql11-service-description/) (this document's use of "SPARQL Service" is the same as "[SPARQL Protocol service](https://www.w3.org/TR/sparql11-protocol/#terminology)" as defined in the SPARQL 1.1 Protocol) [SPROT].

SPARQL endpoint

The URI at which a SPARQL Service listens for requests from clients.

## 2 Accessing a Service Description

SPARQL services made available via the SPARQL Protocol *SHOULD* return a service description document at the service endpoint when dereferenced using the HTTP GET operation without any query parameter strings provided. This service description *MUST* be made available in an RDF serialization, *MAY* be embedded in (X)HTML by way of [RDFa](https://www.w3.org/TR/rdfa-syntax/) [RDFA], and *SHOULD* use [content negotiation](https://www.w3.org/Protocols/rfc2616/rfc2616-sec12.html) [CONNEG] if available in other RDF representations.

## 3 Service Description Vocabulary

### 3.1 SPARQL Service Description Namespace and OWL Ontology

The SPARQL service description namespace IRI is:

[http://www.w3.org/ns/sparql-service-description#](https://www.w3.org/ns/sparql-service-description#)

The prefix used in this document for this namespace is `sd`.

An RDF encoding of the Service Description ontology is available by HTTP content negotiation from the [namespace IRI](https://www.w3.org/ns/sparql-service-description#).

### 3.2 Properties

#### 3.2.1 sd:endpoint

Relates an instance of `sd:Service` (§3.3.1) to a SPARQL endpoint that implements the [SPARQL Protocol service](https://www.w3.org/TR/sparql11-protocol/#terminology) [SPROT] for the service. The object of the sd:endpoint property is an IRI.

| type:   | `owl:InverseFunctionalProperty`                                                |
| ------- | ------------------------------------------------------------------------------ |
| domain: | `sd:Service` (§3.3.1) |

#### 3.2.2 sd:feature

Relates an instance of `sd:Service` (§3.3.1) with a resource representing a supported feature.

| domain: | `sd:Service` (§3.3.1) |
| ------- | ------------------------------------------------------------------------------ |
| range:  | `sd:Feature` (§3.3.2) |

#### 3.2.3 sd:defaultEntailmentRegime

Relates an instance of `sd:Service` (§3.3.1) with a resource representing an entailment regime used for basic graph pattern matching. This property is intended for use when a single entailment regime by default applies to all graphs in the default dataset of the service. In situations where a different entailment regime applies to a specific graph in the dataset, the `sd:entailmentRegime` (§3.2.4) property should be used to indicate this fact in the description of that graph.

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

Relates an instance of `sd:Service` (§3.3.1) with a resource representing a supported profile of the default entailment regime (as declared by `sd:defaultEntailmentRegime` (§3.2.3)). Entailment profiles are discussed more in [SPARQL 1.1 Entailment Regimes](https://www.w3.org/TR/sparql11-entailment/#OWL2ProfilesDS) [SPARQLENT].

Note that this specification does not make any conformance requirements on the compatibility of an advertised entailment profile with the advertised entailment regime in a service description. Providing a reasonable combination of values to the §3.2.4 sd:entailmentRegime/§3.2.3 sd:defaultEntailmentRegime and §3.2.6 sd:supportedEntailmentProfile/§3.2.5 sd:defaultSupportedEntailmentProfile properties is up to the creator of a service description.

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

Relates an instance of `sd:Service` (§3.3.1) to a function that may be used in a SPARQL [SELECT expression](https://www.w3.org/TR/sparql11-query/#selectExpressions) or a [FILTER](https://www.w3.org/TR/sparql11-query/#expressions), [HAVING](https://www.w3.org/TR/sparql11-query/#having), [GROUP BY](https://www.w3.org/TR/sparql11-query/#groupby), [ORDER BY](https://www.w3.org/TR/sparql11-query/#modOrderBy), or [BIND](https://www.w3.org/TR/sparql11-query/#bind) clause.

| subPropertyOf: | `sd:feature` (§3.2.2)   |
| -------------- | -------------------------------------------------------------------------------- |
| domain:        | `sd:Service` (§3.3.1)   |
| range:         | `sd:Function` (§3.3.4) |

#### 3.2.8 sd:extensionAggregate

Relates an instance of `sd:Service` (§3.3.1) to an aggregate that may be used in a SPARQL aggregate query (for instance in a [HAVING](https://www.w3.org/TR/sparql11-query/#having) clause or [SELECT expression](https://www.w3.org/TR/sparql11-query/#selectExpressions)) besides the standard list of [supported aggregates](https://www.w3.org/TR/sparql11-query/#aggregates) COUNT, SUM, MIN, MAX, AVG, GROUP_CONCAT, and SAMPLE.

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

#### 3.2.11 sd:propertyFeature

Relates an instance of `sd:Service` (§3.3.1) to a resource representing an implemented feature that extends the SPARQL Query or Update language and that is accessed by using the named property.

| subPropertyOf: | `sd:feature` (§3.2.2) |
| -------------- | ------------------------------------------------------------------------------ |
| domain:        | `sd:Service` (§3.3.1) |
| range:         | `sd:Feature` (§3.3.2) |

#### 3.2.12 sd:defaultDataset

Relates an instance of `sd:Service` (§3.3.1) to a description of the default dataset available when no explicit dataset is specified in the query, update request or via protocol parameters.

| type:   | `owl:InverseFunctionalProperty`                                                |
| ------- | ------------------------------------------------------------------------------ |
| domain: | `sd:Service` (§3.3.1) |
| range:  | `sd:Dataset` (§3.3.9) |

#### 3.2.13 sd:availableGraphs

Relates an instance of `sd:Service` (§3.3.1) to a description of the graphs which are allowed in the construction of a dataset via the SPARQL Protocol, with FROM/FROM NAMED clauses in a query, or with USING/USING NAMED in an update request, if the service limits the scope of dataset construction.

| domain: | `sd:Service` (§3.3.1)                 |
| ------- | ---------------------------------------------------------------------------------------------- |
| range:  | `sd:GraphCollection` (§3.3.8) |

#### 3.2.14 sd:resultFormat

Relates an instance of `sd:Service` (§3.3.1) to a format that is supported for serializing query results.

URIs for commonly used serialization formats are defined by [Unique URIs for File Formats](https://www.w3.org/ns/formats/). For formats that do not have an existing URI, the `<http://www.w3.org/ns/formats/media_type>` and `<http://www.w3.org/ns/formats/preferred_suffix>` properties defined in that document *SHOULD* be used to describe the format.

| domain: | `sd:Service` (§3.3.1) |
| ------- | ------------------------------------------------------------------------------ |
| range:  | `<http://www.w3.org/ns/formats/Format>`                                        |

#### 3.2.15 sd:inputFormat

Relates an instance of `sd:Service` (§3.3.1) to a format that is supported for parsing RDF input; for example, via a SPARQL 1.1 Update [LOAD statement](https://www.w3.org/TR/sparql11-update/#load), or when URIs are dereferenced in FROM/FROM NAMED/USING/USING NAMED clauses (see also §3.4.4 sd:DereferencesURIs below).

URIs for commonly used serialization formats are defined by [Unique URIs for File Formats](https://www.w3.org/ns/formats/). For formats that do not have an existing URI, the `<http://www.w3.org/ns/formats/media_type>` and `<http://www.w3.org/ns/formats/preferred_suffix>` properties defined in that document *SHOULD* be used to describe the format.

| domain: | `sd:Service` (§3.3.1) |
| ------- | ------------------------------------------------------------------------------ |
| range:  | `<http://www.w3.org/ns/formats/Format>`                                        |

#### 3.2.16 sd:defaultGraph

Relates an instance of `sd:Dataset` (§3.3.9) to the description of its default graph.

| domain: | `sd:Dataset` (§3.3.9) |
| ------- | ------------------------------------------------------------------------------ |
| range:  | `sd:Graph` (§3.3.10)     |

#### 3.2.17 sd:namedGraph

Relates an instance of `sd:GraphCollection` (§3.3.8) (or its subclass `sd:Dataset` (§3.3.9)) to the description of one of its named graphs. The description of such a named graph *MUST* include the `sd:name` (§3.2.18) property and *MAY* include the `sd:graph` (§3.2.19) property.

| domain: | `sd:GraphCollection` (§3.3.8) |
| ------- | ---------------------------------------------------------------------------------------------- |
| range:  | `sd:NamedGraph` (§3.3.11)           |

#### 3.2.18 sd:name

Relates a named graph to the name by which it may be referenced in a FROM/FROM NAMED clause. The object of the sd:name property is an IRI.

| domain: | `sd:NamedGraph` (§3.3.11) |
| ------- | ------------------------------------------------------------------------------------ |

#### 3.2.19 sd:graph

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

An instance of `sd:Feature` (§3.3.2) represents a feature of a SPARQL service. Specific types of features include functions (§3.3.4), aggregates (§3.3.5), languages (§3.3.3), and entailment regimes (§3.3.6) and profiles (§3.3.7). This document defines five instances of `sd:Feature` (§3.3.2): `sd:DereferencesURIs` (§3.4.4), `sd:UnionDefaultGraph` (§3.4.5), `sd:RequiresDataset` (§3.4.6), `sd:EmptyGraphs` (§3.4.7), and `sd:BasicFederatedQuery` (§3.4.8).

| type: | `rdfs:Class` |
| ----- | ------------ |

#### 3.3.3 sd:Language

An instance of `sd:Language` (§3.3.3) represents one of the SPARQL languages, including specific configurations providing particular features or extensions. This document defines three instances of `sd:Language` (§3.3.3): `sd:SPARQL10Query` (§3.4.1), `sd:SPARQL11Query` (§3.4.2), and `sd:SPARQL11Update` (§3.4.3).

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.4 sd:Function

An instance of `sd:Function` (§3.3.4) represents a function that may be used in a SPARQL [SELECT expression](https://www.w3.org/TR/sparql11-query/#selectExpressions) or a [FILTER](https://www.w3.org/TR/sparql11-query/#expressions), [HAVING](https://www.w3.org/TR/sparql11-query/#having), [GROUP BY](https://www.w3.org/TR/sparql11-query/#groupby), [ORDER BY](https://www.w3.org/TR/sparql11-query/#modOrderBy), or [BIND](https://www.w3.org/TR/sparql11-query/#bind) clause.

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.5 sd:Aggregate

An instance of `sd:Aggregate` (§3.3.5) represents an aggregate that may be used in a SPARQL aggregate query (for instance in a [HAVING](https://www.w3.org/TR/sparql11-query/#having) clause or [SELECT expression](https://www.w3.org/TR/sparql11-query/#selectExpressions)) besides the standard list of [supported aggregates](https://www.w3.org/TR/sparql11-query/#aggregates) COUNT, SUM, MIN, MAX, AVG, GROUP_CONCAT, and SAMPLE.

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.6 sd:EntailmentRegime

An instance of `sd:EntailmentRegime` (§3.3.6) represents an entailment regime used in basic graph pattern matching (as described by [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/#sparqlBGPExtend)). URIs for commonly used entailment regimes are defined by [Unique URIs for Semantic Web Entailment Regimes](https://www.w3.org/ns/entailment/) [ENTAILMENT].

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.7 sd:EntailmentProfile

An instance of `sd:EntailmentProfile` (§3.3.7) represents a profile of an entailment regime. An entailment profile *MAY* impose restrictions on what constitutes valid RDF with respect to entailment. URIs for commonly used entailment profiles are defined by [Unique URIs for OWL 2 Profiles](https://www.w3.org/ns/owl-profile/) [OWL2PROF].

| type:       | `rdfs:Class`                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| subClassOf: | `sd:Feature` (§3.3.2) |

#### 3.3.8 sd:GraphCollection

An instance of `sd:GraphCollection` (§3.3.8) represents a collection of zero or more named graph descriptions. Each named graph description belonging to an `sd:GraphCollection` (§3.3.8) *MUST* be linked with the `sd:namedGraph` (§3.2.17) predicate.

| type: | `rdfs:Class` |
| ----- | ------------ |

#### 3.3.9 sd:Dataset

An instance of `sd:Dataset` (§3.3.9) represents a [RDF Dataset](https://www.w3.org/TR/sparql11-query/#rdfDataset) comprised of a default graph and zero or more named graphs.

The default graph of an `sd:Dataset` (§3.3.9) *MUST* be linked with the `sd:defaultGraph` (§3.2.16) predicate.

| type:       | `rdfs:Class`                                                                                   |
| ----------- | ---------------------------------------------------------------------------------------------- |
| subClassOf: | `sd:GraphCollection` (§3.3.8) |

#### 3.3.10 sd:Graph

An instance of `sd:Graph` (§3.3.10) represents the description of an RDF graph.

This document does not define properties with domain `sd:Graph` (§3.3.10). Instead, such instances may be described using other appropriate vocabularies (see example below (§4)).

| type: | `rdfs:Class` |
| ----- | ------------ |

#### 3.3.11 sd:NamedGraph

An instance of `sd:NamedGraph` (§3.3.11) represents a named graph having a name (via `sd:name` (§3.2.18)) and an optional graph description (via `sd:graph` (§3.2.19)).

| type: | `rdfs:Class` |
| ----- | ------------ |

### 3.4 Instances

#### 3.4.1 sd:SPARQL10Query

`sd:SPARQL10Query` is an `sd:Language` (§3.3.3) representing the [SPARQL 1.0 Query language](https://www.w3.org/TR/rdf-sparql-query/) [QUERY10].

| type: | `sd:Language` (§3.3.3) |
| ----- | -------------------------------------------------------------------------------- |

#### 3.4.2 sd:SPARQL11Query

`sd:SPARQL11Query` is an `sd:Language` (§3.3.3) representing the [SPARQL 1.1 Query language](https://www.w3.org/TR/sparql11-query/) [QUERY11].

| type: | `sd:Language` (§3.3.3) |
| ----- | -------------------------------------------------------------------------------- |

#### 3.4.3 sd:SPARQL11Update

`sd:SPARQLUpdate` is an `sd:Language` (§3.3.3) representing the [SPARQL 1.1 Update language](https://www.w3.org/TR/sparql11-update/) [UPDATE11].

| type: | `sd:Language` (§3.3.3) |
| ----- | -------------------------------------------------------------------------------- |

#### 3.4.4 sd:DereferencesURIs

`sd:DereferencesURIs`, when used as the object of the §3.2.2 sd:feature property, indicates that a SPARQL service will [dereference](https://www.w3.org/TR/webarch/#uri-dereference) [AWWW] URIs used in [FROM/FROM NAMED](https://www.w3.org/TR/sparql11-query/#specifyingDataset) and [USING/USING NAMED](https://www.w3.org/TR/sparql11-update/#defUSING) clauses and use the resulting RDF in the dataset during query evaluation.

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.5 sd:UnionDefaultGraph

`sd:UnionDefaultGraph`, when used as the object of the §3.2.2 sd:feature property, indicates that the default graph of the dataset used during query and update evaluation (when an explicit dataset is not specified) is comprised of the union of all the named graphs in that dataset.

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.6 sd:RequiresDataset

`sd:RequiresDataset`, when used as the object of the §3.2.2 sd:feature property, indicates that the SPARQL service requires an explicit dataset declaration (based on either [FROM/FROM NAMED](https://www.w3.org/TR/sparql11-query/#specifyingDataset) clauses in a query, [USING/USING NAMED](https://www.w3.org/TR/sparql11-update/#defUSING) clauses in an update, or the [appropriate SPARQL Protocol parameters](https://www.w3.org/TR/sparql11-protocol/#dataset)).

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.7 sd:EmptyGraphs

`sd:EmptyGraphs`, when used as the object of the §3.2.2 sd:feature property, indicates that the underlying graph store supports empty graphs. A graph store that supports empty graphs *MUST NOT* remove graphs that are left empty after triples are removed from them. (See [3.1 Graph Update in SPARQL 1.1 Update](https://www.w3.org/TR/sparql11-update/#graphUpdate).)

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.8 sd:BasicFederatedQuery

`sd:BasicFederatedQuery`, when used as the object of the §3.2.2 sd:feature property, indicates that the SPARQL service supports basic federated query using the [SERVICE keyword](https://www.w3.org/TR/sparql11-federated-query/#service) as defined by [SPARQL 1.1 Federation Extensions](https://www.w3.org/TR/sparql11-federated-query/) [SPARQLFED].

| type: | `sd:Feature` (§3.3.2) |
| ----- | ------------------------------------------------------------------------------ |

#### 3.4.9 Other Instances

Apart from the instances listed above, custom extensions and other documents may define further instance URIs usable within service descriptions; the following documents also list instance URIs that may be used with some of the properties defined in the previous sections:

- [Unique URIs for Semantic Web Entailment Regimes](https://www.w3.org/ns/entailment/) [ENTAILMENT] (members of the class `sd:EntailmentRegime` (§3.3.6) usable with the properties `sd:defaultEntailmentRegime` (§3.2.3) and `sd:entailmentRegime` (§3.2.4))
- [Unique URIs for OWL 2 Profiles](https://www.w3.org/ns/owl-profile/) [OWL2PROF] (members of the class `sd:EntailmentProfile` (§3.3.7) usable with the properties `sd:defaultSupportedEntailmentProfile` (§3.2.5) and `sd:supportedEntailmentProfile` (§3.2.6))
- [Unique URIs for File Formats](https://www.w3.org/ns/formats/) [FORMATS] (members of the class `<http://www.w3.org/ns/formats/Format>` usable with the properties `sd:resultFormat` (§3.2.14) and `sd:inputFormat` (§3.2.15))

## 4 Example (Informative)

The following HTTP traces illustrate the retrieval of a service description from the SPARQL endpoint `http://www.example/sparql/`.

This RDF describes a SPARQL service available at the URL `http://www.example/sparql/` that supports the SPARQL 1.1 Query language. The service will dereference URLs used in FROM/FROM NAMED clauses, supports both the RDF/XML and Turtle serialization formats, supports the `http://example.org/Distance` extension function, and has a dataset with a default graph and one named graph, both described using the voiD vocabulary [VOID]. The default graph contains 100 triples and supports RDFS entailment while the graph named http://www.example/named-graph contains 2000 triples and supports OWL2 RL entailment.

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
    <sd:supportedLanguage rdf:resource="http://www.w3.org/ns/sparql-service-description#SPARQL11Query"/>
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

the SPARQL service responds with a [Turtle](https://www.w3.org/TeamSubmission/turtle/) [TURTLE] encoded service description:

```
HTTP/1.1 200 OK
Date: Fri, 09 Oct 2009 17:31:12 GMT
Server: Apache/1.3.29 (Unix) PHP/4.3.4 DAV/1.0.3
Connection: close
Content-Type: text/turtle

@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .
@prefix ent: <http://www.w3.org/ns/entailment/> .
@prefix prof: <http://www.w3.org/ns/owl-profile/> .
@prefix void: <http://rdfs.org/ns/void#> .

[] a sd:Service ;
    sd:endpoint <http://www.example/sparql/> ;
    sd:supportedLanguage sd:SPARQL11Query ;
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

## 5 Conformance

A SPARQL service conformant with this specification:

1. *MUST* return RDF content when the service endpoint URL is accessed as described in section 2 Accessing a Service Description (§2).

2. The RDF content returned from dereferencing a service endpoint URL `<service-endpoint-URL>` *MUST* include at least one triple matching:

   ```
   ?service sd:endpoint <service-endpoint-URL> .
   ```

3. The RDF content returned *MUST* make use of the vocabulary defined in this document in accordance with the usage specified in section 3 Service Description Vocabulary (§3).

## A References

### A.1 Normative References

[CONNEG]

[Hypertext Transfer Protocol -- HTTP/1.1, Content Negotiation](https://www.w3.org/Protocols/rfc2616/rfc2616-sec12.html),
Fielding, et al., IETF. June 1999. This document is http://www.w3.org/Protocols/rfc2616/rfc2616-sec12.html .

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](http://www.ietf.org/rfc/rfc2119.txt),
S. Bradner, IETF. March 1997. This document is http://www.ietf.org/rfc/rfc2119.txt .

[QUERY10]

[SPARQL Query Language for RDF](https://www.w3.org/TR/rdf-sparql-query/), E. Prud'hommeaux and Andy Seaborne, Editors, W3C Recommendation, 15 January 2008. This document is http://www.w3.org/TR/rdf-sparql-query/ .

[QUERY11]

[SPARQL 1.1 Query Language](https://www.w3.org/TR/2013/REC-sparql11-query-20130321), S. Harris, A. Seaborne, Editors, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-query-20130321. [Latest version](https://www.w3.org/TR/sparql11-query/ "Latest version of SPARQL 1.1 Query Language") available at http://www.w3.org/TR/sparql11-query.

[SPROT]

[SPARQL 1.1 Protocol](https://www.w3.org/TR/2013/REC-sparql11-protocol-20130321), L. Feigenbaum, G. Williams, K. Clark, E. Torres, Editors, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-protocol-20130321. [Latest version](https://www.w3.org/TR/sparql11-protocol/ "Latest version of SPARQL 1.1 Protocol") available at http://www.w3.org/TR/sparql11-protocol.

[UPDATE11]

[SPARQL 1.1 Update](https://www.w3.org/TR/2013/REC-sparql11-update-20130321), P. Gearon, A. Passant, A. Polleres, Editors, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-update-20130321. [Latest version](https://www.w3.org/TR/sparql11-update/ "Latest version of SPARQL 1.1 Update") available at http://www.w3.org/TR/sparql11-update.

### A.2 Other References

[AWWW]

[Architecture of the World Wide Web, Volume One](https://www.w3.org/TR/webarch/), I. Jacobs and N. Walsh, Editors, W3C Recommendation, 15 December 2004. http://www.w3.org/TR/webarch/ .

[ENTAILMENT]

[Unique URIs for Semantic Web Entailment Regimes](https://www.w3.org/ns/entailment/)

[FORMATS]

[Unique URIs for File Formats](https://www.w3.org/ns/formats/)

[OWL2PROF]

[Unique URIs for OWL 2 Profiles](https://www.w3.org/ns/owl-profile/)

[RDFA]

[RDFa in XHTML: Syntax and Processing](https://www.w3.org/TR/rdfa-syntax/), B. Adida, M. Birbeck, S. McCarron, and S. Pemberton, Editors, W3C Recommendation, 14 October 2008. http://www.w3.org/TR/rdfa-syntax/ .

[SPARQLENT]

[SPARQL 1.1 Entailment Regimes](https://www.w3.org/TR/2013/REC-sparql11-entailment-20130321), B. Glimm, C. Ogbuji, Editors, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-entailment-20130321. [Latest version](https://www.w3.org/TR/sparql11-entailment/ "Latest version of SPARQL 1.1 Entailment Regimes") available at http://www.w3.org/TR/sparql11-entailment.

[SPARQLFED]

[SPARQL 1.1 Federated Query](https://www.w3.org/TR/2013/REC-sparql11-federated-query-20130321), E. Prud'hommeaux, C. Buil-Aranda, Editors, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-federated-query-20130321. [Latest version](https://www.w3.org/TR/sparql11-federated-query/ "Latest version of SPARQL 1.1 Federated Query") available at http://www.w3.org/TR/sparql11-federated-query.

[TURTLE]

[Turtle: Terse RDF Triple Language](https://www.w3.org/TR/2013/CR-turtle-20130219/), E Prud'hommeaux, G Carothers, Editors, W3C Candidate Recommendation, 19 February 2013, http://www.w3.org/TR/2013/CR-turtle-20130219/. [Latest version](https://www.w3.org/TR/turtle/ "Latest version of Turtle") available at http://www.w3.org/TR/turtle/.

[VOID]

[Describing Linked Datasets with the voiD Vocabulary](https://www.w3.org/TR/2011/NOTE-void-20110303/),
K. Alexander, R. Cyganiak, M. Hausenblas, and J. Zhao, Authors, W3C Interest Group Note, 3 March 2011, http://www.w3.org/TR/2011/NOTE-void-20110303/ . [Latest version](https://www.w3.org/TR/void/ "Latest version of Describing Linked Datasets with the voiD Vocabulary") available at http://www.w3.org/TR/void/ .

## Change Log

### Changes since Proposed Recommendation

- Changed example to remove unused namespace prefix

### Changes since Last Call

- Aligned terminology with Protocol document and improved wording regarding SD access
- Clarified usage of sd:availableGraphs based on comment
- Updated references; moved changelog; hid cvs log
