---
title: "PROV-O: The PROV Ontology"
source: https://www.w3.org/TR/prov-o/
family: prov
status: W3C Recommendation
spec_date: 2013-04-30
fetched: 2026-10-26
---

# PROV-O: The PROV Ontology

> OWL2 ontology for provenance interchange.

## Contents

- Abstract
- 1 Introduction
  - 1.1 Compliance with this Document
  - 1.2 Notational Conventions
  - 1.3 Namespaces
- 2 PROV-O at a glance
- 3 The PROV-O Ontology Description
  - 3.1 Starting Point Terms
  - 3.2 Expanded Terms
  - 3.3 Qualified Terms
- 4 Cross reference for PROV-O classes and properties
  - 4.1 Starting Point Terms
  - 4.1.1 (1) Class: prov:Entity back to starting-point classes
  - 4.1.2 (2) Class: prov:Activity back to starting-point classes
  - 4.1.3 (3) Class: prov:Agent back to starting-point classes
  - 4.1.4 (4) Property: prov:wasGeneratedBy op back to starting-point properties
  - 4.1.5 (5) Property: prov:wasDerivedFrom op back to starting-point properties
  - 4.1.6 (6) Property: prov:wasAttributedTo op back to starting-point properties
  - 4.1.7 (7) Property: prov:startedAtTime dp back to starting-point properties
  - 4.1.8 (8) Property: prov:used op back to starting-point properties
  - 4.1.9 (9) Property: prov:wasInformedBy op back to starting-point properties
  - 4.1.10 (10) Property: prov:endedAtTime dp back to starting-point properties
  - 4.1.11 (11) Property: prov:wasAssociatedWith op back to starting-point properties
  - 4.1.12 (12) Property: prov:actedOnBehalfOf op back to starting-point properties
  - 4.2 Expanded Terms
  - 4.2.1 (13) Class: prov:Collection back to expanded classes
  - 4.2.2 (14) Class: prov:EmptyCollection back to expanded classes
  - 4.2.3 (15) Class: prov:Bundle back to expanded classes
  - 4.2.4 (16) Class: prov:Person back to expanded classes
  - 4.2.5 (17) Class: prov:SoftwareAgent back to expanded classes
  - 4.2.6 (18) Class: prov:Organization back to expanded classes
  - 4.2.7 (19) Class: prov:Location back to expanded classes
  - 4.2.8 (20) Property: prov:alternateOf op back to expanded properties
  - 4.2.9 (21) Property: prov:specializationOf op back to expanded properties
  - 4.2.10 (22) Property: prov:generatedAtTime dp back to expanded properties
  - 4.2.11 (23) Property: prov:hadPrimarySource op back to expanded properties
  - 4.2.12 (24) Property: prov:value dp back to expanded properties
  - 4.2.13 (25) Property: prov:wasQuotedFrom op back to expanded properties
  - 4.2.14 (26) Property: prov:wasRevisionOf op back to expanded properties
  - 4.2.15 (27) Property: prov:invalidatedAtTime dp back to expanded properties
  - 4.2.16 (28) Property: prov:wasInvalidatedBy op back to expanded properties
  - 4.2.17 (29) Property: prov:hadMember op back to expanded properties
  - 4.2.18 (30) Property: prov:wasStartedBy op back to expanded properties
  - 4.2.19 (31) Property: prov:wasEndedBy op back to expanded properties
  - 4.2.20 (32) Property: prov:invalidated op back to expanded properties
  - 4.2.21 (33) Property: prov:influenced op back to expanded properties
  - 4.2.22 (34) Property: prov:atLocation op back to expanded properties
  - 4.2.23 (35) Property: prov:generated op back to expanded properties
  - 4.3 Qualified Terms
  - 4.3.1 (36) Class: prov:Influence back to qualified classes
  - 4.3.2 (37) Class: prov:EntityInfluence back to qualified classes
  - 4.3.3 (38) Class: prov:Usage back to qualified classes
  - 4.3.4 (39) Class: prov:Start back to qualified classes
  - 4.3.5 (40) Class: prov:End back to qualified classes
  - 4.3.6 (41) Class: prov:Derivation back to qualified classes
  - 4.3.7 (42) Class: prov:PrimarySource back to qualified classes
  - 4.3.8 (43) Class: prov:Quotation back to qualified classes
  - 4.3.9 (44) Class: prov:Revision back to qualified classes
  - 4.3.10 (45) Class: prov:ActivityInfluence back to qualified classes
  - 4.3.11 (46) Class: prov:Generation back to qualified classes
  - 4.3.12 (47) Class: prov:Communication back to qualified classes
  - 4.3.13 (48) Class: prov:Invalidation back to qualified classes
  - 4.3.14 (49) Class: prov:AgentInfluence back to qualified classes
  - 4.3.15 (50) Class: prov:Attribution back to qualified classes
  - 4.3.16 (51) Class: prov:Association back to qualified classes
  - 4.3.17 (52) Class: prov:Plan back to qualified classes
  - 4.3.18 (53) Class: prov:Delegation back to qualified classes
  - 4.3.19 (54) Class: prov:InstantaneousEvent back to qualified classes
  - 4.3.20 (55) Class: prov:Role back to qualified classes
  - 4.3.21 (56) Property: prov:wasInfluencedBy op back to qualified properties
  - 4.3.22 (57) Property: prov:qualifiedInfluence op back to qualified properties
  - 4.3.23 (58) Property: prov:qualifiedGeneration op back to qualified properties
  - 4.3.24 (59) Property: prov:qualifiedDerivation op back to qualified properties
  - 4.3.25 (60) Property: prov:qualifiedPrimarySource op back to qualified properties
  - 4.3.26 (61) Property: prov:qualifiedQuotation op back to qualified properties
  - 4.3.27 (62) Property: prov:qualifiedRevision op back to qualified properties
  - 4.3.28 (63) Property: prov:qualifiedAttribution op back to qualified properties
  - 4.3.29 (64) Property: prov:qualifiedInvalidation op back to qualified properties
  - 4.3.30 (65) Property: prov:qualifiedStart op back to qualified properties
  - 4.3.31 (66) Property: prov:qualifiedUsage op back to qualified properties
  - 4.3.32 (67) Property: prov:qualifiedCommunication op back to qualified properties
  - 4.3.33 (68) Property: prov:qualifiedAssociation op back to qualified properties
  - 4.3.34 (69) Property: prov:qualifiedEnd op back to qualified properties
  - 4.3.35 (70) Property: prov:qualifiedDelegation op back to qualified properties
  - 4.3.36 (71) Property: prov:influencer op back to qualified properties
  - 4.3.37 (72) Property: prov:entity op back to qualified properties
  - 4.3.38 (73) Property: prov:hadUsage op back to qualified properties
  - 4.3.39 (74) Property: prov:hadGeneration op back to qualified properties
  - 4.3.40 (75) Property: prov:activity op back to qualified properties
  - 4.3.41 (76) Property: prov:agent op back to qualified properties
  - 4.3.42 (77) Property: prov:hadPlan op back to qualified properties
  - 4.3.43 (78) Property: prov:hadActivity op back to qualified properties
  - 4.3.44 (79) Property: prov:atTime dp back to qualified properties
  - 4.3.45 (80) Property: prov:hadRole op back to qualified properties
  - 4.4 Term Index
- A PROV-O OWL Profile
- B Names of inverse properties
- C Changes since WD-prov-o-20120724
- D Changes since CR-prov-o-20121211
- E Changes since PR-prov-o-20130312
- F Acknowledgements
- G References
  - G.1 Normative references
  - G.2 Informative references

---

## Abstract

The PROV Ontology (PROV-O) expresses the PROV Data Model [PROV-DM] using the OWL2 Web Ontology Language (OWL2) [OWL2-OVERVIEW]. It provides a set of classes, properties, and restrictions that can be used to represent and interchange provenance information generated in different systems and under different contexts.
It can also be specialized to create new classes and properties to model provenance information for different applications and domains.
The [PROV Document Overview](https://www.w3.org/TR/2012/WD-prov-overview-20121211/) describes the overall state of PROV, and should be read before other PROV documents.

The namespace for all PROV-O terms is http://www.w3.org/ns/prov#.

The OWL encoding of the PROV Ontology is available [here](https://www.w3.org/ns/prov-o).

## 1. Introduction

The PROV Ontology (PROV-O) defines the OWL2 Web Ontology Language encoding of the PROV Data Model [PROV-DM]. This document describes the set of classes, properties, and restrictions that constitute the PROV Ontology. This ontology specification provides the foundation to implement provenance applications in different domains that can represent, exchange, and integrate provenance information generated in different systems and under different contexts. Together with the PROV Access and Query [PROV-AQ] and PROV Data Model [PROV-DM], this document forms a framework for provenance information interchange in domain-specific Web-based applications.

PROV-O is a lightweight ontology that can be adopted in a wide range of applications.
With the exception of five axioms (§A), PROV-O conforms to the OWL-RL profile [OWL2-PRIMER].
The PROV Ontology classes and properties are defined such that they can not only be used directly to represent provenance information,
but also can be specialized for modeling application-specific provenance details in a variety of domains.
Thus, the PROV Ontology is expected to be both directly usable in applications as well as serve as a *reference model* for creating domain-specific provenance ontologies and thereby facilitates interoperable provenance modeling.
To demonstrate the use of PROV-O classes and properties, this document uses an example provenance scenario similar to the one introduced in the PROV-Primer [PROV-PRIMER].

The PROV Data Model [PROV-DM] introduces a set of concepts to represent provenance information in a variety of application domains. This document maps the PROV Data Model to PROV Ontology using the OWL2 ontology language [OWL2-OVERVIEW].

We briefly introduce some of the OWL2 modeling terms that will be used to describe the PROV Ontology.
An OWL2 *instance* is an individual object in a domain of discourse, for example a person named Alice or a car named KITT.
A set of individuals sharing common characteristics constitutes a *class*.

Person and Car are examples of classes representing the set of individual persons and cars respectively.
The OWL2 object properties are used to link individuals, classes, or create a property hierarchy.
For example, the object property "hasOwner" can be used to link car with person.
The OWL2 datatype properties are used to link individuals or classes to data values, including XML Schema datatypes [XMLSCHEMA11-2].

### 1.1 Compliance with this Document

For the purpose of compliance, the normative sections of this document are Section 1.1 (§1.1), Section 1.2 (§1.2), Section 3 (§3), Section 4 (§4), and Appendix B (§B)

- Information in tables is normative if it appears in a normative section.
- All figures and diagrams are informative.
- All examples are informative.

### 1.2 Notational Conventions

The key words "*must*", "*must not*", "*required*", "*shall*", "*shall not*", "*should*", "*should not*", "*recommended*", "*may*", and "*optional*" in this document are to be interpreted as described in [RFC2119].

### 1.3 Namespaces

*This section is non-normative.*

The following namespace prefixes are used throughout this document.

*Table 1: Prefix and Namespaces used in this specification*

| **prefix** | **namespace IRI**                           | **definition**                                                                                                                                                                                         |
| ---------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| rdf        | http://www.w3.org/1999/02/22-rdf-syntax-ns# | The RDF namespace [RDF-CONCEPTS]                                                                                                                     |
| xsd        | http://www.w3.org/2000/10/XMLSchema#        | XML Schema Namespace [XMLSCHEMA11-2]                                                                                                                |
| owl        | http://www.w3.org/2002/07/owl#              | The OWL namespace [OWL2-OVERVIEW]                                                                                                                   |
| prov       | http://www.w3.org/ns/prov#                  | The PROV namespace [PROV-DM]                                                                                                                              |
| (others)   | (various)                                   | All other namespace prefixes are used in examples only. In particular, IRIs starting with "http://example.com" represent some application-dependent IRI [IRI] |

## 2. PROV-O at a glance

*This section is non-normative.*

PROV-O users may only need to use parts of the entire ontology, depending on their needs and according to how much detail they want to include in their provenance information. For this, the PROV-O terms (classes and properties) are grouped into three categories to provide an incremental introduction to the ontology: Starting Point terms, Expanded terms, and terms for Qualifying relationships.

**Starting Point classes and properties** provide the basis for the rest of the PROV Ontology and thus it is recommended that readers become comfortable with how to apply these terms before continuing to the remaining categories. These terms are used to create simple provenance descriptions that can be elaborated using terms from other categories. The classes and properties in this category are listed below and are discussed in Section 3.1 (§3.1).

- prov:Entity (§4.1.1)
- prov:Activity (§4.1.2)
- prov:Agent (§4.1.3)

- prov:wasGeneratedBy (§4.1.4)
- prov:wasDerivedFrom (§4.1.5)
- prov:wasAttributedTo (§4.1.6)
- prov:startedAtTime (§4.1.7)
- prov:used (§4.1.8)
- prov:wasInformedBy (§4.1.9)
- prov:endedAtTime (§4.1.10)
- prov:wasAssociatedWith (§4.1.11)
- prov:actedOnBehalfOf (§4.1.12)

**Expanded classes and properties** provide additional terms that can be used to relate classes in the Starting Point category. The terms in this category are applied in the same way as the terms in the Starting Point category. Many of the terms in this category are subclasses or subproperties of those in the Starting Point category. The classes and properties in this category are listed below and are discussed in Section 3.2 (§3.2).

- prov:Collection (§4.2.1)
- prov:EmptyCollection (§4.2.2)
- prov:Bundle (§4.2.3)
- prov:Person (§4.2.4)
- prov:SoftwareAgent (§4.2.5)
- prov:Organization (§4.2.6)
- prov:Location (§4.2.7)

- prov:alternateOf (§4.2.8)
- prov:specializationOf (§4.2.9)
- prov:generatedAtTime (§4.2.10)
- prov:hadPrimarySource (§4.2.11)
- prov:value (§4.2.12)
- prov:wasQuotedFrom (§4.2.13)
- prov:wasRevisionOf (§4.2.14)
- prov:invalidatedAtTime (§4.2.15)
- prov:wasInvalidatedBy (§4.2.16)
- prov:hadMember (§4.2.17)
- prov:wasStartedBy (§4.2.18)
- prov:wasEndedBy (§4.2.19)
- prov:invalidated (§4.2.20)
- prov:influenced (§4.2.21)
- prov:atLocation (§4.2.22)
- prov:generated (§4.2.23)

**Qualified classes and properties** provide elaborated information about binary relations asserted using Starting Point and Expanded properties. The terms in this category are applied using a pattern that differs from those in the Starting Point and Expanded categories. While the relations from the previous two categories are applied as direct, binary assertions, the terms in this category are used to provide additional attributes of the binary relations. The pattern used in this category allows users to provide elaborate details that are not available using only Starting Point and Expanded terms. The classes and properties in this category are listed below and are discussed in Section 3.3 (§3.3).

- prov:Influence (§4.3.1)
- prov:EntityInfluence (§4.3.2)
- prov:Usage (§4.3.3)
- prov:Start (§4.3.4)
- prov:End (§4.3.5)
- prov:Derivation (§4.3.6)
- prov:PrimarySource (§4.3.7)
- prov:Quotation (§4.3.8)
- prov:Revision (§4.3.9)
- prov:ActivityInfluence (§4.3.10)
- prov:Generation (§4.3.11)
- prov:Communication (§4.3.12)
- prov:Invalidation (§4.3.13)
- prov:AgentInfluence (§4.3.14)
- prov:Attribution (§4.3.15)
- prov:Association (§4.3.16)
- prov:Plan (§4.3.17)
- prov:Delegation (§4.3.18)
- prov:InstantaneousEvent (§4.3.19)
- prov:Role (§4.3.20)

- prov:wasInfluencedBy (§4.3.21)
- prov:qualifiedInfluence (§4.3.22)
- prov:qualifiedGeneration (§4.3.23)
- prov:qualifiedDerivation (§4.3.24)
- prov:qualifiedPrimarySource (§4.3.25)
- prov:qualifiedQuotation (§4.3.26)
- prov:qualifiedRevision (§4.3.27)
- prov:qualifiedAttribution (§4.3.28)
- prov:qualifiedInvalidation (§4.3.29)
- prov:qualifiedStart (§4.3.30)
- prov:qualifiedUsage (§4.3.31)
- prov:qualifiedCommunication (§4.3.32)
- prov:qualifiedAssociation (§4.3.33)
- prov:qualifiedEnd (§4.3.34)
- prov:qualifiedDelegation (§4.3.35)
- prov:influencer (§4.3.36)
- prov:entity (§4.3.37)
- prov:hadUsage (§4.3.38)
- prov:hadGeneration (§4.3.39)
- prov:activity (§4.3.40)
- prov:agent (§4.3.41)
- prov:hadPlan (§4.3.42)
- prov:hadActivity (§4.3.43)
- prov:atTime (§4.3.44)
- prov:hadRole (§4.3.45)

## 3. The PROV-O Ontology Description

This section introduces the terms in each of the following categories:

- §3.1 Starting Point Terms
- §3.2 Expanded Terms
- §3.3 Qualified Terms

### 3.1 Starting Point Terms

The Starting Point category is a small set of classes and properties that can be used to create simple, initial provenance descriptions.
Three classes provide a basis for the rest of PROV-O:

- An prov:Entity (§4.1.1) is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
- An prov:Activity (§4.1.2) is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
- An prov:Agent (§4.1.3) is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.

The three primary classes relate to one another and to themselves using the properties shown in the following figure.

Activities **start** and **end** at particular points in time (described using properties prov:startedAtTime (§4.1.7) and prov:endedAtTime (§4.1.10), respectively)
and during their lifespan can **use** and **generate** a variety of Entities (described with prov:used (§4.1.8) and prov:wasGeneratedBy (§4.1.4), respectively).
For example, a blog writing activity may use a particular dataset and generate a bar chart.
By expressing usage and generation, one can construct provenance chains comprising both Activities and Entities.

In addition, we can say that an Activity prov:wasInformedBy (§4.1.9) another Activity to provide some dependency information without explicitly providing the activities' start and end times.
A prov:wasInformedBy relation between Activities suggests that the informed Activity used an Entity that was generated by the informing
Activity, but the Entity itself is unknown or is not of interest.
So, the prov:wasInformedBy property allows the construction of provenance chains comprising only Activities.

Provenance chains comprising only Entities can be formed using the prov:wasDerivedFrom (§4.1.5) property.
A derivation is a transformation of one entity into another. For example, if the Activity that created the bar chart is not known or is not of interest,
then we can say that the bar chart prov:wasDerivedFrom the dataset.
Arbitrary RDF properties can be used to describe the fixed aspects of an Entity that are interesting within a particular application (for example,
the file size and format of the dataset, or the aspect ratio of the bar chart).

While the properties prov:used, prov:wasGeneratedBy, prov:wasInformedBy, and prov:wasDerivedFrom can be used to construct provenance chains among
Activities and Entities, Agents may also be ascribed responsibility for any Activity or Entity within a provenance chain.
An Agent's responsibility for an Activity or Entity is described using the properties prov:wasAssociatedWith (§4.1.11) and prov:wasAttributedTo (§4.1.6), respectively.
Agents can also be responsible for other Agents' actions. In this case of delegation, the influencing Agent prov:actedOnBehalfOf (§4.1.12) another Agent that also bears responsibility for the influenced Activity or Entity.

The properties rdf:type and rdfs:label are used to express [prov:type](https://dvcs.w3.org/hg/prov/raw-file/default/model/prov-dm.html#term-attribute-type) and [prov:label](https://dvcs.w3.org/hg/prov/raw-file/default/model/prov-dm.html#term-attribute-label), respectively.

![PROV-O Starting Point terms](https://www.w3.org/TR/prov-o/diagrams/starting-points.svg)

Figure 1.
The three Starting Point classes and the properties that relate them.
The diagrams in this document depict Entities as yellow ovals,
Activities as blue rectangles, and Agents as orange pentagons.
The responsibility properties are shown in pink.
> **Example:**
>
> Example 1: The following PROV-O describes the resources involved when creating a chart about crime statistics. The example uses only Starting Point terms and serves as a basis for elaboration that will be described in subsequent sections. In the example, Derek performs an aggregation of some government crime data, grouping by national regions that are described in a separate dataset by a civil action group.
>
> ```
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.org#> .
>
> :bar_chart
>    a prov:Entity;
>    prov:wasGeneratedBy  :illustrationActivity;
>    prov:wasDerivedFrom  :aggregatedByRegions;
>    prov:wasAttributedTo :derek;
> .
>
> :derek
>    a foaf:Person, prov:Agent;
>    foaf:givenName       "Derek";
>    foaf:mbox            <mailto:derek@example.org>;
>    prov:actedOnBehalfOf :natonal_newspaper_inc;
> .
>
> :national_newspaper_inc
>    a foaf:Organization, prov:Agent;
>    foaf:name "National Newspaper, Inc.";
> .
>
> :illustrationActivity
>    a prov:Activity;
>    prov:used              :aggregatedByRegions;
>    prov:wasAssociatedWith :derek;
>    prov:wasInformedBy     :aggregationActivity;
> .
>
> :aggregatedByRegions
>    a prov:Entity;
>    prov:wasGeneratedBy  :aggregationActivity;
>    prov:wasAttributedTo :derek;
> .
>
> :aggregationActivity
>    a prov:Activity;
>    prov:startedAtTime    "2011-07-14T01:01:01Z"^^xsd:dateTime;
>    prov:wasAssociatedWith :derek;
>    prov:used              :crimeData;
>    prov:used              :nationalRegionsList;
>    prov:endedAtTime      "2011-07-14T02:02:02Z"^^xsd:dateTime;
> .
>
> :crimeData
>    a prov:Entity;
>    prov:wasAttributedTo :government;
> .
> :government a foaf:Organization, prov:Agent .
>
> :nationalRegionsList
>    a prov:Entity;
>    prov:wasAttributedTo :civil_action_group;
> .
> :civil_action_group a foaf:Organization, prov:Agent .
> ```

The example states that the agent `:derek` was associated with two
activities: `:aggregationActivity` and `:illustrationActivity`. The
activity `:aggregationActivity` used
the entities `:crimeData` (a crime statistics dataset) and `:nationalRegionsList` (a list of national regions), and
generated a new entity, `:aggregatedByRegions` that aggregates the statistics in `:crimeData` according to the regions in `:nationalRegionsList`.
The `:aggregatedByRegions` entity was then used by the `:illustrationActivity` activity,
to generate a new entity `:bar_chart` that depicts the aggregated statistics.

The example also states that the activity `:illustrationActivity` was
informed by the activity `:aggregationActivity`. Indeed, the former used
the entity `:aggregatedByRegions`, which was generated by the latter.

Because the agent `:derek` was associated with the activities `:aggregationActivity` and `:illustrationActivity`, the entities
generated by these activities, i.e., `:aggregatedByRegions` and `:bar_chart`, were also
attributed to him.

Finally, the example states that the agent `:derek` acted on behalf of the organization `:national_newspaper_inc`.

![Illustration of Derek making a bar chart from some aggregated government data.](https://www.w3.org/TR/prov-o/diagrams/starting-points-example.svg)

Figure 2.
A graphical illustration of the PROV-O in Example 1,
showing how the three Starting Point classes relate.
The diagrams in this document depict Entities as yellow ovals, Activities as blue rectangles,
and Agents as orange pentagons. The responsibility properties are shown in pink.

### 3.2 Expanded Terms

The terms introduced in this section provide additional ways to describe the provenance among Entities, Activities, and Agents.
The additional terms are illustrated in the following figure and can be separated into five different categories.

![PROV-O Starting Point terms](https://www.w3.org/TR/prov-o/diagrams/expanded.svg)

Figure 3.
The expanded terms build upon those in the Starting Points section (§3.1).
The diagrams in this document depict Entities as yellow ovals, Activities as blue rectangles, and Agents as orange pentagons.
The domain of prov:atLocation (§4.2.22) (prov:Activity or prov:Entity or prov:Agent or prov:InstantaneousEvent) is not illustrated.

The **first** category extends the §3.1 Starting Point Terms with subclasses, subproperties, and a superproperty.

Three subclasses of Agent (prov:Person (§4.2.4), prov:Organization (§4.2.6), and prov:SoftwareAgent (§4.2.5)) and
three subclasses of Entity are provided (prov:Collection (§4.2.1), prov:Bundle (§4.2.3),
and prov:Plan (§4.3.17)).

A prov:Collection is an Entity that provides a structure (e.g. set, list, etc.) to some constituents (which are themselves Entities).
The prov:Collection class can be used to express the provenance of the collection itself:
e.g. who maintained the collection, which members it contained as it evolved, and how it was assembled.
The prov:hadMember (§4.2.17) property is used to assert membership in a collection.

A prov:Bundle is a named set of provenance descriptions, which may itself have provenance.
The named set of provenance descriptions may be expressed as PROV-O or any other form.
The subclass of Bundle that names a set of PROV-O assertions is not provided by PROV-O, since it is more appropriate to do so using other recommendations,
standards, or technologies. In any case, a Bundle of PROV-O assertions is an abstract set of RDF triples, and adding or removing a triple creates a new distinct
Bundle of PROV-O assertions.

A prov:Plan is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals.

More general and more specific properties are also provided by the expanded terms. More generally, the property prov:wasInfluencedBy (§4.3.21) is a superproperty that relates any influenced Entity, Activity, or Agent to any other
influencing Entity, Activity, or Agent that had an effect on its characteristics.

Three subproperties of prov:wasDerivedFrom are also provided for certain kinds of derivation among Entities: prov:wasQuotedFrom (§4.2.13) cites a potentially larger Entity (such as a book, blog, or image) from which a new Entity was created
by repeating some or all of the original, prov:wasRevisionOf (§4.2.14) indicates that the derived Entity contains substantial content from the original Entity
(e.g., two editions of a book), and prov:hadPrimarySource (§4.2.11) cites a preceding Entity produced by some agent with direct experience and
knowledge about the topic (such as a reading from a sensor, or a journal written during an historical event).

The **second** category of expanded terms relates Entities according to their levels of abstraction, where some Entities may present more specific aspects than their more general counterparts.
While prov:specializationOf (§4.2.9) links a more specific Entity to a more general one (e.g., today's BBC news home page versus BBC's news home page on any day), prov:alternateOf (§4.2.8) links Entities that present aspects of the same thing, but not necessarily the same aspects or at the same time (e.g., the serialization of a document in different formats or a backup copy of a computer file).

The **third** category of expanded terms allows further description of Entities. The property prov:value (§4.2.12) provides a literal value that is a direct representation of an entity.
For example, the prov:value of a quote could be a string of the sentences stated, or the prov:value of an Entity involved in a numeric calculation could be the xsd:integer four.
The property prov:atLocation (§4.2.22) can be used to describe the prov:Location (§4.2.7) of any
Entity, Activity, Agent, or prov:InstantaneousEvent (§4.3.19) (i.e., the starting or ending of an activity or the generation, usage, or invalidation of an entity).
The properties used to describe instances of prov:Location are outside the scope of PROV-O;
reuse of other existing vocabulary is encouraged.

The **fourth** category of expanded terms describes the lifetime of an Entity beyond being **generated** by an Activity and **used** by other Activities. For example, a painting could not have been displayed before it was painted, and it could not be sold after it was destroyed by fire.
Similar to how Activities have start and end times, an Entity may be bound by points in time for which it was generated or is no longer usable.
The properties prov:generatedAtTime (§4.2.10) and prov:invalidatedAtTime (§4.2.15) can be used to bound the starting and ending moments of an Entity's existence. The Activities that led to the generation or invalidation of an Entity can be provided using prov:wasGeneratedBy and prov:wasInvalidatedBy (§4.2.16), respectively. prov:generated (§4.2.23) and prov:invalidated (§4.2.20) are the inverses of prov:wasGeneratedBy and prov:wasInvalidatedBy, respectively, and are defined to facilitate Activity-as-subject as well as Entity-as-subject descriptions.
For more about inverses, see the Appendix B (§B).

The **fifth** category of expanded terms describes the lifetime of an Activity beyond its start and end times and predecessor Activities.
Activities may also be started or ended by Entities, which are described using the properties prov:wasStartedBy (§4.2.18) and prov:wasEndedBy (§4.2.19), respectively. Since Entities may start or end Activities, and Agents may be Entities,
then Agents may also start or end Activities.
> **Example:**
>
> The following examples illustrate the expanded terms by elaborating the crime chart example from the previous section.
> After aggregating the dataset and creating the chart, Derek published a post to exhibit his work.
>
> Example 2:
>
> ```
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix sioc: <http://rdfs.org/sioc/ns#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix my:   <http://www.example.org/vocab#> .
> @prefix :     <http://www.example.org#> .
> @base         <http://www.example.com/derek-bundle.ttl> .
>
> <>
>    a prov:Bundle, prov:Entity;
>    prov:wasAttributedTo :postEditor;
>    prov:generatedAtTime "2011-07-16T02:52:02Z"^^xsd:dateTime;
> .
>
> :derek
>    a prov:Person, prov:Agent; ## prov:Agent is inferred from prov:Person
>    foaf:givenName       "Derek";
>    foaf:mbox            <mailto:derek@example.org>;
>    prov:actedOnBehalfOf :national_newspaper_inc;
> .
>
> :national_newspaper_inc
>    a prov:Organization, prov:Agent;        ## prov:Agent is inferred from prov:Organization
>    foaf:name "National Newspaper, Inc.";
> .
>
> :postEditor
>    a prov:SoftwareAgent, prov:Agent;       ## prov:Agent is inferred from prov:SoftwareAgent
>    foaf:name "Post Editor 3000";
> .
>
> :more-crime-happens-in-cities
>    a sioc:Post, prov:Entity;
>    sioc:latest_version   :post9821v2;
>    sioc:previous_version :post9821v1;
> .
>
> ## Version 1 of the post
>
> :post9821v1
>    a sioc:Post, prov:Entity;
>    prov:specializationOf  :more-crime-happens-in-cities; ## PERMALINK to the latest revision.
>    sioc:title             "More crime happens in cities";
>    prov:value             "I was currius...";            ## The text of this version (with a typo).
>    prov:generatedAtTime   "2011-07-16T01:52:02Z"^^xsd:dateTime;
>    prov:wasGeneratedBy    :publicationActivity1123;
>    prov:wasInfluencedBy   :aggregatedByRegions; ## This blog was influenced by Derek's data analysis.
>    prov:hadPrimarySource  :crimeData;           ## Derek's blog derives from the crime data originally
>                                                 ## gathered by the government.
>    prov:invalidatedAtTime "2011-07-16T02:02:02Z"^^xsd:dateTime;
> .
>
> :publicationActivity1123
>    a prov:Activity;
>    prov:startedAtTime     "2011-07-16T01:01:01Z"^^xsd:dateTime;
>    prov:wasStartedBy      :derek;
>    prov:wasAssociatedWith :postEditor;
>    prov:generated         :post9821v1;
>    prov:endedAtTime       "2011-07-16T01:52:02Z"^^xsd:dateTime;
>    prov:wasEndedBy        :derek;
> .
>
> :aggregatedByRegions
>    a prov:Entity;
>    prov:atLocation <file://Users/aggr.txt>;
> .
> <file://Users/aggr.txt> a prov:Location .
>
> :crimeData
>    a prov:Entity;
>    prov:wasAttributedTo :government;
> .
> :government
>    a prov:Organization, prov:Agent;
> .
>
> ## Version 2 of the post
>
> :post9821v2
>    a sioc:Post, prov:Entity;
>    prov:specializationOf :more-crime-happens-in-cities; ## PERMALINK to the latest revision.
>    prov:value            "I was curious...";            ## The text of this version (with fixed typo).
>    prov:generatedAtTime  "2011-07-16T02:02:02Z"^^xsd:dateTime;
>    prov:wasRevisionOf    :post9821v1;
>    prov:alternateOf      :post9821v1;
> .
> ```

Agent `:derek`, acting again on behalf of the `:national_newspaper_inc` organization,
used the `:postEditor` tool to publish a post about his recent data analysis `:aggregatedByRegions`.
The blog editing tool tracked Derek's actions as PROV-O assertions and published them as a Bundle (the current file `<>`).
The tool recorded that `:derek` started and ended the publishing activity (`:publicationActivity1123`)
that generated the post `:post9821v1`. The post
included a permanent link where the content of the latest version is available
(`:more-crime-happens-in-cities`) in addition to a textual snapshot of the current version (using prov:value).
Derek also included additional domain-specific descriptions of the post, such as its title.

Shortly after publishing the post, Derek noticed a typographical error in his narrative.
Because the fix would be minimal, he did not record the activity that led to the new version.
Instead, he related the new version (`:post9821v2`) as a revision of the previous (`:post9821v1`).
Since both versions of the blog are forms of the long-standing blog permalink `:more-crime-happens-in-cities`,
the revisions are alternates of one another and each is a prov:specializationOf (§4.2.9) of `:more-crime-happens-in-cities`.

![PROV-O Starting Point terms](https://www.w3.org/TR/prov-o/diagrams/expanded-terms-example-bundlePost.svg)

Figure 4.
An illustration of the PROV-O assertions in Example 2, where Derek
published two versions of a blog for the National Newspaper, Inc.
The diagrams in this document depict Entities as yellow ovals, Activities as blue rectangles,
and Agents as orange pentagons. The responsibility properties are shown in pink.
> **Example:**
>
> Shortly after Derek published his blog post, Monica adapted the text for a wider audience in a new post (`:post9822`).
> This rewrite is an alternate, abbreviated view of the same topic that Derek wrote about and was created from his original text.
> Since the provenance produced by the activities of Derek and Monica corresponded to different user views, the system
> automatically published it in a different prov:Bundle (§4.2.3).
> The tool also asserted provenance about the bundle that it produced (e.g., the date of creation, its creator, and the fact that it Derek's bundle was used).
> Because a bundle is a kind of entity, all provenance assertions that can be made about entities can also be made about bundles.
> The use of bundles enables the creation of provenance of provenance.
>
> Example 3:
>
> ```
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix sioc: <http://rdfs.org/sioc/ns#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://www.example.org#> .
> @base         <http://www.example.com/monica-bundle.ttl> .
>
> <>
>    a prov:Bundle, prov:Entity;
>    prov:wasAttributedTo :postEditor;
>    prov:wasDerivedFrom  <http://www.example.com/derek-bundle.ttl> .
>    prov:generatedAtTime "2011-07-16T03:03:03Z"^^xsd:dateTime;
> .
>
> :monica
>    a prov:Person, prov:Agent;
>    foaf:givenName "Monica";
>    foaf:mbox      <mailto:monica@example.org>;
> .
>
> ## Revised post for a different audience is a new resource.
>
> :post9822
>    a sioc:Post, prov:Entity;
>    sioc:title "More crime happens in cities (for dummies)";
>    prov:wasAttributedTo  :monica,
>                          :postEditor;
>    prov:alternateOf      :more-crime-happens-in-cities;    ## This post is an alternate of Derek's blog.
>    prov:value            "A quick overview of Derek's..."; ## Snapshot with the content of this version
>    prov:wasRevisionOf    :post9821v2;                      ## Monica rewrote Derek's version 2 to create hers.
> .
> ```
> **Example:**
>
> After some time, John wrote his own conclusions in his own post (`:post19201`) quoting the previous two posts.
> Each quote that John makes (`:quote_from_monica` and `:quote_from_derek`) is a new entity derived from the
> previous blogs and is annotated with the time that the quote was taken.
> The provenance of John's blog notes that his post is the result of the quotes that he took from Derek and Monica.
> The blog post is also derived from Derek's `:aggregatedByRegions` dataset because John inspected it and found a
> concern that he discusses in his blog. All the provenance statements related to John's post are grouped in a new prov:Bundle.
>
> Example 4:
>
> ```
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix sioc: <http://rdfs.org/sioc/ns#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://www.example.org#> .
> @base         <http://www.example.com/john-bundle.ttl> .
>
> <>
>    a prov:Bundle, prov:Entity;
>    prov:wasAttributedTo :postEditor;
>    prov:wasDerivedFrom <http://www.example.com/derek-bundle.ttl>,
>                        <http://www.example.com/monica-bundle.ttl>;
>    prov:generatedAtTime "2012-08-08T08:08:08Z"^^xsd:dateTime;
> .
>
> :publicationActivity1124
>    a prov:Activity;
>    prov:wasAttributedTo :postEditor,
>                         :john;
>    prov:generated :post19201;
> .
>
> :post19201
>    a sioc:Post, prov:Entity;
>    prov:wasAttributedTo :john;
>    prov:value "I'm not so sure that...";
>    prov:wasDerivedFrom :quote_from_derek,
>                        :quote_from_monica,
>                        :aggregatedByRegions;
>    prov:wasGeneratedBy :publicationActivity1124;
> .
>
> :john
>    a prov:Person, prov:Agent;
>    foaf:name "John";
> .
>
> :quote_from_derek
>    a prov:Entity;
>    prov:value "Analysis of the datasets demonstrates that there is more crime.";
>    prov:wasQuotedFrom   :more-crime-happens-in-cities;
>    prov:generatedAtTime "2012-08-08T01:01:01Z"^^xsd:dateTime;
> .
>
> :quote_from_monica
>    a prov:Entity;
>    prov:value "In summary, there are clearly more crimes in the country.";
>    prov:wasQuotedFrom   :post9822;
>    prov:generatedAtTime "2012-08-08T02:02:02Z"^^xsd:dateTime;
> .
> ```
> **Example:**
>
> Unfortunately, there was a problem in the servers where `:post19201` was being stored, and all the data related to the post was lost permanently.
> Thus, the system invalidated the entity automatically and notified John about the error.
>
> Example 5:
>
> ```
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix sioc: <http://rdfs.org/sioc/ns#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.org#> .
>
> :post19201
>    a sioc:Post, prov:Entity;
>    prov:invalidatedAtTime "2012-09-02T01:31:00Z"^^xsd:dateTime;
>    prov:wasInvalidatedBy :hard_disk_failure;
> .
>
> :hard_disk_failure
>    a prov:Activity;
>    prov:endedAtTime "2012-09-02T01:31:00Z"^^xsd:dateTime;
> .
> ```

### 3.3 Qualified Terms

The Qualified Terms category is the result of
applying the **Qualification Pattern** [LD-Patterns-QR] to the simple (unqualified)
relations available in the Starting Point and Expanded categories.
The terms in this category are for users who wish to provide further details about the provenance-related influence among
Entities, Activities, and Agents.

The Qualification Pattern restates an unqualified influence
relation by using an intermediate class that represents the influence between two resources.
This new instance, in turn, can be annotated with additional descriptions of the influence that one resource had upon another.
The following two tables list the influence relations that can be qualified using the Qualification Pattern, along with the properties used to qualify them.

For example, the second row of the first table indicates that to elaborate how an prov:Activity prov:used a particular prov:Entity, one creates an instance of prov:Usage that indicates the influencing entity with the prov:entity property.
Meanwhile, the influenced prov:Activity indicates the prov:Usage with the property prov:qualifiedUsage.
The resulting structure that qualifies the an Activity's usage of an Entity is illustrated in Figure 4a below.

Seven Starting Point (§3.1) relations can be further described using the Qualification Pattern.
They are listed in the following normative table.

*Table 2: Qualification Property and Qualified Influence Class used to qualify a Starting\-point Property.*

| Influenced Class                                                                             | Unqualified Influence                                                                                                   | Influencing Class                                                                            | Qualification Property                                                                                                                 | Qualified Influence                                                                                         | Influencer Property                                                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| prov:Entity (§4.1.1)       | prov:wasGeneratedBy (§4.1.4)          | prov:Activity (§4.1.2) | prov:qualifiedGeneration (§4.3.23)          | prov:Generation (§4.3.11)          | prov:activity (§4.3.40) |
| prov:Entity (§4.1.1)       | prov:wasDerivedFrom (§4.1.5)          | prov:Entity (§4.1.1)       | prov:qualifiedDerivation (§4.3.24)          | prov:Derivation (§4.3.6)          | prov:entity (§4.3.37)       |
| prov:Entity (§4.1.1)       | prov:wasAttributedTo (§4.1.6)       | prov:Agent (§4.1.3)          | prov:qualifiedAttribution (§4.3.28)       | prov:Attribution (§4.3.15)       | prov:agent (§4.3.41)          |
| prov:Activity (§4.1.2) | prov:used (§4.1.8)                                        | prov:Entity (§4.1.1)       | prov:qualifiedUsage (§4.3.31)                         | prov:Usage (§4.3.3)                         | prov:entity (§4.3.37)       |
| prov:Activity (§4.1.2) | prov:wasInformedBy (§4.1.9)             | prov:Activity (§4.1.2) | prov:qualifiedCommunication (§4.3.32) | prov:Communication (§4.3.12) | prov:activity (§4.3.40) |
| prov:Activity (§4.1.2) | prov:wasAssociatedWith (§4.1.11) | prov:Agent (§4.1.3)          | prov:qualifiedAssociation (§4.3.33)       | prov:Association (§4.3.16)       | prov:agent (§4.3.41)          |
| prov:Agent (§4.1.3)          | prov:actedOnBehalfOf (§4.1.12)       | prov:Agent (§4.1.3)          | prov:qualifiedDelegation (§4.3.35)          | prov:Delegation (§4.3.18)          | prov:agent (§4.3.41)          |

Seven Expanded (§3.2) relations can be further described using the Qualification Pattern.
They are listed in the following normative table.

*Table 3: Qualification Property and Qualified Influence Class used to qualify an Expanded Property.*

| Influenced Class                                                                                                                                                                                         | Unqualified Influence                                                                                                | Influencing Class                                                                                                                                                                                        | Qualification Property                                                                                                                 | Qualified Influence                                                                                         | Influencer Property                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| prov:Entity (§4.1.1) or prov:Activity (§4.1.2) or prov:Agent (§4.1.3) | prov:wasInfluencedBy (§4.3.21)                          | prov:Entity (§4.1.1) or prov:Activity (§4.1.2) or prov:Agent (§4.1.3) | prov:qualifiedInfluence (§4.3.22)                                   | prov:Influence (§4.3.1)                                   | prov:influencer (§4.3.36)                   |
| prov:Entity (§4.1.1)                                                                                                                   | prov:hadPrimarySource (§4.2.11) | prov:Entity (§4.1.1)                                                                                                                   | prov:qualifiedPrimarySource (§4.3.25) | prov:PrimarySource (§4.3.7) | prov:entity (§4.3.37)       |
| prov:Entity (§4.1.1)                                                                                                                   | prov:wasQuotedFrom (§4.2.13)          | prov:Entity (§4.1.1)                                                                                                                   | prov:qualifiedQuotation (§4.3.26)             | prov:Quotation (§4.3.8)             | prov:entity (§4.3.37)       |
| prov:Entity (§4.1.1)                                                                                                                   | prov:wasRevisionOf (§4.2.14)          | prov:Entity (§4.1.1)                                                                                                                   | prov:qualifiedRevision (§4.3.27)                | prov:Revision (§4.3.9)                | prov:entity (§4.3.37)       |
| prov:Entity (§4.1.1)                                                                                                                   | prov:wasInvalidatedBy (§4.2.16) | prov:Activity (§4.1.2)                                                                                                             | prov:qualifiedInvalidation (§4.3.29)    | prov:Invalidation (§4.3.13)    | prov:activity (§4.3.40) |
| prov:Activity (§4.1.2)                                                                                                             | prov:wasStartedBy (§4.2.18)             | prov:Entity (§4.1.1)                                                                                                                   | prov:qualifiedStart (§4.3.30)                         | prov:Start (§4.3.4)                         | prov:entity (§4.3.37)       |
| prov:Activity (§4.1.2)                                                                                                             | prov:wasEndedBy (§4.2.19)                   | prov:Entity (§4.1.1)                                                                                                                   | prov:qualifiedEnd (§4.3.34)                               | prov:End (§4.3.5)                               | prov:entity (§4.3.37)       |

The qualification classes and properties shown in the previous two tables can also be found in the normative cross reference (§4) in the next section of this document.

All influence classes (e.g. prov:Association, prov:Usage) are extensions of prov:Influence (§4.3.1) and either prov:EntityInfluence (§4.3.2), prov:ActivityInfluence (§4.3.10), or prov:AgentInfluence (§4.3.14), which determine the property used to cite the influencing resource (either prov:entity (§4.3.37), prov:activity (§4.3.40), or prov:agent (§4.3.41), respectively).
Because prov:Influence is a broad relation, its most specific subclasses (e.g. prov:Communication, prov:Delegation, prov:End, prov:Revision, etc.) should be used when applicable.
> **Example:**
>
> Example 6:
>
> For example, given the unqualified statement:
>
> ```
> :e1
>    a prov:Entity;
>    prov:wasGeneratedBy :a1;
> .
>
> :a1 a prov:Activity .
> ```

One can find that prov:wasGeneratedBy (§4.1.4) can be qualified using the qualification property prov:qualifiedGeneration (§4.3.23),
the class prov:Generation (§4.3.11) (a subclass of prov:ActivityInfluence (§4.3.10)),
and the property prov:activity (§4.3.40).
From this, the influence relation above can be restated with the *qualification pattern* as:
> **Example:**
>
> Example 7:
>
> ```
> :e1
>    a prov:Entity;
>    prov:wasGeneratedBy      :a1;
>    prov:qualifiedGeneration :e1Gen; # Add the qualification.
> .
>
> :e1Gen
>    a prov:Generation;
>    prov:activity            :a1;    # Cite the influencing Activity.
>    ex:foo                   :bar;   # Describe the Activity :a1's influence upon the Entity :e1.
> .
>
> :a1 a prov:Activity .
> ```

The asserter can thus attach additional properties to `:e1Gen` to describe the generation of `:e1` by `:a1`.

As can be seen in this example, qualifying an influence relation provides a second form (e.g. `:e1 prov:qualifiedGeneration :e1Gen`) to express an equivalent influence relation
(e.g. `:e1 prov:wasGeneratedBy :a1`).
It is correct and acceptable for an implementer to use either qualified or unqualified forms as they choose (or both),
and a consuming application should be prepared to recognize either form.
Consuming applications *should* recognize both qualified and unqualified forms, and treat the qualified form as implying the unqualified form.
Because the qualification form is more verbose, the unqualified form should be favored in cases where additional properties are not provided.
When the qualified form is expressed, including the equivalent unqualified form can facilitate PROV-O consumption, and is thus encouraged.

In addition to the previous two tables, Figure 4 illustrates the classes and properties needed to apply the qualification pattern to ten of the fourteen qualifiable influence relations.

For example, while prov:qualifiedUsage (§4.3.31), prov:Usage (§4.3.3), and prov:entity (§4.3.37) are used to qualify prov:used relations, prov:qualifiedAssociation (§4.3.33), prov:Association (§4.3.16),
and prov:agent (§4.3.41) are used to qualify prov:wasAssociatedWith relations. This pattern applies to the twelve other influence relations that can be qualified.

In subfigure **a** the prov:qualifiedUsage property parallels the prov:used property and references an instance of prov:Usage, which in turn provides attributes of the prov:used relation between the Activity and Entity.
The prov:entity property is used to cite the Entity that was used by the Activity.
In this case, the time that the Activity used the Entity is provided using the prov:atTime (§4.3.44) property and a literal xsd:dateTime value. The prov:atTime property can be used to describe any prov:InstantaneousEvent (§4.3.19) (including prov:Start (§4.3.4), prov:Generation (§4.3.11), prov:Usage (§4.3.3), prov:Invalidation (§4.3.13), and prov:End (§4.3.5)).

Similarly in subfigure **j**, the prov:qualifiedAssociation property parallels the prov:wasAssociatedWith property and references an instance of prov:Association, which in turn provides attributes of the prov:wasAssociatedWith relation between the Activity and Agent. The prov:agent property is used to cite the Agent that influenced the Activity.
In this case, the plan of actions and steps that the Agent used to achieve its goals is provided using the prov:hadPlan (§4.3.42) property and an instance of prov:Plan (§4.3.17). Further, the prov:hadRole (§4.3.45) property and prov:Role (§4.3.20) class can be used to describe the function that the agent served with respect to the Activity.
Both prov:Plan and prov:Role are left to be extended by applications.

![Express association between an activity and an agent using a binary relationship and an alternatie qualified relationship](https://www.w3.org/TR/prov-o/diagrams/qualified-patterns.svg)

Figure 4:
Illustration of the properties and classes to use (in blue)
to qualify the starting point (§3.1) and expanded (§3.2) influence relations (**dotted black**).
The diagrams in this document depict Entities as ovals, Activities as rectangles, and Agents as pentagons. Quotation (§4.3.8), Revision (§4.3.9), and PrimarySource (§4.3.7) are omitted because they are special forms of Derivation (§4.3.6) and follow the same pattern as subfigure **g**.

The following two examples show the result of applying the Usage and Association patterns to the chart-making example from Section 3.1 (§3.1).
> **Example:**
>
> Example 8:
>
> > **Example:**
> >
> > **Qualified Usage**
> >
> > The prov:qualifiedUsage property parallels the prov:used property to provide an additional description to `:illustrationActivity`. The instance of prov:Usage cites the data used (`:aggregatedByRegions`) and the time the activity used it (`2011-07-14T03:03:03Z`).
> >
> > ```
> > @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> > @prefix prov: <http://www.w3.org/ns/prov#> .
> > @prefix :     <http://example.org#> .
> >
> > :illustrationActivity
> >    a prov:Activity;                ## Using Starting Point terms,
> >    prov:used :aggregatedByRegions; ##   the illustration activity used the aggregated data (to create the bar chart).
> > .
> >
> > :aggregatedByRegions a prov:Entity .
> >
> > :illustrationActivity
> >    prov:qualifiedUsage [                                ## Qualify how the :illustrationActivity
> >       a prov:Usage;                                     ##   used
> >       prov:entity :aggregatedByRegions;                 ##     the Entity :aggregatedByRegions
> >
> >       prov:atTime "2011-07-14T03:03:03Z"^^xsd:dateTime; ## Qualification: The aggregated data was used
> >                                                         ##   at a particular time to create the bar chart..
> >    ];
> > .
> > ```
> **Example:**
>
> Example 9:
>
> > **Example:**
> >
> > **Qualified Association**
> >
> > The prov:qualifiedAssociation property parallels the prov:wasAssociatedWith property to provide an additional description about the `:illustrationActivity` that Derek influenced.
> > The instance of prov:Association cites the influencing agent (`:derek`) that followed the instructions (`:tutorial_blog`).
> > Further, Derek served the role of `:illustrationist` during the activity.
> >
> > ```
> > @prefix prov: <http://www.w3.org/ns/prov#> .
> > @prefix :     <http://example.org#> .
> >
> > :illustrationActivity
> >    a prov:Activity;                ## Using Starting Point terms,
> >    prov:wasAssociatedWith :derek;  ##   the illustration activity was associated with Derek in some way.
> > .
> >
> > :derek a prov:Agent .
> >
> > :illustrationActivity
> >    prov:qualifiedAssociation [       ## Qualify how the :illustrationActivity
> >       a prov:Association;            ##   was associated with
> >       prov:agent   :derek            ##     the Agent Derek.
> >
> >       prov:hadRole :illustrationist; ## Qualification: The role that Derek served.
> >       prov:hadPlan :tutorial_blog;   ## Qualification: The plan (or recipe, instructions)
> >                                      ##   that Derek followed when creating the graphical chart.
> >    ];
> > .
> >
> > :tutorial_blog   a prov:Plan, prov:Entity .
> > :illustrationist a prov:Role .
> > ```

This section finishes with two more examples of qualification as applied to the chart-making example from Section 3.1 (§3.1).
> **Example:**
>
> Example 10:
>
> > **Example:**
> >
> > **Qualified Generation**
> >
> > The prov:qualifiedGeneration property parallels the prov:wasGeneratedBy property to provide an additional description to `:bar_chart`. The instance of prov:Generation cites the time (2011-07-14T15:52:14Z) that the activity (`:illustrationActivity`) generated the chart (`:bar_chart`).
> >
> > ```
> > @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> > @prefix prov: <http://www.w3.org/ns/prov#> .
> > @prefix :     <http://example.org#> .
> >
> > :bar_chart
> >    a prov:Entity;                              ## Using Starting Point terms,
> >    prov:wasGeneratedBy :illustrationActivity;  ##   the chart was generated in an illustration activity.
> > .
> >
> > :illustrationActivity a prov:Activity .
> >
> > :bar_chart
> >    prov:qualifiedGeneration [                           ## Qualify how the :bar_chart
> >       a prov:Generation;                                ##   was generated by
> >       prov:activity :illustrationActivity;              ##     the Activity :illustrationActivity.
> >
> >       prov:atTime "2011-07-14T15:52:14Z"^^xsd:dateTime; ## Qualification: The Activity generated
> >                                                         ##   the bar_chart at a particular time.
> >    ];
> > .
> > ```
> **Example:**
>
> Example 11:
>
> > **Example:**
> >
> > **Qualified Derivation**
> >
> > The prov:qualifiedDerivation property parallels the prov:wasDerivedFrom property to provide an additional description to `:bar_chart`. The instance of prov:Derivation cites the activity (`:illustrationActivity`) and the Usages and Generations that the activity conduced to create the `:bar_chart`.
> >
> > ```
> > @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> > @prefix prov: <http://www.w3.org/ns/prov#> .
> > @prefix :     <http://example.org#> .
> >
> > :bar_chart
> >    a prov:Entity;                             ## Using Starting Point terms,
> >    prov:wasDerivedFrom :aggregatedByRegions;  ##   the chart was derived from the aggregated dataset.
> > .
> >
> > :aggregatedByRegions a prov:Entity .
> >
> > :bar_chart
> >    prov:qualifiedDerivation [                      ## Qualify
> >       a prov:Derivation;                           ##   how :bar_chart was derived from
> >       prov:entity        :aggregatedByRegions;     ##     the dataset Entity :aggregatedByRegions.
> >
> >       prov:hadActivity   :aggregating_activity;    ## Qualification: The activity that derived the :bar_chart.
> >       prov:hadUsage      :use_of_aggregatedData;   ## Qualification: How the activity used :aggregatedByRegions.
> >       prov:hadGeneration :generation_of_bar_chart; ## Qualification: How the activity generated the :bar_chart.
> >    ];
> > .
> > ```

## 4. Cross reference for PROV-O classes and properties

This section provides details for each class and property defined by the PROV Ontology, grouped by the categories described above:

- §4.1 Starting Point Terms
- §4.2 Expanded Terms
- §4.3 Qualified Terms

The superscripts op and dp denote that a property is an OWL [object property](https://www.w3.org/TR/owl2-syntax/#Object_Properties) or [data property](https://www.w3.org/TR/owl2-syntax/#Data_Properties), respectively.

Each PROV-O term in this cross reference links to the corresponding PROV-DM concept. The PROV-DM's table [Cross-References to PROV-O and PROV-N](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#prov-dm-to-prov-o-and-prov-n) provides an overview of the correspondences between PROV-O and PROV-DM.

The qualification classes and properties shown in Table 2 and Table 3 of the previous section can also be found in each entry of this cross reference.
If the property can be qualified, the **can be qualified with** header indicates the qualifying property and influence class that should be used.
Conversely, the **qualifies** headers in the listings for qualification terms indicate the unqualified property that they qualify.
In the OWL file itself, the annotation properties prov:qualifiedForm and prov:unqualifiedForm provide the same linkages between the unqualified properties and their qualifiying terms.

Most examples shown in this cross reference are encoded using the Turtle RDF serialization.
When it is convenient to do so (e.g., when an example describes a prov:Bundle), it may use the [TRIG] syntax.
Although this document does not specify how to encode Bundles in RDF, TriG's named graph construct is used only to illustrate the concept of
creating a named set of PROV assertions. Note that all examples are non-normative (§1.1).

### 4.1 Starting Point Terms

The classes and properties that provide a basis for all other PROV-O terms are discussed in Section 3.1 (§3.1).

- prov:Entity (§4.1.1)
- prov:Activity (§4.1.2)
- prov:Agent (§4.1.3)

- prov:wasGeneratedBy (§4.1.4)
- prov:wasDerivedFrom (§4.1.5)
- prov:wasAttributedTo (§4.1.6)
- prov:startedAtTime (§4.1.7)
- prov:used (§4.1.8)
- prov:wasInformedBy (§4.1.9)
- prov:endedAtTime (§4.1.10)
- prov:wasAssociatedWith (§4.1.11)
- prov:actedOnBehalfOf (§4.1.12)

### (1) Class: prov:Entity (§4.1.1) back to starting-point classes

**IRI:** http://www.w3.org/ns/prov#Entity

An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:     <http://www.w3.org/2002/07/owl#> .
> @prefix dcterms: <http://purl.org/dc/terms/> .
> @prefix prov:    <http://www.w3.org/ns/prov#> .
> @prefix :        <http://example.com/> .
>
> :bar_chart
>    a prov:Entity;
>    dcterms:title "Aggregated statistics from the crime file"^^xsd:string;
>    prov:wasAttributedTo :derek;
> .
>
> :derek a prov:Agent .
> ```

described with properties:

prov:invalidatedAtTime (§4.2.15) dp , prov:wasAttributedTo (§4.1.6) op , prov:qualifiedGeneration (§4.3.23) op , prov:wasGeneratedBy (§4.1.4) op , prov:wasDerivedFrom (§4.1.5) op , prov:specializationOf (§4.2.9) op , prov:qualifiedDerivation (§4.3.24) op , prov:qualifiedInvalidation (§4.3.29) op , prov:generatedAtTime (§4.2.10) dp , prov:qualifiedQuotation (§4.3.26) op , prov:hadPrimarySource (§4.2.11) op , prov:qualifiedPrimarySource (§4.3.25) op , prov:alternateOf (§4.2.8) op , prov:value (§4.2.12) dp , prov:wasInvalidatedBy (§4.2.16) op , prov:qualifiedAttribution (§4.3.28) op , prov:wasQuotedFrom (§4.2.13) op , prov:qualifiedRevision (§4.3.27) op , prov:wasRevisionOf (§4.2.14) op

prov:wasInfluencedBy (§4.3.21) op , prov:qualifiedInfluence (§4.3.22) op , prov:atLocation (§4.2.22) op

in range of

prov:hadPrimarySource (§4.2.11) op prov:generated (§4.2.23) op prov:wasDerivedFrom (§4.1.5) op prov:entity (§4.3.37) op prov:specializationOf (§4.2.9) op prov:invalidated (§4.2.20) op prov:used (§4.1.8) op prov:hadMember (§4.2.17) op prov:alternateOf (§4.2.8) op prov:wasStartedBy (§4.2.18) op prov:wasQuotedFrom (§4.2.13) op prov:wasEndedBy (§4.2.19) op prov:wasRevisionOf (§4.2.14) op

has subclasses

prov:Collection (§4.2.1) , prov:Plan (§4.3.17) , prov:Bundle (§4.2.3)

PROV-DM term

[entity](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-entity "prov-dm")

### (2) Class: prov:Activity (§4.1.2) back to starting-point classes

**IRI:** http://www.w3.org/ns/prov#Activity

An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :graduation
>    a prov:Activity, :Graduation;
>    prov:startedAtTime "2012-04-15T13:00:00-04:00"^^xsd:dateTime;
>    prov:used          :ms_smith;
>    prov:generated     :doctor_smith;
>    prov:endedAtTime   "2012-04-15T14:30:00-04:00"^^xsd:dateTime;
> .
> :ms_smith     a prov:Entity .
> :doctor_smith a prov:Entity .
> ```

described with properties:

prov:generated (§4.2.23) op , prov:qualifiedAssociation (§4.3.33) op , prov:wasAssociatedWith (§4.1.11) op , prov:qualifiedEnd (§4.3.34) op , prov:wasEndedBy (§4.2.19) op , prov:qualifiedUsage (§4.3.31) op , prov:used (§4.1.8) op , prov:invalidated (§4.2.20) op , prov:endedAtTime (§4.1.10) dp , prov:qualifiedStart (§4.3.30) op , prov:wasInformedBy (§4.1.9) op , prov:wasStartedBy (§4.2.18) op , prov:startedAtTime (§4.1.7) dp , prov:qualifiedCommunication (§4.3.32) op

prov:wasInfluencedBy (§4.3.21) op , prov:qualifiedInfluence (§4.3.22) op , prov:atLocation (§4.2.22) op

in range of

prov:activity (§4.3.40) op prov:wasInformedBy (§4.1.9) op prov:wasGeneratedBy (§4.1.4) op prov:hadActivity (§4.3.43) op prov:wasInvalidatedBy (§4.2.16) op

PROV-DM term

[Activity](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Activity "prov-dm")

### (3) Class: prov:Agent (§4.1.3) back to starting-point classes

**IRI:** http://www.w3.org/ns/prov#Agent

An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix :     <http://example.com#> .
>
> :derek
>    a prov:Agent, prov:Person;
>    foaf:givenName      "Derek"^^xsd:string;
>    foaf:mbox           <mailto:derek@example.org>;
>    foaf:homePage       <http://derek.example.com>;
>    prov:actedOnBehalfOf :national_newspaper_inc;
> .
>
> :national_newspaper_inc
>    a prov:Agent, prov:Organization;
>    foaf:name "National Newspaper, Inc.";
> .
> ```

described with properties:

prov:actedOnBehalfOf (§4.1.12) op , prov:qualifiedDelegation (§4.3.35) op

prov:wasInfluencedBy (§4.3.21) op , prov:qualifiedInfluence (§4.3.22) op , prov:atLocation (§4.2.22) op

in range of

prov:actedOnBehalfOf (§4.1.12) op prov:agent (§4.3.41) op prov:wasAssociatedWith (§4.1.11) op prov:wasAttributedTo (§4.1.6) op

has subclasses

prov:Organization (§4.2.6) , prov:Person (§4.2.4) , prov:SoftwareAgent (§4.2.5)

PROV-DM term

[agent](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-agent "prov-dm")

### (4) Property: prov:wasGeneratedBy (§4.1.4) op back to starting-point properties

**IRI:** http://www.w3.org/ns/prov#wasGeneratedBy

Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :bar_chart
>    a prov:Entity;
>    prov:wasGeneratedBy :illustrating;
> .
>
> :illustrating a prov:Activity .
> ```

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Activity (§4.1.2)

can be qualified with

- prov:Generation (§4.3.11)
- prov:qualifiedGeneration (§4.3.23) op

PROV-DM term

[Generation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Generation "prov-dm")

### (5) Property: prov:wasDerivedFrom (§4.1.5) op back to starting-point properties

**IRI:** http://www.w3.org/ns/prov#wasDerivedFrom

A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> :bar_chart
>    a prov:Entity, ex:Barchart;
>    prov:wasDerivedFrom :aggregatedByRegions;
> .
>
> :aggregatedByRegions
>    a prov:Entity, ex:Dataset;
> .
> ```

The more specific subproperties of prov:wasDerivedFrom (i.e., prov:wasQuotedFrom, prov:wasRevisionOf, prov:hadPrimarySource) should be used when applicable.

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Entity (§4.1.1)

has sub-properties

- prov:hadPrimarySource (§4.2.11)
- prov:wasQuotedFrom (§4.2.13)
- prov:wasRevisionOf (§4.2.14)

can be qualified with

- prov:Derivation (§4.3.6)
- prov:qualifiedDerivation (§4.3.24) op

PROV-DM term

[Derivation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Derivation "prov-dm")

### (6) Property: prov:wasAttributedTo (§4.1.6) op back to starting-point properties

**IRI:** http://www.w3.org/ns/prov#wasAttributedTo

Attribution is the ascribing of an entity to an agent.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :geneSequencing
>    a prov:Activity;
>    prov:startedAtTime "2012-04-25T01:30:00Z"^^xsd:dateTime;
>    prov:used              :drosophilaSample-84;
>    prov:wasAssociatedWith :lab-technician-GH-32;
>    prov:endedAtTime   "2012-04-25T03:40:00Z"^^xsd:dateTime;
> .
>
> :drosophilaSample-84
>    a prov:Entity;
>    prov:wasAttributedTo :lab-technician-FE-56;
> .
>
> :lab-technician-GH-32 a prov:Agent .
> :lab-technician-FE-56 a prov:Agent .
> ```

Attribution is the ascribing of an entity to an agent.

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Agent (§4.1.3)

can be qualified with

- prov:qualifiedAttribution (§4.3.28) op
- prov:Attribution (§4.3.15)

PROV-DM term

[attribution](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-attribution "prov-dm")

### (7) Property: prov:startedAtTime (§4.1.7) dp back to starting-point properties

**IRI:** http://www.w3.org/ns/prov#startedAtTime

Start is when an activity is deemed to have been started by an entity, known as trigger. The activity did not exist before its start. Any usage, generation, or invalidation involving an activity follows the activity's start. A start may refer to a trigger entity that set off the activity, or to an activity, known as starter, that generated the trigger.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :geneSequencing
>    a prov:Activity;
>    prov:startedAtTime "2012-04-25T01:30:00Z"^^xsd:dateTime;
>    prov:used              :drosophilaSample-84;
>    prov:wasAssociatedWith :lab-technician-GH-32;
>    prov:endedAtTime   "2012-04-25T03:40:00Z"^^xsd:dateTime;
> .
>
> :drosophilaSample-84  a prov:Entity .
> :lab-technician-GH-32 a prov:Agent .
> ```

The time at which an activity started. See also prov:endedAtTime.

has domain

- prov:Activity (§4.1.2)

has range

- http://www.w3.org/2001/XMLSchema#dateTime

can be qualified with

- prov:Start (§4.3.4)
- prov:atTime (§4.3.44) dp

PROV-DM term

[Start](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Start "prov-dm")

### (8) Property: prov:used (§4.1.8) op back to starting-point properties

**IRI:** http://www.w3.org/ns/prov#used

Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :sortActivity
>    a prov:Activity;
>    prov:atTime     "2011-07-16T01:52:02Z"^^xsd:dateTime;
>    prov:used       :datasetA;
>    prov:generated  :datasetB;
> .
>
> :datasetA a prov:Entity.
> :datasetB a prov:Entity.
>
> # See qualified Usage for example on how the role of :datasetA can be described for this Activity
> ```

A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven .

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Entity (§4.1.1)

can be qualified with

- prov:Usage (§4.3.3)
- prov:qualifiedUsage (§4.3.31) op

PROV-DM term

[Usage](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Usage "prov-dm")

### (9) Property: prov:wasInformedBy (§4.1.9) op back to starting-point properties

**IRI:** http://www.w3.org/ns/prov#wasInformedBy

Communication is the exchange of an entity by two activities, one activity using the entity generated by the other.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :writing-celebrity-gossip
>    a prov:Activity;
>    prov:wasInformedBy :voicemail-interception;
> .
>
> :voicemail-interception a prov:Activity .
> ```

An activity a2 is dependent on or informed by another activity a1, by way of some unspecified entity that is generated by a1 and used by a2.

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Activity (§4.1.2)

can be qualified with

- prov:Communication (§4.3.12)
- prov:qualifiedCommunication (§4.3.32) op

PROV-DM term

[Communication](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Communication "prov-dm")

### (10) Property: prov:endedAtTime (§4.1.10) dp back to starting-point properties

**IRI:** http://www.w3.org/ns/prov#endedAtTime

End is when an activity is deemed to have been ended by an entity, known as trigger. The activity no longer exists after its end. Any usage, generation, or invalidation involving an activity precedes the activity's end. An end may refer to a trigger entity that terminated the activity, or to an activity, known as ender that generated the trigger.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :geneSequencing
>    a prov:Activity;
>    prov:startedAtTime "2012-04-25T01:30:00Z"^^xsd:dateTime;
>    prov:used              :drosophilaSample-84;
>    prov:wasAssociatedWith :lab-technician-GH-32;
>    prov:endedAtTime   "2012-04-25T03:40:00Z"^^xsd:dateTime;
> .
>
> :drosophilaSample-84  a prov:Entity .
> :lab-technician-GH-32 a prov:Agent .
> ```

The time at which an activity ended. See also prov:startedAtTime.

has domain

- prov:Activity (§4.1.2)

has range

- http://www.w3.org/2001/XMLSchema#dateTime

can be qualified with

- prov:End (§4.3.5)
- prov:atTime (§4.3.44) dp

PROV-DM term

[End](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-End "prov-dm")

### (11) Property: prov:wasAssociatedWith (§4.1.11) op back to starting-point properties

**IRI:** http://www.w3.org/ns/prov#wasAssociatedWith

An activity association is an assignment of responsibility to an agent for an activity, indicating that the agent had a role in the activity. It further allows for a plan to be specified, which is the plan intended by the agent to achieve some goals in the context of this activity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :illustrating
>    a prov:Activity;
>    prov:wasAssociatedWith :derek;
> .
>
> :derek a prov:Person, prov:Agent, prov:Entity .
> ```

An prov:Agent that had some (unspecified) responsibility for the occurrence of this prov:Activity.

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Agent (§4.1.3)

can be qualified with

- prov:Association (§4.3.16)
- prov:qualifiedAssociation (§4.3.33) op

PROV-DM term

[Association](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Association "prov-dm")

### (12) Property: prov:actedOnBehalfOf (§4.1.12) op back to starting-point properties

**IRI:** http://www.w3.org/ns/prov#actedOnBehalfOf

Delegation is the assignment of authority and responsibility to an agent (by itself or by another agent) to carry out a specific activity as a delegate or representative, while the agent it acts on behalf of retains some responsibility for the outcome of the delegated work.

For example, a student acted on behalf of his supervisor, who acted on behalf of the department chair, who acted on behalf of the university; all those agents are responsible in some way for the activity that took place but we do not say explicitly who bears responsibility and to what degree.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :derek
>    a prov:Agent;
>    foaf:givenName "Derek"^^xsd:string;
>    foaf:mbox      <mailto:derek@example.org>;
>    prov:actedOnBehalfOf :national_newspaper_inc;
> .
>
> :national_newspaper_inc
>    a prov:Agent, prov:Organization;
>    foaf:name "National Newspaper, Inc.";
> .
> ```

An object property to express the accountability of an agent towards another agent. The subordinate agent acted on behalf of the responsible agent in an actual activity.

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Agent (§4.1.3)

has range

- prov:Agent (§4.1.3)

can be qualified with

- prov:Delegation (§4.3.18)
- prov:qualifiedDelegation (§4.3.35) op

PROV-DM term

[delegation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-delegation "prov-dm")

### 4.2 Expanded Terms

The additional terms used to describe relations among Starting Point classes are discussed in Section 3.2 (§3.2).

- prov:Collection (§4.2.1)
- prov:EmptyCollection (§4.2.2)
- prov:Bundle (§4.2.3)
- prov:Person (§4.2.4)
- prov:SoftwareAgent (§4.2.5)
- prov:Organization (§4.2.6)
- prov:Location (§4.2.7)

- prov:alternateOf (§4.2.8)
- prov:specializationOf (§4.2.9)
- prov:generatedAtTime (§4.2.10)
- prov:hadPrimarySource (§4.2.11)
- prov:value (§4.2.12)
- prov:wasQuotedFrom (§4.2.13)
- prov:wasRevisionOf (§4.2.14)
- prov:invalidatedAtTime (§4.2.15)
- prov:wasInvalidatedBy (§4.2.16)
- prov:hadMember (§4.2.17)
- prov:wasStartedBy (§4.2.18)
- prov:wasEndedBy (§4.2.19)
- prov:invalidated (§4.2.20)
- prov:influenced (§4.2.21)
- prov:atLocation (§4.2.22)
- prov:generated (§4.2.23)

### (13) Class: prov:Collection (§4.2.1) back to expanded classes

**IRI:** http://www.w3.org/ns/prov#Collection

A collection is an entity that provides a structure to some constituents, which are themselves entities. These constituents are said to be member of the collections.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
> @prefix dcterms: <http://purl.org/dc/terms/> .
> @prefix owl:     <http://www.w3.org/2002/07/owl#> .
> @prefix prov:    <http://www.w3.org/ns/prov#> .
> @prefix ex:      <http://example.com/ontology#> .
> @prefix :        <http://example.com/> .
>
> :todays-us-supreme-court
>    a prov:Collection, :RobertsCourt;
>
>    prov:qualifiedGeneration [
>       a prov:Generation;
>
>       # The generation is being qualified to be imprecise;
>       # prov:generatedAtTime and prov:atTime specify exact instants in time.
>       dcterms:date "2012"^^xsd:gYear;
>    ];
>
>    prov:hadMember
>       <http://dbpedia.org/resource/John_Glover_Roberts,_Jr.>,
>       <http://dbpedia.org/resource/Antonin_Scalia>,
>       <http://dbpedia.org/resource/Anthony_Kennedy>,
>       <http://dbpedia.org/resource/Clarence_Thomas>,
>       <http://dbpedia.org/resource/Ruth_Bader_Ginsburg>,
>       <http://dbpedia.org/resource/Stephen_Breyer>,
>       <http://dbpedia.org/resource/Samuel_Alito>,
>       <http://dbpedia.org/resource/Sonia_Sotomayor>,
>       <http://dbpedia.org/resource/Elena_Kagan>;
>
>    prov:wasDerivedFrom :the-first-us-supreme-court;
>
>    dcterms:description :copied-string;
> .
>
> :copied-string
>    a prov:Entity;
>    prov:value """2010–present: A. Scalia A. Kennedy C. Thomas R.B. Ginsburg
>                  S. Breyer S. Alito S. Sotomayor E. Kagan""";
>    prov:wasQuotedFrom :page-by-composition;
> .
>
> :page-by-seat
>    a prov:Entity, ex:WikipediaPage;
>    prov:specializationOf <http://purl.org/twc/page/wikipedia/us-supreme-court-by-seat>;
>    prov:generatedAtTime "2011-08-31T12:51:00"^^xsd:dateTime;
> .
>
> :page-by-composition
>    a prov:Entity, ex:WikipediaPage;
>    prov:specializationOf <http://purl.org/twc/page/wikipedia/us-supreme-court-by-composition>;
>    prov:generatedAtTime "2012-05-16T14:33:00"^^xsd:dateTime;
> .
> ```

is subclass of

prov:Entity (§4.1.1)

described with properties:

prov:hadMember (§4.2.17) op

has subclass

prov:EmptyCollection (§4.2.2)

PROV-DM term

[collection](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-collection "prov-dm")

### (14) Class: prov:EmptyCollection (§4.2.2) back to expanded classes

**IRI:** http://www.w3.org/ns/prov#EmptyCollection

An empty collection is a collection without members.
> **Example:**
>
> **Example**
>
> ```
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.org/> .
>
> :c a prov:EmptyCollection . # The collection is believed to not contain members.
> ```

is subclass of

prov:Collection (§4.2.1)

described with properties:

prov:hadMember (§4.2.17) op

### (15) Class: prov:Bundle (§4.2.3) back to expanded classes

**IRI:** http://www.w3.org/ns/prov#Bundle

A bundle is a named set of provenance descriptions, and is itself an Entity, so allowing provenance of provenance to be expressed.
> **Example:**
>
> **Example**
>
> ```
> @prefix prov:    <http://www.w3.org/ns/prov#> .
> @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
> @prefix my:      <http://example.com/my#> .
> @prefix :        <http://example.com/#> .
> @base <http://www.example.com/example.ttl> .
>
> <> # A provenance file located at http://www.example.com/example.ttl
>    a prov:Bundle;
>    prov:generatedAtTime "2012-05-24T09:30:00"^^xsd:dateTime;
>    prov:wasAttributedTo :bob;
> .
>
> :report1
>    a my:Report, prov:Entity;
>    my:version "1";
>    prov:generatedAtTime "2012-05-24T01:00:00"^^xsd:dateTime;
>    prov:wasAttributedTo :bob;
> .
> ```

Note that there are kinds of bundles (e.g. handwritten letters, audio recordings, etc.) that are not expressed in PROV-O, but can be still be described by PROV-O.

is subclass of

prov:Entity (§4.1.1)

PROV-DM term

[bundle-entity](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-bundle-entity "prov-dm")

### (16) Class: prov:Person (§4.2.4) back to expanded classes

**IRI:** http://www.w3.org/ns/prov#Person

Person agents are people.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix :     <http://example.com/> .
>
> <http://dbpedia.org/resource/Pablo_Picasso>
>    a prov:Person, prov:Agent;
>    foaf:depiction <http://upload.wikimedia.org/wikipedia/commons/9/98/Pablo_picasso_1.jpg>;
> .
> ```

is subclass of

prov:Agent (§4.1.3)

described with properties:

prov:qualifiedDelegation (§4.3.35) op , prov:actedOnBehalfOf (§4.1.12) op

PROV-DM term

[agent](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-agent "prov-dm")

### (17) Class: prov:SoftwareAgent (§4.2.5) back to expanded classes

**IRI:** http://www.w3.org/ns/prov#SoftwareAgent

A software agent is running software.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> # Googlebot is Google's web crawling bot;
> # it can initiate and participate in web-crawling activities.
>
> :googlebot
>    a prov:SoftwareAgent;
>    rdfs:label "Googlebot"^^xsd:string;
> .
> ```

is subclass of

prov:Agent (§4.1.3)

described with properties:

prov:qualifiedDelegation (§4.3.35) op , prov:actedOnBehalfOf (§4.1.12) op

PROV-DM term

[agent](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-agent "prov-dm")

### (18) Class: prov:Organization (§4.2.6) back to expanded classes

**IRI:** http://www.w3.org/ns/prov#Organization

An organization is a social or legal institution such as a company, society, etc.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix :     <http://example.com/> .
>
> :W3C
>    a prov:Agent, prov:Organization;
>    foaf:name "World Wide Web Consortium";
> .
> ```

is subclass of

prov:Agent (§4.1.3)

described with properties:

prov:qualifiedDelegation (§4.3.35) op , prov:actedOnBehalfOf (§4.1.12) op

PROV-DM term

[agent](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-agent "prov-dm")

### (19) Class: prov:Location (§4.2.7) back to expanded classes

**IRI:** http://www.w3.org/ns/prov#Location

A location can be an identifiable geographic place (ISO 19112), but it can also be a non-geographic place such as a directory, row, or column. As such, there are numerous ways in which location can be expressed, such as by a coordinate, address, landmark, and so forth.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix sioc: <http://rdfs.org/sioc/ns#> .
> @prefix :     <http://example.com/> .
>
> # A Location can be a path or a geographical location.
>
> :post9821
>    a prov:Entity, sioc:Post;
>    prov:wasGeneratedBy :publicationActivity1123;
>    prov:atLocation     :more-crime-happens-in-cities;
>    prov:qualifiedGeneration [
>       a prov:Generation;
>       prov:activity    :publicationActivity1123;
>       prov:atTime     "2011-07-16T01:52:02Z"^^xsd:dateTime;
>       prov:atLocation <http://dbpedia.org/resource/Madrid>;
>    ];
> .
>
> :publicationActivity1123      a prov:Activity.
> :more-crime-happens-in-cities a prov:Location.
> <http://dbpedia.org/resource/Madrid> a prov:Location.
> ```

in range of

prov:atLocation (§4.2.22) op

PROV-DM term

[attribute-location](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-attribute-location "prov-dm")

### (20) Property: prov:alternateOf (§4.2.8) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#alternateOf

Two alternate entities present aspects of the same thing. These aspects may be the same or different, and the alternate entities may or may not overlap in time.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :bbc a prov:Agent .
>
> :london_forecast_0412
>    a prov:Entity;
>    prov:wasAttributedTo :bbc;
>    prov:wasGeneratedBy [
>       a prov:Activity;
>       prov:endedAtTime "2012-04-12T00:00:00-04:00"^^xsd:dateTime;
>    ];
>    prov:alternateOf :london_forecast_0413;
> .
>
> :london_forecast_0413
>    a prov:Entity;
>    prov:wasAttributedTo :bbc;
>    prov:wasGeneratedBy [
>       a prov:Activity;
>       prov:endedAtTime "2012-04-13T00:00:00-04:00"^^xsd:dateTime;
>    ];
>    prov:alternateOf :london_forecast_0412;
> .
>
> ## :london_forecast_0412 and :london_forecast_0413 are both
> ## specialization of the more general entity :london_forecast
>
> :london_forecast
>    a prov:Entity;
>    prov:wasAttributedTo :bbc;
> .
>
> :london_forecast_0412
>    prov:specializationOf :london_forecast;
> .
> :london_forecast_0413
>    prov:specializationOf :london_forecast;
> .
> ```

has domain

- prov:Entity (§4.1.1)

has range

- prov:Entity (§4.1.1)

has sub-properties

- prov:specializationOf (§4.2.9)

PROV-DM term

[alternate](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-alternate "prov-dm")

### (21) Property: prov:specializationOf (§4.2.9) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#specializationOf

An entity that is a specialization of another shares all aspects of the latter, and additionally presents more specific aspects of the same thing as the latter. In particular, the lifetime of the entity being specialized contains that of any specialization. Examples of aspects include a time period, an abstraction, and a context associated with the entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :london_forecast_0412
>    a prov:Entity;
>    prov:wasAttributedTo :bbc;
>    prov:wasGeneratedBy [
>       a prov:Activity;
>       prov:endedAtTime "2012-04-12T00:00:00-04:00"^^xsd:dateTime;
>    ];
> .
>
> :london_forecast_0413
>    a prov:Entity;
>    prov:wasAttributedTo :bbc;
>    prov:wasGeneratedBy [
>       a prov:Activity;
>       prov:endedAtTime "2012-04-13T00:00:00-04:00"^^xsd:dateTime;
>    ];
> .
>
> :london_forecast
>    a prov:Entity;
>    prov:wasAttributedTo :bbc;
> .
>
> ## :london_forecast_0412 and :london_forecast_0413 are both
> ## specialization of the more general entity :london_forecast
>
> :london_forecast_0412
>    prov:alternateOf      :london_forecast_0413;
>    prov:specializationOf :london_forecast;
> .
> ```

has super-properties

- prov:alternateOf (§4.2.8) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Entity (§4.1.1)

PROV-DM term

[specialization](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-specialization "prov-dm")

### (22) Property: prov:generatedAtTime (§4.2.10) dp back to expanded properties

**IRI:** http://www.w3.org/ns/prov#generatedAtTime

Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> # A widget was generated 1:35:23 PM on April 3, 2012 UTC
>
> :widget-789532
>    a prov:Entity;
>    prov:generatedAtTime "2012-04-03T13:35:23Z"^^xsd:dateTime;
> .
>
> # The above statement is equivalent to:
> # :widget-789532 prov:qualifiedGeneration [ prov:atTime "2012-04-03T13:35:23Z"^^xsd:dateTime ] .
> ```

The time at which an entity was completely created and is available for use.

has domain

- prov:Entity (§4.1.1)

has range

- http://www.w3.org/2001/XMLSchema#dateTime

can be qualified with

- prov:Generation (§4.3.11)
- prov:atTime (§4.3.44) dp

PROV-DM term

[Generation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Generation "prov-dm")

### (23) Property: prov:hadPrimarySource (§4.2.11) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#hadPrimarySource

A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight.

Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated.

A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:     <http://www.w3.org/2002/07/owl#> .
> @prefix foaf:    <http://xmlns.com/foaf/0.1/> .
> @prefix prov:    <http://www.w3.org/ns/prov#> .
> @prefix lang:    <http://lexvo.org/id/iso639-3/> .
> @prefix dcterms: <http://purl.org/dc/terms/> .
> @prefix frbr:    <http://purl.org/vocab/frbr/core#> .
> @prefix :        <http://example.com/> .
>
> ## Having an primary source is a particular case of derivation.
>
> <http://www.gutenberg.org/ebooks/996>
>    a prov:Entity, frbr:Work;
>    dcterms:title          "Don Quixote";
>    prov:wasAttributedTo   :ormsby;
>    dcterms:language       lang:eng;
>    prov:hadPrimarySource <http://cultura.linkeddata.es/BNE/resource/C1001/XX2197892>;
> .
>
> #### The English version book is a translation that is based on the original Spanish book
>
> <http://cultura.linkeddata.es/BNE/resource/C1001/XX2197892>
>     a prov:Entity, frbr:Work;
>     prov:wasAttributedTo :cervantes;
>     dcterms:language     lang:spa;
> .
>
> :cervantes
>    a prov:Person;
>    foaf:name "Miguel de Cervantes";
> .
>
> :ormsby
>    a prov:Person;
>    foaf:name "John Ormsby";
> .
> ```

has super-properties

- prov:wasDerivedFrom (§4.1.5) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Entity (§4.1.1)

can be qualified with

- prov:qualifiedPrimarySource (§4.3.25) op
- prov:PrimarySource (§4.3.7)

PROV-DM term

[primary-source](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-primary-source "prov-dm")

### (24) Property: prov:value (§4.2.12) dp back to expanded properties

**IRI:** http://www.w3.org/ns/prov#value

Provides a value that is a direct representation of an entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :copied-string
>    a prov:Entity;
>    prov:value
>       """2010–present: A. Scalia A. Kennedy C. Thomas R.B. Ginsburg
>          S. Breyer S. Alito S. Sotomayor E. Kagan""";
>    prov:wasQuotedFrom
>       <http://purl.org/twc/page/wikipedia/us-supreme-court-by-composition>;
> .
> ```

has domain

- prov:Entity (§4.1.1)

PROV-DM term

[attribute-value](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-attribute-value "prov-dm")

### (25) Property: prov:wasQuotedFrom (§4.2.13) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#wasQuotedFrom

A quotation is the repeat of (some or all of) an entity, such as text or image, by someone who may or may not be its original author. Quotation is a particular case of derivation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :bl-dagstuhl
>    a prov:Entity;
>
>    prov:value """During the workshop, it became clear to me that the consensus
>    based models (which are often graphical in nature) can not only be
>    formalized but also be directly connected to these database focused
>    formalizations. I just needed to get over the differences in syntax.
>    This could imply that we could have nice way to trace provenance across
>    systems and through databases and be able to understand the
>    mathematical properties of this interconnection.""";
>
>    prov:wasQuotedFrom <http://purl.org/twc/page/thoughts-from-the-dagstuhl-workshop>;
> .
>
> <http://purl.org/twc/page/thoughts-from-the-dagstuhl-workshop>
>    a prov:Entity;
> .
> ```

An entity is derived from an original entity by copying, or 'quoting', some or all of it.

has super-properties

- prov:wasDerivedFrom (§4.1.5) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Entity (§4.1.1)

can be qualified with

- prov:qualifiedQuotation (§4.3.26) op
- prov:Quotation (§4.3.8)

PROV-DM term

[quotation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-quotation "prov-dm")

### (26) Property: prov:wasRevisionOf (§4.2.14) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#wasRevisionOf

A revision is a derivation for which the resulting entity is a revised version of some original. The implication here is that the resulting entity contains substantial content from the original. Revision is a particular case of derivation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix sioc: <http://rdfs.org/sioc/ns#> .
> @prefix :     <http://example.com/> .
>
> :post9821v1
>    a prov:Entity, sioc:Post;
>    prov:wasRevisionOf :post9821;
>    rdfs:comment ":post9821v1 is a post, which is a revision of the original post :post9821.";
> .
> ```

A revision is a derivation that revises an entity into a revised version.

has super-properties

- prov:wasDerivedFrom (§4.1.5) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Entity (§4.1.1)

can be qualified with

- prov:Revision (§4.3.9)
- prov:qualifiedRevision (§4.3.27) op

PROV-DM term

[revision](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-revision "prov-dm")

### (27) Property: prov:invalidatedAtTime (§4.2.15) dp back to expanded properties

**IRI:** http://www.w3.org/ns/prov#invalidatedAtTime

Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity. The entity is no longer available for use (or further invalidation) after invalidation. Any generation or usage of an entity precedes its invalidation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/ontology#> .
> @prefix :     <http://example.com/> .
>
> :the-Painter
>    a prov:Entity, ex:Painting;
>    rdfs:label "Le Peintre"@fr, "The Painter"@en;
>    prov:wasAttributedTo <http://dbpedia.org/resource/Pablo_Picasso>;
>    prov:invalidatedAtTime "1998-09-02T01:31:00Z"^^xsd:dateTime;
> .
> ```

The time at which an entity was invalidated (i.e., no longer usable).

has domain

- prov:Entity (§4.1.1)

has range

- http://www.w3.org/2001/XMLSchema#dateTime

can be qualified with

- prov:Invalidation (§4.3.13)
- prov:atTime (§4.3.44) dp

PROV-DM term

[Invalidation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Invalidation "prov-dm")

### (28) Property: prov:wasInvalidatedBy (§4.2.16) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#wasInvalidatedBy

Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity. The entity is no longer available for use (or further invalidation) after invalidation. Any generation or usage of an entity precedes its invalidation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix :     <http://example.com/> .
>
> :the-Painter
>    a prov:Entity, :Painting;
>    rdfs:label "Le Peintre"@fr, "The Painter"@en;
>    prov:wasAttributedTo <http://dbpedia.org/resource/Pablo_Picasso>;
>    prov:wasInvalidatedBy :Swissair_Flight_111_crash; #The painting was destroyed in an airplane crash
> .
>
> <http://dbpedia.org/resource/Pablo_Picasso>
>    a prov:Agent;
>    foaf:depiction <http://upload.wikimedia.org/wikipedia/commons/9/98/Pablo_picasso_1.jpg>;
> .
>
> :Swissair_Flight_111_crash
>    a prov:Activity;
>    prov:used <http://dbpedia.org/resource/Swissair_Flight_111>;
> .
> ```

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Activity (§4.1.2)

can be qualified with

- prov:Invalidation (§4.3.13)
- prov:qualifiedInvalidation (§4.3.29) op

PROV-DM term

[Invalidation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Invalidation "prov-dm")

### (29) Property: prov:hadMember (§4.2.17) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#hadMember

A collection is an entity that provides a structure to some constituents, which are themselves entities. These constituents are said to be member of the collections.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:     <http://www.w3.org/2002/07/owl#> .
> @prefix dcterms: <http://purl.org/dc/terms/> .
> @prefix prov:    <http://www.w3.org/ns/prov#> .
> @prefix ex:      <http://example.com/ontology#> .
> @prefix :        <http://example.com/> .
>
> :todays-us-supreme-court
>    a prov:Collection, ex:RobertsCourt;
>    dcterms:description [
>       a prov:Entity;
>       prov:value """2010–present: A. Scalia A. Kennedy C. Thomas R.B. Ginsburg S.
>                   Breyer S. Alito S. Sotomayor E. Kagan""";
>       prov:wasQuotedFrom :page-by-composition;
>    ];
>    prov:qualifiedGeneration [
>       a prov:Generation;
>
>       # Since we need to be imprecise, we can't use prov:generatedAtTime or prov:atTime
>       dcterms:date "2012"^^xsd:gYear;
>    ];
>
>    prov:wasDerivedFrom :the-first-us-supreme-court;
>
>    prov:hadMember
>       <http://dbpedia.org/resource/John_Glover_Roberts,_Jr.>,
>       <http://dbpedia.org/resource/Antonin_Scalia>,
>       <http://dbpedia.org/resource/Anthony_Kennedy>,
>       <http://dbpedia.org/resource/Clarence_Thomas>,
>       <http://dbpedia.org/resource/Ruth_Bader_Ginsburg>,
>       <http://dbpedia.org/resource/Stephen_Breyer>,
>       <http://dbpedia.org/resource/Samuel_Alito>,
>       <http://dbpedia.org/resource/Sonia_Sotomayor>,
>       <http://dbpedia.org/resource/Elena_Kagan>;
> .
>
> :page-by-seat
>    a prov:Entity, ex:WikipediaPage;
>    prov:specializationOf <http://purl.org/twc/page/wikipedia/us-supreme-court-by-seat>;
>    prov:generatedAtTime "2011-08-31T12:51:00"^^xsd:dateTime;
> .
>
> :page-by-composition
>    a prov:Entity, ex:WikipediaPage;
>    prov:specializationOf <http://purl.org/twc/page/wikipedia/us-supreme-court-by-composition>;
>    prov:generatedAtTime "2012-05-16T14:33:00"^^xsd:dateTime;
> .
> ```

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Collection (§4.2.1)

has range

- prov:Entity (§4.1.1)

PROV-DM term

[collection](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-collection "prov-dm")

### (30) Property: prov:wasStartedBy (§4.2.18) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#wasStartedBy

Start is when an activity is deemed to have been started by an entity, known as trigger. The activity did not exist before its start. Any usage, generation, or invalidation involving an activity follows the activity's start. A start may refer to a trigger entity that set off the activity, or to an activity, known as starter, that generated the trigger.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> # Use prov:qualifiedStart to see when and where the activity was started
>
> :experiment
>    a prov:Activity;
>    prov:wasStartedBy :researcher;
> .
>
> :researcher a prov:Agent .
> ```

Start is when an activity is deemed to have started. A start may refer to an entity, known as trigger, that initiated the activity.

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Entity (§4.1.1)

can be qualified with

- prov:Start (§4.3.4)
- prov:qualifiedStart (§4.3.30) op

PROV-DM term

[Start](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Start "prov-dm")

### (31) Property: prov:wasEndedBy (§4.2.19) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#wasEndedBy

End is when an activity is deemed to have been ended by an entity, known as trigger. The activity no longer exists after its end. Any usage, generation, or invalidation involving an activity precedes the activity's end. An end may refer to a trigger entity that terminated the activity, or to an activity, known as ender that generated the trigger.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :experiment
>    a prov:Activity;
>    prov:wasEndedBy :inconsistentResult;
>    prov:qualifiedEnd [
>       a prov:End;
>       prov:entity     :inconsistentResult;
>       prov:atTime    "2011-07-16T01:52:02Z"^^xsd:dateTime;
>       prov:atLocation :scienceLab_003;
>    ];
> .
>
> :inconsistentResult a prov:Entity .
> :scienceLab_003     a prov:Location .
> ```

End is when an activity is deemed to have ended. An end may refer to an entity, known as trigger, that terminated the activity.

has super-properties

- prov:wasInfluencedBy (§4.3.21) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Entity (§4.1.1)

can be qualified with

- prov:End (§4.3.5)
- prov:qualifiedEnd (§4.3.34) op

PROV-DM term

[End](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-End "prov-dm")

### (32) Property: prov:invalidated (§4.2.20) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#invalidated

Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity. The entity is no longer available for use (or further invalidation) after invalidation. Any generation or usage of an entity precedes its invalidation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix ex:   <http://example.com/ontology#> .
> @prefix :     <http://example.com/> .
>
> :swissair_Flight_111_crash
>    a prov:Activity;
>    prov:used        <http://dbpedia.org/resource/Swissair_Flight_111>;
>    prov:invalidated :the-Painter;
> .
>
> :the-Painter
>    a prov:Entity, ex:Painting;
>    rdfs:label "Le Peintre"@fr, "The Painter"@en;
>    prov:wasAttributedTo <http://dbpedia.org/resource/Pablo_Picasso>;
>
>    # Inferred from prov:invalidated
>    prov:wasInvalidatedBy :swissair_Flight_111_crash;
> .
>
> <http://dbpedia.org/resource/Pablo_Picasso>
>    a prov:Agent;
>    foaf:depiction <http://upload.wikimedia.org/wikipedia/commons/9/98/Pablo_picasso_1.jpg>;
> .
> ```

has super-properties

- prov:influenced (§4.2.21) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Entity (§4.1.1)

has inverse

- prov:wasInvalidatedBy (§4.2.16)

PROV-DM term

[Invalidation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Invalidation "prov-dm")

### (33) Property: prov:influenced (§4.2.21) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#influenced

Influence is the capacity of an entity, activity, or agent to have an effect on the character, development, or behavior of another by means of usage, start, end, generation, invalidation, communication, derivation, attribution, association, or delegation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix w3:   <http://example.com/w3/> .
> @prefix tr:   <http://example.com/tech-report/> .
> @prefix :     <http://example.com/> .
>
> # prov:influenced is a top-level property that links any
> # Entity, Activity, or Agent to any other
> # Entity, Activity, or Agent that it had an effect upon.
>
> w3:Consortium
>    a prov:Agent;
>    prov:influenced tr:WD-prov-dm-20111215;
> .
> ```

has inverse

- prov:wasInfluencedBy (§4.3.21)

has sub-properties

- prov:generated (§4.2.23)
- prov:invalidated (§4.2.20)

PROV-DM term

[influence](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-influence "prov-dm")

### (34) Property: prov:atLocation (§4.2.22) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#atLocation

A location can be an identifiable geographic place (ISO 19112), but it can also be a non-geographic place such as a directory, row, or column. As such, there are numerous ways in which location can be expressed, such as by a coordinate, address, landmark, and so forth.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix sioc: <http://rdfs.org/sioc/ns#> .
> @prefix :     <http://example.com/> .
>
> # A Location can be a path or a geographical location.
>
> :post9821
>    a prov:Entity, sioc:Post;
>    prov:wasGeneratedBy :publicationActivity1123;
>    prov:atLocation     :more-crime-happens-in-cities;
>    prov:qualifiedGeneration [
>       a prov:Generation;
>       prov:activity    :publicationActivity1123;
>       prov:atTime     "2011-07-16T01:52:02Z"^^xsd:dateTime;
>       prov:atLocation <http://dbpedia.org/resource/Madrid>;
>    ];
> .
>
> :publicationActivity1123      a prov:Activity .
> :more-crime-happens-in-cities        a prov:Location .
> <http://dbpedia.org/resource/Madrid> a prov:Location .
> ```

The Location of any resource.

This property has multiple RDFS domains to suit multiple OWL Profiles. See §A PROV-O OWL Profile.

has domain

- prov:Activity (§4.1.2) or prov:Agent (§4.1.3) or prov:Entity (§4.1.1) or prov:InstantaneousEvent (§4.3.19)

has range

- prov:Location (§4.2.7)

PROV-DM term

[attribute-location](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-attribute-location "prov-dm")

### (35) Property: prov:generated (§4.2.23) op back to expanded properties

**IRI:** http://www.w3.org/ns/prov#generated

Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :proteinDigestion
>    a prov:Activity;
>    prov:generated :peptideSample1;
> .
>
> :peptideSample1 a prov:Entity .
> ```

has super-properties

- prov:influenced (§4.2.21) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Entity (§4.1.1)

has inverse

- prov:wasGeneratedBy (§4.1.4)

PROV-DM term

[Generation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Generation "prov-dm")

### 4.3 Qualified Terms

The terms used to qualify the Starting Point and Expanded properties are discussed in Section 3.3 (§3.3).

- prov:Influence (§4.3.1)
- prov:EntityInfluence (§4.3.2)
- prov:Usage (§4.3.3)
- prov:Start (§4.3.4)
- prov:End (§4.3.5)
- prov:Derivation (§4.3.6)
- prov:PrimarySource (§4.3.7)
- prov:Quotation (§4.3.8)
- prov:Revision (§4.3.9)
- prov:ActivityInfluence (§4.3.10)
- prov:Generation (§4.3.11)
- prov:Communication (§4.3.12)
- prov:Invalidation (§4.3.13)
- prov:AgentInfluence (§4.3.14)
- prov:Attribution (§4.3.15)
- prov:Association (§4.3.16)
- prov:Plan (§4.3.17)
- prov:Delegation (§4.3.18)
- prov:InstantaneousEvent (§4.3.19)
- prov:Role (§4.3.20)

- prov:wasInfluencedBy (§4.3.21)
- prov:qualifiedInfluence (§4.3.22)
- prov:qualifiedGeneration (§4.3.23)
- prov:qualifiedDerivation (§4.3.24)
- prov:qualifiedPrimarySource (§4.3.25)
- prov:qualifiedQuotation (§4.3.26)
- prov:qualifiedRevision (§4.3.27)
- prov:qualifiedAttribution (§4.3.28)
- prov:qualifiedInvalidation (§4.3.29)
- prov:qualifiedStart (§4.3.30)
- prov:qualifiedUsage (§4.3.31)
- prov:qualifiedCommunication (§4.3.32)
- prov:qualifiedAssociation (§4.3.33)
- prov:qualifiedEnd (§4.3.34)
- prov:qualifiedDelegation (§4.3.35)
- prov:influencer (§4.3.36)
- prov:entity (§4.3.37)
- prov:hadUsage (§4.3.38)
- prov:hadGeneration (§4.3.39)
- prov:activity (§4.3.40)
- prov:agent (§4.3.41)
- prov:hadPlan (§4.3.42)
- prov:hadActivity (§4.3.43)
- prov:atTime (§4.3.44)
- prov:hadRole (§4.3.45)

### (36) Class: prov:Influence (§4.3.1) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Influence

Influence is the capacity of an entity, activity, or agent to have an effect on the character, development, or behavior of another by means of usage, start, end, generation, invalidation, communication, derivation, attribution, association, or delegation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix my:   <http://example.com/ontology#> .
> @prefix :     <http://example.com/> .
>
> # Although a domain extension (e.g. ':wasConductedBy') is not defined by PROV-O,
> # the relation between a surgery and an agent can still be qualified
> # by reusing prov:Influence and one of its three subclasses
> # (depending on the type of influencer):
> # AgentInfluence, EntityInfluence, and ActivityInfluence.
>
> my:wasConductedBy rdfs:subPropertyOf prov:wasAssociatedWith .
>
> :conductingSurgery_1
>    a prov:Activity;
>
>    # This unqualified influence is unknown in PROV,
>    # but would be a subproperty of wasAssociatedWith.
>    my:wasConductedBy :bob;
>
>    # Even though PROV systems do not understand my:wasConductedBy,
>    prov:qualifiedAssociation [
>       # they can recognize that the unknown relation
>       # is being qualified with a prov:hadRole.
>       a prov:Association,
>         prov:AgentInfluence,   # Inferred
>         prov:Influence;        # Inferred
>       prov:agent   :bob;       # The object of my:wasConductedBy
>       prov:hadRole my:surgeon;
>    ];
> .
>
> :bob       a prov:Agent .
> my:surgeon a prov:Role .
> ```

Because prov:Influence is a broad relation, its most specific subclasses (e.g. prov:Communication, prov:Delegation, prov:End, prov:Revision, etc.) should be used when applicable.

An instance of prov:Influence provides additional descriptions about the binary prov:wasInfluencedBy relation from some influenced Activity, Entity, or Agent to the influencing Activity, Entity, or Agent. For example, :stomach_ache prov:wasInfluencedBy :spoon; prov:qualifiedInfluence [ a prov:Influence; prov:entity :spoon; :foo :bar ] . Because prov:Influence is a broad relation, the more specific relations (Communication, Delegation, End, etc.) should be used when applicable.

described with properties:

prov:influencer (§4.3.36) op , prov:hadRole (§4.3.45) op , prov:hadActivity (§4.3.43) op

in range of

prov:qualifiedInfluence (§4.3.22) op

has subclasses

prov:ActivityInfluence (§4.3.10) , prov:AgentInfluence (§4.3.14) , prov:EntityInfluence (§4.3.2)

qualifies

prov:wasInfluencedBy (§4.3.21) op

PROV-DM term

[influence](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-influence "prov-dm")

### (37) Class: prov:EntityInfluence (§4.3.2) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#EntityInfluence

EntityInfluence is the capacity of an entity to have an effect on the character, development, or behavior of another by means of usage, start, end, derivation, or other.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :sortActivity
>    a prov:Activity;
>    prov:used :rawData;
>    prov:qualifiedUsage [
>       a prov:Usage,
>         prov:EntityInfluence; ## Instances of Start, End, Usage, Derivation, and Invalidation
>       prov:entity  :datasetA; ## qualify the influenced of an Entity (cited by prov:entity).
>       prov:hadRole :inputToBeSorted;
>    ];
>    prov:generated :sortedData;
> .
>
> :rawData    a prov:Entity .
> :sortedData a prov:Entity .
> ```

EntityInfluence provides additional descriptions of an Entity's binary influence upon any other kind of resource. Instances of EntityInfluence use the prov:entity property to cite the influencing Entity.

It is not recommended that the type EntityInfluence be asserted without also asserting one of its more specific subclasses.

is subclass of

prov:Influence (§4.3.1)

described with properties:

prov:entity (§4.3.37) op

prov:hadRole (§4.3.45) op , prov:influencer (§4.3.36) op , prov:hadActivity (§4.3.43) op

has subclasses

prov:End (§4.3.5) , prov:Start (§4.3.4) , prov:Usage (§4.3.3) , prov:Derivation (§4.3.6)

### (38) Class: prov:Usage (§4.3.3) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Usage

Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :sortActivity
>    a prov:Activity;
>    prov:startedAtTime  "2011-07-16T01:52:02Z"^^xsd:dateTime;
>    prov:qualifiedUsage [
>       a prov:Usage;
>       prov:entity    :datasetA;         ## The entity used by the prov:Usage
>       prov:hadRole   :inputToBeSorted;  ## the role of the entity in this prov:Usage
>    ];
>    prov:generated :datasetB;
> .
>
> :datasetA        a prov:Entity .
> :datasetB        a prov:Entity .
> :inputToBeSorted a prov:Role .
>
> ## The role of :datasetA cannot be expressed using only starting-point terms:
>
> :sortActivity
>    a prov:Activity;
>    prov:startedAtTime     "2011-07-16T01:52:02Z"^^xsd:dateTime;
>    prov:used       :datasetA;
>    prov:generated  :datasetB;
> .
> ```

An instance of prov:Usage provides additional descriptions about the binary prov:used relation from some prov:Activity to an prov:Entity that it used. For example, :keynote prov:used :podium; prov:qualifiedUsage [ a prov:Usage; prov:entity :podium; :foo :bar ].

is subclass of

prov:InstantaneousEvent (§4.3.19) , prov:EntityInfluence (§4.3.2)

described with properties:

prov:atTime (§4.3.44) dp , prov:entity (§4.3.37) op

in range of

prov:hadUsage (§4.3.38) op prov:qualifiedUsage (§4.3.31) op

qualifies

prov:used (§4.1.8) op

PROV-DM term

[Usage](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Usage "prov-dm")

### (39) Class: prov:Start (§4.3.4) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Start

Start is when an activity is deemed to have been started by an entity, known as trigger. The activity did not exist before its start. Any usage, generation, or invalidation involving an activity follows the activity's start. A start may refer to a trigger entity that set off the activity, or to an activity, known as starter, that generated the trigger.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> ### Start can be used to qualify wasStartedBy with time and location information.
> ### In this example, a consistency checking activity is started by the update of a data record.
>
> :consistency_checking
>    a prov:Activity;
>    prov:wasStartedBy :updated_data_record;
>    prov:qualifiedStart [
>       a prov:Start;
>       prov:entity       :updated_data_record;
>       prov:atTime       "2011-07-06T01:48:36Z"^^xsd:dateTime;
>       prov:atLocation   :scienceLab_003;
>       prov:hadActivity  :syntax_checking;
>    ];
> .
>
> :updated_data_record a prov:Entity .
>
> ### There is an explicit process of checking the syntax of the updated data record
>
> :syntax_checking
>    a   prov:Activity ;
>    prov:startedAtTime      "2011-07-06T01:48:36Z"^^xsd:dateTime;
>    prov:endedAtTime        "2011-07-06T02:12:36Z"^^xsd:dateTime;
>    prov:wasAssociatedWith  :syntax_checker ;
> .
>
> :syntax_checker   a   prov:SoftwareAgent .
> ```

An instance of prov:Start provides additional descriptions about the binary prov:wasStartedBy relation from some started prov:Activity to an prov:Entity that started it. For example, :foot_race prov:wasStartedBy :bang; prov:qualifiedStart [ a prov:Start; prov:entity :bang; :foo :bar; prov:atTime '2012-03-09T08:05:08-05:00'^^xsd:dateTime ] .

is subclass of

prov:InstantaneousEvent (§4.3.19) , prov:EntityInfluence (§4.3.2)

described with properties:

prov:hadActivity (§4.3.43) op

prov:atTime (§4.3.44) dp , prov:entity (§4.3.37) op

in range of

prov:qualifiedStart (§4.3.30) op

qualifies

prov:wasStartedBy (§4.2.18) op

PROV-DM term

[Start](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Start "prov-dm")

### (40) Class: prov:End (§4.3.5) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#End

End is when an activity is deemed to have been ended by an entity, known as trigger. The activity no longer exists after its end. Any usage, generation, or invalidation involving an activity precedes the activity's end. An end may refer to a trigger entity that terminated the activity, or to an activity, known as ender that generated the trigger.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> ### End can be used to qualify wasEndedBy with time and location information.
> ### In this example, an experiment is stopped because an intermediate inconsitent resul.
>
> :experiment
>    a prov:Activity;
>    prov:wasEndedBy :inconsistentResult;
>    prov:qualifiedEnd [
>       a prov:End;
>       prov:entity       :inconsistentResult;
>       prov:atTime       "2011-07-16T01:52:02Z"^^xsd:dateTime;
>       prov:atLocation   :scienceLab_003;
>       prov:hadActivity  :analyse_intermediate_result ;
>    ];
> .
>
> :inconsistentResult a prov:Entity .
>
> ### An implicit process analyzes the intermediate result to confirm its expected consistency
>
> analyse_intermediate_result
>    a   prov:Activity ;
>    prov:startedAtTime   "2011-07-15T12:52:02Z"^^xsd:dateTime;
>    prov:endedAtTime     "2011-07-16T01:52:02Z"^^xsd:dateTime;
> .
> ```

An instance of prov:End provides additional descriptions about the binary prov:wasEndedBy relation from some ended prov:Activity to an prov:Entity that ended it. For example, :ball_game prov:wasEndedBy :buzzer; prov:qualifiedEnd [ a prov:End; prov:entity :buzzer; :foo :bar; prov:atTime '2012-03-09T08:05:08-05:00'^^xsd:dateTime ].

is subclass of

prov:InstantaneousEvent (§4.3.19) , prov:EntityInfluence (§4.3.2)

described with properties:

prov:hadActivity (§4.3.43) op

prov:atTime (§4.3.44) dp , prov:entity (§4.3.37) op

in range of

prov:qualifiedEnd (§4.3.34) op

qualifies

prov:wasEndedBy (§4.2.19) op

PROV-DM term

[End](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-End "prov-dm")

### (41) Class: prov:Derivation (§4.3.6) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Derivation

A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> # The simplest (and least detailed) form of derivation.
> :bar_chart
>    a prov:Entity;
>    prov:wasDerivedFrom :aggregatedByRegions;
> .
>
> # The simple form can be accompanied by a qualified form:
> # which provides more details about how :bar_chart was
> # derived from :aggregatedRegions.
>
> :bar_chart
>    a prov:Entity;
>
>    prov:wasDerivedFrom :aggregatedByRegions;
>    prov:qualifiedDerivation [
>       a prov:Derivation;
>       prov:entity      :aggregatedByRegions;
>
>       # Derivations can cite the influencing Activity in doing the derivation.
>       prov:hadActivity   :create_the_chart;
>
>       # They can also cite the Usage and Generation that the Activity
>       # performed to generate :bar_chart.
>       prov:hadUsage      :data_loading;
>       prov:hadGeneration :plot_the_chart;
>    ];
> .
>
> ### The process during which the chart was created, from loading the data to the software, to process the data and plot the chart.
> ### Additional metadata was recorded, like when it started (before the usage), ended (after the generation of the chart) and who was associated with it.
>
> :create_the_chart
>    a prov:Activity;
>    prov:wasAssociatedWith :derek;
>    prov:startedAtTime "2012-04-03T00:00:00Z"^^xsd:dateTime;
>    prov:endedAtTime "2012-04-03T00:00:10Z"^^xsd:dateTime;
> .
>
> ### The final chart was plotted
>
> :plot_the_chart
>    a prov:Generation, prov:InstantaneousEvent;
>    prov:atTime "2012-04-03T00:00:01Z"^^xsd:dateTime;
> .
>
> ### The data was getting used to create the chart
>
> :data_loading
>    a prov:Usage;
>    prov:atTime "2012-04-03T00:00:00Z"^^xsd:dateTime;
> .
> ```

The more specific forms of prov:Derivation (i.e., prov:Revision, prov:Quotation, prov:PrimarySource) should be asserted if they apply.

An instance of prov:Derivation provides additional descriptions about the binary prov:wasDerivedFrom relation from some derived prov:Entity to another prov:Entity from which it was derived. For example, :chewed_bubble_gum prov:wasDerivedFrom :unwrapped_bubble_gum; prov:qualifiedDerivation [ a prov:Derivation; prov:entity :unwrapped_bubble_gum; :foo :bar ].

is subclass of

prov:EntityInfluence (§4.3.2)

described with properties:

prov:hadUsage (§4.3.38) op , prov:hadGeneration (§4.3.39) op

prov:hadActivity (§4.3.43) op

prov:entity (§4.3.37) op

in range of

prov:qualifiedDerivation (§4.3.24) op

has subclasses

prov:Revision (§4.3.9) , prov:PrimarySource (§4.3.7) , prov:Quotation (§4.3.8)

qualifies

prov:wasDerivedFrom (§4.1.5) op

PROV-DM term

[Derivation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Derivation "prov-dm")

### (42) Class: prov:PrimarySource (§4.3.7) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#PrimarySource

A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight.

Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated.

A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :myPost
>    a prov:Entity;
>    prov:hadPrimarySource :donQuixote;
>    prov:qualifiedPrimarySource [
>       a prov:PrimarySource;
>       prov:entity :donQuixote;
>       :confidenceValue "6"^^xsd:integer;
>       rdfs:comment """Not sure if Don Quixote was the original source,
>                       so asserting a confidence value of 6 out of 10.""";
>    ];
> .
>
> :donQuixote a prov:Entity.
> ```

An instance of prov:PrimarySource provides additional descriptions about the binary prov:hadPrimarySource relation from some secondary prov:Entity to an earlier, primary prov:Entity. For example, :blog prov:hadPrimarySource :newsArticle; prov:qualifiedPrimarySource [ a prov:PrimarySource; prov:entity :newsArticle; :foo :bar ] .

is subclass of

prov:Derivation (§4.3.6)

described with properties:

prov:hadGeneration (§4.3.39) op , prov:hadUsage (§4.3.38) op

in range of

prov:qualifiedPrimarySource (§4.3.25) op

qualifies

prov:hadPrimarySource (§4.2.11) op

PROV-DM term

[primary-source](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-primary-source "prov-dm")

### (43) Class: prov:Quotation (§4.3.8) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Quotation

A quotation is the repeat of (some or all of) an entity, such as text or image, by someone who may or may not be its original author. Quotation is a particular case of derivation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> :dagstuhl-quote
>    a prov:Entity;
>    prov:value   "why would people record and share provenance in the first place?";
>    prov:wasQuotedFrom <http://purl.org/twc/page/thoughts-from-the-dagstuhl-workshop>;
>    prov:qualifiedQuotation [
>       a prov:Quotation;
>       prov:entity     <http://purl.org/twc/page/thoughts-from-the-dagstuhl-workshop>;
>       ex:fromSection 2;
>    ];
>    prov:wasAttributedTo <http://data.semanticweb.org/person/luc-moreau>;
> .
>
> <http://purl.org/twc/page/thoughts-from-the-dagstuhl-workshop>
>    a prov:Entity;
>    prov:wasAttributedTo <http://data.semanticweb.org/person/paul-groth>;
> .
>
> <http://data.semanticweb.org/person/luc-moreau> a prov:Person, prov:Agent .
> <http://data.semanticweb.org/person/paul-groth> a prov:Person, prov:Agent .
> ```

An instance of prov:Quotation provides additional descriptions about the binary prov:wasQuotedFrom relation from some taken prov:Entity from an earlier, larger prov:Entity. For example, :here_is_looking_at_you_kid prov:wasQuotedFrom :casablanca_script; prov:qualifiedQuotation [ a prov:Quotation; prov:entity :casablanca_script; :foo :bar ].

is subclass of

prov:Derivation (§4.3.6)

described with properties:

prov:hadGeneration (§4.3.39) op , prov:hadUsage (§4.3.38) op

in range of

prov:qualifiedQuotation (§4.3.26) op

qualifies

prov:wasQuotedFrom (§4.2.13) op

PROV-DM term

[quotation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-quotation "prov-dm")

### (44) Class: prov:Revision (§4.3.9) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Revision

A revision is a derivation for which the resulting entity is a revised version of some original. The implication here is that the resulting entity contains substantial content from the original. Revision is a particular case of derivation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> :draft2
>    a prov:Entity;
>    prov:wasRevisionOf    :draft1;
>    prov:qualifiedRevision [
>       a prov:Revision;
>       prov:entity        :draft1;
>       ex:peerReviewed     false;
>    ];
>
>    prov:wasAssociatedWith :edward;
>    prov:qualifiedAssociation [
>       a prov:Association;
>       prov:agent          :edward;
>       prov:hadRole        :editor;
>    ];
> .
>
> :draft1 a prov:Entity .
>
> :edward
>    a prov:Person, prov:Agent;
> .
> ```

An instance of prov:Revision provides additional descriptions about the binary prov:wasRevisionOf relation from some newer prov:Entity to an earlier prov:Entity. For example, :draft_2 prov:wasRevisionOf :draft_1; prov:qualifiedRevision [ a prov:Revision; prov:entity :draft_1; :foo :bar ].

is subclass of

prov:Derivation (§4.3.6)

described with properties:

prov:hadGeneration (§4.3.39) op , prov:hadUsage (§4.3.38) op

in range of

prov:qualifiedRevision (§4.3.27) op

qualifies

prov:wasRevisionOf (§4.2.14) op

PROV-DM term

[revision](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-revision "prov-dm")

### (45) Class: prov:ActivityInfluence (§4.3.10) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#ActivityInfluence

ActivitiyInfluence is the capacity of an activity to have an effect on the character, development, or behavior of another by means of generation, invalidation, communication, or other.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :bar_chart
>    a prov:Entity;
>    prov:wasGeneratedBy      :illustrating;
>    prov:qualifiedGeneration :making-bar-chart;
> .
>
> :making-bar-chart
>    a prov:Generation,
>      prov:ActivityInfluence;  ## Instances of Generation, Invalidation and Communication qualify
>    prov:activity :illustrating; ## the influence of an Activity (cited by prov:activity)
>    rdfs:comment "Ended up with bar chart as line chart looked ugly."@en;
> .
>
> :illustrating a prov:Activity .
> ```

It is not recommended that the type ActivityInfluence be asserted without also asserting one of its more specific subclasses.

ActivityInfluence provides additional descriptions of an Activity's binary influence upon any other kind of resource. Instances of ActivityInfluence use the prov:activity property to cite the influencing Activity.

is subclass of

prov:Influence (§4.3.1)

described with properties:

prov:activity (§4.3.40) op

prov:hadRole (§4.3.45) op , prov:influencer (§4.3.36) op , prov:hadActivity (§4.3.43) op

has subclasses

prov:Generation (§4.3.11) , prov:Invalidation (§4.3.13) , prov:Communication (§4.3.12)

### (46) Class: prov:Generation (§4.3.11) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Generation

Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix bbc:  <http://www.bbc.co.uk/> .
> @prefix eg:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> :bbcNews2012-04-03
>    a prov:Entity, eg:DailyNews;
>    rdfs:comment """The BBC news home page on 2012-04-03 contained a reference
>                    to a given news item, but the BBC news home page on
>                    the next day did not.""";
>
>    prov:wasGeneratedBy :publishingActivity;
>    prov:qualifiedGeneration [
>       a prov:Generation, prov:InstantaneousEvent;
>       prov:atTime "2012-04-03T00:00:01Z"^^xsd:dateTime;
>       prov:activity :publishingActivity;
>    ];
>    prov:qualifiedInvalidation [
>       a prov:Invalidation, prov:InstantaneousEvent;
>       prov:atTime "2012-04-03T23:59:59Z"^^xsd:dateTime;
>    ];
> .
>
> :publishingActivity
>    a prov:Activity;
> .
> ```

An instance of prov:Generation provides additional descriptions about the binary prov:wasGeneratedBy relation from a generated prov:Entity to the prov:Activity that generated it. For example, :cake prov:wasGeneratedBy :baking; prov:qualifiedGeneration [ a prov:Generation; prov:activity :baking; :foo :bar ].

is subclass of

prov:InstantaneousEvent (§4.3.19) , prov:ActivityInfluence (§4.3.10)

described with properties:

prov:activity (§4.3.40) op , prov:atTime (§4.3.44) dp

in range of

prov:hadGeneration (§4.3.39) op prov:qualifiedGeneration (§4.3.23) op

qualifies

prov:wasGeneratedBy (§4.1.4) op

PROV-DM term

[Generation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Generation "prov-dm")

### (47) Class: prov:Communication (§4.3.12) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Communication

Communication is the exchange of an entity by two activities, one activity using the entity generated by the other.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> :writing-celebrity-gossip
>    a prov:Activity;
>    prov:wasInformedBy          :voicemail-interception;
>    prov:qualifiedCommunication :informing-the-journalist;
> .
>
> :informing-the-journalist
>    a prov:Communication;
>    prov:activity   :voicemail-interception;
>    ex:mediaType "email";
> .
>
> :voicemail-interception a prov:Activity .
> ```

An instance of prov:Communication provides additional descriptions about the binary prov:wasInformedBy relation from an informed prov:Activity to the prov:Activity that informed it. For example, :you_jumping_off_bridge prov:wasInformedBy :everyone_else_jumping_off_bridge; prov:qualifiedCommunication [ a prov:Communication; prov:activity :everyone_else_jumping_off_bridge; :foo :bar ].

is subclass of

prov:ActivityInfluence (§4.3.10)

described with properties:

prov:activity (§4.3.40) op

in range of

prov:qualifiedCommunication (§4.3.32) op

qualifies

prov:wasInformedBy (§4.1.9) op

PROV-DM term

[Communication](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Communication "prov-dm")

### (48) Class: prov:Invalidation (§4.3.13) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Invalidation

Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity. The entity is no longer available for use (or further invalidation) after invalidation. Any generation or usage of an entity precedes its invalidation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix wgs:  <http://www.w3.org/2003/01/geo/wgs84_pos#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix :     <http://example.com/> .
>
> :the-Painter
>    a prov:Entity, :Painting;
>    rdfs:label "Le Peintre"@fr, "The Painter"@en;
>    prov:wasAttributedTo <http://dbpedia.org/resource/Pablo_Picasso>;
>
>    prov:wasInvalidatedBy :swissair_Flight_111_crash;
>    prov:qualifiedInvalidation [
>       a prov:Invalidation;
>       prov:activity    :swissair_Flight_111_crash;
>       prov:atTime      "1998-09-02T01:31:00Z"^^xsd:dateTime;
>       prov:atLocation  <http://purl.org/twc/location/Swissair-Flight-111-crash>;
>    ];
> .
>
> <http://purl.org/twc/location/Swissair-Flight-111-crash>
>    a prov:Location;
>    wgs:lat   44.409167;
>    wgs:long -63.973611;
> .
>
> <http://dbpedia.org/resource/Pablo_Picasso>
>    a prov:Agent;
>    foaf:depiction <http://upload.wikimedia.org/wikipedia/commons/9/98/Pablo_picasso_1.jpg>;
> .
>
> :swissair_Flight_111_crash
>    a prov:Activity;
>    prov:used          <http://dbpedia.org/resource/Swissair_Flight_111>;
>    prov:startedAtTime "1998-09-02T01:31:00Z"^^xsd:dateTime;
>    prov:atLocation    <http://dbpedia.org/resource/Atlantic_ocean>;
> .
> ```

An instance of prov:Invalidation provides additional descriptions about the binary prov:wasInvalidatedBy relation from an invalidated prov:Entity to the prov:Activity that invalidated it. For example, :uncracked_egg prov:wasInvalidatedBy :baking; prov:qualifiedInvalidation [ a prov:Invalidation; prov:activity :baking; :foo :bar ].

is subclass of

prov:InstantaneousEvent (§4.3.19) , prov:ActivityInfluence (§4.3.10)

described with properties:

prov:activity (§4.3.40) op , prov:atTime (§4.3.44) dp

in range of

prov:qualifiedInvalidation (§4.3.29) op

qualifies

prov:wasInvalidatedBy (§4.2.16) op

PROV-DM term

[Invalidation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Invalidation "prov-dm")

### (49) Class: prov:AgentInfluence (§4.3.14) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#AgentInfluence

AgentInfluence is the capacity of an agent to have an effect on the character, development, or behavior of another by means of attribution, association, delegation, or other.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :illustrating
>     a prov:Activity;
>     prov:wasAssociatedWith :derek;
>     prov:qualifiedAssociation [
>        a prov:Association,
>          prov:AgentInfluence; ## Instances of Generation, Invalidation and Communication qualify
>        prov:agent   :derek;   ## the influence of an Agent (cited by prov:agent)
>        prov:hadRole :illustrationist
>     ];
> .
>
> :derek a prov:Person, prov:Agent, prov:Entity .
>
> :illustratonist a prov:Role .
> ```

AgentInfluence provides additional descriptions of an Agent's binary influence upon any other kind of resource. Instances of AgentInfluence use the prov:agent property to cite the influencing Agent.

It is not recommended that the type AgentInfluence be asserted without also asserting one of its more specific subclasses.

is subclass of

prov:Influence (§4.3.1)

described with properties:

prov:agent (§4.3.41) op

prov:hadRole (§4.3.45) op , prov:influencer (§4.3.36) op , prov:hadActivity (§4.3.43) op

has subclasses

prov:Delegation (§4.3.18) , prov:Association (§4.3.16) , prov:Attribution (§4.3.15)

### (50) Class: prov:Attribution (§4.3.15) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Attribution

Attribution is the ascribing of an entity to an agent.

When an entity e is attributed to agent ag, entity e was generated by some unspecified activity that in turn was associated to agent ag. Thus, this relation is useful when the activity is not known, or irrelevant.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> <http://dbpedia.org/resource/Fallingwater>
>    a prov:Entity;
>    prov:wasAttributedTo <http://dbpedia.org/resource/Edgar_J._Kaufmann>,
>                         <http://dbpedia.org/resource/Frank_Lloyd_Wright>,
>                         :western-Pennsylvania-Conservancy;
>    prov:qualifiedAttribution [
>       a prov:Attribution;
>       prov:agent <http://dbpedia.org/resource/Edgar_J._Kaufmann>;
>       ex:hadRole :owner;
>    ];
>    prov:qualifiedAttribution [
>       a prov:Attribution;
>       prov:agent <http://dbpedia.org/resource/Frank_Lloyd_Wright>;
>       ex:hadRole :architect;
>    ];
>    prov:qualifiedAttribution [
>       a prov:Attribution;
>       prov:agent :western-Pennsylvania-Conservancy;
>       ex:hadRole :conserver;
>    ];
> .
>
> <http://dbpedia.org/resource/Edgar_J._Kaufmann>  a prov:Person, prov:Agent .
> <http://dbpedia.org/resource/Frank_Lloyd_Wright> a prov:Person, prov:Agent .
> :western-Pennsylvania-Conservancy a prov:Organization, prov:Agent .
> ```

An instance of prov:Attribution provides additional descriptions about the binary prov:wasAttributedTo relation from an prov:Entity to some prov:Agent that had some responsible for it. For example, :cake prov:wasAttributedTo :baker; prov:qualifiedAttribution [ a prov:Attribution; prov:entity :baker; :foo :bar ].

is subclass of

prov:AgentInfluence (§4.3.14)

described with properties:

prov:agent (§4.3.41) op

in range of

prov:qualifiedAttribution (§4.3.28) op

qualifies

prov:wasAttributedTo (§4.1.6) op

PROV-DM term

[attribution](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-attribution "prov-dm")

### (51) Class: prov:Association (§4.3.16) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Association

An activity association is an assignment of responsibility to an agent for an activity, indicating that the agent had a role in the activity. It further allows for a plan to be specified, which is the plan intended by the agent to achieve some goals in the context of this activity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :illustrating
>     a prov:Activity;
>     prov:wasAssociatedWith :derek,
>                            :steve;
>     prov:qualifiedAssociation [
>         a prov:Association;
>         prov:agent   :derek;
>         prov:hadRole :illustrationist;
>     ];
>     prov:qualifiedAssociation [
>         a prov:Association;
>         prov:agent   :steve;
>         prov:hadRole :stylist;
>         prov:hadPlan :style-guide;
>         rdfs:comment "Steve helped Derek conform with the publisher's style guide."@en;
>     ];
> .
>
> :derek a prov:Person, prov:Agent, prov:Entity .
> :steve a prov:Person, prov:Agent, prov:Entity .
>
> :illustratonist a prov:Role .
> :stylist        a prov:Role .
>
> :style-guide a prov:Plan, prov:Entity .
> ```

An instance of prov:Association provides additional descriptions about the binary prov:wasAssociatedWith relation from an prov:Activity to some prov:Agent that had some responsiblity for it. For example, :baking prov:wasAssociatedWith :baker; prov:qualifiedAssociation [ a prov:Association; prov:agent :baker; :foo :bar ].

is subclass of

prov:AgentInfluence (§4.3.14)

described with properties:

prov:hadPlan (§4.3.42) op

prov:hadRole (§4.3.45) op

prov:agent (§4.3.41) op

in range of

prov:qualifiedAssociation (§4.3.33) op

qualifies

prov:wasAssociatedWith (§4.1.11) op

PROV-DM term

[Association](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Association "prov-dm")

### (52) Class: prov:Plan (§4.3.17) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Plan

A plan is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :illustrating
>    a prov:Activity;
>    prov:qualifiedAssociation :steve-checking-style-guide;
> .
>
> :steve-checking-style-guide
>    a prov:Association;
>    prov:agent   :steve;
>    prov:hadPlan :style-guide;
>    rdfs:comment "Steve followed the publisher's style guide"@en;
> .
>
> :style-guide
>    a prov:Plan, prov:Entity;
>    rdfs:comment "Use blue graphs for positive spin, red for negative"@en;
> .
> ```

There exist no prescriptive requirement on the nature of plans, their representation, the actions or steps they consist of, or their intended goals. Since plans may evolve over time, it may become necessary to track their provenance, so plans themselves are entities. Representing the plan explicitly in the provenance can be useful for various tasks: for example, to validate the execution as represented in the provenance record, to manage expectation failures, or to provide explanations.

is subclass of

prov:Entity (§4.1.1)

in range of

prov:hadPlan (§4.3.42) op

PROV-DM term

[Association](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Association "prov-dm")

### (53) Class: prov:Delegation (§4.3.18) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Delegation

Delegation is the assignment of authority and responsibility to an agent (by itself or by another agent) to carry out a specific activity as a delegate or representative, while the agent it acts on behalf of retains some responsibility for the outcome of the delegated work.

For example, a student acted on behalf of his supervisor, who acted on behalf of the department chair, who acted on behalf of the university; all those agents are responsible in some way for the activity that took place but we do not say explicitly who bears responsibility and to what degree.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> ### In this example, Frank (an insurance agent) acts on behalf of his company for performing
> ### a policy sale
>
> :policySale
>    a prov:Activity;
>    prov:wasAssociatedWith :insuranceAgent_Frank;
> .
>
> :insuranceAgent_Frank
>    a prov:Person;
>    prov:actedOnBehalfOf :insuranceCompany_A;
>    prov:qualifiedDelegation [
>       a prov:Delegation;
>       prov:agent        :insuranceCompany_A;
>       ex:rewardScheme   "commission";
>       prov:hadActivity  :policySale ;
>    ];
> .
> ```

An instance of prov:Delegation provides additional descriptions about the binary prov:actedOnBehalfOf relation from a performing prov:Agent to some prov:Agent for whom it was performed. For example, :mixing prov:wasAssociatedWith :toddler . :toddler prov:actedOnBehalfOf :mother; prov:qualifiedDelegation [ a prov:Delegation; prov:entity :mother; :foo :bar ].

is subclass of

prov:AgentInfluence (§4.3.14)

described with properties:

prov:hadActivity (§4.3.43) op

prov:agent (§4.3.41) op

in range of

prov:qualifiedDelegation (§4.3.35) op

qualifies

prov:actedOnBehalfOf (§4.1.12) op

PROV-DM term

[delegation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-delegation "prov-dm")

### (54) Class: prov:InstantaneousEvent (§4.3.19) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#InstantaneousEvent

The PROV data model is implicitly based on a notion of instantaneous events (or just events), that mark transitions in the world. Events include generation, usage, or invalidation of entities, as well as starting or ending of activities. This notion of event is not first-class in the data model, but it is useful for explaining its other concepts and its semantics.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix bbc:  <http://www.bbc.co.uk/> .
> @prefix :     <http://example.com/> .
>
> :bbcNews2012-04-03
>    a prov:Entity, :DailyNews;
>    rdfs:comment """The BBC news home page on 2012-04-03 contained
>                    a reference to a given news item, but the BBC news
>                    home page on the next day did not.""";
>
>    prov:qualifiedGeneration [
>       a prov:Generation, prov:InstantaneousEvent;
>       prov:atTime "2012-04-03T00:00:01Z"^^xsd:dateTime;
>    ];
>    prov:qualifiedInvalidation [
>       a prov:Invalidation, prov:InstantaneousEvent;
>       prov:atTime "2012-04-03T23:59:59Z"^^xsd:dateTime;
>    ];
> .
> ```

An instantaneous event, or event for short, happens in the world and marks a change in the world, in its activities and in its entities. The term 'event' is commonly used in process algebra with a similar meaning. Events represent communications or interactions; they are assumed to be atomic and instantaneous.

described with properties:

prov:atTime (§4.3.44) dp

prov:hadRole (§4.3.45) op , prov:atLocation (§4.2.22) op

has subclasses

prov:Generation (§4.3.11) , prov:Start (§4.3.4) , prov:Invalidation (§4.3.13) , prov:End (§4.3.5) , prov:Usage (§4.3.3)

### (55) Class: prov:Role (§4.3.20) back to qualified classes

**IRI:** http://www.w3.org/ns/prov#Role

A role is the function of an entity or agent with respect to an activity, in the context of a usage, generation, invalidation, association, start, and end.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :divideActivity
>    a prov:Activity;
>    prov:used :variableA, :variableB;
>
>    prov:qualifiedUsage [
>       a prov:Usage;
>       prov:entity  :variableA;
>       prov:hadRole :dividend;
>    ];
>    prov:qualifiedUsage [
>       a prov:Usage;
>       prov:entity  :variableB;
>       prov:hadRole :divisor;
>    ];
>
>    prov:generated :result_112234;
> .
>
> :variableA
>    a prov:Entity;
>    prov:value 10;
> .
> :variableB
>    a prov:Entity;
>    prov:value 2;
> .
>
> :dividend a prov:Role.
> :divisor  a prov:Role.
>
> :result_112234
>    a prov:Entity;
>    prov:value 5;
>    prov:wasGeneratedBy :divideActivity;
> .
> ```

in range of

prov:hadRole (§4.3.45) op

PROV-DM term

[attribute-role](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-attribute-role "prov-dm")

### (56) Property: prov:wasInfluencedBy (§4.3.21) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#wasInfluencedBy

Influence is the capacity of an entity, activity, or agent to have an effect on the character, development, or behavior of another by means of usage, start, end, generation, invalidation, communication, derivation, attribution, association, or delegation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :illustrationActivity
>    a prov:Activity;
>    prov:used              :aggregatedByRegions;
>    prov:wasAssociatedWith :derek;
>    prov:wasInformedBy     :aggregationActivity;
> .
>
> :illustrationActivity
>    a prov:Activity;
>    prov:wasInfluencedBy :aggregatedByRegions, # prov:wasInfluencedBy is a superproperty of
>                         :derek,               # many of the direct binary
>                         :aggregationActivity; # PROV-O properties.
> .
>
> :aggregationActivity a prov:Activity .
> :derek               a prov:Agent .
> :aggregatedByRegions a prov:Entity .
> ```

Because prov:wasInfluencedBy is a broad relation, its more specific subproperties (e.g. prov:wasInformedBy, prov:actedOnBehalfOf, prov:wasEndedBy, etc.) should be used when applicable.

This property has multiple RDFS domains to suit multiple OWL Profiles. See §A PROV-O OWL Profile.

has domain

- prov:Activity (§4.1.2) or prov:Agent (§4.1.3) or prov:Entity (§4.1.1)

has range

- prov:Activity (§4.1.2) or prov:Agent (§4.1.3) or prov:Entity (§4.1.1)

has sub-properties

- prov:hadMember (§4.2.17)
- prov:wasAttributedTo (§4.1.6)
- prov:wasAssociatedWith (§4.1.11)
- prov:wasGeneratedBy (§4.1.4)
- prov:wasDerivedFrom (§4.1.5)
- prov:wasInvalidatedBy (§4.2.16)
- prov:used (§4.1.8)
- prov:actedOnBehalfOf (§4.1.12)
- prov:wasInformedBy (§4.1.9)
- prov:wasStartedBy (§4.2.18)
- prov:wasEndedBy (§4.2.19)

can be qualified with

- prov:qualifiedInfluence (§4.3.22) op
- prov:Influence (§4.3.1)

PROV-DM term

[influence](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-influence "prov-dm")

### (57) Property: prov:qualifiedInfluence (§4.3.22) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedInfluence

Influence is the capacity of an entity, activity, or agent to have an effect on the character, development, or behavior of another by means of usage, start, end, generation, invalidation, communication, derivation, attribution, association, or delegation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix my:   <http://example.com/ontology#> .
> @prefix :     <http://example.com/> .
>
> # Although domain extension 'my:wasConductedBy' is not defined by PROV-O,
> # the relation between a surgery and an agent can still be qualified
> # by reusing prov:Influence and one of its three subclasses:
> # AgentInfluence, EntityInfluence, and ActivityInfluence
> # (depending on the type of the influencing object).
>
> :conductingSurgery_1
>    a prov:Activity;
>
>    # This unqualified influence is unknown in PROV;
>    # it would be a subproperty of prov:wasAssociatedWith.
>    my:wasConductedBy    :bob;
>    prov:wasInfluencedBy :bob;
>    prov:qualifiedInfluence [
>       # Even though PROV systems do not understand my:wasConductedBy,
>       # they will at least understand that :bob influenced the
>       # surgery in some way.
>       a prov:Influence;      # Inferred
>       prov:agent   :bob;     # The object of my:wasConductedBy
>
>       # Domain extension properties may be used to describe the
>       # influences that an Entity, Activity, or Agent
>       # have upon another Entity, Activity, or Agent.
>       my:degree .72;
>    ];
> .
>
> :bob a prov:Agent .
> ```

Because prov:qualifiedInfluence is a broad relation, the more specific relations (qualifiedCommunication, qualifiedDelegation, qualifiedEnd, etc.) should be used when applicable.

has domain

- prov:Activity (§4.1.2) or prov:Agent (§4.1.3) or prov:Entity (§4.1.1)

has range

- prov:Influence (§4.3.1)

has sub-properties

- prov:qualifiedAssociation (§4.3.33)
- prov:qualifiedRevision (§4.3.27)
- prov:qualifiedInvalidation (§4.3.29)
- prov:qualifiedPrimarySource (§4.3.25)
- prov:qualifiedDerivation (§4.3.24)
- prov:qualifiedGeneration (§4.3.23)
- prov:qualifiedUsage (§4.3.31)
- prov:qualifiedQuotation (§4.3.26)
- prov:qualifiedStart (§4.3.30)
- prov:qualifiedAttribution (§4.3.28)
- prov:qualifiedEnd (§4.3.34)
- prov:qualifiedCommunication (§4.3.32)
- prov:qualifiedDelegation (§4.3.35)

qualifies

prov:wasInfluencedBy (§4.3.21) op

PROV-DM term

[influence](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-influence "prov-dm")

### (58) Property: prov:qualifiedGeneration (§4.3.23) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedGeneration

Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :bar_chart
>    a prov:Entity;
>    prov:wasGeneratedBy :illustrating;
>    prov:qualifiedGeneration [
>       a prov:Generation;
>       prov:activity :illustrating;
>       rdfs:comment "Ended up with bar chart as line chart looked ugly."@en;
>    ];
> .
>
> :illustrating a prov:Activity .
> ```

If this Activity prov:generated Entity :e, then it can qualify how it performed the Generation using prov:qualifiedGeneration [ a prov:Generation; prov:entity :e; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Generation (§4.3.11)

qualifies

prov:wasGeneratedBy (§4.1.4) op

PROV-DM term

[Generation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Generation "prov-dm")

### (59) Property: prov:qualifiedDerivation (§4.3.24) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedDerivation

A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :bar_chart
>    a prov:Entity;
>    prov:wasDerivedFrom :aggregatedByRegions;
>    prov:qualifiedDerivation [
>       a prov:Derivation;
>       prov:entity :aggregatedByRegions;
>
>       ## More details about the activity underpinning the derivation
>       prov:hadGeneration :chat_plotting;
>       prov:hadActivity   :chart_creation ;
>    ];
> .
>
> ### The process of creating the chart, from loading the data, to process it, and plot it to end users
>
> :chart_creation
>     a    prov:Activity ;
>     prov:wasAssociatedWith :derek;
>     prov:startedAtTime  "2011-07-16T01:52:02Z"^^xsd:dateTime;
>     prov:endedAtTime "2011-07-16T03:00:02Z"^^xsd:dateTime;
> .
>
> #### Now the chart is plotted
>
> :chat_plotting
>     a    prov:Generation ;
>     prov:atTime    "2011-07-16T03:00:02Z"^^xsd:dateTime;
> .
> ```

If this Entity prov:wasDerivedFrom Entity :e, then it can qualify how it was derived using prov:qualifiedDerivation [ a prov:Derivation; prov:entity :e; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Derivation (§4.3.6)

qualifies

prov:wasDerivedFrom (§4.1.5) op

PROV-DM term

[Derivation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Derivation "prov-dm")

### (60) Property: prov:qualifiedPrimarySource (§4.3.25) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedPrimarySource

A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight.

Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated.

A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:     <http://www.w3.org/2002/07/owl#> .
> @prefix dcterms: <http://purl.org/dc/terms/> .
> @prefix prov:    <http://www.w3.org/ns/prov#> .
> @prefix ex:      <http://example.com/vocab#> .
> @prefix :        <http://example.com/> .
>
> :temperatureDisplay
>    a prov:Entity;
>    prov:hadPrimarySource :sensorReading20120510;
>    prov:qualifiedPrimarySource [
>       a prov:PrimarySource;
>       prov:entity        :sensorReading20120510;
>       ex:precisionLoss true;
>       rdfs:comment """The displayed temperature does not show the full precision
>                       available in the reading.""";
>    ];
> .
>
> :sensorReading20120510
>    a prov:Entity;
>    prov:wasGeneratedBy :temperatureSensor;
> .
> ```

If this Entity prov:hadPrimarySource Entity :e, then it can qualify how using prov:qualifiedPrimarySource [ a prov:PrimarySource; prov:entity :e; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:PrimarySource (§4.3.7)

qualifies

prov:hadPrimarySource (§4.2.11) op

PROV-DM term

[primary-source](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-primary-source "prov-dm")

### (61) Property: prov:qualifiedQuotation (§4.3.26) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedQuotation

A quotation is the repeat of (some or all of) an entity, such as text or image, by someone who may or may not be its original author. Quotation is a particular case of derivation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix my:   <http://example.com/vocab/my#> .
> @prefix :     <http://example.com/> .
>
> :bl-dagstuhl
>    a prov:Entity;
>    prov:value """During the workshop, it became clear to me that the consensus
>    based models (which are often graphical in nature) can not only be
>    formalized but also be directly connected to these database focused
>    formalizations. I just needed to get over the differences in syntax.
>    This could imply that we could have nice way to trace provenance across
>    systems and through databases and be able to understand the
>    mathematical properties of this interconnection.""";
>    prov:wasQuotedFrom <http://purl.org/twc/page/thoughts-from-the-dagstuhl-workshop>;
>    prov:qualifiedQuotation [
>       a prov:Quotation;
>       prov:entity <http://purl.org/twc/page/thoughts-from-the-dagstuhl-workshop>;
>       my:fromSection 1;
>    ];
> .
>
> <http://purl.org/twc/page/thoughts-from-the-dagstuhl-workshop>
>    a prov:Entity;
>    prov:wasAttributedTo <http://data.semanticweb.org/person/paul-groth>;
> .
>
> <http://data.semanticweb.org/person/luc-moreau> a prov:Person, prov:Agent .
> <http://data.semanticweb.org/person/paul-groth> a prov:Person, prov:Agent .
> ```

If this Entity prov:wasQuotedFrom Entity :e, then it can qualify how using prov:qualifiedQuotation [ a prov:Quotation; prov:entity :e; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Quotation (§4.3.8)

qualifies

prov:wasQuotedFrom (§4.2.13) op

PROV-DM term

[quotation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-quotation "prov-dm")

### (62) Property: prov:qualifiedRevision (§4.3.27) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedRevision

A revision is a derivation for which the resulting entity is a revised version of some original. The implication here is that the resulting entity contains substantial content from the original. Revision is a particular case of derivation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :draft2
>    a prov:Entity;
>    prov:wasRevisionOf :draft1;
>    prov:qualifiedRevision [
>       a prov:Revision;
>       prov:entity :draft1
>    ];
>    prov:wasAttributedTo :eddie;
> .
>
> :draft1 a prov:Entity .
> :eddie  a prov:Person, prov:Agent, prov:Entity .
> ```

If this Entity prov:wasRevisionOf Entity :e, then it can qualify how it was revised using prov:qualifiedRevision [ a prov:Revision; prov:entity :e; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Revision (§4.3.9)

qualifies

prov:wasRevisionOf (§4.2.14) op

PROV-DM term

[revision](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-revision "prov-dm")

### (63) Property: prov:qualifiedAttribution (§4.3.28) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedAttribution

Attribution is the ascribing of an entity to an agent.

When an entity e is attributed to agent ag, entity e was generated by some unspecified activity that in turn was associated to agent ag. Thus, this relation is useful when the activity is not known, or irrelevant.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> ## When the role of the agent is not known or does not matter:
>
> :nationalRegionsList
>    a prov:Entity;
>    prov:wasAttributedTo :civil_action_group;
> .
>
> :civil_action_group a prov:Agent .
>
> ## If we want to express the role of the agent:
>
> :nationalRegionsList
>    a prov:Entity;
>    prov:qualifiedAttribution [
>       a prov:Attribution;
>       prov:agent :civil_action_group;
>       ex:hadRole :owner;
>    ]
> .
> ```

If this Entity prov:wasAttributedTo Agent :ag, then it can qualify how it was influenced using prov:qualifiedAttribution [ a prov:Attribution; prov:agent :ag; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Attribution (§4.3.15)

qualifies

prov:wasAttributedTo (§4.1.6) op

PROV-DM term

[attribution](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-attribution "prov-dm")

### (64) Property: prov:qualifiedInvalidation (§4.3.29) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedInvalidation

Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity. The entity is no longer available for use (or further invalidation) after invalidation. Any generation or usage of an entity precedes its invalidation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/ontology#> .
> @prefix :     <http://example.com/> .
>
> :the-Painter
>    a prov:Entity, ex:Painting;
>    rdfs:label "Le Peintre"@fr, "The Painter"@en;
>    prov:wasAttributedTo <http://dbpedia.org/resource/Pablo_Picasso>;
>
>    prov:wasInvalidatedBy :swissair_Flight_111_crash;
>    prov:qualifiedInvalidation [
>       a prov:Invalidation;
>       prov:activity    :swissair_Flight_111_crash;
>       prov:atTime      "1998-09-02T01:31:00Z"^^xsd:dateTime;
>       prov:atLocation  <http://purl.org/twc/location/Swissair-Flight-111-crash>;
>    ];
> .
>
> :swissair_Flight_111_crash a prov:Activity .
> <http://purl.org/twc/location/Swissair-Flight-111-crash> a prov:Location .
> ```

If this Entity prov:wasInvalidatedBy Activity :a, then it can qualify how it was invalidated using prov:qualifiedInvalidation [ a prov:Invalidation; prov:activity :a; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Entity (§4.1.1)

has range

- prov:Invalidation (§4.3.13)

qualifies

prov:wasInvalidatedBy (§4.2.16) op

PROV-DM term

[Invalidation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Invalidation "prov-dm")

### (65) Property: prov:qualifiedStart (§4.3.30) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedStart

Start is when an activity is deemed to have been started by an entity, known as trigger. The activity did not exist before its start. Any usage, generation, or invalidation involving an activity follows the activity's start. A start may refer to a trigger entity that set off the activity, or to an activity, known as starter, that generated the trigger.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> # Start can be used to qualify wasStartedBy with time and location information.
>
> :consistency_checking
>    a prov:Activity;
>    prov:wasStartedBy :updated_data_record;
>    prov:qualifiedStart [
>       a prov:Start;
>       prov:entity       :updated_data_record;
>       prov:atTime       "2011-07-06T01:48:36Z"^^xsd:dateTime;
>       prov:atLocation   :scienceLab_003;
>       prov:hadActivity  :syntax_checking;
>    ];
> .
>
> :updated_data_record a prov:Entity .
>
> ### There is an explicit process of checking the syntax of the updated data record
>
> :syntax_checking
>    a   prov:Activity ;
>    prov:startedAtTime      "2011-07-06T01:48:36Z"^^xsd:dateTime;
>    prov:endedAtTime        "2011-07-06T02:12:36Z"^^xsd:dateTime;
>    prov:wasAssociatedWith  :syntax_checker ;
> .
>
> :syntax_checker   a   prov:SoftwareAgent .
> ```

If this Activity prov:wasStartedBy Entity :e1, then it can qualify how it was started using prov:qualifiedStart [ a prov:Start; prov:entity :e1; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Start (§4.3.4)

qualifies

prov:wasStartedBy (§4.2.18) op

PROV-DM term

[Start](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Start "prov-dm")

### (66) Property: prov:qualifiedUsage (§4.3.31) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedUsage

Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> :newsPublication
>    a prov:Activity;
>    prov:used                    :tsunami_image;
>    prov:qualifiedUsage [
>       a prov:Usage;
>       prov:entity               :tsunami_image;
>       ex:hasCopyrightPermission :licensedUse;
>       ex:hasOwner               :reuters;
>    ];
> .
>
> :tsunami_image a prov:Entity .
> :reuters       a prov:Agent .
> ```

If this Activity prov:used Entity :e, then it can qualify how it used it using prov:qualifiedUsage [ a prov:Usage; prov:entity :e; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Usage (§4.3.3)

qualifies

prov:used (§4.1.8) op

PROV-DM term

[Usage](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Usage "prov-dm")

### (67) Property: prov:qualifiedCommunication (§4.3.32) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedCommunication

Communication is the exchange of an entity by two activities, one activity using the entity generated by the other.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :writing-celebrity-gossip
>    a prov:Activity;
>    prov:wasAssociatedWith :journalist;
>    prov:wasInformedBy     :voicemail-interception;
>    prov:qualifiedCommunication [
>       a prov:Communication;
>       prov:activity :voicemail-interception;
>       rdfs:comment """The journalist was informed by the private
>                       investigator, but we don't know how or what he was told."""@en;
>    ];
> .
>
> :voicemail-interception
>    a prov:Activity;
>    prov:wasAssociatedWith :private-investigator;
> .
>
> :private-investigator a prov:Agent .
> :journalist           a prov:Agent .
> ```

If this Activity prov:wasInformedBy Activity :a, then it can qualify how it was influenced using prov:qualifiedCommunication [ a prov:Communication; prov:activity :a; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Communication (§4.3.12)

can be qualified with

- prov:Communication (§4.3.12)

PROV-DM term

[Communication](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Communication "prov-dm")

### (68) Property: prov:qualifiedAssociation (§4.3.33) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedAssociation

An activity association is an assignment of responsibility to an agent for an activity, indicating that the agent had a role in the activity. It further allows for a plan to be specified, which is the plan intended by the agent to achieve some goals in the context of this activity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :illustrating
>     a prov:Activity;
>     prov:wasAssociatedWith :derek,
>                            :steve;
>     prov:qualifiedAssociation [
>         a prov:Association;
>         prov:agent   :derek;
>         prov:hadRole :illustrationist;
>         rdfs:comment "Derek made the illustration"@en
>     ];
>     prov:qualifiedAssociation [
>         a prov:Association;
>         prov:agent   :steve;
>         prov:hadRole :stylist;
>         prov:hadPlan :style-guide;
>         rdfs:comment "Steve helped Derek conform with the publisher's style guide."@en
>     ];
>     prov:qualifiedAssociation [
>         a prov:Association;
>         prov:agent   :derek;
>         prov:hadRole :stylist;
>         rdfs:comment "But Derek also did some styling of his own."@en
>     ] .
>
> :derek a prov:Person, prov:Agent .
> :steve a prov:Person, prov:Agent .
>
> :illustratonist a prov:Role .
> :stylist        a prov:Role .
>
> :style-guide a prov:Plan, prov:Entity .
> ```

If this Activity prov:wasAssociatedWith Agent :ag, then it can qualify the Association using prov:qualifiedAssociation [ a prov:Association; prov:agent :ag; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:Association (§4.3.16)

qualifies

prov:wasAssociatedWith (§4.1.11) op

PROV-DM term

[Association](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Association "prov-dm")

### (69) Property: prov:qualifiedEnd (§4.3.34) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedEnd

End is when an activity is deemed to have been ended by an entity, known as trigger. The activity no longer exists after its end. Any usage, generation, or invalidation involving an activity precedes the activity's end. An end may refer to a trigger entity that terminated the activity, or to an activity, known as ender that generated the trigger.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> ### End can be used to qualify wasEndedBy with time and location information
>
> :experiment
>    a prov:Activity;
>    prov:wasEndedBy :inconsistentResult;
>    prov:qualifiedEnd [
>       a prov:End;
>       prov:entity       :inconsistentResult;
>       prov:atTime       "2011-07-16T01:52:02Z"^^xsd:dateTime;
>       prov:atLocation   :scienceLab_003;
>       prov:hadActivity  :analyse_intermediate_result ;
>    ];
> .
>
> :inconsistentResult a prov:Entity .
>
> ### An implicit process of analysing the intermediate result to confirm its expected consistency
>
> analyse_intermediate_result
>    a   prov:Activity ;
>    prov:startedAtTime   "2011-07-15T12:52:02Z"^^xsd:dateTime;
>    prov:endedAtTime     "2011-07-16T01:52:02Z"^^xsd:dateTime;
> .
> ```

If this Activity prov:wasEndedBy Entity :e1, then it can qualify how it was ended using prov:qualifiedEnd [ a prov:End; prov:entity :e1; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Activity (§4.1.2)

has range

- prov:End (§4.3.5)

qualifies

prov:wasEndedBy (§4.2.19) op

PROV-DM term

[End](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-End "prov-dm")

### (70) Property: prov:qualifiedDelegation (§4.3.35) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#qualifiedDelegation

Delegation is the assignment of authority and responsibility to an agent (by itself or by another agent) to carry out a specific activity as a delegate or representative, while the agent it acts on behalf of retains some responsibility for the outcome of the delegated work.

For example, a student acted on behalf of his supervisor, who acted on behalf of the department chair, who acted on behalf of the university; all those agents are responsible in some way for the activity that took place but we do not say explicitly who bears responsibility and to what degree.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> :traffic-stop
>    a prov:Activity;
>    prov:wasAssociatedWith :chauffeur,
>                           :traffic-officer-34;
>    prov:qualifiedAssociation [
>       a prov:Association;
>       prov:agent :chauffeur;
>
>       # The chauffeur was the one violating traffic rules.
>       prov:hadRole :violator;
>    ];
>    prov:qualifiedAssociation [
>       a prov:Association;
>       prov:agent :traffic-officer-34;
>
>       # The officer was the one enforcing the traffic rules.
>       prov:hadRole :enforcer;
>    ];
> .
>
> :chauffeur
>    a prov:Person;
>    prov:actedOnBehalfOf :celebrity-in-car;
>    prov:qualifiedDelegation [
>       a prov:Delegation;
>       prov:agent :celebrity-in-car;
>
>       # The celebrity employed the chauffeur during the enforcement.
>       prov:hadRole :employer;
>       prov:hadActivity  :driving-during-the-year ;
>    ];
> .
>
> #The chaffeur was employed for a whole year as a driver
> :driving-during-the-year   a   prov:Activity ;
>    prov:wasAssociatedWith :chaffeur;
>    prov:qualifiedAssociation [
>       a prov:Association;
>       prov:hadRole :driver;
>    ];
>    prov:startedAtTime "2011-07-16T01:52:02Z"^^xsd:dateTime;
>    prov:endedAtTime "2012-07-16T01:52:02Z"^^xsd:dateTime;;
> .
>
> :traffic_officer_34
>    a prov:Person;
>    prov:actedOnBehalfOf :city-of-Paris;
>    prov:qualifiedDelegation [
>       a prov:Delegation;
>       prov:agent :city-of-Paris;
>
>       # The city of Paris employed the officer during the enforcement.
>       prov:hadRole :employer;
>       prov:hadActivity      :control-city-traffic ;
>    ];
> .
>
> :control-city-traffic   a   prov:Activity .
> ```

If this Agent prov:actedOnBehalfOf Agent :ag, then it can qualify how with prov:qualifiedResponsibility [ a prov:Responsibility; prov:agent :ag; :foo :bar ].

has super-properties

- prov:qualifiedInfluence (§4.3.22) op

has domain

- prov:Agent (§4.1.3)

has range

- prov:Delegation (§4.3.18)

qualifies

prov:actedOnBehalfOf (§4.1.12) op

PROV-DM term

[delegation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-delegation "prov-dm")

### (71) Property: prov:influencer (§4.3.36) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#influencer

This property is used as part of the qualified influence pattern. Subclasses of prov:Influence use these subproperties to reference the resource (Entity, Agent, or Activity) whose influence is being qualified.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :illustrationActivity
>    a prov:Activity;
>    prov:qualifiedUsage         :illustration_usage;
>    prov:qualifiedAssociation   :illustration_association;
>    prov:qualifiedCommunication :illustration_communication;
> .
>
> :illustration_usage
>    a prov:Usage;
>    prov:entity     :aggregatedByRegions;
>    prov:influencer :aggregatedByRegions; # Inferred
> .
>
> :illustration_association
>    a prov:Association;
>    prov:agent      :derek;
>    prov:influencer :derek; # - - - - - - - Inferred
> .
>
> :illustration_communication
>    a prov:Communication;
>    prov:activity   :aggregationActivity;
>    prov:influencer :aggregationActivity; # Inferred
> .
>
> :aggregationActivity a prov:Activity .
> :derek               a prov:Agent .
> :aggregatedByRegions a prov:Entity .
> ```

Subproperties of prov:influencer are used to cite the object of an unqualified PROV-O triple whose predicate is a subproperty of prov:wasInfluencedBy (e.g. prov:used, prov:wasGeneratedBy). prov:influencer is used much like rdf:object is used.

has domain

- prov:Influence (§4.3.1)

has range

-

has sub-properties

- prov:agent (§4.3.41)
- prov:entity (§4.3.37)
- prov:activity (§4.3.40)

PROV-DM term

[influence](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-influence "prov-dm")

### (72) Property: prov:entity (§4.3.37) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#entity

The prov:entity property references an prov:Entity which influenced a resource. This property applies to an prov:EntityInfluence, which is given by a subproperty of prov:qualifiedInfluence from the influenced prov:Entity, prov:Activity or prov:Agent.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :world-literature-homework-submission-32
>    a prov:Entity;
>    prov:hadPrimarySource :donQuixote;
>    prov:qualifiedPrimarySource [
>       a prov:PrimarySource;
>       prov:entity :donQuixote;
>       # Other attributes of the relationship
>    ];
> .
>
> :donQuixote a prov:Entity .
> ```

has super-properties

- prov:influencer (§4.3.36) op

has domain

- prov:EntityInfluence (§4.3.2)

has range

- prov:Entity (§4.1.1)

### (73) Property: prov:hadUsage (§4.3.38) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#hadUsage

Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
> :digestedProteinSample1
>    a prov:Entity;
>    prov:wasDerivedFrom :proteinSample;
>    prov:qualifiedDerivation [
>       a prov:Derivation;
>       prov:hadUsage [
>          a prov:Usage;
>          prov:entity :Trypsin;
>         prov:hadRole :treatmentEnzyme;
>       ];
>    ];
>    prov:entity :proteinSample;
> .
> :proteinSample a prov:Entity .
> ```

The _optional_ Usage involved in an Entity's Derivation.

has domain

- prov:Derivation (§4.3.6)

has range

- prov:Usage (§4.3.3)

PROV-DM term

[Usage](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Usage "prov-dm")

### (74) Property: prov:hadGeneration (§4.3.39) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#hadGeneration

Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix ex:   <http://example.com/vocab#> .
> @prefix :     <http://example.com/> .
>
> :bar_chart
>    a prov:Entity, ex:Chart;
>    prov:wasDerivedFrom   :aggregatedByRegions;
>    prov:qualifiedDerivation [
>       a prov:Derivation;
>       prov:entity        :aggregatedByRegions;
>       prov:hadGeneration :illustration;
>    ];
> .
>
> :aggregatedByRegions a ex:Dataset .
>
> :illustration
>    a prov:Generation,
>      prov:InstantaneousEvent;
>    prov:activity :illustrationActivity;
>    prov:atTime   "2012-04-03T00:00:11Z"^^xsd:dateTime;
> .
>
> :illustrationActivity
>    a prov:Activity;
>    prov:startedAtTime "2012-04-03T00:00:00Z"^^xsd:dateTime;
>    prov:endedAtTime   "2012-04-03T00:00:25Z"^^xsd:dateTime;
> .
> ```

The _optional_ Generation involved in an Entity's Derivation.

has domain

- prov:Derivation (§4.3.6)

has range

- prov:Generation (§4.3.11)

PROV-DM term

[Generation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Generation "prov-dm")

### (75) Property: prov:activity (§4.3.40) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#activity

The prov:activity property references an prov:Activity which influenced a resource. This property applies to an prov:ActivityInfluence, which is given by a subproperty of prov:qualifiedInfluence from the influenced prov:Entity, prov:Activity or prov:Agent.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :making-bar-chart
>    a prov:Generation,
>      prov:ActivityInfluence;
>    prov:activity :illustrating;
>    rdfs:comment "Ended up with bar chart as line chart looked ugly."@en;
> .
>
> :illustrating a prov:Activity .
>
> :bar_chart
>    a prov:Entity;
>    prov:wasGeneratedBy :illustrating;
>    prov:qualifiedGeneration :making-bar-chart;
> .
> ```

has super-properties

- prov:influencer (§4.3.36) op

has domain

- prov:ActivityInfluence (§4.3.10)

has range

- prov:Activity (§4.1.2)

### (76) Property: prov:agent (§4.3.41) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#agent

The prov:agent property references an prov:Agent which influenced a resource. This property applies to an prov:AgentInfluence, which is given by a subproperty of prov:qualifiedInfluence from the influenced prov:Entity, prov:Activity or prov:Agent.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :world_flight_1937
>    a prov:Activity;
>
>    prov:wasAssociatedWith <http://dbpedia.org/resource/Amelia_Earhart>,
>                           <http://dbpedia.org/resource/Purdue_University>,
>                           <http://dbpedia.org/resource/Lockheed_Aircraft_Company>;
>    prov:qualifiedAssociation [
>       a prov:Association;
>       prov:agent   <http://dbpedia.org/resource/Amelia_Earhart>;
>       prov:hadRole :pilot;
>    ];
>    prov:qualifiedAssociation [
>       a prov:Association;
>       prov:agent   <http://dbpedia.org/resource/Purdue_University>;
>       prov:hadRole :financer;
>    ];
>    prov:qualifiedAssociation [
>       a prov:Association;
>       prov:agent   <http://dbpedia.org/resource/Lockheed_Aircraft_Company>;
>       prov:hadRole :plane_builder;
>    ];
>
>    rdfs:seeAlso <http://en.wikipedia.org/wiki/Amelia_Earhart#1937_world_flight>;
> .
>
> <http://dbpedia.org/resource/Amelia_Earhart>            a prov:Person,       prov:Agent .
> <http://dbpedia.org/resource/Purdue_University>         a prov:Organization, prov:Agent .
> <http://dbpedia.org/resource/Lockheed_Aircraft_Company> a prov:Organization, prov:Agent .
> ```

has super-properties

- prov:influencer (§4.3.36) op

has domain

- prov:AgentInfluence (§4.3.14)

has range

- prov:Agent (§4.1.3)

### (77) Property: prov:hadPlan (§4.3.42) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#hadPlan

A plan is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :illustrating
>    a prov:Activity;
>    prov:wasAssociatedWith :derek,
>                           :steve;
>    prov:qualifiedAssociation [
>       a prov:Association;
>       prov:agent   :steve;
>       prov:hadRole :stylist;
>       prov:hadPlan :style-guide;
>       rdfs:comment "Steve followed the style guide"@en;
>    ];
> .
>
> :style-guide
>    a prov:Plan, prov:Entity;
>    rdfs:comment "Use blue graphs for positive spin, red for negative"@en;
> .
> ```

The _optional_ Plan adopted by an Agent in Association with some Activity. Plan specifications are out of the scope of this specification.

has domain

- prov:Association (§4.3.16)

has range

- prov:Plan (§4.3.17)

PROV-DM term

[Association](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Association "prov-dm")

### (78) Property: prov:hadActivity (§4.3.43) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#hadActivity

An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> # The activity that which used, generated, invalidated
> # or was responsible for the entity. In this qualified Derivation
> # prov:hadActivity references the activity that generated the bar chart.
>
> :bar_chart
>    a prov:Entity;
>    prov:wasDerivedFrom :aggregatedByRegions;
>    prov:wasGeneratedBy :make_bar_chart;
>    prov:qualifiedDerivation [
>       a prov:Derivation;
>       prov:entity      :aggregatedByRegions;
>       prov:hadActivity :make_bar_chart; # references same activity as prov:wasGeneratedBy
>    ];
> .
>
> :aggregatedByRegions a prov:Entity .
> :make_bar_chart      a prov:Activity .
> ```

The _optional_ Activity of an Influence, which used, generated, invalidated, or was the responsibility of some Entity. This property is _not_ used by ActivityInfluence (use prov:activity instead).

This property has multiple RDFS domains to suit multiple OWL Profiles. See §A PROV-O OWL Profile.

has domain

- prov:Delegation (§4.3.18) or prov:Derivation (§4.3.6) or prov:End (§4.3.5) or prov:Start (§4.3.4)
- prov:Influence (§4.3.1)

has range

- prov:Activity (§4.1.2)

PROV-DM term

[Activity](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-Activity "prov-dm")

### (79) Property: prov:atTime (§4.3.44) dp back to qualified properties

**IRI:** http://www.w3.org/ns/prov#atTime

The PROV data model is implicitly based on a notion of instantaneous events (or just events), that mark transitions in the world. Events include generation, usage, or invalidation of entities, as well as starting or ending of activities. This notion of event is not first-class in the data model, but it is useful for explaining its other concepts and its semantics.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :Timearticle20120430_publication
>    a prov:InstantaneousEvent;
>    prov:atTime "2012-04-30T20:40:40"^^xsd:dateTime;
> .
> ```

The time at which an InstantaneousEvent occurred, in the form of xsd:dateTime.

has domain

- prov:InstantaneousEvent (§4.3.19)

has range

- http://www.w3.org/2001/XMLSchema#dateTime

qualifies

prov:invalidatedAtTime (§4.2.15) dp

### (80) Property: prov:hadRole (§4.3.45) op back to qualified properties

**IRI:** http://www.w3.org/ns/prov#hadRole

A role is the function of an entity or agent with respect to an activity, in the context of a usage, generation, invalidation, association, start, and end.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :divideActivity
>    a prov:Activity;
>
>    prov:used         :variableA;
>    prov:qualifiedUsage [
>       a prov:Usage;
>       prov:entity    :variableA;
>       prov:hadRole   :dividend;
>    ];
>
>    prov:used         :variableB;
>    prov:qualifiedUsage [
>       a prov:Usage;
>       prov:entity    :variableB;
>       prov:hadRole   :divisor;
>    ];
> .
>
> :variableA a prov:Entity .
> :variableB a prov:Entity .
>
> :dividend a prov:Role .
> :divisor  a prov:Role .
> ```

The _optional_ Role that an Entity assumed in the context of an Activity. For example, :baking prov:used :spoon; prov:qualified [ a prov:Usage; prov:entity :spoon; prov:hadRole roles:mixing_implement ].

This property has multiple RDFS domains to suit multiple OWL Profiles. See §A PROV-O OWL Profile.

has domain

- prov:Association (§4.3.16) or prov:InstantaneousEvent (§4.3.19)
- prov:Influence (§4.3.1)

has range

- prov:Role (§4.3.20)

PROV-DM term

[attribute-role](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#term-attribute-role "prov-dm")

### 4.4 Term Index

The PROV-O terms in this cross reference are shown below alphabetically, along with their entry number.

*Table 4 (§4.4): Term Index.*

| PROV-O Term                                                                    | Position within Cross Reference                                  |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| actedOnBehalfOf (§4.1.12)               | Entry 12 (§4.1.12)        |
| Activity (§4.1.2)                             | Entry 2 (§4.1.2)                |
| activity (§4.3.40)                           | Entry 75 (§4.3.40)             |
| ActivityInfluence (§4.3.10)           | Entry 45 (§4.3.10)      |
| Agent (§4.1.3)                                   | Entry 3 (§4.1.3)                   |
| agent (§4.3.41)                                 | Entry 76 (§4.3.41)                |
| AgentInfluence (§4.3.14)                 | Entry 49 (§4.3.14)         |
| alternateOf (§4.2.8)                       | Entry 20 (§4.2.8)            |
| Association (§4.3.16)                       | Entry 51 (§4.3.16)            |
| atLocation (§4.2.22)                         | Entry 34 (§4.2.22)             |
| atTime (§4.3.44)                                 | Entry 79 (§4.3.44)                 |
| Attribution (§4.3.15)                       | Entry 50 (§4.3.15)            |
| Bundle (§4.2.3)                                 | Entry 15 (§4.2.3)                 |
| Collection (§4.2.1)                         | Entry 13 (§4.2.1)             |
| Communication (§4.3.12)                   | Entry 47 (§4.3.12)          |
| Delegation (§4.3.18)                         | Entry 53 (§4.3.18)             |
| Derivation (§4.3.6)                         | Entry 41 (§4.3.6)             |
| EmptyCollection (§4.2.2)               | Entry 14 (§4.2.2)        |
| End (§4.3.5)                                       | Entry 40 (§4.3.5)                    |
| endedAtTime (§4.1.10)                       | Entry 10 (§4.1.10)            |
| Entity (§4.1.1)                                 | Entry 1 (§4.1.1)                  |
| entity (§4.3.37)                               | Entry 72 (§4.3.37)               |
| EntityInfluence (§4.3.2)               | Entry 37 (§4.3.2)        |
| generated (§4.2.23)                           | Entry 35 (§4.2.23)              |
| generatedAtTime (§4.2.10)               | Entry 22 (§4.2.10)        |
| Generation (§4.3.11)                         | Entry 46 (§4.3.11)             |
| hadActivity (§4.3.43)                       | Entry 78 (§4.3.43)            |
| hadGeneration (§4.3.39)                   | Entry 74 (§4.3.39)          |
| hadMember (§4.2.17)                           | Entry 29 (§4.2.17)              |
| hadPlan (§4.3.42)                               | Entry 77 (§4.3.42)                |
| hadPrimarySource (§4.2.11)             | Entry 23 (§4.2.11)       |
| hadRole (§4.3.45)                               | Entry 80 (§4.3.45)                |
| hadUsage (§4.3.38)                             | Entry 73 (§4.3.38)               |
| Influence (§4.3.1)                           | Entry 36 (§4.3.1)              |
| influenced (§4.2.21)                         | Entry 33 (§4.2.21)             |
| influencer (§4.3.36)                         | Entry 71 (§4.3.36)             |
| InstantaneousEvent (§4.3.19)         | Entry 54 (§4.3.19)     |
| invalidated (§4.2.20)                       | Entry 32 (§4.2.20)            |
| invalidatedAtTime (§4.2.15)           | Entry 27 (§4.2.15)      |
| Invalidation (§4.3.13)                     | Entry 48 (§4.3.13)           |
| Location (§4.2.7)                             | Entry 19 (§4.2.7)               |
| Organization (§4.2.6)                     | Entry 18 (§4.2.6)           |
| Person (§4.2.4)                                 | Entry 16 (§4.2.4)                 |
| Plan (§4.3.17)                                     | Entry 52 (§4.3.17)                   |
| PrimarySource (§4.3.7)                   | Entry 42 (§4.3.7)          |
| qualifiedAssociation (§4.3.33)     | Entry 68 (§4.3.33)   |
| qualifiedAttribution (§4.3.28)     | Entry 63 (§4.3.28)   |
| qualifiedCommunication (§4.3.32) | Entry 67 (§4.3.32) |
| qualifiedDelegation (§4.3.35)       | Entry 70 (§4.3.35)    |
| qualifiedDerivation (§4.3.24)       | Entry 59 (§4.3.24)    |
| qualifiedEnd (§4.3.34)                     | Entry 69 (§4.3.34)           |
| qualifiedGeneration (§4.3.23)       | Entry 58 (§4.3.23)    |
| qualifiedInfluence (§4.3.22)         | Entry 57 (§4.3.22)     |
| qualifiedInvalidation (§4.3.29)   | Entry 64 (§4.3.29)  |
| qualifiedPrimarySource (§4.3.25) | Entry 60 (§4.3.25) |
| qualifiedQuotation (§4.3.26)         | Entry 61 (§4.3.26)     |
| qualifiedRevision (§4.3.27)           | Entry 62 (§4.3.27)      |
| qualifiedStart (§4.3.30)                 | Entry 65 (§4.3.30)         |
| qualifiedUsage (§4.3.31)                 | Entry 66 (§4.3.31)         |
| Quotation (§4.3.8)                           | Entry 43 (§4.3.8)              |
| Revision (§4.3.9)                             | Entry 44 (§4.3.9)               |
| Role (§4.3.20)                                     | Entry 55 (§4.3.20)                   |
| SoftwareAgent (§4.2.5)                   | Entry 17 (§4.2.5)          |
| specializationOf (§4.2.9)             | Entry 21 (§4.2.9)       |
| Start (§4.3.4)                                   | Entry 39 (§4.3.4)                  |
| startedAtTime (§4.1.7)                   | Entry 7 (§4.1.7)           |
| Usage (§4.3.3)                                   | Entry 38 (§4.3.3)                  |
| used (§4.1.8)                                     | Entry 8 (§4.1.8)                    |
| value (§4.2.12)                                   | Entry 24 (§4.2.12)                  |
| wasAssociatedWith (§4.1.11)           | Entry 11 (§4.1.11)      |
| wasAttributedTo (§4.1.6)               | Entry 6 (§4.1.6)         |
| wasDerivedFrom (§4.1.5)                 | Entry 5 (§4.1.5)          |
| wasEndedBy (§4.2.19)                         | Entry 31 (§4.2.19)             |
| wasGeneratedBy (§4.1.4)                 | Entry 4 (§4.1.4)          |
| wasInfluencedBy (§4.3.21)               | Entry 56 (§4.3.21)        |
| wasInformedBy (§4.1.9)                   | Entry 9 (§4.1.9)           |
| wasInvalidatedBy (§4.2.16)             | Entry 28 (§4.2.16)       |
| wasQuotedFrom (§4.2.13)                   | Entry 25 (§4.2.13)          |
| wasRevisionOf (§4.2.14)                   | Entry 26 (§4.2.14)          |
| wasStartedBy (§4.2.18)                     | Entry 30 (§4.2.18)           |

## A. PROV-O OWL Profile

*This section is non-normative.*

To encourage widespread adoption, PROV-O's design is intentionally minimal and lightweight.
Because the OWL 2 RL profile is aimed at RDF applications that require scalable reasoning without sacrificing too much expressive power [OWL2-PRIMER],
it served as a baseline for all axioms included in PROV-O. The PROV-O axioms that do not suit the OWL 2 RL profile are listed in Table 5.

All five use an anonymous *class union* for the domain or range of a property, while OWL 2 RL requires the classes to be explicitly named.
Although introducing "placeholder" classes would have suited the
OWL 2 RL profile, these additional "abstract" classes would have been irrelevant
to the modeling of provenance information, increased the size of PROV-O unnecessarily, and exposed a potential to confuse users.
All five axioms listed in the following table *use a non-superclass expression in a position that requires a superclass expression* and do not conform to the OWL 2 RL Profile.

*Table 5: All OWL Axioms in PROV\-O that do not conform to the OWL\-RL profile.*

| Non OWL-RL PROV-O Axiom                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| prov:atLocation (§4.2.22) rdfs:domain [ owl:unionOf (prov:Activity prov:Agent prov:Entity prov:InstantaneousEvent) ] |
| prov:wasInfluencedBy (§4.3.21) rdfs:domain [ owl:unionOf (prov:Activity prov:Agent prov:Entity) ]               |
| prov:wasInfluencedBy (§4.3.21) rdfs:range [ owl:unionOf (prov:Activity prov:Agent prov:Entity) ]                |
| prov:hadActivity (§4.3.43) rdfs:domain [ owl:unionOf (prov:Delegation prov:Derivation prov:Start prov:End) ]        |
| prov:hadRole (§4.3.45) rdfs:domain [ owl:unionOf (prov:Association prov:InstantaneousEvent) ]                           |

To provide guidance for OWL 2 RL environments that ignore the union domain axioms, some
property domains or ranges have also been defined with the closest
common superclass for the classes in the union, as shown in the following table.

*Table 6: Intersecting OWL2 RL compatible domains/ranges*

| Property                                                              | Direction                | Domain/range                                              |
| --------------------------------------------------------------------- | ------------------------ | --------------------------------------------------------- |
| prov:atLocation (§4.2.22)           | rdfs:domain              | (implied: owl:Thing)                                      |
| prov:wasInfluencedBy (§4.3.21) | rdfs:domain / rdfs:range | (implied: owl:Thing)                                      |
| prov:hadActivity (§4.3.43)         | rdfs:domain              | prov:Influence (§4.3.1) |
| prov:hadRole (§4.3.45)                 | rdfs:domain              | prov:Influence (§4.3.1) |

Multiple RDFS domains and ranges [RDF-SCHEMA] for a property are [interpreted as an intersection](https://www.w3.org/TR/2004/REC-rdf-schema-20040210/#ch_range),
and thus the above do not provide any additional
information in an OWL 2 DL or OWL 2 Full profile, which also understands
the unions. The more general domain should not be
interpreted as saying, e.g.,
"prov:hadActivity can be used with any prov:Influence",
but as
"Anything using prov:hadActivity is (at least) a prov:Influence".

## B. Names of inverse properties

To maximize interoperability, PROV-O intentionally avoids defining too many properties' inverses.
In fact, it only defines two (prov:generated (§4.2.23) and prov:invalidated (§4.2.20)).
When all inverses are defined for all properties, modelers may choose from two logically equivalent properties when making each assertion.
Although the two options may be logically equivalent, developers consuming the assertions may need to exert extra effort to handle both
(e.g., by either adding an OWL reasoner or writing code and queries to handle both cases).
This extra effort can be reduced by preferring one inverse over another.
> **Example:**
>
> For example, the first PROV-O statement (below) could just as easily be asserted as the second statement.
> But if a client queries using prov:wasDerivedFrom (§4.1.5) when :hadDerivation was used in the assertion, no results will be returned unless OWL reasoning is applied (or the size of the query is doubled).
>
> ```
> <http://www.w3.org/TR/prov-o/>  prov:wasDerivedFrom <http://www.w3.org/TR/prov-dm/> .
>
>    # These two statements are equivalent if prov:wasDerivedFrom is an inverse of :hadDerivation.
>    # But extra effort is required to handle both cases (if one is not already using OWL reasoning).
>    # We cannot assume that everybody is using OWL reasoning.
>    # We do not want people to write more code and query than necessary.
>
> <http://www.w3.org/TR/prov-dm/>     :hadDerivation  <http://www.w3.org/TR/prov-o/>  .
> ```

So, PROV-O avoids this situation by encouraging modelers to use one property instead of its inverse; the preferred property to use is the one defined in the PROV-O ontology. Those asserting and querying for the preferred property avoid the need for OWL reasoning, additional code, and larger queries while maintaining the same level of interoperability.

However, the **absence** of defined inverses can lead to a **different** risk to interoperability.
Because modelers are free to create their own properties to suit their needs,
they may be motivated to assert the inverse of any PROV-O property defined herein.
> **Example:**
>
> For example, since PROV-O does not define the inverse of prov:wasDerivedFrom (§4.1.5),
> and if three developers would rather model their assertions in the opposite direction, the following set of assertions might be found in the future web of provenance.
> These assertions are not in an interoperable form without the use of an OWL reasoner, additional code, or larger queries.
>
> ```
> # If PROV-O's properties' inverses are not defined, modelers may be motivated to introduce their own inverse property name.
> # The following three statements are equivalent if their predicates are all inverses of prov:wasDerivedFrom.
>
> <http://www.w3.org/TR/prov-dm/>    my:hadDerivation  <http://www.w3.org/TR/prov-o/>  .
> <http://www.w3.org/TR/prov-dm/>  your:ledTo          <http://www.w3.org/TR/prov-o/>  .
> <http://www.w3.org/TR/prov-dm/> their:derivedTo      <http://www.w3.org/TR/prov-o/>  .
> ```

To balance these two interoperability risks, this document reserves the names of the PROV-O inverses.
The name of a property's inverse is determined by appending the value of its http://www.w3.org/ns/prov#inverse annotation to the PROV namespace (http://www.w3.org/ns/prov#).
Modelers wishing to use inverses of the properties defined by PROV-O *should* use those reserved by this document.
> **Example:**
>
> For example, the same three modelers above that defined `my:hadDerivation`, `your:ledTo`, and `their:derivedTo` should instead look for the http://www.w3.org/ns/prov#inverse annotation on prov:wasDerivedFrom (§4.1.5) to determine that they should use the property http://www.w3.org/ns/prov#hadDerivation.
>
> ```
> @prefix prov: <http://www.w3.org/ns/prov#> .
>
> # Each PROV-O property is annotated with the local name of its inverse.
>
> prov:wasDerivedFrom
>    a owl:ObjectProperty;
>    rdfs:isDefinedBy <http://www.w3.org/ns/prov#>;
>    prov:inverse     "hadDerivation";
>    rdfs:domain  prov:Entity;
>    rdfs:range   prov:Entity;
> .
>
> # Instead of defining their own, modelers should use the
> # recommended inverse local name within the PROV namespace:
>
> <http://www.w3.org/TR/prov-dm/> prov:hadDerivation <http://www.w3.org/TR/prov-o/>  .
>
> # Following this recommendation avoids a proliferation of inverse definitions,
> # while encouraging the use of one inverse over another.
> # This increases interoperability.
> ```

The following table lists the recommended inverse names that should be used if a modeler does not want to use the recommended PROV-O property.
For convenience, [this file](https://www.w3.org/ns/prov-o-inverses) lists the resulting inverse properties.

*Table 5: Names of inverses*

| Domain                                                                                                                  | PROV-O Property                                                                                                                        | Recommended inverse name      | Range                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------- |
| prov:Agent (§4.1.3)                                     | prov:actedOnBehalfOf (§4.1.12)                      | prov:hadDelegate              | prov:Agent (§4.1.3)                         |
| prov:ActivityInfluence (§4.3.10) | prov:activity (§4.3.40)                                         | prov:activityOfInfluence      | prov:Activity (§4.1.2)                |
| prov:AgentInfluence (§4.3.14)          | prov:agent (§4.3.41)                                                  | prov:agentOfInfluence         | prov:Agent (§4.1.3)                         |
| prov:Entity (§4.1.1)                                  | prov:alternateOf (§4.2.8)                                  | prov:alternateOf              | prov:Entity (§4.1.1)                      |
| union                                                                                                                   | prov:atLocation (§4.2.22)                                     | prov:locationOf               | prov:Location (§4.2.7)                |
| prov:EntityInfluence (§4.3.2)       | prov:entity (§4.3.37)                                               | prov:entityOfInfluence        | prov:Entity (§4.1.1)                      |
| prov:Activity (§4.1.2)                            | prov:generated (§4.2.23)                                        | prov:wasGeneratedBy           | prov:Entity (§4.1.1)                      |
| union                                                                                                                   | prov:hadActivity (§4.3.43)                                  | prov:wasActivityOfInfluence   | prov:Activity (§4.1.2)                |
| prov:Derivation (§4.3.6)                      | prov:hadGeneration (§4.3.39)                            | prov:generatedAsDerivation    | prov:Generation (§4.3.11)          |
| prov:Collection (§4.2.1)                      | prov:hadMember (§4.2.17)                                        | prov:wasMemberOf              | prov:Entity (§4.1.1)                      |
| prov:Association (§4.3.16)                   | prov:hadPlan (§4.3.42)                                              | prov:wasPlanOf                | prov:Plan (§4.3.17)                            |
| prov:Entity (§4.1.1)                                  | prov:hadPrimarySource (§4.2.11)                   | prov:wasPrimarySourceOf       | prov:Entity (§4.1.1)                      |
| union                                                                                                                   | prov:hadRole (§4.3.45)                                              | prov:wasRoleIn                | prov:Role (§4.3.20)                            |
| prov:Derivation (§4.3.6)                      | prov:hadUsage (§4.3.38)                                           | prov:wasUsedInDerivation      | prov:Usage (§4.3.3)                         |
|                                                                                                                         | prov:influenced (§4.2.21)                                     | prov:wasInfluencedBy          |                                                                                                             |
| prov:Influence (§4.3.1)                         | prov:influencer (§4.3.36)                                     | prov:hadInfluence             | union                                                                                                       |
| prov:Activity (§4.1.2)                            | prov:invalidated (§4.2.20)                                  | prov:wasInvalidatedBy         | prov:Entity (§4.1.1)                      |
| prov:Activity (§4.1.2)                            | prov:qualifiedAssociation (§4.3.33)       | prov:qualifiedAssociationOf   | prov:Association (§4.3.16)       |
| prov:Entity (§4.1.1)                                  | prov:qualifiedAttribution (§4.3.28)       | prov:qualifiedAttributionOf   | prov:Attribution (§4.3.15)       |
| prov:Activity (§4.1.2)                            | prov:qualifiedCommunication (§4.3.32) | prov:qualifiedCommunicationOf | prov:Communication (§4.3.12) |
| prov:Agent (§4.1.3)                                     | prov:qualifiedDelegation (§4.3.35)          | prov:qualifiedDelegationOf    | prov:Delegation (§4.3.18)          |
| prov:Entity (§4.1.1)                                  | prov:qualifiedDerivation (§4.3.24)          | prov:qualifiedDerivationOf    | prov:Derivation (§4.3.6)          |
| prov:Activity (§4.1.2)                            | prov:qualifiedEnd (§4.3.34)                               | prov:qualifiedEndOf           | prov:End (§4.3.5)                               |
| prov:Entity (§4.1.1)                                  | prov:qualifiedGeneration (§4.3.23)          | prov:qualifiedGenerationOf    | prov:Generation (§4.3.11)          |
| union                                                                                                                   | prov:qualifiedInfluence (§4.3.22)             | prov:qualifiedInfluenceOf     | prov:Influence (§4.3.1)             |
| prov:Entity (§4.1.1)                                  | prov:qualifiedInvalidation (§4.3.29)    | prov:qualifiedInvalidationOf  | prov:Invalidation (§4.3.13)    |
| prov:Entity (§4.1.1)                                  | prov:qualifiedPrimarySource (§4.3.25) | prov:qualifiedSourceOf        | prov:PrimarySource (§4.3.7) |
| prov:Entity (§4.1.1)                                  | prov:qualifiedQuotation (§4.3.26)             | prov:qualifiedQuotationOf     | prov:Quotation (§4.3.8)             |
| prov:Entity (§4.1.1)                                  | prov:qualifiedRevision (§4.3.27)                | prov:revisedEntity            | prov:Revision (§4.3.9)                |
| prov:Activity (§4.1.2)                            | prov:qualifiedStart (§4.3.30)                         | prov:qualifiedStartOf         | prov:Start (§4.3.4)                         |
| prov:Activity (§4.1.2)                            | prov:qualifiedUsage (§4.3.31)                         | prov:qualifiedUsingActivity   | prov:Usage (§4.3.3)                         |
| prov:Entity (§4.1.1)                                  | prov:specializationOf (§4.2.9)                   | prov:generalizationOf         | prov:Entity (§4.1.1)                      |
| prov:Activity (§4.1.2)                            | prov:used (§4.1.8)                                                       | prov:wasUsedBy                | prov:Entity (§4.1.1)                      |
| prov:Activity (§4.1.2)                            | prov:wasAssociatedWith (§4.1.11)                | prov:wasAssociateFor          | prov:Agent (§4.1.3)                         |
| prov:Entity (§4.1.1)                                  | prov:wasAttributedTo (§4.1.6)                      | prov:contributed              | prov:Agent (§4.1.3)                         |
| prov:Entity (§4.1.1)                                  | prov:wasDerivedFrom (§4.1.5)                         | prov:hadDerivation            | prov:Entity (§4.1.1)                      |
| prov:Activity (§4.1.2)                            | prov:wasEndedBy (§4.2.19)                                     | prov:ended                    | prov:Entity (§4.1.1)                      |
| prov:Entity (§4.1.1)                                  | prov:wasGeneratedBy (§4.1.4)                         | prov:generated                | prov:Activity (§4.1.2)                |
| union                                                                                                                   | prov:wasInfluencedBy (§4.3.21)                      | prov:influenced               | union                                                                                                       |
| prov:Activity (§4.1.2)                            | prov:wasInformedBy (§4.1.9)                            | prov:informed                 | prov:Activity (§4.1.2)                |
| prov:Entity (§4.1.1)                                  | prov:wasInvalidatedBy (§4.2.16)                   | prov:invalidated              | prov:Activity (§4.1.2)                |
| prov:Entity (§4.1.1)                                  | prov:wasQuotedFrom (§4.2.13)                            | prov:quotedAs                 | prov:Entity (§4.1.1)                      |
| prov:Entity (§4.1.1)                                  | prov:wasRevisionOf (§4.2.14)                            | prov:hadRevision              | prov:Entity (§4.1.1)                      |
| prov:Activity (§4.1.2)                            | prov:wasStartedBy (§4.2.18)                               | prov:started                  | prov:Entity (§4.1.1)                      |

## C. Changes since WD-prov-o-20120724

*This section is non-normative.*

- Restated prov:hadRole (§4.3.45)'s domain to 'Association or InstantaneousEvent'
  instead of the original that enumerated the subclasses of InstantaneousEvent
  ('Association or End or Generation or Invalidation or Start or Usage').
- Renamed prov:Source to prov:PrimarySource (§4.3.7) and prov:qualifiedSource to prov:qualifiedPrimarySource (§4.3.25).
- Examples have been rewritten to avoid usage of TriG named
  graph syntax except for when showing bundles in
  prov:asInBundle and prov:mentionOf (since removed to a separate Note). A citation to TriG was added.
- Some examples have been elaborated to use resource names
  like `:illustration_usage` rather than `:usage_1`.
- Fixed naming mismatch by changing prov:hadOriginalSource to prov:hadPrimarySource (§4.2.11).
- Rephrased definitions for prov:EntityInfluence (§4.3.2), prov:ActivityInfluence (§4.3.10), and prov:AgentInfluence (§4.3.14) to align with the definition of their superclass prov:Influence (§4.3.1).
- Updated definitions for prov:Start (§4.3.4) and prov:End (§4.3.5) from PROV-DM.
- The property chain for prov:wasInformedBy (§4.1.9) was fixed from
  "qualifiedCommunication o entity subproperty of wasInformedBy"
  to "prov:qualifiedCommunication (§4.3.32) o prov:activity (§4.3.40) subproperty of wasInformedBy"
- Removed prov:mentionOf and prov:asInBundle, which have been relocated to its own Note.
- Added comments encouraging the use of the more specific forms of prov:Influence (§4.3.1).
- Added uniform references to other "dated" PROV documents.
- Added prefix namespace table.
- Added §1.1 Compliance with this Document section.
- Corrected Turtle syntax for RL violations in §A PROV-O OWL Profile section. They were missing owl:unionOf.
- Updated attributions for the tools used to produce this document in §F Acknowledgements section.
- Reworked the §3.2 Expanded Terms narrative and examples to better highlight each term.

## D. Changes since CR-prov-o-20121211

*This section is non-normative.*

- Updated exemplar in cross reference entry prov:hadGeneration (§4.3.39) to include prov:activity (§4.3.40) property.
- Reordered class and predicate terms from alphabetical to a more natural narrative-based order.
- Added §4.4 Term Index to aid reading this document in printed form.
- Fixed typo 'iteself' to 'itself'.
- Removed inaccurate property characteristics (AsymmetricProperty, IrreflexiveProperty)
  in third example of Appendix B (§B).
- Added note to §3.1 Starting Point Terms stating that
  rdf:type and rdfs:label are used to express PROV-DM's prov:type and prov:label.
- Updated prov:value's out-of-date definition to conform to PROV-DM's (i.e., "Provides a value that is a direct representation of an entity.".
- Updated prov:wasDerivedFrom's out-of-date definition to conform to PROV-DM's
  (i.e., "A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.".
- Added xsd:dateType datatypes to exemplar in Invalidation and invalidatedAtTime.
- Fixed some incorrect wasAttributedTo/wasAssociatedWith in the cross reference exemplars.
- Changed the status of this document section: added new documents to the PROV Family of Document, and removed the how to read section, referring instead to PROV-OVERVIEW.
- Changed all URLs to PROV documents.

## E. Changes since PR-prov-o-20130312

*This section is non-normative.*

- Fixed typo in [alternateOf](https://www.w3.org/TR/2013/PR-prov-o-20130312/#alternateOf) example: `:london_forecast_043` became `:london_forecast_0413`
- Changed capitalization in definitions for [Organization](https://www.w3.org/TR/2013/PR-prov-o-20130312/#SoftwareAgent) (new (§4.2.6)) and [Person](https://www.w3.org/TR/2013/PR-prov-o-20130312/#SoftwareAgent) (new (§4.2.4)).

## F. Acknowledgements

*This section is non-normative.*

This document has been produced by the PROV Working Group, and its contents reflect extensive discussion within the Working Group as a whole. The editors extend special thanks to Sandro Hawke (W3C/MIT) and Ivan Herman (W3C/ERCIM), W3C contacts for the PROV Working Group.

The editors acknowledge valuable contributions from the following:
Tom Baker,
David Booth,
Robert Freimuth,
Satrajit Ghosh,
Ralph Hodgson,
Renato Iannella,
Jacek Kopecky,
James Leigh,
Jacco van Ossenbruggen,
Alan Ruttenberg,
Reza Samavi, and
Antoine Zimmermann.

Members of the PROV Working Group at the time of publication of this document were:

Ilkay Altintas (Invited expert),
Reza B'Far (Oracle Corporation),
Khalid Belhajjame (University of Manchester),
James Cheney (University of Edinburgh, School of Informatics),
Sam Coppens (iMinds - Ghent University),
David Corsar (University of Aberdeen, Computing Science),
Stephen Cresswell (The National Archives),
Tom De Nies (iMinds - Ghent University),
Helena Deus (DERI Galway at the National University of Ireland, Galway, Ireland),
Simon Dobson (Invited expert),
Martin Doerr (Foundation for Research and Technology - Hellas(FORTH)),
Kai Eckert (Invited expert),
Jean-Pierre EVAIN (European Broadcasting Union, EBU-UER),
James Frew (Invited expert),
Irini Fundulaki (Foundation for Research and Technology - Hellas(FORTH)),
Daniel Garijo (Ontology Engineering Group, Universidad Politécnica de Madrid, Spain),
Yolanda Gil (Invited expert),
Ryan Golden (Oracle Corporation),
Paul Groth (Vrije Universiteit),
Olaf Hartig (Invited expert),
David Hau (National Cancer Institute, NCI),
Sandro Hawke (W3C/MIT),
Jörn Hees (German Research Center for Artificial Intelligence (DFKI) Gmbh),
Ivan Herman, (W3C/ERCIM),
Ralph Hodgson (TopQuadrant),
Hook Hua (Invited expert),
Trung Dong Huynh (University of Southampton),
Graham Klyne (University of Oxford),
Michael Lang (Revelytix, Inc.),
Timothy Lebo (Rensselaer Polytechnic Institute),
James McCusker (Rensselaer Polytechnic Institute),
Deborah McGuinness (Rensselaer Polytechnic Institute),
Simon Miles (Invited expert),
Paolo Missier (School of Computing Science, Newcastle university),
Luc Moreau (University of Southampton),
James Myers (Rensselaer Polytechnic Institute),
Vinh Nguyen (Wright State University),
Edoardo Pignotti (University of Aberdeen, Computing Science),
Paulo da Silva Pinheiro (Rensselaer Polytechnic Institute),
Carl Reed (Open Geospatial Consortium),
Adam Retter (Invited Expert),
Christine Runnegar (Invited expert),
Satya Sahoo (Invited expert),
David Schaengold (Revelytix, Inc.),
Daniel Schutzer (FSTC, Financial Services Technology Consortium),
Yogesh Simmhan (Invited expert),
Stian Soiland-Reyes (University of Manchester),
Eric Stephan (Pacific Northwest National Laboratory),
Linda Stewart (The National Archives),
Ed Summers (Library of Congress),
Maria Theodoridou (Foundation for Research and Technology - Hellas(FORTH)),
Ted Thibodeau (OpenLink Software Inc.),
Curt Tilmes (National Aeronautics and Space Administration),
Craig Trim (IBM Corporation),
Stephan Zednik (Rensselaer Polytechnic Institute),
Jun Zhao (University of Oxford),
Yuting Zhao (University of Aberdeen, Computing Science).

The editors also thank the developers of the tools that helped create the PROV-O ontology and portions of this document. Without these great tools, developing PROV-O would have been much less of a pleasure.

- Stanford's [Protege](http://protege.stanford.edu) for editing the ontology.
- Dave Beckett's [rapper](http://librdf.org/raptor/) for the many serialization checks of so many examples.
- Cosmin Basca's [SuRF](http://packages.python.org/SuRF/) for easing the construction of this page's cross reference section.
- The creators, contributors, and maintainers of [rdflib](https://github.com/RDFLib) for easing the construction of this page's cross reference section.
- Alvaro Graves' [LODSpeaKr](http://alangrafu.github.io/lodspeakr/) for constructing portions of this page with SPARQL queries of PROV-O.
- Silvio Peroni's [LODE](http://lode.sourceforge.net) for the CSS styling of this page's cross reference section.
- Robin Berjon's [respec](http://dev.w3.org/2009/dap/ReSpec.js/documentation.html) for handling the W3C styling.

## G. References

### G.1 Normative references

[IRI]

M. Duerst, M. Suignard. [Internationalized Resource Identifiers (IRI).](http://www.ietf.org/rfc/rfc3987.txt) January 2005. Internet RFC 3987. URL: [http://www.ietf.org/rfc/rfc3987.txt](http://www.ietf.org/rfc/rfc3986.txt)

[OWL2-OVERVIEW]

W3C OWL Working Group. [OWL 2 Web Ontology Language: Overview.](https://www.w3.org/TR/2009/REC-owl2-overview-20091027/) 27 October 2009. W3C Recommendation. URL: [http://www.w3.org/TR/2009/REC-owl2-overview-20091027/](https://www.w3.org/TR/2009/REC-owl2-overview-20091027/)

[PROV-CONSTRAINTS]

James Cheney; Paolo Missier; Luc Moreau; eds. [Constraints of the PROV Data Model](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-constraints-20130430/](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/)

[PROV-DM]

Luc Moreau; Paolo Missier; eds. [PROV-DM: The PROV Data Model](https://www.w3.org/TR/2013/REC-prov-dm-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-dm-20130430/](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)

[PROV-N]

Luc Moreau; Paolo Missier; eds. [PROV-N: The Provenance Notation](https://www.w3.org/TR/2013/REC-prov-n-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-n-20130430/](https://www.w3.org/TR/2013/REC-prov-n-20130430/)

[RDF-CONCEPTS]

Graham Klyne; Jeremy J. Carroll. [Resource Description Framework (RDF): Concepts and Abstract Syntax.](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/) 10 February 2004. W3C Recommendation. URL: [http://www.w3.org/TR/2004/REC-rdf-concepts-20040210](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/)

[RFC2119]

S. Bradner. [Key words for use in RFCs to Indicate Requirement Levels.](http://www.ietf.org/rfc/rfc2119.txt) March 1997. Internet RFC 2119. URL: <http://www.ietf.org/rfc/rfc2119.txt>

[XMLSCHEMA11-2]

Henry S. Thompson; et al. [W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes.](https://www.w3.org/TR/2012/REC-xmlschema11-2-20120405/) 5 April 2012. W3C Recommendation URL: [http://www.w3.org/TR/2012/REC-xmlschema11-2-20120405/](https://www.w3.org/TR/2012/REC-xmlschema11-2-20120405/)

### G.2 Informative references

[LD-Patterns-QR]

Leigh Dodds; Ian Davis. [Qualified Relation](http://patterns.dataincubator.org/book/qualified-relation.html). modified 31 May 2012, accessed 01 June 2012 URL: <http://patterns.dataincubator.org/book/qualified-relation.html>

[OWL2-PRIMER]

Pascal Hitzler; Markus Krötzsch; Bijan Parsia; Peter F. Patel-Schneider; Sebastian Rudolph. [OWL 2 Web Ontology Language:Primer.](https://www.w3.org/TR/2009/REC-owl2-primer-20091027/) 27 October 2009. W3C Recommendation. URL: [http://www.w3.org/TR/2009/REC-owl2-primer-20091027/](https://www.w3.org/TR/2009/REC-owl2-primer-20091027/)

[PROV-AQ]

Graham Klyne; Paul Groth; eds. [Provenance Access and Query](https://www.w3.org/TR/2013/NOTE-prov-aq-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-aq-20130430/](https://www.w3.org/TR/2013/NOTE-prov-aq-20130430/)

[PROV-DC]

Daniel Garijo; Kai Eckert; eds. [Dublin Core to PROV Mapping](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/). 30 April 2013, W3C Note. URL : [http://www.w3.org/TR/2013/NOTE-prov-dc-20130430/](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/)

[PROV-DICTIONARY]

Tom De Nies; Sam Coppens; eds. [PROV-Dictionary: Modeling Provenance for Dictionary Data Structures](https://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/](https://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/)

[PROV-LINKS]

Luc Moreau; Timothy Lebo; eds. [Linking Across Provenance Bundles](https://www.w3.org/TR/2013/NOTE-prov-links-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-links-20130430/](https://www.w3.org/TR/2013/NOTE-prov-links-20130430/)

[PROV-OVERVIEW]

Paul Groth; Luc Moreau; eds. [PROV-OVERVIEW: An Overview of the PROV Family of Documents](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-overview-20130430/](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/)

[PROV-PRIMER]

Yolanda Gil; Simon Miles; eds. [PROV Model Primer](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-primer-20130430/](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/)

[PROV-SEM]

James Cheney; ed. [Semantics of the PROV Data Model](https://www.w3.org/TR/2013/NOTE-prov-sem-20130430). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-sem-20130430](https://www.w3.org/TR/2013/NOTE-prov-sem-20130430).

[PROV-XML]

Hook Hua; Curt Tilmes; Stephan Zednik; eds. [PROV-XML: The PROV XML Schema](https://www.w3.org/TR/2013/NOTE-prov-xml-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-xml-20130430/](https://www.w3.org/TR/2013/NOTE-prov-xml-20130430/)

[RDF-SCHEMA]

Dan Brickley; Ramanathan V. Guha. [RDF Vocabulary Description Language 1.0: RDF Schema.](https://www.w3.org/TR/2004/REC-rdf-schema-20040210/) 10 February 2004. W3C Recommendation. URL: [http://www.w3.org/TR/2004/REC-rdf-schema-20040210](https://www.w3.org/TR/2004/REC-rdf-schema-20040210/)

[TRIG]

Chris Bizer; Richard Cyganiak. [The TriG Syntax](http://wifo5-03.informatik.uni-mannheim.de/bizer/trig/). modified 30 July 2007, accessed 05 November 2012 URL: <http://wifo5-03.informatik.uni-mannheim.de/bizer/trig/>
