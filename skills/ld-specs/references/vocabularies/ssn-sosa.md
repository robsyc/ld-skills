---
title: "Semantic Sensor Network Ontology"
source: https://www.w3.org/TR/vocab-ssn/
family: vocabularies
status: W3C Recommendation
spec_date: 2017-10-19
fetched: 2026-10-26
---

# Semantic Sensor Network Ontology

> Sensors, observations, procedures, and features of interest.

## Contents

- Abstract
- 1 Introduction
- 2 Modularization
- 2.1 Vertical Segmentation
- 2.2 Horizontal Segmentation
- 3 Origins of SSN and SOSA
- 4 Axiomatization
  - 4.1 Namespaces
  - 4.2 Overview of Classes and Properties
  - 4.3 Observations
    - 4.3.1 Overview and examples
    - 4.3.2 Specification
  - 4.4 Actuations
    - 4.4.1 Overview and examples
    - 4.4.2 Specification
  - 4.5 Samplings
    - 4.5.1 Overview and examples
    - 4.5.2 Specification
  - 4.6 Features of Interest and Properties
    - 4.6.1 Overview and examples
    - 4.6.2 Specification
  - 4.7 Results
    - 4.7.1 Overview and examples
    - 4.7.2 Specification
  - 4.8 Procedures
    - 4.8.1 Overview and examples
    - 4.8.2 Specification
  - 4.9 Systems and their Deployment
    - 4.9.1 Overview and examples
    - 4.9.2 Specification
- 5 Horizontal Segmentation
  - 5.1 System Capabilities Module
    - 5.1.1 Overview and examples
    - 5.1.2 Specification
  - 5.2 Sample Relations Module
    - 5.2.1 Sample Relationships Specification
- 6 Vertical Segmentation
  - 6.1 Dolce-Ultralite Alignment Module
    - 6.1.1 Namespaces
    - 6.1.2 Class Alignments
    - 6.1.3 Property Alignments
  - 6.2 SSNX Alignment Module
    - 6.2.1 Namespaces
    - 6.2.2 Class Alignments
    - 6.2.3 Property Alignments
  - 6.3 O&M Alignment Module
    - 6.3.1 Identifying the UML elements
    - 6.3.2 Namespaces
    - 6.3.3 Utility Classes
    - 6.3.4 Class Alignments
    - 6.3.5 Property Alignments
  - 6.4 OBOE Alignment Module
    - 6.4.1 Namespaces
    - 6.4.2 Class Alignments
    - 6.4.3 Property Alignments
  - 6.5 PROV Alignment Module
    - 6.5.1 Namespaces
    - 6.5.2 Class Alignments
    - 6.5.3 Property Alignments
- 7 Common Modeling Questions
  - 7.1 Location
  - 7.2 Forecasts
  - 7.3 Quantity Values and Unit of Measures
  - 7.4 Generic or Specific Instances of ssn:Property
  - 7.5 Generic or Specific Instances of ssn:System
- A Wide review
- B Complete Examples
  - B.1 iPhone Barometer
  - B.2 Coal Oil Point Reserve
  - B.3 apartment 134
  - B.4 Tree height measurement
  - B.5 Seismographs
  - B.6 Number of sunspots
  - B.7 Wind sensor spinning cups
  - B.8 Ice Core
  - B.9 DHT22 Description
  - B.10 DHT22 Deployment
  - B.11 IP68 Smart Sensor
  - B.12 Examples from O&M
- D Change History
- Changes since Original (https://www.w3.org/2005/Incubator/ssn/XGR-ssn-20110628/)
- Changes since 1st Public Working Draft (http://www.w3.org/TR/2016/WD-vocab-ssn-20160531/)
  - Changes since 2nd Public Working Draft (https://www.w3.org/TR/2017/WD-vocab-ssn-20170105/)
  - Changes since 3rd Public Working Draft (https://www.w3.org/TR/2017/WD-vocab-ssn-20170504/)
  - Changes since W3C Candidate Recommendation 11 July 2017 (https://www.w3.org/TR/2017/CR-vocab-ssn-20170711/)
- E References
  - E.1 Normative references
  - E.2 Informative references

---

## Abstract

The Semantic Sensor Network (SSN) ontology is an ontology for describing sensors and their observations, the involved procedures, the studied features of interest, the samples used to do so, and the observed properties, as well as actuators. SSN
follows a horizontal and vertical modularization architecture by including a lightweight but self-contained core ontology called SOSA (Sensor, Observation, Sample, and Actuator) for its elementary classes and properties. With their different
scope and different degrees of axiomatization, SSN and SOSA are able to support a wide range of applications and use cases, including satellite imagery, large-scale scientific monitoring, industrial and household infrastructures, social sensing,
citizen science, observation-driven ontology engineering, and the Web of Things. Both ontologies are described below, and examples of their usage are given.

The namespace for SSN terms is http://www.w3.org/ns/ssn/.
The namespace for SOSA terms is http://www.w3.org/ns/sosa/.

The suggested prefix for the SSN namespace is ssn.
The suggested prefix for the SOSA namespace is sosa.

The SSN ontology is available at [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/).
The SOSA ontology is available at [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/).

## 1. Introduction

*This section is non-normative.*

Sensors are a major source of data available on the Web today. While sensor data may be published as mere values, searching, reusing, integrating, and interpreting these data requires more than just the observation results. Of equal importance
for the proper interpretation of these values is information about the studied feature of interest, such as a river, the observed property, such as flow velocity, the utilized sampling strategy, such as the specific locations and times at
which the velocity was measured, and a variety of other information. OGC's Sensor Web Enablement standards [ OandM], [SensorML] provide a means to annotate sensors and their observations. However, these standards are not integrated and aligned
with W3C Semantic Web technologies and Linked Data in particular, which are key drivers for creating and maintaining a global and densely interconnected graph of data. With the rise of the Web
of Things and smart cities and homes more generally, actuators and the data they produce also become first-class citizens of the Web. Given their close relation to sensors, observations, procedures, and features of interest, it is desirable
to provide a common ontology that also includes actuators and actuation. Finally, with the increasing diversity of data and data providers, definitions such as those for sensors need to be broadened, e.g., to include social sensing. The following
specifications introduce the new Semantic Sensor Network (SSN) and Sensor, Observation, Sample, and Actuator (SOSA) ontologies that are set out to provide flexible but coherent perspectives for representing the entities, relations, and activities
involved in sensing, sampling, and actuation. SOSA provides a lightweight core for SSN and aims at broadening the target audience and application areas that can make use of Semantic Web ontologies. At the same time, SOSA acts as minimal interoperability
fall-back level, i.e., it defines those common classes and properties for which data can be safely exchanged across all uses of SSN, its modules, and SOSA.

## 2. Modularization

*This section is non-normative.*

Practitioners using the original Semantic Sensor Network Ontology as defined in the *W3C Semantic Sensor Network Incubator Group* [SSNO]
have identified a major issue in its complexity, partly due to the layering underneath the Dolce-UltraLite (DUL) upper level ontology. In response to this, the new Semantic Sensor Network (SSN) ontology offers several ontology subsets that
are distinguished mainly through their ontological commitments. This section explains the rationale and method for modularizing SSN, i.e., offering several distinct ontologies that are similar in their domain of discourse, but with different
ontological commitments, suitable to several use cases and target audiences. For example, SOSA is intended to provide Schema.org-style semantic enrichment capabilities for data repositories managed by an audience broader than typical ontology
engineers, while still ensuring interoperability with SSN-based repositories.

Ontology modularization is a common method used in ontology engineering to segment an ontology into smaller parts. In general, ontology modularization aims at providing users of ontologies with the knowledge they require, reducing the scope as
much as possible to what is strictly necessary in a given use case. Two main categories of ontology modularization can be distinguished.

The first category comprises those approaches that focus on the composition of existing ontologies by means of integrating and mapping ontologies, most commonly through `owl:import` statements. OWL import has a direction from a dependent
ontology to a dependency ontology. Although import is transitive, knowledge is propagated in only one direction. The importing ontology assumes all the meaning of the imported terms used, by including all axioms relevant to the meaning of
these terms. However, the imported ontology does not capture any of the semantics of the importing ontology.

The second category comprises of mapping approaches that aim to partition and extract parts of ontologies as modules. These mapping approaches are not necessarily directional, but most approaches of ontology extraction rely on the directionality
of the imported modules. The main feature of an ontology module under the second category is that it is self-contained, i.e., the module captures the meaning of the imported terms used by including all axioms relevant to the meaning of these
terms. This means, that the result of certain reasoning tasks such as subsumption or query answering within a single module should be possible and result in the same answers without the need to access other modules of the ontology.

Our modularization uses the first approach by composing the ontology into several modules that use `owl:import` statements, whereby we distinguish two methods depending on the directionality of the segmentation: a vertical segmentation
and a horizontal segmentation.

![Ontology Modules](https://www.w3.org/TR/vocab-ssn/images/modular_ontology.png)

*Figure 1 The SOSA and SSN ontologies and their vertical and horizontal modules.*

## Vertical Segmentation

Vertical modules build upon each other, i.e., they directionally `owl:import` lower level modules. Lower level modules are independent of their higher level modules and logically consistent on their own.

For example, the *Dolce-UltraLite Alignment Module* imports the *SSN
Ontology* which itself imports the *SOSA Ontology*. However, in reverse, neither *SOSA* nor *SSN* import the *Dolce-UltraLite
Alignment Module*. In fact, *SOSA* as the core, does not import any other ontologies, which makes it truly independent of vertical modules that add more expressivity and further ontological commitments to the lightweight semantics of *SOSA*.

Note that higher level here is not to be confused with upper level ontologies. Upper level ontologies are general knowledge ontologies that can be directionally imported in many domains, whereas our definition of higher level ontologies here refers
to an ontology that extends one or several ontology modules to capture a larger part of a knowledge domain and/or combine knowledge domains.

## Horizontal Segmentation

Modules that are horizontally layered may depend on each other, i.e., they may rely on the directional import of another horizontal module. Only one horizontal module that is dependent on the SSN ontology is presented in this specification, the *Sample Relations Module*. Other ontologies that add domain-specific terms to SSN, but require the import of SSN, can be considered horizontal modules.

## 3. Origins of SSN and SOSA

*This section is non-normative.*

Here we briefly review the origins of SSN and SOSA, namely the initial SSN version published by the *W3C Semantic Sensor Network Incubator
Group* [SSNO] and work on Sensor Web Enablement by the OGC. We also highlight the most substantial changes made since the initial release of the SSN ontology.

Starting in 2002, the OGC's Sensor Web Enablement initiative has developed a generic framework for delivering sensor data, dealing with remote-sensing, moving platforms, and in-situ monitoring and sensing. The Sensor Observation Service defines
a standard query interface for sensor and observation data, following the pattern established by OGC for their Web Services. The returned XML data conforms with the Sensor Model Language [SensorML]
and OMXML [OMXML], whereby the latter implements Observations and Measurements [OandM].

SensorML and O&M are complementary viewpoints. SensorML is 'provider-centric' and encodes details of the sensor along with raw observation data. SensorML is self-contained and highly flexible. This makes life easy for data producers but is
demanding on consumers. SensorML provides extensive support for serialization of numeric data arrays and is particularly optimized for data that includes multiple parallel streams that must be processed together. For example, the data collected
by cameras on airborne vehicles must be geo-referenced based on the instantaneous position of the platform and orientation of the camera. In contrast, O&M was designed to be more 'user-centric' with the target of the observation and the
observed property as first-class objects. O&M works at a higher semantic level than SensorML, but only provides abstract classes for sensors, features of interest and observable properties, expecting the details to be provided by specific
applications and domains. O&M also provided a model for sampling, since almost all scientific observations are made on a subset of, or proxy for, the ultimate feature of interest.

The initial *W3C Semantic Sensor Network Incubator Group* ontology (SSN) was built around an ontology design pattern called the *Stimulus
Sensor Observation* (SSO) pattern [SSO-Pattern]. The SSO was developed as a minimal and common ground for heavy-weight ontologies for the use on the Semantic Sensor Web as well
as to explicitly address the need for light-weight semantics requested by the Linked Data community. The SSO was also aligned to the *Dolce-Ultralite* upper ontology (DUL).

The new SSN described in this document is based on a revised and expanded version of this pattern, namely the *Sensor, Observation,
Sample, and Actuator* (SOSA) ontology. Similar to the original SSO, SOSA acts as a central building block for the SSN but puts more emphasis on light-weight use and the ability to be used standalone. The axiomatization also changed to
provide an experience more related to Schema.org. Notable differences include the usage of the Schema.org `domainIncludes` and `rangeIncludes` annotation properties that provide an informal semantics compared to the inferential semantics of their OWL 2 counterparts. In line with the changes implemented for the new SSN, SOSA
also drops the direct DUL alignment although an optional alignment can be achieved via the SSN-DUL alignment provided in Section 6.1 (§6.1). SOSA is also more explicit than SSO in its support for virtual and human sensor.
Finally, and most notably, SOSA extends SSO's original scope beyond sensors and their observations by including classes and properties for actuators and sampling. SOSA also distinguishes between `phenomenonTime` and `resultTime`.

Drawing on considerable implementation and application experience with SSN and sensor and observation ontologies more broadly, the new SSN and SOSA ontologies presented here are set out to address changes in scope and audience, shortcomings of
the initial work, as well as new technical developments. The list below highlights the most important (but by far not exclusive) updates.

- **Addressing changes in scope and audience**
  * The initial SSN was developed with ontology engineers in mind as the primary audience. Due to the widespread adoption of SSN, the increasing role of citizen science, the strong focus on lightweight vocabularies by the Linked Data community,
    and vocabularies such as Schema.org, the ontology was streamlined. SOSA is added as a core, and is also useful as a standalone ontology targeting Web developers, citizen science, lightweight Linked Data publishing, resource-constraint
    IoT devices, data intensive applications (with the possibility of using lightweight reasoning), and so on. The new SSN introduces additional classes and relations on top of SOSA to model the capabilities of sensors and actuators,
    the compositionality of systems, and so forth to suit more complex needs or cases in which more provenance data is required, e.g., to improve reproducibility.
  * Almost all scientific observations make heavy use of sampling strategies, and, therefore, the Sampling, Sampler, and Sample classes, as well as their corresponding properties, have been added to SOSA and SSN.
  * Due to the increasing importance of the Web of Things and smart instrumentation and environments more generally, the classes Actuator and Actuation have been added to SOSA and SSN.
- **Addressing shortcomings of the initial SSN**
  * The new SSN streamlines the relations (and need for) the old Device, Platform, and Systems classes.
  * The old SSN was perceived as too heavyweight (on its axiomatization) and too dependent on OWL reasoning by some users. To strike a balance, DL expressivity of the new lightweight SOSA ontology is ALI(D) which is efficiently supported
    by modern triple stores, while the new SSN is ALRIN(D). In contrast, the old SSN is SRIQ.
  * The SSN previously imported DUL and many SSN terms inherited from DUL terms. Due to frequent user requests, this has been redesigned so that SSN (and SOSA) can be used entirely independently of DUL if desired. Some of the alignments
    with DUL have been reconsidered. Those parts of SSN that use DUL terms have been separated into the [SSN Alignment with DUL ontology.](https://www.w3.org/ns/ssn/dul) This alignment and therefore the role of DUL in SSN
    have been declared non-normative.
  * The definitions for many classes and properties have changed slightly to improve explanation or to correct minor errors. Examples have been separated from the main definitions.
  * The initial SSN has been criticized for its partially inconsistent handling of virtual sensors (including software and simulations) and related classes and properties. The new SSN and SOSA address this issue by allowing all major classes
    to be virtual, and to better support humans and other animals as agents.
  * The notion of Procedure (formerly Plan) has been clarified to describe a workflow, protocol, plan, algorithm, or computational method specifying how to make an Observation, create a Sample, or make a change to the state of the world
    via an Actuator.
  * The Observation class in the initial SSN was conceptualized as a subclass of the DUL Situation class. To improve alignment with O&M and user expectations, as well as to follow a consistent modeling strategy for observations, sampling,
    and actuation, the Observation class defined in SOSA and the new SSN are now conceptualized as activities.
- **Addressing technical developments**
  * The initial SSN used local/guarded domain and range restrictions. The lightweight SOSA ontology uses an even more restrained axiomatization to foster wide reuse and adaptation among an audience that is not necessarily familiar with
    OWL. SOSA makes use of the `domainIncludes` and `rangeIncludes` annotation properties defined in Schema.org. These had not been available before.
  * Given the increased interest in using Semantic Web technologies directly on the level of individual sensors, actuators, or platforms, SOSA's axiomatization does not use many of the more complex language elements introduced by SSN.

## 4. Axiomatization

This section introduces the specifications for SOSA and SSN.

### 4.1 Namespaces

The namespace for SSN terms is http://www.w3.org/ns/ssn/.
The namespace for SOSA terms is http://www.w3.org/ns/sosa/.

The suggested prefix for the SSN namespace is ssn.
The suggested prefix for the SOSA namespace is sosa.

The SSN ontology is available at [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/).
The SOSA ontology is available at [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/).

### 4.2 Overview of Classes and Properties

*This section is non-normative.*

Classes: §4.4.2.1 sosa:ActuatableProperty , §4.4.2.2 sosa:Actuation , §4.4.2.5 sosa:Actuator , §4.9.2.6 ssn:Deployment , §4.6.2.1 sosa:FeatureOfInterest , §4.8.2.6 ssn:Input , §4.3.2.1 sosa:ObservableProperty , §4.3.2.2 sosa:Observation , §4.8.2.8 ssn:Output , §4.9.2.1 sosa:Platform , §4.6.2.4 ssn:Property , §4.8.2.1 sosa:Procedure , §4.7.2.1 sosa:Result , §4.5.2.1 sosa:Sample , §4.5.2.5 sosa:Sampler , §4.5.2.4 sosa:Sampling , §4.3.2.5 sosa:Sensor , §4.3.2.10 ssn:Stimulus , §4.9.2.4 ssn:System

[Show all SOSA and SSN terms] [Show only core SOSA terms]

Object Properties: §4.4.2.3 sosa:actsOnProperty , §4.4.2.7 sosa:madeByActuator , §4.9.2.9 ssn:deployedOnPlatform , §4.9.2.7 ssn:deployedSystem , §4.3.2.13 ssn:detects , §4.6.2.7 ssn:forProperty , §4.9.2.8 ssn:hasDeployment , §4.6.2.2 sosa:hasFeatureOfInterest , §4.8.2.5 ssn:hasInput , §4.8.2.7 ssn:hasOutput , §4.6.2.5 ssn:hasProperty , §4.7.2.2 sosa:hasResult , §4.5.2.2 sosa:hasSample , §4.9.2.5 ssn:hasSubSystem , §4.9.2.2 sosa:hosts , §4.8.2.4 ssn:implementedBy , §4.8.2.3 ssn:implements , §4.9.2.10 ssn:inDeployment , §4.4.2.4 sosa:isActedOnBy , §4.6.2.3 sosa:isFeatureOfInterestOf , §4.9.2.3 sosa:isHostedBy , §4.3.2.7 sosa:isObservedBy , §4.6.2.6 ssn:isPropertyOf , §4.3.2.11 ssn:isProxyFor , §4.7.2.3 sosa:isResultOf , §4.5.2.3 sosa:isSampleOf , §4.4.2.6 sosa:madeActuation , §4.5.2.7 sosa:madeBySampler , §4.3.2.9 sosa:madeBySensor , §4.3.2.8 sosa:madeObservation , §4.5.2.6 sosa:madeSampling , §4.3.2.3 sosa:observedProperty , §4.3.2.6 sosa:observes , §4.3.2.4 sosa:phenomenonTime , §4.8.2.2 sosa:usedProcedure , §4.3.2.12 ssn:wasOriginatedBy

[Show all SOSA and SSN terms] [Show only core SOSA terms]

Datatype Properties: §4.7.2.4 sosa:hasSimpleResult , §4.7.2.5 sosa:resultTime

Several conceptual modules have been defined to cover key sensor, actuation and sampling concepts. The different conceptual modules of SOSA/SSN can be seen in the following figure.

![SOSA/SSN ontology modules - overview](https://www.w3.org/TR/vocab-ssn/images/SSN-OntStructure-Overview.png)

*Figure 2 Overview of the SOSA/SSN ontology modules*

An overview of the main classes and properties inside the ontology modules can be seen in the following figures, from the perspectives of Observation, Actuation and Sampling. In the figures, and in the rest of the document, SOSA-related components
and restrictions are shown in green, while SSN-only components are shown in blue.

![SOSA ontology modules - Observation](https://www.w3.org/TR/vocab-ssn/images/SOSA-OntStructure-Observation.png)

*Figure 3 Overview of the SOSA classes and properties (observation perspective)*

![SSN ontology modules - Observation](https://www.w3.org/TR/vocab-ssn/images/SSN-OntStructure-Observation.png)

*Figure 4 Overview of the SSN classes and properties (observation perspective)*

![SOSA ontology modules - Actuation](https://www.w3.org/TR/vocab-ssn/images/SOSA-OntStructure-Actuation.png)

*Figure 5 Overview of the SOSA classes and properties (actuation perspective)*

![SSN ontology modules - Actuation](https://www.w3.org/TR/vocab-ssn/images/SSN-OntStructure-Actuation.png)

*Figure 6 Overview of the SSN classes and properties (actuation perspective)*

![SOSA ontology modules - Sampling](https://www.w3.org/TR/vocab-ssn/images/SOSA-OntStructure-Sampling.png)

*Figure 7 Overview of the SOSA classes and properties (sampling perspective)*

![SSN ontology modules - Sampling](https://www.w3.org/TR/vocab-ssn/images/SSN-OntStructure-Sampling.png)

*Figure 8 Overview of the SSN classes and properties (sampling perspective)*

### 4.3 Observations

#### 4.3.1 Overview and examples

*This section is non-normative.*

The following figure provides an overview of the core classes and properties that are specifically related to modeling Observations. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

[Show all SOSA and SSN terms (§4.3)] [Show only core SOSA terms (§4.3)]

[![Observation (SOSA)](https://www.w3.org/TR/vocab-ssn/images/SOSA-Observation.png)](https://www.w3.org/TR/vocab-ssn/images/SOSA-Observation.png)

*Figure 9 Classes and relationships involved in Observation (SOSA)*

[![Observation (SOSA/SSN)](https://www.w3.org/TR/vocab-ssn/images/SSN-Observation.png)](https://www.w3.org/TR/vocab-ssn/images/SSN-Observation.png)

*Figure 10 Classes and relationships involved in Observation (SOSA/SSN)*

The following examples illustrate how the terms related to Observation can be used:

- §B.1 iPhone Barometer
- §B.2 Coal Oil Point Reserve
- §B.3 apartment 134
- §B.4 Tree height measurement
- §B.6 Number of sunspots
- §B.5 Seismographs
- §B.7 Wind sensor spinning cups
- §B.11 IP68 Smart Sensor

#### 4.3.2 Specification

This section introduces the following classes and properties:

§4.3.2.1 sosa:ObservableProperty, §4.3.2.2 sosa:Observation, §4.3.2.3 sosa:observedProperty, §4.3.2.4 sosa:phenomenonTime, §4.3.2.5 sosa:Sensor, §4.3.2.6 sosa:observes, §4.3.2.7 sosa:isObservedBy, §4.3.2.8 sosa:madeObservation, §4.3.2.9 sosa:madeBySensor, §4.3.2.10 ssn:Stimulus, §4.3.2.11 ssn:isProxyFor, §4.3.2.12 ssn:wasOriginatedBy, §4.3.2.13 ssn:detects

[Show all SOSA and SSN terms] [Show only core SOSA terms]

##### 4.3.2.1 §4.3.2.1 sosa:ObservableProperty

**IRI:** http://www.w3.org/ns/sosa/ObservableProperty

**a OWL Class**

*Observable Property* - An observable quality (property, characteristic) of a `FeatureOfInterest` (§4.6.2.1).

| Example       | The height of a tree, the depth of a water body, or the temperature of a surface are examples of observable properties, while the value of a classic car is not (directly) observable but asserted.      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sub class of  | §4.6.2.4 ssn:Property                                                                                                                                             |
| Restrictions  | §4.3.2.7 sosa:isObservedBy ***ONLY*** §4.3.2.5 sosa:Sensor ***inverse Of*** §4.3.2.3 sosa:observedProperty ***ONLY*** §4.3.2.2 sosa:Observation ***inverse Of*** §4.3.2.11 ssn:isProxyFor ***ONLY*** §4.3.2.10 ssn:Stimulus |
| is Defined By | [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/)                                                                                                                                                |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.2 §4.3.2.2 sosa:Observation

**IRI:** http://www.w3.org/ns/sosa/Observation

**a OWL Class**

*Observation* - Act of carrying out an (Observation) `Procedure` (§4.8.2.1) to estimate or calculate a value of a property of a `FeatureOfInterest` (§4.6.2.1). Links to a `Sensor` (§4.3.2.5) to describe what made the `Observation` (§4.3.2.2) and how; links to an `ObservableProperty` (§4.3.2.1) to describe what the result is an estimate of, and to a `FeatureOfInterest` (§4.6.2.1) to detail what that property was associated with.

| Example      | The activity of estimating the intensity of an Earthquake using the Mercalli intensity scale is an `Observation` (§4.3.2.2) as is measuring the moment magnitude, i.e., the energy released by said earthquake. |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions | §4.3.2.9 sosa:madeBySensor ***EXACTLY 1*** §4.3.2.9 sosa:madeBySensor ***ONLY*** §4.3.2.5 sosa:Sensor §4.8.2.2 sosa:usedProcedure ***ONLY*** §4.8.2.1 sosa:Procedure §4.6.2.2 sosa:hasFeatureOfInterest ***EXACTLY 1*** §4.6.2.2 sosa:hasFeatureOfInterest ***ONLY*** §4.6.2.1 sosa:FeatureOfInterest §4.3.2.3 sosa:observedProperty ***EXACTLY 1*** §4.3.2.3 sosa:observedProperty ***ONLY*** §4.3.2.1 sosa:ObservableProperty §4.3.2.12 ssn:wasOriginatedBy ***EXACTLY 1*** §4.3.2.12 ssn:wasOriginatedBy ***ONLY*** §4.3.2.10 ssn:Stimulus §4.3.2.4 sosa:phenomenonTime ***EXACTLY 1*** §4.7.2.2 sosa:hasResult ***MIN 1*** §4.7.2.2 sosa:hasResult ***ONLY*** §4.7.2.1 sosa:Result §4.7.2.5 sosa:resultTime ***EXACTLY 1*** |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.3 §4.3.2.3 sosa:observedProperty

**IRI:** http://www.w3.org/ns/sosa/observedProperty

**a OWL Object Property**

*observed property* - Relation linking an `Observation` (§4.3.2.2) to the property that was observed. The `ObservableProperty` (§4.3.2.1) should be a property of the `FeatureOfInterest` (§4.6.2.1) (linked by `hasFeatureOfInterest` (§4.6.2.2)) of this `Observation` (§4.3.2.2).

| Domain Includes | §4.3.2.2 sosa:Observation               |
| --------------- | ---------------------------------------------------------------------------------- |
| Range Includes  | §4.3.2.1 sosa:ObservableProperty |

[Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.4 §4.3.2.4 sosa:phenomenonTime

**IRI:** http://www.w3.org/ns/sosa/phenomenonTime

**a OWL Object Property**

*phenomenon time* - The time that the `Result` (§4.7.2.1) of an `Observation` (§4.3.2.2), `Actuation` (§4.4.2.2), or `Sampling` (§4.5.2.4) applies to the `FeatureOfInterest` (§4.6.2.1). Not necessarily the same as the `resultTime` (§4.7.2.5). May be an interval or an instant, or some other compound temporal entity [owl-time].

| Domain Includes | §4.4.2.2 sosa:Actuation, §4.3.2.2 sosa:Observation, §4.5.2.4 sosa:Sampling |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Range Includes  | [time:TemporalEntity](https://www.w3.org/TR/owl-time/#time:TemporalEntity)                                                                                                                             |

[Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.5 §4.3.2.5 sosa:Sensor

**IRI:** http://www.w3.org/ns/sosa/Sensor

**a OWL Class**

*Sensor* - Device, agent (including humans), or software (simulation) involved in, or implementing, a `Procedure` (§4.8.2.1). `Sensors` (§4.3.2.5) respond to a `Stimulus` (§4.3.2.10), e.g., a change in the environment, or `Input` (§4.8.2.6) data composed from the `Results` (§4.7.2.1) of prior `Observations` (§4.3.2.2), and generate a `Result` (§4.7.2.1). `Sensors` (§4.3.2.5) can be hosted by `Platforms` (§4.9.2.1).

| Example      | Accelerometers, gyroscopes, barometers, magnetometers, and so forth are `Sensors` (§4.3.2.5) that are typically mounted on a modern smart phone (which acts as `Platform` (§4.9.2.1)). Other examples of `Sensors` (§4.3.2.5) include the human eyes. |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sub class of | §4.9.2.4 ssn:System                                                                                                                                                 |
| Restrictions | §4.8.2.3 ssn:implements ***MIN 1*** §4.3.2.6 sosa:observes ***ONLY*** §4.3.2.1 sosa:ObservableProperty §4.3.2.13 ssn:detects ***ONLY*** §4.3.2.10 ssn:Stimulus §4.3.2.8 sosa:madeObservation ***ONLY*** §4.3.2.2 sosa:Observation |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.6 §4.3.2.6 sosa:observes

**IRI:** http://www.w3.org/ns/sosa/observes

**a OWL Object Property**

*observes* - Relation between a `Sensor` (§4.3.2.5) and an `ObservableProperty` (§4.3.2.1) that it is capable of sensing.

| Domain Includes     | §4.3.2.5 sosa:Sensor                         |
| ------------------- | ---------------------------------------------------------------------------------- |
| Range Includes      | §4.3.2.1 sosa:ObservableProperty |
| Inverse property of | §4.3.2.7 sosa:isObservedBy             |
| Sub property of     | §4.6.2.7 ssn:forProperty                 |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.7 §4.3.2.7 sosa:isObservedBy

**IRI:** http://www.w3.org/ns/sosa/isObservedBy

**a OWL Object Property**

*is observed by* - Relation between an `ObservableProperty` (§4.3.2.1) and the `Sensor` (§4.3.2.5) able to observe it.

| Domain Includes     | §4.3.2.1 sosa:ObservableProperty |
| ------------------- | ---------------------------------------------------------------------------------- |
| Range Includes      | §4.3.2.5 sosa:Sensor                         |
| Inverse property of | §4.3.2.6 sosa:observes                     |

[Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.8 §4.3.2.8 sosa:madeObservation

**IRI:** http://www.w3.org/ns/sosa/madeObservation

**a OWL Object Property**

*made observation* - Relation between a `Sensor` (§4.3.2.5) and an `Observation` (§4.3.2.2) made by the `Sensor` (§4.3.2.5).

| Domain Includes     | §4.3.2.5 sosa:Sensor             |
| ------------------- | ---------------------------------------------------------------------- |
| Range Includes      | §4.3.2.2 sosa:Observation   |
| Inverse property of | §4.3.2.9 sosa:madeBySensor |

[Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.9 §4.3.2.9 sosa:madeBySensor

**IRI:** http://www.w3.org/ns/sosa/madeBySensor

**a OWL Object Property**

*made by `Sensor` (§4.3.2.5)* - Relation between an `Observation` (§4.3.2.2) and the `Sensor` (§4.3.2.5) which made the `Observations` (§4.3.2.2).

| Domain Includes     | §4.3.2.2 sosa:Observation         |
| ------------------- | ---------------------------------------------------------------------------- |
| Range Includes      | §4.3.2.5 sosa:Sensor                   |
| Inverse property of | §4.3.2.8 sosa:madeObservation |

[Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.10 §4.3.2.10 ssn:Stimulus

**IRI:** http://www.w3.org/ns/ssn/Stimulus

**a OWL Class**

*Stimulus* - An event in the real world that 'triggers' the `Sensor` (§4.3.2.5). The properties associated to the `Stimulus` (§4.3.2.10) may be different to the eventual observed `ObservableProperty` (§4.3.2.1). It is the event, not the object, that triggers the `Sensor` (§4.3.2.5).

| Restrictions  | §4.3.2.11 ssn:isProxyFor ***ONLY*** §4.3.2.1 sosa:ObservableProperty ***inverse Of*** §4.3.2.12 ssn:wasOriginatedBy ***ONLY*** §4.3.2.2 sosa:Observation ***inverse Of*** §4.3.2.13 ssn:detects ***ONLY*** §4.3.2.5 sosa:Sensor |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                                                                  |

[Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.11 §4.3.2.11 ssn:isProxyFor

**IRI:** http://www.w3.org/ns/ssn/isProxyFor

**a OWL Object Property**

*isProxyFor* - A relation from a `Stimulus` (§4.3.2.10) to the `Property` (§4.6.2.4) that the `Stimulus` (§4.3.2.10) is serving as a proxy for.

| Example       | For example, the expansion of quicksilver is a `Stimulus` (§4.3.2.10) that serves as a proxy for some temperature `Property` (§4.6.2.4). An increase or decrease in the velocity of spinning cups on a wind `Sensor` (§4.3.2.5) is serving as a proxy for the wind speed. |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                                                                  |

[Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.12 §4.3.2.12 ssn:wasOriginatedBy

**IRI:** http://www.w3.org/ns/ssn/wasOriginatedBy

**a OWL Object Property**

*was originated by* - Relation between an `Observation` (§4.3.2.2) and the `Stimulus` (§4.3.2.10) that originated it.

| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/) |
| ------------- | ------------------------------------------------------- |

[Back to module overview and examples (§4.3)] [Back to top (§4.2)]

##### 4.3.2.13 §4.3.2.13 ssn:detects

**IRI:** http://www.w3.org/ns/ssn/detects

**a OWL Object Property**

*detects* - A relation from a `Sensor` (§4.3.2.5) to the `Stimulus` (§4.3.2.10) that the `Sensor` (§4.3.2.5) detects. The `Stimulus` (§4.3.2.10) itself will be serving as a proxy (`isProxyFor` (§4.3.2.11)) for some `ObservableProperty` (§4.3.2.1).

| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/) |
| ------------- | ------------------------------------------------------- |

[Back to module overview and examples (§4.3)] [Back to top (§4.2)]

### 4.4 Actuations

#### 4.4.1 Overview and examples

*This section is non-normative.*

The following figure provides an overview of the core classes and properties that are secifically related to modeling Actuations. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

[Show all SOSA and SSN terms (§4.4)] [Show only core SOSA terms (§4.4)]

[![Actuation (SOSA)](https://www.w3.org/TR/vocab-ssn/images/SOSA-Actuation.png)](https://www.w3.org/TR/vocab-ssn/images/SOSA-Actuation.png)

*Figure 11 Classes and relationships involved in Actuation (SOSA)*

[![Actuation (SOSA/SSN)](https://www.w3.org/TR/vocab-ssn/images/SSN-Actuation.png)](https://www.w3.org/TR/vocab-ssn/images/SSN-Actuation.png)

*Figure 12 Classes and relationships involved in Actuation (SOSA/SSN)*

The following example illustrate how the terms related to Actuations can be used:

- §B.3 apartment 134

#### 4.4.2 Specification

This section introduces the following classes and properties:

§4.4.2.1 sosa:ActuatableProperty, §4.4.2.2 sosa:Actuation, §4.4.2.3 sosa:actsOnProperty, §4.4.2.4 sosa:isActedOnBy, §4.4.2.5 sosa:Actuator, §4.4.2.6 sosa:madeActuation, §4.4.2.7 sosa:madeByActuator

##### 4.4.2.1 §4.4.2.1 sosa:ActuatableProperty

**IRI:** http://www.w3.org/ns/sosa/ActuatableProperty

**a OWL Class**

*Actuatable Property* - An actuatable quality (property, characteristic) of a `FeatureOfInterest` (§4.6.2.1).

| Example       | A window actuator acts by changing the state between a frame and a window. The ability of the window to be opened and closed is its `ActuatableProperty` (§4.4.2.1). |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sub class of  | §4.6.2.4 ssn:Property                                                                                                                                             |
| Restriction   | §4.4.2.4 sosa:isActedOnBy ***ONLY*** §4.4.2.2 sosa:Actuation                                                         |
| is Defined By | [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/)                                                                                                                                                |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.4)] [Back to top (§4.2)]

##### 4.4.2.2 §4.4.2.2 sosa:Actuation

**IRI:** http://www.w3.org/ns/sosa/Actuation

**a OWL Class**

*Actuation* - An `Actuation` (§4.4.2.2) carries out an (Actuation) `Procedure` (§4.8.2.1) to change the state of the world using an `Actuator` (§4.4.2.5).

| Example      | The activity of automatically closing a window if the temperature in a room drops below 20 degree Celsius. The activity is the `Actuation` (§4.4.2.2) and the device that closes the window is the `Actuator` (§4.4.2.5). The `Procedure` (§4.8.2.1) is the rule, plan, or specification that defines the `Conditions` (§5.1.2.3) that triggers the `Actuation` (§4.4.2.2), here a drop in temperature. |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions | §4.4.2.7 sosa:madeByActuator ***EXACTLY 1*** §4.4.2.7 sosa:madeByActuator ***ONLY*** §4.4.2.5 sosa:Actuator §4.8.2.2 sosa:usedProcedure ***ONLY*** §4.8.2.1 sosa:Procedure §4.6.2.2 sosa:hasFeatureOfInterest ***EXACTLY 1*** §4.6.2.2 sosa:hasFeatureOfInterest ***ONLY*** §4.6.2.1 sosa:FeatureOfInterest §4.4.2.3 sosa:actsOnProperty ***MIN 1*** §4.4.2.3 sosa:actsOnProperty ***ONLY*** §4.4.2.1 sosa:ActuatableProperty §4.7.2.2 sosa:hasResult ***MIN 1*** §4.7.2.2 sosa:hasResult ***ONLY*** §4.7.2.1 sosa:Result §4.7.2.5 sosa:resultTime ***EXACTLY 1*** |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.4)] [Back to top (§4.2)]

##### 4.4.2.3 §4.4.2.3 sosa:actsOnProperty

**IRI:** http://www.w3.org/ns/sosa/actsOnProperty

**a OWL Object Property**

*acts on property* - Relation between an `Actuation` (§4.4.2.2) and the property of a `FeatureOfInterest` (§4.6.2.1) it is acting upon.

| Example             | In the activity (`Actuation` (§4.4.2.2)) of automatically closing a window if the temperature in a room drops below 20 degrees Celsius, the property on which the `Actuator` (§4.4.2.5) acts upon is the state of the window as it changes from being open to being closed. |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Domain Includes     | §4.4.2.2 sosa:Actuation                                                                                                                                         |
| Range Includes      | §4.4.2.1 sosa:ActuatableProperty                                                                                                                       |
| Inverse property of | §4.4.2.4 sosa:isActedOnBy                                                                                                                                     |

[Back to module overview and examples (§4.4)] [Back to top (§4.2)]

##### 4.4.2.4 §4.4.2.4 sosa:isActedOnBy

**IRI:** http://www.w3.org/ns/sosa/isActedOnBy

**a OWL Object Property**

*is acted on by* - Relation between an `ActuatableProperty` (§4.4.2.1) of a `FeatureOfInterest` (§4.6.2.1) and an `Actuation` (§4.4.2.2) changing its state.

| Example             | In the activity (`Actuation`) of automatically closing a window if the temperature in a room drops below 20 degrees Celsius, the property on which the `Actuator` (§4.4.2.5) acts upon is the state of the window as it changes from being open to being closed. |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Domain Includes     | §4.4.2.1 sosa:ActuatableProperty                                                                                                                       |
| Range Includes      | §4.4.2.2 sosa:Actuation                                                                                                                                         |
| Inverse property of | §4.4.2.3 sosa:actsOnProperty                                                                                                                               |

[Back to module overview and examples (§4.4)] [Back to top (§4.2)]

##### 4.4.2.5 §4.4.2.5 sosa:Actuator

**IRI:** http://www.w3.org/ns/sosa/Actuator

**a OWL Class**

*Actuator* - A device that is used by, or implements, an (Actuation) `Procedure` (§4.8.2.1) that changes the state of the world.

| Example      | A window actuator for automatic window control, i.e., opening or closing the window.                                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sub class of | §4.9.2.4 ssn:System                                                                                                                                                 |
| Restrictions | §4.8.2.3 ssn:implements ***MIN 1*** §4.6.2.7 ssn:forProperty ***ONLY*** §4.4.2.1 sosa:ActuatableProperty §4.4.2.6 sosa:madeActuation ***ONLY*** §4.4.2.2 sosa:Actuation |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.4)] [Back to top (§4.2)]

##### 4.4.2.6 §4.4.2.6 sosa:madeActuation

**IRI:** http://www.w3.org/ns/sosa/madeActuation

**a OWL Object Property**

*made actuation* - Relation between an `Actuator` (§4.4.2.5) and the `Actuation` (§4.4.2.2) made by the `Actuator` (§4.4.2.5).

| Domain Includes     | §4.4.2.5 sosa:Actuator             |
| ------------------- | -------------------------------------------------------------------------- |
| Range Includes      | §4.4.2.2 sosa:Actuation           |
| Inverse property of | §4.4.2.7 sosa:madeByActuator |

[Back to module overview and examples (§4.4)] [Back to top (§4.2)]

##### 4.4.2.7 §4.4.2.7 sosa:madeByActuator

**IRI:** http://www.w3.org/ns/sosa/madeByActuator

**a OWL Object Property**

*made by actuator* - Relation linking an `Actuation` (§4.4.2.2) to the `Actuator` (§4.4.2.5) that made that `Actuation` (§4.4.2.2).

| Domain Includes     | §4.4.2.2 sosa:Actuation         |
| ------------------- | ------------------------------------------------------------------------ |
| Range Includes      | §4.4.2.5 sosa:Actuator           |
| Inverse property of | §4.4.2.6 sosa:madeActuation |

[Back to module overview and examples (§4.4)] [Back to top (§4.2)]

### 4.5 Samplings

#### 4.5.1 Overview and examples

*This section is non-normative.*

The following figure provides an overview of the core classes and properties that are secifically related to modeling Samplings. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

[Show all SOSA and SSN terms (§4.5)] [Show only core SOSA terms (§4.5)]

[![Sampling and samples (SOSA)](https://www.w3.org/TR/vocab-ssn/images/SOSA-Sampling.png)](https://www.w3.org/TR/vocab-ssn/images/SOSA-Sampling.png)

*Figure 13 Classes and relationships involved in Sampling (SOSA)*

[![Sampling and samples (SOSA/SSN)](https://www.w3.org/TR/vocab-ssn/images/SSN-Sampling.png)](https://www.w3.org/TR/vocab-ssn/images/SSN-Sampling.png)

*Figure 14 Classes and relationships involved in Sampling (SOSA/SSN)*

The following examples illustrate how the terms related to Samplings can be used:

- §B.1 iPhone Barometer
- §B.2 Coal Oil Point Reserve
- §B.5 Seismographs
- §B.8 Ice Core
- §B.10 DHT22 Deployment
- §B.11 IP68 Smart Sensor

#### 4.5.2 Specification

This section introduces the following classes and properties:

§4.5.2.1 sosa:Sample, §4.5.2.2 sosa:hasSample, §4.5.2.3 sosa:isSampleOf, §4.5.2.4 sosa:Sampling, §4.5.2.5 sosa:Sampler, §4.5.2.6 sosa:madeSampling, §4.5.2.7 sosa:madeBySampler

##### 4.5.2.1 §4.5.2.1 sosa:Sample

**IRI:** http://www.w3.org/ns/sosa/Sample

**a OWL Class**

*Sample* - Feature which is intended to be representative of a `FeatureOfInterest` (§4.6.2.1) on which `Observations` (§4.3.2.2) may be made.

| Comment       | Samples are typically subsets or extracts from the feature of interest of an observation. They are used in situations where observations cannot be made directly on the ultimate feature of interest, either because the entire feature cannot be observed, or because it is more convenient to use a proxy. Samples are thus artifacts of an observational strategy, and usually have no significant function outside of their role in the observation process. The characteristics of the samples themselves are generally of little interest, except to the manager of a sampling campaign, or sample curator. A Sample is intended to sample some FeatureOfInterest, so there is an expectation of at least one isSampleOf property. However, in some cases the identity, and even the exact type, of the sampled feature may not be known when observations are made using the sampling features. Physical samples are sometimes known as 'specimens'. |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Example       | A 'station' is essentially an identifiable locality where a `Sensor` (§4.3.2.5) system or procedure may be deployed and an observation made. In the context of the observation model, it connotes the 'world in the vicinity of the station', so the observed properties relate to the physical medium at the station, and not to any physical artifact such as a mooring, buoy, benchmark, monument, well, etc. A statistical sample is often designed to be characteristic of an entire population, so that `Observations` (§4.3.2.2) can be made regarding the sample that provide a good estimate of the properties of the population. |
| Sub class of  | §4.6.2.1 sosa:FeatureOfInterest, §4.7.2.1 sosa:Result                                                             |
| Restrictions  | §4.7.2.3 sosa:isResultOf ***ONLY*** §4.5.2.4 sosa:Sampling §4.7.2.3 sosa:isResultOf ***MIN 1*** §4.5.2.4 sosa:Sampling §4.5.2.3 sosa:isSampleOf ***ONLY*** §4.6.2.1 sosa:FeatureOfInterest §4.5.2.3 sosa:isSampleOf ***MIN 1*** |
| is Defined By | [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/)                                                                                                                                                |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.5)] [Back to top (§4.2)]

##### 4.5.2.2 §4.5.2.2 sosa:hasSample

**IRI:** http://www.w3.org/ns/sosa/hasSample

**a OWL Object Property**

*has sample* - Relation between a `FeatureOfInterest` (§4.6.2.1) and the `Sample` (§4.5.2.1) used to represent it.

| Domain Includes                                                                                  | §4.6.2.1 sosa:FeatureOfInterest |
| ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| Range Includes                                                                                   | §4.5.2.1 sosa:Sample                       |
| Inverse property of                                                                              | §4.5.2.3 sosa:isSampleOf               |
| is [Inverse-Functional](https://www.w3.org/TR/owl2-syntax/#Inverse-Functional_Object_Properties) | |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.5)] [Back to top (§4.2)]

##### 4.5.2.3 §4.5.2.3 sosa:isSampleOf

**IRI:** http://www.w3.org/ns/sosa/isSampleOf

**a OWL Object Property**

*is sample of* - Relation from a `Sample` (§4.5.2.1) to the `FeatureOfInterest` (§4.6.2.1) that it is intended to be representative of.

| Domain Includes                                                                  | sosa:Sample (§4.4.2.2)                    |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Range Includes                                                                   | §4.6.2.1 sosa:FeatureOfInterest |
| Inverse property of                                                              | §4.5.2.2 sosa:hasSample                 |
| is [Functional](https://www.w3.org/TR/owl2-syntax/#Functional_Object_Properties) | |

[Back to module overview and examples (§4.5)] [Back to top (§4.2)]

##### 4.5.2.4 §4.5.2.4 sosa:Sampling

**IRI:** http://www.w3.org/ns/sosa/Sampling

**a OWL Class**

*Sampling* - An act of `Sampling` (§4.5.2.4) carries out a (Sampling) `Procedure` (§4.8.2.1) to create or transform one or more `Samples` (§4.5.2.1).

| Example      | Crushing a rock sample in a ball mill. Digging a pit through a soil sequence. Dividing a field site into quadrants. Drawing blood from a patient. Drilling an observation well. Establishing a station for environmental monitoring. Registering an image of the landscape. Sieving a powder to separate the subset finer than 100-mesh. Selecting a subset of a population. Splitting a piece of drill-core to create two new samples. Taking a diamond-drill core from a rock outcrop. |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions | §4.5.2.7 sosa:madeBySampler ***EXACTLY 1*** §4.5.2.7 sosa:madeBySampler ***ONLY*** §4.5.2.5 sosa:Sampler §4.8.2.2 sosa:usedProcedure ***ONLY*** §4.8.2.1 sosa:Procedure §4.6.2.2 sosa:hasFeatureOfInterest ***EXACTLY 1*** §4.6.2.2 sosa:hasFeatureOfInterest ***ONLY*** §4.6.2.1 sosa:FeatureOfInterest §4.7.2.2 sosa:hasResult ***MIN 1*** §4.5.2.1 sosa:Sample §4.7.2.2 sosa:hasResult ***ONLY*** §4.5.2.1 sosa:Sample §4.7.2.5 sosa:resultTime ***EXACTLY 1*** |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.5)] [Back to top (§4.2)]

##### 4.5.2.5 §4.5.2.5 sosa:Sampler

**IRI:** http://www.w3.org/ns/sosa/Sampler

**a OWL Class**

*Sampler* - A device that is used by, or implements, a (Sampling) `Procedure` (§4.8.2.1) to create or transform one or more samples.

| Example      | A ball mill, diamond drill, hammer, hypodermic syringe and needle, image `Sensor` (§4.3.2.5) or a soil auger can all act as sampling devices (i.e., be `Samplers` (§4.5.2.5)). However, sometimes the distinction between the `Sampler` (§4.5.2.5) and the `Sensor` (§4.5.2.5) is not evident, as they are packaged as a unit. A `Sampler` (§4.5.2.5) need not be a physical device. |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sub class of | §4.9.2.4 ssn:System                                                                                                                                                 |
| Restrictions | §4.8.2.3 ssn:implements ***MIN 1*** §4.5.2.6 sosa:madeSampling ***ONLY*** §4.5.2.4 sosa:Sampling |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.5)] [Back to top (§4.2)]

##### 4.5.2.6 §4.5.2.6 sosa:madeSampling

**IRI:** http://www.w3.org/ns/sosa/madeSampling

**a OWL Object Property**

*made sampling* - Relation between a `Sampler` (§4.5.2.5) (sampling device or entity) and the `Sampling` (§4.5.2.4) act it performed.

| Domain Includes     | §4.5.2.5 sosa:Sampler             |
| ------------------- | ------------------------------------------------------------------------ |
| Range Includes      | §4.5.2.4 sosa:Sampling           |
| Inverse property of | §4.5.2.7 sosa:madeBySampler |

[Back to module overview and examples (§4.5)] [Back to top (§4.2)]

##### 4.5.2.7 §4.5.2.7 sosa:madeBySampler

**IRI:** http://www.w3.org/ns/sosa/madeBySampler

**a OWL Object Property**

*made by sampler* - Relation linking an act of `Sampling` (§4.5.2.4) to the `Sampler` (§4.5.2.5) (sampling device or entity) that made it.

| Domain Includes     | §4.5.2.4 sosa:Sampling         |
| ------------------- | ---------------------------------------------------------------------- |
| Range Includes      | §4.5.2.5 sosa:Sampler           |
| Inverse property of | §4.5.2.6 sosa:madeSampling |

[Back to module overview and examples (§4.5)] [Back to top (§4.2)]

### 4.6 Features of Interest and Properties

#### 4.6.1 Overview and examples

*This section is non-normative.*

The following figure provides an overview of the core classes and properties that are secifically related to modeling Features of Interest and Properties. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

[![Features of Interest and Properties](https://www.w3.org/TR/vocab-ssn/images/SSN-Features.png)](https://www.w3.org/TR/vocab-ssn/images/SSN-Features.png)

*Figure 15 Classes and relationships related to features of interest and properties*

The following examples illustrate how the terms related to Features of Interest and Properties can be used:

- §B.1 iPhone Barometer
- §B.2 Coal Oil Point Reserve
- §B.3 apartment 134
- §B.4 Tree height measurement
- §B.5 Seismographs
- §B.6 Number of sunspots
- §B.7 Wind sensor spinning cups
- §B.8 Ice Core
- §B.10 DHT22 Deployment
- §B.11 IP68 Smart Sensor

#### 4.6.2 Specification

This section introduces the following classes and properties:

§4.6.2.1 sosa:FeatureOfInterest, §4.6.2.2 sosa:hasFeatureOfInterest, §4.6.2.3 sosa:isFeatureOfInterestOf, §4.6.2.4 ssn:Property, §4.6.2.5 ssn:hasProperty, §4.6.2.6 ssn:isPropertyOf, §4.6.2.7 ssn:forProperty

[Show all SOSA and SSN terms (§4.6.2)] [Show only core SOSA terms (§4.6.2)]

##### 4.6.2.1 §4.6.2.1 sosa:FeatureOfInterest

**IRI:** http://www.w3.org/ns/sosa/FeatureOfInterest

**a OWL Class**

*Feature Of Interest* - The thing whose property is being estimated or calculated in the course of an `Observation` (§4.3.2.2) to arrive at a `Result` (§4.7.2.1), or whose property is being manipulated by an `Actuator` (§4.4.2.5), or which is being sampled or transformed in an act of `Sampling` (§4.5.2.4).

| Example       | When measuring the height of a tree, the height is the observed `ObservableProperty` (§4.3.2.2), 20m may be the `Result` (§4.7.2.1) of the `Observation` (§4.3.2.2), and the tree is the `FeatureOfInterest` (§4.6.2.1). A window is a `FeatureOfInterest` (§4.6.2.1) for an automatic window control `Actuator` (§4.4.2.5). |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions  | §4.6.2.5 ssn:hasProperty ***ONLY*** §4.6.2.4 ssn:Property §4.6.2.5 ssn:hasProperty ***MIN 1*** §4.5.2.2 sosa:hasSample ***ONLY*** §4.5.2.1 sosa:Sample |
| is Defined By | [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/)                                                                                                                                                |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.6)] [Back to top (§4.2)]

##### 4.6.2.2 §4.6.2.2 sosa:hasFeatureOfInterest

**IRI:** http://www.w3.org/ns/sosa/hasFeatureOfInterest

**a OWL Object Property**

*has feature of interest* - A relation between an `Observation` (§4.3.2.2) and the entity whose quality was observed, or between an `Actuation` (§4.4.2.2) and the entity whose property was modified, or between an act of `Sampling` (§4.5.2.4) and the entity that was sampled.

| Example             | For example, in an `Observation` (§4.3.2.2) of the weight of a person, the `FeatureOfInterest` (§4.6.2.1) is the person and the property is its weight. |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Domain Includes     | §4.3.2.2 sosa:Observation, §4.4.2.2 sosa:Actuation, §4.5.2.4 sosa:Sampling   |
| Range Includes      | §4.6.2.1 sosa:FeatureOfInterest, §4.5.2.1 sosa:Sample                                                             |
| Inverse property of | §4.6.2.3 sosa:isFeatureOfInterestOf                                                                                                                 |

[Back to module overview and examples (§4.6)] [Back to top (§4.2)]

##### 4.6.2.3 §4.6.2.3 sosa:isFeatureOfInterestOf

**IRI:** http://www.w3.org/ns/sosa/isFeatureOfInterestOf

**a OWL Object Property**

*is feature of interest of* - A relation between a `FeatureOfInterest` (§4.6.2.1) and an `Observation` (§4.3.2.2) about it or an `Actuation` (§4.4.2.2) acting on it, or an act of `Sampling` (§4.5.2.4) that sampled it.

| Domain Includes     | §4.6.2.1 sosa:FeatureOfInterest, §4.5.2.1 sosa:Sample                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Range Includes      | §4.3.2.2 sosa:Observation, §4.4.2.2 sosa:Actuation, §4.5.2.4 sosa:Sampling |
| Inverse property of | §4.6.2.2 sosa:hasFeatureOfInterest                                                                                                                 |

[Back to module overview and examples (§4.6)] [Back to top (§4.2)]

##### 4.6.2.4 §4.6.2.4 ssn:Property

**IRI:** http://www.w3.org/ns/ssn/Property

**a OWL Class**

*Property* - A quality of an entity. An aspect of an entity that is intrinsic to and cannot exist without the entity.

| Restrictions: | §4.6.2.6 ssn:isPropertyOf ***ONLY*** §4.6.2.1 sosa:FeatureOfInterest |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                          |

[Back to module overview and examples (§4.6)] [Back to top (§4.2)]

##### 4.6.2.5 §4.6.2.5 ssn:hasProperty

**IRI:** http://www.w3.org/ns/ssn/hasProperty

**a OWL Object Property**

*has property* - Relation between an entity and a `Property` (§4.6.2.4) of that entity.

| Inverse property of | §4.6.2.6 ssn:isPropertyOf |
| ------------------- | -------------------------------------------------------------------- |
| is Defined By       | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)              |

[Back to module overview and examples (§4.6)] [Back to top (§4.2)]

##### 4.6.2.6 §4.6.2.6 ssn:isPropertyOf

**IRI:** http://www.w3.org/ns/ssn/isPropertyOf

**a OWL Object Property**

*is property of* - Relation between a `Property` (§4.6.2.4) and the entity it belongs to.

| Inverse property of | §4.6.2.5 ssn:hasProperty |
| ------------------- | ------------------------------------------------------------------ |
| is Defined By       | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)            |

[Back to module overview and examples (§4.6)] [Back to top (§4.2)]

##### 4.6.2.7 §4.6.2.7 ssn:forProperty

**IRI:** http://www.w3.org/ns/ssn/forProperty

**a OWL Object Property**

*for property* - A relation between some aspect of an entity and a `Property` (§4.6.2.4).

| Example       | For example, from a `Sensor` (§4.3.2.5) to the properties it can observe; from an `Actuator` (§4.4.2.5) to the properties it can act on; from a `Deployment` (§4.9.2.6) to the properties it was installed to observe or act on; from a `SystemCapability` (§5.1.2.5) to the `Property` (§4.6.2.4) the capability is described for. |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                                                                  |

[Back to module overview and examples (§4.6)] [Back to top (§4.2)]

### 4.7 Results

#### 4.7.1 Overview and examples

*This section is non-normative.*

The following figure provides an overview of the core classes and properties that are secifically related to modeling Results. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

[![Results](https://www.w3.org/TR/vocab-ssn/images/SSN-Results.png)](https://www.w3.org/TR/vocab-ssn/images/SSN-Results.png)

*Figure 16 Classes and relationships related to results*

The following examples illustrate how the terms related to Results can be used:

- §B.1 iPhone Barometer
- §B.2 Coal Oil Point Reserve
- §B.3 apartment 134
- §B.4 Tree height measurement
- §B.5 Seismographs
- §B.6 Number of sunspots
- §B.7 Wind sensor spinning cups
- §B.8 Ice Core
- §B.11 IP68 Smart Sensor

#### 4.7.2 Specification

This section introduces the following classes and properties:

§4.7.2.1 sosa:Result, §4.7.2.2 sosa:hasResult, §4.7.2.3 sosa:isResultOf, §4.7.2.4 sosa:hasSimpleResult, §4.7.2.5 sosa:resultTime

##### 4.7.2.1 §4.7.2.1 sosa:Result

**IRI:** http://www.w3.org/ns/sosa/Result

**a OWL Class**

*Result* - The `Result` (§4.7.2.1) of an `Observation` (§4.3.2.2), `Actuation` (§4.4.2.2), or act of `Sampling` (§4.5.2.4). To store an observation's simple result value one can use the `hasSimpleResult` (§4.7.2.4) property.

| Example     | The value 20 as the height of a certain tree together with the unit, e.g., Meter. |
| ----------- | --------------------------------------------------------------------------------- |
| Restriction | §4.7.2.3 sosa:isResultOf ***MIN 1***    |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.7)] [Back to top (§4.2)]

##### 4.7.2.2 §4.7.2.2 sosa:hasResult

**IRI:** http://www.w3.org/ns/sosa/hasResult

**a OWL Object Property**

*has result* - Relation linking an `Observation` (§4.3.2.2) and a `Sensor` (§4.3.2.5) or `Actuator` (§4.4.2.5) and a `Result` (§4.7.2.1), which contains a value representing the value associated with the observed `Property`.

| Domain Includes     | §4.4.2.2 sosa:Actuation, §4.3.2.2 sosa:Observation, §4.5.2.4 sosa:Sampling |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Range Includes      | §4.7.2.1 sosa:Result, §4.5.2.1 sosa:Sample                                                                                 |
| Inverse property of | §4.7.2.3 sosa:isResultOf                                                                                                                                     |

[Back to module overview and examples (§4.7)] [Back to top (§4.2)]

##### 4.7.2.3 §4.7.2.3 sosa:isResultOf

**IRI:** http://www.w3.org/ns/sosa/isResultOf

**a OWL Object Property**

*is result of* - Relation linking a `Result` (§4.7.2.1) to the `Observation` (§4.3.2.2) or `Actuation` (§4.4.2.2) that created or caused it.

| Domain Includes     | §4.7.2.1 sosa:Result, §4.5.2.1 sosa:Sample                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Range Includes      | §4.4.2.2 sosa:Actuation, §4.3.2.2 sosa:Observation, §4.5.2.4 sosa:Sampling |
| Inverse property of | §4.7.2.2 sosa:hasResult                                                                                                                                       |

[Back to module overview and examples (§4.7)] [Back to top (§4.2)]

##### 4.7.2.4 §4.7.2.4 sosa:hasSimpleResult

**IRI:** http://www.w3.org/ns/sosa/hasSimpleResult

**a OWL Datatype Property**

*has simple result* - The simple value of an `Observation` (§4.3.2.2) or `Actuation` (§4.4.2.2).

| Example         | For instance, the values 23 or true.                                                                                                   |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Domain Includes | §4.3.2.2 sosa:Observation, §4.4.2.2 sosa:Actuation |

[Back to module overview and examples (§4.7)] [Back to top (§4.2)]

##### 4.7.2.5 §4.7.2.5 sosa:resultTime

**IRI:** http://www.w3.org/ns/sosa/resultTime

**a OWL Datatype Property**

*result time* - The result time is the instant of time when the `Observation` (§4.3.2.2), `Actuation` (§4.4.2.2) or `Sampling` (§4.5.2.4) activity was completed.

| Domain Includes | §4.4.2.2 sosa:Actuation, §4.3.2.2 sosa:Observation, §4.5.2.4 sosa:Sampling |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Range           | [xsd:dateTime](https://www.w3.org/TR/xmlschema-2/#dateTime)                                                                                                                                            |

[Back to module overview and examples (§4.7)] [Back to top (§4.2)]

### 4.8 Procedures

#### 4.8.1 Overview and examples

*This section is non-normative.*

The following figure provides an overview of the core classes and properties that are secifically related to modeling Procedures. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

[![Procedures](https://www.w3.org/TR/vocab-ssn/images/SSN-Procedures.png)](https://www.w3.org/TR/vocab-ssn/images/SSN-Procedures.png)

*Figure 17 Classes and relationships related to procedures*

The following examples illustrate how the terms related to Procedures can be used:

- §B.9 DHT22 Description
- §B.11 IP68 Smart Sensor

#### 4.8.2 Specification

This section introduces the following classes and properties:

§4.8.2.1 sosa:Procedure, §4.8.2.2 sosa:usedProcedure, §4.8.2.3 ssn:implements, §4.8.2.4 ssn:implementedBy, §4.8.2.5 ssn:hasInput, §4.8.2.7 ssn:hasOutput, §4.8.2.6 ssn:Input, §4.8.2.8 ssn:Output,

[Show all SOSA and SSN terms (§4.6.2)] [Show only core SOSA terms (§4.6.2)]

##### 4.8.2.1 §4.8.2.1 sosa:Procedure

**IRI:** http://www.w3.org/ns/sosa/Procedure

**a OWL Class**

*Procedure* - A workflow, protocol, plan, algorithm, or computational method specifying how to make an `Observation` (§4.3.2.2), create a `Sample` (§4.5.2.1), or make a change to the state of the world (via an `Actuator` (§4.4.2.5)). A `Procedure` (§4.8.2.1) is re-usable, and might be involved in many `Observations` (§4.3.2.2), `Samplings` (§4.5.2.4), or `Actuations` (§4.4.2.2). It explains the steps to be carried out to arrive at reproducible `Results` (§4.7.2.1).

| Example      | The measured wind speed differs depending on the height of the `Sensor` (§4.3.2.5) above the surface, e.g., due to friction. Consequently, procedures for measuring wind speed define a standard height for anemometers above ground, typically 10m for meteorological measures and 2m in Agrometeorology. This definition of height, `Sensor` (§4.3.2.5) placement, and so forth are defined by the `Procedure` (§4.8.2.1). |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Note         | Many `Observations` (§4.3.2.2) may be created via the same Procedure, the same way as many tables are assembled using the same instructions (as information objects, not their concrete realization). |
| Restrictions | §4.8.2.5 ssn:hasInput ***ONLY*** §4.8.2.6 ssn:Input §4.8.2.7 ssn:hasOutput ***ONLY*** §4.8.2.8 ssn:Output §4.8.2.4 ssn:implementedBy ***ONLY*** §4.9.2.4 ssn:System |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.8)] [Back to top (§4.2)]

##### 4.8.2.2 §4.8.2.2 sosa:usedProcedure

**IRI:** http://www.w3.org/ns/sosa/usedProcedure

**a OWL Object Property**

*used procedure* - A relation to link to a re-usable `Procedure` (§4.8.2.1) used in making an `Observation` (§4.3.2.2), an `Actuation` (§4.4.2.2), or a `Sample` (§4.5.2.1), typically through a `Sensor` (§4.3.2.5), `Actuator` (§4.4.2.5) or `Sampler` (§4.5.2.5).

| Domain Includes       | §4.4.2.2 sosa:Actuation, §4.3.2.2 sosa:Observation, §4.5.2.4 sosa:Sampling   |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Range Includes        | §4.8.2.1 sosa:Procedure                                                                                                                                         |
| Sub property of Chain | §4.3.2.9 sosa:madeBySensor o §4.8.2.3 ssn:implements §4.4.2.7 sosa:madeByActuator o §4.8.2.3 ssn:implements §4.5.2.7 sosa:madeBySampler o §4.8.2.3 ssn:implements |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.8)] [Back to top (§4.2)]

##### 4.8.2.3 §4.8.2.3 ssn:implements

**IRI:** http://www.w3.org/ns/ssn/implements

**a OWL Object Property**

*implements* - Relation between an entity that implements a `Procedure` (§4.8.2.1) in some executable way and the `Procedure` (§4.8.2.1) (an algorithm, procedure or method).

| Inverse property of | §4.8.2.4 ssn:implementedBy |
| ------------------- | ---------------------------------------------------------------------- |
| is Defined By       | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                |

[Back to module overview and examples (§4.8)] [Back to top (§4.2)]

##### 4.8.2.4 §4.8.2.4 ssn:implementedBy

**IRI:** http://www.w3.org/ns/ssn/implementedBy

**a OWL Object Property**

*implemented by* - Relation between a `Procedure` (§4.8.2.1) (an algorithm, procedure or method) and an entity that implements that `Procedure` (§4.8.2.1) in some executable way.

| Inverse property of | §4.8.2.3 ssn:implements |
| ------------------- | ---------------------------------------------------------------- |
| is Defined By       | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)          |

[Back to module overview and examples (§4.8)] [Back to top (§4.2)]

##### 4.8.2.5 §4.8.2.5 ssn:hasInput

**IRI:** http://www.w3.org/ns/ssn/hasInput

**a OWL Object Property**

*has Input* - Relation between a `Procedure` (§4.8.2.1) and an `Input` (§4.8.2.6) to it.

| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/) |
| ------------- | ------------------------------------------------------- |

[Back to module overview and examples (§4.8)] [Back to top (§4.2)]

##### 4.8.2.6 §4.8.2.6 ssn:Input

**IRI:** http://www.w3.org/ns/ssn/Input

**a OWL Class**

*Input* - Any information that is provided to a `Procedure` (§4.8.2.1) for its use.

| Restrictions  | ***inverse Of*** §4.8.2.5 ssn:hasInput ***ONLY*** §4.8.2.1 sosa:Procedure ***inverse Of*** §4.8.2.5 ssn:hasInput ***MIN 1*** |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                                                                  |

[Back to module overview and examples (§4.8)] [Back to top (§4.2)]

##### 4.8.2.7 §4.8.2.7 ssn:hasOutput

**IRI:** http://www.w3.org/ns/ssn/hasOutput

**a OWL Object Property**

*has Output* - Relation between a `Procedure` (§4.8.2.1) and an `Output` (§4.8.2.8) of it.

| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/) |
| ------------- | ------------------------------------------------------- |

[Back to module overview and examples (§4.8)] [Back to top (§4.2)]

##### 4.8.2.8 §4.8.2.8 ssn:Output

**IRI:** http://www.w3.org/ns/ssn/Output

**a OWL Class**

*Output* - Any information that is reported from a `Procedure` (§4.8.2.1).

| Restrictions  | ***inverse Of*** §4.8.2.7 ssn:hasOutput ***ONLY*** §4.8.2.1 sosa:Procedure ***inverse Of*** §4.8.2.7 ssn:hasOutput ***MIN 1*** |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                                                                  |

[Back to module overview and examples (§4.8)] [Back to top (§4.2)]

### 4.9 Systems and their Deployment

#### 4.9.1 Overview and examples

*This section is non-normative.*

The following figure provides an overview of the core classes and properties that are secifically related to modeling systems and their deployment. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

[![Systems and deployment](https://www.w3.org/TR/vocab-ssn/images/SSN-Systems.png)](https://www.w3.org/TR/vocab-ssn/images/SSN-Systems.png)

*Figure 18 Classes and relationships related to systems and deployments*

The following examples illustrate how the terms related to Systems and their Deployment can be used:

- §B.9 DHT22 Description
- §B.10 DHT22 Deployment

#### 4.9.2 Specification

This section introduces the following classes and properties:

§4.9.2.1 sosa:Platform, §4.9.2.2 sosa:hosts, §4.9.2.3 sosa:isHostedBy, §4.9.2.4 ssn:System, §4.9.2.5 ssn:hasSubSystem, §4.9.2.6 ssn:Deployment, §4.9.2.7 ssn:deployedSystem, §4.9.2.8 ssn:hasDeployment, §4.9.2.9 ssn:deployedOnPlatform, §4.9.2.10 ssn:inDeployment

[Show all SOSA and SSN terms (§4.9.2)] [Show only core SOSA terms (§4.9.2)]

##### 4.9.2.1 §4.9.2.1 sosa:Platform

**IRI:** http://www.w3.org/ns/sosa/Platform

**a OWL Class**

*Platform* - A `Platform` (§4.9.2.1) is an entity that `hosts` (§4.9.2.2) other entities, particularly `Sensors` (§4.3.2.5), `Actuators` (§4.4.2.5), `Samplers` (§4.5.2.5), and other `Platforms` (§4.9.2.1).

| Example      | A post, buoy, vehicle, ship, aircraft, satellite, cell-phone, human or animal may act as `Platforms` (§4.9.2.1) for (technical or biological) `Sensors` (§4.3.2.5) or `Actuators` (§4.4.2.5). |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions | §4.9.2.2 sosa:hosts ***ONLY*** §4.9.2.4 ssn:System §4.9.2.10 ssn:inDeployment ***ONLY*** §4.9.2.6 ssn:Deployment |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.9)] [Back to top (§4.2)]

##### 4.9.2.2 §4.9.2.2 sosa:hosts

**IRI:** http://www.w3.org/ns/sosa/hosts

**a OWL Object Property**

*hosts* - Relation between a `Platform` (§4.9.2.1) and a `Sensor` (§4.3.2.5), `Actuator` (§4.4.2.5), `Sampler` (§4.5.2.5), or `Platform` (§4.9.2.1), hosted or mounted on it.

| Domain Includes       | §4.9.2.1 sosa:Platform                                                                                                                                           |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Range Includes        | §4.4.2.5 sosa:Actuator, §4.3.2.5 sosa:Sensor, §4.5.2.5 sosa:Sampler, §4.9.2.1 sosa:Platform |
| Inverse property of   | §4.9.2.3 sosa:isHostedBy                                                                                                                                       |
| Sub property of Chain | §4.9.2.10 ssn:inDeployment o §4.9.2.7 ssn:deployedSystem                                                          |

[Show additional SSN axioms] [Hide additional SSN axioms] [Back to module overview and examples (§4.9)] [Back to top (§4.2)]

##### 4.9.2.3 §4.9.2.3 sosa:isHostedBy

**IRI:** http://www.w3.org/ns/sosa/isHostedBy

**a OWL Object Property**

*is hosted by* - Relation between a `Sensor` (§4.3.2.5), or `Actuator` (§4.4.2.5), `Sampler` (§4.5.2.5), or `Platform` (§4.9.2.1), and the `Platform` (§4.9.2.1) that it is mounted on or hosted by.

| Domain Includes     | §4.4.2.5 sosa:Actuator, §4.3.2.5 sosa:Sensor, §4.5.2.5 sosa:Sampler, §4.9.2.1 sosa:Platform |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Range Includes      | §4.9.2.1 sosa:Platform                                                                                                                                           |
| Inverse property of | §4.9.2.2 sosa:hosts                                                                                                                                                 |

[Back to module overview and examples (§4.9)] [Back to top (§4.2)]

##### 4.9.2.4 §4.9.2.4 ssn:System

**IRI:** http://www.w3.org/ns/ssn/System

**a OWL Class**

*System* - System is a unit of abstraction for pieces of infrastructure that implement `Procedures` (§4.8.2.1). A System may have components, its subsystems, which are other Systems.

| Restrictions  | §4.9.2.3 sosa:isHostedBy ***ONLY*** §4.9.2.1 sosa:Platform §4.8.2.3 ssn:implements ***ONLY*** §4.8.2.1 sosa:Procedure §4.9.2.5 ssn:hasSubSystem ***ONLY*** §4.9.2.4 ssn:System ***inverse Of*** §4.9.2.5 ssn:hasSubSystem ***ONLY*** §4.9.2.4 ssn:System §4.9.2.8 ssn:hasDeployment ***ONLY*** §4.9.2.6 ssn:Deployment |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                                                                  |

[Back to module overview and examples (§4.9)] [Back to top (§4.2)]

##### 4.9.2.5 §4.9.2.5 ssn:hasSubSystem

**IRI:** http://www.w3.org/ns/ssn/hasSubSystem

**a OWL Object Property**

*has subsystem* - Relation between a `System` (§4.9.2.4) and its component parts.

| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/) |
| ------------- | ------------------------------------------------------- |

[Back to module overview and examples (§4.9)] [Back to top (§4.2)]

##### 4.9.2.6 §4.9.2.6 ssn:Deployment

**IRI:** http://www.w3.org/ns/ssn/Deployment

**a OWL Class**

*Deployment* - Describes the `Deployment` (§4.9.2.6) of one or more `Systems` (§4.9.2.4) for a particular purpose. `Deployment` (§4.9.2.6) may be done on a `Platform` (§4.9.2.1).

| Example       | For example, a temperature `Sensor` (§4.3.2.5) deployed on a wall, or a whole network of Sensors deployed for an Observation campaign.                               |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions  | §4.9.2.7 ssn:deployedSystem ***ONLY*** §4.9.2.4 ssn:System §4.9.2.9 ssn:deployedOnPlatform ***ONLY*** §4.9.2.1 sosa:Platform §4.6.2.7 ssn:forProperty ***ONLY*** §4.6.2.4 ssn:Property |
| is Defined By | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                                                                  |

[Back to module overview and examples (§4.9)] [Back to top (§4.2)]

##### 4.9.2.7 §4.9.2.7 ssn:deployedSystem

**IRI:** http://www.w3.org/ns/ssn/deployedSystem

**a OWL Object Property**

*deployed system* - Relation between a `Deployment` (§4.9.2.6) and a deployed `System` (§4.9.2.4).

| Inverse property of | §4.9.2.8 ssn:hasDeployment |
| ------------------- | ---------------------------------------------------------------------- |
| is Defined By       | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                |

[Back to module overview and examples (§4.9)] [Back to top (§4.2)]

##### 4.9.2.8 §4.9.2.8 ssn:hasDeployment

**IRI:** http://www.w3.org/ns/ssn/hasDeployment

**a OWL Object Property**

*has deployment* - Relation between a `System` (§4.9.2.4) and a `Deployment` (§4.9.2.6), recording that the `System` (§4.9.2.4) is deployed in that `Deployment` (§4.9.2.6).

| Inverse property of | §4.9.2.7 ssn:deployedSystem |
| ------------------- | ------------------------------------------------------------------------ |
| is Defined By       | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                  |

[Back to module overview and examples (§4.9)] [Back to top (§4.2)]

##### 4.9.2.9 §4.9.2.9 ssn:deployedOnPlatform

**IRI:** http://www.w3.org/ns/ssn/deployedOnPlatform

**a OWL Object Property**

*deployed on platform* - Relation between a `Deployment` (§4.9.2.6) and the `Platform` (§4.9.2.1) on which the Systems are deployed.

| Inverse property of | §4.9.2.10 ssn:inDeployment |
| ------------------- | -------------------------------------------------------------------- |
| is Defined By       | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)              |

[Back to module overview and examples (§4.9)] [Back to top (§4.2)]

##### 4.9.2.10 §4.9.2.10 ssn:inDeployment

**IRI:** http://www.w3.org/ns/ssn/inDeployment

**a OWL Object Property**

*in deployment* - Relation between a `Platform` (§4.9.2.1) and a `Deployment` (§4.9.2.6), meaning that the `deployedSystems` of the `Deployment` (§4.9.2.6) are hosted on the `Platform` (§4.9.2.1).

| Example             | For example, a relation between a buoy and a `Deployment` (§4.9.2.6) of several `Sensors` (§4.3.2.5). |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inverse property of | §4.9.2.9 ssn:deployedOnPlatform                                                                                                 |
| is Defined By       | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                                          |

[Back to module overview and examples (§4.9)] [Back to top (§4.2)]

## 5. Horizontal Segmentation

*This section is non-normative.*

This section provides details on the currently available horizontal segmentation modules.

### 5.1 System Capabilities Module

The namespace for system capabilities, operating ranges, and survival ranges terms is http://www.w3.org/ns/ssn/systems/

The suggested prefix for the system capabilities, operating ranges, and survival ranges terms is ssn-system

An [ontology graph for this is available](https://www.w3.org/ns/ssn/System).

#### 5.1.1 Overview and examples

*This section is non-normative.*

The following figure provides an overview on the core classes and properties that are specifically related to modeling System capabilities, operating ranges, and survival ranges, under given conditions.

[![Conditions](https://www.w3.org/TR/vocab-ssn/images/SSN-Conditions.png)](https://www.w3.org/TR/vocab-ssn/images/SSN-Conditions.png)

*Figure 19 Classes and relationships related to system capabilities,
operating ranges, and survival ranges, under given conditions*

[![System properties](https://www.w3.org/TR/vocab-ssn/images/SSN-System-Properties.png)](https://www.w3.org/TR/vocab-ssn/images/SSN-System-Properties.png)

*Figure 20 Classes and relationships related to system capabilities, operating ranges and survival ranges*

The following examples illustrate how the terms related to System capabilities, operating ranges, and survival ranges can be used:

- §B.9 DHT22 Description
- §B.11 IP68 Smart Sensor

#### 5.1.2 Specification

This section introduces the following classes and properties:

§5.1.2.2 ssn-system:inCondition, §5.1.2.3 ssn-system:Condition, §5.1.2.4 ssn-system:hasSystemCapability, §5.1.2.5 ssn-system:SystemCapability, §5.1.2.6 ssn-system:hasSystemProperty, §5.1.2.7 ssn-system:SystemProperty, §5.1.2.8 ssn-system:MeasurementRange, §5.1.2.9 ssn-system:ActuationRange, §5.1.2.10 ssn-system:Accuracy, §5.1.2.11 ssn-system:DetectionLimit, §5.1.2.12 ssn-system:Drift, §5.1.2.13 ssn-system:Frequency, §5.1.2.14 ssn-system:Latency, §5.1.2.15 ssn-system:Precision, §5.1.2.16 ssn-system:Resolution, §5.1.2.17 ssn-system:ResponseTime, §5.1.2.18 ssn-system:Selectivity, §5.1.2.19 ssn-system:Sensitivity, §5.1.2.20 ssn-system:hasOperatingRange, §5.1.2.21 ssn-system:OperatingRange, §5.1.2.22 ssn-system:hasOperatingProperty, §5.1.2.23 ssn-system:OperatingProperty, §5.1.2.24 ssn-system:MaintenanceSchedule, §5.1.2.25 ssn-system:OperatingPowerRange §5.1.2.26 ssn-system:hasSurvivalRange, §5.1.2.27 ssn-system:SurvivalRange, §5.1.2.28 ssn-system:hasSurvivalProperty, §5.1.2.29 ssn-system:SurvivalProperty §5.1.2.30 ssn-system:SystemLifetime, §5.1.2.31 ssn-system:BatteryLifetime §5.1.2.32 ssn-system:qualityOfObservation

##### 5.1.2.1 §4.9.2.4 ssn:System

**IRI:** http://www.w3.org/ns/ssn/System

**a OWL Class**

*System* - System is a unit of abstraction for pieces of infrastructure that implement `Procedures` (§4.8.2.1). A System may have components, its subsystems, which are other Systems.

| Additional Restrictions | §5.1.2.4 ssn-system:hasSystemCapability ***ONLY*** §5.1.2.5 ssn-system:SystemCapability §5.1.2.20 ssn-system:hasOperatingRange ***ONLY*** §5.1.2.21 ssn-system:OperatingRange §5.1.2.26 ssn-system:hasSurvivalRange ***ONLY*** §5.1.2.27 ssn-system:SurvivalRange |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is Defined By           | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.2 §5.1.2.2 ssn-system:inCondition

**IRI:** http://www.w3.org/ns/ssn/systems/inCondition

**a OWL Object Property**

*in condition* - Describes the prevailing environmental `Conditions` (§5.1.2.3) for `SystemCapabilites` (§5.1.2.5), `OperatingRanges` (§5.1.2.21) and `SurvivalRanges` (§5.1.2.27).

| Example       | Used for example to say that a `Sensor` (§4.3.2.5) has a particular accuracy in particular `Conditions` (§5.1.2.3). |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                             |

[Back to module overview and examples (§5.1)]

##### 5.1.2.3 §5.1.2.3 ssn-system:Condition

**IRI:** http://www.w3.org/ns/ssn/systems/Condition

**a OWL Class**

*Condition* - Used to specify ranges for qualities that act as `Conditions` (§5.1.2.3) on a Systems' operation.

| Example       | For example, wind speed of 10-60m/s may be used as the `Condition` on a `SystemProperty` (§5.1.2.7), for example, to state that a `Sensor` (§4.3.2.5) has a particular `Accuracy` (§5.1.2.10) under that `Condition`. |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sub class of  | §4.6.2.4 ssn:Property                                                                                                                                             |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.4 §5.1.2.4 ssn-system:hasSystemCapability

**IRI:** http://www.w3.org/ns/ssn/systems/hasSystemCapability

**a OWL Object Property**

*has system capability* - Relation from a `System` (§4.9.2.4) to a `SystemCapability` (§5.1.2.5) describing the capabilities of the `System` (§4.9.2.4) under certain `Conditions` (§5.1.2.3).

| Sub property of | §4.6.2.5 ssn:hasProperty      |
| --------------- | ----------------------------------------------------------------------- |
| is Defined By   | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/) |

[Back to module overview and examples (§5.1)]

##### 5.1.2.5 §5.1.2.5 ssn-system:SystemCapability

**IRI:** http://www.w3.org/ns/ssn/systems/SystemCapability

**a OWL Class**

*System Capability* - Describes normal measurement, actuation, sampling properties such as accuracy, range, precision, etc. of a `System` (§4.9.2.4) under some specified `Conditions` (§5.1.2.3) such as a temperature range.
The capabilities specified here are those that affect the primary purpose of the `System` (§4.9.2.4), while those in `OperatingRange` (§5.1.2.21) represent the system's normal operating environment, including `Conditions` (§5.1.2.3) that don't affect the `Observations` (§4.3.2.2) or the `Actuations` (§4.4.2.2).

| Sub class of  | §4.6.2.4 ssn:Property                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions  | §4.6.2.7 ssn:forProperty ***ONLY*** §4.6.2.4 ssn:Property §5.1.2.6 ssn-system:hasSystemProperty ***ONLY*** §5.1.2.7 ssn-system:SystemProperty §5.1.2.2 ssn-system:inCondition ***ONLY*** §5.1.2.3 ssn-system:Condition §5.1.2.2 ssn-system:inCondition ***MIN 1*** ***inverse Of*** §5.1.2.4 ssn-system:hasSystemCapability ***ONLY*** §4.9.2.4 ssn:System |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.6 §5.1.2.6 ssn-system:hasSystemProperty

**IRI:** http://www.w3.org/ns/ssn/systems/hasSystemProperty

**a OWL Object Property**

*has system property* - Relation from an `SystemCapability` (§5.1.2.5) of a `System` (§4.9.2.4) to a `SystemProperty` (§5.1.2.7) describing the capabilities of the `System` (§4.9.2.4).

| Sub property of | §4.6.2.5 ssn:hasProperty      |
| --------------- | ----------------------------------------------------------------------- |
| is Defined By   | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/) |

[Back to module overview and examples (§5.1)]

##### 5.1.2.7 §5.1.2.7 ssn-system:SystemProperty

**IRI:** http://www.w3.org/ns/ssn/systems/SystemProperty

**a OWL Class**

*System Property* - An identifiable and observable characteristic that represents the `System` (§4.9.2.4)'s ability to operate its primary purpose: a `Sensor` (§4.3.2.5) to make `Observations` (§4.3.2.2), an `Actuator` (§4.4.2.5) to make `Actuations` (§4.4.2.2), or a `Sampler` (§4.5.2.5) to make `Sampling` (§4.5.2.4).

| Sub class of  | §4.6.2.4 ssn:Property                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions  | ***inverse Of*** §5.1.2.6 ssn-system:hasSystemProperty ***ONLY*** §5.1.2.5 ssn-system:SystemCapability ***inverse Of*** §5.1.2.6 ssn-system:hasSystemProperty ***MIN 1*** |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.8 §5.1.2.8 ssn-system:MeasurementRange

**IRI:** http://www.w3.org/ns/ssn/systems/MeasurementRange

**a OWL Class**

*Measurement Range* - The set of values that the `Sensor` (§4.3.2.5) can return as the `Result` (§4.7.2.1) of an `Observation` (§4.3.2.2) under the defined `Conditions` (§5.1.2.3) with the defined system properties.

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty                                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions  | ***inverse Of*** §5.1.2.6 ssn-system:hasSystemProperty ***ONLY*** ***inverse Of*** §5.1.2.4 ssn-system:hasSystemCapability ***ONLY*** §4.3.2.5 sosa:Sensor |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.9 §5.1.2.9 ssn-system:ActuationRange

**IRI:** http://www.w3.org/ns/ssn/systems/ActuationRange

**a OWL Class**

*Actuation Range* - The range of `Property` (§4.6.2.4) values that can be the `Result` (§4.7.2.1) of an `Actuation` (§4.4.2.2) under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty                                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restriction   | ***inverse Of*** §5.1.2.6 ssn-system:hasSystemProperty ***ONLY*** ***inverse Of*** §5.1.2.4 ssn-system:hasSystemCapability ***ONLY*** §4.4.2.5 sosa:Actuator |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.10 §5.1.2.10 ssn-system:Accuracy

**IRI:** http://www.w3.org/ns/ssn/systems/Accuracy

**a OWL Class**

*Accuracy* - The closeness of agreement between the `Result` (§4.7.2.1) of an `Observation` (§4.3.2.2) (resp. the command of an `Actuation` (§4.4.2.2)) and the true value of the observed `ObservableProperty` (§4.3.2.1) (resp. of the acted on `ActuatableProperty` (§4.4.2.1)) under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty |
| ------------- | ------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)               |

[Back to module overview and examples (§5.1)]

##### 5.1.2.11 §5.1.2.11 ssn-system:DetectionLimit

**IRI:** http://www.w3.org/ns/ssn/systems/DetectionLimit

**a OWL Class**

*Detection Limit* - An observed value for which the probability of falsely claiming the absence of a component in a material is beta, given a probability alpha of falsely claiming its presence.

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty                                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restriction   | ***inverse Of*** §5.1.2.6 ssn-system:hasSystemProperty ***ONLY*** ***inverse Of*** §5.1.2.4 ssn-system:hasSystemCapability ***ONLY*** §4.3.2.5 sosa:Sensor |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.12 §5.1.2.12 ssn-system:Drift

**IRI:** http://www.w3.org/ns/ssn/systems/Drift

**a OWL Class**

*Drift* - As a `Sensor` (§4.3.2.5) `Property` (§4.6.2.4): a continuous or incremental change in the reported values of `Observations` (§4.3.2.2) over time for an unchanging `Property` (§4.6.2.4) under the defined `Conditions` (§5.1.2.3).
As an `Actuator` (§4.4.2.5) `Property` (§4.6.2.4): a continuous or incremental change in the true value of the acted on `ActuatableProperty` (§4.4.2.1) over time for an unchanging command under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty |
| ------------- | ------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)               |

[Back to module overview and examples (§5.1)]

##### 5.1.2.13 §5.1.2.13 ssn-system:Frequency

**IRI:** http://www.w3.org/ns/ssn/systems/Frequency

**a OWL Class**

*Frequency* - The smallest possible time between one `Observation` (§4.3.2.2), `Actuation` (§4.4.2.2), or `Sampling` (§4.5.2.4) and the next, under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty |
| ------------- | ------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)               |

[Back to module overview and examples (§5.1)]

##### 5.1.2.14 §5.1.2.14 ssn-system:Latency

**IRI:** http://www.w3.org/ns/ssn/systems/Latency

**a OWL Class**

*Latency* - The time between a command for an `Observation` (§4.3.2.2) (resp. `Actuation` (§4.4.2.2)) and the `Sensor` (§4.3.2.5) providing a `Result` (§4.7.2.1) (resp. the `Actuator` (§4.4.2.5) operating the `Actuation` (§4.4.2.2)), under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty |
| ------------- | ------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)               |

[Back to module overview and examples (§5.1)]

##### 5.1.2.15 §5.1.2.15 ssn-system:Precision

**IRI:** http://www.w3.org/ns/ssn/systems/Precision

**a OWL Class**

*Precision* - As a sensor capability: The closeness of agreement between replicate `Observations` (§4.3.2.2) on an unchanged or similar quality value: i.e., a measure of a `Sensor` (§4.3.2.5)'s ability to consistently reproduce an `Observation` (§4.3.2.2), under the defined `Conditions` (§5.1.2.3).
As an actuator capability: The closeness of agreement between replicate `Actuations` (§4.4.2.2) for an unchanged or similar command: i.e., a measure of an `Actuator` (§4.4.2.5)'s ability to consistently reproduce an `Actuations` (§4.4.2.2), under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty |
| ------------- | ------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)               |

[Back to module overview and examples (§5.1)]

##### 5.1.2.16 §5.1.2.16 ssn-system:Resolution

**IRI:** http://www.w3.org/ns/ssn/systems/Resolution

**a OWL Class**

*Resolution* - As a `Sensor` (§4.3.2.5) `Property` (§4.6.2.4): the smallest difference in the value of a `ObservableProperty` (§4.3.2.1) being observed that would result in perceptably different values of `Observation` (§4.3.2.2) `Results` (§4.7.2.1), under the defined `Conditions` (§5.1.2.3).
As an `Actuator` (§4.4.2.5) `Property` (§4.6.2.4): the smallest difference in the value of an `Actuation` (§4.4.2.2) command that would result in a value change of the `ActuatableProperty` (§4.4.2.1) being acted on, under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty |
| ------------- | ------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)               |

[Back to module overview and examples (§5.1)]

##### 5.1.2.17 §5.1.2.17 ssn-system:ResponseTime

**IRI:** http://www.w3.org/ns/ssn/systems/ResponseTime

**a OWL Class**

*Response time* - As a `Sensor` (§4.3.2.5) `Property` (§4.6.2.4): the time between a (step) change in the value of an observed `ObservableProperty` (§4.3.2.1) and a `Sensor` (§4.3.2.5) (possibly with specified error) 'settling' on an observed value, under the defined `Conditions` (§5.1.2.3).
As an `Actuator` (§4.4.2.5) `Property` (§4.6.2.4): the time between a (step) change in the command of an `Actuator` (§4.4.2.5) and the 'settling' of the value of the acted on `ActuatableProperty` (§4.4.2.1), under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty |
| ------------- | ------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)               |

[Back to module overview and examples (§5.1)]

##### 5.1.2.18 §5.1.2.18 ssn-system:Selectivity

**IRI:** http://www.w3.org/ns/ssn/systems/Selectivity

**a OWL Class**

*Selectivity* - As a `Sensor` (§4.3.2.5) `Property` (§4.6.2.4): Selectivity is a `Property` (§4.6.2.4) of a `Sensor` (§4.3.2.5) whereby it provides observed values for one or more `ObservableProperties` (§4.3.2.1) such that the `Result` (§4.7.2.1) for each `ObservableProperty` (§4.3.2.1) are independent of other `Properties` (§4.6.2.4) in the `FeatureOfInterest` (§4.6.2.1) being investigated, under the defined `Conditions` (§5.1.2.3).
As an `Actuator` (§4.4.2.5) `Property` (§4.6.2.4): Selectivity is a `Property` (§4.6.2.4) of an `Actuator` (§4.4.2.5) whereby it acts on one or more `ActuatableProperties` (§4.4.2.1) such as the `Results` (§4.7.2.1) for each `ActuatableProperty` (§4.4.2.1) are independent of other `Properties` (§4.6.2.4) in the `FeatureOfInterest` (§4.6.2.1) being acted on, under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty |
| ------------- | ------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)               |

[Back to module overview and examples (§5.1)]

##### 5.1.2.19 §5.1.2.19 ssn-system:Sensitivity

**IRI:** http://www.w3.org/ns/ssn/systems/Sensitivity

**a OWL Class**

*Sensitivity* - As a `Sensor` (§4.3.2.5) `Property` (§4.6.2.4): Sensitivity is the quotient of the change in a `Result` (§4.7.2.1) of `Observations` (§4.3.2.2) and the corresponding change in a value of an `ObservableProperty` (§4.3.2.1) being observed, under the defined `Conditions` (§5.1.2.3).
As an `Actuator` (§4.4.2.5) `Property` (§4.6.2.4): Sensitivity is the quotient of the change in a command of `Actuation` (§4.4.2.2) and the corresponding change in a value of an `ActuatableProperty` (§4.4.2.1) being acted on, under the defined `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.7 ssn-system:SystemProperty |
| ------------- | ------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)               |

[Back to module overview and examples (§5.1)]

##### 5.1.2.20 §5.1.2.20 ssn-system:hasOperatingRange

**IRI:** http://www.w3.org/ns/ssn/systems/hasOperatingRange

**a OWL Object Property**

*has operating range* - Relation from a `System` (§4.9.2.4) to an `OperatingRange` (§5.1.2.21) describing the normal operating environment of the `System` (§4.9.2.4).

| Sub property of | §4.6.2.5 ssn:hasProperty      |
| --------------- | ----------------------------------------------------------------------- |
| is Defined By   | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/) |

[Back to module overview and examples (§5.1)]

##### 5.1.2.21 §5.1.2.21 ssn-system:OperatingRange

**IRI:** http://www.w3.org/ns/ssn/systems/OperatingRange

**a OWL Class**

*Operating Range* - Describes normal `OperatingProperties` (§5.1.2.23) of a `System` (§4.9.2.4) under some specified `Conditions` (§5.1.2.3). For example, to the power requirement or maintenance schedule of a `System` under a specified temperature range.
In the absence of `OperatingProperties` (§5.1.2.23), it simply describes the `Conditions` (§5.1.2.3) in which a `System` (§4.9.2.4) is expected to operate.
The `System` (§4.9.2.4) continues to operate as defined using `SystemCapability` (§5.1.2.5). If, however, the `OperatingProperty` (§5.1.2.23) is violated, the System is operating 'out of operating range' and `SystemCapability` (§5.1.2.5) specifications may no longer hold.

| Sub class of  | §4.6.2.4 ssn:Property                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions: | §5.1.2.22 ssn-system:hasOperatingProperty ***ONLY*** §5.1.2.23 ssn-system:OperatingProperty §5.1.2.2 ssn-system:inCondition ***ONLY*** §5.1.2.3 ssn-system:Condition §5.1.2.2 ssn-system:inCondition ***MIN 1*** ***inverse Of*** §5.1.2.20 ssn-system:hasOperatingRange ***ONLY*** §4.9.2.4 ssn:System |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.22 §5.1.2.22 ssn-system:hasOperatingProperty

**IRI:** http://www.w3.org/ns/ssn/systems/hasOperatingProperty

**a OWL Object Property**

*has operating property* - Relation from an `OperatingRange` (§5.1.2.21) of a `System` (§4.9.2.4) to an `OperatingProperty` (§5.1.2.23) describing the operating range of the `System` (§4.9.2.4).

| Sub property of | §4.6.2.5 ssn:hasProperty      |
| --------------- | ----------------------------------------------------------------------- |
| is Defined By   | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/) |

[Back to module overview and examples (§5.1)]

##### 5.1.2.23 §5.1.2.23 ssn-system:OperatingProperty

**IRI:** http://www.w3.org/ns/ssn/systems/OperatingProperty

**a OWL Class**

*Operating Property* - An identifiable characteristic that represents how the `System` (§4.9.2.4) operates under the specified `Conditions` (§5.1.2.3). May describe power ranges, power sources, standard configurations, attachments and the like.

| Sub class of  | §4.6.2.4 ssn:Property                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions  | ***inverse Of*** §5.1.2.22 ssn-system:hasOperatingProperty ***ONLY*** §5.1.2.21 ssn-system:OperatingRange ***inverse Of*** §5.1.2.22 ssn-system:hasOperatingProperty ***MIN 1*** |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.24 §5.1.2.24 ssn-system:MaintenanceSchedule

**IRI:** http://www.w3.org/ns/ssn/systems/MaintenanceSchedule

**a OWL Class**

*Maintenance Schedule* - Schedule of maintenance for a `System` (§4.9.2.4) in the specified `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.23 ssn-system:OperatingProperty |
| ------------- | ------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                     |

[Back to module overview and examples (§5.1)]

##### 5.1.2.25 §5.1.2.25 ssn-system:OperatingPowerRange

**IRI:** http://www.w3.org/ns/ssn/systems/OperatingPowerRange

**a OWL Class**

*Operating Power Range* - Power range in which `System` (§4.9.2.4) is expected to operate in the specified `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.23 ssn-system:OperatingProperty |
| ------------- | ------------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                     |

[Back to module overview and examples (§5.1)]

##### 5.1.2.26 §5.1.2.26 ssn-system:hasSurvivalRange

**IRI:** http://www.w3.org/ns/ssn/systems/hasSurvivalRange

**a OWL Object Property**

*has survival range* - Relation from a `System` (§4.9.2.4) to a `SurvivalRange` (§5.1.2.27).

| Sub property of | §4.6.2.5 ssn:hasProperty      |
| --------------- | ----------------------------------------------------------------------- |
| is Defined By   | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/) |

[Back to module overview and examples (§5.1)]

##### 5.1.2.27 §5.1.2.27 ssn-system:SurvivalRange

**IRI:** http://www.w3.org/ns/ssn/systems/SurvivalRange

**a OWL Class**

*Survival Range* - Describes `SurvivalProperties` (§5.1.2.29) of a `System` (§4.9.2.4) under some specified `Conditions` (§5.1.2.3). For example, the lifetime of a System under a specified temperature range.
In the absence of `SurvivalProperties` (§5.1.2.29), simply describes the `Conditions` (§5.1.2.3) a `System` (§4.9.2.4) can be exposed to without damage. For example, the temperature range a System can withstand before being considered damaged.
The System continues to operate as defined using `SystemCapability` (§5.1.2.5). If, however, the SurvivalRange is violated, the `System` (§4.9.2.4) is 'damaged' and `SystemCapability` (§5.1.2.5) specifications may no longer hold.

| Sub class of  | §4.6.2.4 ssn:Property                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions  | §5.1.2.28 ssn-system:hasSurvivalProperty ***ONLY*** §5.1.2.29 ssn-system:SurvivalProperty §5.1.2.2 ssn-system:inCondition ***ONLY*** §5.1.2.3 ssn-system:Condition §5.1.2.2 ssn-system:inCondition ***MIN 1*** ***inverse Of*** §5.1.2.26 ssn-system:hasSurvivalRange ***ONLY*** §4.9.2.4 ssn:System |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.28 §5.1.2.28 ssn-system:hasSurvivalProperty

**IRI:** http://www.w3.org/ns/ssn/systems/hasSurvivalProperty

**a OWL Object Property**

*has survival property* - Relation from a `SurvivalRange` (§5.1.2.27) of a `System` (§4.9.2.4) to a `SurvivalProperty` (§5.1.2.29) describing the survival range of the `System` (§4.9.2.4).

| Sub property of | §4.6.2.5 ssn:hasProperty      |
| --------------- | ----------------------------------------------------------------------- |
| is Defined By   | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/) |

[Back to module overview and examples (§5.1)]

##### 5.1.2.29 §5.1.2.29 ssn-system:SurvivalProperty

**IRI:** http://www.w3.org/ns/ssn/systems/SurvivalProperty

**a OWL Class**

*Survival Property* - An identifiable characteristic that represents the extent of the `System` (§4.9.2.4)'s useful life under the specified `Conditions` (§5.1.2.3). May describe for example total battery life or number of recharges, or, for `Sensors` (§4.3.2.5) that are used only a fixed number of times, the number of `Observations` (§4.3.2.2) that can be made before the sensing capability is depleted.

| Sub class of  | §4.6.2.4 ssn:Property                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Restrictions  | ***inverse Of*** §5.1.2.28 ssn-system:hasSurvivalProperty ***ONLY*** §5.1.2.27 ssn-system:SurvivalRange ***inverse Of*** §5.1.2.28 ssn-system:hasSurvivalProperty ***MIN 1*** |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                                                                                                                                  |

[Back to module overview and examples (§5.1)]

##### 5.1.2.30 §5.1.2.30 ssn-system:SystemLifetime

**IRI:** http://www.w3.org/ns/ssn/systems/SystemLifetime

**a OWL Class**

*System Lifetime* - Total useful life of a `System` (§4.9.2.4) (expressed as total life since manufacture, time in use, number of operations, etc.) in the specified `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.29 ssn-system:SurvivalProperty |
| ------------- | ----------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                   |

[Back to module overview and examples (§5.1)]

##### 5.1.2.31 §5.1.2.31 ssn-system:BatteryLifetime

**IRI:** http://www.w3.org/ns/ssn/systems/BatteryLifetime

**a OWL Class**

*Battery Lifetime* - Total useful life of a `System` (§4.9.2.4)'s battery in the specified `Conditions` (§5.1.2.3).

| Sub class of  | §5.1.2.29 ssn-system:SurvivalProperty |
| ------------- | ----------------------------------------------------------------------------------------- |
| is Defined By | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/)                   |

[Back to module overview and examples (§5.1)]

##### 5.1.2.32 §5.1.2.32 ssn-system:qualityOfObservation

**IRI:** http://www.w3.org/ns/ssn/systems/qualityOfObservation

**a OWL Object Property**

*quality of observation* - Relation linking an `Observation` (§4.3.2.2) to the adjudged quality of the `Result` (§4.7.2.1). This is complementary to the `SystemCapability` (§5.1.2.5) information recorded for the `Sensor` (§4.3.2.5) that made the `Observation` (§4.3.2.2).

| Sub property of | §4.6.2.5 ssn:hasProperty      |
| --------------- | ----------------------------------------------------------------------- |
| is Defined By   | [http://www.w3.org/ns/ssn/systems/](https://www.w3.org/ns/ssn/systems/) |

[Back to module overview and examples (§5.1)]

### 5.2 Sample Relations Module

*This section is non-normative.*

Samples are often related to other samples, by sub-sampling, topological relationships (stations along a traverse, pixels within an image, probe spots on a polished section, specimens retrieved within a borehole) or as parts of sample processing
chains (crushing, splitting, dissecting, disolving). There are an essentially unlimited set of relationships between samples, so the nature of the relationship has its own class. This section describes a flexible model to describe such
relationships between samples. The model is based on the [QualifiedRelation pattern](http://patterns.dataincubator.org/book/qualified-relation.html).

The namespace for Sample relationships terms is http://www.w3.org/ns/sosa/sampling/

The suggested prefix for the sample relationships namespace is sampling

An [ontology graph for this is available](https://www.w3.org/ns/sosa/sampling/).

The following figure provides an overview on the classes and properties that are specifically related to modeling Sample relationships.

[![Sample relationships](https://www.w3.org/TR/vocab-ssn/images/sample-relationships.png)](https://www.w3.org/TR/vocab-ssn/images/sample-relationships.png)

*Figure 21 Model of sample relationships*

#### 5.2.1 Sample Relationships Specification

This section introduces the following classes and properties:

§5.2.1.1 sampling:RelationshipNature, §5.2.1.3 sampling:hasSampleRelationship, §5.2.1.4 sampling:natureOfRelationship, §5.2.1.5 sampling:relatedSample

##### 5.2.1.1 §5.2.1.1 sampling:RelationshipNature

**IRI:** http://www.w3.org/ns/sosa/sampling/RelationshipNature

**a OWL Class**

*Nature of relationship (between samples)* - Members of this class indicate the nature of a relationship between two `Samples.` (§4.5.2.1)

| Sub class of  | skos:Concept                                                                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Examples      | Adjacent flight-line Females Juveniles Males Pixel within image or scene Probe spot on polished specimen Specimen taken from borehole Split of core sample Station along a traverse Sub-sample with grain size smaller than specified seive mesh |
| is Defined By | [http://www.w3.org/ns/sosa/sampling/](https://www.w3.org/ns/sosa/sampling/)                                                                                                                              |

[Back to module overview (§5.2)]

##### 5.2.1.2 §5.2.1.2 sampling:SampleRelationship

**IRI:** http://www.w3.org/ns/sosa/sampling/SampleRelationship

**a OWL Class**

*Sample relationship* - Members of this class represent a relationship between a `Sample` (§4.5.2.1) and another.

| is Defined By | [http://www.w3.org/ns/sosa/sampling/](https://www.w3.org/ns/sosa/sampling/) |
| ------------- | --------------------------------------------------------------------------- |

[Back to module overview (§5.2)]

##### 5.2.1.3 §5.2.1.3 sampling:hasSampleRelationship

**IRI:** http://www.w3.org/ns/sosa/sampling/hasSampleRelationship

**a OWL Object Property**

*has sample relationship* - Links a sample to a `Sample Relationship` (§5.2.1.2) (which links to a related `Sample` (§4.5.2.1)).

| Domain Includes | §4.5.2.1 sosa:Sample                             |
| --------------- | -------------------------------------------------------------------------------------- |
| Range Includes  | §5.2.1.2 sampling:SampleRelationship |
| is Defined By   | [http://www.w3.org/ns/sosa/sampling/](https://www.w3.org/ns/sosa/sampling/)            |

[Back to module overview (§5.2)]

##### 5.2.1.4 §5.2.1.4 sampling:natureOfRelationship

**IRI:** http://www.w3.org/ns/sosa/sampling/natureOfRelationship

**a OWL Object Property**

*nature of (sample) relationship* - Links a `Sample Relationship` (§5.2.1.2) to an indication of the nature of the relationship.

| Domain Includes | §5.2.1.2 sampling:SampleRelationship |
| --------------- | -------------------------------------------------------------------------------------- |
| Range Includes  | sampling:SampleRelationship (§5.2.1.1) |
| is Defined By   | [http://www.w3.org/ns/sosa/sampling/](https://www.w3.org/ns/sosa/sampling/)            |

[Back to module overview (§5.2)]

##### 5.2.1.5 §5.2.1.5 sampling:relatedSample

**IRI:** http://www.w3.org/ns/sosa/sampling/relatedSample

**a OWL Object Property**

*related sample* - Links a `Sample Relationship` (§5.2.1.2) to the related `Sample.` (§4.5.2.1)

| Domain Includes | §5.2.1.2 sampling:SampleRelationship |
| --------------- | -------------------------------------------------------------------------------------- |
| Range Includes  | §4.5.2.1 sosa:Sample                             |
| is Defined By   | [http://www.w3.org/ns/sosa/sampling/](https://www.w3.org/ns/sosa/sampling/)            |

[Back to module overview (§5.2)]

## 6. Vertical Segmentation

This section introduces the specifications for the vertical segmentation modules that align SOSA and SSN to a variety of related ontologies and specifications.

### 6.1 Dolce-Ultralite Alignment Module

*This section is non-normative.*

This section introduces the alignment of SSN to the DOLCE UltraLite upper ontology (DUL) which is the core dependency of the previous version of SSN. This serves to axiomatically clarify the intended meaning of SSN terms and will assist SSN
users wishing to interoperate with other DUL-aligned ontologies. It is also imported in the SSNX alignment module that aligns SSN to the previous version of SSN. Note, however, that the DUL alignment can be used independently to align
SSN with more generic concepts/properties of DUL.

The DUL alignment, known as "ssn-dul" is available at [http://www.w3.org/ns/ssn/dul](https://www.w3.org/ns/ssn/dul).

#### 6.1.1 Namespaces

*This section is non-normative.*

The following namespace prefixes are used in the alignment to SOSA and SSN

| Prefix | Namespace                                                                                                       |
| ------ | --------------------------------------------------------------------------------------------------------------- |
| sosa:  | [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/)                                                       |
| ssn:   | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                                                         |
| dul:   | [http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#](http://www.ontologydesignpatterns.org/ont/dul/DUL.owl) |

#### 6.1.2 Class Alignments

*This section is non-normative.*

The following classes in SOSA and SSN can be aligned via a subclass relation as follows.

| sosa:Procedure   | subclass of | dul:Method  |
| ---------------- | ----------- | ----------- |
| sosa:Sensor      | subclass of | dul:Object  |
| sosa:Observation | subclass of | dul:Event   |
| ssn:Property     | subclass of | dul:Quality |
| ssn:Stimulus     | subclass of | dul:Event   |
| ssn:System       | subclass of | dul:Object  |
| sosa:Platform    | subclass of | dul:Object  |
| ssn:Deployment   | subclass of | dul:Event   |

For more complex alignments, the axiomatic alignments are defined as follows.

| sosa:FeatureOfInterest                                                    | subclass of | owl:unionOf ( dul:Event dul:Object dul:InformationEntity) |
| ------------------------------------------------------------------------- | ----------- | --------------------------------------------------------- |
| sosa:Result                                                               | subclass of | owl:unionOf ( dul:Region dul:Object )                     |
| (not (oldssn:Observation)) and (old-ssn:observationResult some owl:Thing) | subclass of | sosa:Observation                                          |

#### 6.1.3 Property Alignments

*This section is non-normative.*

Additional alignments from SOSA/SSN to DUL properties are defined as follows.

| ssn:hasProperty        | sub-property of | dul:hasQuality     |
| ---------------------- | --------------- | ------------------ |
| ssn:isPropertyOf       | sub-property of | dul:isQualityOf    |
| sosa:hosts             | sub-property of | dul:isLocationOf   |
| sosa:isHostedBy        | sub-property of | dul:hasLocation    |
| ssn:implementedBy      | sub-property of | dul:describes      |
| ssn:implements         | sub-property of | dul:isDescribedBy  |
| sosa:usedProcedure     | sub-property of | dul:hasParticipant |
| sosa:madeObservation   | sub-property of | dul:associatedWith |
| sosa:madeBySensor      | sub-property of | dul:associatedWith |
| sosa:observedProperty  | sub-property of | dul:associatedWith |
| sosa:hasResult         | sub-property of | dul:associatedWith |
| sosa:phenomenonTime    | sub-property of | dul:hasRegion      |
| ssn:hasSubSystem       | sub-property of | dul:hasPart        |
| ssn:deployedOnPlatform | sub-property of | dul:associatedWith |
| ssn:deployedSystem     | sub-property of | dul:associatedWith |
| ssn:hasDeployment      | sub-property of | dul:associatedWith |
| ssn:inDeployment       | sub-property of | dul:associatedWith |

### 6.2 SSNX Alignment Module

*This section is non-normative.*

This section formally relates the SSN ontology to the previous version of SSN that was published by the SSN-XG ("old SSN"). This may be useful for backward-compatibility and transition purposes. While the namespaces for SSN and DUL have changed
since the SSN-XG first published the old SSN, the SSN alignment, known as "SSN-SSNX" is available at [http://www.w3.org/2017/01/ssn-ssnx/](https://www.w3.org/2017/01/ssn-ssnx/). Note that SSN-SSNX imports SSN-DUL.

#### 6.2.1 Namespaces

*This section is non-normative.*

The following namespace prefixes are used in the alignment to SOSA and SSN

| Prefix  | Namespace                                                               |
| ------- | ----------------------------------------------------------------------- |
| sosa:   | [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/)               |
| ssn:    | [http://www.w3.org/ns/ssn/](https://www.w3.org/ns/ssn/)                 |
| oldssn: | [http://purl.oclc.org/NET/ssnx/ssn#](http://purl.oclc.org/NET/ssnx/ssn) |

#### 6.2.2 Class Alignments

*This section is non-normative.*

The primary classes from SSN-XG have direct equivalent classes in SOSA and SSN as shown below.

| oldssn:FeatureOfInterest   | equivalent class | sosa:FeatureOfInterest         |
| -------------------------- | ---------------- | ------------------------------ |
| oldssn:Property            | equivalent class | ssn:Property                   |
| oldssn:System              | equivalent class | ssn:System                     |
| oldssn:Platform            | equivalent class | sosa:Platform                  |
| oldssn:Input               | equivalent class | ssn:Input                      |
| oldssn:Output              | equivalent class | ssn:Output                     |
| oldssn:Stimulus            | equivalent class | ssn:Stimulus                   |
| oldssn:MeasurementRange    | equivalent class | ssn-system:MeasurementRange    |
| oldssn:Sensor              | equivalent class | sosa:Sensor                    |
| oldssn:Condition           | equivalent class | ssn-system:Condition           |
| oldssn:Precision           | equivalent class | ssn-system:Precision           |
| oldssn:Sensitivity         | equivalent class | ssn-system:Sensitivity         |
| oldssn:OperatingProperty   | equivalent class | ssn-system:OperatingProperty   |
| oldssn:MaintenanceSchedule | equivalent class | ssn-system:MaintenanceSchedule |
| oldssn:OperatingPowerRange | equivalent class | ssn-system:OperatingPowerRange |
| oldssn:SurvivalProperty    | equivalent class | ssn-system:SurvivalProperty    |
| oldssn:BatteryLifetime     | equivalent class | ssn-system:BatteryLifetime     |
| oldssn:SystemLifetime      | equivalent class | ssn-system:SystemLifetime      |

The following classes in SOSA and SSN are interpreted as superclasses of the corresponding ones in SSN-XG.

| oldssn:Device              | subclass of | sosa:Platform; ssn:System |
| -------------------------- | ----------- | ------------------------- |
| oldssn:Sensing             | subclass of | sosa:Procedure            |
| oldssn:ObservationValue    | subclass of | sosa:Result               |
| oldssn:MeasurementProperty | subclass of | ssn-system:SystemProperty |
| oldssn:Accuracy            | subclass of | ssn-system:Accuracy       |
| oldssn:DetectionLimit      | subclass of | ssn-system:DetectionLimit |
| oldssn:Drift               | subclass of | ssn-system:Drift          |
| oldssn:Frequency           | subclass of | ssn-system:Frequency      |
| oldssn:Latency             | subclass of | ssn-system:Latency        |
| oldssn:Resolution          | subclass of | ssn-system:Resolution     |
| oldssn:ResponseTime        | subclass of | ssn-system:ResponseTime   |
| oldssn:Selectivity         | subclass of | ssn-system:Selectivity    |

The more complex aligments of SSN-XG classes are expressed as combinations of axiomatic statements as follows.

| oldssn:Process               | equivalent class | sosa:Procedure                                                                                                                                                |
| ---------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:hasOutput ; owl:someValuesFrom oldssn:Output ]                                                                    |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:hasInput ; owl:allValuesFrom oldssn:Input ]                                                                       |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:hasOutput ; owl:allValuesFrom oldssn:Output ]                                                                     |
| oldssn:Observation           | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:featureOfInterest ; owl:allValuesFrom oldssn:FeatureOfInterest ]                                                  |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:observationResult ; owl:allValuesFrom oldssn:SensorOutput ]                                                       |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:observedBy ; owl:allValuesFrom oldssn:Sensor ]                                                                    |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:observedProperty ; owl:allValuesFrom oldssn:Property ]                                                            |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:sensingMethodUsed ; owl:allValuesFrom oldssn:Sensing ]                                                            |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:observationResultTime ; owl:minCardinality "0"^^xsd:nonNegativeInteger ]                                          |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:observationSamplingTime ; owl:minCardinality "0"^^xsd:nonNegativeInteger ]                                        |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:qualityOfObservation ; owl:minCardinality "0"^^xsd:nonNegativeInteger ]                                           |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:featureOfInterest ; owl:qualifiedCardinality "1"^^xsd:nonNegativeInteger ; owl:onClass oldssn:FeatureOfInterest ] |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:observedBy ; owl:qualifiedCardinality "1"^^xsd:nonNegativeInteger ; owl:onClass oldssn:Sensor ]                   |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:observedProperty ; owl:qualifiedCardinality "1"^^xsd:nonNegativeInteger ; owl:onClass oldssn:Property ]           |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:sensingMethodUsed ; owl:qualifiedCardinality "1"^^xsd:nonNegativeInteger ; owl:onClass oldssn:Sensing ]           |
| oldssn:SensorOutput          | subclass of      | sosa:Result                                                                                                                                                   |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:hasValue ; owl:someValuesFrom oldssn:ObservationValue ]                                                           |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:isProducedBy ; owl:someValuesFrom oldssn:Sensor ]                                                                 |
| oldssn:ObservationValue      | subclass of      | sosa:Result                                                                                                                                                   |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty dul:isRegionFor ; owl:someValuesFrom oldssn:SensorOutput ]                                                               |
| oldssn:Deployment            | equivalent class | ssn:Deployment                                                                                                                                                |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:deployedOnPlatform ; owl:allValuesFrom oldssn:Platform ]                                                          |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:deployedSystem ; owl:allValuesFrom oldssn:System ]                                                                |
| oldssn:MeasurementCapability | subclass of      | ssn-system:SystemCapability                                                                                                                                   |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:forProperty ; owl:allValuesFrom oldssn:Property ]                                                                 |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:hasMeasurementProperty ; owl:allValuesFrom oldssn:MeasurementProperty ]                                           |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:inCondition ; owl:allValuesFrom oldssn:Condition ]                                                                |
| oldssn:OperatingRange        | equivalent class | ssn-system:OperatingRange                                                                                                                                     |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:hasOperatingProperty ; owl:allValuesFrom oldssn:OperatingProperty ]                                               |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:inCondition ; owl:allValuesFrom oldssn:Condition ]                                                                |
| oldssn:SurvivalRange         | equivalent class | ssn-system:SurvivalRange                                                                                                                                      |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:hasSurvivalProperty ; owl:allValuesFrom oldssn:SurvivalProperty ]                                                 |
|                              | subclass of      | [ a owl:Restriction ; owl:onProperty oldssn:inCondition ; owl:allValuesFrom oldssn:Condition ]                                                                |

#### 6.2.3 Property Alignments

*This section is non-normative.*

The following properties from SSN-XG have direct equivalent properties in SOSA and SSN.

| oldssn:hasProperty             | equivalent property | ssn:hasProperty                 |
| ------------------------------ | ------------------- | ------------------------------- |
| oldssn:isPropertyOf            | equivalent property | ssn:isPropertyOf                |
| oldssn:attachedSystem          | equivalent property | sosa:hosts                      |
| oldssn:onPlatform              | equivalent property | sosa:isHostedBy                 |
| oldssn:hasInput                | equivalent property | ssn:hasInput                    |
| oldssn:hasOutput               | equivalent property | ssn:hasOutput                   |
| oldssn:implements              | equivalent property | ssn:implements                  |
| oldssn:implementedBy           | equivalent property | ssn:implementedBy               |
| oldssn:sensingMethodUsed       | equivalent property | sosa:usedProcedure              |
| oldssn:featureOfInterest       | equivalent property | sosa:hasFeatureOfInterest       |
| oldssn:madeObservation         | equivalent property | sosa:madeObservation            |
| oldssn:observedBy              | equivalent property | sosa:madeBySensor               |
| oldssn:observedProperty        | equivalent property | sosa:observedProperty           |
| oldssn:detects                 | equivalent property | ssn:detects                     |
| oldssn:isProxyFor              | equivalent property | ssn:isProxyFor                  |
| oldssn:hasValue                | equivalent property | sosa:hasResult                  |
| oldssn:isProducedBy            | equivalent property | sosa:isResultOf                 |
| oldssn:observationResult       | equivalent property | sosa:hasResult                  |
| oldssn:observationSamplingTime | equivalent property | sosa:phenomenonTime             |
| oldssn:qualityOfObservation    | equivalent property | ssn-system:qualityOfObservation |
| oldssn:hasSubSystem            | equivalent property | ssn:hasSubSystem                |
| oldssn:deployedOnPlatform      | equivalent property | ssn:deployedOnPlatform          |
| oldssn:deployedSystem          | equivalent property | ssn:deployedSystem              |
| oldssn:hasDeployment           | equivalent property | ssn:hasDeployment               |
| oldssn:inDeployment            | equivalent property | ssn:inDeployment                |
| oldssn:forProperty             | equivalent property | ssn:forProperty                 |
| oldssn:inCondition             | equivalent property | ssn-system:inCondition          |
| oldssn:hasSurvivalRange        | equivalent property | ssn-system:hasSurvivalRange     |
| oldssn:hasSurvivalProperty     | equivalent property | ssn-system:hasSurvivalProperty  |
| oldssn:hasOperatingRange       | equivalent property | ssn-system:hasOperatingRange    |
| oldssn:hasOperatingProperty    | equivalent property | ssn-system:hasOperatingProperty |

Additional alignments from SSG-XG properties to SOSA and SSN are defined as follows.

| oldssn:hasMeasurementCapability | sub-property of | ssn-system:hasSystemCapability |
| ------------------------------- | --------------- | ------------------------------ |
| oldssn:hasMeasurementProperty   | sub-property of | ssn-system:hasSystemProperty   |
| oldssn:hasSurvivalRange         | sub-property of | sosa:hasResult                 |

The more complicated alignments are presented in combination with the property-chain axioms as follows.

| oldssn:observes | equivalent property  | sosa:observes                                          |
| --------------- | -------------------- | ------------------------------------------------------ |
|                 | property chain axiom | ( oldssn:hasMeasurementCapability oldssn:forProperty ) |
|                 | property chain axiom | ( oldssn:madeObservation oldssn:observedProperty )     |

### 6.3 O&M Alignment Module

This section introduces the alignment of SOSA/SSN to OGC Observations and Measurements [OandM] (also known as ISO 19156:2011).

The XML implementation of O&M [OMXML] is used for the payload for Sensor Observation Services, of which there are many operational deployments. Integration of these with observation
data formalized using SOSA and SSN is highly desirable, and would be expected to significantly enrich the set of resources represented using SOSA/SSN. The alignment presented here provides a basis for transforming OM-XML data into RDF
resources or OWL individuals according to the SOSA/SSN ontologies.

#### 6.3.1 Identifying the UML elements

O&M is specified as a UML model, following the patterns specified in ISO 19109 Geographic Information - Rules for Application Schema [ISO-19109]. This means that the classes
represent concepts from the application domain, so can be approximately equated with classes in an ontology.

An OWL implementation of O&M may be generated by explicit translation of the UML following rules specified in [ISO-19150-2] - see [OM-Heavy].
This translation generates an RDF entity denoted by a URI for every class, class attribute, and association-role from the original O&M UML model. The form of the URIs is also specified in [ISO-19150-2],
and appear explicitly in the [official OWL implementation of ISO 19156 (O&M) maintained by the ISO/TC 211 Group on Ontology Management](https://github.com/ISO-TC211/GOM/tree/master/isotc211_GOM_harmonizedOntology/19156/2011). These URIs are therefore convenient identifiers for elements of the O&M in a formal alignment.

The explicit translation from the UML model comes at the cost of a large set of dependencies on similar OWL translations of other UML models from the ISO 19100 series standards. Furthermore, the ontology structure reflects artefacts of
the UML-style of modeling. This implementation *may* introduce entailments that are inconsistent with SOSA/SSN (though no inconsistencies have been identified yet) so it is important to understand that use of these URIs here are principally intended to denote the original
UML classes and properties, rather than this OWL implementation.

NOTE: In response to the complexity of the explicit translation, a handcrafted version in more idiomatic OWL, without the dependencies, is also available [OM-Lite].

NOTE: At time of writing, the ISO-specified URIs do not de-reference. However, ISO/TC 211 are currently developing a publication system to enable this and thus the use of these URIs as Linked Data.

#### 6.3.2 Namespaces

The following namespace prefixes are used in the alignment to SOSA.

| Prefix        | Namespace                                                       |
| ------------- | --------------------------------------------------------------- |
| sosa:         | [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/)       |
| sosa-om:      | [http://www.w3.org/ns/sosa/om#](https://www.w3.org/ns/sosa/om#) |
| iso19156-gfi: | http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#   |
| iso19156-om:  | http://def.isotc211.org/iso19156/2011/Observation#              |
| iso19156-sf:  | http://def.isotc211.org/iso19156/2011/SamplingFeature#          |
| iso19156-sfs: | http://def.isotc211.org/iso19156/2011/SpatialSamplingFeature#   |
| iso19156-sp:  | http://def.isotc211.org/iso19156/2011/Specimen#                 |

#### 6.3.3 Utility Classes

Three utility classes are defined locally to support the formalization of the alignment.

| sosa-om:ActuationProcedure   | Actuation procedures or recipes                                  |
| ---------------------------- | ---------------------------------------------------------------- |
| sosa-om:ObservationProcedure | Observation procedures or recipes                                |
| sosa-om:SamplingProcedure    | Sampling, sample preparation or processing procedures or recipes |

#### 6.3.4 Class Alignments

The primary classes from [OandM] have direct equivalents in SOSA classes supplemented by the utility classes described above, as follows.

| iso19156-om:OM_Observation     | equivalent class | sosa:Observation                                         |
| ------------------------------ | ---------------- | -------------------------------------------------------- |
| iso19156-om:OM_Process         | equivalent class | Union of ( sosa:Sensor or sosa-om:ObservationProcedure ) |
| iso19156-sf:SF_SamplingFeature | equivalent class | sosa:Sample                                              |
| iso19156-sf:SF_Process         | equivalent class | Union of ( sosa:Sampler or sosa-om:SamplingProcedure )   |

Additional alignments from SOSA/SSN classes to O&M classes are as follows.

| iso19156_sp:PreparationStep | subclass of | sosa:Sampling |
| --------------------------- | ----------- | ------------- |

iso19156_sp:PreparationStep is a subclass since the act of Sampling applies to all sample types, not only physical specimens.

| sosa:FeatureOfInterest | subclass of | iso19156_gfi:GFI_DomainFeature |
| ---------------------- | ----------- | ------------------------------ |

where iso19156_gfi:GFI_DomainFeature has the definition:

*The class GFI_DomainFeature represents 'real-world' features
which are the ultimate subject of an observation campaign, i.e.
the features from an application domain that are not artefacts
of the observation process (sampling features).*

sosa:FeatureOfInterest is a subclass of iso19156_gfi:GFI_DomainFeature since not all domain features are subjects of observation.

| sosa:Actuator | subclass of | iso19156_gfi:GFI_Feature |
| ------------- | ----------- | ------------------------ |
| sosa:Platform | subclass of | iso19156_gfi:GFI_Feature |

where iso19156_gfi:GFI_Feature has the definition

*The class GFI_Feature represents the set of all classes which
are feature types. In an implementation this abstract class
shall be substituted by a concrete class representing a feature
type from an application schema associated with a domain of
discourse (ISO 19109, ISO 19101).*

#### 6.3.5 Property Alignments

The following properties from [OandM] have direct equivalents in SOSA properties.

| iso19156-om:OM_Observation.featureOfInterest  | equivalent property | sosa:hasFeatureOfInterest |
| --------------------------------------------- | ------------------- | ------------------------- |
| iso19156-om:OM_Observation.observedProperty   | equivalent property | sosa:observedProperty     |
| iso19156-om:OM_Observation.phenomenonTime     | equivalent property | sosa:phenomenonTime       |
| iso19156-sf:SF_SamplingFeature.sampledFeature | equivalent property | sosa:isSampleOf           |

Additional alignments from O&M properties to SOSA are as follows.

| iso19156-om:OM_Observation.procedure      | sub-property of | sosa:usedProcedure |
| ----------------------------------------- | --------------- | ------------------ |
| iso19156-sp:SF_Specimen.samplingMethod    | sub-property of | sosa:usedProcedure |
| iso19156-om:OM_Observation.result         | sub-property of | sosa:hasResult     |
| iso19156-om:OM_Observation.resultTime     | sub-property of | sosa:resultTime    |
| iso19156-sp:SF_Specimen.samplingTime      | sub-property of | sosa:resultTime    |
| iso19156-sp:PreparationStep.time          | sub-property of | sosa:resultTime    |
| iso19156-sp:SF_Specimen.processingDetails | sub-property of | sosa:isResultOf    |

These are modeled as sub-properties because sosa:usedProcedure, sosa:hasResult, sosa:isResultOf and sosa:resultTime applies to actuation, observation or sampling activities.

| iso19156-sfs:SF_SpatialSamplingFeature.hostedProcedure | sub-property of | sosa:hosts |
| ------------------------------------------------------ | --------------- | ---------- |

This is modeled as a sub-property because the domain of iso19156-sfs:SF_SpatialSamplingFeature.hostedProcedure is a spatial sampling feature, such as a station, rather than a more general platform.

An RDF file containing a [graph corresponding to this alignment is available](https://www.w3.org/ns/sosa/om).

### 6.4 OBOE Alignment Module

*This section is non-normative.*

This section introduces the alignment of SOSA to [OBOE](https://github.com/NCEAS/oboe/).

OBOE, the Extensible Observation Ontology, is used within the biodiversity community for semantic representation of observation data. The ontology is composed of multiple modules. The core observation elements are in the module OBOE-core.

#### 6.4.1 Namespaces

The following namespace prefixes are used in the alignment to SOSA.

| Prefix | Namespace                                                 |
| ------ | --------------------------------------------------------- |
| sosa:  | [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/) |
| oboe:  | <http://ecoinformatics.org/oboe/oboe.1.0/oboe-core.owl#>  |

#### 6.4.2 Class Alignments

*This section is non-normative.*

An oboe:Observation is composed of a collection of oboe:Measurements with the same feature of interest. Each oboe:Measurement concerns a distinct observed-property ("characteristic") and uses a distinct procedure ("protocol"). We therefore
choose to align sosa:Observation with oboe:Measurement.

[![OBOE core classes](https://www.w3.org/TR/vocab-ssn/images/OBOE-core.png)](https://www.w3.org/TR/vocab-ssn/images/OBOE-core.png) [![SOSA Observation](https://www.w3.org/TR/vocab-ssn/images/SOSA-obs-core.png)](https://www.w3.org/TR/vocab-ssn/images/SOSA-obs-core.png)

*Figure 22 Core classes from OBOE alongside the SOSA observation model.*

The primary classes from [OBOE] are aligned with SOSA classes as follows.

| oboe:Measurement    | subclass of      | sosa:Observation        |
| ------------------- | ---------------- | ----------------------- |
| oboe:Characteristic | equivalent class | sosa:ObservableProperty |
| oboe:Protocol       | equivalent class | sosa:Procedure          |

The class oboe:Entity appears in OBOE as the range of the oboe:ofEntity and oboe:hasValue properties, so we interpret it as a general superclass.

| sosa:FeatureOfInterest | subclass of | oboe:Entity |
| ---------------------- | ----------- | ----------- |
| sosa:Result            | subclass of | oboe:Entity |

#### 6.4.3 Property Alignments

*This section is non-normative.*

The following properties from [OBOE] may be directly aligned with SOSA properties.

| oboe:ofCharacteristic | equivalent property | sosa:observedProperty |
| --------------------- | ------------------- | --------------------- |
| oboe:hasValue         | equivalent property | sosa:hasResult        |
| oboe:usesProtocol     | equivalent property | sosa:usedProcedure    |
| oboe:usesMethod       | equivalent property | sosa:usedProcedure    |

oboe:hasValue, oboe:usesProtocol and oboe:usesMethod are sub-properties of the corresponding SOSA properties which apply to actuation and sampling as well as observation.

The feature of interest is linked to the oboe:Observation that contains a oboe:Measurement, rather than to the oboe:Measurement directly, so a property-chain axiom is required to express the alignment.

| sosa:hasFeatureOfInterest | property-chain axiom | [oboe:measurementFor, oboe:ofEntity] |
| ------------------------- | -------------------- | ------------------------------------ |

The properties oboe:hasMeasurement and its inverse oboe:measurementFor link an oboe:Observation to its member oboe:Measurements. These could be modeled as sub-properties related to rdfs:member and its inverse as follows.

| oboe:hasMeasurement | sub-property of | rdfs:member                   |
| ------------------- | --------------- | ----------------------------- |
| oboe:measurementFor | sub-property of | [ owl:inverseOf rdfs:member ] |

An RDF file containing a [graph corresponding to this alignment is available](https://www.w3.org/ns/sosa/oboe).

### 6.5 PROV Alignment Module

*This section is non-normative.*

This section introduces the alignment of SOSA to W3C PROV ([prov-overview], [prov-dm],
[prov-o]).

The underlying structure of PROV is based around a process-flow model, with three base classes: [Entity](https://www.w3.org/TR/prov-o/#Entity), which is the class of physical, digital, conceptual, or other kinds of things with some
fixed aspects; [Activity](https://www.w3.org/TR/prov-o/#Activity), which is the class of things that occur over a period of time and act upon or with entities, and it may include consuming, processing, transforming, modifying,
relocating, using, or generating entities; and [Agent](https://www.w3.org/TR/prov-o/#Agent), the class of things that bear some form of responsibility for an activity taking place, for the existence of an entity, or for another
agent's activity.

[![PROV-O](https://www.w3.org/TR/vocab-ssn/images/prov-o.png)](https://www.w3.org/TR/vocab-ssn/images/prov-o.png) [![Observation PROV-O](https://www.w3.org/TR/vocab-ssn/images/observation-prov.png)](https://www.w3.org/TR/vocab-ssn/images/observation-prov.png) [![Actuation PROV-O](https://www.w3.org/TR/vocab-ssn/images/actuation-prov.png)](https://www.w3.org/TR/vocab-ssn/images/actuation-prov.png) [![Sampling PROV-O](https://www.w3.org/TR/vocab-ssn/images/sampling-prov.png)](https://www.w3.org/TR/vocab-ssn/images/sampling-prov.png)

*Figure 23 Core PROV classes and some of the properties that relate them, shown alongside the core SOSA structure for observation, actuation and sampling. Classes generally aligned with prov:Entity in yellow ellipses; with prov:Activity in purple boxes; with prov:Agent in orange boxes.*

The SOSA/SSN ontologies conceive observations, actuations, and acts of sampling as activities or events, that results in information being produced, or a change in the world, or the production or transformation of a sample. Thus, an alignment
of SOSA to PROV is natural. Compton et al. [SSN-PROV] and Cox [OM-Lite] have previously described alignments of the SSNX and
O&M models with [prov-o]. The alignment here is based on that work, also extended to consider actuation.

#### 6.5.1 Namespaces

*This section is non-normative.*

The following namespace prefixes are used in the alignment of SOSA to PROV.

| Prefix | Namespace                                                       |
| ------ | --------------------------------------------------------------- |
| sosa:  | [http://www.w3.org/ns/sosa/](https://www.w3.org/ns/sosa/)       |
| prov:  | [http://www.w3.org/ns/prov#](https://www.w3.org/ns/prov-o)      |
| sp:    | [http://www.w3.org/ns/sosa/prov/](https://www.w3.org/ns/prov-o) |

#### 6.5.2 Class Alignments

*This section is non-normative.*

The primary classes from SOSA are aligned with the PROV classes as follows.

1\. Acts of Observation, Actuation and Sampling are each kinds of Activity, thus:

| sosa:Observation | subclass of | prov:Activity |
| ---------------- | ----------- | ------------- |
| sosa:Actuation   |             |               |
| sosa:Sampling    |             |               |

2\. Sensors, Actuators and Samplers are entities that are responsible for the corresponding activities, thus:

| sosa:Sensor   | subclass of | prov:Agent , prov:Entity |
| ------------- | ----------- | ------------------------ |
| sosa:Actuator |             |                          |
| sosa:Sampler  |             |                          |

3\. Procedures for observation, actuation or sampling are a kind of prov:Plan, thus:

| sosa:Procedure | subclass of | prov:Plan |
| -------------- | ----------- | --------- |

4\. The other classes from the core SOSA ontology represent either real or information resources, so are interpreted as kinds of prov:Entity, thus:

| sosa:FeatureOfInterest  | subclass of | prov:Entity |
| ----------------------- | ----------- | ----------- |
| sosa:ObservableProperty | subclass of | prov:Entity |
| sosa:Platform           | subclass of | prov:Entity |
| sosa:Result             | subclass of | prov:Entity |
| sosa:Sample             | subclass of | prov:Entity |

#### 6.5.3 Property Alignments

*This section is non-normative.*

The following properties from SOSA have simple alignments with PROV properties:

| sosa:madeByActuator       | subproperty of | prov:wasAssociatedWith |
| ------------------------- | -------------- | ---------------------- |
| sosa:hasFeatureOfInterest | subproperty of | prov:used              |
| sosa:hasResult            | subproperty of | prov:generated         |
| sosa:invokedBy            | subproperty of | prov:wasAssociatedWith |
| sosa:isResultOf           | subproperty of | prov:wasGeneratedBy    |
| sosa:isSampleOf           | subproperty of | prov:wasDerivedFrom    |
| sosa:madeBySampler        | subproperty of | prov:wasAssociatedWith |
| sosa:madeBySensor         | subproperty of | prov:wasAssociatedWith |
| sosa:resultTime           | subproperty of | prov:endedAtTime       |

The final property alignment first requires some sub-properties of PROV properties to be defined:

| sp:eventAssociation | subproperty of | prov:qualifiedAssociation                                        |
| ------------------- | -------------- | ---------------------------------------------------------------- |
|                     | domain         | Union of ( sosa:Observation or sosa:Actuation or sosa:Sampling ) |
| sp:hadProcedure     | subproperty of | prov:hadPlan                                                     |
|                     | range          | sosa:Procedure                                                   |

Then sosa:usedProcedure is given by a property chain axiom:

| sosa:usedProcedure | property chain axiom | [ sp:eventAssociation , sp:hadProcedure ] |
| ------------------ | -------------------- | ----------------------------------------- |

An RDF file containing a [graph corresponding to this alignment is available](https://www.w3.org/ns/sosa/prov/).

## 7. Common Modeling Questions

*This section is non-normative.*

This section informally discusses how to handle common modeling questions such as locations, forecasts, and quantity values with a unit of measure.

### 7.1 Location

Many of the key classes provided by SOSA and SSN represent entities that can be located in space such as sensors, features of interest, actuators, samples, and so forth, or activities that can be located via their participating entities, e.g.,
platforms. These entities will usually be described using models and ontologies defined for application domains, including technical disciplines, social and business contexts. In these contexts there are a number of implementations that
support the expression of spatial properties, including location. These are discussed further in the Spatial Data on the Web Best Practices note [SDW-BP].

In particular, GeoSPARQL [GeoSPARQL] provides a flexible and relatively complete platform for geospatial objects, that fosters interoperability between geo-datasets. To do so, these
entities can be declared as instances of geo:Feature and geometries can be assigned to them via the geo:hasGeometry property. In case of classes, e.g., specific features of interests such as rivers, these can be defined as subclasses of
geo:Feature.

### 7.2 Forecasts

*This section is non-normative.*

One may also represent forecasts as observations if the value of `sosa:phenomenonTime` is later in time than the `sosa:resultTime`. Given the definition of these terms, it means that: *The time when the
Observation act was completed is before the time that the Result of
the observation applies to the FeatureOfInterest.*
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Other means to represent forecasts are reported, but not in the scope of this specification. For example [ Lefrancois-et-al-2017] derives the SSN `Sensing/Sensor/Observation` pattern and define `Forecasting/Forecaster/Forecast` classes.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Describing a plan for some actuation or observation in the future is not covered by this specification.

### 7.3 Quantity Values and Unit of Measures

*This section is non-normative.*

The result of an `sosa:Observation` (§4.3.2.2) or an `sosa:Actuation` (§4.4.2.2) can be a quantity value with a numeric value and a unit of measure.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> It is not in the scope of this specification to recommend any particular way of modeling results as quantity values. There exists external vocabularies that are specifically designed for modeling quantity values as OWL individuals. Examples
> include the Quantities, Units, Dimensions and Data Types Ontologies (QUDT, [QUDT]) and the Ontology of Units of Measure (OM, [Rijgersberg-et-al-2013]).
> With QUDT 1.1, a `sosa:Result` (§4.7.2.1) would be a [`qudt:QuantityValue`](http://qudt.org/).
> With OM 2, a `sosa:Result` (§4.7.2.1) would be a [`om:Measure` or `om:Point`](http://www.wurvoc.org/vocabularies/).
> **Example:**
>
> > **Example:**
> >
> > Example 1
>
> ```
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
>
> <Observation/234534> a sosa:Observation ;
>    rdfs:comment "Observation of the difference between
>                     the outside temperature and the inside temperature."@en ;
>    sosa:hasFeatureOfInterest <apartment/134> ;
>    sosa:hasResult [
>       a qudt-1-1:QuantityValue ;
>       qudt-1-1:unit qudt-unit-1-1:DegreeCelsius ;
>       qudt-1-1:numericValue "-29.9"^^xsd:double ] .
>
> <Observation/83985> a sosa:Observation ;
>    rdfs:comment "Observation of the temperature inside apartment #134."@en ;
>    sosa:hasFeatureOfInterest <apartment/134> ;
>    sosa:hasResult [
>       a qudt-1-1:QuantityValue ;
>       qudt-1-1:unit qudt-unit-1-1:DegreeCelsius ;
>       qudt-1-1:numericValue "22.4"^^xsd:double ] .
> ```
> **Example:**
>
> > **Example:**
> >
> > Example 2
>
> ```
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
> @prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/> .
>
> <Observation/234534> a sosa:Observation ;
>    rdfs:comment "Observation of the difference between
>                     the outside temperature and the inside temperature."@en ;
>    sosa:hasFeatureOfInterest <apartment/134> ;
>    sosa:hasResult [
>       a om:Measure ;
>       om:hasUnit om:degreeCelsius ;
>       om:hasNumericalValue "-29.9"^^xsd:double ] .
>
> <Observation/83985> a sosa:Observation ;
>    rdfs:comment "Observation of the temperature inside apartment #134."@en ;
>    sosa:hasFeatureOfInterest <apartment/134> ;
>    sosa:hasResult [
>       a om:Point ;
>       om:hasScale om:CelsiusScale ;
>       om:hasNumericalValue "22.4"^^xsd:double ] .
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Other means to represent quantity values as literals are reported, but not in the scope of this specification. This solution would require the use of some custom datatype whose value space is some set of quantity values. Such a datatype
> should be supported by RDF and SPARQL engines to support the comparison of quantity values. On the other hand, this approach is not compatible with the OWL specifications, that restrict the set of datatypes that can be used. See sec.
> 5.2 in [owl2-syntax] for more details.
> **Example:**
>
> > **Example:**
> >
> > Example 3
>
> ```
> @prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
>
> <observation/123> a sosa:Observation ;
>   sosa:hasSimpleResult "12.4 m"^^cdt:length .
> ```

### 7.4 Generic or Specific Instances of ssn:Property

*This section is non-normative.*

This specification does not specify whether an instance of `ssn:Property` (§4.6.2.4) should be generic to all features of interest (e.g., `ex:Temperature`, `ex:OnOffStatus`), or specific to a single feature of interest (e.g., `<myBodyTemperature>`, `<LightStatus>`). Implementers are free to choose one way of modeling things or the other.

On the other hand, one *SHOULD NOT* use [OWL punning](https://www.w3.org/TR/owl2-new-features/#F12:_Punning) to make `ex:Temperature` denote both a subclass of `ssn:Property` (§4.6.2.4) and an instance of `ssn:Property` (§4.6.2.4). In fact, merging the two examples below in a single RDF Graph would make an OWL reasoner infer that `ex:Temperature`, `<office/1/temperature>`, and `<office/2/temperature>`, denote the same individual.

This also holds for subclasses of `ssn:Property` (§4.6.2.4): `sosa:ObservableProperty` (§4.3.2.1), and `sosa:ActuatableProperty` (§4.4.2.1).

This first example is modeling instances of `ssn:Property` (§4.6.2.4) as generic to all features of interest:
> **Example:**
>
> > **Example:**
> >
> > Example 4
>
> ```
> ex:Temperature a ssn:Property .
>
> <office/1> a sosa:FeatureOfInterest;
>   ssn:hasProperty ex:Temperature .
>
> <Observation/1> a sosa:Observation ;
>   sosa:observedProperty ex:Temperature ;
>   sosa:hasFeatureOfInterest <office/1> .
>
> <office/2> a sosa:FeatureOfInterest;
>   ssn:hasProperty ex:Temperature .
>
> <Observation/2> a sosa:Observation ;
>   sosa:observedProperty ex:Temperature ;
>   sosa:hasFeatureOfInterest <office/2> .
> ```

This second example is modeling instances of `ssn:Property` (§4.6.2.4) as specific to a features of interest:
> **Example:**
>
> > **Example:**
> >
> > Example 5
>
> ```
> ex:Temperature a owl:Class ;
>   rdfs:subClassOf ssn:Property .
>
> <office/1> a sosa:FeatureOfInterest;
>   ssn:hasProperty <office/1/temperature> .
>
> <office/1/temperature> a ex:Temperature , ssn:Property .
>
> <Observation/1> a sosa:Observation ;
>   sosa:observedProperty <office/1/temperature> ;
>   sosa:hasFeatureOfInterest <office/1> .
>
> <office/2> a sosa:FeatureOfInterest;
>   ssn:hasProperty <office/2/temperature> .
>
> <office/2/temperature> a ex:Temperature , ssn:Property .
>
> <Observation/2> a sosa:Observation ;
>   sosa:observedProperty <office/2/temperature> ;
>   sosa:hasFeatureOfInterest <office/2> .
> ```

### 7.5 Generic or Specific Instances of ssn:System

*This section is non-normative.*

This specification does not specify whether an instance of `ssn:System` (§4.9.2.4) should be generic (e.g., `ex:TemperatureSensor`, `ex:LightActuator`), or specific to a single feature of interest (e.g., `<temperatureSensor/84>`, `<light/112>`). Implementers are free to choose one way of modeling things or the other.

On the other hand, one *SHOULD NOT* use [OWL punning](https://www.w3.org/TR/owl2-new-features/#F12:_Punning) to make `ex:Temperature` denote both a subclass of `ssn:Property` (§4.6.2.4) and an instance of ssn:Property. In fact, merging the two examples below in a single RDF Graph would make an OWL reasoner infer that `ex:TemperatureSensor`, `<TemperatureSensor/1>`,
and `<TemperatureSensor/2>`, denote the same individual.

This also holds for subclasses of `ssn:System` (§4.9.2.4): `sosa:Sensor` (§4.3.2.5), `sosa:Actuator` (§4.4.2.5), and `sosa:Sampler` (§4.5.2.5).

This first example is modeling instances of `ssn:System` (§4.9.2.4) as generic:
> **Example:**
>
> > **Example:**
> >
> > Example 6
>
> ```
> ex:TemperatureSensor a ssn:System .
>
> <Observation/1> a sosa:Observation ;
>   sosa:madeBySensor ex:TemperatureSensor .
>
> <Observation/2> a sosa:Observation ;
>   sosa:madeBySensor ex:TemperatureSensor .
>
> # describing the system capabilities and operating/survival range can be done generically
> # with this modeling choice:
>
> ex:TemperatureSensor ssn-system:hasOperatingRange ex:TemperatureSensorOperatingRange .
>
> ex:TemperatureSensorOperatingRange a ssn-system:OperatingRange ;
>   ssn-system:inCondition ex:NormalTemperatureCondition , ex:NormalHumidityCondition .
> ```

This second example is modeling instances of `ssn:System` (§4.9.2.4) as specific:
> **Example:**
>
> > **Example:**
> >
> > Example 7
>
> ```
> ex:TemperatureSensor a owl:Class ;
>   rdfs:subClassOf ssn:System .
>
> <TemperatureSensor/1> a ex:TemperatureSensor , ssn:System .
>
> <Observation/1> a sosa:Observation ;
>   sosa:madeBySensor <TemperatureSensor/1> .
>
> <TemperatureSensor/2> a ex:TemperatureSensor , ssn:System .
>
> <Observation/2> a sosa:Observation ;
>   sosa:madeBySensor <TemperatureSensor/2> .
>
> # describing the system capabilities and operating/survival range can be done at the level of
> # the class or at the level of each instance with this modeling choice:
>
> ex:TemperatureSensor  rdfs:subClassOf [
>     owl:onProperty ssn-system:hasOperatingRange ;
>     owl:hasValue ex:TemperatureSensorOperatingRange ] .
>
> <TemperatureSensor/1>
>   ssn-system:hasOperatingRange ex:TemperatureSensorOperatingRange ; # this axiom can be inferred
>   ssn-system:hasOperatingRange <moreSpecificTemperatureSensorOperatingRange> .
>
> <moreSpecificTemperatureSensorOperatingRange> a ssn-system:OperatingRange ;
>   ssn-system:inCondition <modeSpecificTemperatureCondition> , <modeSpecificHumidityCondition> .
> ```

## A. Wide review

Results of the wide review of SOSA and SSN is [summarized here](https://www.w3.org/2015/spatial/wiki/Wide_Review).

## B. Complete Examples

### B.1 iPhone Barometer

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/iphone_barometer-sosa.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 8
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix time: <http://www.w3.org/2006/time#>.
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
> @base <http://example.org/data/> .
>
> # The barometric readings from a Bosch Sensortec BMP282 sensor in an Apple IPhone 7
> # observed on June 6 2017 using only the SOSA core for modelling.
>
> <earthAtmosphere> rdf:type sosa:FeatureOfInterest ;
>   rdfs:label "Atmosphere of Earth"@en .
>
>
> # An iPhone 7 as the Platform that hosts several sensors,
> # among others the Bosch Sensortec BMP282 atmospheric pressure sensor.
>
> <iphone7/35-207306-844818-0> a sosa:Platform ;
>   rdfs:label "IPhone 7 - IMEI 35-207306-844818-0"@en ;
>   rdfs:comment "IPhone 7 - IMEI 35-207306-844818-0 - John Doe"@en ;
>   sosa:hosts <sensor/35-207306-844818-0/BMP282> .
>
> <sensor/35-207306-844818-0/BMP282> rdf:type sosa:Sensor ;
>   rdfs:label "Bosch Sensortec BMP282"@en ;
>   sosa:observes <sensor/35-207306-844818-0/BMP282/atmosphericPressure> .
>
>
> # An observation made by the BMP282 atmospheric pressure sensor.
>
> <Observation/346344> rdf:type sosa:Observation ;
>   sosa:observedProperty <sensor/35-207306-844818-0/BMP282/atmosphericPressure> ;
>   sosa:hasFeatureOfInterest  <earthAtmosphere> ;
>   sosa:madeBySensor <sensor/35-207306-844818-0/BMP282> ;
>   sosa:hasSimpleResult "1021.45 hPa"^^cdt:ucum ;
>   sosa:resultTime "2017-06-06T12:36:12Z"^^xsd:dateTime .
>
>
> # Another observation made a second later by the BMP282 atmospheric pressure sensor
> # using the QUDT Ontology for the Units of Measurement
> # and the Time Ontology for the instant.
>
> <Observation/346345> rdf:type sosa:Observation ;
>   sosa:observedProperty <sensor/35-207306-844818-0/BMP282/atmosphericPressure> ;
>   sosa:hasFeatureOfInterest  <earthAtmosphere> ;
>   sosa:madeBySensor <sensor/35-207306-844818-0/BMP282> ;
>   sosa:hasResult [
>     rdf:type qudt-1-1:QuantityValue ;
>     qudt-1-1:numericValue "101936"^^xsd:double ;
>     qudt-1-1:unit qudt-unit-1-1:Pascal ] ;
>   sosa:resultTime [
>     rdf:type time:Instant ;
>     time:inXSDDateTimeStamp "2017-06-06T12:36:13+00:00"^^xsd:dateTimeStamp ] .
> ```

### B.2 Coal Oil Point Reserve

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/IDEAS.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 9
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
>  @prefix owl: <http://www.w3.org/2002/07/owl#> .
>  @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
>  @prefix sosa: <http://www.w3.org/ns/sosa#> .
>  @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
>  @prefix cdt: <http://w3id.org/lindt/custom_datatypes#>.
>
> @base <http://example.org/data/> .
>
> <IDEA> a owl:Ontology ;
>    owl:imports <http://www.w3.org/ns/sosa> .
>
>  <COPR> a sosa:FeatureOfInterest ;
>    sosa:hasSample <COPR_SL> ;
>    rdfs:comment "Coal Oil Point Reserve: UC Santa Barbara Natural Reserve System"@en ;
>    rdfs:label "Coal Oil Point Reserve"@en .
>
>  <COPR_Station_Location> a sosa:Sample ;
>    rdfs:comment "."@en ;
>    rdfs:label "Air around COPR Station"@en ;
>    sosa:isSampleOf <COPR> .
>
>  <COPR_Station> a sosa:Platform ;
>    rdfs:comment "Station at Coal Oil Point Reserve, CA (see http://www.geog.ucsb.edu/ideas/COPR.html for details)"@en ;
>    rdfs:label "Coal Oil Point Reserve Wx Station"@en ;
>    rdfs:seeAlso <http://www.geog.ucsb.edu/ideas/COPR.html> ;
>    sosa:hosts <COPR-HMP45C-L> .
>
>  <COPR-HMP45C-L> a sosa:Platform ;
>    rdfs:label "HMP45C-L Temperature and Relative Humidity Probe at Coal Oil Point, UCSB, CA"@en ;
>    sosa:hosts <HUMICAP-H> ;
>    sosa:isHostedBy <COPR_Station> .
>
>  <HUMICAP-H> a sosa:Sensor ;
>    rdfs:label "Vaisala HUMICAP H-chip"@en ;
>    sosa:isHostedBy <COPR-HMP45C-L> .
>
>  <RelativeHumidity> a sosa:ObservableProperty ;
>    rdfs:comment "Humidity is a measure of the moisture content of air."@en ;
>    rdfs:label "Relative Humidity"@en .
>
>  <MeasuringRelativeHumidity> a sosa:Procedure ;
>    rdfs:comment "Instructions for measuring relative humidity"@en .
>
>  <RH_avg_1_COPR_15min_201706020300PM> a sosa:Observation ;
>    rdfs:comment "Relative humidity as averaged over 15min at COPR."@en ;
>    rdfs:label "Relative humidity, AVG, 15min, COPR, 06.02.2017, 3:00 PM"@en ;
>    sosa:madeBySensor <HUMICAP-H> ;
>    sosa:hasFeatureOfInterest <COPR_Station_Location> ;
>    sosa:hasSimpleResult "92.5 %"^^cdt:ucum ;
>    sosa:resultTime "2017-06-02-T03:00:00-7:00"^^xsd:dateTime ;
>    sosa:observedProperty <RelativeHumidity> ;
>    sosa:usedProcedure <MeasuringRelativeHumidity> .
> ```

### B.3 apartment 134

[Show all SOSA and SSN terms] [Show only core SOSA terms]

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/apartment-134.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 10
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix time: <http://www.w3.org/2006/time#>.
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix ssn:  <http://www.w3.org/ns/ssn/> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @base <http://example.org/data/> .
>
> # The electric consumption of apartment #134 on April 15 2017 was 22.4 kWh as
> # observed by sensor #926. The result was available 12 seconds later.
>
> <Observation/235714> rdf:type sosa:Observation ;
>   sosa:observedProperty  <apartment/134/electricConsumption> ;
>   sosa:madeBySensor <sensor/926> ;
>   sosa:hasResult [
>      rdf:type qudt-1-1:QuantityValue ;
>      qudt-1-1:numericValue "22.4"^^xsd:double ;
>      qudt-1-1:unit qudt-unit-1-1:Kilowatthour ] ;
>   sosa:phenomenonTime [
>     rdf:type time:Interval ;
>     time:hasBeginning [
>       rdf:type time:Instant ;
>       time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTimeStamp ] ;
>     time:hasEnd [
>       rdf:type time:Instant ;
>       time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTimeStamp ] ] ;
>   sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTimeStamp .
>
>
> # Sensor #926 observes the electric consumption of apartment #134, and we know that
> # it made some observations.
>
> <sensor/926> rdf:type sosa:Sensor ;
>   sosa:observes  <apartment/134/electricConsumption> ;
>   sosa:madeObservation <Observation/235714>, <Observation/235715>, <Observation/235716> .
>
> # mobile sensor tempSensor #23 observes the temperature in its surroundings, and we know
> # that it made some observations.
>
> <tempSensor/23> rdf:type sosa:Sensor ;
>   sosa:observes  <tempSensor/23#temperature> ;
>   sosa:madeObservation <tempSensor/23/4572>, <tempSensor/23/4573>, <tempSensor/23/4574> .
>
>
> # Sensor #926 observes the electric consumption of apartment #134
>
> <sensor/926> rdf:type sosa:Sensor ;
>   sosa:observes  <apartment/134/electricConsumption> .
>
> # This is equivalent to saying that the electric consumption of apartment #134 is
> # observed by Sensor #926
>
> <apartment/134/electricConsumption> rdf:type sosa:ObservableProperty ;
>   sosa:isObservedBy <sensor/926>  .
>
>
> # Sensor #926 made observations identified by <Observation/235714> and <Observation/235715>.
>
> <sensor/926> rdf:type sosa:Sensor ;
>   sosa:madeObservation <Observation/235714>, <Observation/235715> .
>
> # This is equivalent to saying that these observations have been made by sensor #926.
>
> <Observation/235714> rdf:type sosa:Observation ;
>   sosa:madeBySensor <sensor/926> .
>
> <Observation/235754> rdf:type sosa:Observation ;
>   sosa:madeBySensor <sensor/926> .
>
>
> # the window opening state is an ActuatableProperty.
> # SSN allows to explicitly say that <window/104#state> is a property of <window>
>
> <window> rdf:type sosa:FeatureOfInterest ;
>   ssn:hasProperty <window/104#state> .
>
> <window/104#state> rdf:type sosa:ActuatableProperty ;
>   sosa:isActedOnBy <actuation/188> .
>
>
> # WindowCloser #987 made actuation #188
> # SSN allows to explicitly say that <windowCloser/987> is designed to automatically open and close window #104.
>
> <windowCloser/987> rdf:type sosa:Actuator ;
>   sosa:madeActuation <actuation/188> ;
>   ssn:forProperty <window/104#state> .
>
>
> # Actuation #188 acted on the state of window #104 and returned 'true'.
>
> <actuation/188> rdf:type sosa:Actuation ;
>   sosa:actsOnProperty  <window/104#state> ;
>   sosa:actuationMadeBy <windowCloser/987> ;
>   sosa:hasSimplResult true ;
>   sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp .
> ```

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/apartment-134-sosa.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 11
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix time: <http://www.w3.org/2006/time#>.
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @base <http://example.org/data/> .
>
> # The electric consumption of apartment #134 on April 15 2017 was 22.4 kWh as
> # observed by sensor #926. The result was available 12 seconds later.
>
> <Observation/235714> rdf:type sosa:Observation ;
>   sosa:observedProperty  <apartment/134/electricConsumption> ;
>   sosa:madeBySensor <sensor/926> ;
>   sosa:hasResult [
>      rdf:type qudt-1-1:QuantityValue ;
>      qudt-1-1:numericValue "22.4"^^xsd:double ;
>      qudt-1-1:unit qudt-unit-1-1:Kilowatthour ] ;
>   sosa:phenomenonTime [
>     rdf:type time:Interval ;
>     time:hasBeginning [
>       rdf:type time:Instant ;
>       time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTimeStamp ] ;
>     time:hasEnd [
>       rdf:type time:Instant ;
>       time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTimeStamp ] ] ;
>   sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTimeStamp .
>
>
> # Sensor #926 observes the electric consumption of apartment #134, and we know that
> # it made some observations.
>
> <sensor/926> rdf:type sosa:Sensor ;
>   sosa:observes  <apartment/134/electricConsumption> ;
>   sosa:madeObservation <Observation/235714>, <Observation/235715>, <Observation/235716> .
>
> # mobile sensor tempSensor #23 observes the temperature in its surroundings, and we know
> # that it made some observations.
>
> <tempSensor/23> rdf:type sosa:Sensor ;
>   sosa:observes  <tempSensor/23#temperature> ;
>   sosa:madeObservation <tempSensor/23/4572>, <tempSensor/23/4573>, <tempSensor/23/4574> .
>
>
> # Sensor #926 observes the electric consumption of apartment #134
>
> <sensor/926> rdf:type sosa:Sensor ;
>   sosa:observes  <apartment/134/electricConsumption> .
>
> # This is equivalent to saying that the electric consumption of apartment #134 is
> # observed by Sensor #926
>
> <apartment/134/electricConsumption> rdf:type sosa:ObservableProperty ;
>   sosa:isObservedBy <sensor/926>  .
>
>
> # Sensor #926 made observations identified by <Observation/235714> and <Observation/235715>.
>
> <sensor/926> rdf:type sosa:Sensor ;
>   sosa:madeObservation <Observation/235714>, <Observation/235715> .
>
> # This is equivalent to saying that these observations have been made by sensor #926.
>
> <Observation/235714> rdf:type sosa:Observation ;
>   sosa:madeBySensor <sensor/926> .
>
> <Observation/235754> rdf:type sosa:Observation ;
>   sosa:madeBySensor <sensor/926> .
>
>
> # the window opening state is an ActuatableProperty.
>
> <window> rdf:type sosa:FeatureOfInterest .
>
> <window/104#state> rdf:type sosa:ActuatableProperty ;
>   sosa:isActedOnBy <actuation/188> .
>
>
> # WindowCloser #987 made actuation #188
>
> <windowCloser/987> rdf:type sosa:Actuator ;
>   sosa:madeActuation <actuation/188> .
>
>
> # Actuation #188 acted on the state of window #104 and returned 'true'.
>
> <actuation/188> rdf:type sosa:Actuation ;
>   sosa:actsOnProperty  <window/104#state> ;
>   sosa:actuationMadeBy <windowCloser/987> ;
>   sosa:hasSimplResult true ;
>   sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp .
> ```

[Show all SOSA and SSN terms] [Show only core SOSA terms]

### B.4 Tree height measurement

[Show all SOSA and SSN terms] [Show only core SOSA terms]

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/tree-height.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 12
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix ssn: <http://www.w3.org/ns/ssn/> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @base <http://example.org/data/> .
>
> # rangefinder #30 is a laser range finder sensor that was used
> # to observe the height of tree #124 and #125.
>
> <rangefinder/30>        rdf:type           sosa:Sensor ;
>   rdfs:label "rangefinder #30"@en ;
>   rdfs:comment "rangefinder #30 is a laser range finder sensor."@en .
>
> # rangefinder #30 made observation #1087 of the height of tree #124.
>
> <observation/1087>  rdf:type               sosa:Observation ;
>   rdfs:label "observation #1087"@en ;
>   sosa:hasFeatureOfInterest  <tree/124> ;
>   sosa:observedProperty  <tree/124/height> ;
>   sosa:madeBySensor <rangefinder/30> ;
>   sosa:hasResult [
>     qudt-1-1:unit qudt-unit-1-1:Meter ;
>     qudt-1-1:numericalValue "15.3"^^xsd:double ] .
>
> # using SSN, one can explicitly link a property and its feature of interest.
>
> <tree/124>  rdf:type    sosa:FeatureOfInterest ;
>   rdfs:label "tree #124"@en ;
>   ssn:hasProperty <tree/124#height> .
>
> <tree/124#height>  rdf:type    sosa:ObservableProperty , ssn:Property ;
>   rdfs:label "the height of tree #124"@en ;
>   ssn:isPropertyOf <tree/124> .
>
> # rangefinder #30 made observation #1088 of the height of tree #125.
>
> <observation/1088>  rdf:type               sosa:Observation ;
>   rdfs:label "observation #1088"@en ;
>   sosa:hasFeatureOfInterest  <tree/125> ;
>   sosa:observedProperty  <tree/125/height> ;
>   sosa:madeBySensor <rangefinder/30> ;
>   sosa:hasResult [
>     qudt-1-1:numericValue "23.0"^^xsd:double ;
>     qudt-1-1:unit qudt-unit-1-1:Meter ] .
>
> # using SSN, one can explicitly link a property and its feature of interest.
>
> <tree/125>  rdf:type    sosa:FeatureOfInterest ;
>   rdfs:label "tree #125"@en ;
>   ssn:hasProperty <tree/125#height> .
>
> <tree/125#height>  rdf:type    sosa:ObservableProperty , ssn:Property ;
>   rdfs:label "the height of tree #125"@en ;
>   ssn:isPropertyOf <tree/124> .
> ```

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/tree-height-sosa.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 13
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @base <http://example.org/data/> .
>
> # rangefinder #30 is a laser range finder sensor that was used
> # to observe the height of tree #124 and #125.
>
> <rangefinder/30>        rdf:type           sosa:Sensor ;
>   rdfs:label "rangefinder #30"@en ;
>   rdfs:comment "rangefinder #30 is a laser range finder sensor."@en .
>
> # rangefinder #30 made observation #1087 of the height of tree #124.
>
> <observation/1087>  rdf:type               sosa:Observation ;
>   rdfs:label "observation #1087"@en ;
>   sosa:hasFeatureOfInterest  <tree/124> ;
>   sosa:observedProperty  <tree/124/height> ;
>   sosa:madeBySensor <rangefinder/30> ;
>   sosa:hasResult [
>     qudt-1-1:unit qudt-unit-1-1:Meter ;
>     qudt-1-1:numericalValue "15.3"^^xsd:double ] .
>
> <tree/124>  rdf:type    sosa:FeatureOfInterest ;
>   rdfs:label "tree #124"@en .
>
> <tree/124#height>  rdf:type    sosa:ObservableProperty , ssn:Property ;
>   rdfs:label "the height of tree #124"@en .
>
> # rangefinder #30 made observation #1088 of the height of tree #125.
>
> <observation/1088>  rdf:type               sosa:Observation ;
>   rdfs:label "observation #1088"@en ;
>   sosa:hasFeatureOfInterest  <tree/125> ;
>   sosa:observedProperty  <tree/125/height> ;
>   sosa:madeBySensor <rangefinder/30> ;
>   sosa:hasResult [
>     qudt-1-1:numericValue "23.0"^^xsd:double ;
>     qudt-1-1:unit qudt-unit-1-1:Meter ] .
>
> <tree/125>  rdf:type    sosa:FeatureOfInterest ;
>   rdfs:label "tree #125"@en .
>
> <tree/125#height>  rdf:type    sosa:ObservableProperty , ssn:Property ;
>   rdfs:label "the height of tree #125"@en .
> ```

[Show all SOSA and SSN terms] [Show only core SOSA terms]

### B.5 Seismographs

[Show all SOSA and SSN terms] [Show only core SOSA terms]

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/seismograph.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 14
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix ssn:  <http://www.w3.org/ns/ssn/> .
> @prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @base <http://example.org/data/> .
>
> # Observation #358 of seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca) measured
> # a earth displacement speed of 0.000500 cm/sec at 8:23 am on April 18, 2017, Pacific
> # Daylight Time.
>
> <earth>  rdf:type    sosa:FeatureOfInterest ;
>   rdfs:label "earth"@en .
>
> <VCAB-DP1-BP-40> rdf:type sosa:Sensor ;
>   rdfs:label "seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca)"@en ;
>   rdfs:seeAlso <https://earthquake.usgs.gov/monitoring/seismograms/153> ;
>   sosa:observes <VCAB-DP1-BP-40#groundDisplacementSpeed> .
>
> <VCAB-DP1-BP-40#location> rdf:type sosa:FeatureOfInterest ;
>   rdfs:label "location of VCAB-DP1-BP-40"@en ;
>   geo:lat 35.8648067 ;
>   geo:long -120.6195831 ;
>   geo:alt 12.75 ;
>   sosa:isSampleOf <earth> .
>
> <VCAB-DP1-BP-40#groundDisplacementSpeed>  rdf:type    sosa:ObservableProperty , ssn:Property ;
>   rdfs:label "the ground displacement speed at location of VCAB-DP1-BP-40"@en ;
>   sosa:isObservedBy <VCAB-DP1-BP-40> .
>
> <VCAB-DP1-BP-40?t=2017-04-18T08%3A23%3A00-07%3A00> rdf:type sosa:Observation ;
>   sosa:madeBySensor <VCAB-DP1-BP-40> ;
>   sosa:hasFeatureOfInterest  <VCAB-DP1-BP-40#location> ;
>   sosa:observedProperty  <VCAB-DP1-BP-40#groundDisplacementSpeed> ;
>   sosa:hasResult [
>      rdf:type qudt-1-1:QuantityValue ;
>      qudt-1-1:numericValue "5e-4"^^xsd:double ;
>      qudt-1-1:unit qudt-unit-1-1:CentimeterPerSecond ] ;
>   sosa:resultTime "2017-04-18T08:23:00-07:00"^^xsd:dateTimeStamp .
>
> # using SSN one can explicitly state that <VCAB-DP1-BP-40#groundDisplacementSpeed> is the property of <VCAB-DP1-BP-40#location> .
>
> <VCAB-DP1-BP-40#location> ssn:hasProperty <VCAB-DP1-BP-40#groundDisplacementSpeed> ;
> ```

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/seismograph-sosa.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 15
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @base <http://example.org/data/> .
>
> # Observation #358 of seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca) measured
> # a earth displacement speed of 0.000500 cm/sec at 8:23 am on April 18, 2017, Pacific
> # Daylight Time.
>
> <earth>  rdf:type    sosa:FeatureOfInterest ;
>   rdfs:label "earth"@en .
>
> <VCAB-DP1-BP-40> rdf:type sosa:Sensor ;
>   rdfs:label "seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca)"@en ;
>   rdfs:seeAlso <https://earthquake.usgs.gov/monitoring/seismograms/153> ;
>   sosa:observes <VCAB-DP1-BP-40#groundDisplacementSpeed> .
>
> <VCAB-DP1-BP-40#location> rdf:type sosa:FeatureOfInterest ;
>   rdfs:label "location of VCAB-DP1-BP-40"@en ;
>   geo:lat 35.8648067 ;
>   geo:long -120.6195831 ;
>   geo:alt 12.75 ;
>   sosa:isSampleOf <earth> .
>
> <VCAB-DP1-BP-40#groundDisplacementSpeed>  rdf:type    sosa:ObservableProperty , ssn:Property ;
>   rdfs:label "the ground displacement speed at location of VCAB-DP1-BP-40"@en ;
>   sosa:isObservedBy <VCAB-DP1-BP-40> .
>
> <VCAB-DP1-BP-40?t=2017-04-18T08%3A23%3A00-07%3A00> rdf:type sosa:Observation ;
>   sosa:madeBySensor <VCAB-DP1-BP-40> ;
>   sosa:hasFeatureOfInterest  <VCAB-DP1-BP-40#location> ;
>   sosa:observedProperty  <VCAB-DP1-BP-40#groundDisplacementSpeed> ;
>   sosa:hasResult [
>      rdf:type qudt-1-1:QuantityValue ;
>      qudt-1-1:numericValue "5e-4"^^xsd:double ;
>      qudt-1-1:unit qudt-unit-1-1:CentimeterPerSecond ] ;
>   sosa:resultTime "2017-04-18T08:23:00-07:00"^^xsd:dateTimeStamp .
> ```

[Show all SOSA and SSN terms] [Show only core SOSA terms]

### B.6 Number of sunspots

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/sunspots.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 16
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix time: <http://www.w3.org/2006/time#>.
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @base <http://example.org/data/> .
>
> # The result of an observation of the sunspot number is available a few minutes
> # after the phenomenon time, due to the light travel duration.
>
> <Observation/7536> rdf:type sosa:Observation ;
>   sosa:observedProperty  <Sun#sunspotNumber> ;
>   sosa:hasSimpleResult 66 ;
>   sosa:phenomenonTime [
>     rdf:type time:Instant ;
>     time:inXSDDateTimeStamp "2017-03-31T11:51:42+00:00"^^xsd:dateTimeStamp ] ;
>   sosa:resultTime "2017-03-31T12:00:00+00:00"^^xsd:dateTimeStamp .
> ```

### B.7 Wind sensor spinning cups

[Show all SOSA and SSN terms] [Show only core SOSA terms]

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/spinning-cups.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 17
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix ssn:  <http://www.w3.org/ns/ssn/> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @base <http://example.org/data/> .
>
> # movements of spinning cups on wind sensor #14 serves as proxies for the wind speed
> # at the location of the wind sensor.
>
> <windSensor/14> rdf:type sosa:Sensor ;
>   sosa:observes <location/4687#windSpeed> .
>
> # wind sensor #14 detected some movement of spinning cups, from which originated the
> # observations #147 and #148.
>
> <windSensor/14> rdf:type sosa:Sensor ;
>   sosa:madeObservation <observation/147> , <observation/148> ;
>   ssn:detects <observation/147#spinningCupsMovement> , <observation/148#spinningCupsMovement> .
>
> # observation #147 was originated by the movement of the spinning cups of sensor #14.
> # the result of observations #147 and #148 is using some custom datatype that encodes the unit of measure.
>
> <observation/147> rdf:type sosa:Observation ;
>   sosa:observedProperty <location/4687#windSpeed> ;
>   sosa:madeBySensor <windSensor/14> ;
>   ssn:wasOriginatedBy <observation/147#spinningCupsMovement> ;
>   sosa:resultTime "2017-04-12T12:00:00Z"^^xsd:dateTime ;
>   sosa:hasSimpleResult "47 km/h"^^<speed> .
>
> <observation/147#spinningCupsMovement> rdf:type ssn:Stimulus ;
>   ssn:isProxyFor <location/4687#windSpeed> .
>
> <observation/148> rdf:type sosa:Observation ;
>   sosa:observedProperty <location/4687#windSpeed> ;
>   sosa:madeBySensor <windSensor/14> ;
>   ssn:wasOriginatedBy <observation/148#spinningCupsMovement> ;
>   sosa:resultTime "2017-04-12T12:01:00Z"^^xsd:dateTime ;
>   sosa:hasSimpleResult "43 km/h"^^<speed> .
>
> <observation/148#spinningCupsMovement> rdf:type ssn:Stimulus ;
>   ssn:isProxyFor <location/4687#windSpeed> .
> ```

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/spinning-cups-sosa.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 18
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @base <http://example.org/data/> .
>
> # movements of spinning cups on wind sensor #14 serves as proxies for the wind speed
> # at the location of the wind sensor.
>
> <windSensor/14> rdf:type sosa:Sensor ;
>   sosa:observes <location/4687#windSpeed> .
>
> # wind sensor #14 made observations #147 and #148.
>
> <windSensor/14> rdf:type sosa:Sensor ;
>   sosa:madeObservation <observation/147> , <observation/148> .
>
> # the result of observations #147 and #148 is using some custom datatype that encodes the unit of measure.
>
> <observation/147> rdf:type sosa:Observation ;
>   sosa:observedProperty <location/4687#windSpeed> ;
>   sosa:madeBySensor <windSensor/14> ;
>   sosa:resultTime "2017-04-12T12:00:00Z"^^xsd:dateTime ;
>   sosa:hasSimpleResult "47 km/h"^^<speed> .
>
> <observation/148> rdf:type sosa:Observation ;
>   sosa:observedProperty <location/4687#windSpeed> ;
>   sosa:madeBySensor <windSensor/14> ;
>   sosa:resultTime "2017-04-12T12:01:00Z"^^xsd:dateTime ;
>   sosa:hasSimpleResult "43 km/h"^^<speed> .
> ```

[Show all SOSA and SSN terms] [Show only core SOSA terms]

### B.8 Ice Core

[Show all SOSA and SSN terms] [Show only core SOSA terms]

In order to characterize a thing with a large extent, or which is not directly accessible, the usual observational strategy is to obtain one or more samples. Observations may then be made more conveniently on the samples, with the intention
of characterizing the larger thing. This intentionality is captured using the property `sosa:isSampleOf`.

In the following example, the ice core is a sample of the Antarctic ice sheet, and observations are made on the ice core.

A convenient side effect of this feature is that all observations related to the larger thing (the ice sheet) can be found, and then potentially joined together in a meta-analysis in order to characterize that.

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/ice-core.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 19
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix time: <http://www.w3.org/2006/time#>.
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix ssn:  <http://www.w3.org/ns/ssn/> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>.
> @base <http://example.org/data/> .
>
>
> # The CO2 level observed in an ice core is 240 parts per million.
> # the ice core is a sample of the polar ice sheet of Antarctica.
>
> <http://dbpedia.org/resource/Antarctic_ice_sheet> a sosa:FeatureOfInterest ;
>   sosa:hasSample <iceCore/12>, <iceCore/13>, <iceCore/14> .
>
> <iceCore/12> rdf:type sosa:Sample ;
>   sosa:isSampleOf <http://dbpedia.org/resource/Antarctic_ice_sheet> ;
>   sosa:isResultOf <WellDrilling/4578> ;
>   sosa:madeBySampler <thermalDrill/2> .
>
>   <WellDrilling/4578> a sosa:Sampling ;
>     geo:lat -73.35 ;
>     geo:long 9.32 ;
>     sosa:hasResult <iceCore/12> ;
>     sosa:madeBySampler <thermalDrill/2> ;
>     sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
>     sosa:hasFeatureOfInterest <http://dbpedia.org/resource/Antarctic_ice_sheet> .
>
> <iceCore/12#observation> a sosa:Observation ;
>   sosa:observedProperty <iceCore/12#CO2> ;
>   sosa:hasSimpleResult 240 .
>
> # using SSN one can explicitly state that <iceCore/12#CO2> is the property of <iceCore/12> .
>
> <iceCore/12#CO2> ssn:isPropertyOf <iceCore/12> .
> ```

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/ice-core-sosa.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 20
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix time: <http://www.w3.org/2006/time#>.
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>.
> @base <http://example.org/data/> .
>
>
> # The CO2 level observed in an ice core is 240 parts per million.
> # the ice core is a sample of the polar ice sheet of Antarctica.
>
> <http://dbpedia.org/resource/Antarctic_ice_sheet> a sosa:FeatureOfInterest ;
>   sosa:hasSample <iceCore/12>, <iceCore/13>, <iceCore/14> .
>
> <iceCore/12> rdf:type sosa:Sample ;
>   sosa:isSampleOf <http://dbpedia.org/resource/Antarctic_ice_sheet> ;
>   sosa:isResultOf <WellDrilling/4578> ;
>   sosa:madeBySampler <thermalDrill/2> .
>
>   <WellDrilling/4578> a sosa:Sampling ;
>     geo:lat -73.35 ;
>     geo:long 9.32 ;
>     sosa:hasResult <iceCore/12> ;
>     sosa:madeBySampler <thermalDrill/2> ;
>     sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
>     sosa:hasFeatureOfInterest <http://dbpedia.org/resource/Antarctic_ice_sheet> .
>
> <iceCore/12#observation> a sosa:Observation ;
>   sosa:observedProperty <iceCore/12#CO2> ;
>   sosa:hasSimpleResult 240 .
> ```

[Show all SOSA and SSN terms] [Show only core SOSA terms]

### B.9 DHT22 Description

[Show all SOSA and SSN terms] [Show only core SOSA terms]

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/dht22.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 21
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @prefix schema: <http://schema.org/>.
>
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix ssn: <http://www.w3.org/ns/ssn/> .
> @prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .
>
> @prefix rdfp: <https://w3id.org/rdfp/>.
>
> @base <http://example.org/data/> .
>
>
> <DHT22#Procedure> a sosa:Procedure ;
>   ssn:hasOutput <DHT22#output> .
>
> <DHT22#output> a ssn:Output , rdfp:GraphDescription ;
>   rdfs:comment "The output is a RDF Graph that describes both the temperature and the humidity. It can be validated by a SHACL shapes graph."@en ;
>   rdfp:presentedBy [
>     a rdfp:GraphDescription ;
>     rdfp:validationRule <shacl_shapes_graph> ;
>   ] .
>
>
> <DHT22/4578> a ssn:System ;
>   rdfs:comment "DHT22 sensor #4578 contains a humidity and a temperature sensor."@en ;
>   rdfs:seeAlso <https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf> ;
>   ssn:hasSubSystem <DHT22/4578#TemperatureSensor>, <DHT22/4578#HumiditySensor> .
>
>
>
> <DHT22/4578#TemperatureSensor> a sosa:Sensor , ssn:System ;
>   rdfs:comment "The embedded temperature sensor, a specific instance of temperature sensor."@en ;
>   ssn-system:hasOperatingRange <DHT22/4578#TemperatureSensorOperatingRange> ;
>   ssn-system:hasSystemCapability <DHT22/4578#TemperatureSensorCapability> ;
>   ssn:implements <DHT22#Procedure> .
>
> <DHT22/4578#HumiditySensor> a sosa:Sensor , ssn:System ;
>   rdfs:comment "The embedded humidity sensor, a specific instance of humidity sensor."@en ;
>   ssn-system:hasOperatingRange <DHT22/4578#HumiditySensorOperatingRange> ;
>   ssn:implements <DHT22#Procedure> .
>
>
>
> <DHT22/4578#TemperatureSensorOperatingRange> a ssn-system:OperatingRange ;
>   rdfs:comment "The conditions in which the DHT22 temperature sensor is expected to operate."@en ;
>   ssn-system:inCondition <NormalTemperatureCondition> , <NormalHumidityCondition> .
>
> <DHT22/4578#HumiditySensorOperatingRange> a ssn-system:OperatingRange ;
>   rdfs:comment "The conditions in which the DHT22 humidity sensor is expected to operate."@en ;
>   ssn-system:inCondition <NormalTemperatureCondition> , <NormalHumidityCondition> .
>
>
>
> <NormalOperatingCondition> a ssn-system:Condition , schema:PropertyValue ;
>   rdfs:comment "A temperature range of -40 to 80 Celsius."@en ;
>   schema:minValue -40.0 ;
>   schema:maxValue 80.0 ;
>   schema:unitCode qudt-unit-1-1:DegreeCelsius .
>
> <NormalHumidityCondition> a ssn-system:Condition , schema:PropertyValue ;
>   rdfs:comment "A relative humidity range of 5 to 85 %."@en ;
>   schema:minValue 5.0 ;
>   schema:maxValue 85.0 ;
>   schema:unitCode qudt-unit-1-1:Percent .
>
>
>
> <DHT22/4578#TemperatureSensorCapability> a ssn:Property , ssn-system:SystemCapability , schema:PropertyValue ;
>   rdfs:comment "The capabilities of the temperature sensor in normal temperature and humidity conditions." ;
>   ssn-system:inCondition <NormalTemperatureCondition> , <NormalHumidityCondition> ;
>   ssn-system:hasSystemProperty <DHT22/4578#TemperatureSensorAccuracy> , <DHT22/4578#TemperatureSensorSensitivity> , <DHT22/4578#TemperatureSensorRepeatability> , <DHT22/4578#TemperatureSensorFrequency> .
>
> <DHT22/4578#TemperatureSensorAccuracy> a ssn:Property , ssn-system:Accuracy , schema:PropertyValue ;
>   rdfs:comment "The accuracy of the temperature sensor is +-0.5 °C in normal temperature and humidity conditions."@en ;
>   schema:minValue -0.5 ;
>   schema:maxValue 0.5 ;
>   schema:unitCode qudt-unit-1-1:DegreeCelsius .
>
> <DHT22/4578#TemperatureSensorSensitivity> a ssn:Property , ssn-system:Sensitivity , ssn-system:Resolution , schema:PropertyValue ;
>   rdfs:comment "The sensitivity and resolution of the temperature sensor is 0.1 °C in normal temperature and humidity conditions."@en ;
>   schema:value 0.1 ;
>   schema:unitCode qudt-unit-1-1:DegreeCelsius .
>
> <DHT22/4578#TemperatureSensorPrecision> a ssn:Property , ssn-system:Precision , schema:PropertyValue ;
>   rdfs:comment "The precision (= repeatability) of the temperature sensor is +-0.2 °C in normal temperature and humidity conditions."@en ;
>   schema:minValue 0.2 ;
>   schema:maxValue 0.2 ;
>   schema:unitCode qudt-unit-1-1:DegreeCelsius .
>
> <DHT22/4578#TemperatureSensorFrequency> a ssn:Property , ssn-system:Frequency , schema:PropertyValue ;
>   rdfs:comment "The smallest possible time between one observation and the next is 2 s on average."@en ;
>   schema:value 2 ;
>   schema:unitCode qudt-unit-1-1:Second .
>
>
> <observation/1087> rdf:type sosa:Observation ;
>   sosa:madeBySensor <DHT22/4578#TemperatureSensor> ;
>   sosa:usedProcedure <DHT22#Procedure> ;
>   ssn-system:qualityOfObservation <observation/1087#quality> ;
>
>
> # one may classify the quality of observation using some class:
>
> <observation/1087#quality> rdf:type ex:FairQuality .
>
>
> # one may use some other ontology to further qualify this quality.
>
> <observation/1087#quality>
>   ex:evaluatedBy <Tom> ;
>   ex:confidenceValue "6"^^xsd:integer;
>   rdfs:comment """Tom gave a confidence value of 6 out of 10 on this observation."""@en .
>
> # one may use some quantity ontology.
>
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
>
> <observation/1087#quality> rdf:type qudt-1-1:Quantity ;
>   qudt-1-1:quantityValue [
>     rdf:type qudt-1-1:QuantityValue ;
>     qudt-1-1:numericValue "98.4"^^xsd:double ;
>     qudt-1-1:unit qudt-unit-1-1:Percent ] .
> ```

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/dht22-sosa.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 22
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @prefix schema: <http://schema.org/>.
>
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix ssn: <http://www.w3.org/ns/ssn/> .
> @prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .
>
> @prefix rdfp: <https://w3id.org/rdfp/>.
>
> @base <http://example.org/data/> .
>
>
> <DHT22#Procedure> a sosa:Procedure .
>
> <DHT22/4578> a sosa:Platform ;
>   rdfs:comment "DHT22 sensor #4578 contains a humidity and a temperature sensor."@en ;
>   rdfs:seeAlso <https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf> .
>
>
> <DHT22/4578#TemperatureSensor> a sosa:Sensor ;
>   sosa:isHostedBy <DHT22/4578> .
>   rdfs:comment "The embedded temperature sensor, a specific instance of temperature sensor."@en .
>
>
> <observation/1087> a sosa:Observation ;
>   sosa:madeBySensor <DHT22/4578#TemperatureSensor> ;
>   sosa:usedProcedure <DHT22#Procedure> .
> ```

[Show all SOSA and SSN terms] [Show only core SOSA terms]

### B.10 DHT22 Deployment

[Show all SOSA and SSN terms] [Show only core SOSA terms]

This example shows how the conditions (temperature and humidity) in a room may be measured using one or more sensors. Each sensor observes the conditions in its immediate vicinity, and the values are then used to characterize the room.

In Room 145 one of the walls is external in the building, so there is expected to be a temperature gradient across the room, and there are two sensors on different walls. In room 245 there is one sensor on the south wall. Each of these
locations corresponds to a `sosa:Sample` of the entire room. The wall also serves as a `sosa:Platform` on which the sensors are mounted.

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/dht22-deployment.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 23
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @prefix schema: <http://schema.org/>.
>
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix ssn: <http://www.w3.org/ns/ssn/> .
> @prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .
>
> @base <http://example.org/data/> .
>
>
> <Room145> a sosa:FeatureOfInterest ;
>   rdfs:label "Room #145"@en ;
>   sosa:hasSample <Room145/east> ;
>   sosa:hasSample <Room145/south> .
>
>   <Room145/east> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
>     rdfs:label "East wall of room #145."@en ;
>     rdfs:comment "This wall hosts PCB Board 1 with DHT22 temperature and humidity sensor #4578."@en ;
>     sosa:hosts <PCBBoard1> .
>
>   <Room145/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
>     rdfs:label "South wall of room #145."@en ;
>     rdfs:comment "This wall hosts PCB Board 2 with DHT22 temperature and humidity sensor #4579."@en ;
>     sosa:hosts <PCBBoard2> .
>
>
> <Room245> a sosa:FeatureOfInterest ;
>   rdfs:label "Room #245"@en ;
>   sosa:hasProperty <Room245#temperature> , <Room245#humidity> ;
>   sosa:hasSample <Room245/south> .
>
>   <Room245/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
>     rdfs:label "South wall of room #245."@en ;
>     sosa:hosts <PCBBoard3> .
>
>
>
>
>
> <PCBBoard1> a ssn:System , sosa:Platform ;
>   rdfs:label "PCB Board 1"@en ;
>   rdfs:comment "PCB Board 1 hosts DHT22 temperature and humidity sensor #4578 permanently, one can say it has it as one of its subsystems."@en ;
>   sosa:hosts <DHT22/4578> ;
>   ssn:hasSubSystem <DHT22/4578> .
>
>   <DHT22/4578> a ssn:System ;
>     rdfs:label "DHT22 sensor #4578"@en ;
>     sosa:isHostedBy <PCBBoard1> .
>
>
> <PCBBoard2> a ssn:System , sosa:Platform ;
>   rdfs:label "PCB Board 2"@en ;
>   rdfs:comment "PCB Board 2 hosts DHT22 temperature and humidity sensor #4579 permanently, one can say it has it as one of its subsystems."@en ;
>   sosa:hosts <DHT22/4578> ;
>   ssn:hasSubSystem <DHT22/4578> .
>
>   <DHT22/4579> a ssn:System ;
>     rdfs:label "DHT22 sensor #4579."@en ;
>     sosa:isHostedBy <PCBBoard2> .
>
>
> <PCBBoard3> a ssn:System , sosa:Platform ;
>   rdfs:label "PCB Board 3"@en ;
>   rdfs:comment "PCB Board 3 hosts DHT22 temperature and humidity sensor #4580 permanently, one can say it has it as one of its subsystems."@en ;
>   sosa:hosts <DHT22/4578> ;
>   ssn:hasSubSystem <DHT22/4578> .
>
>   <DHT22/4580> a ssn:System ;
>     rdfs:label "DHT22 sensor #4580."@en ;
>     sosa:isHostedBy <PCBBoard3> .
>
>
>
>
> <Room245Deployment> a ssn:Deployment ;
>   rdfs:comment "Deployment of PCB Board 3 on the south wall of room #245 for the purpose of observing the temperature and humidity of room #245."@en ;
>   ssn:deployedOnPlatform <Room245/south> ;
>   ssn:deployedSystem <PCBBoard3> ;
>   ssn:forProperty <Room245#temperature> , <Room245#humidity> .
>
>
> <Room145Deployment> a ssn:Deployment ;
>   rdfs:comment "Deployment of PCB Board 1 and 2 on the east and south wall of room #145, respectively, for the purpose of observing the temperature and humidity of room #145."@en ;
>   ssn:deployedOnPlatform <Room245/east> , <Room245/south> ;
>   ssn:deployedSystem <PCBBoard1> , <PCBBoard2> ;
>   ssn:forProperty <Room145#temperature> , <Room145#humidity> .
> ```

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/dht22-deployment-sosa.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 24
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
> @prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
> @prefix schema: <http://schema.org/>.
>
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
>
> @base <http://example.org/data/> .
>
>
> <Room145> a sosa:FeatureOfInterest ;
>   rdfs:label "Room #145"@en ;
>   sosa:hasSample <Room145/east> ;
>   sosa:hasSample <Room145/south> .
>
>   <Room145/east> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
>     rdfs:label "East wall of room #145."@en ;
>     rdfs:comment "This wall hosts PCB Board 1 with DHT22 temperature and humidity sensor #4578."@en ;
>     sosa:hosts <PCBBoard1> .
>
>   <Room145/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
>     rdfs:label "South wall of room #145."@en ;
>     rdfs:comment "This wall hosts PCB Board 2 with DHT22 temperature and humidity sensor #4579."@en ;
>     sosa:hosts <PCBBoard2> .
>
>
> <Room245> a sosa:FeatureOfInterest ;
>   rdfs:label "Room #245"@en ;
>   sosa:hasProperty <Room245#temperature> , <Room245#humidity> ;
>   sosa:hasSample <Room245/south> .
>
>   <Room245/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
>     rdfs:label "South wall of room #245."@en ;
>     sosa:hosts <PCBBoard3> .
>
>
> <PCBBoard1> a sosa:Platform ;
>   rdfs:label "PCB Board 1"@en ;
>   rdfs:comment "PCB Board 1 hosts DHT22 temperature and humidity sensor #4578 permanently."@en ;
>   sosa:hosts <DHT22/4578> .
>
>   <DHT22/4578> a sosa:Platform ;
>     rdfs:label "DHT22 sensor #4578"@en ;
>     sosa:isHostedBy <PCBBoard1> .
>
>
> <PCBBoard2> a sosa:Platform ;
>   rdfs:label "PCB Board 2"@en ;
>   rdfs:comment "PCB Board 2 hosts DHT22 temperature and humidity sensor #4579 permanentlys."@en ;
>   sosa:hosts <DHT22/4578> .
>
>   <DHT22/4579> a sosa:Platform ;
>     rdfs:label "DHT22 sensor #4579."@en ;
>     sosa:isHostedBy <PCBBoard2> .
>
>
> <PCBBoard3> a sosa:Platform ;
>   rdfs:label "PCB Board 3"@en ;
>   rdfs:comment "PCB Board 3 hosts DHT22 temperature and humidity sensor #4580 permanently."@en ;
>   sosa:hosts <DHT22/4578> .
>
>   <DHT22/4580> a sosa:Platform ;
>     rdfs:label "DHT22 sensor #4580."@en ;
>     sosa:isHostedBy <PCBBoard3> .
> ```

### B.11 IP68 Smart Sensor

This example describes the IP68 Smart Sensor that and some of its capabilities and operating ranges. A specific IP68 Smart Sensor observes the air temperature, and its own battery state.

An RDF file containing a [graph corresponding to this example is available](https://www.w3.org/TR/vocab-ssn/integrated/examples/dht22-deployment-sosa.ttl).
> **Example:**
>
> > **Example:**
> >
> > Example 25
>
> ```
> @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
> @prefix gr: <http://purl.org/goodrelations/v1#> .
> @prefix org: <http://www.w3.org/ns/org#> .
> @prefix schema: <http://schema.org/> .
> @prefix sosa: <http://www.w3.org/ns/sosa/> .
> @prefix ssn: <http://www.w3.org/ns/ssn/> .
> @prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .
> @prefix qudt-unit-1-1: <http://qudt.org/vocab/unit#> .
> @prefix prov: <http://www.w3.org/ns/prov#>.
> @prefix owl: <http://www.w3.org/2002/07/owl#>.
> @prefix seas: <https://w3id.org/seas/>.
> @prefix cdt: <http://w3id.org/lindt/custom_datatypes#>.
>
> @base <https://data.grandlyon.com/> .
>
> <Organization/1> a org:Organization ;
>     owl:sameAs <http://dbpedia.org/page/Metropolis_of_Lyon> .
>
> <Air> a sosa:FeatureOfInterest ;
>   rdfs:label "The air."@en .
>
> <IP68_Outdoor_Temperature_Sensor> a owl:Class , gr:ProductOrServiceModel ;
>   gr:name "IP68 Outdoor Temperature Sensor"@en ;
>   rdfs:label "IP68 Outdoor Temperature Sensor"@en ;
>   rdfs:subClassOf [
>     owl:onProperty ssn-system:hasOperatingRange ;
>     owl:hasValue <IP68_Outdoor_Temperature_Sensor#operatingRange> ] ;
>   rdfs:subClassOf [
>     owl:onProperty ssn-system:hasSystemCapability ;
>     owl:hasValue <IP68_Outdoor_Temperature_Sensor#systemCapability> ] .
>
> <IP68_Outdoor_Temperature_Sensor#operatingRange> a ssn-system:OperatingRange , ssn:Property ;
>   ssn-system:inCondition <IP68_Outdoor_Temperature_Sensor#normalOperatingCondition> .
>
> <IP68_Outdoor_Temperature_Sensor#normalOperatingCondition> a ssn-system:Condition , schema:PropertyValue ;
>   rdfs:comment "A temperature range of -20 to 70 Celsius."@en ;
>   schema:minValue -20.0 ;
>   schema:maxValue 70.0 ;
>   schema:unitCode qudt-unit-1-1:DegreeCelsius .
>
> <IP68_Outdoor_Temperature_Sensor#systemCapability> a ssn:Property , ssn-system:SystemCapability ;
>   rdfs:comment "The sensor capability in normal operating conditions."@en ;
>   ssn-system:hasSystemProperty <IP68_Outdoor_Temperature_Sensor#RFSensitivity> , <IP68_Outdoor_Temperature_Sensor#TemperatureAccuracy> , <IP68_Outdoor_Temperature_Sensor#TemperatureResolution> , <IP68_Outdoor_Temperature_Sensor#BatteryAccuracy> , <IP68_Outdoor_Temperature_Sensor#BatteryResolution> ;
>   ssn-system:inCondition <IP68_Outdoor_Temperature_Sensor#normalOperatingCondition> .
>
> <IP68_Outdoor_Temperature_Sensor#RFSensitivity> a ssn:Property , ssn-system:Sensitivity , schema:PropertyValue ;
>   schema:value -137 ;
>   schema:unitCode qudt-unit-1-1:DecibelReferredToOneMilliwatt .
>
> <IP68_Outdoor_Temperature_Sensor#TemperatureAccuracy> a ssn:Property , ssn-system:Accuracy , schema:PropertyValue ;
>   ssn:forProperty <Air?lat=45.75&long=4.85#temperature> ;
>   schema:minValue -0.2 ;
>   schema:maxValue 0.2 ;
>   schema:unitCode qudt-unit-1-1:DegreeCelsius .
>
> <IP68_Outdoor_Temperature_Sensor#TemperatureResolution> a ssn:Property , ssn-system:Resolution , schema:PropertyValue ;
>   ssn:forProperty <Air?lat=45.75&long=4.85#temperature> ;
>   schema:value 0.0625 ;
>   schema:unitCode qudt-unit-1-1:DegreeCelsius .
>
> <IP68_Outdoor_Temperature_Sensor#BatteryResolution> a ssn:Property , ssn-system:Resolution , schema:PropertyValue ;
>   ssn:forProperty <Sensor/SL-T-P1#battery> ;
>   schema:value 3.937e-3 ;
>   schema:unitCode qudt-unit-1-1:Percent .
>
> <Air?lat=45.75&long=4.85> a sosa:Sample ;
>   rdfs:label "The air at lat 45.75 and long 4.85."@en ;
>   sosa:isSampleOf <Air> ;
>   ssn:hasProperty <Air?lat=45.75&long=4.85#temperature> .
>
> <Air?lat=45.75&long=4.85#temperature> a ssn:Property , sosa:ObservableProperty ;
>   ssn:isPropertyOf <Air?lat=45.75&long=4.85> .
>
> <Sensor/SL-T-P1> a gr:ProductOrService, sosa:Sensor , seas:LoRaCommunicationDevice , <IP68_Outdoor_Temperature_Sensor> ;
>     gr:hasBrand [ a gr:Brand ; gr:name "Sensing Labs"@en ] ;
>     geo:alt 100.0 ;
>     geo:lat 45.75 ;
>     geo:lon 4.85 ;
>     ssn:implements <IP68_Outdoor_Temperature_Sensor#temperatureSensingProcedure> ;
>     ssn:implements <IP68_Outdoor_Temperature_Sensor#batterySensingProcedure> ;
>     ssn:observes <Sensor/SL-T-P1#battery> ;
>     ssn:observes <Air?lat=45.75&long=4.85#temperature> .
>
> <Deployment/SL-T-P1/2017-06-06> a ssn:Deployment ;
>   ssn:deployedSystem <Sensor/SL-T-P1> ;
>   prov:startedAtTime "2017-06-06"^^xsd:date ;
>   prov:wasAssociatedWith <Organization/1> ;
>   ssn:deployedOnPlatform <Tree/1> .
>
> <Observation/5872357#temperature> a sosa:Observation ;
>     sosa:hasSimpleResult "64.5244681928429 Cel"^^cdt:ucum ;
>     sosa:madeBySensor <Sensor/SL-T-P1> ;
>     sosa:hasFeatureOfInterest <Air?lat=45.75&long=4.85> ;
>     sosa:observedProperty <Air?lat=45.75&long=4.85#temperature> ;
>     sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime .
>
> <Observation/5872357#battery> a sosa:Observation ;
>     sosa:hasSimpleResult "73.2 %"^^cdt:ucum ;
>     sosa:madeBySensor <Sensor/SL-T-P1> ;
>     sosa:hasFeatureOfInterest <Sensor/SL-T-P1> ;
>     sosa:observedProperty <Sensor/SL-T-P1#battery> ;
>     sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime .
> ```

### B.12 Examples from O&M

An XML implementation of the Observations and Measurements specification is available from OGC [OandM], known as [OMXML]. Annex C in
that document contains a large set of examples. To assist users of O&M to understand SOSA/SSN, and potentially to migrate services based on OMXML to SOSA/SSN, an RDF file containing a [graph corresponding to the OMXML examples is provided](https://www.w3.org/TR/vocab-ssn/integrated/examples/om-20.ttl).

Note that in some cases the information contained in the OMXML examples goes beyond what is supported directly by SOSA/SSN, so the examples use terms from some other well known RDF vocabularies, such as [GeoSPARQL],
[QUDT], [owl-time], and [prov-o], as well as the sample relations (§5.2) module. In some cases these only approximate the semantics of the OMXML examples. This is indicated in editorial notes embedded in the RDF file. In a few places where there was no well-known RDF implementation matching the requirements,
the details have been omitted.

## D. Change History

A full change-log is available on [GitHub](https://github.com/w3c/sdw/commits/gh-pages/ssn).

## Changes since Original [(https://www.w3.org/2005/Incubator/ssn/XGR-ssn-20110628/)](https://www.w3.org/2005/Incubator/ssn/XGR-ssn-20110628/)

1. The DUL ontology, that was imported in SSN, is no longer imported and all axioms using terms from DUL have been removed from SSN and collected in the DUL-SSN alignment module.
2. The namespace was changed to match the planned namespace for this publication.
3. The modularization as presented here, including the core, is entirely new.

## Changes since 1st Public Working Draft [(http://www.w3.org/TR/2016/WD-vocab-ssn-20160531/)](https://www.w3.org/TR/2016/WD-vocab-ssn-20160531/)

1. Correction to include some SSN terms that were unintentionally dropped from the FPWD. Correction to remove an asserted subclass of owl:Thing that was introduced into FPWD (these were both by-products of the DUL removal).
2. Correction to some https namespace usage that crept into the FPWD.
3. Transition to the new namespace used by the DUL module.
4. Inclusion of the DUL alignment and the old SSN (of the SSN-XG) alignment.
5. ssn:Sensor has been changed to be a subclass of dul:Object instead of dul:Physical Object.
6. Various typography and spelling errors and consistency of expression in annotation properties have been improved. These do not induce any changes in the intended meaning of the terms.
7. Specgen 6 has been used to generate the ontology documentation. The popular sketch of SSN structure has been removed.
8. Object properties ssn:isValueOf, ssn:produces and ssn:featureInObservation, along with a propertychain subproperty of produces and another propertychain subproperty of hasProperty, were introduced unintentionally in the FPWD.

### Changes since 2nd Public Working Draft [(https://www.w3.org/TR/2017/WD-vocab-ssn-20170105/)](https://www.w3.org/TR/2017/WD-vocab-ssn-20170105/)

1. Changed meta prefix declaration to schema
2. Added voaf:Vocabulary class to ontology instances
3. Added dcterms:license statements
4. Added vann:preferredNamespacePrefix and vann:preferredNamespaceUri statements
5. Added SOSA and SSN alignment
6. Added SSN/SOSA alignments with O&M
7. Consistently added Capitalization of all ontology terms in all rdfs:comments
8. Addressed naming inconsistency with changes in name to isObservedBy/observes, madeBySensor/madeObservation
9. Use skos:examples to describe examples of classes/properties
10. Removed history skos:historyNote
11. SOSA-specific changes:
    - Various typography and spelling errors and consistency of expression in annotation properties have been improved
    - Added "sosa:hasResult meta:domainIncludes sosa:Actuation" and "sosa:isResultOf meta:rangeIncludes sosa:Actuation"
    - Changed the defintion of FeatureofInterest to account for actuators
    - Introduced sosa:actsOnProperty and its inverse property sosa:isActedOnBy
    - Added madeBySensor property
    - Renamed invokes and invokedBy to madeActuation and madeByActuator
    - Changed hostedBy to isHostedBy
    - Added Sampler (device) and Sampling (act) to SOSA
    - Added madeSampling and madeBySampler properties
    - Added Sample to range of hasResult, and to domain or isResultOf
    - Added hasSimpleResult and hasResult instead of hasValue
    - Added ObservableProperty and ActuatableProperty
    - Changed rdfs:comment and skos:definition of sosa:Platform
    - Refined sosa:Result
    - Changed sosa:madeByActuator to sosa:actuationMadeBy
    - Added schema:domainIncludes sosa:Sampling to sosa:observedProperty
    - Added schema:rangeIncludes time:TemporalEntity and schema:domainIncludes sosa:Sampling to sosa:phenomenonTime
    - Changed sosa:actuationMadeBy to sosa:madeByActuator
12. SSN-specific changes:
    - Changed syntax and layout in the alignment to SSN of the SSN-XG
    - Refine ssn:Property: ObservableProperty in sosa, Property in ssn, old SSN Property equivalent with ssn:Property
    - Import sosa: "ssn: a owl:Ontology ; owl:imports sosa:."
    - Update prefix for featureOfInterest in ssn:Observation and ssn:Property definition
    - Added skos:examples to several rdfs:comments
    - Changed sub class relation of Accuracy from ssn:MeasurementProperty to ssn:SystemProperty
    - Changed sub class of ssn:Deployment from DeploymentRelatedProcess to DeploymentRelatedProcedure
    - Changed DeploymentRelatedProcess Class to DeploymentRelatedProcedure
    - Changed sub class of ssn:DetectionLimit from ssn:MeasurementProperty to ssn:SystemProperty
    - Deprecated the ssn:Device class
    - Changed sub class of ssn:Drift from ssn:MeasurementProperty to ssn:SystemProperty
    - Changed the rdfs:comment of ssn:Drift to include Actuators
    - Changed sub class of ssn:Frequency from ssn:MeasurementProperty to ssn:SystemProperty
    - Changed sub class of ssn:Latency from ssn:MeasurementProperty to ssn:SystemProperty
    - Changed the rdfs:comment of ssn:Latency to include Actuators
    - Changed the rdfs:comment of ssn:MaintenanceSchedule to reference the System class only
    - Changed MeasurementCapability to SystemCapability and changed its axiom from hasMeasurementProperty to hasSystemProperty
    - Changed MeasurementProperty to SystemProperty
    - Changed sub class of ssn:MeasurementRange from ssn:MeasurementProperty to ssn:SystemProperty and changed its rdfs:comment
    - Changed the Observation’s classes qualified property restriction from ssn:featureOfInterest to sosa:hasFeatureOfInterest and ssn:FeatureOfInterest to sosa:FeatureOfInterest
    - Changed the Observation’s class universal property restrictions from ssn:observationResult to sosa:hasResult and ssn:SensorOutput to sosa:Result
    - Changed the Observation’s class universal property restriction from ssn:observedProperty to sosa:observedProperty and ssn:ObservedProperty to sosa:ObservableProperty
    - Changed the Observation’s class qualified property restriction from ssn:observedProperty to sosa:observedProperty and ssn:ObservedProperty to sosa:ObservableProperty
    - Changed the Observation’s class qualified property restrictions from ssn:observedBy to sosa:madeBySensor and ssn:Sensor to sosa:Sensor
    - Changed the Observation’s class universal property restrictions from ssn:sensingMethodUsed to sosa:usedProcedure and sosa:usedProcedure
    - Changed the Observation’s class qualified property restrictions from ssn:sensingMethodUsed to sosa:usedProcedure and sosa:usedProcedure
    - Changed the minimum cardinality restriction on the Observation class from ssn:observationSamplingTime to sosa:resultTime
    - Removed ssn:ObservationValue Class
    - Changed rdfs:comment of ssn:OperatingPowerRange
    - Changed rdfs:comment of ssn:OperatingProperty
    - Changed rdfs:comment of ssn:OperatingRange
    - Changed rdfs:comment of ssn:Output
    - Changed the Platform’s class universal property restrictions from ssn:attachedSystem
    - Changed sub class of ssn:Precision from ssn:MeasurementProperty to ssn:SystemProperty
    - Changed ssn:Process to sosa:Procedure
    - Changed rdfs:comment for ssn:Property
    - Changed the Property’s class existential property restrictions class range from ssn:FeatureOfInterest to sosa:FeatureOfInterest
    - Changed rdfs:comment for ssn:Resolution
    - Changed sub class of ssn:Resolution from ssn:MeasurementProperty to ssn:SystemProperty
    - Changed rdfs:comment for ssn:ResponseTime
    - Changed sub class of ssn:ResponseTime from ssn:MeasurementProperty to ssn:SystemProperty
    - Changed rdfs:comment for ssn:Selectivity
    - Changed sub class of ssn:Selectivitye from ssn:MeasurementProperty to ssn:SystemProperty
    - Removed ssn:Sensing Class
    - Removed ssn:SensingDevice Class
    - Changed the Sensor classes existential property restrictions from ssn:hasMeasurementCapability to ssn:SystemCapability and ssn:MeasurementCapability to ssn:SystemCapability
    - Changed the Sensor classes universal property restriction on ssn:observes to sosa:observes
    - Changed the Sensor classes existential property restrictions range class from ssn:Sensing to sosa:Procedure
    - Removed ssn:SensorDataSheet Class
    - Removed ssn:SensorInput Class
    - Removed ssn:SensorOutput Class
    - Changed rdfs:comment for ssn:Stimulus
    - Changed rdfs:comment for ssn:SurvivalProperty
    - Changed rdfs:comment for ssn:SurvivalRange
    - Changed rdfs:comment for ssn:System
    - Changed the System’s class universal property restriction from ssn:onPlatform to sosa:isHostedBy and ssn:Platform to sosa:Platform
    - Added a universal property restriction to the System’s class on the hasSystemCapability property with a class range of SystemCapability
    - Changed rdfs:comment for ssn:SystemLifetime
    - Added Property Restrictions to SOSA:ActuatableProperty for sosa:isActedOnBy
    - Added Property Restrictions to SOSA:Actuation for sosa:hasFeatureOfInterest, sosa:hasResult, sosa:resultTime, sosa:usedProcedure, sosa:hasFeatureOfInterest and sosa:actuationMadeBy
    - Added ssn:ActuationRange Class
    - Added Property Restrictions to sosa:Actuator for ssn:implements, ssn:forProperty and sosa:MadeActuation and sosa:hasResult
    - Removed ssn:DeploymentRelatedProcess
    - Added Property Restrictions to ssn:Input for ssn:hasInput
    - Added Property Restriction to ssn:MeasurementRange
    - Added Property Restrictions to sosa:ObservableProperty for isObservedBy, inverseOf sosa:observedProperty and inverseOf ssn:isProxyFor
    - Added Property Restrictions to ssn:OperatingProperty
    - Added Property Restrictions to ssn:Precision
    - Added Property Restrictions to sosa:Result
    - Added Property Restrictions to sosa:Sample
    - Added Property Restrictions to sosa:Sampler
    - Added Property Restrictions to sosa:Sampling
    - Added Property Restrictions to ssn:SystemProperty
    - Added sub class of System relation to sosa:Sensor
    - Added Property Restrictions to ssn:Stimulus
    - Added Property Restrictions to ssn:SurvivalProperty
    - Added Property Restrictions to ssn:SurvivalRange
    - Added Property Restrictions to ssn:System
    - Removed attachedSystem property
    - Changed rdfs:comment for ssn:deployedOnPlatform
    - Removed ssn:deploymentProcessPart
    - Changed rdfs:comment for ssn:detects
    - Removed ssn:featureOfInterest property
    - Changed rdfs:comment for ssn:forProperty and added a skos:example property
    - Changed rdfs:comment for ssn:hasDeployment
    - Renamed ssn:hasMeasurementCapability to ssn:hasSystemCapability and changed its rdf:comment
    - Renamed ssn:hasMeasurementProperty to ssn:hasSystemProperty and changed its rdf:comment
    - Changed rdfs:comment for ssn:hasOperatingProperty
    - Changed rdfs:comment for ssn:hasSurvivalProperty
    - Changed rdfs:comment for ssn:hasSurvivalRange
    - Changed rdfs:comment for ssn:implementedBy
    - Changed rdfs:comment for ssn:implements
    - Changed rdfs:comment for ssn:inCondition and added skos:example property
    - Changed rdfs:comment for ssn:inDeployment and added skos:example property
    - Removed ssn:isProducedBy property
    - Changed rdfs:comment for ssn:isPropertyOf
    - Changed rdfs:comment for ssn:isProxyFor and added skos:example property
    - Removed ssn:madeObservation property
    - Removed ssn:observationResult property
    - Removed ssn:observationResultTime property
    - Removed ssn:observationSamplingTime property
    - Removed ssn:observedProperty property
    - Changed ssn:observes to sosa:observes, removed sub-property chain for sosa:observes and defined it as sub-property of ssn:forProperty
    - Removed ssn:ofFeature property
    - Removed ssn:onPlatform property
    - Changed rdfs:comment for ssn:qualityOfObservation
    - Removed ssn:sensingMethodUsed property
    - Added rdfs:comment for ssn:hasInput
    - Changed sosa:Platform subclass of dul:PhysicalObject
    - Removed axiom FunctionalProperty(ssn:isPropertyOf) to account for generic modeling of ssn:Property such as ex:Temperature

### Changes since 3rd Public Working Draft [(https://www.w3.org/TR/2017/WD-vocab-ssn-20170504/)](https://www.w3.org/TR/2017/WD-vocab-ssn-20170504/)

1. Fixed colouring of O&M module in Figure 1 to be normative
2. Updated figures in the Axiomatization section
3. Added examples to Appendix
4. Added a "at risk" section in Status of This Document section
5. Reorganized specification sections to have:
   - One non-normative overview section, with links to the examples that showcase the terms in that section
   - The normative specification section
   - Moved ssn:qualityOfObservation, properties related to system capabilities, operating range, and survival range, to horizontal ontology module http://www.w3.org/ns/ssn/systems/ marked at risk
6. Added new horizontal module for System Capabilities to Figure 1
7. Fixed errors in class alignments in Dolce-Ultralite Alignment Module, ssn:Sensor to sosa:Sensor, ssn:FeatureOfInterest to sosa:FeatureOfInterest and sosa:Deployment to ssn:Deployment
8. Fixed errors in property alignments in Dolce-Ultralite Alignment Module, ssn:usedProcedure to sosa:usedProcedure
9. Applied consistent use of Manchester OWL Syntax in all axioms in SSN/SOSA
10. Fixed error in sosa:actsOnProperty axiom of sosa:Actuation, i.e. changed Qualified Cardinality to Minimum Cardinality
11. Fixed error in the use of Hash URIs and SlashURIs in the System Capabilities module
12. Combined Location and Forecasting in one section and added an example how to model Quantity Values and Unit of Measures
13. Added Wide Review Section and Exit Criteria Section
14. Switched Horizontal Segmentation and Vertical Segmentation sections around
15. Requested bug fixes to correct the SSN/SOSA alignment to DUL

### Changes since W3C Candidate Recommendation 11 July 2017 [(https://www.w3.org/TR/2017/CR-vocab-ssn-20170711/)](https://www.w3.org/TR/2017/CR-vocab-ssn-20170711/)

1. Made System Capabilities Module informative as of exit criteria
2. Fixed wrong link in Origins of SSN and SOSA Section to point to Section 6.1
3. Added Coal Oil Point Reserve and IP68 Smart Sensor examples
4. Fixed inconsistency in Fig. 6 & 7, i.e. defined the range of property sosa:isActedOnBy as sosa:Actuation
5. Removed Features at Risk section
6. Removed Candidate Recommendation Exit Criteria section

## E. References

### E.1 Normative references

[owl-time]

[Time Ontology in OWL](https://www.w3.org/TR/owl-time/). Simon Cox; Chris Little. W3C. 19 October 2017. W3C Recommendation. URL: <https://www.w3.org/TR/owl-time/>

### E.2 Informative references

[GeoSPARQL]

[GeoSPARQL - A Geographic Query Language for RDF Data](http://www.opengeospatial.org/standards/geosparql). Matthew Perry; John Herring.10 September 2012. URL: <http://www.opengeospatial.org/standards/geosparql>

[ISO-19109]

[Geographic information -- Rules for application schema](https://www.iso.org/standard/59193.html). ISO. December 2015. URL: <https://www.iso.org/standard/59193.html>

[ISO-19150-2]

[Geographic information -- Ontology -- Part 2: Rules for developing ontologies in the Web Ontology Language (OWL)](https://www.iso.org/standard/57466.html). ISO. July 2015. URL: <https://www.iso.org/standard/57466.html>

[Lefrancois-et-al-2017]

[The SEAS Knowledge Model](https://w3id.org/seas/SEAS-D2_2-SEAS-Knowledge-Model.pdf). Maxime Lefrançois; Jarmo Kalaoja; Takoua Ghariani; Antoine Zimmermann. ITEA2 12004 Smart Energy Aware Systems. 2017. Deliverable
2.2. URL: <https://w3id.org/seas/SEAS-D2_2-SEAS-Knowledge-Model.pdf>

[OBOE]

[OBOE: the Extensible Observation Ontology, version 1.1](https://dx.doi.org/10.5063/F11C1TTM). Mark Schildhauer; Matthew B. Jones; Shawn Bowers; Joshua Madin; Sergeui Krivov; Deana Pennington; Ferdinando Villa; Benjamin
Leinfelder; Christopher Jones; Margaret O'Brien.2016. URL: [http://dx.doi.org/10.5063/F11C1TTM](https://dx.doi.org/10.5063/F11C1TTM)

[OM-Heavy]

[An explicit OWL representation of ISO/OGC Observations and Measurements](http://ceur-ws.org/Vol-1063/paper1.pdf) . S.J.D. Cox. CEUR: 6th International Conference on Semantic Sensor Networks. 2013. URL: <http://ceur-ws.org/Vol-1063/paper1.pdf>

[OM-Lite]

[Ontology for observations and sampling features, with alignments to existing models](https://content.iospress.com/articles/semantic-web/sw214). S.J.D. Cox. Semantic Web. 2017. URL: <https://content.iospress.com/articles/semantic-web/sw214>

[OMXML]

[Observations and Measurements - XML Implementation](http://portal.opengeospatial.org/files/41510). S.J.D. Cox. Open Geospatial Consortium. 2010. URL: <http://portal.opengeospatial.org/files/41510>

[OandM]

[Observations and Measurements (O&M)](http://www.opengeospatial.org/standards/om). Simon Cox. Open Geospatial Consortium. 2011. URL: <http://www.opengeospatial.org/standards/om>

[QUDT]

[QUDT - Quantities, Units, Dimensions and Data Types Ontologies](http://www.qudt.org/). Ralph Hodgson; Paul J. Keller; Jack Hodges; Jack Spivak.18 March 2014. URL: <http://www.qudt.org/>

[Rijgersberg-et-al-2013]

[Ontology of Units of Measure and Related Concepts](http://www.semantic-web-journal.net/content/ontology-units-measure-and-related-concepts). Hajo Rijgersberg; Mark van Assem; Jan Top. Semantic Web journal, IOS
Press. 2013. URL: <http://www.semantic-web-journal.net/content/ontology-units-measure-and-related-concepts>

[SDW-BP]

[Spatial Data on the Web Best Practices](https://www.w3.org/TR/sdw-bp/). Jeremy Tandy; Linda van den Brink; Payam Barnaghi. W3C. 11 May 2017. W3C Note. URL: <https://www.w3.org/TR/sdw-bp/>

[SSN-PROV]

[Sensor Data Provenance: SSNO and PROV-O Together at Last](http://ceur-ws.org/Vol-1401/paper-05.pdf). Michael Compton; David Corsar; Kerry Taylor. CEUR: 7th International Conference on Semantic Sensor Networks.
2014. URL: <http://ceur-ws.org/Vol-1401/paper-05.pdf>

[SSNO]

[The SSN ontology of the W3C semantic sensor network incubator group](http://www.sciencedirect.com/science/article/pii/S1570826812000571). Michael Compton; Payam Barnaghi; Luis Bermudez; Raúl García-Castro; Oscar
Corcho; Simon Cox; John Graybeal; Manfred Hauswirth; Cory Henson; Arthur Herzog; Vincent Huang; Krzysztof Janowicz; W. David Kelsey; Danh Le Phuoc; Laurent Lefort; Myriam Leggieri; Holger Neuhaus; Andriy Nikolov; Kevin Page; Alexandre
Passant; Amit Sheth; Kerry Taylor. Web Semantics: Science, Services and Agents on the World Wide Web, 17:25-32 . December 2012. URL: <http://www.sciencedirect.com/science/article/pii/S1570826812000571>

[SSO-Pattern]

[The Stimulus-Sensor-Observation Ontology Design Pattern and its Integration into the Semantic Sensor Network Ontology](http://ceur-ws.org/Vol-668/paper12.pdf). Krzysztof Janowicz; Michael Compton. CEUR: Proceedings
of the 3rd International Workshop on Semantic Sensor Networks (SSN10). 2010. URL: <http://ceur-ws.org/Vol-668/paper12.pdf>

[SensorML]

[SensorML: Model and XML Encoding Standard 2.0](http://portal.opengeospatial.org/files/55939). Mike Botts; Alex Robin. OGC. 2014. Encoding Standard, OGC 12-000. URL: <http://portal.opengeospatial.org/files/55939>

[owl2-syntax]

[OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition)](https://www.w3.org/TR/owl2-syntax/). Boris Motik; Peter Patel-Schneider; Bijan Parsia. W3C. 11 December 2012. W3C
Recommendation. URL: <https://www.w3.org/TR/owl2-syntax/>

[prov-dm]

[PROV-DM: The PROV Data Model](https://www.w3.org/TR/prov-dm/). Luc Moreau; Paolo Missier. W3C. 30 April 2013. W3C Recommendation. URL: <https://www.w3.org/TR/prov-dm/>

[prov-o]

[PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/). Timothy Lebo; Satya Sahoo; Deborah McGuinness. W3C. 30 April 2013. W3C Recommendation. URL: <https://www.w3.org/TR/prov-o/>

[prov-overview]

[PROV-Overview](https://www.w3.org/TR/prov-overview/). Paul Groth; Luc Moreau. W3C. 30 April 2013. W3C Note. URL: <https://www.w3.org/TR/prov-overview/>
