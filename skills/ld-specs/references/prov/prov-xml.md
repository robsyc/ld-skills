---
title: "PROV-XML: The PROV XML Schema"
source: https://www.w3.org/TR/prov-xml/
family: prov
spec_date: 2013-04-30
fetched: 2026-11-02
---

# PROV-XML: The PROV XML Schema

> XML serialization of PROV.

## Contents

- Abstract
- 1 Introduction
  - 1.1 PROV Namespace
  - 1.2 Conventions
- 2 XML Schema Design
  - 2.1 Schema Modularization
  - 2.2 Salami Slice Design Pattern
  - 2.3 Elements vs. Attributes
  - 2.4 Type Conventions
    - 2.4.1 PROV Type Attribute
    - 2.4.2 Extension Types
    - 2.4.3 XSI Type
  - 2.5 Identifier Conventions
  - 2.6 Naming Conventions
- 3 PROV XML Schema
  - 3.1 Component 1: Entities and Activities
    - 3.1.1 Entity
    - 3.1.2 Activity
    - 3.1.3 Generation
    - 3.1.4 Usage
    - 3.1.5 Communication
    - 3.1.6 Start
    - 3.1.7 End
    - 3.1.8 Invalidation
  - 3.2 Component 2: Derivations
    - 3.2.1 Derivation
    - 3.2.2 Revision
    - 3.2.3 Quotation
    - 3.2.4 Primary Source
  - 3.3 Component 3: Agents, Responsibility, and Influence
    - 3.3.1 Agent
    - 3.3.2 Attribution
    - 3.3.3 Association
    - 3.3.4 Delegation
    - 3.3.5 Influence
  - 3.4 Component 4: Bundles
    - 3.4.1 Bundle
    - 3.4.2 Bundle Constructor
  - 3.5 Component 5: Alternate Entities
    - 3.5.1 Specialization
    - 3.5.2 Alternate
  - 3.6 Component 6: Collections
    - 3.6.1 Collection
    - 3.6.2 Membership
  - 3.7 Further Elements of PROV
    - 3.7.1 Identifier
    - 3.7.2 Reference
    - 3.7.3 Attributes
    - 3.7.4 Value
  - 3.8 Structural Elements of PROV-XML
    - 3.8.1 Document
    - 3.8.2 Other
- 4 Media Type
- A XML Schema
  - A.1 Main Schema
  - A.2 Core Schema
  - A.3 Extension Schemas
- B Change Log
  - B.1 Change Log Since WD Working Draft 12 March 2013
  - B.2 Change Log Since First Public Working Draft
- D References
  - D.1 Informative references

---

## Abstract

Provenance is information about entities, activities, and people involved in producing a piece of data or thing, which can be used to form assessments about its quality, reliability or trustworthiness. PROV-DM is the conceptual data model that forms a basis for the W3C provenance (PROV) family of specifications. It defines a concepts for expressing provenance information enabling interchange. This document introduces an XML schema for the PROV data model (PROV-DM), allowing instances of the PROV data model to be serialized in XML.

The [PROV Document Overview](https://www.w3.org/TR/2013/WD-prov-overview-20130312/) describes the overall state of PROV, and should be read before other PROV documents.

## 1. Introduction

For the purpose of this specification, *provenance* ◊ is defined as a record that describes the people, institutions, entities, and activities involved in producing, influencing, or delivering a piece of data or a thing. In particular, the provenance of information is crucial in deciding whether information is to be trusted, how it should be integrated with other diverse information sources, and how to give credit to its originators when reusing it. In an open and inclusive environment such as the Web, where users find information that is often contradictory or questionable, provenance can help those users to make trust judgements.

The PROV data model, PROV-DM, presents a generic data model for provenance that allows domain and application specific representations of provenance to be translated into such a data model and *interchanged* between systems. Thus, heterogeneous systems can export their native provenance into such a core data model, and applications that need to make sense of provenance can then import it,
process it, and reason over it.

The PROV data model distinguishes *core structures* from *extended structures*: core structures form the essence of provenance information, and are commonly found in various domain-specific vocabularies that deal with provenance or similar kinds of information [Mappings]. Extended structures enhance and refine core structures with more expressive capabilities to cater for more advanced uses of provenance. The PROV data model, comprising both core and extended structures, is a domain-agnostic model, but with clear extensibility points allowing further domain-specific and application-specific extensions to be defined.

The PROV data model has a modular design and is structured according to six components covering various facets of provenance:

- component 1: entities and activities, and the time at which they were created, used, or ended;
- component 2: derivations of entities from others;
- component 3: agents bearing responsibility for entities that were generated and activities that happened;
- component 4: bundles, a mechanism to support provenance of provenance;
- component 5: properties to link entities that refer to a same thing;
- component 6: collections forming a logical structure for its members.

*This specification's goal is to provide a succinct definition of the XML form of PROV-DM*, thus, we refer the reader to the PROV-DM to provide overall justification and context to the definitions presented here.

### 1.1 PROV Namespace

The PROV namespace is http://www.w3.org/ns/prov#.

All the concepts, reserved names and attributes introduced in this specification belong to the PROV namespace.

The prefix **prov** is used when referring to the PROV namespace.

### 1.2 Conventions

The key words "*MUST*", "*MUST NOT*", "*REQUIRED*", "*SHALL*", "*SHALL
NOT*", "*SHOULD*", "*SHOULD NOT*", "*RECOMMENDED*", "*MAY*", and
"*OPTIONAL*" in this document are to be interpreted as described in
[RFC2119].

## 2. XML Schema Design

Several general design principles and patterns were used in the construction of the PROV XML Schema.

### 2.1 Schema Modularization

The PROV-XML schema have been modularized so that xml-elements denoting terms defined in Working Group Notes are defined in separate extension schemas. All xml-elements denoting terms defined in the PROV-DM are defined in the **[http://www.w3.org/ns/prov-core.xsd](https://www.w3.org/ns/prov-core.xsd)** schema and xml-elements denoting terms defined in PROV Working Group Notes are defined in extension schemas (e.g. **[http://www.w3.org/ns/prov-dictionary.xsd](https://www.w3.org/ns/prov-dictionary.xsd)**, **[http://www.w3.org/ns/prov-links.xsd](https://www.w3.org/ns/prov-links.xsd)**). The default schema, **[http://www.w3.org/ns/prov.xsd](https://www.w3.org/ns/prov.xsd)**, imports **[http://www.w3.org/ns/prov-core.xsd](https://www.w3.org/ns/prov-core.xsd)** and all extension schemas. With this modeling all PROV xml-elements, even those denoting terms defined in Notes, are declared from the default schema. If the user wishes to leverage a schema that does not include xml-elements corresponding to terms from the PROV Notes the user can use schemaLocation to directly reference the core schema.

The default schema - **[http://www.w3.org/ns/prov.xsd](https://www.w3.org/ns/prov.xsd)**

```
<?xml version="1.0" encoding="utf-8"?>
<xs:schema targetNamespace="http://www.w3.org/ns/prov#"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:prov="http://www.w3.org/ns/prov#"
    elementFormDefault="qualified"
    attributeFormDefault="unqualified">

  <xs:include schemaLocation="prov-core.xsd"/>
  <xs:include schemaLocation="prov-dictionary.xsd"/>
  <xs:include schemaLocation="prov-links.xsd"/>

</xs:schema>
```

Extension schemas import the **[http://www.w3.org/ns/prov-core.xsd](https://www.w3.org/ns/prov-core.xsd)** schema and make use of a substitution group on the `prov:internalElement` to add extension-defined xml-elements to the list of valid PROV xml-elements in a bundle or document.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This schema design leveraging substitutionGroups on an abstract xml-element may result in sub-optimal binding classes being generated by Object-to-XML frameworks such as JAXB, JiBX, etc. See the PROV FAQ entry at [How should I generate JAXB classes from the PROV-XML schemas?](https://www.w3.org/2001/sw/wiki/PROV-FAQ#How_should_I_generate_JAXB_classes_from_the_PROV-XML_schemas.3F) for a JAXB-specific discussion on using OXM technologies with the PROV schemas.

The **[http://www.w3.org/ns/prov-links.xsd](https://www.w3.org/ns/prov-links.xsd)** extension schema.

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
    targetNamespace="http://www.w3.org/ns/prov#" xmlns:prov="http://www.w3.org/ns/prov#"
    elementFormDefault="qualified">

  <xs:include schemaLocation="prov-core.xsd" />

  <xs:complexType name="Mention">
    <xs:sequence>
      <xs:element name="specificEntity" type="prov:IDRef" />
      <xs:element name="generalEntity" type="prov:IDRef" />
      <xs:element name="bundle" type="prov:IDRef" />
    </xs:sequence>
  </xs:complexType>

  <xs:element name="mentionOf" type="prov:Mention" substitutionGroup="prov:internalElement" />

</xs:schema>
```

All schemas developed by the PROV WG utilize the PROV namespace.

### 2.2 *Salami Slice* Design Pattern

The general design pattern for the XML schema has been called *Salami Slice Design*. With this design, the individual components are each defined at the top level as separate xml-elements with distinct xml-types. This allows the xml-types to be easily reusable for domain specific extensions.

The `prov:document` xml-element has been defined to act as a convenient root xml-element for a PROV-XML document, but it's use as the root xml-element is not required. The schema follows the Salami Slice pattern to ensure PROV XML xml-elements can be integrated with mixed-schema XML documents which require a different document root.

### 2.3 Elements vs. Attributes

The PROV Notation (PROV-N) is a serialization of the PROV Data Model described in [PROV-N]. Examples in the [PROV-DM] document are encoded using PROV-N. Because of the heavy use of PROV-N syntax in [PROV-DM], the PROV-XML editors feel it is important to present a comparison of the PROV-N and PROV-XML syntaxes and justifications behind the select syntax decisions in PROV-XML.

The general PROV-N syntax patterns for expressing provenance
concepts are:

```
thing(id, elem1, elem2, ..., [attr1=val1, attr2=val2])
concept(id; elem1, elem2, ... [attr1=val2, attr2=val2])
```

In PROV-XML the PROV identifier is treated as an xml-attribute (`prov:id`), the prov-"elements" are treated as xml-elements, always with the same required order (position) as the PROV-DM/PROV-N description followed by optional prov-"attributes" which are also represented by xml-elements. As in PROV-N, the prov-"attributes" can be specified multiple times, but unlike PROV-N the prov-"attributes" have a fixed (alphabetical) order. The prov-"attribute" xml-elements are always defined at the end of the encompassing sequence after all prov-"element" xml-elements. XML Elements defined in namespaces other than the PROV namespace may be included after the prov-"attribute" xml-elements.

Wherever an "id" is referenced from a later concept, the id is
referenced as a prov:ref attribute of the element within the concept.

This transformation technique yields a general XML pattern:

```
<prov:thing prov:id="id">
  <prov:elem1 />
  <prov:elem2 />
  ...
  <ex:attr1>val1</ex:attr1>
  <ex:attr2>val2</ex:attr2>
  ...
</prov:thing>
```

Most of the concepts described below follow this general pattern.

### 2.4 Type Conventions

#### 2.4.1 PROV Type Attribute

The PROV-DM states type information is described using the prov:type prov-"attribute" and may occur multiple times for a given entity, activity, agent, or relation.

PROV-XML uses the xml-element `prov:type` to represent the prov:type prov-"attribute". This xml-element can be use to represent both PROV and non-PROV type information. The following examples shows type information encoded using the `prov:type` xml-element.
> **Example:**
>
> > **Example:**
> >
> > Example 1: type information using prov:type PROV attribute
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:tr="http://example.com/ns/tr#">
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111215">
>     <prov:type xsi:type="xsd:QName">prov:Plan</prov:type>
>     <prov:type xsi:type="xsd:QName">ex:Workflow</prov:type>
>   </prov:entity>
>
> </prov:document>
> ```

The `prov:type` xml-element can be used in conjunction with schema-defined PROV types (see examples 2-5).

#### 2.4.2 Extension Types

PROV-XML defines complexTypes to match the PROV defined type values (prov-type). These xml-types provide a more native XML representation of prov-"types". The following example is considered equivalent to the previous example because the xml-element `prov:plan` has `xs:type=prov:Plan`. All complexTypes representing a prov-"type" which is defined as a subclass of another prov-"type" are defined in PROV-XML as extensions of their parent prov-"type's" complexType. For example, `prov:Plan` is defined as an extension of the complexType `prov:Entity` and may be referenced by either `prov:plan` or `prov:entity` xml-elements.
> **Example:**
>
> > **Example:**
> >
> > Example 2: type information using schema defined types
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:tr="http://example.com/ns/tr#">
>
>   <prov:plan prov:id="tr:WD-prov-dm-20111215">
>     <prov:type xsi:type="xsd:QName">ex:Workflow</prov:type>
>   </prov:plan>
>
> </prov:document>
> ```

When an extension xml-type is used a prov-"type" may be inferred.

Explicit type declarations made using the `prov:type` xml-element may be easier for some encoding transformation tools (such as XSLT) to process, therefore use of the `prov:type` xml-element is highly encouraged even in cases where prov-"type" information is determinable from schema defined ComplexTypes.
> **Example:**
>
> > **Example:**
> >
> > Example 3: type information using schema defined types - type inferences
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:tr="http://example.com/ns/tr#">
>
>   <prov:plan prov:id="tr:WD-prov-dm-20111215">
>     <prov:type xsi:type="xsd:QName">ex:Workflow</prov:type>
>     <prov:type>prov:Plan</prov:type> <!-- inferred -->
>     <prov:type>prov:Entity</prov:type> <!-- inferred -->
>   </prov:plan>
>
> </prov:document>
> ```

#### 2.4.3 XSI Type

Because the `prov:Plan` complexType is defined as an extension of the complexType `prov:Entity`, the following example using `xsi:type` is valid and considered equivalent to the two previous examples. The xml-attribute `xsi:type` tells an XML parser the complexType of the xml-element. The value of `xsi:type` must be a complexType derived from the default xml-element xml-type in a schema with known location (referenced through `xsi:schemaLocation`).
> **Example:**
>
> > **Example:**
> >
> > Example 4: type information using xsi:type
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:tr="http://example.com/ns/tr#">
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111215" xsi:type="prov:Plan">
>     <prov:type xsi:type="xsd:QName">ex:Workflow</prov:type>
>   </prov:entity>
>
> </prov:document>
> ```

A prov-"type" xml-element may be inferred by the use of the `xsi:type` xml-attribute.
> **Example:**
>
> > **Example:**
> >
> > Example 5: type information using xsi:type - type inferences
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:tr="http://example.com/ns/tr#">
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111215" xsi:type="prov:Plan">
>     <prov:type xsi:type="xsd:QName">ex:Workflow</prov:type>
>     <prov:type>prov:Plan</prov:type> <!-- inferred -->
>     <prov:type>prov:Entity</prov:type> <!-- inferred -->
>   </prov:entity>
>
> </prov:document>
> ```

### 2.5 Identifier Conventions

[PROV-DM] defines a PROV Identifier as a qualified name with the following definition:

From [PROV-DM]:
> *A qualified name is a name subject to namespace interpretation. It consists of a namespace, denoted by an optional prefix, and a local name.*

[PROV-DM] also mandates that all qualified names be mappable to a URI by concatenating the namespace URI with a local name.

PROV-XML uses the `prov:id` xml-attribute to denote a PROV Identifier and the `prov:ref` xml-attribute to denote a reference-by-id to an instance of a prov-"type" or prov-"relation" which has a matching PROV Identifier. The value of `prov:ref` must be a valid PROV Identifier, but there is no requirement that for every `prov:ref` a corresponding `prov:id` must be known to exist.

PROV-XML defines the type of both the `prov:id` and `prov:ref` xml-attributes to be `xsd:QName` as that is the XSD datatype that most closely matches the qualified name definition by [PROV-DM]. Care should be taken when generating PROV identifier values in PROV-XML such that there is a known mapping to a URI.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The xsd:QName datatype is more restrictive than the QualifiedName defined in [PROV-N] (e.g. PROV-N allows local names to start with numbers), therefore valid identifier values in [PROV-N] serializations have to potential to not be valid identifier values in PROV-XML. It is recommended to enhance interoperability that provenance users strive to always use identifier schemes that map to valid xsd:QNames and URIs.

### 2.6 Naming Conventions

XML element names are aligned with [PROV-N] record names (e.g. `prov:wasGeneratedBy`, `prov:actedOnBehalfOf`) and record parameter roles (e.g. `prov:delegate`, `prov:responsible` on a Delegation). XML Elements are named in camelCase which also conforms with [PROV-N] naming conventions.

ComplexType names are aligned with [PROV-DM] prov-"type" names (e.g. `prov:Generation`, `prov:Delegation`). ComplexTypes are named in PascalCase which conforms to [PROV-DM] naming conventions and differentiates complexTypes from xml-elements in the schema.

## 3. PROV XML Schema

Provenance concepts, expressed as prov-"types" and prov-"relations", are organized according to six components that are defined in this section.

- **Component 1: entities and activities.** The first component consists of entities, activities, and concepts linking them, such as generation, usage, start, end. The first component is the only one comprising time-related concepts.
- **Component 2: derivations.** The second component is formed with derivations and derivation subtypes.
- **Component 3: agents, responsibility, and influence.** The third component consists of agents and concepts ascribing responsibility to agents.
- **Component 4: bundles.** The fourth component is concerned with bundles, a mechanism to support provenance of provenance.
- **Component 5: alternate.** The fifth component consists of relations linking entities referring to the same thing.
- **Component 6: collections.** The sixth component is about collections.

![PROV-DM Components](https://www.w3.org/TR/prov-xml/images/dm/components-dependencies.png)
Figure 1 ◊: PROV-DM Components (Informative, from PROV-DM Fig. 4)

Table 1 is a mapping of PROV-DM prov-"types" and prov-"relations" in PROV-XML schema XML complexTypes and xml-elements.

*Table 1 ◊: PROV\-DM Types and Relations to XML Schema Mapping*

| **PROV-DM Term / Concept**                                                                    | **XML Schema ComplexType**                                                       | **XML Schema XML Element** | **Component**                                                                                |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------- |
|                                                                                               |                                                                                  |                            |                                                                                              |
| [Entity](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-entity)                        | prov:Entity (§3.1.1)                       | prov:entity                | Component 1: Entities/Activities (§3.1)               |
| [Activity](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-Activity)                    | prov:Activity (§3.1.2)                   | prov:activity              |                                                                                              |
| [Generation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-Generation)                | prov:Generation (§3.1.3)               | prov:wasGeneratedBy        |                                                                                              |
| [Usage](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-Usage)                          | prov:Usage (§3.1.4)                         | prov:used                  |                                                                                              |
| [Communication](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-Communication)          | prov:Communication (§3.1.5)         | prov:wasInformedBy         |                                                                                              |
| [Start](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-Start)                          | prov:Start (§3.1.6)                         | prov:wasStartedBy          |                                                                                              |
| [End](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-End)                              | prov:End (§3.1.7)                             | prov:wasEndedBy            |                                                                                              |
| [Invalidation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-Invalidation)            | prov:Invalidation (§3.1.8)           | prov:wasInvalidatedBy      |                                                                                              |
|                                                                                               | | |                                                                                              |
| [Derivation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-Derivation)                | prov:Derivation (§3.2.1)               | prov:wasDerivedFrom        | §3.2 Component 2: Derivations                       |
| [Revision](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-revision)                    | prov:Revision (§3.2.2)                   | prov:wasRevisionOf         |                                                                                              |
| [Quotation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-quotation)                  | prov:Quotation (§3.2.3)                 | prov:wasQuotedFrom         |                                                                                              |
| [Primary Source](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-primary-source)        | prov:PrimarySource (§3.2.4)         | prov:hadPrimarySource      |                                                                                              |
|                                                                                               | | |                                                                                              |
| [Agent](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-agent)                          | prov:Agent (§3.3.1)                         | prov:agent                 | Component 3: Agents, Responsibility, Influence (§3.3) |
| [Attribution](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-attribution)              | prov:Attribution (§3.3.2)             | prov:wasAttributedTo       |                                                                                              |
| [Association](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-Association)              | prov:Association (§3.3.3)             | prov:wasAssociatedWith     |                                                                                              |
| [Delegation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-delegation)                | prov:Delegation (§3.3.4)               | prov:actedOnBehalfOf       |                                                                                              |
| [Plan](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#concept-plan)                         | prov:Plan (§3.3.3.1)                           | prov:plan                  |                                                                                              |
| [Person](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#concept-person)                     | prov:Person (§3.3.1.1)                       | prov:person                |                                                                                              |
| [Organization](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#concept-organization)         | prov:Organization (§3.3.1.2)           | prov:organization          |                                                                                              |
| [Software Agent](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#concept-software-agent)     | prov:SoftwareAgent (§3.3.1.3)         | prov:softwareAgent         |                                                                                              |
| [Influence](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-influence)                  | prov:Influence (§3.3.5)                 | prov:wasInfluencedBy       |                                                                                              |
|                                                                                               | | |                                                                                              |
| [Bundle](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-bundle-entity)                 | prov:Bundle (§3.4.1)                       | prov:bundle                | §3.4 Component 4: Bundles                           |
| [Bundle Constructor](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-bundle)            | prov:BundleConstructor (§3.4.2) | prov:bundleContent         |                                                                                              |
|                                                                                               | | |                                                                                              |
| [Alternate](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-alternate)                  | prov:Alternate (§3.5.2)                 | prov:alternateOf           | Component 5: Alternate (§3.5)                         |
| [Specialization](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-specialization)        | prov:Specialization (§3.5.1)       | prov:specializationOf      |                                                                                              |
|                                                                                               | | |                                                                                              |
| [Collection](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-collection)                | prov:Collection (§3.6.1)               | prov:collection            | §3.6 Component 6: Collections                       |
| [Empty Collection](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#concept-empty-collection) | prov:EmptyCollection (§3.6.1.1)     | prov:emptyCollection       |                                                                                              |
| [Membership](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-membership)                | prov:Membership (§3.6.2)               | prov:hadMember             |                                                                                              |

In the rest of the section, each type is defined, in English initially, followed by its XML schema definition and some example.

### 3.1 Component 1: Entities and Activities

The first component of PROV-DM is concerned with entities (§3.1.1) and activities (§3.1.2), and their inter-relations: §3.1.4 Usage, §3.1.3 Generation, §3.1.6 Start, §3.1.7 End, and §3.1.5 Communication.

#### 3.1.1 Entity

From [PROV-DM]:
> *An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Entity">
  <xs:sequence>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:location" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:value" minOccurs="0"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:entity` is used to denote a prov:Entity prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="entity" type="prov:Entity"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 6: prov:entity
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:tr="http://example.com/ns/tr#">
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111215">
>     <prov:type xsi:type="xsd:QName">document</prov:type>
>     <ex:version>2</ex:version>
>   </prov:entity>
>
> </prov:document>
> ```

#### 3.1.2 Activity

From [PROV-DM]:
> *An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Activity">
  <xs:sequence>
    <xs:element name="startTime" type="xs:dateTime" minOccurs="0"/>
    <xs:element name="endTime" type="xs:dateTime" minOccurs="0"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:location" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:activity` is used to denote a prov:Activity prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="activity" type="prov:Activity"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 7: prov:activity
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:activity prov:id="ex:a1">
>     <prov:startTime>2011-11-16T16:05:00</prov:startTime>
>     <prov:endTime>2011-11-16T16:06:00</prov:endTime>
>     <prov:type xsi:type="xsd:QName">ex:edit</prov:type>
>     <ex:host>server.example.org</ex:host>
>   </prov:activity>
>
> </prov:document>
> ```

#### 3.1.3 Generation

From [PROV-DM]:
> *Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Generation">
  <xs:sequence>
    <xs:element name="entity" type="prov:IDRef"/>
    <xs:element name="activity" type="prov:IDRef" minOccurs="0"/>
    <xs:element name="time" type="xs:dateTime" minOccurs="0"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:location" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:role" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:wasGeneratedBy` is used to denote a prov:Generation prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasGeneratedBy" type="prov:Generation"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 8: prov:wasGeneratedBy
>
> ```
> <prov:document
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:e1"/>
>
>   <prov:activity prov:id="ex:a1"/>
>
>   <prov:wasGeneratedBy>
>     <prov:entity prov:ref="ex:e1"/>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:time>2001-10-26T21:32:52</prov:time>
>     <ex:port>p1</ex:port>
>   </prov:wasGeneratedBy>
>
>   <prov:entity prov:id="ex:e2"/>
>
>   <prov:wasGeneratedBy>
>     <prov:entity prov:ref="ex:e2"/>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:time>2001-10-26T10:00:00</prov:time>
>     <ex:port>p2</ex:port>
>   </prov:wasGeneratedBy>
>
> </prov:document>
> ```

#### 3.1.4 Usage

From [PROV-DM]:
> *Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Usage">
  <xs:sequence>
    <xs:element name="activity" type="prov:IDRef"/>
    <xs:element name="entity" type="prov:IDRef" minOccurs="0"/>
    <xs:element name="time" type="xs:dateTime" minOccurs="0"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:location" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:role" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
<xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:used` is used to denote a prov:Usage prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="used" type="prov:Usage"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 9: prov:used
>
> ```
> <prov:document
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:activity prov:id="ex:a1"/>
>
>   <prov:entity prov:id="ex:e1"/>
>
>   <prov:entity prov:id="ex:e2"/>
>
>   <prov:used>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:entity prov:ref="ex:e1"/>
>     <prov:time≶2011-11-16T16:00:00</prov:time>
>     <ex:parameter>p1</ex:parameter>
>   </prov:used>
>
>   <prov:used>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:entity prov:ref="ex:e2"/>
>     <prov:time>2011-11-16T16:00:01</prov:time>
>     <ex:parameter>p2</ex:parameter>
>   </prov:used>
>
> </prov:document>
> ```

#### 3.1.5 Communication

From [PROV-DM]:
> *Communication is the exchange of some unspecified entity by two activities, one activity using some entity generated by the other.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Communication">
  <xs:sequence>
    <xs:element name="informed" type="prov:IDRef"/>
    <xs:element name="informant" type="prov:IDRef"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:wasInformedBy` is used to denote a prov:Communication prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasInformedBy" type="prov:Communication"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 10: prov:wasInformedBy
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:activity prov:id="ex:a1">
>     <prov:type xsi:type="xsd:string">traffic regulations enforcing<prov:type>
>   </prov:activity>
>
>   <prov:activity prov:id="ex:a2">
>     <prov:type xsi:type="xsd:string">fine paying, check writing, and mailing</prov:type>
>   </prov:activity>
>
>   <prov:wasInformedBy>
>     <prov:informed prov:ref="ex:a2"/>
>     <prov:informant prov:ref="ex:a1"/>
>   </prov:wasInformedBy>
>
> </prov:document>
> ```

#### 3.1.6 Start

From [PROV-DM]:
> *Start is when an activity is deemed to have been started by an entity, known as trigger. The activity did not exist before its start. Any usage, generation, or invalidation involving an activity follows the activity's start. A start may refer to a trigger entity that set off the activity, or to an activity, known as starter, that generated the trigger.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Start">
  <xs:sequence>
    <xs:element name="activity" type="prov:IDRef"/>
    <xs:element name="trigger" type="prov:IDRef" minOccurs="0"/>
    <xs:element name="starter" type="prov:IDRef" minOccurs="0"/>
    <xs:element name="time" type="xs:dateTime" minOccurs="0"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:location" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:role" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:wasStartedBy` is used to denote a prov:Start prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasStartedBy" type="prov:Start"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 11: prov:wasStartedBy
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:e1">
>     <prov:type xsi:type="xsd:string">email message</prov:type>
>   </prov:entity>
>
>   <prov:activity prov:id="ex:a1">
>     <prov:type xsi:type="xsd:QName">Discuss</prov:type>
>   </prov:activity>
>
>   <prov:wasStartedBy>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:trigger prov:ref="ex:e1"/>
>     <prov:time>2011-11-16T16:05:00</prov:time>
>   </prov:wasStartedBy>
>
>   <prov:used>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:entity prov:ref="ex:e1"/>
>   </prov:used>
>
>   <prov:activity prov:id="ex:a0">
>     <prov:type xsi:type="xsd:QName">Write</prov:type>
>   </prov:activity>
>
>   <prov:wasGeneratedBy>
>     <prov:entity prov:ref="ex:e1"/>
>     <prov:activity prov:ref="ex:a0"/>
>   </prov:wasGeneratedBy>
>
>   <prov:wasStartedBy>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:trigger prov:ref="ex:e1"/>
>     <prov:starter prov:ref="ex:a0"/>
>     <prov:time>2011-11-16T16:05:00</prov:time>
>   </prov:wasStartedBy>
>
>   <prov:wasStartedBy>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:starter prov:ref="ex:a0"/>
>     <prov:time>2011-11-16T16:05:00</prov:time>
>   </prov:wasStartedBy>
>
> </prov:document>
> ```

#### 3.1.7 End

From [PROV-DM]:
> *End is when an activity is deemed to have been ended by an entity, known as trigger. The activity no longer exists after its end. Any usage, generation, or invalidation involving an activity precedes the activity's end. An end may refer to a trigger entity that terminated the activity, or to an activity, known as ender that generated the trigger.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="End">
  <xs:sequence>
    <xs:element name="activity" type="prov:IDRef"/>
    <xs:element name="trigger" type="prov:IDRef"  minOccurs="0"/>
    <xs:element name="ender" type="prov:IDRef" minOccurs="0"/>
    <xs:element name="time" type="xs:dateTime" minOccurs="0"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:location" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:role" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:wasEndedBy` is used to denote a prov:End prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasEndedBy" type="prov:End"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 12: prov:wasEndedBy
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:e1">
>     <prov:type xsi:type="xsd:string">approval document</prov:type>
>   </prov:entity>
>
>   <prov:activity prov:id="ex:a1">
>     <prov:type xsi:type="xsd:QName">Editing</prov:type>
>   </prov:activity>
>
>   <prov:wasEndedBy>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:trigger prov:ref="ex:e1"/>
>   </prov:wasEndedBy>
>
> </prov:document>
> ```

#### 3.1.8 Invalidation

From [PROV-DM]:
> *Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity. The entity is no longer available for use (or further invalidation) after invalidation. Any generation or usage of an entity precedes its invalidation.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Invalidation">
  <xs:sequence>
    <xs:element name="entity" type="prov:IDRef"/>
    <xs:element name="activity" type="prov:IDRef" minOccurs="0"/>
    <xs:element name="time" type="xs:dateTime" minOccurs="0"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:location" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:role" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:wasInvalidatedBy` is used to denote a prov:Invalidation prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasInvalidatedBy" type="prov:Invalidation"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 13: prov:wasInvalidatedBy
>
> ```
> <prov:document
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:bbc="http://www.bbc.co.uk/news/">
>
>   <prov:entity prov:id="ex:The-Painter"/>
>
>   <prov:agent prov:id="ex:Picasso"/>
>
>   <prov:wasAttributedTo>
>     <prov:entity prov:ref="ex:The-Painter" />
>     <prov:agent prov:ref="ex:Picasso" />
>   </prov:wasAttributedTo>
>
>   <prov:activity prov:id="ex:crash"/>
>
>   <prov:wasInvalidatedBy>
>     <prov:entity prov:ref="ex:The-Painter"/>
>     <prov:activity prov:ref="ex:crash"/>
>     <prov:time>1998-09-03T01:31:00</prov:time>
>     <ex:circumstances>plane accident</ex:circumstances>
>   </prov:wasInvalidatedBy>
>
> </prov:document>
> ```

### 3.2 Component 2: Derivations

The second component of PROV-DM is concerned with: derivations (§3.2.1) of entities from other entities and derivation subtypes§3.2.2 Revision, §3.2.3 Quotation, and §3.2.4 Primary Source.

#### 3.2.1 Derivation

From [PROV-DM]:
> *A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Derivation">
  <xs:sequence>
    <xs:element name="generatedEntity" type="prov:IDRef"/>
    <xs:element name="usedEntity" type="prov:IDRef"/>
    <xs:element name="activity" type="prov:IDRef" minOccurs="0"/>
    <xs:element name="generation" type="prov:IDRef" minOccurs="0"/>
    <xs:element name="usage" type="prov:IDRef" minOccurs="0"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:wasDerivedFrom` is used to denote a prov:Derivation prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasDerivedFrom" type="prov:Derivation"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 14: prov:wasDerivedFrom
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:e1"/>
>
>   <prov:entity prov:id="ex:e2"/>
>
>   <prov:wasDerivedFrom>
>     <prov:generatedEntity prov:ref="ex:e2"/>
>     <prov:usedEntity prov:ref="ex:e1"/>
>   </prov:wasDerivedFrom>
>
>   <prov:wasDerivedFrom>
>     <prov:generatedEntity prov:ref="ex:e2"/>
>     <prov:usedEntity prov:ref="ex:e1"/>
>     <prov:type xsi:type="xsd:string">physical transform</prov:type>
>   </prov:wasDerivedFrom>
>
> </prov:document>
> ```

#### 3.2.2 Revision

From [PROV-DM]:
> *A revision is a derivation for which the resulting entity is a revised version of some original.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Revision">
  <xs:complexContent>
    <xs:extension base="prov:Derivation">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:wasRevisionOf` is used to denote a prov:Revision prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasRevisionOf" type="prov:Revision"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 15: prov:wasRevisionOf
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:rec54="http://www.w3.org/2001/02pd/rec54#"
>     xmlns:tr="http://example.com/ns/tr#">
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111215">
>     <prov:type xsi:type="xsd:QName">rec54:WD</prov:type>
>   </prov:entity>
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111018">
>     <prov:type xsi:type="xsd:QName">rec54:WD</prov:type>
>   </prov:entity>
>
>   <prov:wasRevisionOf>
>     <prov:generatedEntity prov:ref="tr:WD-prov-dm-20111215"/>
>     <prov:usedEntity prov:ref="tr:WD-prov-dm-20111018"/>
>   </prov:wasRevisionOf>
>
> </prov:document>
> ```

#### 3.2.3 Quotation

From [PROV-DM]:
> *A quotation is the repeat of (some or all of) an entity, such as text or image, by someone who may or may not be its original author.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Quotation">
  <xs:complexContent>
    <xs:extension base="prov:Derivation">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:wasQuotedFrom` is used to denote a prov:Quotation prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasQuotedFrom" type="prov:Quotation"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 16: prov:wasQuotedFrom
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:wp="http://thinklinks.wordpress.com/2012/03/07/"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:dm="http://dvcs.w3.org/hg/prov/raw-file/default/model/prov-dm.html#">
>
>   <prov:entity prov:id="wp:thoughts-from-the-dagstuhl-principles-of-provenance-workshop"/>
>
>   <prov:entity prov:id="dm:bl-dagstuhl"/>
>
>   <prov:person prov:id="ex:Luc"/>
>
>   <prov:person prov:id="ex:Paul"/>
>
>   <prov:wasQuotedFrom>
>     <prov:generatedEntity prov:ref="dm:gl-dagstuhl"/>
>     <prov:usedEntity prov:ref="wp:thoughts-from-the-dagstuhl-principles-of-provenance-workshop"/>
>   </prov:wasQuotedFrom>
>
>   <prov:wasAttributedTo>
>     <prov:entity prov:ref="dm:bl-dagstuhl"/>
>     <prov:agent prov:ref="ex:Luc"/>
>   </prov:wasAttributedTo>
>
>   <prov:wasAttributedTo>
>     <prov:entity prov:ref="wp:thoughts-from-the-dagstuhl-principles-of-provenance-workshop"/>
>     <prov:agent prov:ref="ex:Paul"/>
>   </prov:wasAttributedTo>
>
> </prov:document>
> ```

#### 3.2.4 Primary Source

From [PROV-DM]:
> *A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="PrimarySource">
  <xs:complexContent>
    <xs:extension base="prov:Derivation">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:hadPrimarySource` is used to denote a prov:PrimarySource prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="hadPrimarySource" type="prov:PrimarySource"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 17: prov:hadPrimarySource
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:la-campagne-de-Russie-1812-1813">
>     <prov:type xsi:type="xsd:QName">map</prov:type>
>   </prov:entity>
>
>   <prov:entity prov:id="ex:revue-d-Histoire-de-la-Pharmacie-t-XVIII">
>     <prov:type xsi:type="xsd:QName">journal</prov:type>
>   </prov:entity>
>
>   <prov:hadPrimarySource>
>     <prov:generatedEntity prov:ref="ex:la-campagne-de-Russie-1812-1813"/>
>     <prov:usedEntity prov:ref="ex:revue-d-Histoire-de-la-Pharmacie-t-XVIII"/>
>   </prov:hadPrimarySource>
>
> </prov:document>
> ```

### 3.3 Component 3: Agents, Responsibility, and Influence

The third component of PROV-DM is concerned with agents and the relations §3.3.2 Attribution, §3.3.3 Association, and §3.3.4 Delegation, relating agents to entities, activities, and agents, respectively.

#### 3.3.1 Agent

From [PROV-DM]:
> *An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Agent">
  <xs:sequence>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:location" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:agent` is used to denote a prov:Agent prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="agent" type="prov:Agent"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 18: prov:agent
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:agent prov:id="ex:e1">
>     <prov:type xsi:type="xsd:QName">prov:Person</prov:type>
>     <ex:name>Alice</ex:name>
>     <ex:employee>1234</ex:employee>
>   </prov:agent>
>
> </prov:document>
> ```

##### 3.3.1.1 Person

From [PROV-DM]:
> *Person agents are people.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Person">
  <xs:complexContent>
    <xs:extension base="prov:Agent">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:person` is used to denote a prov:Person prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="person" type="prov:Person"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 19: prov:person
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:person prov:id="ex:Paolo" />
>
> </prov:document>
> ```

##### 3.3.1.2 Organization

From [PROV-DM]:
> *An organization is a social or legal institution such as a company, society, etc.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Organization">
  <xs:complexContent>
    <xs:extension base="prov:Agent">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:organization` is used to denote a prov:Organization prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="organization" type="prov:Organization"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 20: prov:organization
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:w3="http://w3.org/">
>
>   <prov:organization prov:id="w3:Consortium" />
>
> </prov:document>
> ```

##### 3.3.1.3 Software Agent

From [PROV-DM]:
> *A software agent is running software.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="SoftwareAgent">
  <xs:complexContent>
    <xs:extension base="prov:Agent">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:softwareAgent` is used to denote a prov:SoftwareAgent prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="softwareAgent" type="prov:SoftwareAgent"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 21: prov:softwareAgent
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:softwareAgent prov:id="ex:ag" />
>
> </prov:document>
> ```

#### 3.3.2 Attribution

From [PROV-DM]:
> *Attribution is the ascribing of an entity to an agent.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Attribution">
  <xs:sequence>
    <xs:element name="entity" type="prov:IDRef"/>
    <xs:element name="agent" type="prov:IDRef"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:wasAttributedTo` is used to denote a prov:Attribution prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasAttributedTo" type="prov:Attribution"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 22: prov:wasAttributedTo
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:tr="http://example.com/ns/tr#"
>     xmlns:rec54="http://example.com/ns/rec54#">
>
>   <prov:agent prov:id="ex:Paolo">
>     <prov:typexsi:type="xsd:QName">prov:Person</prov:type>
>   </prov:agent>
>
>   <prov:agent prov:id="ex:Simon">
>     <prov:type xsi:type="xsd:QName">prov:Person</prov:type>
>   </prov:agent>
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111215">
>     <prov:type xsi:type="xsd:QName">rec54:WD</prov:type>
>   </prov:entity>
>
>   <prov:wasAttributedTo>
>     <prov:entity prov:ref="tr:WD-prov-dm-20111215"/>
>     <prov:agent prov:ref="ex:Paolo"/>
>     <prov:type xsi:type="xsd:QName">editorship</prov:type>
>   </prov:wasAttributedTo>
>
>   <prov:wasAttributedTo>
>     <prov:entity prov:ref="tr:WD-prov-dm-20111215"/>
>     <prov:agent prov:ref="ex:Simon"/>
>     <prov:type xsi:type="xsd:QName">authorship</prov:type>
>   </prov:wasAttributedTo>
>
> </prov:document>
> ```

#### 3.3.3 Association

From [PROV-DM]:
> *An activity association is an assignment of responsibility to an agent for an activity, indicating that the agent had a role in the activity. It further allows for a plan to be specified, which is the plan intended by the agent to achieve some goals in the context of this activity.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Association">
  <xs:sequence>
    <xs:element name="activity" type="prov:IDRef"/>
    <xs:element name="agent" type="prov:IDRef" minOccurs="0"/>
    <xs:element name="plan" type="prov:IDRef" minOccurs="0"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:role" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:wasAssociatedWith` is used to denote a prov:Association prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasAssociatedWith" type="prov:Association"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 23: prov:wasAssociatedWith
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:activity prov:id="ex:a">
>     <prov:type xsi:type="xsd:string">workflow execution</prov:type>
>   </prov:activity>
>
>   <prov:agent prov:id="ex:ag1">
>     <prov:type xsi:type="xsd:QName">operator</prov:type>
>   </prov:agent>
>
>   <prov:agent prov:id="ex:ag2">
>     <prov:type xsi:type="xsd:QName">designator</prov:type>
>   </prov:agent>
>
>   <prov:wasAssociatedWith>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:agent prov:ref="ex:ag1"/>
>     <prov:role xsi:type="xsd:QName">loggedInUser</prov:role>
>     <ex:how>webapp</ex:how>
>   </prov:wasAssociatedWith>
>
>   <prov:wasAssociatedWith>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:agent prov:ref="ex:ag2"/>
>     <prov:plan prov:ref="ex:wf"/>
>     <prov:role xsi:type="xsd:QName">designer</prov:role>
>     <ex:content>project1</ex:content>
>   </prov:wasAssociatedWith>
>
>   <prov:plan prov:id="ex:wf">
>     <ex:label>Workflow 1</ex:label>
>     <prov:location xsi:type="xsd:anyURI">http://example.org/workflow1.bpel</prov:location>
>   </prov:plan>
>
> </prov:document>
> ```

##### 3.3.3.1 Plan

From [PROV-DM]:
> *A plan is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Plan">
  <xs:complexContent>
    <xs:extension base="prov:Entity">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:plan` is used to denote a prov:Plan prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="plan" type="prov:Plan"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 24: prov:plan
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:activity prov:id="ex:a">
>     <prov:type xsi:type="xsd:string">workflow execution</prov:type>
>   </prov:activity>
>
>   <prov:agent prov:id="ex:ag1">
>     <prov:type xsi:type="xsd:QName">operator</prov:type>
>   </prov:agent>
>
>   <prov:agent prov:id="ex:ag2">
>     <prov:type xsi:type="xsd:QName">designator</prov:type>
>   </prov:agent>
>
>   <prov:wasAssociatedWith>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:agent prov:ref="ex:ag1"/>
>     <prov:role xsi:type="xsd:QName">loggedInUser</prov:role>
>     <ex:how>webapp</ex:how>
>   </prov:wasAssociatedWith>
>
>   <prov:wasAssociatedWith>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:agent prov:ref="ex:ag2"/>
>     <prov:plan prov:ref="ex:wf"/>
>     <prov:role xsi:type="xsd:QName">designer</prov:role>
>     <ex:content>project1</ex:content>
>   </prov:wasAssociatedWith>
>
>   <prov:plan prov:id="ex:wf">
>     <ex:label>Workflow 1</ex:label>
>     <prov:location xsi:type="xsd:anyURI">http://example.org/workflow1.bpel</prov:location>
>   </prov:plan>
>
> </prov:document>
> ```

#### 3.3.4 Delegation

From [PROV-DM]:
> *Delegation is the assignment of authority and responsibility to an agent (by itself or by another agent) to carry out a specific activity as a delegate or representative, while the agent it acts on behalf of retains some responsibility for the outcome of the delegated work.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Delegation">
  <xs:sequence>
    <xs:element name="delegate" type="prov:IDRef"/>
    <xs:element name="responsible" type="prov:IDRef"/>
    <xs:element name="activity" type="prov:IDRef" minOccurs="0"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:actedOnBehalfOf` is used to denote a prov:Delegation prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="actedOnBehalfOf" type="prov:Delegation"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 25: prov:actedOnBehalfOf
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:activity prov:id="ex:a">
>     <prov:type xsi:type="xsd:QName">workflow</prov:type>
>   </prov:activity>
>
>   <prov:agent prov:id="ex:ag1">
>     <prov:type xsi:type="xsd:QName">programmer</prov:type>
>   </prov:agent>
>
>   <prov:agent prov:id="ex:ag2">
>     <prov:type xsi:type="xsd:QName">researcher</prov:type>
>   </prov:agent>
>
>   <prov:agent prov:id="ex:ag3">
>     <prov:type xsi:type="xsd:QName">funder</prov:type>
>   </prov:agent>
>
>   <prov:wasAssociatedWith>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:agent prov:ref="ex:ag1"/>
>     <prov:role xsi:type="xsd:QName">loggedInUser</prov:role>
>   </prov:wasAssociatedWith>
>
>   <prov:wasAssociatedWith>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:agent prov:ref="ex:ag2"/>
>   </prov:wasAssociatedWith>
>
>   <prov:wasAssociatedWith>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:agent prov:ref="ex:ag3"/>
>   </prov:wasAssociatedWith>
>
>   <prov:actedOnBehalfOf>
>     <prov:delegate prov:ref="ex:ag1"/>
>     <prov:responsible prov:ref="ex:ag2"/>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:type xsi:type="xsd:QName">line-management</prov:type>
>   </prov:actedOnBehalfOf>
>
>   <prov:actedOnBehalfOf>
>     <prov:delegate prov:ref="ex:ag2"/>
>     <prov:responsible prov:ref="ex:ag3"/>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:type xsi:type="xsd:QName">contract</prov:type>
>   </prov:actedOnBehalfOf>
>
> </prov:document>
> ```

#### 3.3.5 Influence

From [PROV-DM]:
> *Influence is the capacity of an entity, activity, or agent to have an effect on the character, development, or behavior of another by means of usage, start, end, generation, invalidation, communication, derivation, attribution, association, or delegation.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Influence">
  <xs:sequence>
    <xs:element name="influencee" type="prov:IDRef"/>
    <xs:element name="influencer" type="prov:IDRef"/>
    <!-- prov attributes -->
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:wasInfluencedBy` is used to denote a prov:Influence prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="wasInfluencedBy" type="prov:Influence"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 26: prov:wasInfluencedBy
>
> ```
> <prov:document
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:tr="http://example.com/ns/tr#"
>     xmlns:w3="http://w3.org/">
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111215"/>
>
>   <prov:agent prov:id="w3:Consortium"/>
>
>   <prov:wasInfluencedBy>
>     <prov:influencee prov:ref="tr:WD-prov-dm-20111215"/>
>     <prov:influencer prov:ref="w3:Consortium"/>
>   </prov:wasInfluencedBy>
>
> </prov:document>
> ```

### 3.4 Component 4: Bundles

The fourth component is concerned with bundles, a mechanism to support provenance of provenance.

#### 3.4.1 Bundle

From [PROV-DM]:
> *A bundle is a named set of provenance descriptions, and is itself an entity, so allowing provenance of provenance to be expressed.*

A `prov:Bundle` identifies a set of provenance descriptions, and is an extension of `prov:Entity`, so allowing provenance of provenance to be expressed by referencing the associated entity. The content of a bundle, i.e. its provenance records, can be represented by the `prov:BundleConstructor` ComplexType and is denoted with the `prov:bundleContent` xml-element, its `prov:id` corresponds to the bundle entity.

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Bundle">
  <xs:complexContent>
    <xs:extension base="prov:Entity">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:bundle` is used to denote a prov:Bundle prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="bundle" type="prov:Bundle"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 27: prov:bundle
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:bob="http://example.com/ns/bob#"
>     xmlns:alice="http://example.com/ns/alice#"
>     xmlns:agg="http://example.com/ns/agg#">
>
>   <prov:bundle prov:id="ex:bundle1">
>     <ex:version>1</ex:version>
>   </prov:bundle>
>
>   <prov:bundleContent prov:id="ex:bundle1">
>     <prov:entity prov:id="ex:report1"/>
>
>     <prov:entity prov:id="ex:report2">
>       <prov:type xsi:type="xsd:QName">report</prov:type>
>       <ex:version>2</ex:version>
>     </prov:entity>
>
>     <prov:wasGeneratedBy>
>       <prov:entity prov:ref="ex:report2"/>
>       <prov:time>2012-05-25T11:00:01</prov:time>
>     </prov:wasGeneratedBy>
>
>     <prov:wasDerivedFrom>
>       <prov:generatedEntity prov:ref="ex:report2"/>
>       <prov:usedEntity prov:ref="ex:report1"/>
>     </prov:wasDerivedFrom>
>   </prov:bundleContent>
>
> </prov:document>
> ```

#### 3.4.2 Bundle Constructor

The `prov:BundleConstructor` ComplexType is used to define a named set of provenance statements. The Bundle Constructor supports the `prov:id` xml-attribute.

The bundle entity associated with a bundle constructor set must have the same `prov:id` as the bundle constructor set.

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="BundleConstructor">
  <xs:choice minOccurs="0" maxOccurs="unbounded">
    <-- references to standard non-PROV attribute PROV elements -->
  </xs:choice>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

The xml-element `prov:bundleContent` is used to denote a set of nested provenance statements from within a prov:Document.

Although `prov:bundleContent` can only be expressed at the `prov:document` level, the corresponding bundle entities may be specified from either the `prov:document` or any `prov:bundleContent`.

```
<xs:complexType name="Document">
  <xs:choice minOccurs="0" maxOccurs="unbounded">
    <!-- references to standard non-PROV attribute PROV elements -->
    <xs:element name="bundleContent" type="prov:BundleConstructor" minOccurs="0"/>
  </xs:choice>
</xs:complexType>
```
> **Example:**
>
> > **Example:**
> >
> > Example 28: prov:bundleContent
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:bob="http://example.com/ns/bob#"
>     xmlns:alice="http://example.com/ns/alice#"
>     xmlns:agg="http://example.com/ns/agg#">
>
>   <prov:bundle prov:id="ex:bundle1">
>     <ex:version>1</ex:version>
>   </prov:bundle>
>
>   <prov:bundleContent prov:id="ex:bundle1">
>     <prov:entity prov:id="ex:report1"/>
>
>     <prov:entity prov:id="ex:report2">
>       <prov:type xsi:type="xsd:QName">report</prov:type>
>       <ex:version>2</ex:version>
>     </prov:entity>
>
>     <prov:wasGeneratedBy>
>       <prov:entity prov:ref="ex:report2"/>
>       <prov:time>2012-05-25T11:00:01</prov:time>
>     </prov:wasGeneratedBy>
>
>     <prov:wasDerivedFrom>
>       <prov:generatedEntity prov:ref="ex:report2"/>
>       <prov:usedEntity prov:ref="ex:report1"/>
>     </prov:wasDerivedFrom>
>   </prov:bundleContent>
>
> </prov:document>
> ```

### 3.5 Component 5: Alternate Entities

The fifth component of PROV-DM is concerned with the
relations §3.5.1 Specialization and §3.5.2 Alternate, relating entities to entities.

#### 3.5.1 Specialization

From [PROV-DM]:
> *An entity that is a specialization of another shares all aspects of the latter, and additionally presents more specific aspects of the same thing as the latter. In particular, the lifetime of the entity being specialized contains that of any specialization.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Specialization">
  <xs:sequence>
    <xs:element name="specificEntity" type="prov:IDRef"/>
    <xs:element name="generalEntity" type="prov:IDRef"/>
  </xs:sequence>
</xs:complexType>
```

The xml-element `prov:specializationOf` is used to denote a prov:Specialization prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="specializationOf" type="prov:Specialization"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 29: prov:specializationOf
>
> ```
> <prov:document
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:bbc="http://www.bbc.co.uk/">
>
>   <prov:entity prov:id="ex:bbcNews2012-03-23"/>
>
>   <prov:entity prov:id="bbc:news"/>
>
>   <prov:specializationOf>
>     <prov:specificEntity prov:ref="ex:bbcNews2012-03-23"/>
>     <prov:generalEntity prov:ref="bbc:news"/>
>   </prov:specializationOf>
>
> </prov:document>
> ```

#### 3.5.2 Alternate

From [PROV-DM]:
> *Two alternate entities present aspects of the same thing. These aspects may be the same or different, and the alternate entities may or may not overlap in time.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Alternate">
  <xs:sequence>
    <xs:element name="alternate1" type="prov:IDRef"/>
    <xs:element name="alternate2" type="prov:IDRef"/>
  </xs:sequence>
</xs:complexType>
```

The xml-element `prov:alternateOf` is used to denote a prov:Alternate prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="alternateOf" type="prov:Alternate"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 30: prov:alternateOf
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:bbc="http://www.bbc.co.uk/news"
>     xmlns:bbcmobile="http://www.bbc.co.uk/news/mobile">
>
>   <prov:entity prov:id="bbc:science-environment-17526723">
>     <prov:type xsi:type="xsd:string">a news item for desktop</prov:type>
>   </prov:entity>
>
>   <prov:entity prov:id="bbcmobile:science-environment-17526723">
>     <prov:type xsi:type="xsd:string">a news item for mobile devices</prov:type>
>   </prov:entity>
>
>   <prov:alternateOf>
>     <prov:alternate1 prov:ref="bbcmobile:science-environment-17526723"/>
>     <prov:alternate2 prov:ref="bbc:science-environment-17526723"/>
>   </prov:alternateOf>
>
> </prov:document>
> ```

### 3.6 Component 6: Collections

The sixth component of PROV-DM is concerned with the notion of collections.
A collection is an entity that has some members. The members are themselves entities, and therefore their provenance can be expressed. Some applications need to be able to express the provenance of the collection itself: e.g. who maintains the collection (attribution), which members it contains as it evolves, and how it was assembled. The purpose of Component 6 is to define the types and relations that are useful to express the provenance of collections.

#### 3.6.1 Collection

From [PROV-DM]:
> *A collection is an entity that provides a structure to some constituents that must themselves be entities. These constituents are said to be member of the collections.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Collection">
  <xs:complexContent>
    <xs:extension base="prov:Entity">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:collection` is used to denote a prov:Collection prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="collection" type="prov:Collection"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 31: prov:collection
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:collection prov:id="ex:c1" />
>
> </prov:document>
> ```

##### 3.6.1.1 Empty Collection

From [PROV-DM]:
> *An empty collection is a collection without members.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="EmptyCollection">
  <xs:complexContent>
    <xs:extension base="prov:Collection">
    </xs:extension>
  </xs:complexContent>
</xs:complexType>
```

The xml-element `prov:emptyCollection` is used to denote a prov:EmptyCollection prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="emptyCollection" type="prov:EmptyCollection"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 32: prov:emptyCollection
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:bbc="http://www.bbc.co.uk/news"
>     xmlns:bbcmobile="http://www.bbc.co.uk/news/mobile">
>
>     <prov:emptyCollection prov:id="ex:c0"/>
>
> </prov:document>
> ```

#### 3.6.2 Membership

From [PROV-DM]:
> *Membership is the belonging of an entity to a collection.*

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Membership">
  <xs:sequence>
    <xs:element name="collection" type="prov:IDRef"/>
    <xs:element name="entity" type="prov:IDRef" maxOccurs="unbounded"/>
  </xs:sequence>
</xs:complexType>
```

The xml-element `prov:hadMember` is used to denote a prov:Membership prov-"type" from within a prov:Document or prov:BundleConstructor.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="hadMember" type="prov:Membership"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 33: prov:hadMember
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:e0"/>
>   <prov:entity prov:id="ex:e1"/>
>   <prov:entity prov:id="ex:e2"/>
>
>   <prov:collection prov:id="ex:c"/>
>
>   <prov:hadMember>
>     <prov:collection prov:ref="ex:c"/>
>     <prov:entity prov:ref="ex:e0"/>
>     <prov:entity prov:ref="ex:e1"/>
>     <prov:entity prov:ref="ex:e2"/>
>   </prov:hadMember>
>
> </prov:document>
> ```

### 3.7 Further Elements of PROV

This section introduces further elements of PROV.

#### 3.7.1 Identifier

From [PROV-DM]:

The xml-attribute used to identify an instances of a prov-"type" or prov-"relation".

```
<xs:attribute xmlns:xs="http://www.w3.org/2001/XMLSchema" name="id" type="xs:QName"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 34: prov:id
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:tr="http://example.com/ns/tr#">
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111215">
>     <prov:type xsi:type="xsd:Qname">document</prov:type>
>     <ex:version>2</ex:version>
>   </prov:entity>
>
> </prov:document>
> ```

#### 3.7.2 Reference

From [PROV-DM]:

A xml-attribute that denotes a reference-by-id to an instance of a prov-"type" or prov-"relation".

```
<xs:attribute ref="prov:ref" use="required" />
```
> **Example:**
>
> > **Example:**
> >
> > Example 35: prov:ref
>
> ```
> <prov:document
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:e1"/>
>
>   <prov:activity prov:id="ex:a1"/>
>
>   <prov:wasGeneratedBy>
>     <prov:entity prov:ref="ex:e1"/>
>     <prov:activity prov:ref="ex:a1"/>
>     <prov:time>2001-10-26T21:32:52</prov:time>
>     <ex:port>p1</ex:port>
>   </prov:wasGeneratedBy>
>
> </prov:document>
> ```

#### 3.7.3 Attributes

The PROV-DM defined prov-"attributes" are represented in XML as xml-elements.

##### 3.7.3.1 Label

From [PROV-DM]:
> *The attribute prov:label provides a human-readable representation of an instance of a PROV-DM type or relation.*

The xml-element `prov:label` is used to denote a label prov-"attribute" and has prov-"type" prov:InternationalizedString.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="label" type="prov:InternationalizedString"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 36: prov:label
>
> ```
> <prov:document
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:e1">
>     <prov:label>This is a human-readable label</prov:label>
>   </prov:entity>
>
>   <prov:entity prov:id="ex:car01">
>     <prov:label xml:lang="fr">Voiture 01</prov:label>
>     <prov:label xml:lang="en">Car 01</prov:label>
>   </prov:entity>
>
> </prov:document>
> ```

##### 3.7.3.2 Location

From [PROV-DM]:
> *A location can be an identifiable geographic place (ISO 19112), but it can also be a non-geographic place such as a directory, row, or column.*

The xml-element `prov:location` is used to denote a location prov-"attribute" and has prov-"type" xs:anySimpleType.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="location" type="xs:anySimpleType"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 37: prov:location
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:MonaLisa">
>     <prov:type xsi:type="xsd:QName">StillImage</prov:type>
>     <prov:location xsi:type="xsd:string">Le Louvre, Paris</prov:location>
>   </prov:entity>
>
>   <prov:entity prov:id="ex:cell">
>     <prov:location xsi:type="xsd:string">(5,5)</prov:location>
>     <prov:value xsi:type="xsd:integer">10</prov:value>
>   </prov:entity>
>
> </prov:document>
> ```

##### 3.7.3.3 Role

From [PROV-DM]:
> *A role is the function of an entity or agent with respect to an activity, in the context of a usage, generation, invalidation, association, start, and end.*

The xml-element `prov:role` is used to denote a Role prov-"attribute" and has prov-"type" xs:anySimpleType.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="role" type="xs:anySimpleType"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 38: prov:role
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:wasAssociatedWith>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:agent prov:ref="ex:ag1"/>
>     <prov:role xsi:type="xsd:QName">loggedInUser</prov:role>
>     <ex:how>webapp</ex:how>
>   </prov:wasAssociatedWith>
>
>   <prov:wasAssociatedWith>
>     <prov:activity prov:ref="ex:a"/>
>     <prov:agent prov:ref="ex:ag2"/>
>     <prov:plan prov:ref="ex:wf"/>
>     <prov:role xsi:type="xsd:QName">designer</prov:role>
>     <ex:content>project1</ex:content>
>   </prov:wasAssociatedWith>
>
> </prov:document>
> ```

##### 3.7.3.4 Type

From [PROV-DM]:
> *The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.*

The xml-element `prov:type` is used to denote a Type prov-"attribute" and has prov-"type" xs:anySimpleType.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="type" type="xs:anySimpleType"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 39: prov:type
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#"
>     xmlns:tr="http://example.com/ns/tr#">
>
>   <prov:entity prov:id="tr:WD-prov-dm-20111215">
>     <prov:type xsi:type="xsd:QName">document</prov:type>
>     <ex:version>2</ex:version>
>   </prov:entity>
>
>   <prov:agent prov:id="ex:e1">
>     <prov:type xsi:type="xsd:QName">prov:Person</prov:type>
>     <ex:name>Alice</ex:name>
>     <ex:employee>1234</ex:employee>
>   </prov:agent>
>
>   <prov:activity prov:id="ex:a1">
>     <prov:startTime>2011-11-16T16:05:00</prov:startTime>
>     <prov:endTime>2011-11-16T16:06:00</prov:endTime>
>     <prov:type xsi:type="xsd:QName">ex:edit</prov:type>
>     <ex:host>server.example.org</ex:host>
>   </prov:activity>
>
> </prov:document>
> ```

##### 3.7.3.5 Value

From [PROV-DM]:
> *The attribute prov:value provides a value that is a direct representation of an entity as a PROV-DM Value.*

The xml-element `prov:value` is used to denote a Value prov-"attribute" and has prov-"type" xs:anySimpleType.

XML Element definition in XML Schema:

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="value" type="xs:anySimpleType"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 40: prov:value
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="ex:in">
>     <prov:value xsi:type="xsd:string">abcd</prov:value>
>   </prov:entity>
>
>   <prov:entity prov:id="ex:out">
>     <prov:value xsi:type="xsd:integer">4</prov:value>
>   </prov:entity>
>
> </prov:document>
> ```

#### 3.7.4 Value

From [PROV-DM]:
> *A value is a constant such as a string, number, time, qualified name, IRI, and encoded binary data, whose interpretation is outside the scope of PROV.*

Relations defined by the PROV-DM to have prov-"type" Value have type `xs:anySimpleType` in PROV-XML unless otherwise specified.

### 3.8 Structural Elements of PROV-XML

#### 3.8.1 Document

The root xml-element of all PROV-XML documents is `prov:document` which has xml-type `prov:Document`.

Similar to a `prov:BundleConstructor`, the `prov:Document` complexType is used to define a set of provenance statements.

Unlike the `prov:BundleConstructor`, a `prov:Document`

- may contain `prov:bundle` xml-elements (but not other `prov:document` xml-elements)
- does not support the prov:id xml-attribute.

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Document">
  <xs:choice minOccurs="0" maxOccurs="unbounded">
    <!-- references to standard non-PROV attribute PROV elements -->
    <xs:element name="bundleContent" type="prov:BundleConstructor" minOccurs="0"/>
  </xs:choice>
</xs:complexType>
```

The xml-element `prov:document` may only be used as the root xml-element of a a PROV-XML document.

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="document" type="prov:Document"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 41: prov:document
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <!-- prov statements go here -->
>
> </prov:document>
> ```

#### 3.8.2 Other

The `prov:other` xml-element provides a place to include non-PROV xml-elements inside a `prov:document` or `prov:bundleContent`.

ComplexType definition (denoting a similarly named prov-"type") in XML Schema:

```
<xs:complexType name="Other">
  <xs:sequence>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
</xs:complexType>
```

The xml-element `prov:other` may be used in a `prov:document` or a `prov:bundleContent` but may not be used inside a prov-"relation", entity, or activity xml-element.

```
<xs:element name="other" type="prov:Other"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 42: prov:other
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <!-- prov statements go here -->
>
>   <prov:other>
>     <ex:foo>
>       <ex:content>bar</ex:content>
>     </ex:foo>
>   </prov:other>
>
>   <!-- more prov statements can go here -->
>
> </prov:document>
> ```

## 4. Media Type

Contact:

Ivan Herman

See also:

[How to Register a Media Type for a W3C Specification](https://www.w3.org/2002/06/registering-mediatype)

[Internet Media Type registration, consistency of use](https://www.w3.org/2001/tag/2002/0129-mime)
TAG Finding 3 June 2002 (Revised 4 September 2002)

The Internet Media Type / MIME type for PROV-XML is "`application/provenance+xml`".

It is recommended that PROV-XML files have the extension "`.provx`" (all lowercase) on all platforms.

It is recommended that PROV-XML files stored on Macintosh HFS file systems be given a file type of `TEXT`.

The information that follows has been [registered with the IANA](http://www.iana.org/assignments/media-types/application/provenance+xml).

Type name:

application

Subtype name:

provenance+xml

Required parameters:

none

Optional parameters:

Same as charset parameter of application/xml as specified in RFC3023 (Section 3.2).

Encoding considerations:

Same as encoding considerations of application/xml as specified in RFC 3023 (Section 3.2).

Security considerations:

PROV-XML is an XML language for describing the provenance of things; applications may evaluate given data to dereference URIs, invoking the security considerations of the scheme for that URI. Note in particular, the privacy issues in [RFC3023] section 10 for HTTP URIs. Data obtained from an inaccurate or malicious data source may lead to inaccurate or misleading conclusions, as well as the dereferencing of unintended URIs. Care must be taken to align the trust in consulted resources with the sensitivity of the intended use of the data.

PROV-XML can express data which is presented to the user, for example, by means of label attributes. Application rendering strings retrieved from untrusted PROV-N documents must ensure that malignant strings may not be used to mislead the reader. The security considerations in the media type registration for XML ([RFC3023] section 10) provide additional guidance around the expression of arbitrary data and markup.

PROV-XML is a language for describing the provenance of things, and therefore a PROV-XML document is metadata for other resources. Untrusted PROV-XML documents may mislead its consumers by indicating that a third-party resource has a reputable lineage, when it has not. Provenance of PROV-XML document should be sought.

PROV-XML uses QNames mappable to IRIs as term identifiers. Applications interpreting data expressed in PROV-XML should address the security issues of [Internationalized Resource Identifiers (IRIs)](http://www.ietf.org/rfc/rfc3987.txt) [RFC3987] Section 8, as well as [Uniform Resource Identifier (URI): Generic Syntax](http://www.ietf.org/rfc/rfc3986.txt) [RFC3986] Section 7.

Multiple IRIs may have the same appearance. Characters in different scripts may look similar (a Cyrillic "о" may appear similar to a Latin "o"). A character followed by combining characters may have the same visual representation as another character (LATIN SMALL LETTER E followed by COMBINING ACUTE ACCENT has the same visual representation as LATIN SMALL LETTER E WITH ACUTE). Any person or application that is writing or interpreting data in PROV-N must take care to use the IRI that matches the intended semantics, and avoid IRIs that make look similar. Further information about matching of similar characters can be found in [Unicode Security Considerations](http://www.unicode.org/reports/tr36/) [UNISEC] and [Internationalized Resource Identifiers (IRIs)](http://www.ietf.org/rfc/rfc3987.txt) [RFC3987] Section 8.

Interoperability considerations:

There are no known interoperability issues.

Published specification:

PROV-XML: The PROV XML Schema, Hua, Tilmes, Zednik (eds), Moreau [http://www.w3.org/TR/prov-xml/](https://www.w3.org/TR/prov-xml/), 2013.

Applications which use this media type:

It may be used by any application for publishing provenance information. This format is designed to be an XML form of provenance.

Fragment identifier considerations:

N/A

Additional Information:

Magic number(s):

PROV-XML documents are XML documents and thus may have initial strings similar to any XML document.

File extension(s):

.provx

Macintosh file type code(s):

"TEXT"

Person & email address to contact for further information:

Ivan Herman, ivan@w3.org

Intended usage:

COMMON

Restrictions on usage:

none

Author:

The PROV-XML specification is the product of the World Wide Web Consortium's Provenance Working Group.

Change controller:

The W3C, and the W3C Provenance Working Group, have change control over this specification.

## A. XML Schema

### A.1 Main Schema

The main PROV schema is an aggregation of the PROV core schema and all PROV-defined extension schemas.

The main PROV schema is available at [http://www.w3.org/ns/prov.xsd](https://www.w3.org/ns/prov.xsd)

### A.2 Core Schema

The PROV core schema defines an XML representation of the PROV data model defined by the PROV-DM. Extensions to PROV, defined in WG Notes, are defined in separate extension schemas.

The PROV core schema is available at [http://www.w3.org/ns/prov-core.xsd](https://www.w3.org/ns/prov-core.xsd)

### A.3 Extension Schemas

Extension schemas are schemas in the PROV Namespace that define additional PROV elements not from the PROV-DM. Workgroup Notes provide extension schemas to define their Note-introduced PROV elements. Extension schemas must import (using `xs:include`) the **prov-core.xsd** schema and make use of a substitution group on the `prov:internalElement` to add extension defined elements to the list of valid PROV elements in a bundle or document.

The PROV-defined extension schemas are available at

- PROV-Dictionary: [http://www.w3.org/ns/prov-dictionary.xsd](https://www.w3.org/ns/prov-dictionary.xsd)
- PROV-Links: [http://www.w3.org/ns/prov-links.xsd](https://www.w3.org/ns/prov-links.xsd)

## B. Change Log

### B.1 Change Log Since WD Working Draft 12 March 2013

- Updated Component section descriptive text
- Added links to schemas in Schema Modularization section
- Fixed typo in Status of this Document section
- Added Identifier Conventions section
- Updated naming conventions to clarify distinction between PROV elements, attributes, and types and XML elements, attributes, and types.
- Added links to PROV-DM term/concepts in Table 1.
- Removed inline schema, added links to published schemas.
- Updated BundleConstructor and Document sections to reflect changes to schema.
- Added Other section for prov:other element and type.
- Updated the Status of this Document section.
- Added a note about potential OXM issues to Schema Modularization section, referenced FAQ entry on subject.

### B.2 Change Log Since First Public Working Draft

- Added Change Log section
- Changed the status of this document section: added new documents to the PROV Family of Document, and removed the how to read section, referring instead to PROV-OVERVIEW.
- Changed all URLs to PROV documents.
- Removed Review notes.
- Updated table 1 with XML Schema Referencing Element column.
- Added Type Conventions and Schema Modularization sections to XML Schema Design section.
- Updated Bundle section to reflect changes in schema design.
- Updated inline schema and schema examples to reflect updates to schema design.
- Updated text that appears before schema snippets and examples in PROV XML Schema subsections.
- Added extension schema example to appendix.
- Removed Macintosh HFS file type paragraph from Media Type section.
- Made all references informative instead of normative since PROV-XML is a note.

## D. References

### D.1 Informative references

[Mappings]

Satya Sahoo and Paul Groth and Olaf Hartig and Simon Miles and Sam Coppens and James Myers and Yolanda Gil and Luc Moreau and Jun Zhao and Michael Panzer and Daniel Garijo [Provenance Vocabulary Mappings](https://www.w3.org/2005/Incubator/prov/wiki/Provenance_Vocabulary_Mappings). August 2010 URL: [http://www.w3.org/2005/Incubator/prov/wiki/Provenance_Vocabulary_Mappings](https://www.w3.org/2005/Incubator/prov/wiki/Provenance_Vocabulary_Mappings)

[PROV-AQ]

Graham Klyne; Paul Groth; eds. [Provenance Access and Query](https://www.w3.org/TR/2013/NOTE-prov-aq-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-aq-20130430/](https://www.w3.org/TR/2013/NOTE-prov-aq-20130430/)

[PROV-CONSTRAINTS]

James Cheney; Paolo Missier; Luc Moreau; eds. [Constraints of the PROV Data Model](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-constraints-20130430/](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/)

[PROV-DC]

Daniel Garijo; Kai Eckert; eds. [Dublin Core to PROV Mapping](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-dc-20130430/](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/)

[PROV-DICTIONARY]

Tom De Nies; Sam Coppens; eds. [PROV-Dictionary: Modeling Provenance for Dictionary Data Structures](https://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/](https://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/)

[PROV-DM]

Luc Moreau; Paolo Missier; eds. [PROV-DM: The PROV Data Model](https://www.w3.org/TR/2013/REC-prov-dm-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-dm-20130430/](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)

[PROV-LINKS]

Luc Moreau; Timothy Lebo; eds. [Linking Across Provenance Bundles](https://www.w3.org/TR/2013/NOTE-prov-links-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-links-20130430/](https://www.w3.org/TR/2013/NOTE-prov-links-20130430/)

[PROV-N]

Luc Moreau; Paolo Missier; eds. [PROV-N: The Provenance Notation](https://www.w3.org/TR/2013/REC-prov-n-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-n-20130430/](https://www.w3.org/TR/2013/REC-prov-n-20130430/)

[PROV-O]

Timothy Lebo; Satya Sahoo; Deborah McGuinness; eds. [PROV-O: The PROV Ontology](https://www.w3.org/TR/2013/REC-prov-o-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-o-20130430/](https://www.w3.org/TR/2013/REC-prov-o-20130430/)

[PROV-OVERVIEW]

Paul Groth; Luc Moreau; eds. [PROV-OVERVIEW: An Overview of the PROV Family of Documents](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-overview-20130430/](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/)

[PROV-PRIMER]

Yolanda Gil; Simon Miles; eds. [PROV Model Primer](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-primer-20130430/](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/)

[PROV-SEM]

James Cheney; ed. [Semantics of the PROV Data Model](https://www.w3.org/TR/2013/NOTE-prov-sem-20130430). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-sem-20130430](https://www.w3.org/TR/2013/NOTE-prov-sem-20130430).

[RFC2119]

S. Bradner. [Key words for use in RFCs to Indicate Requirement Levels.](http://www.ietf.org/rfc/rfc2119.txt) March 1997. Internet RFC 2119. URL: <http://www.ietf.org/rfc/rfc2119.txt>

[RFC3023]

M. Murata; S. St.Laurent; D. Kohn. [XML Media Types (RFC 3023)](http://www.ietf.org/rfc/rfc3023.txt). January 2001. RFC. URL: <http://www.ietf.org/rfc/rfc3023.txt>

[RFC3986]

T. Berners-Lee; R. Fielding; L. Masinter. [Uniform Resource Identifier (URI): Generic Syntax (RFC 3986)](http://www.ietf.org/rfc/rfc3986.txt). January 2005. RFC. URL: <http://www.ietf.org/rfc/rfc3986.txt>

[RFC3987]

M. Dürst; M. Suignard. [Internationalized Resource Identifiers (IRIs) (RFC 3987)](http://www.ietf.org/rfc/rfc3987.txt). January 2005. RFC. URL: <http://www.ietf.org/rfc/rfc3987.txt>

[UNISEC]

Mark Davis; Michel Suignard. [Unicode Security Considerations](http://www.unicode.org/reports/tr36/). 4 August 2010. URL: <http://www.unicode.org/reports/tr36/>
