---
title: "SHACL 1.2 Overview"
source: https://w3c.github.io/data-shapes/shacl12-overview/
family: shacl
version: "1.2"
fetched: 2026-10-21
---

# SHACL 1.2 Overview

> Map of the SHACL 1.2 document suite.

## Contents

- SHACL Specifications
- 1 Introduction
- 2 What's New in SHACL 1.2
  - 2.1 Community Resources
- 3 SHACL-SHACL
- 4 SHACL-OWL
- 5 Security and Privacy Considerations

---

This document provides an overview of SHACL.

SHACL, the Shapes Constraint Language, is a language for describing the structure of RDF graphs.
It may be used for a variety of purposes such as validating, inferencing, modeling domains, generating ontologies and building user interfaces.

This document provides a non-normative, high-level, overview of the various SHACL specifications and how SHACL has
changed between its original and 1.2 releases. It also describes and lists some SHACL resources not found in the
specification documents.

This documentation is published by the [Data Shapes Working Group](https://www.w3.org/groups/wg/data-shapes/).

## SHACL Specifications

This specification is part of the SHACL 1.2 family of specifications.

The specifications are as follows:

**Working Drafts:**

[shacl12-core]

defines the Core of SHACL

[shacl12-node-expr]

defines expressions used to derive focus nodes and value nodes in SHACL

[shacl12-sparql]

defines SPARQL-related extensions of SHACL

[shacl12-inference-rules]

defines SHACL's framework of rule-based inference

[shacl12-profiling]

defines the use of SHACL for profiling data, including SHACL data

[shacl12-ui]

defines SHACL's use for User Interface generation

[sparql12-rl]

defines a Datalog-style rules language for RDF that can be used with SHACL 1.2 Inference Rules

**Editor's Drafts:**

[SHACL 1.2 Overview](https://w3c.github.io/data-shapes/shacl12-overview/)

overviews the set of SHACL specifications

## Introduction

The second iteration of the World Wide Web Consortium's [Data Shapes Working Group](https://www.w3.org/groups/wg/data-shapes/) aimed to "...update data shapes standards in line with the versions of core Semantic Web standards that cater
for RDF-star and to extend the applications of data shapes with new packaging and use specifications". The
outcome of the Working Group's operations was a set of specifications - W3C 'Recommendations' - that cover core
SHACL elements, extended elements for advanced validation and SHACL functions beyond validation, such as rule
evaluation, User Interface generation and the packaging of SHACL.

The original SHACL specifications as published in 2017 are:

1. [shacl-20170720] - W3C Recommendation
2. [shacl-ucr] - W3C Note
3. [shacl-af-20170608] - W3C Note
4. [shacl-js-20170608] - W3C Note

Additionally, there is [DASH - Data Shapes](https://datashapes.org/) which is a members' extension to
the above specifications including new types of validation result, extended SPARQL instructions and UI
generation.

Section [#specifications] above lists the Data Shapes Working Group's original and current (1.2)
specifications.

Section [#whatsnew] below describes the changes between SHACL, as published in 2017 and SHACL 1.2.

Section [#community-resources] below describes SHACL resources managed by W3C groups following on from
the Data Shapes Working Group.

The appendixes below contain material supporting the set of SHACL specifications and provide SHACL users with
additional support, such as validators for shapes graphs.

## What's New in SHACL 1.2

SHACL 1.2 covers new elements in RDF 1.2 and SPARQL 1.2, see [rdf12-new] and [sparql12-new]. It adds
formal specification - Recommendations - for what previously were Working Group Notes or member publications and
takes SHACL into new areas such as profile definition.

While SHACL 1.2 does aim to cater for all aspects of [rdf12-concepts] and [sparql12-query],
those specifications are not finalized while this note remains here, so coverage may not yet be complete.

Following are the major new things in SHACL 1.2 and the specifications in which they appear.

| New Feature                                       | Description                                                                                                                                                                                              | SHACL 1.2 Specification                          |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Derived Properties                                | In the original SHACL specifications, shapes and constraints could only operate on asserted triples in a graph, and computed inferred triples was left as an optional pre-processing step using languages like RDF Schema and OWL. SHACL 1.2 introduces its own inferencing and reasoning capabilities, which make SHACL more self-contained and cover different use cases than RDFS/OWL. Node expressions can be used to dynamically derive property values (before validation and for display purposes). | [shacl12-core] [shacl12-node-expr]       |
| Flexible Target Nodes                             | In SHACL 1.2, node expressions can be used in more places than derived properties, to which they were limited in the original SHACL-AF specification. Particularly, they can now also be used to compute the target nodes of a shape. Furthermore, a new shape-based target type `sh:targetWhere` was intoduced. These features provide greater flexibility than the built-in target types such as `sh:targetClass` and `sh:targetSubjectsOf`. | [shacl12-node-expr]                          |
| Inference Rules                                   | The data shapes working group has produced two rule-related specifications: [shacl12-inference-rules] defines an extension to SHACL for representing inference rules, in particular rules that can be linked to shapes. It was inspired by the SPARQL-based rules introduced by the [shacl-af-20170608] and older technologies such as [SPIN](https://spinrdf.org/). [sparql12-rl] allows the representation and execution of [Datalog](https://en.wikipedia.org/wiki/Datalog)-based rules using a SPARQL-like syntax. These have a straight-forward mapping to SPARQL `CONSTRUCT` statements and can be executed within a SHACL Inferencing Rules envelope, allowing for integration with other SHACL features such as node expressions. | [sparql12-rl], [shacl12-inference-rules] |
| Better Syntax for Unions of Datatypes and Classes | In the original SHACL specifications, when you wanted to express that the datatype of a property was either `xsd:string`, `rdf:langString`, or `rdf:HTML`, you needed to use a verbose, repetitive construct. In SHACL 1.2, this can be written as a single list. | [shacl12-core]                               |
| Constraints on RDF 1.2 Reification                | The major new feature in RDF 1.2 is reification, enabling RDF statements to be easily made about other RDF statements. SHACL 1.2 introduces new constraint properties (`sh:reifierShape` and `sh:reificationRequired`) which allow a shape targeting a triple to be chained to another shape targeting reification elements. | [shacl12-core]                               |
| Use of Reification in Constraint Definitions      | In the original SHACL specifications, the severity and messages of a constraint had to be declared for the surrounding shape, sometimes requiring artificial intermediate shapes to be introduced to change only the severity or a message. SHACL 1.2 syntax is more flexible, allowing severity and messages to be directly attached to individual constraint triples. | [shacl12-core]                               |
| The `sh:ShapeClass` Metaclass                     | A new class, `sh:ShapeClass`, comparable to `owl:Class`, is used to define classes that can declare constraints that apply to all instances of the class. It is equivalent to OWL syntax for declaring a class that may hold [OWL axioms](https://www.w3.org/TR/owl2-primer/#Annotating_Axioms_and_Entities). This allows SHACL to be a more self-contained ontology modeling language. | [shacl12-core]                               |
| Cleaner Separation between Core and SPARQL        | We now have a cleaner separation of Core and SPARQL concerns into separate specifications. This helps indicate SHACL Core is not dependent on SPARQL, clarify other dependencies, and make some implementations easier. | [shacl12-core], [shacl12-sparql]         |
| Using SHACL to define User Interfaces             | Industry has used the original SHACL specifications for user interface generation since publication, with non-W3C extensions such as [DASH](https://www.datashapes.org/). This is now formalized in a new specification. | [shacl12-ui]                                 |
| More Annotation Properties                        | The SHACL namespace now covers annotation properties for a variety of new use cases. `sh:codeIdentifier` and `sh:codeType` support code generation from shapes. `sh:unit` can link a property to units of measure. `sh:agentInstruction` and `sh:intent` are designed to make shapes more useful for LLMs. `sh:incomplete` marks data that is known to be incomplete and `sh:incompleteURIStart` clarifies that external resources are used without fully importing their defining graphs. | [shacl12-core]                               |
| Packaging of SHACL                                | SHACL elements have long been used in sets, typically OWL ontologies, and sometimes with additional semantic relations for management. [shacl12-profiling] now provides guidance on packaging of elements for validation and for reporting validation results. | [shacl12-profiling]                          |
| Profiles of SHACL                                 | Since 2017's SHACL and SHACL-AF, there were subsets of SHACL. In the SHACL 1.2 specifications, there are more. There is now a mechanism defined for profiling SHACL and a list of known profiles. There is also a set of 'SHACL-SHACL' validators - for each specification - rather than just one. | [shacl12-profiling]                          |
| Profiling with SHACL                              | SHACL has always been used to *profile* RDF graphs and make validators for specifications that do not supply them, such as older W3C vocabularies/ontologies. [shacl12-profiling] now indicates how to use SHACL to profile other things, within the conceptual model of [dx-prof-1.0]. | [shacl12-profiling]                          |

### Community Resources

Since the initial publication of the original SHACL specifications, the SHACL user community has generated a lot
of resources, some of which would benefit everyone by being shared for reuse.

A version control repository has been established by the W3C for shared SHACL resources:

- <https://github.com/w3c/shacl-resources>

Within the life of the SHACL Working Group responsible for this note, resources such as definitions of profiles
of SHACL, SHACL-SHACL validators, see below, and more where added to this repository for maintenance beyond the
life of the Working Group.

The SHACL community is encouraged to use that repository by improving the existing resources there, submitting
new useful resources and by providing references to other interesting resources.

## SHACL-SHACL

The [Data Shapes Working Group](https://www.w3.org/groups/wg/data-shapes/) maintains SHACL Shapes Graphs known as "SHACL-SHACL", which are used to validate other SHACL Shapes Graphs. Multiple graphs exist to enable the validation of subsets of the complete body of SHACL elements. The subsets are based on the scopes of the various SHACL Specifications.

Each SHACL-SHACL Shapes Graph corresponds to the scope of an individual SHACL specification and is available as an RDF resource:

[SHACL 1.2 Core shapes graph](http://www.w3.org/ns/shacl-shacl/core)

Core specification elements only

[SHACL 1.2 SPARQL shapes graph](http://www.w3.org/ns/shacl-shacl/sparql)

SPARQL specification elements only

[SHACL 1.2 Node Expressions shapes graph](http://www.w3.org/ns/shacl-shacl/node-expr)

Node Expression specification elements only

[SHACL 1.2 Rules shapes graph](http://www.w3.org/ns/shacl-shacl/rules)

Rules specification elements only

[SHACL 1.2 UI shapes graph](http://www.w3.org/ns/shacl-shacl/ui)

UI specification elements only

[SHACL 1.2 Profiling shapes graph](http://www.w3.org/ns/shacl-shacl/profiling)

Profiling specification elements only

In addition, the union of the above shapes graphs is provided:

[SHACL 1.2 union shapes graph](http://www.w3.org/ns/shacl-shacl)

the union of all other SHACL-SHACL graphs

The SHACL-SHACL Shapes Graphs listed above can be retrieved from their namespace IRIs and are also available
as described in Section [#community-resources].

## SHACL-OWL

The [Data Shapes Working Group](https://www.w3.org/groups/wg/data-shapes/) maintains a SHACL graph known as "SHACL-OWL", which is used to cast SHACL concepts as OWL classes and properties, conformant to typing constraints of OWL 2 DL. This graph enables OWL 2 DL validation for ontologies that use SHACL and OWL modeling concepts together within ontology graphs.

SHACL concepts appear undefined from the perspective of an OWL syntax validator, unless OWL type assertions have been inlined somehow in the OWL validator's inputs. Definitions for SHACL `rdfs:Class`es are straightforward, but property types face potential decision points. Typing constraints of OWL 2 DL require that exactly one of `owl:ObjectProperty`, `owl:DatatypeProperty`, or `owl:AnnotationProperty` be the type of any property used in an OWL ontology but SHACL does not specify typing like this. SHACL-OWL provides these types, designating most SHACL properties as `owl:AnnotationProperty` unless a reason was found by the Data Shapes Working Group to use another type.

SHACL-OWL is available as an RDF resource:

[SHACL 1.2 OWL graph](http://www.w3.org/ns/shacl-owl)

All SHACL 1.2 RDF classes and properties cast with OWL types

The SHACL-OWL Shapes Graph listed above can be retrieved from its namespace IRIs and also as described in
Section [#community-resources].

## Security and Privacy Considerations

The SHACL-SHACL Shapes graphs do not import or modify the data they evaluate, ensuring that they do not impact an organization's information when applied to it. They only report on the data's validity according to the vocabulary-subset of
SHACL corresponding to the utilized Shapes graph and any imports of other SHACL-SHACL Shapes graphs (e.g., all SHACL-SHACL shapes graphs will import SHACL-SHACL Core). Additionally, they do not automatically export results anywhere beyond
a SHACL processor's standard output channel.

For these reasons, this content is expected to present minimal security and privacy concerns.
