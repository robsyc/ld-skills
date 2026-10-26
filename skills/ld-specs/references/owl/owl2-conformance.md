---
title: "OWL 2 Web Ontology Language Conformance (Second Edition)"
source: https://www.w3.org/TR/owl2-conformance/
family: owl
status: W3C Recommendation
spec_date: 2012-12-11
fetched: 2026-10-26
---

# OWL 2 Web Ontology Language Conformance (Second Edition)

> Conformance criteria and test types.

## Contents

- Abstract
    - May Be Superseded
    - Summary of Changes
    - Please Send Comments
    - Endorsed By W3C
    - Patents
- 1 Introduction
- 2 Conformance (Normative)
  - 2.1 Document Conformance
    - 2.1.1 Syntactic Conformance
  - 2.2 Tool Conformance
    - 2.2.1 Entailment Checker
    - 2.2.2 Query Answering Tool
- 3 Test Cases
  - 3.1 Test Types
    - 3.1.1 Syntactic Tests
    - 3.1.2 Semantic Tests
  - 3.2 Test Case Format
    - 3.2.1 Input Ontologies
    - 3.2.2 Type
    - 3.2.3 Normative Syntax
    - 3.2.4 Applicable Semantics
    - 3.2.5 Species
    - 3.2.6 Profiles
    - 3.2.7 Imported Ontologies
    - 3.2.8 Status
    - 3.2.9 Identifier
    - 3.2.10 Creator
    - 3.2.11 Description
    - 3.2.12 Specification Reference
    - 3.2.13 Issue Reference
    - 3.2.14 Complete Test Ontology
  - 3.3 Test Case Repositories
  - 3.4 Approval Process Overview
  - 3.5 Changes From WebOnt Tests
    - 3.5.1 Formatting Changes
    - 3.5.2 Changes to Test Types
    - 3.5.3 Changes to Process
- 4 Appendix: An Inconsistent Ontology
- 5 Appendix: Change Log (Informative)
  - 5.1 Changes Since Recommendation
  - 5.2 Changes Since Proposed Recommendation
  - 5.3 Changes Since Candidate Recommendation
- 6 Acknowledgments
- 7 References

---

---

## Abstract

The OWL 2 Web Ontology Language, informally OWL 2, is an ontology language for the Semantic Web with formally defined meaning. OWL 2 ontologies provide classes, properties, individuals, and data values and are stored as Semantic Web documents. OWL 2 ontologies can be used along with information written in RDF, and OWL 2 ontologies themselves are primarily exchanged as RDF documents. The OWL 2 [Document Overview](https://www.w3.org/TR/2012/REC-owl2-overview-20121211/ "Document Overview") describes the overall state of OWL 2, and should be read before other OWL 2 documents.

This document describes the conditions that OWL 2 tools must satisfy in order to be conformant with the language specification. It also presents a common format for OWL 2 test cases that both illustrate the features of the language and can be used for testing conformance.

#### May Be Superseded

*This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at http://www.w3.org/TR/.*

#### Summary of Changes

There have been no [substantive](https://www.w3.org/2005/10/Process-20051014/tr#substantive-change) changes since the [previous version](https://www.w3.org/TR/2012/PER-owl2-conformance-20121018/). For details on the minor changes see the change log (§5) and [color-coded diff](https://www.w3.org/TR/2012/REC-owl2-conformance-20121211/diff-from-20121018).

#### Please Send Comments

Please send any comments to <public-owl-comments@w3.org> ([public archive](http://lists.w3.org/Archives/Public/public-owl-comments/)). Although work on this document by the [OWL Working Group](https://www.w3.org/2007/OWL/) is complete, comments may be addressed in the [errata](https://www.w3.org/2007/OWL/errata) or in future revisions. Open discussion among developers is welcome at <public-owl-dev@w3.org> ([public archive](http://lists.w3.org/Archives/Public/public-owl-dev/)).

#### Endorsed By W3C

*This document has been reviewed by W3C Members, by software developers, and by other W3C groups and interested parties, and is endorsed by the Director as a W3C Recommendation. It is a stable document and may be used as reference material or cited from another document. W3C's role in making the Recommendation is to draw attention to the specification and to promote its widespread deployment. This enhances the functionality and interoperability of the Web.*

#### Patents

*This document was produced by a group operating under the [5 February 2004 W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy-20040205/). W3C maintains a [public list of any patent disclosures](https://www.w3.org/2004/01/pp-impl/41712/status) made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent.*

---

## 1 Introduction

This document describes conformance conditions for OWL 2, and introduces the format of OWL 2 test cases that are provided as part of the OWL 2 Test Case Repository [OWL 2 Test Cases]. Conformance conditions are described for both OWL 2 documents and for tools that process such documents. In particular, the conformance conditions for an OWL 2 entailment checker are described in some detail.

A categorization and common format of test cases is presented. The purpose of test cases is to illustrate various features and to help in testing conformance. The provided set of test cases is "incomplete" in the sense that passing all the tests does not prove that a given system conforms to the OWL 2 specification; failing a test does, however, prove that the system does not conform to the specification. The presented format is intended to facilitate the use of tests by OWL system developers, e.g., in a test harness, as well as the extension of the test suite with new tests.

This document does not contain actual test cases. Test cases that have been approved by the Working Group can be found in the OWL 2 Test Case Repository [OWL 2 Test Cases], and a public test case repository [Contributed Test Cases] is provided as a platform for collecting further test cases even after the termination of the Working Group.

The italicized keywords *MUST*, *MUST NOT*, *SHOULD*, *SHOULD NOT*, and *MAY* are used to specify normative features of OWL 2 documents and tools, and are interpreted as specified in RFC 2119 [RFC 2119].

## 2 Conformance (Normative)

This section describes conformance conditions for OWL 2 documents and tools. In particular, it describes the syntactic conditions that characterize OWL 2 ontology documents, including those that conform to the various OWL 2 profiles [OWL 2 Profiles], and the syntactic and semantic conditions that *MUST* be satisfied by conformant OWL 2 tools.

### 2.1 Document Conformance

Several syntaxes have been defined for OWL 2 ontology documents, some or all of which could be used by OWL 2 tools for exchanging documents. However, conformant OWL 2 tools that take ontology documents as input(s) *MUST* accept ontology documents using the RDF/XML serialization [OWL 2 RDF Mapping], and conformant OWL 2 tools that publish ontology documents *MUST* be able to publish them in the RDF/XML serialization if asked to do so (e.g., via HTTP content negotiation), provided that the ontology can be so serialized. OWL 2 tools *MAY* also accept and/or publish ontology documents using other serializations, for example the XML serialization [OWL 2 XML].

#### 2.1.1 Syntactic Conformance

For documents using the RDF/XML serialization, syntactic conformance is defined as follows:

An **OWL 2 Full ontology document** is any RDF/XML document [RDF Syntax].

An **OWL 2 DL ontology document** is an OWL 2 Full ontology document that can be successfully parsed using the [canonical parsing process](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Canonical_Parsing_of_OWL_2_Ontologies "Syntax") as defined in the OWL 2 Syntax specification [OWL 2 Specification] and the [procedure for mapping from RDF graphs to the structural specification](https://www.w3.org/TR/2012/REC-owl2-mapping-to-rdf-20121211/#Mapping_from_RDF_Graphs_to_the_Structural_Specification "Mapping to RDF Graphs") described in the OWL 2 Mapping to RDF Graphs [OWL 2 RDF Mapping] to produce an instance of the OWL 2 ontology class satisfying all of the restrictions described in [Section 3 of the OWL 2 Syntax specification](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Ontologies "Syntax") [OWL 2 Specification].

An **OWL 2 EL ontology document** is an OWL 2 DL ontology document where the corresponding instance of the OWL 2 ontology class satisfies the definition of an OWL 2 EL ontology given in the OWL 2 Profiles specification [OWL 2 Profiles].

An **OWL 2 QL ontology document** is an OWL 2 DL ontology document where the corresponding instance of the OWL 2 ontology class satisfies the definition of an OWL 2 QL ontology given in the OWL 2 Profiles specification [OWL 2 Profiles].

An **OWL 2 RL ontology document** is an OWL 2 DL ontology document where the corresponding instance of the OWL 2 ontology class satisfies the definition of an OWL 2 RL ontology given in the OWL 2 Profiles specification [OWL 2 Profiles].

For documents using other serializations, conformance is a direct consequence of the relevant serialization specification, the OWL 2 Syntax specification [OWL 2 Specification] (in particular, the definition of the [canonical parsing process](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Canonical_Parsing_of_OWL_2_Ontologies "Syntax")), and the OWL 2 Profiles specification [OWL 2 Profiles].
> **Example:**
>
> An XML document is an OWL 2 DL ontology document iff it validates against the OWL 2 XML Schema [OWL 2 XML], it can be successfully parsed using the [canonical parsing process](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Canonical_Parsing_of_OWL_2_Ontologies "Syntax") as defined in the OWL 2 Syntax specification [OWL 2 Specification], and the resulting instance of the OWL 2 ontology class satisfies all of the restrictions described in [Section 3 of the OWL 2 Syntax specification](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Ontologies "Syntax") [OWL 2 Specification]; it is an OWL 2 EL (respectively QL, RL) ontology document iff the resulting instance of the OWL 2 ontology class satisfies the definition of an OWL 2 EL (respectively QL, RL) ontology given in the OWL 2 Profiles specification [OWL 2 Profiles].

Note that:

1. The conditions for document conformance are entirely syntactic and say nothing about semantics. For example, an OWL 2 DL ontology document is simply an OWL 2 Full ontology document that satisfies certain syntactic constraints, and it could be taken as input by tools that use either the Direct Semantics [OWL 2 Direct Semantics] or the RDF-Based Semantics [OWL 2 RDF-Based Semantics].
2. OWL 2 Profiles may support only a reduced set of datatypes. This is, however, a syntactic condition that must be met by documents in order to fall within the relevant profile, and the semantic conditions on the supported datatypes are unchanged, i.e., they are defined by the OWL 2 datatype map. Unsupported datatypes cannot occur in conforming documents, so syntactic and semantic conditions on these datatypes are irrelevant and can be ignored.

### 2.2 Tool Conformance

An OWL 2 tool takes one or more OWL 2 ontology documents and checks some (syntactic or semantic) condition. A given tool is characterized by three largely independent parameters:

- the ontology documents it accepts (Full, DL, EL, QL or RL);
- the semantics it applies (Direct [OWL 2 Direct Semantics] or RDF-Based [OWL 2 RDF-Based Semantics]).

When the Direct Semantics are being applied, semantic conditions are defined with respect to ontology structures (i.e., instances of the Ontology class as defined in the OWL 2 Syntax specification [OWL 2 Specification]), and we denote with *Ont(d)* the ontology structure corresponding to an input ontology document *d*. When the RDF-Based Semantics are being applied, semantic conditions are defined with respect to RDF graphs, and we denote with *Ont(d)* the RDF graph corresponding to an input ontology document *d*.

As noted above, any conformant OWL 2 tool *MUST* accept ontology documents using the RDF/XML serialization [OWL 2 RDF Mapping]. Given an ontology document *d* in the RDF/XML serialization, for a tool applying the Direct Semantics, *Ont(d)* denotes the ontology structure obtained by applying to *d* the [canonical parsing process](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Canonical_Parsing_of_OWL_2_Ontologies "Syntax") as defined in the OWL 2 Syntax specification [OWL 2 Specification] using, in steps
2.2 and 3.3, the procedure for mapping from RDF graphs to the structural specification described in the OWL 2 Mapping to RDF Graphs [OWL 2 RDF Mapping]; for a tool applying the RDF-Based Semantics, *Ont(d)* simply denotes the RDF graph corresponding to *d*, as defined in the RDF/XML Syntax Specification [RDF Syntax].

A conformant OWL 2 tool *MAY* also accept ontology documents using other serializations, for example Turtle [Turtle] or the XML Serialization [OWL 2 XML]. Alternative RDF serializations are treated in much the same way as RDF/XML, i.e., *Ont(d)* denotes either the ontology structure obtained from *d* via the procedure for mapping from RDF graphs to the structural specification or the RDF graph corresponding to *d*, depending on the semantics being applied. When using non-RDF serializations, e.g., the XML Serialization [OWL 2 XML], *Ont(d)* denotes either the ontology structure obtained from *d* using the canonical parsing process as defined in the OWL 2 Syntax specification [OWL 2 Specification], or the RDF graph obtained by applying the OWL 2 Mapping to RDF Graphs [OWL 2 RDF Mapping] to the ontology structure obtained from *d*, depending on the semantics being applied.

The conformance conditions related to entailment checking and query answering are defined below. Similar conditions would apply to other OWL 2 tools. In particular, they *MUST* be consistent with the Direct Semantics [OWL 2 Direct Semantics] and/or the RDF-Based Semantics [OWL 2 RDF-Based Semantics].

#### 2.2.1 Entailment Checker

An OWL 2 entailment checker takes as input two OWL 2 ontology documents *d1* and *d2* and checks whether *Ont(d1)* entails *Ont(d2)* with respect to either the Direct Semantics [OWL 2 Direct Semantics] or the RDF-Based Semantics [OWL 2 RDF-Based Semantics]. When using the Direct Semantics, *Ont(d1)* and *Ont(d2)* denote ontology structures that satisfy all of the restrictions on OWL 2 ontologies described in [Section 3 of the OWL 2 Syntax specification](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Ontologies "Syntax") [OWL 2 Specification]; when using the RDF-Based Semantics, *Ont(d1)* and *Ont(d2)* denote RDF graphs. Additionally, an OWL 2 entailment checker:

- *MUST* provide a means to determine any limits it has on datatype lexical forms – they could, for example, be listed in supporting documentation (see [Section 4 of the OWL 2 Syntax specification](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Datatype_Maps "Syntax") [OWL 2 Specification]); and
- *MUST* provide a means to determine the semantics it uses (either the Direct Semantics [OWL 2 Direct Semantics] or the RDF-Based Semantics [OWL 2 RDF-Based Semantics]) – for example, by specifying in its supporting documentation which of the two semantics it uses.

An OWL 2 entailment checker returns a single result, being True, False, Unknown or Error. True indicates that the relevant entailment holds; False indicates that the relevant entailment does not hold; Unknown indicates that the algorithm used by the checker is not able to determine if the entailment holds; Error indicates that the checker encountered an error condition such as receiving an invalid input or exceeding resource limits. While sometimes needed (for example, for pragmatic reasons), Unknown and Error are not desired responses for valid inputs.

Additionally, an OWL 2 entailment checker:

- *MUST* return Error if the parsing process fails (for example, due to network errors);
- *MUST* return Error if an input document uses datatypes that are not supported by its datatype map or datatype lexical forms that exceed any limits it has on datatype lexical forms – for example, very large integers (see [Section 4 of the OWL 2 Syntax specification](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Datatype_Maps "Syntax") [OWL 2 Specification]); and
- *MUST* return Error if the computation fails, for example as a result of exceeding resource limits.

Five different conformance classes of OWL 2 entailment checkers are defined:

**An OWL 2 Full entailment checker** is an OWL 2 entailment checker that takes OWL 2 Full ontology documents as input. It *MUST* return True only when *Ont(d1)* entails *Ont(d2)*, and it *MUST* return False only when *Ont(d1)* does not entail *Ont(d2)*. It *SHOULD NOT* return Unknown.

**An OWL 2 DL entailment checker** is an OWL 2 entailment checker that takes OWL 2 DL ontology documents as input. It *MUST* return True only when *Ont(d1)* entails *Ont(d2)*, and it *MUST* return False only when *Ont(d1)* does not entail *Ont(d2)*. It *SHOULD NOT* return Unknown.

**An OWL 2 EL entailment checker** is an OWL 2 entailment checker that takes OWL 2 EL ontology documents as input. It *MUST* return True only when *Ont(d1)* entails *Ont(d2)*, and it *MUST* return False only when *Ont(d1)* does not entail *Ont(d2)*. It *SHOULD NOT* return Unknown.

**An OWL 2 QL entailment checker** is an OWL 2 entailment checker that takes OWL 2 QL ontology documents as input. It *MUST* return True only when *Ont(d1)* entails *Ont(d2)*, and it *MUST* return False only when *Ont(d1)* does not entail *Ont(d2)*. It *SHOULD NOT* return Unknown.

**An OWL 2 RL entailment checker** is an OWL 2 entailment checker that takes OWL 2 Full ontology documents as input. It *MUST* return True only when *Ont(d1)* entails *Ont(d2)*, and it *MUST* return False only when *Ont(d1)* does not entail *Ont(d2)*. If applying the Direct Semantics, it *SHOULD NOT* return Unknown. If applying the RDF-Based Semantics, it *SHOULD NOT* return Unknown if it is possible to derive True using the OWL 2 RL/RDF rules; more formally, it *SHOULD NOT* return Unknown if *FO(Ont(d1))* ∪ *R* entails *FO(Ont(d2))* under the standard first-order semantics, where *R* denotes the OWL 2 RL/RDF rules, and *FO(Ont(di))* denotes the first-order theory corresponding to *Ont(di)* in which triples are represented using the T predicate – that is, T(s, p, o) represents an RDF triple with the subject s, predicate p, and the object o.

Note that it follows from [Theorem PR1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Theorem-PR1 "Profiles") of Profiles [OWL 2 Profiles] that it is always safe for an OWL 2 RL entailment checker using the RDF-Based Semantics to return False if:

- *d1* and *d2* are OWL 2 RL ontology documents;
- *Ont(d1)* and *Ont(d2)* satisfy the constraints described in [Theorem PR1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Theorem-PR1 "Profiles"); and
- it is not possible to derive True using the OWL 2 RL/RDF rules (see above for a more formal definition of what this means).

An OWL 2 entailment checker is **terminating** if, given sufficient resources (memory, addressing space, etc.), it will always return True, False, or Unknown in a finite amount of time (i.e., CPU cycles) on syntactically-valid inputs; it is **complete** if, given sufficient resources, it will always return True or False on syntactically-valid inputs.

#### 2.2.2 Query Answering Tool

Query answering is closely related to entailment checking (see [Section 2.5](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/#Inference_Problems "Direct Semantics") of the OWL 2 Direct Semantics [OWL 2 Direct Semantics]). A query can be thought of as an ontology *Q* in which some of the terms have been replaced by variables *x1, ..., xn*. Given an ontology *O*, a tuple *t = <t1, ..., tn>* is **an** answer for *Q* with respect to *O* if *O* entails *Q[x/t]*, where *Q[x/t]* is derived from *Q* by substituting the variables *x1, ..., xn* with *t1, ..., tn*; **the** answer to *Q* with respect to *O* is the set of all such tuples.

Although highly inefficient in practice, query answering could be performed simply by iterating through all possible n-tuples formed from terms occurring in *O* and checking the corresponding entailment using an OWL 2 entailment checker. The properties of OWL 2 entailment checkers mean that the resulting answer will always be **sound**, i.e., every tuple occurring in the answer set is an answer to the query. If any one of the entailment checks might return Unknown, then the answer to the query may be **incomplete**, i.e., there may exist a tuple *t* that is an answer to the query but that does not occur in the answer set; implementations *SHOULD* issue a warning in this case.

The properties of OWL 2 Full, DL, EL and QL entailment checkers mean that a query answering tool based on such an entailment checker *SHOULD* be both sound and complete. In the case of OWL 2 RL, a query answering tool based on an OWL 2 RL entailment checker *SHOULD* be sound; a tool based on an OWL 2 RL entailment checker using the Direct Semantics *SHOULD* also be complete; and a tool based on an OWL 2 RL entailment checker using the RDF-Based Semantics and the OWL 2 RL/RDF rules *SHOULD* also be complete if both *O* and *Q* are OWL 2 RL ontology documents, and *Ont(O)* and *Ont(Q)* satisfy the constraints described in [Theorem PR1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Theorem-PR1 "Profiles").

## 3 Test Cases

This section introduces various types of test cases. Each test case describes certain inputs that can be provided to OWL 2 tools and specifies the behavior required to satisfy the conformance conditions described above, given the inputs. Test cases adhere to a common format that simplifies automatic processing, e.g. in a test harness, which is detailed below.

Concrete sets of test cases can be found in various repositories as described below. They are divided into a fixed set of test cases that have been approved based on a process defined later in this section, and an open set of user-contributed test cases that can be collected via a dedicated web site.

### 3.1 Test Types

There are several distinguished types of test cases detailed in the following sub-sections. The type of a test determines the task and expected outcome of the test. The type thus also affects the data associated to a test case, e.g., since only certain kinds tests require the specification of an entailed ontology.

While all test cases have some primary purpose specified by their type, it is often possible to use the provided data for other tests as well. For example, the inputs of any negative entailment test can also be used in a consistency test. Such re-interpretations of test cases can generally be useful, depending on the tool being validated and the goal of validation. For this reason, a concrete test case may have more than one type and thus allow multiple uses.

#### 3.1.1 Syntactic Tests

Syntactic tests can be applied to tools that process OWL 2 ontology documents, or that transform between various syntactic forms of OWL 2. These modes of operation are not covered by any conformance requirement, but syntactic tests may still be useful in tool development.

##### 3.1.1.1 Profile and Species Identification Tests

Profile and species identification tests validate a tool's recognition of Syntactic Conformance. These tests require at least one input ontology document. Each test describes the conformance of *all* provided input ontology documents relative to structural and syntactic restrictions that are specified by the test case.

Since all test cases usually specify the profiles and species of the input ontology documents, essentially all test cases can be used as profile identification tests.

##### 3.1.1.2 Syntax Translation Tests

Syntax translation tests validate the translation of OWL 2 ontology documents from one syntax to another, using the definition of structural equivalence defined in the OWL 2 Syntax specification [OWL 2 Specification]. Each test case of this type specifies input ontology documents in multiple syntactic forms which describe structurally equivalent ontologies. Tools that parse and serialize ontology documents may use this data to verify their correct operation. Note that tests of this kind do not prescribe a particular syntactic form to be the outcome of a syntactic translation: Different serializations are correct as long as they describe the same ontological structure.

Tests of this type specify multiple input ontology documents, and indicate which of the provided syntactic forms are normative for the translation test.

#### 3.1.2 Semantic Tests

Semantic tests specifically address the functionality of OWL 2 entailment checkers. Each test case of this type specifies necessary requirements that *MUST* be satisfied by any entailment checker that meets the according conformance conditions.

Each semantic test case also specifies whether it is applicable to the Direct Semantics [OWL 2 Direct Semantics], to the RDF-Based Semantics [OWL 2 RDF-Based Semantics], or to both. A test is only relevant for testing conformance of tools that use a semantics to which the test applies.

Semantic tests specify one or more OWL 2 ontology documents and check semantic conditions defined with respect to abstract structures obtained from the ontology documents, typically via a parsing process. When using the Direct Semantics [OWL 2 Direct Semantics] the abstract structure is an OWL 2 ontology as defined in the OWL 2 Syntax specification [OWL 2 Specification]; when using the RDF-Based semantics [OWL 2 RDF-Based Semantics] the abstract structure is an RDF graph. We will denote with *Ont(d)* the abstract structure obtained from the ontology document *d*.

##### 3.1.2.1 Entailment Tests

Entailment tests (or positive entailment tests) specify two ontology documents: a premise ontology document *d1* and a conclusion ontology document *d2* where *Ont(d1)* entails *Ont(d2)* with respect to the specified semantics. If provided with inputs *d1* and *d2* (and, if applicable, with access to any imported ontologies), a conforming entailment checker *SHOULD* return True, it *SHOULD NOT* return Unknown, and it *MUST NOT* return False.

In all entailment tests, the ontologies *Ont(d1)* and *Ont(d2)* are consistent. Therefore, all entailment tests are also consistency tests.

##### 3.1.2.2 Non-Entailment Tests

Non-Entailment tests (or negative entailment tests) specify two ontology documents: a premise ontology document *Ont(d1)* and a non-conclusion ontology *Ont(d2)* where *Ont(d1)* does not entail *Ont(d2)* with respect to the specified semantics. If provided with inputs *d1* and *d2* (and, if applicable, with access to any imported ontologies), a conforming entailment checker *SHOULD* return False, it *SHOULD NOT* return Unknown, and it *MUST NOT* return True.

In all non-entailment tests, the ontologies *Ont(d1)* and *Ont(d2)* are consistent. Therefore, all non-entailment tests are also consistency tests.

##### 3.1.2.3 Consistency Tests

Consistency tests validate a tool's recognition of consistency, as defined in the Direct Semantics [OWL 2 Direct Semantics] and the RDF-Based Semantics [OWL 2 RDF-Based Semantics]. These tests specify an input ontology document, the premise ontology document *d*, where *Ont(d)* is consistent with respect to the specified semantics.

Entailment checkers that directly support consistency checking *SHOULD* determine *Ont(d)* to be consistent, and *MUST NOT* determine *Ont(d)* to be inconsistent. Entailment checkers that do not support this operation may execute consistency tests as if they were non-entailment tests: if the ontology *Ont(d)* is consistent, then *Ont(d)* does not entail the inconsistent ontology *Oin* (see Appendix). Given inputs *d* and *din*, a conforming entailment checker *SHOULD* thus return False, it *SHOULD NOT* return Unknown, and it *MUST NOT* return True.

##### 3.1.2.4 Inconsistency Tests

Inconsistency tests validate a tool's recognition of consistency, as defined in the Direct Semantics [OWL 2 Direct Semantics] and the RDF-Based Semantics [OWL 2 RDF-Based Semantics]. These tests specify an input ontology document, the premise ontology document *d*, where *Ont(d)* is inconsistent with respect to the specified semantics.

Entailment checkers that directly support inconsistency checking *SHOULD* determine *Ont(d)* to be inconsistent, and *MUST NOT* determine *Ont(d)* to be consistent. Entailment checkers that do not support this operation may transform inconsistency tests into entailment tests: if the ontology *Ont(d)* is inconsistent, then *Ont(d)* entails any inconsistent ontology – e.g., the inconsistent ontology *Oin* given in the Appendix. Given inputs *d* and *din*, a conforming entailment checker *SHOULD* thus return True, it *SHOULD NOT* return Unknown, and it *MUST NOT* return False.

### 3.2 Test Case Format

Test cases are described using OWL 2, based on a test case ontology documented in this section. The given test case format is mainly based upon two design choices. Firstly, each test case in OWL 2 can be completely represented within a single file, and the location of this file is not relevant. In this way, all test cases adhering to this format are completely portable, and can be published and distributed freely.

A second design choice was to allow individual test case documents to be processed with any OWL tool that can handle at least OWL 2 DL ontology documents. Thus the presented test case ontology and all test case documents using it conform to the definition of OWL 2 DL ontology documents. This design choice also motivates the use of dedicated IRIs (based on the namespace prefix http://www.w3.org/2007/OWL/testOntology#) for all elements of the test case ontology: Existing test ontologies, such as the ones used by the WebOnt working group [OWL 1 Test Cases], have not been crafted this way and do not meet the above requirements. Details of the changes in the test case format as compared to WebOnt are found in Section 3.5.

Overall, the given design is intended to ensure maximal compatibility and ease of use in a variety of different tools. This section describes various elements of the test ontology grouped according to their purpose, and it includes axioms using the functional-style syntax [OWL 2 Specification]. The complete test ontology is summarized in the last section. This ontology uses OWL as a tool for conceptual modeling, describing the intended structure of test case documents – it is, however, not necessary to compute entailments of this ontology in order to use the provided test case documents.

#### 3.2.1 Input Ontologies

The *:inputOntology* data property associates a test with one or more input ontologies. Values of this property (and thus of all of its subproperties) are of type *xsd:string*. Subproperties are used to differentiate among multiple input ontologies that are provided for different purposes depending on the type of test:

```
   Declaration( DataProperty( :inputOntology ) )
   DataPropertyRange( :inputOntology xsd:string )

   Declaration( DataProperty( :premiseOntology ) )
   Declaration( DataProperty( :conclusionOntology ) )
   Declaration( DataProperty( :nonConclusionOntology ) )

   SubDataPropertyOf( :premiseOntology :inputOntology )
   SubDataPropertyOf( :conclusionOntology :inputOntology )
   SubDataPropertyOf( :nonConclusionOntology :inputOntology )
```

Similarly, further subproperties of *:inputOntology* are used to indicate the syntax of the input ontology:

```
   Declaration( DataProperty( :fsInputOntology ) )
   Declaration( DataProperty( :owlXmlInputOntology ) )
   Declaration( DataProperty( :rdfXmlInputOntology ) )

   SubDataPropertyOf( :fsInputOntology :inputOntology )
   SubDataPropertyOf( :owlXmlInputOntology :inputOntology )
   SubDataPropertyOf( :rdfXmlInputOntology :inputOntology )

   DisjointDataProperties( :fsInputOntology :owlXmlInputOntology :rdfXmlInputOntology )
```

To fully specify the purpose *and* syntax of a given input ontology, the test case ontology specifies "intersection properties" that combine (i.e. are subproperties of) two of the above properties. An example is the property *:rdfXmlPremiseOntology*, used to denote a premise ontology in RDF/XML syntax. These more specific properties are used in many test cases, the only exception being pure syntactic tests where the purpose of the given input ontologies does not need to be specified.

#### 3.2.2 Type

All test cases are individuals in the *:TestCase* class. Subclasses of this class are used to map tests to the test types described above. The axioms below describe the relationships between the test types and the input ontology requirements of each test type.

```
   Declaration( Class( :TestCase ) )
   Declaration( Class( :ProfileIdentificationTest ) )
   Declaration( Class( :SyntaxTranslationTest ) )
   Declaration( Class( :ConsistencyTest ) )
   Declaration( Class( :InconsistencyTest ) )
   Declaration( Class( :PositiveEntailmentTest ) )
   Declaration( Class( :NegativeEntailmentTest ) )

   SubClassOf( :ProfileIdentificationTest :TestCase )
   SubClassOf( :SyntaxTranslationTest :TestCase )
   SubClassOf( :ConsistencyTest :ProfileIdentificationTest )
   SubClassOf( :InconsistencyTest :ProfileIdentificationTest )
   SubClassOf( :PositiveEntailmentTest :ConsistencyTest )
   SubClassOf( :NegativeEntailmentTest :ConsistencyTest )

   SubClassOf( :ConsistencyTest DataMinCardinality( 1 :premiseOntology ) )
   SubClassOf( :InconsistencyTest DataMinCardinality( 1 :premiseOntology ) )
   SubClassOf( :PositiveEntailmentTest DataMinCardinality( 1 :conclusionOntology ) )
   SubClassOf( :NegativeEntailmentTest DataMinCardinality( 1 :nonConclusionOntology ) )

   DisjointClasses( :ConsistencyTest :InconsistencyTest )
```

Note that the cardinality restrictions only specify minimal cardinalities. In practice, semantic tests will indeed have only one premise, conclusion, or non-conclusion, but for convenience each of those may be provided in multiple syntactic forms. This is the reason why the above assertions do not require exact cardinalities.

#### 3.2.3 Normative Syntax

The *:normativeSyntax* object property associates a test case with individuals indicating one or more syntactic forms which are normative for all input ontologies associated with this test case. For convenience, test cases may still provide redundant input ontologies using additional syntactic forms which are not normative. Most types of tests usually provide exactly one normative form. Syntax translation tests may provide multiple normative syntactic forms.

The property *:normativeSyntax* may take an instance of the *:Syntax* class as a value. The following mutually different individuals are members of the *:Syntax* class:

- The individual *:FUNCTIONAL* indicates that all functional-style syntax input ontologies associated with the test case are normative.
- The individual *:OWLXML* indicates that all OWL 2 XML syntax input ontologies associated with the test case are normative.
- The individual *:RDFXML* indicates that all RDF/XML syntax input ontologies associated with the test case are normative.

```
   Declaration( Class( :Syntax ) )
   ClassAssertion( :Syntax :RDFXML )
   ClassAssertion( :Syntax :FUNCTIONAL )
   ClassAssertion( :Syntax :OWLXML )
   DifferentIndividuals( :RDFXML :FUNCTIONAL :OWLXML )

   Declaration( ObjectProperty( :normativeSyntax ) )
   ObjectPropertyRange( :normativeSyntax :Syntax )

   SubClassOf( :TestCase ObjectMinCardinality( 1 :normativeSyntax ) )
```

#### 3.2.4 Applicable Semantics

The *:semantics* object property indicates to which kind of OWL 2 semantics a semantic test case is applicable. The property can take the following mutually distinct individuals as possible values:

- The individual *:RDF-BASED* indicates that the test is applicable if the RDF-Based Semantics are used [OWL 2 RDF-Based Semantics].
- The individual *:DIRECT* indicates that the test is applicable if the Direct Semantics are used [OWL 2 Direct Semantics].

Each test should have one property assertion for each of the possible semantics: either a positive property assertion to confirm that the tests is applicable under this semantics, or a negative property assertion indicating it is not.

```
   Declaration( ObjectProperty( :semantics ) )
   DifferentIndividuals( :DIRECT :RDF-BASED )
   ObjectPropertyRange( :semantics ObjectOneOf( :DIRECT :RDF-BASED ) )
```

If a test case is not applicable under one of the two semantics, then it is required that another test case is provided to highlight and illustrate the semantic difference (e.g. an entailment in the RDF-Based Semantics might be a non-entailment in the Direct Semantics). The symmetric property *:alternativeSemanticsTest* is used to associate two test cases that are complementary in this sense.

```
   Declaration( ObjectProperty( :alternativeSemanticsTest ) )
   FunctionalObjectProperty( :alternativeSemanticsTest )
   SymmetricObjectProperty( :alternativeSemanticsTest )

   SubClassOf(
     ObjectIntersectionOf( :TestCase ObjectComplementOf( ObjectHasValue( :semantics :RDF-BASED ) ) )
     ObjectSomeValuesFrom( :alternativeSemanticsTest ObjectHasValue( :semantics :RDF-BASED ) )
   )

   SubClassOf(
     ObjectIntersectionOf( :TestCase ObjectComplementOf( ObjectHasValue( :semantics :DIRECT ) ) )
     ObjectSomeValuesFrom( :alternativeSemanticsTest ObjectHasValue( :semantics :DIRECT ) )
   )
```

#### 3.2.5 Species

The *:species* property describes the syntactic conformance of the input ontology documents with respect to OWL 2 Full ontology documents and OWL 2 DL ontology documents. The property may take either of the following two mutually distinct individuals as values:

- The individual *:FULL* indicates that all input ontologies are OWL 2 Full ontology documents. This should be the case for all tests.
- The individual *:DL* indicates that all input ontologies are OWL 2 DL ontology documents.

Each test should either have a property assertion indicating the input ontology is an OWL 2 DL ontology, or a negative property assertion indicating that it is not.

```
   Declaration( ObjectProperty( :species ) )
   ObjectPropertyRange( :species ObjectOneOf( :DL :FULL ) )
   DifferentIndividuals( :DL :FULL )
   SubClassOf( :TestCase ObjectHasValue( :species :FULL ) )
```

#### 3.2.6 Profiles

The *:profile* object property describes the syntactic conformance of the input ontology with respect to the profiles of OWL 2. It may take one of the following mutually different individuals as values:

- The individual *:EL* indicates that all input ontologies are OWL 2 EL ontology documents.
- The individual *:QL* indicates that all input ontologies are OWL 2 QL ontology documents.
- The individual *:RL* indicates that all input ontologies are OWL 2 RL ontology documents.

Each test should have one property assertion for each of the profiles: either a positive property assertion to confirm that the test conforms to the restrictions of the profile, or a negative property assertion indicating it does not.

```
   Declaration( ObjectProperty( :profile ) )
   ObjectPropertyRange( :profile ObjectOneOf( :EL :QL :RL ) )
   DifferentIndividuals( :EL :QL :RL )
```

The following axiom reflects the fact that if an ontology conforms to the restrictions of OWL 2 EL, OWL 2 QL, or OWL 2 RL it also conforms to the restrictions of OWL 2 DL.

```
   SubClassOf(
       ObjectSomeValuesFrom( :profile ObjectOneOf( :EL :QL :RL ) )
       ObjectHasValue( :species :DL )
   )
```

#### 3.2.7 Imported Ontologies

The *:importedOntology* property associates a test case with an individual that describes an auxiliary ontology which is required to resolve import directives, as explained in [Section 3.4 of the OWL 2 Syntax specification](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Imports "Syntax") [OWL 2 Specification]. The fact that import directives refer to *ontology locations* conflicts with the goal of maintaining test cases in single, location-independent files. Indeed, all contributed test cases would have to ensure imported ontologies to be available in the specified locations, and web access would be required to execute such tests.

Thus imported ontologies will be made available under the according URLs for all approved test cases (see Test Case Repositories). For contributed test cases, this may not be guaranteed, and it is generally desirable to execute all tests off-line based on a single manifest file. Test cases therefore also provide copies of the contents of all imported ontologies as part of their data, so that tools may use a simple location redirection mechanism as described in [Section 3.2 of the OWL 2 Syntax specification](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Ontology_Documents "Syntax") [OWL 2 Specification] when executing test cases.

Each imported ontology is represented by an auxiliary individual with multiple property values:

- one value for the object property *:importedOntologyIRI*, specifying the location that the ontology should be in,
- one or more values for the properties *:fsInputOntology*, *:owlXMLInputOntology*, or *:rdfXMLInputOntology*, specifying the contents of the ontology, possibly in different syntactic forms, and
- one or more values for the property *:normativeSyntax* to define which of the given syntactic forms is to be considered normative.

Tools that execute tests off-line can simulate imports by assuming that a document containing any of the provided normative-syntax input ontologies is located at the given IRI.

```
   Declaration( ObjectProperty( :importedOntology ) )
   Declaration( ObjectProperty( :importedOntologyIRI ) )

   SubClassOf(
       ObjectSomeValuesFrom( ObjectInverseOf(:importedOntology) :TestCase )
       ObjectIntersectionOf(
           ObjectExactCardinality( 1 :importedOntologyIRI )
           DataMinCardinality( 1 :inputOntology )
           ObjectMinCardinality( 1 :normativeSyntax )
       )
   )
```

#### 3.2.8 Status

The *:status* object property specifies the status of a test case according to the test case approval process. The status might thus be PROPOSED, APPROVED, REJECTED, or EXTRACREDIT.

```
   Declaration( ObjectProperty( :status ) )
   FunctionalObjectProperty( :status )
   ObjectPropertyRange( :status ObjectOneOf( :Proposed :Approved :Rejected :Extracredit ) )
   DifferentIndividuals( :Proposed :Approved :Rejected :Extracredit )
```

#### 3.2.9 Identifier

The *:identifier* data property should be used to associate a unique identifier with a test case.

```
   Declaration( DataProperty( :identifier ) )
```

#### 3.2.10 Creator

A test can be related to a literal description (name) of its author using the *:creator* data property. A test can have multiple creators.

```
   Declaration( DataProperty( :creator ) )
```

#### 3.2.11 Description

A literal containing a human-readable description can associated with a test using *:description* data property.

```
   Declaration( DataProperty( :description ) )
```

#### 3.2.12 Specification Reference

Tests that are specifically related to a particular (part of an) OWL 2 specification document may indicate this using the *:specRef* object property. The value of this property is the URL (possibly with section reference) of the referred specification.

```
   Declaration( ObjectProperty( :specRef ) )
```

Note that this property is only provided to specify concrete URL references. To describe the relationship of some test to the specification more verbosely, the description can be used.

#### 3.2.13 Issue Reference

The *:issue* object property can be used to associate a test with a specific WG issue. The value of this property is the URL of the according page in the Working Group's issue tracker.

```
   Declaration( ObjectProperty( :issue ) )
```

#### 3.2.14 Complete Test Ontology

```
Prefix( : = <http://www.w3.org/2007/OWL/testOntology#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Ontology(<http://www.w3.org/2007/OWL/testOntology>
   Annotation( rdfs:label "The OWL 2 Test Ontology" )
   Annotation( rdfs:isDefinedBy <http://www.w3.org/TR/owl2-test/> )

   Declaration( Class( :TestCase ) )

   Declaration( DataProperty( :identifier ) )
   Declaration( DataProperty( :description ) )
   Declaration( DataProperty( :creator ) )
   Declaration( ObjectProperty( :specRef ) )
   Declaration( ObjectProperty( :issue ) )

   Declaration( DataProperty( :inputOntology ) )
   DataPropertyRange( :inputOntology xsd:string )
   Declaration( DataProperty( :premiseOntology ) )
   Declaration( DataProperty( :conclusionOntology ) )
   Declaration( DataProperty( :nonConclusionOntology ) )

   SubDataPropertyOf( :premiseOntology :inputOntology )
   SubDataPropertyOf( :conclusionOntology :inputOntology )
   SubDataPropertyOf( :nonConclusionOntology :inputOntology )

   Declaration( Class( :ProfileIdentificationTest ) )

   SubClassOf( :ProfileIdentificationTest :TestCase )
   SubClassOf( :ProfileIdentificationTest DataMinCardinality( 1 :inputOntology ) )

   Declaration( Class( :SyntaxTranslationTest ) )

   SubClassOf( :SyntaxTranslationTest :TestCase )

   Declaration( Class( :ConsistencyTest ) )
   Declaration( Class( :InconsistencyTest ) )

   SubClassOf( :ConsistencyTest :ProfileIdentificationTest )
   SubClassOf( :InconsistencyTest :ProfileIdentificationTest )
   SubClassOf( :ConsistencyTest DataMinCardinality( 1 :premiseOntology ) )
   SubClassOf( :InconsistencyTest DataMinCardinality( 1 :premiseOntology ) )
   DisjointClasses( :ConsistencyTest :InconsistencyTest )

   Declaration( Class( :PositiveEntailmentTest ) )

   SubClassOf( :PositiveEntailmentTest :ConsistencyTest )
   SubClassOf( :PositiveEntailmentTest DataMinCardinality( 1 :conclusionOntology ) )

   Declaration( Class( :NegativeEntailmentTest ) )

   SubClassOf( :NegativeEntailmentTest :ConsistencyTest )
   SubClassOf( :NegativeEntailmentTest DataMinCardinality( 1 :nonConclusionOntology ) )

   Declaration( ObjectProperty( :status ) )
   FunctionalObjectProperty( :status )
   ObjectPropertyRange( :status ObjectOneOf( :Proposed :Approved :Rejected :Extracredit ) )
   DifferentIndividuals( :Proposed :Approved :Rejected :Extracredit )

   Declaration( ObjectProperty( :species ) )
   ObjectPropertyRange( :species ObjectOneOf( :DL :FULL ) )
   DifferentIndividuals( :DL :FULL )
   SubClassOf( ObjectHasValue( :species :DL ) ObjectHasValue( :species :FULL ) )

   Declaration( ObjectProperty( :profile ) )
   ObjectPropertyRange( :profile ObjectOneOf( :EL :QL :RL ) )
   DifferentIndividuals( :EL :QL :RL )

   SubClassOf(
       ObjectSomeValuesFrom( :profile ObjectOneOf( :EL :QL :RL ) )
       ObjectHasValue( :species :DL )
   )

   Declaration( Class( :Syntax ) )
   ClassAssertion( :Syntax :RDFXML )
   ClassAssertion( :Syntax :FUNCTIONAL )
   ClassAssertion( :Syntax :OWLXML )
   DifferentIndividuals( :RDFXML :FUNCTIONAL :OWLXML )

   Declaration( ObjectProperty( :normativeSyntax ) )
   ObjectPropertyRange( :normativeSyntax :Syntax )

   SubClassOf( :TestCase ObjectMinCardinality( 1 :normativeSyntax ) )

   Declaration( ObjectProperty( :semantics ) )
   Declaration( ObjectProperty( :alternativeSemanticsTest ) )

   ObjectPropertyRange( :semantics ObjectOneOf( :DIRECT :RDF-BASED ) )
   DifferentIndividuals( :DIRECT :RDF-BASED )
   FunctionalObjectProperty( :alternativeSemanticsTest )
   SymmetricObjectProperty( :alternativeSemanticsTest )

   SubClassOf(
     ObjectIntersectionOf( :TestCase ObjectComplementOf( ObjectHasValue( :semantics :RDF-BASED ) ) )
     ObjectSomeValuesFrom( :alternativeSemanticsTest ObjectHasValue( :semantics :RDF-BASED ) )
   )

   SubClassOf(
     ObjectIntersectionOf( :TestCase ObjectComplementOf( ObjectHasValue( :semantics :DIRECT ) ) )
     ObjectSomeValuesFrom( :alternativeSemanticsTest ObjectHasValue( :semantics :DIRECT ) )
   )

   Declaration( DataProperty( :fsInputOntology ) )
   SubDataPropertyOf( :fsInputOntology :inputOntology )

   Declaration( DataProperty( :owlXmlInputOntology ) )
   SubDataPropertyOf( :owlXmlInputOntology :inputOntology )

   Declaration( DataProperty( :rdfXmlInputOntology ) )
   SubDataPropertyOf( :rdfXmlInputOntology :inputOntology )

   DisjointDataProperties( :fsInputOntology :owlXmlInputOntology :rdfXmlInputOntology )

   Declaration( ObjectProperty( :importedOntology ) )
   Declaration( ObjectProperty( :importedOntologyIRI ) )

   SubClassOf(
       ObjectSomeValuesFrom( ObjectInverseOf(:importedOntology) :TestCase )
       ObjectIntersectionOf(
           ObjectExactCardinality( 1 :importedOntologyIRI )
           DataMinCardinality( 1 :inputOntology )
           ObjectMinCardinality( 1 :normativeSyntax )
       )
   )

   Declaration( DataProperty( :fsPremiseOntology ) )
   Declaration( DataProperty( :fsConclusionOntology ) )
   Declaration( DataProperty( :fsNonConclusionOntology ) )
   SubDataPropertyOf( :fsPremiseOntology :premiseOntology )
   SubDataPropertyOf( :fsPremiseOntology :fsInputOntology )
   SubDataPropertyOf( :fsConclusionOntology :conclusionOntology )
   SubDataPropertyOf( :fsConclusionOntology :fsInputOntology )
   SubDataPropertyOf( :fsNonConclusionOntology :nonConclusionOntology )
   SubDataPropertyOf( :fsNonConclusionOntology :fsInputOntology )

   Declaration( DataProperty( :owlXmlPremiseOntology ) )
   Declaration( DataProperty( :owlXmlConclusionOntology ) )
   Declaration( DataProperty( :owlXmlNonConclusionOntology ) )
   SubDataPropertyOf( :owlXmlPremiseOntology :premiseOntology )
   SubDataPropertyOf( :owlXmlPremiseOntology :owlXmlInputOntology )
   SubDataPropertyOf( :owlXmlConclusionOntology :conclusionOntology )
   SubDataPropertyOf( :owlXmlConclusionOntology :owlXmlInputOntology )
   SubDataPropertyOf( :owlXmlNonConclusionOntology :nonConclusionOntology )
   SubDataPropertyOf( :owlXmlNonConclusionOntology :owlXmlInputOntology )

   Declaration( DataProperty( :rdfXmlPremiseOntology ) )
   Declaration( DataProperty( :rdfXmlConclusionOntology ) )
   Declaration( DataProperty( :rdfXmlNonConclusionOntology ) )
   SubDataPropertyOf( :rdfXmlPremiseOntology :premiseOntology )
   SubDataPropertyOf( :rdfXmlPremiseOntology :rdfXmlInputOntology )
   SubDataPropertyOf( :rdfXmlConclusionOntology :conclusionOntology )
   SubDataPropertyOf( :rdfXmlConclusionOntology :rdfXmlInputOntology )
   SubDataPropertyOf( :rdfXmlNonConclusionOntology :nonConclusionOntology )
   SubDataPropertyOf( :rdfXmlNonConclusionOntology :rdfXmlInputOntology )
)
```

### 3.3 Test Case Repositories

A set of approved test cases is provided in the OWL 2 Test Case Repository [OWL 2 Test Cases]. These test cases have been collected based on the approval process described below, and are expected to remain static after the Working Group has finished.

Like any test set, the approved OWL 2 tests are necessarily incomplete in that they cannot cover all relevant situations or possible implementation challenges. For this reason, an additional public test repository [Contributed Test Cases] is provided as a platform for collecting further test cases even after the termination of the Working Group. Since the Working Group does not control the approval process for those additional test cases, they may not be subjected to extensive review and may result in erroneous or misleading information. It is hoped that the additional repository will provide a valuable tool for the development of OWL after the finalization of the recommendation.

### 3.4 Approval Process Overview

This section outlines the process by means of which test cases have been selected for inclusion into the OWL 2 Test Case Repository [OWL 2 Test Cases].

- At the chairs' discretion, individual tests or groups of tests are put to the Working Group in the weekly telecon or at a face-to-face meeting.

- The Working Group may approve, reject, or defer decision on a test.
  * If the Working Group approves a test, its status is changed to APPROVED. All approved and only approved tests are included in the test case repository [OWL 2 Test Cases]. The working group may decide to approve some tests as EXTRACREDIT, indicating that implementors are not expected to implement the required functionality. Further details are found below.
  * If the Working Group rejects a test, its status is changed to REJECTED.
  * If the Working Group defers decision on a test, its status remains PROPOSED.
- At the chairs' discretion, the Working Group may review any previous decision regarding any test cases.

The Working Group has complete discretion to approve or reject tests independent of their conformance with this process or their conformance with the OWL Working Drafts.

**Extra credit tests** are approved test cases of status EXTRACREDIT. These tests have been found to be particularly hard to implement efficiently. Many extra credit tests are rather testing the performance of an implementation than highlighting a particular semantic interaction of OWL constructs. The name indicates that there is no expectation that any implementation will successfully run such tests and any that do gain extra credit.

### 3.5 Changes From WebOnt Tests

This section provides an overview of the differences of the OWL 2 test cases format and collection as compared to the test cases of the first OWL specification as developed by the WebOnt working group [OWL 1 Test Cases].

#### 3.5.1 Formatting Changes

As explained above, changes of the test case format are motivated by the desire to supply test cases within single stand-alone documents that meet the syntactic conformance criteria of OWL 2 DL. In order to avoid confusion with the earlier test case format, all elements of the ontology use new IRIs based on a dedicated namespace. Many properties still reflect the general structure of test cases, as outlined in [Test Metadata], and are applied in the same sense. In addition, some new ontology elements were introduced to account for aspects that are specific to OWL 2 (e.g. the *:profile* property).

Besides the change in vocabulary, the main structural change compared to WebOnt test cases is the embedding of all relevant data in single files, instead of using separate files for each involved ontology.

#### 3.5.2 Changes to Test Types

"Profile Identification Tests" and "Syntax Translation Tests" did not exist in the WebOnt test suite.

"Tests for Incorrect Use of OWL Namespace" has been removed as a type. These tests were intended to highlight differences between the OWL RDF vocabulary and the DAML+OIL vocabulary. Time has reduced the motivation for such tests.

"True Tests", "OWL for OWL Tests", and "Import Entailment Tests" have been removed as types. These types were each specializations of entailment tests. To the extent that they are present in the current test suite, these tests are marked as positive entailment tests.

"Import Level Tests" has been removed as a type. This type is now included in the "Profile Identification Tests".

#### 3.5.3 Changes to Process

Status of each test no longer includes "OBSOLETED".

## 4 Appendix: An Inconsistent Ontology

Consistency tests and inconsistency tests can be considered as entailment tests and non-entailment tests, respectively, by checking the entailment of an (arbitrary) inconsistent ontology. This appendix provides an ontology document *din* in the functional-style syntax that can be used for this purpose and that is compatible with all profiles. The corresponding ontology *Oin=Ont(din)* (see Section 2.3) is inconsistent with respect to both the Direct Semantics [OWL 2 Direct Semantics] and the RDF-Based Semantics [OWL 2 RDF-Based Semantics]).

```
Namespace( owl =  <http://www.w3.org/2002/07/owl#> )
Ontology(<http://example.com/inconsistentOntology>
   SubClassOf( owl:Thing owl:Nothing )
)
```

## 5 Appendix: Change Log (Informative)

### 5.1 Changes Since Recommendation

This section summarizes the changes to this document since the [Recommendation of 27 October 2009](https://www.w3.org/TR/2009/REC-owl2-conformance-20091027/ "http://www.w3.org/TR/2009/REC-owl2-conformance-20091027/").

- With the publication of the XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes [Recommendation of 5 April 2012](https://www.w3.org/TR/2012/REC-xmlschema11-2-20120405/ "http://www.w3.org/TR/2012/REC-xmlschema11-2-20120405/"), the elements of OWL 2 which are based on XSD 1.1 are now considered required, and the note detailing the optional dependency on the XSD 1.1 [Candidate Recommendation of 30 April, 2009](https://www.w3.org/TR/2009/CR-xmlschema11-2-20090430/ "http://www.w3.org/TR/2009/CR-xmlschema11-2-20090430/") has been removed from the "Status of this Document" section.
- Removal of the section discussing dependencies on the XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes [Candidate Recommendation of 30 April, 2009](https://www.w3.org/TR/2009/CR-xmlschema11-2-20090430/ "http://www.w3.org/TR/2009/CR-xmlschema11-2-20090430/"), which became a [Recommendation on 5 April, 2012](https://www.w3.org/TR/2012/REC-xmlschema11-2-20120405/ "http://www.w3.org/TR/2012/REC-xmlschema11-2-20120405/").

### 5.2 Changes Since Proposed Recommendation

This section summarizes the changes to this document since the [Proposed Recommendation of 22 September, 2009](https://www.w3.org/TR/2009/PR-owl2-conformance-20090922/ "http://www.w3.org/TR/2009/PR-owl2-conformance-20090922/").

- Some minor editorial changes were made.

### 5.3 Changes Since Candidate Recommendation

This section summarizes the changes to this document since the [Candidate Recommendation of 11 June, 2009](https://www.w3.org/TR/2009/CR-owl2-conformance-20090611/ "http://www.w3.org/TR/2009/CR-owl2-conformance-20090611/").

- Some conformance conditions relating to the OWL 2 datatype map were removed from Section 2.1 as the strengthening of the definition in the OWL 2 Syntax specification [OWL 2 Specification] rendered them redundant.
- In Section 2.2 datatype maps are no longer mentioned as the strengthening of the definition of the OWL 2 datatype map (in the OWL 2 Syntax specification [OWL 2 Specification]) renders this redundant.
- The role of "Extra Credit" test cases was clarified.
- Text was added to explain the dependency on XML Schema Datatypes.
- Some minor editorial changes were made.

## 6 Acknowledgments

The starting point for the development of OWL 2 was the [OWL1.1 member submission](https://www.w3.org/Submission/2006/10/ "http://www.w3.org/Submission/2006/10/"), itself a result of user and developer feedback, and in particular of information gathered during the [OWL Experiences and Directions (OWLED) Workshop series](http://www.webont.org/owled/ "http://www.webont.org/owled/"). The working group also considered [postponed issues](https://www.w3.org/2001/sw/WebOnt/webont-issues.html "http://www.w3.org/2001/sw/WebOnt/webont-issues.html") from the [WebOnt Working Group](https://www.w3.org/2004/OWL/ "http://www.w3.org/2004/OWL/").

This document has been produced by the OWL Working Group (see below), and its contents reflect extensive discussions within the Working Group as a whole.
The editors extend special thanks to
Bernardo Cuenca Grau (Oxford University Computing Laboratory),
Peter F. Patel-Schneider (Bell Labs Research, Alcatel-Lucent),
Jonathan Rees (Science Commons),
Alan Ruttenberg (Science Commons) and
Michael Schneider (FZI)
for their thorough reviews.

The regular attendees at meetings of the OWL Working Group at the time of publication of this document were:
Jie Bao (RPI),
Diego Calvanese (Free University of Bozen-Bolzano),
Bernardo Cuenca Grau (Oxford University Computing Laboratory),
Martin Dzbor (Open University),
Achille Fokoue (IBM Corporation),
Christine Golbreich (Université de Versailles St-Quentin and LIRMM),
Sandro Hawke (W3C/MIT),
Ivan Herman (W3C/ERCIM),
Rinke Hoekstra (University of Amsterdam),
Ian Horrocks (Oxford University Computing Laboratory),
Elisa Kendall (Sandpiper Software),
Markus Krötzsch (FZI),
Carsten Lutz (Universität Bremen),
Deborah L. McGuinness (RPI),
Boris Motik (Oxford University Computing Laboratory),
Jeff Pan (University of Aberdeen),
Bijan Parsia (University of Manchester),
Peter F. Patel-Schneider (Bell Labs Research, Alcatel-Lucent),
Sebastian Rudolph (FZI),
Alan Ruttenberg (Science Commons),
Uli Sattler (University of Manchester),
Michael Schneider (FZI),
Mike Smith (Clark & Parsia),
Evan Wallace (NIST),
Zhe Wu (Oracle Corporation), and
Antoine Zimmermann (DERI Galway).
We would also like to thank past members of the working group:
Jeremy Carroll,
Jim Hendler, and
Vipul Kashyap.

## 7 References

[Contributed Test Cases]

[Public Test Case Repository](http://owl.semanticweb.org/page/OWL_2_Test_Cases "http://owl.semanticweb.org/page/OWL_2_Test_Cases").

[OWL 2 Specification]

[OWL 2 Web Ontology Language: Structural Specification and Functional-Style Syntax (Second Edition)](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/) Boris Motik, Peter F. Patel-Schneider, Bijan Parsia, eds. W3C Recommendation, 11 December 2012, [http://www.w3.org/TR/2012/REC-owl2-syntax-20121211/](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/). Latest version available at [http://www.w3.org/TR/owl2-syntax/](https://www.w3.org/TR/owl2-syntax/).

[OWL 2 RDF Mapping]

[OWL 2 Web Ontology Language: Mapping to RDF Graphs (Second Edition)](https://www.w3.org/TR/2012/REC-owl2-mapping-to-rdf-20121211/) Peter F. Patel-Schneider, Boris Motik, eds. W3C Recommendation, 11 December 2012, [http://www.w3.org/TR/2012/REC-owl2-mapping-to-rdf-20121211/](https://www.w3.org/TR/2012/REC-owl2-mapping-to-rdf-20121211/). Latest version available at [http://www.w3.org/TR/owl2-mapping-to-rdf/](https://www.w3.org/TR/owl2-mapping-to-rdf/).

[OWL 2 Direct Semantics]

[OWL 2 Web Ontology Language: Direct Semantics (Second Edition)](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/) Boris Motik, Peter F. Patel-Schneider, Bernardo Cuenca Grau, eds. W3C Recommendation, 11 December 2012, [http://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/). Latest version available at [http://www.w3.org/TR/owl2-direct-semantics/](https://www.w3.org/TR/owl2-direct-semantics/).

[OWL 2 RDF-Based Semantics]

[OWL 2 Web Ontology Language: RDF-Based Semantics (Second Edition)](https://www.w3.org/TR/2012/REC-owl2-rdf-based-semantics-20121211/) Michael Schneider, editor. W3C Recommendation, 11 December 2012, [http://www.w3.org/TR/2012/REC-owl2-rdf-based-semantics-20121211/](https://www.w3.org/TR/2012/REC-owl2-rdf-based-semantics-20121211/). Latest version available at [http://www.w3.org/TR/owl2-rdf-based-semantics/](https://www.w3.org/TR/owl2-rdf-based-semantics/).

[OWL 2 XML Serialization]

[OWL 2 Web Ontology Language: XML Serialization (Second Edition)](https://www.w3.org/TR/2012/REC-owl2-xml-serialization-20121211/) Boris Motik, Bijan Parsia, Peter F. Patel-Schneider, eds. W3C Recommendation, 11 December 2012, [http://www.w3.org/TR/2012/REC-owl2-xml-serialization-20121211/](https://www.w3.org/TR/2012/REC-owl2-xml-serialization-20121211/). Latest version available at [http://www.w3.org/TR/owl2-xml-serialization/](https://www.w3.org/TR/owl2-xml-serialization/).

[OWL 2 Profiles]

[OWL 2 Web Ontology Language: Profiles (Second Edition)](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/) Boris Motik, Bernardo Cuenca Grau, Ian Horrocks, Zhe Wu, Achille Fokoue, Carsten Lutz, eds. W3C Recommendation, 11 December 2012, [http://www.w3.org/TR/2012/REC-owl2-profiles-20121211/](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/). Latest version available at [http://www.w3.org/TR/owl2-profiles/](https://www.w3.org/TR/owl2-profiles/).

[OWL 2 Test Cases]

[OWL 2 Test Case Repository](https://www.w3.org/2009/owl-test-cases "http://www.w3.org/2009/owl-test-cases").

[OWL 1 Test Cases]

[OWL Web Ontology Language: Test Cases](https://www.w3.org/TR/2004/REC-owl-test-20040210/ "http://www.w3.org/TR/2004/REC-owl-test-20040210/"). Jeremy J. Carroll, and Jos De Roo, eds. W3C Recommendation, 10 February 2004, http://www.w3.org/TR/2004/REC-owl-test-20040210/. Latest version available at http://www.w3.org/TR/owl-test/.

[RDF Syntax]

[RDF/XML Syntax Specification (Revised)](https://www.w3.org/TR/2004/REC-rdf-syntax-grammar-20040210/ "http://www.w3.org/TR/2004/REC-rdf-syntax-grammar-20040210/"). Dave Beckett, ed. W3C Recommendation, 10 February 2004, http://www.w3.org/TR/2004/REC-rdf-syntax-grammar-20040210/. Latest version available as http://www.w3.org/TR/rdf-syntax-grammar/.

[RFC 2119]

[RFC 2119: Key words for use in RFCs to Indicate Requirement Levels](http://www.ietf.org/rfc/rfc2119.txt "http://www.ietf.org/rfc/rfc2119.txt"). Network Working Group, S. Bradner. IETF, March 1997, http://www.ietf.org/rfc/rfc2119.txt

[Test Metadata]

[Test Metadata](https://www.w3.org/TR/2005/NOTE-test-metadata-20050914/ "http://www.w3.org/TR/2005/NOTE-test-metadata-20050914/"). Patrick Curran and Karl Dubost, eds., W3C Working Group Note 14 September 2005, [http://www.w3.org/TR/2005/NOTE-test-metadata-20050914/](https://www.w3.org/TR/2005/NOTE-test-metadata-20050914/ "http://www.w3.org/TR/2005/NOTE-test-metadata-20050914/"). Latest version available at [http://www.w3.org/TR/test-metadata/](https://www.w3.org/TR/test-metadata/ "http://www.w3.org/TR/test-metadata/").

[Turtle]

[Turtle: Terse RDF Triple Language](https://www.w3.org/TR/turtle/ "http://www.w3.org/TR/turtle/"). Eric Prud'hommeaux and Gavin Carothers. W3C Last Call Working Draft, 10 July 2012, http://www.w3.org/TR/2012/WD-turtle-20120710/. Latest version available at http://www.w3.org/TR/turtle/.
