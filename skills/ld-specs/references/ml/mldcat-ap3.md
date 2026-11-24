---
title: "MLDCAT-AP"
source: https://semiceu.github.io/MLDCAT-AP/releases/3.1.0/
family: ml
version: "3.1.0"
spec_date: 2026-05-13
fetched: 2026-11-24
---

# MLDCAT-AP

> SEMIC DCAT-AP extension for ML models, datasets, tasks, runs, and evaluations.

## Contents

- Abstract
- 1 Introduction
- 2 Status
- 3 License
- 4 Terminology
  - 4.1 Used Prefixes
- 5 Overview
- 6 Main Entities
  - 6.1 Agent
  - 6.2 Algorithm
  - 6.3 Catalogue
  - 6.4 Dataset
  - 6.5 Distribution
  - 6.6 File
  - 6.7 Harm Risk
  - 6.8 Machine Learning Model
  - 6.9 Paper
  - 6.10 Quality Measurement
- 7 Supportive Entities
  - 7.1 Activity
  - 7.2 Benchmark
  - 7.3 Bibliographic Reference
  - 7.4 Catalogue Record
  - 7.5 Catalogued Resource
  - 7.6 Checksum
  - 7.7 Checksum Algorithm
  - 7.8 Collection
  - 7.9 Computer Infrastructure
  - 7.10 Concept
  - 7.11 Cost Matrix
  - 7.12 Data Quality
  - 7.13 Data Service
  - 7.14 Document
  - 7.15 Engagement
  - 7.16 Environmental Impact
  - 7.17 Estimation Procedure
  - 7.18 Evaluation
  - 7.19 Evaluation Measure
  - 7.20 Feature
  - 7.21 Flow
  - 7.22 Flow Parameter
  - 7.23 Hardware
  - 7.24 Image Object
  - 7.25 Library
  - 7.26 Licence Document
  - 7.27 Linguistic System
  - 7.28 Location
  - 7.29 Measure
  - 7.30 Media Type
  - 7.31 Media Type Or Extent
  - 7.32 Modality
  - 7.33 Output File Description
  - 7.34 Parameter
  - 7.35 Policy
  - 7.36 Prediction
  - 7.37 Prediction Feature
  - 7.38 Quality Measurement Dataset
  - 7.39 Repository
  - 7.40 Resource
  - 7.41 Rights Statement
  - 7.42 Run
  - 7.43 Run Collection
  - 7.44 Split
  - 7.45 Standard
  - 7.46 Task
  - 7.47 Task Collection
  - 7.48 Task Type
- 8 Datatypes
- 9 Examples
  - 9.1 Example Credit-g Dataset on OpenML
  - 9.2 Example Bloom-7b1 Machine Learning Model on HuggingFace
  - 9.3 Example Apertus Machine Learning Model on HuggingFace
  - 9.4 Example Thermal Bridges Machine Learning Model on EOSC
- 10 Controlled Vocabularies
  - 10.1 Requirements for controlled vocabularies
  - 10.2 Expected usage of controlled vocabularies
  - 10.3 Controlled vocabularies to be used
    - 10.3.1 Properties with controlled vocabularies that MUST be used for the listed properties
    - 10.3.2 Properties with AT LEAST 1 value from the controlled vocabularies
    - 10.3.3 Properties with a RECOMMENDED use of controlled vocabularies
    - 10.3.4 Properties with MAY use a controlled vocabularies
  - 10.4 Other controlled vocabularies
- 11 Usage Guidelines
- 12 Support for implementation
  - 12.1 JSON-LD context file
  - 12.2 Validation
  - 12.3 UML representation
- 13 Governance
  - 13.1 Versioning governance
  - 13.2 Governance requirements for re-used assets
  - 13.3 Lexicalisation rules
- 14 Mappings
- 15 Quick Reference of Classes and Properties

---

## Abstract

MLDCAT-AP aims to describe machine learning models, together with their datasets, quality measured on the datasets and citing papers. It has been originally developed in collaboration with [OpenML](https://www.openml.org/).

Over time, concepts coming from AI Act and AI Code of Practice (AI Cop) have been included and a reference to them has been added for each class or property where needed, including those references to existing data models.

## Introduction

MLDCAT-AP (Machine Learning DCAT-AP) is an Application Profile that extends DCAT-AP in the field of machine learning by adding concepts such as Machine Learning Model, Task, etc.

## Status

This Application Profile has the status SEMIC Candidate Recommendation published at 2026-05-13.

Information about the process and the decisions involved in the creation of this specification can be consulted at the [Changelog](https://github.com/SEMICeu/MLDCAT-AP/blob/main/releases/3.1.0/html/Changelog.md).

## License

Copyright © 2024 European Union. All material in this repository is published under the license CC-BY 4.0, unless explicitly otherwise mentioned.

## Terminology

An Application Profile is a data specification aimed to facilitate the data exchange in a well-defined application context. It re-uses concepts from one or more semantic data specifications, while adding more specificity, by identifying mandatory, recommended, and optional elements, addressing particular application needs, and providing recommendations for controlled vocabularies to be used.
More information can be found on the [SEMIC Style Guide](https://semiceu.github.io/style-guide/1.0.0/terminological-clarifications.html#sec:what-is-a-cv-specification).

### Used Prefixes

MLDCAT-AP is a semantic specification, where each class and property has an URI.

The prefixed form of the URI, can be found in part in the class diagram and in the quick reference table at the bottom, while, for ease of reading, full URI can be found in the hyperlink of each class and property.

This specification uses the following prefixes to shorten the URIs for readability:

| Prefix  | Namespace IRI                                 |
| ------- | --------------------------------------------- |
| `adms`  | `http://www.w3.org/ns/adms#`                  |
| `biro`  | `http://purl.org/spar/biro/`                  |
| `cv`    | `http://data.europa.eu/m8g/`                  |
| `dcat`  | `http://www.w3.org/ns/dcat#`                  |
| `dct`   | `http://purl.org/dc/terms/`                   |
| `dpv`   | `https://w3id.org/dpv#`                       |
| `dqv`   | `http://www.w3.org/ns/dqv#`                   |
| `foaf`  | `http://xmlns.com/foaf/0.1/`                  |
| `frapo` | `http://purl.org/cerif/frapo/`                |
| `it6`   | `http://data.europa.eu/it6/`                  |
| `lpwc`  | `https://linkedpaperswithcode.com/property/`  |
| `lpwcc` | `https://linkedpaperswithcode.com/class/`     |
| `mls`   | `http://www.w3.org/ns/mls#`                   |
| `mlso`  | `http://w3id.org/mlso/`                       |
| `odrl`  | `http://www.w3.org/ns/odrl/2/`                |
| `owl`   | `http://www.w3.org/2002/07/owl#`              |
| `prov`  | `http://www.w3.org/ns/prov#`                  |
| `qb`    | `http://purl.org/linked-data/cube#`           |
| `rdf`   | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs`  | `http://www.w3.org/2000/01/rdf-schema#`       |
| `skos`  | `http://www.w3.org/2004/02/skos/core#`        |
| `spdx`  | `http://spdx.org/rdf/terms#`                  |
| `xsd`   | `http://www.w3.org/2001/XMLSchema#`           |

## Overview

This document describes the usage of the following main entities for a correct usage of the Application Profile:
| §6.1 Agent | §6.2 Algorithm | §6.3 Catalogue | §6.4 Dataset | §6.5 Distribution | §6.6 File | §6.7 Harm Risk | §6.8 Machine Learning Model | §6.9 Paper | §6.10 Quality Measurement |

The main entities are supported by:
| §7.1 Activity | §7.2 Benchmark | §7.3 Bibliographic Reference | §7.4 Catalogue Record | §7.5 Catalogued Resource | §7.6 Checksum | §7.7 Checksum Algorithm | §7.8 Collection | §7.9 Computer Infrastructure | §7.10 Concept | §7.11 Cost Matrix | §7.12 Data Quality | §7.13 Data Service | §7.14 Document | §7.15 Engagement | §7.16 Environmental Impact | §7.17 Estimation Procedure | §7.18 Evaluation | §7.19 Evaluation Measure | §7.20 Feature | §7.21 Flow | §7.22 Flow Parameter | §7.23 Hardware | §7.24 Image Object | §7.25 Library | §7.26 Licence Document | §7.27 Linguistic System | §7.28 Location | §7.29 Measure | §7.30 Media Type | §7.31 Media Type Or Extent | §7.32 Modality | §7.33 Output File Description | §7.34 Parameter | §7.35 Policy | §7.36 Prediction | §7.37 Prediction Feature | §7.38 Quality Measurement Dataset | §7.39 Repository | §7.40 Resource | §7.41 Rights Statement | §7.42 Run | §7.43 Run Collection | §7.44 Split | §7.45 Standard | §7.46 Task | §7.47 Task Collection | §7.48 Task Type |

And supported by these datatypes:
| hexBinary | integer | Literal | nonNegativeInteger | Temporal Literal |

## Main Entities

The main entities are those that form the core of the Application Profile.
The properties and their associated constraints that apply in the context of this profile are listed in a tabular form.
Each row corresponds to one property.
In addition to the constraints also cross-references are provided to DCAT. To save space, the following abbreviations are used to indicate in short the difference with DCAT:

- A: reused as-is defined and expressed in DCAT [vocab-dcat-3]
- E: reused with additional usage notes or additional restrictions compared to DCAT [vocab-dcat-3]
- P: DCAT-AP profile specific extension where DCAT had no requirements earlier on specified

This reuse qualification assessment is with respect to a specific version of DCAT.
Therefore it may vary over time when new versions of DCAT-AP are created.

### [Agent](http://xmlns.com/foaf/0.1/Agent)

Definition

Any entity carrying out actions with respect to the entities Catalogue and the Catalogued Resources.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Agent)

Usage Note

If the Agent is an organisation, the use of the [Organisation Ontology](https://www.w3.org/TR/vocab-org/) is recommended.

Properties

For this entity the following properties are defined: acted on behalf of , name .

| Property                                                        | Range                                                                  | Card | Definition                                                                                                                                                                 | Usage                                                                                                                                                              | REF                                                                                                   |
| --------------------------------------------------------------- | ---------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [acted on behalf of](http://www.w3.org/ns/prov#actedOnBehalfOf) | §6.1 Agent     | 0..* | Delegation is the assignment of authority and responsibility to an agent (by itself or by another agent) to carry out a specific activity as a delegate or representative. | It can include a software agent that for example can generate a dataset but also, a person as authorised representative of providers of general-purpose AI models. | [AI Act Art. 54](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#d1e5680-1-1) |
| [name](http://xmlns.com/foaf/0.1/name)                          | Literal | 1..* | A name of the agent.                                                                                                                                                       | This property can be repeated for different versions of the name (e.g. the name in different languages).                                                           | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Agent.name)                           |

### [Algorithm](http://www.w3.org/ns/mls#Algorithm)

Definition

The algorithm regardless software implementation.

Reference

[MLS [A]](https://www.w3.org/ns/mls#Algorithm)

Properties

For this entity the following properties are defined: has algorithm type , has learning method type .

| Property                                                               | Range                                                                  | Card | Definition                                                                                                         | Usage | REF                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------ | ----- | ------------------------------------------------------------------ |
| [has algorithm type](http://w3id.org/mlso/hasAlgorithmType)            | §7.10 Concept | 0..* | A relation between an algorithm and the category of algorithms that belongs to.                                    |       | [MLSO [A]](https://dtai-kg.github.io/MLSO/#/hasAlgorithmType)      |
| [has learning method type](http://w3id.org/mlso/hasLearningMethodType) | §7.10 Concept | 0..1 | A relation between an algorithm learning method and the category of algorithm learning methods that it belongs to. |       | [MLSO [A]](https://dtai-kg.github.io/MLSO/#/hasLearningMethodType) |

### [Catalogue](http://www.w3.org/ns/dcat#Catalog)

Definition

A catalogue or repository that hosts the Datasets or Data Services being described.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue)

Properties

For this entity the following properties are defined: creator , dataset , description , homepage , identifier , keyword , licence , modification date , publisher , record , release date , service , title .

| Property                                               | Range                                                                                   | Card | Definition                                                               | Usage                                                                                                                                                                                                    | REF                                                                                         |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------- | ---- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [creator](http://purl.org/dc/terms/creator)            | §6.1 Agent                      | 0..1 | An entity responsible for the creation of the Catalogue.                 |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.creator)          |
| [dataset](http://www.w3.org/ns/dcat#dataset)           | §6.4 Dataset                  | 0..* | A Dataset that is part of the Catalogue.                                 | As empty Catalogues are usually indications of problems, this property should be combined with the property service to implement an empty Catalogue check. | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.dataset)          |
| [description](http://purl.org/dc/terms/description)    | Literal                  | 1..* | A free-text account of the Catalogue.                                    | This property can be repeated for parallel language versions of the description.                                                                                                                         | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.description)      |
| [homepage](http://xmlns.com/foaf/0.1/homepage)         | §7.14 Document                | 0..1 | A web page that acts as the main page for the Catalogue.                 |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.homepage)         |
| [identifier](http://purl.org/dc/terms/identifier)      | Literal                  | 0..1 | A unique identifier of the resource being described or cataloged.        |                                                                                                                                                                                                          | [DCAT [E]](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_identifier)                |
| [keyword](http://www.w3.org/ns/dcat#keyword)           | Literal                  | 0..* | A keyword or tag describing the resource.                                |                                                                                                                                                                                                          | [DCAT [A]](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_keyword)                   |
| [licence](http://purl.org/dc/terms/license)            | §7.26 Licence Document | 0..1 | A licence under which the Catalogue can be used or reused.               |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.licence)          |
| [modification date](http://purl.org/dc/terms/modified) | Temporal Literal | 0..1 | The most recent date on which the Catalogue was modified.                |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.modificationdate) |
| [publisher](http://purl.org/dc/terms/publisher)        | §6.1 Agent                      | 1    | An entity (organisation) responsible for making the Catalogue available. | In case multiple organisations are considered the publishers of the catalogue, it is recommended to use foaf:Group to bundle them into one entity.                                                       | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.publisher)        |
| [record](http://www.w3.org/ns/dcat#record)             | §7.4 Catalogue Record | 0..* | A Catalogue Record that is part of the Catalogue.                        |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.record)           |
| [release date](http://purl.org/dc/terms/issued)        | Temporal Literal | 0..1 | The date of formal issuance (e.g., publication) of the Catalogue.        |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.releasedate)      |
| [service](http://www.w3.org/ns/dcat#service)           | §7.13 Data Service         | 0..* | A site or end-point (Data Service) that is listed in the Catalogue.      | As empty Catalogues are usually indications of problems, this property should be combined with the property [dataset](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.dataset) to implement an empty Catalogue check | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.service)          |
| [title](http://purl.org/dc/terms/title)                | Literal                  | 1..* | A name given to the Catalogue.                                           | This property can be repeated for parallel language versions of the name.                                                                                                                                | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Catalogue.title)            |

### [Dataset](http://www.w3.org/ns/dcat#Dataset)

Definition

A conceptual entity that represents the information published.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)

Usage Note

If a Dataset is used as part of a Dataset Series, the usage of the properties listed below must be coherent with the associated Dataset Series. For this usage, consult the guidelines in section [14. General usage guidelines](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#UsageGuidelines).

Subclass of

§7.5 Catalogued Resource

Properties

For this entity the following properties are defined: access rights , bias method , collection date , collection method , contributor , creator , curation method , data provenance , dataset distribution , description , geographical coverage , has version , identifier , is referenced by , is version of , keyword , landing page , language , publisher , release date , status , theme , title , type , unsuitability method , version , version label , visibility , was generated by .

| Property                                                              | Range                                                                                     | Card | Definition                                                                                                                                                                                               | Usage                                                                                                                                                                                                    | REF                                                                                                                                                                              |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [access rights](http://purl.org/dc/terms/accessRights)                | §7.41 Rights Statement   | 0..1 | Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public.                                                                                         | The recommended controlled vocabulary is the [Access Rights Named Authority List](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/access-right). | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.accessrights)                                                                                            |
| [bias method](http://data.europa.eu/it6/biasMethod)                   | Literal                    | 0..* | A description of any methods implemented in data acquisition or processing, if any, to address the prevalence of identifiable biases in the training data.                                               |                                                                                                                                                                                                          | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                   |
| [collection date](http://data.europa.eu/it6/collectionDate)           | Temporal Literal   | 1    | The date the data was originally collected, given by the uploader.                                                                                                                                       |                                                                                                                                                                                                          | No references available.                                                                                                                                                         |
| [collection method](http://data.europa.eu/it6/collectionMethod)       | Literal                    | 0..1 | Method used to collect the data, provided by the uploader.                                                                                                                                               |                                                                                                                                                                                                          | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) |
| [contributor](http://purl.org/dc/terms/contributor)                   | §6.1 Agent                        | 0..* | An entity responsible for making contributions to the dataset.                                                                                                                                           |                                                                                                                                                                                                          | No references available.                                                                                                                                                         |
| [creator](http://purl.org/dc/terms/creator)                           | §6.1 Agent                        | 0..* | An entity responsible for producing the Dataset.                                                                                                                                                         |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.creator)                                                                                                 |
| [curation method](http://data.europa.eu/it6/curationMethod)           | Literal                    | 0..* | General description of the data processing involved in transforming the acquired data into training, testing, and validation data for the model, such as cleaning (e.g. filtering out irrelevant content such as advertisements), normalisation (e.g. tokenizing), augmentation (e.g. back-translation). |                                                                                                                                                                                                          | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                   |
| [data provenance](http://data.europa.eu/it6/dataProvenance)           | Literal                    | 0..* | A documented trail that accounts for the origin of the data.                                                                                                                                             |                                                                                                                                                                                                          | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                   |
| [dataset distribution](http://www.w3.org/ns/dcat#distribution)        | §6.5 Distribution          | 0..* | An available Distribution for the Dataset.                                                                                                                                                               |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.datasetdistribution)                                                                                     |
| [description](http://purl.org/dc/terms/description)                   | Literal                    | 1..* | A free-text account of the Dataset.                                                                                                                                                                      | This property can be repeated for parallel language versions of the description.                                                                                                                         | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.description) , [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)            |
| [geographical coverage](http://purl.org/dc/terms/spatial)             | §7.28 Location                  | 0..* | A geographic region that is covered by the Dataset.                                                                                                                                                      |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.geographicalcoverage) , [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)   |
| [has version](http://www.w3.org/ns/dcat#hasVersion)                   | §6.4 Dataset                    | 0..* | A related Dataset that is a version, edition, or adaptation of the described Dataset.                                                                                                                    |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.hasversion)                                                                                              |
| [identifier](http://purl.org/dc/terms/identifier)                     | Literal                    | 0..* | The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue.                                                                                            |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.identifier)                                                                                              |
| [is referenced by](http://purl.org/dc/terms/isReferencedBy)           | §6.9 Paper                        | 0..* | A related resource that references, cites, or otherwise points to the dataset.                                                                                                                           |                                                                                                                                                                                                          | [DCAT-AP [E]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.isreferencedby)                                                                                          |
| [is version of](http://purl.org/dc/terms/isVersionOf)                 | §6.4 Dataset                    | 0..* | A related Dataset of which the described Dataset is a version, edition, or adaptation.                                                                                                                   |                                                                                                                                                                                                          | No references available.                                                                                                                                                         |
| [keyword](http://www.w3.org/ns/dcat#keyword)                          | Literal                    | 0..* | A keyword or tag describing the Dataset.                                                                                                                                                                 |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.keyword)                                                                                                 |
| [landing page](http://www.w3.org/ns/dcat#landingPage)                 | §7.14 Document                  | 0..* | A web page that provides access to the Dataset, its Distributions and/or additional information.                                                                                                         | It is intended to point to a landing page at the original data provider, not to a page on a site of a third party, such as an aggregator.                                                                | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.landingpage)                                                                                             |
| [language](http://purl.org/dc/terms/language)                         | §7.27 Linguistic System | 0..* | A language of the Dataset.                                                                                                                                                                               |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.language) , [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)               |
| [publisher](http://purl.org/dc/terms/publisher)                       | §6.1 Agent                        | 0..1 | An entity (organisation) responsible for making the resource available.                                                                                                                                  |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.publisher)                                                                                               |
| [release date](http://purl.org/dc/terms/issued)                       | Temporal Literal   | 0..1 | The date of formal issuance (e.g., publication) of the Dataset.                                                                                                                                          |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.releasedate)                                                                                             |
| [status](http://www.w3.org/ns/adms#status)                            | §7.10 Concept                    | 0..1 | The stage of the dataset in the context of the publication process.                                                                                                                                      | The recommended controlled vocabulary is the [Dataset status](https://semiceu.github.io/MLDCAT-AP/releases/codelist/dataset-status.html) code list.                                                      | [DCAT [E]](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_status)                                                                                                         |
| [theme](http://www.w3.org/ns/dcat#theme)                              | §7.10 Concept                    | 0..* | A category of the Dataset.                                                                                                                                                                               |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.theme) , [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                  |
| [title](http://purl.org/dc/terms/title)                               | Literal                    | 1..* | A name given to the Dataset.                                                                                                                                                                             | This property can be repeated for parallel language versions of the name.                                                                                                                                | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.title)                                                                                                   |
| [type](http://purl.org/dc/terms/type)                                 | §7.10 Concept                    | 0..* | A type of the Dataset.                                                                                                                                                                                   | A recommended controlled vocabulary data-type is foreseen.                                                                                                                                               | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.type) , [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                   |
| [unsuitability method](http://data.europa.eu/it6/unsuitabilityMethod) | Literal                    | 0..* | A description of any methods implemented in data acquisition or processing, if any, to detect the presence of unsuitable data sources considering the model's intended uses, including but not limited to illegal content, child sexual abuse material (CSAM), non-consensual intimate imagery (NCII), and personal data leading to its unlawful processing. |                                                                                                                                                                                                          | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                   |
| [version](http://www.w3.org/ns/dcat#version)                          | Literal                    | 0..1 | The version indicator (name or identifier) of a resource.                                                                                                                                                |                                                                                                                                                                                                          | [DCAT [A]](https://www.w3.org/TR/vocab-dcat-3/#Dataset.version)                                                                                                                  |
| [version label](http://data.europa.eu/it6/versionLabel)               | Literal                    | 0..1 | User-provided version label, which can be a date, hash, or other identifier relevant to the user.                                                                                                        |                                                                                                                                                                                                          | No references available.                                                                                                                                                         |
| [visibility](http://data.europa.eu/it6/visibility)                    | §7.10 Concept                    | 0..1 | Settings for a dataset that determine who can access or view it. Options typically include 'Everyone', 'All my friends', 'Only me', or specific user-defined circles.                                    | The recommended controlled vocabulary is the [Dataset visibility](https://semiceu.github.io/MLDCAT-AP/releases/codelist/dataset-visibility.html) code list.                                              | No references available.                                                                                                                                                         |
| [was generated by](http://www.w3.org/ns/prov#wasGeneratedBy)          | §7.1 Activity                  | 0..* | An activity that generated, or provides the business context for, the creation of the dataset.                                                                                                           |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Dataset.wasgeneratedby)                                                                                          |

### [Distribution](http://www.w3.org/ns/dcat#Distribution)

Definition

A physical embodiment of the Dataset in a particular format.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution)

Properties

For this entity the following properties are defined: access service , access URL , byte size , checksum , default target attribute , download URL , format , has data , has feature , has policy , has quality measurement , identifier , ignore attribute , language , licence , linked schemas , media type , number of datapoints , processing date , processing error , processing warning , row ID attribute , title .

| Property                                                                     | Range                                                                                         | Card | Definition                                                                                                                                                                                               | Usage                                                                                                                                                                                                    | REF                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [access service](http://www.w3.org/ns/dcat#accessService)                    | §7.13 Data Service               | 0..* | A data service that gives access to the distribution of the dataset.                                                                                                                                     |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.accessservice)                                                                                                              |
| [access URL](http://www.w3.org/ns/dcat#accessURL)                            | §7.5 Catalogued Resource | 1..* | A URL that gives access to a Distribution of the Dataset.                                                                                                                                                | The resource at the access URL may contain information about how to get the Dataset.                                                                                                                     | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.accessURL)                                                                                                                  |
| [byte size](http://www.w3.org/ns/dcat#byteSize)                              | nonNegativeInteger  | 0..1 | The size of a Distribution in bytes.                                                                                                                                                                     |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.bytesize)                                                                                                                   |
| [checksum](http://spdx.org/rdf/terms#checksum)                               | §7.6 Checksum                      | 0..1 | A mechanism that can be used to verify that the contents of a distribution have not changed.                                                                                                             | The checksum is related to the downloadURL.                                                                                                                                                              | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.checksum)                                                                                                                   |
| [default target attribute](http://data.europa.eu/it6/defaultTargetAttribute) | Literal                        | 0..* | The primary attribute intended for analysis or processing, if applicable.                                                                                                                                | Tasks can also be defined that use another attribute as target.                                                                                                                                          | No references available.                                                                                                                                                                                 |
| [download URL](http://www.w3.org/ns/dcat#downloadURL)                        | §7.5 Catalogued Resource | 0..* | A URL that is a direct link to a downloadable file in a given format.                                                                                                                                    |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.downloadURL)                                                                                                                |
| [format](http://purl.org/dc/terms/format)                                    | §7.31 Media Type Or Extent | 0..1 | The file format of the Distribution.                                                                                                                                                                     | The recommended controlled vocabulary is the [EU Vocabularies File Type Named Authority List](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/file-type). | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.format)                                                                                                                     |
| [has data](https://w3id.org/dpv#hasData)                                     | §7.10 Concept                        | 0..* | Indicates association with Data (may or may not be personal).                                                                                                                                            | The suggested code list is the [Data Categories](https://w3c.github.io/dpv/2.3/dpv/modules/personal_data#vocab-personal-data).                                                                           | No references available.                                                                                                                                                                                 |
| [has feature](http://data.europa.eu/it6/hasFeature)                          | §7.20 Feature                        | 0..* | The attribute or column being part of a distribution.                                                                                                                                                    |                                                                                                                                                                                                          | No references available.                                                                                                                                                                                 |
| [has policy](http://www.w3.org/ns/odrl/2/hasPolicy)                          | §7.35 Policy                          | 0..1 | The policy expressing the rights associated with the distribution if using the [ODRL] vocabulary.                                                                                                      |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.haspolicy)                                                                                                                  |
| [has quality measurement](http://www.w3.org/ns/dqv#hasQualityMeasurement)    | §6.10 Quality Measurement | 1..* | Metrics that can be performed to assess the quality of any kind of resource (e.g., a dataset, a linkset, a graph, a set of triples). However, in the DQV context, it is generally expected to be used in statements in which subjects are instances of dcat:Dataset or dcat:Distribution. |                                                                                                                                                                                                          | No references available.                                                                                                                                                                                 |
| [identifier](http://purl.org/dc/terms/identifier)                            | Literal                        | 0..1 | An unambiguous identifier for the resource.                                                                                                                                                              |                                                                                                                                                                                                          | No references available.                                                                                                                                                                                 |
| [ignore attribute](http://data.europa.eu/it6/ignoreAttribute)                | Literal                        | 0..* | Attributes that should be excluded in modelling, such as identifiers and indexes.                                                                                                                        |                                                                                                                                                                                                          | No references available.                                                                                                                                                                                 |
| [language](http://purl.org/dc/terms/language)                                | §7.27 Linguistic System     | 0..* | A language used in the Distribution.                                                                                                                                                                     | This property can be repeated if the metadata is provided in multiple languages. The recommended controlled vocabulary is the [EU Vocabularies Languages Named Authority List](http://publications.europa.eu/resource/authority/language). | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.language)                                                                                                                   |
| [licence](http://purl.org/dc/terms/license)                                  | §7.26 Licence Document       | 0..1 | A licence under which the Distribution is made available.                                                                                                                                                |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.licence) , [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                   |
| [linked schemas](http://purl.org/dc/terms/conformsTo)                        | §7.45 Standard                      | 0..* | An established schema to which the described Distribution conforms.                                                                                                                                      |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.linkedschemas)                                                                                                              |
| [media type](http://www.w3.org/ns/dcat#mediaType)                            | §7.30 Media Type                   | 0..1 | The media type of the Distribution as defined in the official register of media types managed by IANA.                                                                                                   |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.mediatype)                                                                                                                  |
| [number of datapoints](http://data.europa.eu/it6/numberOfDatapoints)         | nonNegativeInteger  | 0..1 | The total count of individual data entries or observations contained.                                                                                                                                    |                                                                                                                                                                                                          | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII) , [AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII) |
| [processing date](http://data.europa.eu/it6/processingDate)                  | Temporal Literal       | 0..1 | Date of processing.                                                                                                                                                                                      |                                                                                                                                                                                                          | No references available.                                                                                                                                                                                 |
| [processing error](http://data.europa.eu/it6/processingError)                | Literal                        | 0..1 | Errors discovered while processing the dataset.                                                                                                                                                          |                                                                                                                                                                                                          | No references available.                                                                                                                                                                                 |
| [processing warning](http://data.europa.eu/it6/processingWarning)            | Literal                        | 0..1 | Warnings while processing the dataset.                                                                                                                                                                   |                                                                                                                                                                                                          | No references available.                                                                                                                                                                                 |
| [row ID attribute](http://data.europa.eu/it6/rowIDAttribute)                 | Literal                        | 0..1 | The attribute that represents the row-id column, if present in the dataset.                                                                                                                              |                                                                                                                                                                                                          | No references available.                                                                                                                                                                                 |
| [title](http://purl.org/dc/terms/title)                                      | Literal                        | 0..* | A name given to the Distribution.                                                                                                                                                                        | This property can be repeated for parallel language versions of the name.                                                                                                                                | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Distribution.title)                                                                                                                      |

### [File](http://data.europa.eu/it6/File)

Definition

A physical embodiment of the machine learning model in a particular format.

Reference

[AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)

Properties

For this entity the following properties are defined: checksum , format , id , title , url .

| Property                                       | Range                                                                                         | Card | Definition                                                                                   | Usage | REF                                                                            |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------ |
| [checksum](http://spdx.org/rdf/terms#checksum) | §7.6 Checksum                      | 0..* | A mechanism that can be used to verify that the contents of a distribution have not changed. |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) |
| [format](http://purl.org/dc/terms/format)      | §7.10 Concept                        | 1    | The file format, physical medium, or dimensions of the resource.                             |       | No references available.                                                       |
| [id](http://purl.org/dc/terms/identifier)      | Literal                        | 1    | An unambiguous identifier for the resource.                                                  |       | No references available.                                                       |
| [title](http://purl.org/dc/terms/title)        | Literal                        | 1    | The name assigned to the resource.                                                           |       | No references available.                                                       |
| [url](http://data.europa.eu/it6/url)           | §7.5 Catalogued Resource | 1    | The url of the file to be downloaded.                                                        |       | No references available.                                                       |

### [Harm Risk](http://data.europa.eu/it6/HarmRisk)

Definition

The combination of the probability of an occurrence of harm and the severity of that harm.

Reference

[AI Act art_3.tit_1](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#art_3.tit_1)

Properties

For this entity the following properties are defined: description , mitigation , nature , probability , severity , source , title , type .

| Property                                             | Range                                                                  | Card | Definition                                                     | Usage | REF                                                                                                       |
| ---------------------------------------------------- | ---------------------------------------------------------------------- | ---- | -------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------- |
| [description](http://purl.org/dc/terms/description)  | Literal | 1    | An account of the resource.                                    |       | No references available.                                                                                  |
| [mitigation](http://data.europa.eu/it6/mitigation)   | Literal | 0..* | The action of reducing the likelihood or severity of the risk. |       | [AI Act rct_114](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#rct_114)         |
| [nature](http://data.europa.eu/it6/nature)           | §7.10 Concept | 0..* | The inherent characteristics of the risk.                      |       | [AI Act rct_116](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#rct_116)         |
| [probability](http://data.europa.eu/it6/probability) | Literal | 0..1 | The likelihood that a given event will occur.                  |       | [AI Act art_3.tit_1](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#art_3.tit_1) |
| [severity](http://data.europa.eu/it6/severity)       | Literal | 0..1 | The extent of the damage resulting from an event occurring.    |       | [AI Act art_3.tit_1](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#art_3.tit_1) |
| [source](http://data.europa.eu/it6/source)           | §7.10 Concept | 0..* | The origin or cause of the risk.                               |       | [AI Act rct_116](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#rct_116)         |
| [title](http://purl.org/dc/terms/title)              | Literal | 1    | A name associated to the risk.                                 |       | No references available.                                                                                  |
| [type](http://purl.org/dc/terms/type)                | §7.10 Concept | 0..* | The nature or genre of the resource.                           |       | No references available.                                                                                  |

### [Machine Learning Model](http://data.europa.eu/it6/MachineLearningModel)

Definition

A file that has been trained to recognize certain types of patterns.

Reference

[AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689)

Properties

For this entity the following properties are defined: bias , contributor , created , creator , description , design specifications , evaluation results , evaluation strategies , fine tuned from , has benchmark , has bibliographic reference , has engagement , has file , has input modality , has output modality , has policy , has prediction , has provider , has registered user , has repository , has risk , has uploader , has variation , how to use , identifier , intended use , is funded by , keyword , language , licence , limitations , logo , method of distribution , model architecture , modified , name , placed on market date , ran on , release date , short description , tested on , testing description , total number of parameters , trained on , training methodologies , training process , type , validated on , version .

| Property                                                                           | Range                                                                                                 | Card | Definition                                                                                                                                                                                               | Usage                                              | REF                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bias](http://data.europa.eu/it6/bias)                                             | Literal                                | 0..1 | A description of the possible biases affecting the overall output of the model.                                                                                                                          |                                                    | No references available.                                                                                                                                                                                 |
| [contributor](http://purl.org/dc/terms/contributor)                                | §6.1 Agent                                    | 0..* | An entity responsible for making contributions to the resource.                                                                                                                                          |                                                    | No references available.                                                                                                                                                                                 |
| [created](http://purl.org/dc/terms/created)                                        | Temporal Literal               | 1    | Date of creation of the resource.                                                                                                                                                                        |                                                    | No references available.                                                                                                                                                                                 |
| [creator](http://purl.org/dc/terms/creator)                                        | §6.1 Agent                                    | 0..* | An entity responsible for making the resource.                                                                                                                                                           |                                                    | No references available.                                                                                                                                                                                 |
| [description](http://purl.org/dc/terms/description)                                | Literal                                | 0..* | Description of the resource.                                                                                                                                                                             |                                                    | No references available.                                                                                                                                                                                 |
| [design specifications](http://data.europa.eu/it6/designSpecifications)            | Literal                                | 0..* | A general description of the main steps or stages involved in the training process, including training methodologies and techniques, the key design choices, assumptions made and what the model is designed to optimise for, and the relevance of different parameters, as applicable. |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                                           |
| [evaluation results](http://data.europa.eu/it6/evaluationResults)                  | Literal                                | 0..1 | A description of the evaluation against the validation dataset.                                                                                                                                          |                                                    | No references available.                                                                                                                                                                                 |
| [evaluation strategies](http://data.europa.eu/it6/evaluationStrategies)            | Literal                                | 0..1 | A description of the evaluation strategies used.                                                                                                                                                         |                                                    | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                                                                                                          |
| [fine tuned from](http://data.europa.eu/it6/fineTunedFrom)                         | §6.8 Machine Learning Model    | 0..1 | The model from which this model has been fine tuned.                                                                                                                                                     |                                                    | No references available.                                                                                                                                                                                 |
| [has benchmark](http://data.europa.eu/it6/hasBenchmark)                            | §7.2 Benchmark                            | 0..* | The benchmarks used to evaluate this model.                                                                                                                                                              |                                                    | [AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII)                                                                                                      |
| [has bibliographic reference](http://data.europa.eu/it6/hasBibliographicReference) | §7.3 Bibliographic Reference | 0..* | The reference to a paper.                                                                                                                                                                                |                                                    | No references available.                                                                                                                                                                                 |
| [has engagement](http://data.europa.eu/it6/hasEngagement)                          | §7.15 Engagement                          | 0..1 | Statistics resulting of user engagement.                                                                                                                                                                 |                                                    | No references available.                                                                                                                                                                                 |
| [has file](http://data.europa.eu/it6/hasFile)                                      | §6.6 File                                      | 1..* | The file in which the model is expressed.                                                                                                                                                                |                                                    | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                                                                                                          |
| [has input modality](http://data.europa.eu/it6/hasInputModality)                   | §7.32 Modality                              | 0..* | The modality of the input of the model.                                                                                                                                                                  |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                         |
| [has output modality](http://data.europa.eu/it6/hasOutputModality)                 | §7.32 Modality                              | 0..* | The modality of the output of the model.                                                                                                                                                                 |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                         |
| [has policy](http://www.w3.org/ns/odrl/2/hasPolicy)                                | §7.35 Policy                                  | 0..* | The policy expressing the rights associated with the distribution if using the [ODRL] vocabulary.                                                                                                      |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                         |
| [has prediction](http://data.europa.eu/it6/hasPrediction)                          | §6.4 Dataset                                | 0..* | The predicted dataset generated as output of a machine learning model.                                                                                                                                   |                                                    | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                                                                                                          |
| [has provider](http://data.europa.eu/it6/hasProvider)                              | §6.1 Agent                                    | 0..* | A natural or legal person, public authority, agency or other body that develops a Machine Learning Model or places it on the market or puts the it into service under its own name or trademark, whether for payment or free of charge. |                                                    | No references available.                                                                                                                                                                                 |
| [has registered user](http://data.europa.eu/it6/hasRegisteredUser)                 | §6.1 Agent                                    | 0..* | The registered user associated to the model.                                                                                                                                                             |                                                    | [AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII)                                                                                                      |
| [has repository](http://data.europa.eu/it6/hasRepository)                          | §7.39 Repository                          | 0..* | The repository associated.                                                                                                                                                                               |                                                    | No references available.                                                                                                                                                                                 |
| [has risk](http://data.europa.eu/it6/hasRisk)                                      | §6.7 Harm Risk                             | 0..* | A possible risk that can occur.                                                                                                                                                                          |                                                    | No references available.                                                                                                                                                                                 |
| [has uploader](http://data.europa.eu/it6/hasUploader)                              | §6.1 Agent                                    | 0..1 | An entity responsible for uploading the resource.                                                                                                                                                        |                                                    | No references available.                                                                                                                                                                                 |
| [has variation](http://data.europa.eu/it6/hasVariation)                            | §6.8 Machine Learning Model    | 0..* | The model that is variant of this model.                                                                                                                                                                 |                                                    | No references available.                                                                                                                                                                                 |
| [how to use](http://data.europa.eu/it6/howToUse)                                   | Literal                                | 0..1 | An explanation of how to use or deploy the model.                                                                                                                                                        |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                                           |
| [identifier](http://purl.org/dc/terms/identifier)                                  | Literal                                | 1    | An unambiguous identifier for the resource.                                                                                                                                                              |                                                    | No references available.                                                                                                                                                                                 |
| [intended use](http://data.europa.eu/it6/intendedUse)                              | Literal                                | 0..* | The prescribed application of the model.                                                                                                                                                                 |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII) |
| [is funded by](http://purl.org/cerif/frapo/isFundedBy)                             | §6.1 Agent                                    | 0..* | An object property linking something to the funding that funds it (i.e. that finances or pays for it), or to the funding agency providing that funding. This flexibility is given because of alternative usages of the English word 'funds'. |                                                    | No references available.                                                                                                                                                                                 |
| [keyword](http://www.w3.org/ns/dcat#keyword)                                       | Literal                                | 0..* | A tag describing the resource.                                                                                                                                                                           |                                                    | No references available.                                                                                                                                                                                 |
| [language](http://purl.org/dc/terms/language)                                      | §7.27 Linguistic System             | 0..* | A language of the resource.                                                                                                                                                                              | The language that the model is able to understand. | No references available.                                                                                                                                                                                 |
| [licence](http://purl.org/dc/terms/license)                                        | §7.26 Licence Document               | 0..* | The licence under which the resource is made available.                                                                                                                                                  |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII) |
| [limitations](http://data.europa.eu/it6/limitations)                               | Literal                                | 0..1 | The limited capabilities of the model.                                                                                                                                                                   |                                                    | No references available.                                                                                                                                                                                 |
| [logo](http://data.europa.eu/m8g/logo)                                             | §7.24 Image Object                       | 0..* | An image or logo of the model.                                                                                                                                                                           |                                                    | No references available.                                                                                                                                                                                 |
| [method of distribution](http://data.europa.eu/it6/methodOfDistribution)           | Literal                                | 0..* | A method of distribution through which the model has been made or can be made available to downstream providers.                                                                                         |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII)                       |
| [model architecture](http://data.europa.eu/it6/modelArchitecture)                  | Literal                                | 0..* | A general description of the model architecture, e.g. a transformer architecture.                                                                                                                        |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                         |
| [modified](http://purl.org/dc/terms/modified)                                      | Temporal Literal               | 0..* | The date the machine learning model was last modified.                                                                                                                                                   |                                                    | No references available.                                                                                                                                                                                 |
| [name](http://purl.org/dc/terms/title)                                             | Literal                                | 1..* | The name assigned to the resource.                                                                                                                                                                       |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689)                                       |
| [placed on market date](http://data.europa.eu/it6/placedOnMarketDate)              | Temporal Literal               | 0..1 | Date when the model was placed on the Union market.                                                                                                                                                      |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                                           |
| [ran on](http://data.europa.eu/it6/ranOn)                                          | §6.4 Dataset                                | 0..* | The dataset on which a machine learning model is executed.                                                                                                                                               |                                                    | No references available.                                                                                                                                                                                 |
| [release date](http://data.europa.eu/it6/releaseDate)                              | Temporal Literal               | 0..1 | The date a model is released.                                                                                                                                                                            |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII) |
| [short description](http://data.europa.eu/it6/shortDescription)                    | Literal                                | 0..1 | A short description of a machine learning model.                                                                                                                                                         |                                                    | No references available.                                                                                                                                                                                 |
| [tested on](http://data.europa.eu/it6/testedOn)                                    | §6.4 Dataset                                | 0..* | The testing dataset used to evaluate the machine learning model.                                                                                                                                         |                                                    | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                                                                                                          |
| [testing description](http://data.europa.eu/it6/testingDescription)                | Literal                                | 0..1 | A detailed description of the measures put in place for the purpose of conducting internal and/or external adversarial testing (e.g. red teaming), model adaptations, including alignment and fine-tuning. |                                                    | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                                                                                                          |
| [total number of parameters](http://data.europa.eu/it6/totalNumberOfParameters)    | nonNegativeInteger          | 0..* | The total number of parameters of the model.                                                                                                                                                             |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII)                       |
| [trained on](http://data.europa.eu/it6/trainedOn)                                  | §6.4 Dataset                                | 1..* | The training dataset used to train the machine learning model.                                                                                                                                           |                                                    | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                                                                                                          |
| [training methodologies](http://data.europa.eu/it6/trainingMethodologies)          | Literal                                | 0..1 | A description of the methodologies used.                                                                                                                                                                 |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                         |
| [training process](http://data.europa.eu/it6/trainingProcess)                      | Literal                                | 0..1 | A description of the training process.                                                                                                                                                                   |                                                    | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                         |
| [type](http://purl.org/dc/terms/type)                                              | §7.10 Concept                                | 0..* | The nature or genre of the resource.                                                                                                                                                                     |                                                    | No references available.                                                                                                                                                                                 |
| [validated on](http://data.europa.eu/it6/validatedOn)                              | §6.4 Dataset                                | 0..* | The validation dataset used to fine-tune the machine learning model.                                                                                                                                     |                                                    | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                                                                                                          |
| [version](http://www.w3.org/ns/dcat#version)                                       | Literal                                | 1    | The current version of the model.                                                                                                                                                                        |                                                    | No references available.                                                                                                                                                                                 |

### [Paper](https://linkedpaperswithcode.com/class/paper)

Definition

A paper makes content and research results available to the general public.

Reference

[LPWC [A]](https://linkedpaperswithcode.com/resource/?uri=https%3A%2F%2Flinkedpaperswithcode.com%2Fclass%2Fpaper&ontology=https%3A%2F%2Flinkedpaperswithcode.com%2Fontology%23)

Properties

For this entity the following properties are defined: abstract , creator , date , has document , has model , has repository , references , subject , title .

| Property                                                                  | Range                                                                                              | Card | Definition                                                                                       | Usage | REF                                                                                                                                                                             |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [abstract](http://purl.org/dc/terms/abstract)                             | Literal                             | 0..1 | A summary of the resource.                                                                       |       | [LPWC [E]](https://linkedpaperswithcode.com/resource/?uri=https%3A%2F%2Flinkedpaperswithcode.com%2Fclass%2Fpaper&ontology=https%3A%2F%2Flinkedpaperswithcode.com%2Fontology%23) |
| [creator](http://purl.org/dc/terms/creator)                               | §6.1 Agent                                 | 0..* | An entity responsible for making the resource.                                                   |       | No references available.                                                                                                                                                        |
| [date](http://purl.org/dc/terms/date)                                     | Temporal Literal            | 1    | A point or period of time associated with an event in the lifecycle of the resource.             |       | [LPWC [E]](https://linkedpaperswithcode.com/resource/?uri=https%3A%2F%2Flinkedpaperswithcode.com%2Fclass%2Fpaper&ontology=https%3A%2F%2Flinkedpaperswithcode.com%2Fontology%23) |
| [has document](http://data.europa.eu/it6/hasDocument)                     | §7.14 Document                           | 1    | The url or location of the document itself.                                                      |       | No references available.                                                                                                                                                        |
| [has model](https://linkedpaperswithcode.com/property/hasModel)           | §6.8 Machine Learning Model | 0..* | The model that is used by a paper or an evaluation.                                              |       | [LPWC [E]](https://linkedpaperswithcode.com/resource/?uri=https%3A%2F%2Flinkedpaperswithcode.com%2Fclass%2Fpaper&ontology=https%3A%2F%2Flinkedpaperswithcode.com%2Fontology%23) |
| [has repository](https://linkedpaperswithcode.com/property/hasRepository) | §7.39 Repository                       | 0..* | The repository of a paper.                                                                       |       | [LPWC [A]](https://linkedpaperswithcode.com/resource/?uri=https%3A%2F%2Flinkedpaperswithcode.com%2Fclass%2Fpaper&ontology=https%3A%2F%2Flinkedpaperswithcode.com%2Fontology%23) |
| [references](http://purl.org/dc/terms/references)                         | §6.4 Dataset                             | 0..* | A related resource that is referenced, cited, or otherwise pointed to by the described resource. |       | No references available.                                                                                                                                                        |
| [subject](http://purl.org/dc/terms/subject)                               | Literal                             | 0..1 | A topic of the resource.                                                                         |       | No references available.                                                                                                                                                        |
| [title](http://purl.org/dc/terms/title)                                   | Literal                             | 1    | A name given to the resource.                                                                    |       | [LPWC [E]](https://linkedpaperswithcode.com/resource/?uri=https%3A%2F%2Flinkedpaperswithcode.com%2Fclass%2Fpaper&ontology=https%3A%2F%2Flinkedpaperswithcode.com%2Fontology%23) |

### [Quality Measurement](http://www.w3.org/ns/dqv#QualityMeasurement)

Definition

The evaluation of a given dataset (or dataset distribution) against a specific quality metric.

Properties

For this entity the following properties are defined: dataset , feature index , interval end , interval start , type , value .

| Property                                                  | Range                                                                                                        | Card | Definition                                        | Usage | REF                      |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---- | ------------------------------------------------- | ----- | ------------------------ |
| [dataset](http://purl.org/linked-data/cube#dataSet)       | §7.38 Quality Measurement Dataset | 0..* | The data set of which this observation is a part. |       | No references available. |
| [feature index](http://data.europa.eu/it6/featureIndex)   | §7.20 Feature                                       | 0..1 | The feature on which the quality is measure on.   |       | No references available. |
| [interval end](http://data.europa.eu/it6/intervalEnd)     | Temporal Literal                      | 0..1 | The maximum value of the Quality Measure.         |       | No references available. |
| [interval start](http://data.europa.eu/it6/intervalStart) | Temporal Literal                      | 0..1 | The minimum value of the Quality Measure.         |       | No references available. |
| [type](http://purl.org/dc/terms/type)                     | §7.12 Data Quality                              | 1    | A classification for a quality.                   |       | No references available. |
| [value](http://www.w3.org/ns/dqv#value)                   | Literal                                       | 1    | Values computed by metric.                        |       | No references available. |

## Supportive Entities

The supportive entities are supporting the main entities in the Application Profile.
They are included in the Application Profile because they form the range of properties.

### [Activity](http://www.w3.org/ns/prov#Activity)

Definition

An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Activity)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Benchmark](http://data.europa.eu/it6/Benchmark)

Definition

A type of comparison between two or more resources.

Reference

[AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII)

Properties

For this entity the following properties are defined: title .

| Property                                | Range                                                                  | Card | Definition                         | Usage | REF                                                                                                 |
| --------------------------------------- | ---------------------------------------------------------------------- | ---- | ---------------------------------- | ----- | --------------------------------------------------------------------------------------------------- |
| [title](http://purl.org/dc/terms/title) | Literal | 1..* | The name assigned to the resource. |       | [AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII) |

### [Bibliographic Reference](http://purl.org/spar/biro/BibliographicReference)

Definition

An expression of a bibliographic record in a specific format, that references a particular textual or data publication (or a work in preparation for publication). Each bibliographic reference is a list of items containing entities that describe aspects of the referenced work - for example authors, title, journal, publication year - selected from the bibliographic record. Note that because different journal styles may require omission of elements of the bibliographic record in references included in a paper's reference list (e.g. the title, the identifier, the names of the eighth and subsequent authors), and because errors can be introduced when an author creates a bibliographic reference, the bibliographic reference to a published work may not be a complete or fully accurate expression of the information contained within the authoritative bibliographic record for that work.

Properties

For this entity the following properties are defined: bibliographic citation , format , references .

| Property                                                                 | Range                                                                  | Card | Definition                                                                                       | Usage | REF                      |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------ | ----- | ------------------------ |
| [bibliographic citation](http://purl.org/dc/terms/bibliographicCitation) | Literal | 1    | A bibliographic reference for the resource.                                                      |       | No references available. |
| [format](http://purl.org/dc/terms/format)                                | Literal | 1    | The file format, physical medium, or dimensions of the resource.                                 |       | No references available. |
| [references](http://purl.org/dc/terms/references)                        | §6.9 Paper     | 0..* | A related resource that is referenced, cited, or otherwise pointed to by the described resource. |       | No references available. |

### [Catalogue Record](http://www.w3.org/ns/dcat#CatalogRecord)

Definition

A description of a Catalogued Resource's entry in the Catalogue.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#CatalogueRecord)

Properties

For this entity the following properties are defined: description , description version , modification date , primary topic .

| Property                                                            | Range                                                                                         | Card | Definition                                                                 | Usage                                                                                                                                                                                                    | REF                                                                                               |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [description](http://purl.org/dc/terms/description)                 | Literal                        | 0..* | A free-text account of the record.                                         | This property can be repeated for parallel language versions of the description.                                                                                                                         | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#CatalogueRecord.description)      |
| [description version](http://data.europa.eu/it6/descriptionVersion) | Literal                        | 0..1 | Version number of the description. '1' for original version.               |                                                                                                                                                                                                          | No references available.                                                                          |
| [modification date](http://purl.org/dc/terms/modified)              | Temporal Literal       | 1    | The most recent date on which the Catalogue entry was changed or modified. |                                                                                                                                                                                                          | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#CatalogueRecord.modificationdate) |
| [primary topic](http://xmlns.com/foaf/0.1/primaryTopic)             | §7.5 Catalogued Resource | 1    | A link to the Dataset, Data service or Catalog described in the record.    | A catalogue record will refer to one entity in a catalogue. This can be either a Dataset or a Data Service. To ensure an unambiguous reading of the cardinality the range is set to Catalogued Resource. However it is not the intend with this range to require the explicit use of the class Catalogued Record. As abstract class, an subclass should be used. | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#CatalogueRecord.primarytopic)     |

### [Catalogued Resource](http://www.w3.org/ns/dcat#Resource)

Definition

Resource published or curated by a single agent.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#CataloguedResource)

Usage Note

This class Catalogued Record is an abstract class for DCAT-AP. Therefore only subclasses should be used in a data exchange.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Checksum](http://spdx.org/rdf/terms#Checksum)

Definition

A value that allows the contents of a file to be authenticated.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Checksum)

Usage Note

This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.

Properties

For this entity the following properties are defined: algorithm , checksum value .

| Property                                                  | Range                                                                                       | Card | Definition                                                                         | Usage                                                                                                      | REF                                                                                     |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ---- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [algorithm](http://spdx.org/rdf/terms#algorithm)          | §7.7 Checksum Algorithm | 1    | The algorithm used to produce the subject Checksum.                                | The members of this property are the [supported checksum algorithms](https://spdx.org/rdf/terms/#d4e2129). | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Checksum.algorithm)     |
| [checksum value](http://spdx.org/rdf/terms#checksumValue) | hexBinary                  | 1    | A lower case hexadecimal encoded digest value produced using a specific algorithm. |                                                                                                            | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Checksum.checksumvalue) |

### [Checksum Algorithm](http://spdx.org/rdf/terms#ChecksumAlgorithm)

Definition

Algorithm for Checksums.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#ChecksumAlgorithm)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Collection](http://data.europa.eu/it6/Collection)

Definition

A group of task or runs to easily refer to them and share them with others.

Properties

For this entity the following properties are defined: creation date , description , has uploader , identifier , title , visibility .

| Property                                                | Range                                                                                   | Card | Definition                                                                                                                                                            | Usage                                                                                                                                                             | REF                      |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| [creation date](http://data.europa.eu/it6/creationDate) | Temporal Literal | 1    | Date of creation of the resource.                                                                                                                                     |                                                                                                                                                                   | No references available. |
| [description](http://purl.org/dc/terms/description)     | Literal                  | 0..1 | Description of the resource.                                                                                                                                          |                                                                                                                                                                   | No references available. |
| [has uploader](http://data.europa.eu/it6/hasUploader)   | §6.1 Agent                      | 1    | An entity responsible for uploading the resource.                                                                                                                     |                                                                                                                                                                   | No references available. |
| [identifier](http://purl.org/dc/terms/identifier)       | Literal                  | 1    | An unambiguous identifier for the resource.                                                                                                                           |                                                                                                                                                                   | No references available. |
| [title](http://purl.org/dc/terms/title)                 | Literal                  | 1    | A name assigned to the resource.                                                                                                                                      |                                                                                                                                                                   | No references available. |
| [visibility](http://data.europa.eu/it6/visibility)      | §7.10 Concept                  | 1    | Settings for a dataset that determine who can access or view it. Options typically include 'Everyone', 'All my friends', 'Only me', or specific user-defined circles. | The recommended controlled vocabulary is the [Collection visibility](https://semiceu.github.io/MLDCAT-AP/releases/codelist/collection-visibility.html) code list. | No references available. |

### [Computer Infrastructure](http://data.europa.eu/it6/ComputerInfrastructure)

Definition

The architecture that represents the set of hardware, software, network resources and services required for the operation of an IT environment.

Reference

[AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII)

Properties

For this entity the following properties are defined: has hardware , has library , title .

| Property                                              | Range                                                                    | Card | Definition                                                | Usage | REF                                                                                                                                                                              |
| ----------------------------------------------------- | ------------------------------------------------------------------------ | ---- | --------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [has hardware](http://data.europa.eu/it6/hasHardware) | §7.23 Hardware | 1..* | The hardware associated with the computer infrastructure. |       | No references available.                                                                                                                                                         |
| [has library](http://data.europa.eu/it6/hasLibrary)   | §7.25 Library   | 1..* | The library associated with the computer infrastructure.  |       | No references available.                                                                                                                                                         |
| [title](http://purl.org/dc/terms/title)               | Literal   | 1    | The name assigned to the resource.                        |       | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) |

### [Concept](http://www.w3.org/2004/02/skos/core#Concept)

Definition

An idea or notion; a unit of thought.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Concept)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Cost Matrix](http://data.europa.eu/it6/CostMatrix)

Definition

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Data Quality](http://data.europa.eu/it6/DataQuality)

Definition

A measurable property of datasets, such as size, shape, statistical properties, benchmarks, and the presence of missing values.

Usage Note

Examples are size, shape, statistical properties, benchmarks, and the presence of missing values.

Subclass of

§7.29 Measure

Properties

For this entity the following properties are defined: description , identifier , title .

| Property                                            | Range                                                                  | Card | Definition                                  | Usage | REF                      |
| --------------------------------------------------- | ---------------------------------------------------------------------- | ---- | ------------------------------------------- | ----- | ------------------------ |
| [description](http://purl.org/dc/terms/description) | Literal | 0..1 | An explanation of the quality type.         |       | No references available. |
| [identifier](http://purl.org/dc/terms/identifier)   | Literal | 1    | An unambiguous identifier for the resource. |       | No references available. |
| [title](http://purl.org/dc/terms/title)             | Literal | 1    | The name assigned to the resource.          |       | No references available. |

### [Data Service](http://www.w3.org/ns/dcat#DataService)

Definition

A collection of operations that provides access to one or more datasets or data processing functions.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#DataService)

Subclass of

§7.5 Catalogued Resource

Properties

For this entity the following properties are defined: endpoint URL , serves dataset , serves model , title .

| Property                                                  | Range                                                                                              | Card | Definition                                                     | Usage                                                                     | REF                                                                                        |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [endpoint URL](http://www.w3.org/ns/dcat#endpointURL)     | §7.5 Catalogued Resource      | 1..* | The root location or primary endpoint of the service (an IRI). |                                                                           | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#DataService.endpointURL)   |
| [serves dataset](http://www.w3.org/ns/dcat#servesDataset) | §6.4 Dataset                             | 0..* | A collection of data that this data service can distribute.    |                                                                           | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#DataService.servesdataset) |
| [serves model](http://data.europa.eu/it6/servesModel)     | §6.8 Machine Learning Model | 0..* | A model that this data service can distribute.                 |                                                                           | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)             |
| [title](http://purl.org/dc/terms/title)                   | Literal                             | 1..* | A name given to the Data Service.                              | This property can be repeated for parallel language versions of the name. | [DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#DataService.title)         |

### [Document](http://xmlns.com/foaf/0.1/Document)

Definition

A textual resource intended for human consumption that contains information, e.g. a web page about a Dataset.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Document)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Engagement](http://data.europa.eu/it6/Engagement)

Definition

Properties

For this entity the following properties are defined: download , like .

| Property                                       | Range                                                                  | Card | Definition                                               | Usage | REF                      |
| ---------------------------------------------- | ---------------------------------------------------------------------- | ---- | -------------------------------------------------------- | ----- | ------------------------ |
| [download](http://data.europa.eu/it6/download) | integer | 0..1 | The number of downloads of the machine learning model.   |       | No references available. |
| [like](http://data.europa.eu/it6/like)         | integer | 0..1 | The number of likes the machine learning model received. |       | No references available. |

### [Environmental Impact](http://data.europa.eu/it6/EnvironmentalImpact)

Definition

The measurable effects of activities on the environment.

Reference

[AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII)

Properties

For this entity the following properties are defined: carbon emitted , measurement methodology , power consumption .

| Property                                                                    | Range                                                                  | Card | Definition                                            | Usage | REF                                                                                                                                                                                                   |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---- | ----------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [carbon emitted](http://data.europa.eu/it6/carbonEmitted)                   | Literal | 0..1 | The emitted carbon.                                   |       | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI)                                                                                                       |
| [measurement methodology](http://data.europa.eu/it6/measurementMethodology) | Literal | 0..* | The methodology with which the resource was measured. |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                                        |
| [power consumption](http://data.europa.eu/it6/powerConsumption)             | Literal | 0..1 | The consumed power.                                   |       | [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII) |

### [Estimation Procedure](http://data.europa.eu/it6/EstimationProcedure)

Definition

How models should be evaluated, typically by defining specific kinds of train- and test splits.

Subclass of

§7.29 Measure

Properties

For this entity the following properties are defined: description , has parameter , has split , identifier , title , type .

| Property                                                | Range                                                                      | Card | Definition                                           | Usage                                                                                                                                                                    | REF                      |
| ------------------------------------------------------- | -------------------------------------------------------------------------- | ---- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| [description](http://purl.org/dc/terms/description)     | Literal     | 1    | Description of the resource.                         |                                                                                                                                                                          | No references available. |
| [has parameter](http://data.europa.eu/it6/hasParameter) | §7.34 Parameter | 1..* | The configured setting.                              |                                                                                                                                                                          | No references available. |
| [has split](http://data.europa.eu/it6/hasSplit)         | §7.44 Split         | 0..* | The split that is used for the estimation procedure. |                                                                                                                                                                          | No references available. |
| [identifier](http://purl.org/dc/terms/identifier)       | Literal     | 1    | An unambiguous identifier for the resource.          |                                                                                                                                                                          | No references available. |
| [title](http://purl.org/dc/terms/title)                 | Literal     | 1    | The name assigned to the resource.                   |                                                                                                                                                                          | No references available. |
| [type](http://purl.org/dc/terms/type)                   | §7.10 Concept     | 1    | A classification of the resource.                    | The recommended controlled vocabulary is the [Estimation Procedure type](https://semiceu.github.io/MLDCAT-AP/releases/codelist/estimationprocedure-type.html) code list. | No references available. |

### [Evaluation](http://data.europa.eu/it6/Evaluation)

Definition

Properties

For this entity the following properties are defined: array data , fold , has flow , identifier , interval end , interval start , label , repeat , sample , sample size , stdev , title , value .

| Property                                                  | Range                                                                                   | Card | Definition                                                                                                                       | Usage | REF                      |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------------------ |
| [array data](http://data.europa.eu/it6/arrayData)         | Literal                  | 0..1 | For composite evaluation measures (e.g. per-class measures, confusion matrix), a string (JSON) representation of the evaluation. |       | No references available. |
| [fold](http://data.europa.eu/it6/fold)                    | Literal                  | 0..1 | The number of the fold in the inner cross-validation.                                                                            |       | No references available. |
| [has flow](http://data.europa.eu/it6/hasFlow)             | §7.21 Flow                        | 0..* |                                                                                                                                  |       | No references available. |
| [identifier](http://purl.org/dc/terms/identifier)         | Literal                  | 0..1 | An unambiguous identifier for the resource.                                                                                      |       | No references available. |
| [interval end](http://data.europa.eu/it6/intervalEnd)     | Temporal Literal | 0..1 |                                                                                                                                  |       | No references available. |
| [interval start](http://data.europa.eu/it6/intervalStart) | Temporal Literal | 0..1 |                                                                                                                                  |       | No references available. |
| [label](http://www.w3.org/2000/01/rdf-schema#label)       | Literal                  | 0..1 |                                                                                                                                  |       | No references available. |
| [repeat](http://data.europa.eu/it6/repeat)                | Literal                  | 0..1 | The number of the repeat in the outer cross-validation.                                                                          |       | No references available. |
| [sample](http://data.europa.eu/it6/sample)                | Literal                  | 0..1 |                                                                                                                                  |       | No references available. |
| [sample size](http://data.europa.eu/it6/sampleSize)       | Literal                  | 0..1 |                                                                                                                                  |       | No references available. |
| [stdev](http://data.europa.eu/it6/stdev)                  | Literal                  | 0..1 |                                                                                                                                  |       | No references available. |
| [title](http://purl.org/dc/terms/title)                   | Literal                  | 1    | The name assigned to the resource.                                                                                               |       | No references available. |
| [value](http://data.europa.eu/it6/value)                  | Literal                  | 0..1 | The result of evaluation.                                                                                                        |       | No references available. |

### [Evaluation Measure](http://data.europa.eu/it6/EvaluationMeasure)

Definition

A way to score the outputs of machine learning models (e.g. predictions).

Subclass of

§7.29 Measure

Properties

For this entity the following properties are defined: description , implementation , title , value , value bad , value good .

| Property                                                   | Range                                                                  | Card | Definition                         | Usage | REF                      |
| ---------------------------------------------------------- | ---------------------------------------------------------------------- | ---- | ---------------------------------- | ----- | ------------------------ |
| [description](http://purl.org/dc/terms/description)        | Literal | 0..1 |                                    |       | No references available. |
| [implementation](http://data.europa.eu/it6/implementation) | Literal | 0..1 |                                    |       | No references available. |
| [title](http://purl.org/dc/terms/title)                    | Literal | 1    | The name assigned to the resource. |       | No references available. |
| [value](http://data.europa.eu/it6/value)                   | Literal | 1    |                                    |       | No references available. |
| [value bad](http://data.europa.eu/it6/valueBad)            | Literal | 0..1 |                                    |       | No references available. |
| [value good](http://data.europa.eu/it6/valueGood)          | Literal | 0..1 |                                    |       | No references available. |

### [Feature](http://data.europa.eu/it6/Feature)

Definition

The attribute or column in which a distribution is structured.

Properties

For this entity the following properties are defined: description , title , type .

| Property                                            | Range                                                                  | Card | Definition                         | Usage                                                                                                                                           | REF                      |
| --------------------------------------------------- | ---------------------------------------------------------------------- | ---- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| [description](http://purl.org/dc/terms/description) | Literal | 0..1 | An explanation of the attribute.   |                                                                                                                                                 | No references available. |
| [title](http://purl.org/dc/terms/title)             | Literal | 1    | The name assigned to the resource. |                                                                                                                                                 | No references available. |
| [type](http://purl.org/dc/terms/type)               | §7.10 Concept | 1    | A classification of the resource.  | The recommended controlled vocabulary is the [Feature type](https://semiceu.github.io/MLDCAT-AP/releases/codelist/feature-type.html) code list. | No references available. |

### [Flow](http://data.europa.eu/it6/Flow)

Definition

A machine learning pipeline or neural architectures, or (untrained) machine learning models, such as in general.

Usage Note

Flows contain all the information necessary to build a model, including its exact structure and any software dependencies. Given a flow, supported machine learning libraries can reproduce the model exactly.

Properties

For this entity the following properties are defined: class name , custom name , description , external version , has dependency , has flow parameter , has uploader , identifier , keyword , status , title , uploaded , version .

| Property                                                         | Range                                                                                   | Card | Definition                                                                                                                             | Usage                                                                                                                                         | REF                      |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| [class name](http://data.europa.eu/it6/className)                | Literal                  | 0..1 |                                                                                                                                        |                                                                                                                                               | No references available. |
| [custom name](http://data.europa.eu/it6/customName)              | Literal                  | 0..1 |                                                                                                                                        |                                                                                                                                               | No references available. |
| [description](http://purl.org/dc/terms/description)              | Literal                  | 0..1 | Description of the resource.                                                                                                           |                                                                                                                                               | No references available. |
| [external version](http://data.europa.eu/it6/externalVersion)    | Literal                  | 0..1 | The version of the flow, as defined by the uploader, for reference.The version of the flow, as defined by the uploader, for reference. |                                                                                                                                               | No references available. |
| [has dependency](http://data.europa.eu/it6/hasDependency)        | §7.25 Library                  | 0..* | The libraries that a flow depends on.                                                                                                  |                                                                                                                                               | No references available. |
| [has flow parameter](http://data.europa.eu/it6/hasFlowParameter) | §7.22 Flow Parameter     | 0..* |                                                                                                                                        |                                                                                                                                               | No references available. |
| [has uploader](http://data.europa.eu/it6/hasUploader)            | §6.1 Agent                      | 0..1 | An entity responsible for uploading the resource.                                                                                      |                                                                                                                                               | No references available. |
| [identifier](http://purl.org/dc/terms/identifier)                | Literal                  | 0..1 | An unambiguous identifier for the resource.                                                                                            |                                                                                                                                               | No references available. |
| [keyword](http://www.w3.org/ns/dcat#keyword)                     | Literal                  | 0..* |                                                                                                                                        |                                                                                                                                               | No references available. |
| [status](http://www.w3.org/ns/adms#status)                       | §7.10 Concept                  | 1    |                                                                                                                                        | The recommended controlled vocabulary is the [Flow status](https://semiceu.github.io/MLDCAT-AP/releases/codelist/flow-status.html) code list. | No references available. |
| [title](http://purl.org/dc/terms/title)                          | Literal                  | 0..1 | The name assigned to the resource.                                                                                                     |                                                                                                                                               | No references available. |
| [uploaded](http://data.europa.eu/it6/uploaded)                   | Temporal Literal | 1    | The time that the flow was uploaded.                                                                                                   |                                                                                                                                               | No references available. |
| [version](http://data.europa.eu/it6/version)                     | Literal                  | 0..1 | The version of the flow.                                                                                                               |                                                                                                                                               | No references available. |

### [Flow Parameter](http://data.europa.eu/it6/FlowParameter)

Definition

Properties

For this entity the following properties are defined: default value , description , recommended range , title , type .

| Property                                                        | Range                                                                  | Card | Definition                          | Usage                                                                                                                                                        | REF                      |
| --------------------------------------------------------------- | ---------------------------------------------------------------------- | ---- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| [default value](http://data.europa.eu/it6/defaultValue)         | Literal | 0..1 | The default value of the parameter. |                                                                                                                                                              | No references available. |
| [description](http://purl.org/dc/terms/description)             | Literal | 0..1 | Description of the resource.        |                                                                                                                                                              | No references available. |
| [recommended range](http://data.europa.eu/it6/recommendedRange) | Literal | 0..1 |                                     |                                                                                                                                                              | No references available. |
| [title](http://purl.org/dc/terms/title)                         | Literal | 1    | The name assigned to the resource.  |                                                                                                                                                              | No references available. |
| [type](http://purl.org/dc/terms/type)                           | §7.10 Concept | 0..1 | The data type of the parameter.     | The recommended controlled vocabulary is the [Flow Parameter type](https://semiceu.github.io/MLDCAT-AP/releases/codelist/flowparameter-type.html) code list. | No references available. |

### [Hardware](http://data.europa.eu/it6/Hardware)

Definition

The tangible, physical devices and components that support the operation of software applications and services.

Reference

[AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII)

Properties

For this entity the following properties are defined: description , title .

| Property                                            | Range                                                                  | Card | Definition                         | Usage | REF                                                                            |
| --------------------------------------------------- | ---------------------------------------------------------------------- | ---- | ---------------------------------- | ----- | ------------------------------------------------------------------------------ |
| [description](http://purl.org/dc/terms/description) | Literal | 0..* | Description of the resource.       |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) |
| [title](http://purl.org/dc/terms/title)             | Literal | 1    | The name assigned to the resource. |       | No references available.                                                       |

### [Image Object](http://data.europa.eu/m8g/ImageObject)

Definition

A logo to describe / represent an entity.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Library](http://data.europa.eu/it6/Library)

Definition

A collection of code.

Reference

[AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII) , [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)

Properties

For this entity the following properties are defined: description , is executed by , licence , title , version .

| Property                                                 | Range                                                                                   | Card | Definition                                           | Usage | REF                                                                            |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---- | ---------------------------------------------------- | ----- | ------------------------------------------------------------------------------ |
| [description](http://purl.org/dc/terms/description)      | Literal                  | 0..* | Description of the resource.                         |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) |
| [is executed by](http://data.europa.eu/it6/isExecutedBy) | §6.6 File                        | 0..* | The library that is executed by this file.           |       | No references available.                                                       |
| [licence](http://purl.org/dc/terms/license)              | §7.26 Licence Document | 0..* | A licence under which the Library is made available. |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) |
| [title](http://purl.org/dc/terms/title)                  | Literal                  | 1    | The name assigned to the resource.                   |       | No references available.                                                       |
| [version](http://data.europa.eu/it6/version)             | Literal                  | 0..1 | Version of the resource.                             |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) |

### [Licence Document](http://purl.org/dc/terms/LicenseDocument)

Definition

A legal document giving official permission to do something with a resource.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#LicenceDocument)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Linguistic System](http://purl.org/dc/terms/LinguisticSystem)

Definition

A system of signs, symbols, sounds, gestures, or rules used in communication, e.g. a language.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Linguisticsystem)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Location](http://purl.org/dc/terms/Location)

Definition

A spatial region or named place.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Location)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Measure](http://data.europa.eu/it6/Measure)

Definition

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Media Type](http://purl.org/dc/terms/MediaType)

Definition

A file format or physical medium.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#MediaType)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Media Type Or Extent](http://purl.org/dc/terms/MediaTypeOrExtent)

Definition

A media type or extent.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#MediaTypeorExtent)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Modality](http://data.europa.eu/it6/Modality)

Definition

The distinct format of structure of input or output data.

Reference

[AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII) , [AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII)

Properties

For this entity the following properties are defined: classification , size .

| Property                                                   | Range                                                                  | Card | Definition                          | Usage | REF                                                                                                                                                                                                      |
| ---------------------------------------------------------- | ---------------------------------------------------------------------- | ---- | ----------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [classification](http://data.europa.eu/it6/classification) | §7.10 Concept | 0..* | The classification of the modality. |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI Act anx_XII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XII) , [AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII) |
| [size](http://data.europa.eu/it6/size)                     | Literal | 0..* | The maximum size of the modality.   |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                                           |

### [Output File Description](http://data.europa.eu/it6/OutputFileDescription)

Definition

The degree or extent of something, as determined by measurement or calculation.

Properties

For this entity the following properties are defined: id , title , url .

| Property                                  | Range                                                                                         | Card | Definition                                  | Usage | REF                      |
| ----------------------------------------- | --------------------------------------------------------------------------------------------- | ---- | ------------------------------------------- | ----- | ------------------------ |
| [id](http://purl.org/dc/terms/identifier) | Literal                        | 1    | An unambiguous identifier for the resource. |       | No references available. |
| [title](http://purl.org/dc/terms/title)   | Literal                        | 1    | The name assigned to the resource.          |       | No references available. |
| [url](http://data.europa.eu/it6/url)      | §7.5 Catalogued Resource | 1    |                                             |       | No references available. |

### [Parameter](http://data.europa.eu/it6/Parameter)

Definition

The various configuration settings that are specified prior to and during training a model.

Properties

For this entity the following properties are defined: component , name , value .

| Property                                         | Range                                                                  | Card | Definition                         | Usage | REF                      |
| ------------------------------------------------ | ---------------------------------------------------------------------- | ---- | ---------------------------------- | ----- | ------------------------ |
| [component](http://data.europa.eu/it6/component) | Literal | 0..1 |                                    |       | No references available. |
| [name](http://purl.org/dc/terms/title)           | Literal | 1    | The name assigned to the resource. |       | No references available. |
| [value](http://data.europa.eu/it6/value)         | Literal | 1    |                                    |       | No references available. |

### [Policy](http://www.w3.org/ns/odrl/2/Policy)

Definition

A non-empty group of Permissions and/or Prohibitions.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Policy)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Prediction](http://data.europa.eu/it6/Prediction)

Definition

Properties

For this entity the following properties are defined: format , has prediction feature .

| Property                                                                 | Range                                                                                       | Card | Definition | Usage | REF                      |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ---- | ---------- | ----- | ------------------------ |
| [format](http://purl.org/dc/terms/format)                                | §7.10 Concept                      | 1    |            |       | No references available. |
| [has prediction feature](http://data.europa.eu/it6/hasPredictionFeature) | §7.37 Prediction Feature | 1..* |            |       | No references available. |

### [Prediction Feature](http://data.europa.eu/it6/PredictionFeature)

Definition

Properties

For this entity the following properties are defined: title , type .

| Property                                | Range                                                                  | Card | Definition                         | Usage                                                                                                                                                                | REF                      |
| --------------------------------------- | ---------------------------------------------------------------------- | ---- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| [title](http://purl.org/dc/terms/title) | Literal | 1    | The name assigned to the resource. |                                                                                                                                                                      | No references available. |
| [type](http://purl.org/dc/terms/type)   | §7.10 Concept | 1    | A classification of the resource.  | The recommended controlled vocabulary is the [Prediction Feature type](https://semiceu.github.io/MLDCAT-AP/releases/codelist/predictionfeature-type.html) code list. | No references available. |

### [Quality Measurement Dataset](http://www.w3.org/ns/dqv#QualityMeasurementDataset)

Definition

A dataset of quality measurements, evaluations of one or more datasets (or dataset distributions) against specific quality metrics.

Properties

For this entity the following properties are defined: evaluation engine id , identifier .

| Property                                                           | Range                                                                  | Card | Definition                                          | Usage | REF                      |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------- | ---- | --------------------------------------------------- | ----- | ------------------------ |
| [evaluation engine id](http://data.europa.eu/it6/evaluationEngine) | Literal | 0..1 | The engine responsible for extracting the features. |       | No references available. |
| [identifier](http://purl.org/dc/terms/identifier)                  | Literal | 1    | An unambiguous identifier for the resource.         |       | No references available. |

### [Repository](https://linkedpaperswithcode.com/class/repository)

Definition

A repository is a place where code and data is stored.

Reference

[LPWC [A]](https://linkedpaperswithcode.com/resource/?uri=https%3A%2F%2Flinkedpaperswithcode.com%2Fclass%2Frepository&ontology=https%3A%2F%2Flinkedpaperswithcode.com%2Fontology%23)

Properties

For this entity the following properties are defined: has file , name .

| Property                                      | Range                                                                  | Card | Definition                         | Usage | REF                      |
| --------------------------------------------- | ---------------------------------------------------------------------- | ---- | ---------------------------------- | ----- | ------------------------ |
| [has file](http://data.europa.eu/it6/hasFile) | §6.6 File       | 0..* |                                    |       | No references available. |
| [name](http://purl.org/dc/terms/title)        | Literal | 1    | The name assigned to the resource. |       | No references available. |

### [Resource](http://www.w3.org/2000/01/rdf-schema#Resource)

Definition

Anything described by RDF.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Resource)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Rights Statement](http://purl.org/dc/terms/RightsStatement)

Definition

A statement about the intellectual property rights (IPR) held in or over a resource, a legal document giving official permission to do something with a resource, or a statement about access rights.

Reference

[DCAT-AP [A]](https://semiceu.github.io/DCAT-AP/releases/3.0.1/#Rightsstatement)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Run](http://data.europa.eu/it6/Run)

Definition

An evaluation of machine learning models (flows) trained on a given task.

Usage Note

Runs can be created and shared automatically from supported machine learning libraries. They contain the exact hyperparameters used, all detailed results, and potentially the trained models.

Properties

For this entity the following properties are defined: error message , executes , has evaluation , has flow , has inferencing impact , has output file description , has output file prediction , has parameter , has task , has training impact , has uploader , identifier , keyword , run details , setup Id , setup string , training time .

| Property                                                                          | Range                                                                                                | Card | Definition                                                | Usage | REF                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- | --------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [error message](http://data.europa.eu/it6/errorMessage)                           | Literal                               | 0..1 |                                                           |       | No references available.                                                                                                                                                                                 |
| [executes](http://www.w3.org/ns/mls#realizes)                                     | §6.2 Algorithm                           | 1..* | The Algorithm executed by the run.                        |       | No references available.                                                                                                                                                                                 |
| [has evaluation](http://data.europa.eu/it6/hasEvaluation)                         | §7.18 Evaluation                         | 0..* |                                                           |       | No references available.                                                                                                                                                                                 |
| [has flow](http://data.europa.eu/it6/hasFlow)                                     | §7.21 Flow                                     | 1    | The reference to the flow used in this run.               |       | No references available.                                                                                                                                                                                 |
| [has inferencing impact](http://data.europa.eu/it6/hasInferencingImpact)          | §7.16 Environmental Impact      | 0..* | The impact of inferencing the model.                      |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                                           |
| [has output file description](http://data.europa.eu/it6/hasOutputFileDescription) | §7.33 Output File Description | 1    |                                                           |       | No references available.                                                                                                                                                                                 |
| [has output file prediction](http://data.europa.eu/it6/hasOutputFilePrediction)   | §6.6 File                                     | 1    |                                                           |       | No references available.                                                                                                                                                                                 |
| [has parameter](http://data.europa.eu/it6/hasParameter)                           | §7.34 Parameter                           | 0..* | The configured setting.                                   |       | No references available.                                                                                                                                                                                 |
| [has task](http://data.europa.eu/it6/hasTask)                                     | §7.46 Task                                     | 0..1 |                                                           |       | No references available.                                                                                                                                                                                 |
| [has training impact](http://data.europa.eu/it6/hasTrainingImpact)                | §7.16 Environmental Impact      | 0..* | Measured or estimated amount of energy used for training. |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) , [AI Act anx_XI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XI) , [AI Act anx_XIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689#anx_XIII) |
| [has uploader](http://data.europa.eu/it6/hasUploader)                             | §6.1 Agent                                   | 0..1 | An entity responsible for uploading the resource.         |       | No references available.                                                                                                                                                                                 |
| [identifier](http://purl.org/dc/terms/identifier)                                 | Literal                               | 0..1 | An unambiguous identifier for the resource.               |       | No references available.                                                                                                                                                                                 |
| [keyword](http://www.w3.org/ns/dcat#keyword)                                      | Literal                               | 0..* |                                                           |       | No references available.                                                                                                                                                                                 |
| [run details](http://data.europa.eu/it6/runDetails)                               | Literal                               | 0..1 |                                                           |       | No references available.                                                                                                                                                                                 |
| [setup Id](http://data.europa.eu/it6/setupId)                                     | Literal                               | 0..1 |                                                           |       | No references available.                                                                                                                                                                                 |
| [setup string](http://data.europa.eu/it6/setupString)                             | Literal                               | 0..1 |                                                           |       | No references available.                                                                                                                                                                                 |
| [training time](http://data.europa.eu/it6/trainingTime)                           | Temporal Literal              | 0..* | A description of the training time.                       |       | [AI CoP](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)                                                                                                                           |

### [Run Collection](http://data.europa.eu/it6/RunCollection)

Definition

A group of runs to easily refer to them and share them with others.

Subclass of

§7.8 Collection

Properties

For this entity the following properties are defined: has run .

| Property                                    | Range                                                          | Card | Definition | Usage | REF                      |
| ------------------------------------------- | -------------------------------------------------------------- | ---- | ---------- | ----- | ------------------------ |
| [has run](http://data.europa.eu/it6/hasRun) | §7.42 Run | 1..* |            |       | No references available. |

### [Split](http://data.europa.eu/it6/Split)

Definition

Represents a partition of a distribution of data.

Properties

For this entity the following properties are defined: description , id , is applied to , title , type .

| Property                                               | Range                                                                            | Card | Definition                                  | Usage | REF                      |
| ------------------------------------------------------ | -------------------------------------------------------------------------------- | ---- | ------------------------------------------- | ----- | ------------------------ |
| [description](http://purl.org/dc/terms/description)    | Literal           | 0..1 | An explanation of the attribute.            |       | No references available. |
| [id](http://purl.org/dc/terms/identifier)              | Literal           | 1    | An unambiguous identifier for the resource. |       | No references available. |
| [is applied to](http://data.europa.eu/it6/isAppliedTo) | §6.5 Distribution | 1..* |                                             |       | No references available. |
| [title](http://purl.org/dc/terms/title)                | Literal           | 1    | The name assigned to the resource.          |       | No references available. |
| [type](http://purl.org/dc/terms/type)                  | §7.10 Concept           | 0..1 | A classification of the resource.           |       | No references available. |

### [Standard](http://purl.org/dc/terms/Standard)

Definition

A standard or other specification to which a resource conforms.

Usage Note

It could be used, for example, to point directly to a Croissant file. In alignment with [STATDCAT-AP #25](https://github.com/SEMICeu/StatDCAT-AP/issues/25)

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Task](http://data.europa.eu/it6/Task)

Definition

A task defines specific problems to be solved using a given dataset.

Usage Note

Tasks specify train and test sets, which target feature(s) to predict for supervised problems, and possibly which evaluation measure to optimize. They make the problem reproducible and machine-readable.

Properties

For this entity the following properties are defined: has cost matrix , has estimation procedure , has evaluation measure , has output , has task type , id , keyword , source data , target feature , title .

| Property                                                                     | Range                                                                                           | Card | Definition                                  | Usage                                                                                                                                     | REF                      |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| [has cost matrix](http://data.europa.eu/it6/hasCostMatrix)                   | §7.11 Cost Matrix                   | 0..1 |                                             |                                                                                                                                           | No references available. |
| [has estimation procedure](http://data.europa.eu/it6/hasEstimationProcedure) | §7.17 Estimation Procedure | 1..* |                                             |                                                                                                                                           | No references available. |
| [has evaluation measure](http://data.europa.eu/it6/hasEvaluationMeasure)     | §7.19 Evaluation Measure     | 1..* |                                             |                                                                                                                                           | No references available. |
| [has output](http://data.europa.eu/it6/hasOutput)                            | §7.36 Prediction                    | 1    |                                             |                                                                                                                                           | No references available. |
| [has task type](http://data.europa.eu/it6/hasTaskType)                       | §7.48 Task Type                       | 1    |                                             | The recommended controlled vocabulary is the [Task type](https://semiceu.github.io/MLDCAT-AP/releases/codelist/task-type.html) code list. | No references available. |
| [id](http://purl.org/dc/terms/identifier)                                    | Literal                          | 0..1 | An unambiguous identifier for the resource. |                                                                                                                                           | No references available. |
| [keyword](http://www.w3.org/ns/dcat#keyword)                                 | Literal                          | 0..* | A keyword or tag describing the resource.   |                                                                                                                                           | No references available. |
| [source data](http://data.europa.eu/it6/sourceData)                          | §6.4 Dataset                          | 1..* |                                             |                                                                                                                                           | No references available. |
| [target feature](http://data.europa.eu/it6/targetFeature)                    | §7.20 Feature                          | 1..* |                                             |                                                                                                                                           | No references available. |
| [title](http://purl.org/dc/terms/title)                                      | Literal                          | 1    | The name assigned to the resource.          |                                                                                                                                           | No references available. |

### [Task Collection](http://data.europa.eu/it6/TaskCollection)

Definition

A group of tasks to easily refer to them and share them with others.

Subclass of

§7.8 Collection

Properties

For this entity the following properties are defined: has task .

| Property                                      | Range                                                            | Card | Definition | Usage | REF                      |
| --------------------------------------------- | ---------------------------------------------------------------- | ---- | ---------- | ----- | ------------------------ |
| [has task](http://data.europa.eu/it6/hasTask) | §7.46 Task | 1..* |            |       | No references available. |

### [Task Type](http://data.europa.eu/it6/TaskType)

Definition

Properties

For this entity the following properties are defined: description , id , title .

| Property                                                      | Range                                                                  | Card | Definition                                  | Usage | REF                      |
| ------------------------------------------------------------- | ---------------------------------------------------------------------- | ---- | ------------------------------------------- | ----- | ------------------------ |
| [description](http://www.w3.org/2004/02/skos/core#definition) | Literal | 1    |                                             |       | No references available. |
| [id](http://www.w3.org/2004/02/skos/core#notation)            | Literal | 1    | An unambiguous identifier for the resource. |       | No references available. |
| [title](http://www.w3.org/2004/02/skos/core#prefLabel)        | Literal | 1    | The name assigned to the resource.          |       | No references available. |

## Datatypes

The following datatypes are used within this specification.

| Class                                                                     | Definition                                                                                                                                                                                               |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [hexBinary](http://www.w3.org/2001/XMLSchema#hexBinary)                   | Hex-encoded binary data. The ·value space· of hexBinary is the set of finite-length sequences of binary octets.                                                                                          |
| [integer](http://www.w3.org/2001/XMLSchema#integer)                       | Integer is derived from decimal by fixing the value of fractionDigits to be 0 and disallowing the trailing decimal point. This results in the standard mathematical concept of the integer numbers.      |
| [Literal](http://www.w3.org/2000/01/rdf-schema#Literal)                   | A literal value such as a string or integer; Literals may be typed, e.g. as a date according to xsd:date. Literals that contain human-readable text have an optional language tag as defined by BCP 47[rfc5646]. |
| [nonNegativeInteger](http://www.w3.org/2001/XMLSchema#nonNegativeInteger) | Number derived from integer by setting the value of minInclusive to be 0.                                                                                                                                |
| [Temporal Literal](http://www.w3.org/2000/01/rdf-schema#Literal)          | rdfs:Literal encoded using the relevant [ISO8601] Date and Time compliant string and typed using the appropriate XML Schema datatype (xsd:gYear, xsd:gYearMonth, xsd:date, or xsd:dateTime).           |

## Examples

### Example [Credit-g](https://www.openml.org/search?type=data&status=active&id=31&sort=runs) Dataset on OpenML

### Example [Bloom-7b1](https://huggingface.co/bigscience/bloomz-7b1) Machine Learning Model on HuggingFace

### Example [Apertus](https://huggingface.co/swiss-ai/Apertus-8B-2509) Machine Learning Model on HuggingFace

### Example [Thermal Bridges](https://dashboard.cloud.ai4eosc.eu/marketplace/modules/thermal-bridges-rooftops-detector) Machine Learning Model on EOSC

## Controlled Vocabularies

### Requirements for controlled vocabularies

The following is a list of requirements that were identified for the controlled vocabularies to be recommended in this Application Profile.
Controlled vocabularies SHOULD:

- Be published under an open licence.
- Be operated and/or maintained by an institution of the European Union, by a recognised standards organisation or another trusted organisation.
- Be properly documented.
- Have labels in multiple languages, ideally in all official languages of the European Union.
- Contain a relatively small number of terms (e.g. 10-25) that are general enough to enable a wide range of resources to be classified.
- Have terms that are identified by URIs with each URI resolving to documentation about the term.
- Have associated persistence and versioning policies.

These criteria do not intend to define a set of requirements for controlled vocabularies in general; they are only intended to be used for the selection of the controlled vocabularies that are proposed for this Application Profile.

### Expected usage of controlled vocabularies

To increase the interoperability, the value spaces of properties can be further harmonised using shared controlled vocabularies.
This kind of restriction may be subject to a varying interpretation on what the expected usage of a controlled vocabulary is.
To ensure a common interpretation the following expectations are defined:

- The property MUST use as range values codes from {codelist}
  This expectation results in that the value space is closed under the codelist.
Validation systems SHOULD produce errors.
All profiles in the ecosystem MUST avoid conflicts by creating subproperties.

- The property MUST have at least one value from {codelist}
  This expectation makes the value space minimally constrained.
Validation systems SHOULD produce warnings.
All profiles in the ecosystem MUST adopt this interpretation in case they want to restrict the value space.
Adopting the former expectation will lead to cross-profile interpretations challenges.

- The property IS RECOMMENDED to use as range values codes from {codelist}
  The value space is closed under the codelist, but other values are tolerated.
Recommending means expressing a strong preference.
To make this stronger direction towards harmonisation visible in the data exchanges, validation systems SHOULD produce warnings.

- The property MAY use as range values codes from {codelist}
  The value space is closed under the codelist, but other values are accepted.
  This expectation is more a hint to be used.
  As there is no obligation nor strongly suggestion expressed here, the use of other codelists is valid is all cases.
  Therefore validation systems MAY produce warnings but users are free to ignore them.
  No validation in this case is also acceptable.

The first two (and preferably also the others) SHOULD only be used for requirements that can be verified by a machine.
If the validation can only be realised with the involvement of humans, then a less strong requirement (RECOMMMENDED or MAY) is used,
even if the intention is to be very strict.
This is to ensure that the provided SHACL representations correspond closely to all use cases possible.
Stronger enforcements are left for implementations as they have control on actual data exchange.

### Controlled vocabularies to be used

The tables below show the usage of the codelists with the expected qualification.

#### Properties with controlled vocabularies that MUST be used for the listed properties

| Property URI   | Used for Class                                                                                                                                           | Vocabulary name                                                                                              | Usage note                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| dcat:mediaType | §6.5 Distribution                                                                         | [IANA Media Types](http://www.iana.org/assignments/media-types/media-types.xhtml)                            |                                                                                             |
| dct:format     | §6.5 Distribution                                                                         | [EU Vocabularies File Type Named Authority List](http://publications.europa.eu/resource/authority/file-type) |                                                                                             |
| dct:language   | §6.4 Dataset, §6.5 Distribution | [EU Vocabularies Languages Named Authority List](http://publications.europa.eu/resource/authority/language)  |                                                                                             |
| spdx:algorithm | §7.6 Checksum                                                                                 | [Checksum algorithm members](https://spdx.org/rdf/terms/#d4e2129)                                            | The members listed are considered a controlled vocabulary of supported checksum algorithms. |

#### Properties with AT LEAST 1 value from the controlled vocabularies

| Property URI | Used for Class                                                         | Vocabulary name                                                                         | Usage note                                                                              |
| ------------ | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| dcat:theme   | §6.4 Dataset | [Dataset Theme Vocabulary](http://publications.europa.eu/resource/authority/data-theme) | The values to be used for this property are the URIs of the concepts in the vocabulary. |

#### Properties with a RECOMMENDED use of controlled vocabularies

| Property URI     | Used for Class                                                         | Vocabulary name                                                                                     | Usage note                                                           |
| ---------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| dct:accessRights | §6.4 Dataset | [Access Rights Named Authority List](http://publications.europa.eu/resource/authority/access-right) | Use one of the following values (:PUBLIC, :RESTRICTED, :NON_PUBLIC). |

#### Properties with MAY use a controlled vocabularies

| Property URI    | Used for Class                                                                                                                                                                                           | Vocabulary name                                                                                                                                                                                          | Usage note                                                                                                                                                                                               |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adms:status     | §6.4 Dataset, §7.21 Flow                                                                 | [Dataset status](https://semiceu.github.io/MLDCAT-AP/releases/codelist/dataset-status.html), [Flow status](https://semiceu.github.io/MLDCAT-AP/releases/codelist/flow-status.html)                       | This list of terms provide status of datasets and flows.                                                                                                                                                 |
| dct:publisher   | §6.3 Catalogue, §6.4 Dataset                                                       | [EU Vocabularies Corporate bodies Named Authority List](http://publications.europa.eu/resource/authority/corporate-body)                                                                                 | The Corporate bodies NAL must be used for European institutions and a small set of international organisations. In case of other types of organisations, national, regional or local vocabularies should be used. |
| dct:type        | §6.4 Dataset, §7.17 Estimation Procedure, §7.20 Feature, §7.22 Flow Parameter, §7.37 Prediction Feature | [Dataset-type authority table](http://publications.europa.eu/resource/authority/dataset-type), [Estimation Procedure type](https://semiceu.github.io/MLDCAT-AP/releases/codelist/estimationprocedure-type.html), [Flow Parameter type](https://semiceu.github.io/MLDCAT-AP/releases/codelist/flowparameter-type.html), [Prediction Feature type](https://semiceu.github.io/MLDCAT-AP/releases/codelist/predictionfeature-type.html) | This list of terms provide types of datasets, estimation procedures, features, flow parameters, prediction features.                                                                                     |
| dpv:hasData     | §6.5 Distribution                                                                                                                         | [Distribution data categories](https://w3id.org/dpv#vocab-personal-data)                                                                                                                                 | This list of terms provide types of data included in a distribution.                                                                                                                                     |
| it6:hasTaskType | §7.46 Task                                                                                                                                         | [Task type](https://semiceu.github.io/MLDCAT-AP/releases/codelist/task-type.html)                                                                                                                        | This list of terms provide types of tasks.                                                                                                                                                               |
| it6:visibility  | §6.4 Dataset, §7.8 Collection                                                     | [Dataset visibility](https://semiceu.github.io/MLDCAT-AP/releases/codelist/dataset-visibility.html), [Collection visibility](https://semiceu.github.io/MLDCAT-AP/releases/codelist/collection-visibility.html) | This list of terms provide visibility of datasets and collections.                                                                                                                                       |

### Other controlled vocabularies

In addition to the proposed common controlled vocabularies, which are mandatory to ensure minimal interoperability, implementers are encouraged to publish and to use further region or domain-specific vocabularies that are available online. While those may not be recognised by general implementations of the Application Profile, they may serve to increase interoperability across applications in the same region or domain. Examples are the full set of concepts in [EuroVoc](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc), [the CERIF standard vocabularies](https://dspacecris.eurocris.org/), [the Dewey Decimal Classification](http://www.oclc.org/content/dam/oclc/dewey/versions/print/intro.pdf) and numerous other schemes.

## Usage Guidelines

## Support for implementation

The following section provides support for implementing the MLDCAT-AP.

### JSON-LD context file

One common technical question is the format in which the data is being exchanged.
For conformance with the MLDCAT-AP, it is not mandatory that this happens in an RDF serialisation, but the exchanged format SHOULD be unambiguously transformable into RDF.
For the format JSON, a popular format to exchange data between systems, SEMIC provides a [JSON-LD context file](https://semiceu.github.io/MLDCAT-AP/releases/3.1.0/context/mldcat-ap.jsonld).
JSON-LD is a W3C Recommendation [json-ld11] that provided a standard approach to interpret JSON structures as RDF.
The provided JSON-LD context file can be used by implementers.
This JSON-LD context is not normative, i.e. other JSON-LD contexts are allowed.

The JSON-LD context file is downloadable [here](https://semiceu.github.io/MLDCAT-AP/releases/3.1.0/context/mldcat-ap.jsonld).

### Validation

To verify if the data is (technically) conformant to the MLDCAT-AP, the exchanged data can be validated using the provided SHACL shapes.
SHACL is a W3C Recommendation to express constraints on an RDF knowledge graph.

To support the check whether or not a catalogue satisfies the expressed constraints in this Application Profile, the constraints in this specification are expressed using SHACL [shacl].
Each constraint in this specification that could be converted into a SHACL expression has been included.
As such this collection of SHACL expressions can be used to build a validation check for data.

It is up to the implementers to define the validation they expect.
Each implementation happens within a context, and that context is beyond the SHACL expressions here.

The shapes can be found [here](https://semiceu.github.io/MLDCAT-AP/releases/3.1.0/shacl/mldcat-ap-SHACL.ttl).

The Interoperability Test Bed (ITB) provides a [SEMIC SHACL validation service](https://www.itb.ec.europa.eu/shacl/semic-shacl/upload) where it is possible to validate for MLDCAT-AP reusing the linked shapes.
There are 4 types of validation for this version:

- **3.1.0**: to validate against the data model version 3.1.0
- **3.1.0 for AI Office**: to validate against the data model + the [transparency requirements](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai#ecl-inpage-the-3-chapters-of-the-code) for the AI Office coming for the AI Code Of Practice
- **3.1.0 for Downstream Providers**: to validate against the data model + the [transparency requirements](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai#ecl-inpage-the-3-chapters-of-the-code) for the Downstream providers coming for the AI Code Of Practice
- **3.1.0 for National Competent Authority**: to validate against the data model + the [transparency requirements](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai#ecl-inpage-the-3-chapters-of-the-code) for the National Competent Authorities coming for the AI Code Of Practice

The additional shapes can be found in the [SEMIC SHACL validator](https://github.com/SEMICeu/semic-shacl-validator/tree/main/resources/semic-shacl) repository.

The examples in this specification can be validated via the [ITB REST API](https://www.itb.ec.europa.eu/shacl/swagger-ui/index.html).

### UML representation

The UML representation from which the MLDCAT-AP has been build is available [here](https://github.com/SEMICeu/MLDCAT-AP/tree/main/releases/3.1.0/uml).

## Governance

### Versioning governance

All specifications produced in SEMIC will follow the versioning rule described by the SEMIC Style Guide rule[PC-R3](https://semiceu.github.io/style-guide/1.0.0/gc-publication-conventions.html#sec:pc-r3).
In case a SEMIC asset is deprecated the asset will remain available through its PURI.

The serialisation will have:

- a dct:isReplacedBy referencing the new assets used instead and
- an adms:status indicating its deprecated [status](http://publications.europa.eu/resource/authority/concept-status/DEPRECATED).

### Governance requirements for re-used assets

In order to adhere to the SEMIC Style Guide rule [GC-R2](https://semiceu.github.io/style-guide/1.0.0/gc-general-conventions.html#sec:gc-r2) a specification should have quality and governance standards for the assets that are being reused.

In order for an asset to be considered for reuse within a SEMIC specification it can be requested by a community member or it requires to adhere to the following requirements:

- The asset is part of a recommendation by a major standards body or an EU institution.
- The asset is actively being maintained.

After being taken into consideration the asset will be validated in three steps:

- Syntax validation will be performed on the relevant artefacts.
- Constraint validation will be performed on the relevant artefacts.
- The PURI will be validated.

Once considered and validated an asset can be adopted if it is approved by the community.

### Lexicalisation rules

In order to adhere to the SEMIC Style Guide rule [SC-R3](https://semiceu.github.io/style-guide/1.0.0/gc-semantic-conventions.html#sec:sc-r3) a specification requires formal lexicalisation rules.
The Style Guide proposes two options either by using RDFS or SKOS lexicalisation.

SEMIC uses and will use the RDFS lexicalisation for all of its specifications. More specifically:

- rdfs:label is used to provide a human-readable version of a resource's name.
- The usage of certain resource can be clarified in a skos:usageNote.

## Mappings

- A mapping towards Croissant can be found [here](https://github.com/SEMICeu/Semantic-Mappings/tree/main/MLDCAT-AP/ML%20Croissant)
- A mapping towards FAIR4ML can be found [here](https://github.com/SEMICeu/Semantic-Mappings/tree/main/MLDCAT-AP/FAIR4ML)
- A mapping towards DPV can be found [here](https://github.com/SEMICeu/Semantic-Mappings/tree/main/MLDCAT-AP/DPV)

## Quick Reference of Classes and Properties

This section provides a condensed tabular overview of the mentioned classes and properties in this specification.
The properties are indicated as mandatory, recommended, optional and deprecated. These terms have the following meaning.

- Mandatory property: a receiver MUST be able to process the information for that property; a sender MUST provide the information for that property.
- Recommended property: a receiver MUST be able to process the information for that property; a sender SHOULD provide the information for that property if it is available.
- Optional property: a receiver MUST be able to process the information for that property; a sender MAY provide the information for that property but is not obliged to do so.
- Deprecated property: a receiver SHOULD be able to process information about instances of that property; a sender SHOULD NOT provide the information about instances of that property.

| Class                                                                                                        | Class IRI                                          | Property Type | Property                                                                                                                          | Property IRI                                            |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| §7.1 Activity                                     | http://www.w3.org/ns/prov#Activity                 |               |                                                                                                                                   |                                                         |
| §6.1 Agent                                           | http://xmlns.com/foaf/0.1/Agent                    | Mandatory     | name                                                            | http://xmlns.com/foaf/0.1/name                          |
| §6.1 Agent                                           | http://xmlns.com/foaf/0.1/Agent                    |               | acted on behalf of                                   | http://www.w3.org/ns/prov#actedOnBehalfOf               |
| §6.2 Algorithm                                   | http://www.w3.org/ns/mls#Algorithm                 | Optional      | has algorithm type                              | http://w3id.org/mlso/hasAlgorithmType                   |
| §6.2 Algorithm                                   | http://www.w3.org/ns/mls#Algorithm                 | Optional      | has learning method type                   | http://w3id.org/mlso/hasLearningMethodType              |
| §7.2 Benchmark                                   | http://data.europa.eu/it6/Benchmark                | Mandatory     | title                                                      | http://purl.org/dc/terms/title                          |
| §7.3 Bibliographic Reference        | http://purl.org/spar/biro/BibliographicReference   | Mandatory     | bibliographic citation        | http://purl.org/dc/terms/bibliographicCitation          |
| §7.3 Bibliographic Reference        | http://purl.org/spar/biro/BibliographicReference   | Mandatory     | format                                       | http://purl.org/dc/terms/format                         |
| §7.3 Bibliographic Reference        | http://purl.org/spar/biro/BibliographicReference   | Optional      | references                               | http://purl.org/dc/terms/references                     |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Mandatory     | description                                          | http://purl.org/dc/terms/description                    |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Mandatory     | publisher                                              | http://purl.org/dc/terms/publisher                      |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Mandatory     | title                                                      | http://purl.org/dc/terms/title                          |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | creator                                                  | http://purl.org/dc/terms/creator                        |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | dataset                                                  | http://www.w3.org/ns/dcat#dataset                       |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | homepage                                                | http://xmlns.com/foaf/0.1/homepage                      |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | identifier                                            | http://purl.org/dc/terms/identifier                     |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | keyword                                                  | http://www.w3.org/ns/dcat#keyword                       |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | licence                                                  | http://purl.org/dc/terms/license                        |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | modification date                               | http://purl.org/dc/terms/modified                       |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | record                                                    | http://www.w3.org/ns/dcat#record                        |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | release date                                         | http://purl.org/dc/terms/issued                         |
| §6.3 Catalogue                                   | http://www.w3.org/ns/dcat#Catalog                  | Optional      | service                                                  | http://www.w3.org/ns/dcat#service                       |
| §7.4 Catalogue Record                      | http://www.w3.org/ns/dcat#CatalogRecord            | Optional      | description                                    | http://purl.org/dc/terms/description                    |
| §7.4 Catalogue Record                      | http://www.w3.org/ns/dcat#CatalogRecord            | Optional      | description version                     | http://data.europa.eu/it6/descriptionVersion            |
| §7.4 Catalogue Record                      | http://www.w3.org/ns/dcat#CatalogRecord            | Optional      | modification date                         | http://purl.org/dc/terms/modified                       |
| §7.4 Catalogue Record                      | http://www.w3.org/ns/dcat#CatalogRecord            | Optional      | primary topic                                 | http://xmlns.com/foaf/0.1/primaryTopic                  |
| §7.5 Catalogued Resource                | http://www.w3.org/ns/dcat#Resource                 |               |                                                                                                                                   |                                                         |
| §7.6 Checksum                                     | http://spdx.org/rdf/terms#Checksum                 | Mandatory     | algorithm                                               | http://spdx.org/rdf/terms#algorithm                     |
| §7.6 Checksum                                     | http://spdx.org/rdf/terms#Checksum                 | Mandatory     | checksum value                                      | http://spdx.org/rdf/terms#checksumValue                 |
| §7.7 Checksum Algorithm                  | http://spdx.org/rdf/terms#ChecksumAlgorithm        |               |                                                                                                                                   |                                                         |
| §7.8 Collection                                 | http://data.europa.eu/it6/Collection               | Mandatory     | creation date                                      | http://data.europa.eu/it6/creationDate                  |
| §7.8 Collection                                 | http://data.europa.eu/it6/Collection               | Mandatory     | has uploader                                        | http://data.europa.eu/it6/hasUploader                   |
| §7.8 Collection                                 | http://data.europa.eu/it6/Collection               | Mandatory     | identifier                                           | http://purl.org/dc/terms/identifier                     |
| §7.8 Collection                                 | http://data.europa.eu/it6/Collection               | Mandatory     | title                                                     | http://purl.org/dc/terms/title                          |
| §7.8 Collection                                 | http://data.europa.eu/it6/Collection               | Mandatory     | visibility                                           | http://data.europa.eu/it6/visibility                    |
| §7.8 Collection                                 | http://data.europa.eu/it6/Collection               | Optional      | description                                         | http://purl.org/dc/terms/description                    |
| §7.9 Computer Infrastructure        | http://data.europa.eu/it6/ComputerInfrastructure   | Mandatory     | has hardware                            | http://data.europa.eu/it6/hasHardware                   |
| §7.9 Computer Infrastructure        | http://data.europa.eu/it6/ComputerInfrastructure   | Mandatory     | has library                              | http://data.europa.eu/it6/hasLibrary                    |
| §7.9 Computer Infrastructure        | http://data.europa.eu/it6/ComputerInfrastructure   | Mandatory     | title                                         | http://purl.org/dc/terms/title                          |
| §7.10 Concept                                       | http://www.w3.org/2004/02/skos/core#Concept        |               |                                                                                                                                   |                                                         |
| §7.11 Cost Matrix                                | http://data.europa.eu/it6/CostMatrix               |               |                                                                                                                                   |                                                         |
| §7.12 Data Quality                              | http://data.europa.eu/it6/DataQuality              | Mandatory     | identifier                                          | http://purl.org/dc/terms/identifier                     |
| §7.12 Data Quality                              | http://data.europa.eu/it6/DataQuality              | Mandatory     | title                                                    | http://purl.org/dc/terms/title                          |
| §7.12 Data Quality                              | http://data.europa.eu/it6/DataQuality              | Optional      | description                                        | http://purl.org/dc/terms/description                    |
| §7.13 Data Service                              | http://www.w3.org/ns/dcat#DataService              | Mandatory     | endpoint URL                                       | http://www.w3.org/ns/dcat#endpointURL                   |
| §7.13 Data Service                              | http://www.w3.org/ns/dcat#DataService              | Mandatory     | title                                                    | http://purl.org/dc/terms/title                          |
| §7.13 Data Service                              | http://www.w3.org/ns/dcat#DataService              | Optional      | serves dataset                                   | http://www.w3.org/ns/dcat#servesDataset                 |
| §7.13 Data Service                              | http://www.w3.org/ns/dcat#DataService              | Optional      | serves model                                       | http://data.europa.eu/it6/servesModel                   |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Mandatory     | collection date                                     | http://data.europa.eu/it6/collectionDate                |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Mandatory     | description                                            | http://purl.org/dc/terms/description                    |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Mandatory     | title                                                        | http://purl.org/dc/terms/title                          |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | access rights                                         | http://purl.org/dc/terms/accessRights                   |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | bias method                                             | http://data.europa.eu/it6/biasMethod                    |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | collection method                                 | http://data.europa.eu/it6/collectionMethod              |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | contributor                                            | http://purl.org/dc/terms/contributor                    |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | creator                                                    | http://purl.org/dc/terms/creator                        |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | curation method                                     | http://data.europa.eu/it6/curationMethod                |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | data provenance                                     | http://data.europa.eu/it6/dataProvenance                |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | dataset distribution                           | http://www.w3.org/ns/dcat#distribution                  |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | geographical coverage                         | http://purl.org/dc/terms/spatial                        |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | has version                                             | http://www.w3.org/ns/dcat#hasVersion                    |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | identifier                                              | http://purl.org/dc/terms/identifier                     |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | is referenced by                                    | http://purl.org/dc/terms/isReferencedBy                 |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | is version of                                          | http://purl.org/dc/terms/isVersionOf                    |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | keyword                                                    | http://www.w3.org/ns/dcat#keyword                       |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | landing page                                           | http://www.w3.org/ns/dcat#landingPage                   |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | language                                                  | http://purl.org/dc/terms/language                       |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | publisher                                                | http://purl.org/dc/terms/publisher                      |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | release date                                           | http://purl.org/dc/terms/issued                         |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | status                                                      | http://www.w3.org/ns/adms#status                        |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | theme                                                        | http://www.w3.org/ns/dcat#theme                         |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | type                                                          | http://purl.org/dc/terms/type                           |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | unsuitability method                           | http://data.europa.eu/it6/unsuitabilityMethod           |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | version                                                    | http://www.w3.org/ns/dcat#version                       |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | version label                                         | http://data.europa.eu/it6/versionLabel                  |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  | Optional      | visibility                                              | http://data.europa.eu/it6/visibility                    |
| §6.4 Dataset                                       | http://www.w3.org/ns/dcat#Dataset                  |               | was generated by                                    | http://www.w3.org/ns/prov#wasGeneratedBy                |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Mandatory     | access URL                                          | http://www.w3.org/ns/dcat#accessURL                     |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Mandatory     | has quality measurement                 | http://www.w3.org/ns/dqv#hasQualityMeasurement          |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | access service                                  | http://www.w3.org/ns/dcat#accessService                 |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | byte size                                            | http://www.w3.org/ns/dcat#byteSize                      |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | checksum                                             | http://spdx.org/rdf/terms#checksum                      |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | default target attribute               | http://data.europa.eu/it6/defaultTargetAttribute        |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | download URL                                      | http://www.w3.org/ns/dcat#downloadURL                   |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | format                                                 | http://purl.org/dc/terms/format                         |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | has data                                              | https://w3id.org/dpv#hasData                            |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | has feature                                        | http://data.europa.eu/it6/hasFeature                    |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | has policy                                          | http://www.w3.org/ns/odrl/2/hasPolicy                   |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | identifier                                         | http://purl.org/dc/terms/identifier                     |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | ignore attribute                              | http://data.europa.eu/it6/ignoreAttribute               |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | language                                             | http://purl.org/dc/terms/language                       |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | licence                                               | http://purl.org/dc/terms/license                        |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             |               | linked schemas                                  | http://purl.org/dc/terms/conformsTo                     |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | media type                                          | http://www.w3.org/ns/dcat#mediaType                     |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | number of datapoints                       | http://data.europa.eu/it6/numberOfDatapoints            |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | processing date                                | http://data.europa.eu/it6/processingDate                |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | processing error                              | http://data.europa.eu/it6/processingError               |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | processing warning                          | http://data.europa.eu/it6/processingWarning             |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | row ID attribute                               | http://data.europa.eu/it6/rowIDAttribute                |
| §6.5 Distribution                             | http://www.w3.org/ns/dcat#Distribution             | Optional      | title                                                   | http://purl.org/dc/terms/title                          |
| §7.14 Document                                     | http://xmlns.com/foaf/0.1/Document                 |               |                                                                                                                                   |                                                         |
| §7.15 Engagement                                 | http://data.europa.eu/it6/Engagement               | Optional      | download                                               | http://data.europa.eu/it6/download                      |
| §7.15 Engagement                                 | http://data.europa.eu/it6/Engagement               | Optional      | like                                                       | http://data.europa.eu/it6/like                          |
| §7.16 Environmental Impact              | http://data.europa.eu/it6/EnvironmentalImpact      | Optional      | carbon emitted                           | http://data.europa.eu/it6/carbonEmitted                 |
| §7.16 Environmental Impact              | http://data.europa.eu/it6/EnvironmentalImpact      | Optional      | measurement methodology         | http://data.europa.eu/it6/measurementMethodology        |
| §7.16 Environmental Impact              | http://data.europa.eu/it6/EnvironmentalImpact      | Optional      | power consumption                     | http://data.europa.eu/it6/powerConsumption              |
| §7.17 Estimation Procedure              | http://data.europa.eu/it6/EstimationProcedure      | Mandatory     | description                                | http://purl.org/dc/terms/description                    |
| §7.17 Estimation Procedure              | http://data.europa.eu/it6/EstimationProcedure      | Mandatory     | has parameter                             | http://data.europa.eu/it6/hasParameter                  |
| §7.17 Estimation Procedure              | http://data.europa.eu/it6/EstimationProcedure      | Mandatory     | has split                                     | http://data.europa.eu/it6/hasSplit                      |
| §7.17 Estimation Procedure              | http://data.europa.eu/it6/EstimationProcedure      | Mandatory     | identifier                                  | http://purl.org/dc/terms/identifier                     |
| §7.17 Estimation Procedure              | http://data.europa.eu/it6/EstimationProcedure      | Mandatory     | title                                            | http://purl.org/dc/terms/title                          |
| §7.17 Estimation Procedure              | http://data.europa.eu/it6/EstimationProcedure      | Mandatory     | type                                              | http://purl.org/dc/terms/type                           |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Mandatory     | title                                                     | http://purl.org/dc/terms/title                          |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | array data                                            | http://data.europa.eu/it6/arrayData                     |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | fold                                                       | http://data.europa.eu/it6/fold                          |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | has flow                                                | http://data.europa.eu/it6/hasFlow                       |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | identifier                                           | http://purl.org/dc/terms/identifier                     |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | interval end                                        | http://data.europa.eu/it6/intervalEnd                   |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | interval start                                    | http://data.europa.eu/it6/intervalStart                 |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | label                                                     | http://www.w3.org/2000/01/rdf-schema#label              |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | repeat                                                   | http://data.europa.eu/it6/repeat                        |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | sample                                                   | http://data.europa.eu/it6/sample                        |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | sample size                                          | http://data.europa.eu/it6/sampleSize                    |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | stdev                                                     | http://data.europa.eu/it6/stdev                         |
| §7.18 Evaluation                                 | http://data.europa.eu/it6/Evaluation               | Optional      | value                                                     | http://data.europa.eu/it6/value                         |
| §7.19 Evaluation Measure                  | http://data.europa.eu/it6/EvaluationMeasure        | Mandatory     | title                                              | http://purl.org/dc/terms/title                          |
| §7.19 Evaluation Measure                  | http://data.europa.eu/it6/EvaluationMeasure        | Mandatory     | value                                              | http://data.europa.eu/it6/value                         |
| §7.19 Evaluation Measure                  | http://data.europa.eu/it6/EvaluationMeasure        | Optional      | description                                  | http://purl.org/dc/terms/description                    |
| §7.19 Evaluation Measure                  | http://data.europa.eu/it6/EvaluationMeasure        | Optional      | implementation                            | http://data.europa.eu/it6/implementation                |
| §7.19 Evaluation Measure                  | http://data.europa.eu/it6/EvaluationMeasure        | Optional      | value bad                                       | http://data.europa.eu/it6/valueBad                      |
| §7.19 Evaluation Measure                  | http://data.europa.eu/it6/EvaluationMeasure        | Optional      | value good                                     | http://data.europa.eu/it6/valueGood                     |
| §7.20 Feature                                       | http://data.europa.eu/it6/Feature                  | Mandatory     | title                                                        | http://purl.org/dc/terms/title                          |
| §7.20 Feature                                       | http://data.europa.eu/it6/Feature                  | Mandatory     | type                                                          | http://purl.org/dc/terms/type                           |
| §7.20 Feature                                       | http://data.europa.eu/it6/Feature                  | Optional      | description                                            | http://purl.org/dc/terms/description                    |
| §6.6 File                                             | http://data.europa.eu/it6/File                     | Mandatory     | format                                                         | http://purl.org/dc/terms/format                         |
| §6.6 File                                             | http://data.europa.eu/it6/File                     | Mandatory     | id                                                                 | http://purl.org/dc/terms/identifier                     |
| §6.6 File                                             | http://data.europa.eu/it6/File                     | Mandatory     | title                                                           | http://purl.org/dc/terms/title                          |
| §6.6 File                                             | http://data.europa.eu/it6/File                     | Mandatory     | url                                                               | http://data.europa.eu/it6/url                           |
| §6.6 File                                             | http://data.europa.eu/it6/File                     | Optional      | checksum                                                     | http://spdx.org/rdf/terms#checksum                      |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Mandatory     | status                                                         | http://www.w3.org/ns/adms#status                        |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Mandatory     | uploaded                                                     | http://data.europa.eu/it6/uploaded                      |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | class name                                                  | http://data.europa.eu/it6/className                     |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | custom name                                                | http://data.europa.eu/it6/customName                    |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | description                                               | http://purl.org/dc/terms/description                    |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | external version                                      | http://data.europa.eu/it6/externalVersion               |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | has dependency                                          | http://data.europa.eu/it6/hasDependency                 |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | has flow parameter                                   | http://data.europa.eu/it6/hasFlowParameter              |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | has uploader                                              | http://data.europa.eu/it6/hasUploader                   |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | identifier                                                 | http://purl.org/dc/terms/identifier                     |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | keyword                                                       | http://www.w3.org/ns/dcat#keyword                       |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | title                                                           | http://purl.org/dc/terms/title                          |
| §7.21 Flow                                             | http://data.europa.eu/it6/Flow                     | Optional      | version                                                       | http://data.europa.eu/it6/version                       |
| §7.22 Flow Parameter                          | http://data.europa.eu/it6/FlowParameter            | Mandatory     | title                                                  | http://purl.org/dc/terms/title                          |
| §7.22 Flow Parameter                          | http://data.europa.eu/it6/FlowParameter            | Optional      | default value                                   | http://data.europa.eu/it6/defaultValue                  |
| §7.22 Flow Parameter                          | http://data.europa.eu/it6/FlowParameter            | Optional      | description                                      | http://purl.org/dc/terms/description                    |
| §7.22 Flow Parameter                          | http://data.europa.eu/it6/FlowParameter            | Optional      | recommended range                           | http://data.europa.eu/it6/recommendedRange              |
| §7.22 Flow Parameter                          | http://data.europa.eu/it6/FlowParameter            | Optional      | type                                                    | http://purl.org/dc/terms/type                           |
| §7.23 Hardware                                     | http://data.europa.eu/it6/Hardware                 | Mandatory     | title                                                       | http://purl.org/dc/terms/title                          |
| §7.23 Hardware                                     | http://data.europa.eu/it6/Hardware                 | Optional      | description                                           | http://purl.org/dc/terms/description                    |
| §6.7 Harm Risk                                    | http://data.europa.eu/it6/HarmRisk                 | Mandatory     | description                                           | http://purl.org/dc/terms/description                    |
| §6.7 Harm Risk                                    | http://data.europa.eu/it6/HarmRisk                 | Mandatory     | title                                                       | http://purl.org/dc/terms/title                          |
| §6.7 Harm Risk                                    | http://data.europa.eu/it6/HarmRisk                 | Optional      | mitigation                                             | http://data.europa.eu/it6/mitigation                    |
| §6.7 Harm Risk                                    | http://data.europa.eu/it6/HarmRisk                 | Optional      | nature                                                     | http://data.europa.eu/it6/nature                        |
| §6.7 Harm Risk                                    | http://data.europa.eu/it6/HarmRisk                 | Optional      | probability                                           | http://data.europa.eu/it6/probability                   |
| §6.7 Harm Risk                                    | http://data.europa.eu/it6/HarmRisk                 | Optional      | severity                                                 | http://data.europa.eu/it6/severity                      |
| §6.7 Harm Risk                                    | http://data.europa.eu/it6/HarmRisk                 | Optional      | source                                                     | http://data.europa.eu/it6/source                        |
| §6.7 Harm Risk                                    | http://data.europa.eu/it6/HarmRisk                 | Optional      | type                                                         | http://purl.org/dc/terms/type                           |
| §7.24 Image Object                              | http://data.europa.eu/m8g/ImageObject              |               |                                                                                                                                   |                                                         |
| §7.25 Library                                       | http://data.europa.eu/it6/Library                  | Mandatory     | title                                                        | http://purl.org/dc/terms/title                          |
| §7.25 Library                                       | http://data.europa.eu/it6/Library                  | Optional      | description                                            | http://purl.org/dc/terms/description                    |
| §7.25 Library                                       | http://data.europa.eu/it6/Library                  | Optional      | is executed by                                        | http://data.europa.eu/it6/isExecutedBy                  |
| §7.25 Library                                       | http://data.europa.eu/it6/Library                  | Optional      | licence                                                    | http://purl.org/dc/terms/license                        |
| §7.25 Library                                       | http://data.europa.eu/it6/Library                  | Optional      | version                                                    | http://data.europa.eu/it6/version                       |
| §7.26 Licence Document                      | http://purl.org/dc/terms/LicenseDocument           |               |                                                                                                                                   |                                                         |
| §7.27 Linguistic System                    | http://purl.org/dc/terms/LinguisticSystem          |               |                                                                                                                                   |                                                         |
| §7.28 Location                                     | http://purl.org/dc/terms/Location                  |               |                                                                                                                                   |                                                         |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Mandatory     | created                                       | http://purl.org/dc/terms/created                        |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Mandatory     | has file                                      | http://data.europa.eu/it6/hasFile                       |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Mandatory     | identifier                                 | http://purl.org/dc/terms/identifier                     |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Mandatory     | name                                             | http://purl.org/dc/terms/title                          |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Mandatory     | trained on                                  | http://data.europa.eu/it6/trainedOn                     |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Mandatory     | version                                       | http://www.w3.org/ns/dcat#version                       |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | bias                                             | http://data.europa.eu/it6/bias                          |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | contributor                               | http://purl.org/dc/terms/contributor                    |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | creator                                       | http://purl.org/dc/terms/creator                        |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | description                               | http://purl.org/dc/terms/description                    |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | design specifications            | http://data.europa.eu/it6/designSpecifications          |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | evaluation results                  | http://data.europa.eu/it6/evaluationResults             |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | evaluation strategies            | http://data.europa.eu/it6/evaluationStrategies          |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | fine tuned from                         | http://data.europa.eu/it6/fineTunedFrom                 |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has benchmark                            | http://data.europa.eu/it6/hasBenchmark                  |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has bibliographic reference | http://data.europa.eu/it6/hasBibliographicReference     |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has engagement                          | http://data.europa.eu/it6/hasEngagement                 |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has input modality                   | http://data.europa.eu/it6/hasInputModality              |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has output modality                 | http://data.europa.eu/it6/hasOutputModality             |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has policy                                  | http://www.w3.org/ns/odrl/2/hasPolicy                   |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has prediction                          | http://data.europa.eu/it6/hasPrediction                 |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has provider                              | http://data.europa.eu/it6/hasProvider                   |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has registered user                 | http://data.europa.eu/it6/hasRegisteredUser             |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has repository                          | http://data.europa.eu/it6/hasRepository                 |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has risk                                      | http://data.europa.eu/it6/hasRisk                       |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has uploader                              | http://data.europa.eu/it6/hasUploader                   |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | has variation                            | http://data.europa.eu/it6/hasVariation                  |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | how to use                                   | http://data.europa.eu/it6/howToUse                      |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | intended use                              | http://data.europa.eu/it6/intendedUse                   |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | is funded by                               | http://purl.org/cerif/frapo/isFundedBy                  |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | keyword                                       | http://www.w3.org/ns/dcat#keyword                       |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | language                                     | http://purl.org/dc/terms/language                       |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | licence                                       | http://purl.org/dc/terms/license                        |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | limitations                               | http://data.europa.eu/it6/limitations                   |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | logo                                             | http://data.europa.eu/m8g/logo                          |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | method of distribution           | http://data.europa.eu/it6/methodOfDistribution          |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | model architecture                  | http://data.europa.eu/it6/modelArchitecture             |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | modified                                     | http://purl.org/dc/terms/modified                       |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | placed on market date              | http://data.europa.eu/it6/placedOnMarketDate            |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | ran on                                          | http://data.europa.eu/it6/ranOn                         |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | release date                              | http://data.europa.eu/it6/releaseDate                   |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | short description                    | http://data.europa.eu/it6/shortDescription              |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | tested on                                    | http://data.europa.eu/it6/testedOn                      |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | testing description                | http://data.europa.eu/it6/testingDescription            |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | total number of parameters    | http://data.europa.eu/it6/totalNumberOfParameters       |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | training methodologies          | http://data.europa.eu/it6/trainingMethodologies         |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | training process                      | http://data.europa.eu/it6/trainingProcess               |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | type                                             | http://purl.org/dc/terms/type                           |
| §6.8 Machine Learning Model           | http://data.europa.eu/it6/MachineLearningModel     | Optional      | validated on                              | http://data.europa.eu/it6/validatedOn                   |
| §7.29 Measure                                       | http://data.europa.eu/it6/Measure                  |               |                                                                                                                                   |                                                         |
| §7.30 Media Type                                  | http://purl.org/dc/terms/MediaType                 |               |                                                                                                                                   |                                                         |
| §7.31 Media Type Or Extent                | http://purl.org/dc/terms/MediaTypeOrExtent         |               |                                                                                                                                   |                                                         |
| §7.32 Modality                                     | http://data.europa.eu/it6/Modality                 | Optional      | classification                                     | http://data.europa.eu/it6/classification                |
| §7.32 Modality                                     | http://data.europa.eu/it6/Modality                 | Optional      | size                                                         | http://data.europa.eu/it6/size                          |
| §7.33 Output File Description         | http://data.europa.eu/it6/OutputFileDescription    | Mandatory     | id                                                | http://purl.org/dc/terms/identifier                     |
| §7.33 Output File Description         | http://data.europa.eu/it6/OutputFileDescription    | Mandatory     | title                                          | http://purl.org/dc/terms/title                          |
| §7.33 Output File Description         | http://data.europa.eu/it6/OutputFileDescription    | Mandatory     | url                                              | http://data.europa.eu/it6/url                           |
| §6.9 Paper                                           | https://linkedpaperswithcode.com/class/paper       | Mandatory     | date                                                            | http://purl.org/dc/terms/date                           |
| §6.9 Paper                                           | https://linkedpaperswithcode.com/class/paper       | Mandatory     | has document                                             | http://data.europa.eu/it6/hasDocument                   |
| §6.9 Paper                                           | https://linkedpaperswithcode.com/class/paper       | Mandatory     | title                                                          | http://purl.org/dc/terms/title                          |
| §6.9 Paper                                           | https://linkedpaperswithcode.com/class/paper       | Optional      | abstract                                                    | http://purl.org/dc/terms/abstract                       |
| §6.9 Paper                                           | https://linkedpaperswithcode.com/class/paper       | Optional      | creator                                                      | http://purl.org/dc/terms/creator                        |
| §6.9 Paper                                           | https://linkedpaperswithcode.com/class/paper       | Optional      | has model                                                   | https://linkedpaperswithcode.com/property/hasModel      |
| §6.9 Paper                                           | https://linkedpaperswithcode.com/class/paper       | Optional      | has repository                                         | https://linkedpaperswithcode.com/property/hasRepository |
| §6.9 Paper                                           | https://linkedpaperswithcode.com/class/paper       | Optional      | references                                                | http://purl.org/dc/terms/references                     |
| §6.9 Paper                                           | https://linkedpaperswithcode.com/class/paper       | Optional      | subject                                                      | http://purl.org/dc/terms/subject                        |
| §7.34 Parameter                                   | http://data.europa.eu/it6/Parameter                | Mandatory     | name                                                        | http://purl.org/dc/terms/title                          |
| §7.34 Parameter                                   | http://data.europa.eu/it6/Parameter                | Mandatory     | value                                                      | http://data.europa.eu/it6/value                         |
| §7.34 Parameter                                   | http://data.europa.eu/it6/Parameter                | Optional      | component                                              | http://data.europa.eu/it6/component                     |
| §7.35 Policy                                         | http://www.w3.org/ns/odrl/2/Policy                 |               |                                                                                                                                   |                                                         |
| §7.36 Prediction                                 | http://data.europa.eu/it6/Prediction               | Mandatory     | format                                                   | http://purl.org/dc/terms/format                         |
| §7.36 Prediction                                 | http://data.europa.eu/it6/Prediction               | Mandatory     | has prediction feature                     | http://data.europa.eu/it6/hasPredictionFeature          |
| §7.37 Prediction Feature                  | http://data.europa.eu/it6/PredictionFeature        | Mandatory     | title                                              | http://purl.org/dc/terms/title                          |
| §7.37 Prediction Feature                  | http://data.europa.eu/it6/PredictionFeature        | Mandatory     | type                                                | http://purl.org/dc/terms/type                           |
| §6.10 Quality Measurement                | http://www.w3.org/ns/dqv#QualityMeasurement        | Mandatory     | type                                               | http://purl.org/dc/terms/type                           |
| §6.10 Quality Measurement                | http://www.w3.org/ns/dqv#QualityMeasurement        | Mandatory     | value                                             | http://www.w3.org/ns/dqv#value                          |
| §6.10 Quality Measurement                | http://www.w3.org/ns/dqv#QualityMeasurement        | Optional      | dataset                                         | http://purl.org/linked-data/cube#dataSet                |
| §6.10 Quality Measurement                | http://www.w3.org/ns/dqv#QualityMeasurement        | Optional      | feature index                              | http://data.europa.eu/it6/featureIndex                  |
| §6.10 Quality Measurement                | http://www.w3.org/ns/dqv#QualityMeasurement        | Optional      | interval end                                | http://data.europa.eu/it6/intervalEnd                   |
| §6.10 Quality Measurement                | http://www.w3.org/ns/dqv#QualityMeasurement        | Optional      | interval start                            | http://data.europa.eu/it6/intervalStart                 |
| §7.38 Quality Measurement Dataset | http://www.w3.org/ns/dqv#QualityMeasurementDataset | Mandatory     | identifier                            | http://purl.org/dc/terms/identifier                     |
| §7.38 Quality Measurement Dataset | http://www.w3.org/ns/dqv#QualityMeasurementDataset | Optional      | evaluation engine id          | http://data.europa.eu/it6/evaluationEngine              |
| §7.39 Repository                                 | https://linkedpaperswithcode.com/class/repository  | Mandatory     | name                                                       | http://purl.org/dc/terms/title                          |
| §7.39 Repository                                 | https://linkedpaperswithcode.com/class/repository  | Optional      | has file                                                | http://data.europa.eu/it6/hasFile                       |
| §7.40 Resource                                     | http://www.w3.org/2000/01/rdf-schema#Resource      |               |                                                                                                                                   |                                                         |
| §7.41 Rights Statement                      | http://purl.org/dc/terms/RightsStatement           |               |                                                                                                                                   |                                                         |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Mandatory     | executes                                                      | http://www.w3.org/ns/mls#realizes                       |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Mandatory     | has flow                                                       | http://data.europa.eu/it6/hasFlow                       |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Mandatory     | has output file description                   | http://data.europa.eu/it6/hasOutputFileDescription      |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Mandatory     | has output file prediction                     | http://data.europa.eu/it6/hasOutputFilePrediction       |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | error message                                             | http://data.europa.eu/it6/errorMessage                  |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | has evaluation                                           | http://data.europa.eu/it6/hasEvaluation                 |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | has inferencing impact                            | http://data.europa.eu/it6/hasInferencingImpact          |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | has parameter                                             | http://data.europa.eu/it6/hasParameter                  |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | has task                                                       | http://data.europa.eu/it6/hasTask                       |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | has training impact                                  | http://data.europa.eu/it6/hasTrainingImpact             |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | has uploader                                               | http://data.europa.eu/it6/hasUploader                   |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | identifier                                                  | http://purl.org/dc/terms/identifier                     |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | keyword                                                        | http://www.w3.org/ns/dcat#keyword                       |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | run details                                                 | http://data.europa.eu/it6/runDetails                    |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | setup Id                                                       | http://data.europa.eu/it6/setupId                       |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | setup string                                               | http://data.europa.eu/it6/setupString                   |
| §7.42 Run                                               | http://data.europa.eu/it6/Run                      | Optional      | training time                                             | http://data.europa.eu/it6/trainingTime                  |
| §7.43 Run Collection                          | http://data.europa.eu/it6/RunCollection            | Mandatory     | has run                                               | http://data.europa.eu/it6/hasRun                        |
| §7.44 Split                                           | http://data.europa.eu/it6/Split                    | Mandatory     | id                                                                | http://purl.org/dc/terms/identifier                     |
| §7.44 Split                                           | http://data.europa.eu/it6/Split                    | Mandatory     | is applied to                                            | http://data.europa.eu/it6/isAppliedTo                   |
| §7.44 Split                                           | http://data.europa.eu/it6/Split                    | Mandatory     | title                                                          | http://purl.org/dc/terms/title                          |
| §7.44 Split                                           | http://data.europa.eu/it6/Split                    | Optional      | description                                              | http://purl.org/dc/terms/description                    |
| §7.44 Split                                           | http://data.europa.eu/it6/Split                    | Optional      | type                                                            | http://purl.org/dc/terms/type                           |
| §7.45 Standard                                     | http://purl.org/dc/terms/Standard                  |               |                                                                                                                                   |                                                         |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Mandatory     | has estimation procedure                       | http://data.europa.eu/it6/hasEstimationProcedure        |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Mandatory     | has evaluation measure                           | http://data.europa.eu/it6/hasEvaluationMeasure          |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Mandatory     | has output                                                  | http://data.europa.eu/it6/hasOutput                     |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Mandatory     | has task type                                             | http://data.europa.eu/it6/hasTaskType                   |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Mandatory     | source data                                                | http://data.europa.eu/it6/sourceData                    |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Mandatory     | target feature                                          | http://data.europa.eu/it6/targetFeature                 |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Mandatory     | title                                                           | http://purl.org/dc/terms/title                          |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Optional      | has cost matrix                                         | http://data.europa.eu/it6/hasCostMatrix                 |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Optional      | id                                                                 | http://purl.org/dc/terms/identifier                     |
| §7.46 Task                                             | http://data.europa.eu/it6/Task                     | Optional      | keyword                                                       | http://www.w3.org/ns/dcat#keyword                       |
| §7.47 Task Collection                        | http://data.europa.eu/it6/TaskCollection           | Mandatory     | has task                                            | http://data.europa.eu/it6/hasTask                       |
| §7.48 Task Type                                    | http://data.europa.eu/it6/TaskType                 | Mandatory     | description                                           | http://www.w3.org/2004/02/skos/core#definition          |
| §7.48 Task Type                                    | http://data.europa.eu/it6/TaskType                 | Mandatory     | id                                                             | http://www.w3.org/2004/02/skos/core#notation            |
| §7.48 Task Type                                    | http://data.europa.eu/it6/TaskType                 | Mandatory     | title                                                       | http://www.w3.org/2004/02/skos/core#prefLabel           |
