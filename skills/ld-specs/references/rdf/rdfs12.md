---
title: "RDF 1.2 Schema"
source: https://www.w3.org/TR/rdf12-schema/
family: rdf
version: "1.2"
status: W3C Working Draft
spec_date: 2026-10-10
fetched: 2026-10-21
---

# RDF 1.2 Schema

> Data-modelling vocabulary (class/property hierarchy) for RDF.

## Contents

- Abstract
- 1 Introduction
- 2 Data-modelling vocabulary
  - 2.1 Classes
    - 2.1.1 rdfs:Resource
    - 2.1.2 rdfs:Class
    - 2.1.3 rdfs:Literal
    - 2.1.4 rdfs:Datatype
    - 2.1.5 rdf:Property
  - 2.2 Semantic Properties
    - 2.2.1 rdfs:range
    - 2.2.2 rdfs:domain
    - 2.2.3 rdf:type
    - 2.2.4 rdfs:subClassOf
    - 2.2.5 rdfs:subPropertyOf
  - 2.3 Documentation Properties
    - 2.3.1 rdfs:label
    - 2.3.2 rdfs:comment
    - 2.3.3 rdfs:seeAlso
    - 2.3.4 rdfs:isDefinedBy
  - 2.4 Using the Domain and Range vocabulary
- 3 Datatypes
  - 3.1 rdf:langString
  - 3.2 rdf:dirLangString
  - 3.3 rdf:HTML
  - 3.4 rdf:XMLLiteral
  - 3.5 rdf:JSON
  - 3.6 XML Schema datatypes
- 4 RDF Collections
  - 4.1 rdf:List
  - 4.2 rdf:first
  - 4.3 rdf:rest
  - 4.4 rdf:nil
- 5 Triple-term based reification
  - 5.1 rdfs:Proposition
  - 5.2 rdf:reifies
- 6 Utility Properties
  - 6.1 rdf:value
- 7 Legacy vocabularies
  - 7.1 Containers
    - 7.1.1 rdfs:Container
    - 7.1.2 rdf:Bag
    - 7.1.3 rdf:Seq
    - 7.1.4 rdf:Alt
    - 7.1.5 rdfs:ContainerMembershipProperty
    - 7.1.6 rdfs:member
  - 7.2 "Old-style" Reification
    - 7.2.1 rdf:Statement
    - 7.2.2 rdf:subject
    - 7.2.3 rdf:predicate
    - 7.2.4 rdf:object
- 8 RDF Schema summary
  - 8.1 RDF classes
  - 8.2 RDF properties
- A Vocabulary Registry
  - A.1 rdf: Namespace
  - A.2 rdfs: Namespace
- B Privacy Considerations
- C Security Considerations
- E Change since 2004 Recommendation
- F Changes between RDF 1.1 and RDF 1.2
- G Index
  - G.1 Terms defined by this specification
  - G.2 Terms defined by reference
- H References
  - H.1 Informative references

---

## Abstract

RDF
Schema provides a data-modelling vocabulary for RDF data. RDF Schema
is an extension of the basic RDF vocabulary.

## 1. Introduction

RDF Schema provides a data-modelling vocabulary for RDF data.
It is complemented by several companion documents which
describe the basic concepts and abstract syntax of RDF
[RDF12-CONCEPTS], the formal semantics of RDF [RDF12-SEMANTICS], and
various concrete syntaxes for RDF, such as Turtle [RDF12-TURTLE],
TriG, [RDF12-TRIG], and JSON-LD [JSON-LD11]. The RDF Primer
[RDF12-PRIMER] provides an informal introduction and
examples of the use of the concepts specified in this document.

This document serves two complementary purposes:

- It defines RDF Schema as a vocabulary for specifying lightweight
  ontologies, underlying the semantic extension described in
  RDF Semantics (§9 of [RDF12-SEMANTICS]).
- It enumerates all terms defined within the `rdf:` and `rdfs:` namespaces, including both terms relevant to
  ontology construction and general-purpose terms used broadly within
  RDF applications.

This document is intended to provide a clear specification of RDF
Schema to those who find the formal semantics
specification [RDF12-SEMANTICS]
daunting. Thus, this document duplicates material also specified in the
RDF
Semantics specification. Where there is disagreement between this
document
and the RDF Semantics specification, the RDF Semantics specification
should
be taken to be correct.

RDF Schema is a [semantic extension](https://www.w3.org/TR/rdf12-semantics/#semantic-extensions-and-entailment-regimes) of RDF. It provides mechanisms for describing groups of
related resources and the relationships between these resources. RDF
Schema is written in RDF
using the terms described in this document. These resources are used to
determine characteristics of other resources, such as the domains (§2.2.2) and ranges (§2.2.1) of properties.

The RDF Schema class and property system is similar to the type
systems of object-oriented programming languages such as Java. RDF
Schema differs from many such systems in that instead of defining a
class in
terms of the properties its instances may have, RDF Schema
describes properties in terms of the classes of
resource to which they apply. This is the role of the domain (§2.2.2) and range (§2.2.1) mechanisms described in this specification. For example, we could
define the `eg:author` property to have a domain of `eg:Document` and a range of `eg:Person`, whereas a classical object oriented system might
typically define a class `eg:Book` with an attribute called `eg:author` of type `eg:Person`. Using the RDF
approach, it is easy for others to subsequently define additional
properties with a domain of `eg:Document` or a range of `eg:Person`. This can be done without the need to re-define
the original description of
these classes. One benefit of the RDF property-centric approach is that
it
allows anyone to extend the description of existing resources, one of
the
architectural principles of the Web [RDF-NOT].

However, RDF Schema also includes numerous terms in the rdf: and rdfs: namespaces that support broader RDF functionality
and general data representation needs. These terms are not exclusively
tied to ontology specification but serve essential roles in RDF’s
broader architecture.

This specification does not attempt to enumerate all the possible forms
of
representing the meaning of RDF
classes and properties. Instead, the RDF Schema strategy is
to acknowledge that there are many techniques through which the meaning
of
classes and properties can be described. Richer vocabulary or 'ontology'
languages such as OWL [OWL2-OVERVIEW], inference rule
languages and other formalisms (for example temporal logics) will each
contribute to our ability to capture meaningful generalizations about
data in
the Web.

The language defined in this specification consists of a collection of
RDF resources that can be used to describe other RDF resources in
application-specific RDF vocabularies. The core vocabulary is defined in
a namespace informally called `rdfs` here.

The IRIs in an RDF vocabulary often begin with
a common substring known as a namespace IRI.
Some namespace IRIs are associated by convention with a short name
known as a namespace prefix.

*Some namespace prefixes and IRIs used in this specification*

| Namespace prefix | Namespace IRI                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------- |
| rdf              | [`http://www.w3.org/1999/02/22-rdf-syntax-ns#`](https://www.w3.org/1999/02/22-rdf-syntax-ns#) |
| rdfs             | [`http://www.w3.org/2000/01/rdf-schema#`](https://www.w3.org/2000/01/rdf-schema#)             |
| xsd              | [`http://www.w3.org/2001/XMLSchema#`](https://www.w3.org/2001/XMLSchema#)                     |

For convenience and readability, this specification uses an abbreviated
form to represent IRIs. A name of the form `prefix:suffix` should be
interpreted as a IRI consisting of the IRI associated
with the `prefix` concatenated with the `suffix`.

## 2. Data-modelling vocabulary

### 2.1 Classes

Resources may be divided into groups called classes. The members of a
class are known as *instances* of the class. Classes are
themselves
resources. They are often identified by [IRIs](https://www.w3.org/TR/rdf12-concepts/#section-IRIs) and
may be described using RDF properties. The `rdf:type` (§2.2.3) property may be used to state that a
resource is an instance of a class.

RDF distinguishes between a class and the set of its instances.
Associated
with each class is a set, called the class extension of the class, which
is
the set of the instances of the class. Two classes may have the same set
of
instances but be different classes. For example, the tax office may
define
the class of people living at the same address as the editor of this
document. The Post Office may define the class of people whose address
has
the same zip code as the address of the author. It is possible for these
classes to have exactly the same instances, yet to have different
properties.
Only one of the classes has the property that it was defined by the tax
office, and only the other has the property that it was defined by the
Post
Office.

A class may be a member of its own class extension and may be an
instance of itself.

The group of resources that are RDF Schema classes is itself a class
called `rdfs:Class` (§2.1.2).

If a class *C* is a *subclass* of a class *C'*, then all instances
of *C* will
also be instances of *C'*. The `rdfs:subClassOf` (§2.2.4) property may be used to state that one class is a subclass of another.
The term super-class is used as the inverse of subclass. If a class *C'* is a super-class of a class *C*, then all instances of *C* are also
instances of *C'*.

The RDF Concepts and Abstract Syntax [RDF12-CONCEPTS] specification
defines the RDF concept of an [RDF datatype](https://www.w3.org/TR/rdf12-concepts/#section-Datatypes). All datatypes are classes. The instances of a class that
is a
datatype are the members of the value space of the datatype.

#### 2.1.1 `rdfs:Resource`

All things described by RDF are called *resources*, and are
instances of the class `rdfs:Resource`. This is the class
of
everything. All other classes are subclasses of
this class. `rdfs:Resource` is an instance of `rdfs:Class` (§2.1.2).

#### 2.1.2 `rdfs:Class`

This is the class of resources that are RDF classes. `rdfs:Class` is an instance of `rdfs:Class.`

#### 2.1.3 `rdfs:Literal`

The class `rdfs:Literal` is the class of [literal](https://www.w3.org/TR/rdf12-concepts/#section-Graph-Literal) values such as strings and integers. Property values such as textual
strings are examples of RDF literals.

`rdfs:Literal` is an instance of `rdfs:Class` (§2.1.2). `rdfs:Literal` is a subclass of `rdfs:Resource` (§2.1.1).

#### 2.1.4 `rdfs:Datatype`

`rdfs:Datatype` is the class of datatypes. All instances
of `rdfs:Datatype` correspond to the [RDF model of a datatype](https://www.w3.org/TR/rdf12-concepts/#section-Datatypes) described in the RDF Concepts specification
[RDF12-CONCEPTS]. `rdfs:Datatype` is
both an instance of and a subclass of `rdfs:Class` (§2.1.2). Each instance of `rdfs:Datatype` is a subclass of `rdfs:Literal` (§2.1.3).

#### 2.1.5 `rdf:Property`

`rdf:Property` is the class of RDF properties. `rdf:Property` is an instance of `rdfs:Class` (§2.1.2).

### 2.2 Semantic Properties

The RDF Concepts and Abstract Syntax specification [RDF12-CONCEPTS]
describes the concept of an RDF property as a relation between subject
resources and object resources.

This specification defines the concept of subproperty. The `rdfs:subPropertyOf` (§2.2.4) property may be used to state that one property is a subproperty of
another.
If a property *P* is a subproperty of property *P'*, then all pairs of
resources which are related by *P* are also related by *P'*. The term
super-property is often
used as the inverse of subproperty. If a property *P'* is a super-property
of a property *P*, then all pairs of resources which are related by *P* are
also related by *P'*. This specification does not define a top
property that is the super-property of all properties.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The basic facilities provided by `rdfs:domain` (§2.2.2) and `rdfs:range` (§2.2.1) do not provide any
> direct way to indicate property restrictions that are local to a class.
> Although it is possible to combine use `rdfs:domain` (§2.2.2) and `rdfs:range` (§2.2.1) with sub-property
> hierarchies, direct support for such declarations are provided by richer
> Web Ontology languages such as OWL [OWL2-OVERVIEW].

#### 2.2.1 `rdfs:range`

`rdfs:range` is an instance of `rdf:Property` (§2.1.5) that is used to state that
the values of a property are instances of one or more classes.

The triple
> `P rdfs:range C`

states that *P* is an instance of the class `rdf:Property` (§2.1.5),
that *C* is an instance of the class `rdfs:Class` (§2.1.2) and that the resources denoted by the objects of triples whose
predicate is *P* are instances of the class *C*.

Where *P* has more than one `rdfs:range` property, then the resources
denoted by the objects of triples with predicate *P* are instances of
all the classes stated by the `rdfs:range` properties.

The `rdfs:range` property can be applied to itself. The `rdfs:range` of `rdfs:range` is the class `rdfs:Class` (§2.1.2).
This states that any resource
that is the value of an `rdfs:range` property is an
instance of `rdfs:Class` (§2.1.2).

The `rdfs:range` property is applied to properties. This
can be represented in RDF using the `rdfs:domain` (§2.2.2) property. The `rdfs:domain` (§2.2.2) of `rdfs:range` is
the class `rdf:Property` (§2.1.5). This
states
that any resource with an `rdfs:range` property is an
instance of `rdf:Property` (§2.1.5).

#### 2.2.2 `rdfs:domain`

`rdfs:domain` is an instance of `rdf:Property` (§2.1.5) that is used to state that
any resource that has a given property is an instance of one or more
classes.

A triple of the form:
> `P rdfs:domain C`

states that *P* is an instance of the class `rdf:Property` (§2.1.5),
that *C* is a instance of the class `rdfs:Class` (§2.1.2) and that the resources denoted by the subjects of triples whose
predicate is *P* are instances of the class C.

Where a property *P* has more than one `rdfs:domain` property, then the
resources denoted by subjects of triples with predicate *P* are
instances of all the classes stated by the `rdfs:domain` properties.

The `rdfs:domain` property may be applied to itself. The `rdfs:domain` of `rdfs:domain` is the class `rdf:Property` (§2.1.5).
This states that any
resource with an `rdfs:domain` property is an instance of `rdf:Property` (§2.1.5).

The `rdfs:range` (§2.2.1) of `rdfs:domain` is the class `rdfs:Class` (§2.1.2).
This states that any resource that is the value of an `rdfs:domain` property is an
instance of `rdfs:Class` (§2.1.2).

#### 2.2.3 `rdf:type`

`rdf:type` is an instance of `rdf:Property` (§2.1.5) that is used to
state that a resource is an instance of a class.

A triple of the form:
> `R rdf:type C`

states that *C* is an instance of `rdfs:Class` (§2.1.2) and *R* is an instance of *C*.

The `rdfs:domain` (§2.2.2) of `rdf:type` is §2.1.1 rdfs:Resource.
The `rdfs:range` (§2.2.1) of `rdf:type` is `rdfs:Class` (§2.1.2).

#### 2.2.4 `rdfs:subClassOf`

The property `rdfs:subClassOf` is an instance of `rdf:Property` (§2.1.5) that is used to state
that all the instances of one class are instances of another.

A triple of the form:
> `C1 rdfs:subClassOf C2`

states that *C1* is an instance of `rdfs:Class` (§2.1.2), *C2* is an instance of `rdfs:Class` (§2.1.2) and *C1* is a subclass of *C2*. The `rdfs:subClassOf` property is transitive.

The `rdfs:domain` (§2.2.2) of `rdfs:subClassOf` is `rdfs:Class` (§2.1.2).
The `rdfs:range` (§2.2.1) of `rdfs:subClassOf` is `rdfs:Class` (§2.1.2).

#### 2.2.5 `rdfs:subPropertyOf`

The property `rdfs:subPropertyOf` is an instance of `rdf:Property` (§2.1.5) that is used to state
that all resources related by one property are also related by
another.

A triple of the form:
> `P1 rdfs:subPropertyOf P2`

states that *P1* is an instance of `rdf:Property` (§2.1.5), *P2* is an instance of `rdf:Property` (§2.1.5) and *P1* is a subproperty of *P2*. The `rdfs:subPropertyOf` property is transitive.

The `rdfs:domain` (§2.2.2) of `rdfs:subPropertyOf` is `rdf:Property` (§2.1.5).
The `rdfs:range` (§2.2.1) of `rdfs:subPropertyOf` is `rdf:Property` (§2.1.5).

### 2.3 Documentation Properties

#### 2.3.1 `rdfs:label`

`rdfs:label` is an instance of `rdf:Property` (§2.1.5) that may be used to provide a human-readable version of a resource's
name.

A triple of the form:
> `R rdfs:label L`

states that *L* is a human readable label for *R*.

The `rdfs:domain` (§2.2.2) of `rdfs:label` is `rdfs:Resource` (§2.1.1).
The `rdfs:range` (§2.2.1) of `rdfs:label` is `rdfs:Literal` (§2.1.3).

Multilingual labels are supported using the [language tagging](https://www.w3.org/TR/rdf12-concepts/#section-Graph-Literal) facility of RDF literals.

#### 2.3.2 `rdfs:comment`

`rdfs:comment` is an instance of `rdf:Property` (§2.1.5) that may be used to provide a human-readable description of a
resource.

A triple of the form:
> `R rdfs:comment L`

states that *L* is a human readable description of *R*.

The `rdfs:domain` (§2.2.2) of `rdfs:comment` is `rdfs:Resource` (§2.1.1).
The `rdfs:range` (§2.2.1) of `rdfs:comment` is `rdfs:Literal` (§2.1.3).

A textual comment helps clarify the meaning of RDF classes and
properties.
Such in-line documentation complements the use of both formal
techniques
(Ontology and rule languages) and informal (prose documentation,
examples,
test cases). A variety of documentation forms can be combined to
indicate the
intended meaning of the classes and properties described in an RDF
vocabulary. Since RDF vocabularies are expressed as RDF graphs,
vocabularies
defined in other namespaces may be used to provide richer
documentation.

Multilingual documentation is supported through use of the [language tagging](https://www.w3.org/TR/rdf12-concepts/#section-Graph-Literal) facility of RDF literals.

#### 2.3.3 `rdfs:seeAlso`

`rdfs:seeAlso` is an instance of `rdf:Property` (§2.1.5) that is used to indicate a
resource that might provide additional information about the subject
resource.

A triple of the form:
> `S rdfs:seeAlso O`

states that the resource *O* may provide additional information about *S*. It
may be possible to retrieve representations of *O* from the Web, but
this is
not required. When such representations may be retrieved, no
constraints are
placed on the format of those representations.

The `rdfs:domain` (§2.2.2) of `rdfs:seeAlso` is `rdfs:Resource` (§2.1.1).
The `rdfs:range` (§2.2.1) of `rdfs:seeAlso` is `rdfs:Resource` (§2.1.1).

#### 2.3.4 `rdfs:isDefinedBy`

`rdfs:isDefinedBy` is an instance of `rdf:Property` (§2.1.5) that is used to indicate a
resource defining the subject resource. This property may be used to
indicate
an RDF vocabulary in which a resource is described.

A triple of the form:
> `S rdfs:isDefinedBy O`

states that the resource *O* defines *S*. It may be possible to
retrieve
representations of *O* from the Web, but this is not required. When
such
representations may be retrieved, no constraints are placed on the
format of
those representations. `rdfs:isDefinedBy` is a subproperty of `rdfs:seeAlso` (§2.3.3).

The `rdfs:domain` (§2.2.2) of `rdfs:isDefinedBy` is `rdfs:Resource` (§2.1.1).
The `rdfs:range` (§2.2.1) of `rdfs:isDefinedBy` is `rdfs:Resource` (§2.1.1).

### 2.4 Using the Domain and Range vocabulary

*This section is non-normative.*

This specification introduces an RDF vocabulary for describing the
meaningful use of properties and classes in RDF data. For example, an
RDF
vocabulary might describe limitations on the types of values that are
appropriate for some property, or on the classes to which it makes sense
to
ascribe such properties.

RDF Schema provides a mechanism for describing this information, but
does not say whether or how an application should use it. For example,
while an RDF vocabulary can assert that an `author` property
is used to
indicate resources that are instances of the class `Person`,
it
does not say whether or how an application should act in processing that
range information. Different applications will use this information in
different ways. For example, data checking tools might use this to help
discover errors in some data set, an interactive editor might suggest
appropriate values, and a reasoning application might use it to infer
additional information from instance data.

RDF vocabularies can describe relationships between vocabulary items
from
multiple independently developed vocabularies. Since IRIs are used
to identify classes and properties on the Web, it is possible to create
new
properties that have a `domain` or `range` whose
value
is a class defined in another namespace.

## 3. Datatypes

An RDF datatype is a class of literal values with an associated value space, lexical space, and lexical-to-value mapping,
identified by a datatype IRI [RDF12-CONCEPTS].

RDF 1.2 recognizes both RDF‑native datatypes (e.g., `rdf:langString`, `rdf:dirLangString`, `rdf:HTML`, `rdf:XMLLiteral`, `rdf:JSON`) and the RDF‑compatible subset of XML Schema 1.1
datatypes, which are enumerated below.

[https://www.w3.org/TR/rdf12-schema/datatypes.svg](https://www.w3.org/TR/rdf12-schema/datatypes.svg)

*Figure 1 Built-in datatypes hierarchy illustrating the relationships among primitive and derived data types defined in XML Schema and RDF.*

### 3.1 `rdf:langString`

The class `rdf:langString` is the class of [language-tagged string values](https://www.w3.org/TR/rdf12-concepts/#dfn-language-tagged-string). `rdf:langString` is an instance of `rdfs:Datatype` and a subclass of `rdfs:Literal` (§2.1.3).

### 3.2 `rdf:dirLangString`

The class `rdf:dirLangString` is the class of [directional language-tagged string values](https://www.w3.org/TR/rdf12-concepts/#dfn-dir-lang-string). `rdf:dirLangString` is an instance of `rdfs:Datatype` and a subclass of `rdfs:Literal` (§2.1.3).

### 3.3 `rdf:HTML`

*This section is non-normative.*

The class `rdf:HTML` is the class of [HTML literal values](https://www.w3.org/TR/rdf12-concepts/#section-html). `rdf:HTML` is an instance of `rdfs:Datatype` and a subclass of `rdfs:Literal` (§2.1.3).
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 79](https://github.com/w3c/rdf-schema/issues/79): sections describing `rdf:HTML`, `rdf:XMLLiteral` and `rdf:JSON` should be normative
>
> contrarily to RDF 1.1, the sectionc of RDF 1.2 Concepts describing `rdf:HTML` and `rdf:XMLLiteral` are normative,
> so they should also be normative in RDF Schema.
>
> As for `rdf:JSON`, it was defined normatively in JSON-LD 1.1, and is defined normatively in RDF 1.2 Concepts. So this should also be normative in RDF Schema.

### 3.4 `rdf:XMLLiteral`

*This section is non-normative.*

The class `rdf:XMLLiteral` is the class of [XML literal values](https://www.w3.org/TR/rdf12-concepts/#section-XMLLiteral). `rdf:XMLLiteral` is an instance of `rdfs:Datatype` and a subclass of `rdfs:Literal` (§2.1.3).
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 79](https://github.com/w3c/rdf-schema/issues/79): sections describing `rdf:HTML`, `rdf:XMLLiteral` and `rdf:JSON` should be normative
>
> contrarily to RDF 1.1, the sectionc of RDF 1.2 Concepts describing `rdf:HTML` and `rdf:XMLLiteral` are normative,
> so they should also be normative in RDF Schema.
>
> As for `rdf:JSON`, it was defined normatively in JSON-LD 1.1, and is defined normatively in RDF 1.2 Concepts. So this should also be normative in RDF Schema.

### 3.5 `rdf:JSON`

*This section is non-normative.*

The class `rdf:JSON` is the class of [JSON literal values](https://www.w3.org/TR/rdf12-concepts/#section-json). `rdf:JSON` is an instance of `rdfs:Datatype` and a subclass of `rdfs:Literal` (§2.1.3).
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 79](https://github.com/w3c/rdf-schema/issues/79): sections describing `rdf:HTML`, `rdf:XMLLiteral` and `rdf:JSON` should be normative
>
> contrarily to RDF 1.1, the sectionc of RDF 1.2 Concepts describing `rdf:HTML` and `rdf:XMLLiteral` are normative,
> so they should also be normative in RDF Schema.
>
> As for `rdf:JSON`, it was defined normatively in JSON-LD 1.1, and is defined normatively in RDF 1.2 Concepts. So this should also be normative in RDF Schema.

### 3.6 XML Schema datatypes

All built-in datatypes defined in the W3C XML Schema Definition
Language (XSD) 1.1 Part 2: Datatypes [XMLSCHEMA11-2] are identified
using IRIs of the form `http://www.w3.org/2001/XMLSchema#xxx`,
where `xxx` is the local name of the datatype. Among the full
set of XSD datatypes, the subset listed below comprises those that
are compatible with the RDF data model and are known as RDF-compatible
XSD datatypes [RDF12-CONCEPTS].

- Core types
  * `xsd:string`
  * `xsd:boolean`
  * `xsd:decimal`
  * `xsd:integer`
- IEEE floating-point numbers
  * `xsd:double`
  * `xsd:float`
- Time and date
  * `xsd:date`
  * `xsd:time`
  * `xsd:dateTime`
  * `xsd:dateTimeStamp`
- Recurring and partial dates
  * `xsd:gYear`
  * `xsd:gMonth`
  * `xsd:gDay`
  * `xsd:gYearMonth`
  * `xsd:gMonthDay`
- Duration
  * `xsd:duration`
  * `xsd:yearMonthDuration`
  * `xsd:dayTimeDuration`
- Limited-range integer numbers
  * `xsd:byte`
  * `xsd:short`
  * `xsd:int`
  * `xsd:long`
  * `xsd:unsignedByte`
  * `xsd:unsignedShort`
  * `xsd:unsignedInt`
  * `xsd:unsignedLong`
  * `xsd:positiveInteger`
  * `xsd:nonNegativeInteger`
  * `xsd:negativeInteger`
  * `xsd:nonPositiveInteger`
- Encoded binary data
  * `xsd:hexBinary`
  * `xsd:base64Binary`
- Miscellaneous XSD types
  * `xsd:anyURI`
  * `xsd:language`
  * `xsd:normalizedString`
  * `xsd:token`
  * `xsd:NMTOKEN`
  * `xsd:Name`
  * `xsd:NCName`

## 4. RDF Collections

*This section is non-normative.*

RDF containers are open in the sense that the core RDF specifications
define no mechanism to state that there are no more members. The RDF
Collection vocabulary of classes and properties can describe a closed
collection, i.e. one that can have no more members.

A collection is represented as a list of items, a representation that
will be familiar to those with experience of Lisp and similar
programming languages. There is a [shorthand notation](https://www.w3.org/TR/rdf12-turtle/#collections) in the Turtle syntax specification for representing
collections.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> RDFS does not require that there be only one first element of a
> list-like structure, or even that a list-like structure have a first
> element.

RDF provides a vocabulary for describing collections, i.e.'list
structures', in terms of head-tail links. Collections differ from
containers in allowing branching structure and in having an
explicit terminator, allowing applications to determine the exact
set of items in the collection.

As with containers, no special semantic conditions are imposed on this vocabulary
other than the type of `rdf:nil` being `rdf:List`. It
is intended for use typically in a context where a container is described using
blank nodes to connect a 'well-formed' sequence of items, each described by
two triples of the form `       _:c1 rdf:first aaa .`
`       _:c1 rdf:rest _:c2 .`

where the final item is indicated by the use of `rdf:nil` as the
value of the property `rdf:rest`. In a familiar convention, `rdf:nil` can be thought of as the empty collection. Any such graph amounts to an assertion
that the collection exists, and since the members of the collection can be determined
by inspection, this is often sufficient to enable applications to determine
what is meant. The semantics does not require any collections
to exist other than those mentioned explicitly in a graph (and the empty collection).
For example, the existence of a collection containing two items does not automatically
guarantee that the similar collection with the items permuted also exists: `       _:c1 rdf:first ex:aaa .`
`       _:c1 rdf:rest _:c2 .`
`       _:c2 rdf:first ex:bbb .`
`       _:c2 rdf:rest rdf:nil . `

does not entail

`_:c3 rdf:first ex:bbb .`
`       _:c3 rdf:rest _:c4 .`
` _:c4 rdf:first ex:aaa .`
`      _:c4 rdf:rest rdf:nil .      `

Also, RDF imposes no 'well-formedness' conditions on the use of this
vocabulary, so that it is possible to write RDF graphs which assert
the existence of highly peculiar objects such as lists with forked
or non-list tails, or multiple heads:

`_:666 rdf:first ex:aaa .`
`       _:666 rdf:first ex:bbb .`
`       _:666 rdf:rest ex:ccc .`
`       _:666 rdf:rest rdf:nil . `

It is also possible to write a set of triples which under-specify a collection
by failing to specify its `rdf:rest` property value.

Semantic extensions may
place extra syntactic well-formedness restrictions on the use of this vocabulary
in order to rule out such graphs. They may
exclude interpretations of the collection vocabulary which violate the convention
that the subject of a 'linked' collection of two-triple items of the form described
above, ending with an item ending with `rdf:nil`, denotes a totally
ordered sequence whose members are the referents of the `rdf:first` values of the items, in the order got by tracing the `rdf:rest` properties
from the subject to `rdf:nil`. This permits sequences which contain
other sequences.

The RDFS semantic conditions require that any
subject of the `rdf:first` property, and any subject or object of
the `rdf:rest` property, be of `rdf:type rdf:List`.

### 4.1 `rdf:List`

`rdf:List` is an instance of `rdfs:Class` (§2.1.2) that can be used to build descriptions of lists and other list-like
structures.

### 4.2 `rdf:first`

`rdf:first` is an instance of `rdf:Property` (§2.1.5) that can be used to build descriptions of lists and other list-like
structures.

A triple of the form:
> `L rdf:first O`

states that there is a first-element relationship between *L* and *O*.

The `rdfs:domain` (§2.2.2) of `rdf:first` is `rdf:List` (§4.1). The `rdfs:range` (§2.2.1) of `rdf:first` is `rdfs:Resource` (§2.1.1).

### 4.3 `rdf:rest`

`rdf:rest` is an instance of `rdf:Property` (§2.1.5) that can be used to build descriptions of lists and other list-like
structures.

A triple of the form:
> `L rdf:rest O`

states that there is a rest-of-list relationship between *L* and *O*.

The `rdfs:domain` (§2.2.2) of `rdf:rest` is `rdf:List` (§4.1). The `rdfs:range` (§2.2.1) of `rdf:rest` is `rdf:List` (§4.1).

### 4.4 `rdf:nil`

The resource `rdf:nil` is an instance of `rdf:List` (§4.1) that can be used to represent an empty list or other list-like
structure.

A triple of the form:
> `L rdf:rest rdf:nil`

states that *L* is an instance of `rdf:List` (§4.1) that has one item; that item can be indicated using the `rdf:first` (§4.2) property.

## 5. Triple-term based reification

A triple term is a construct defined in [RDF12-CONCEPTS], consisting in an RDF triple that is used
as a value, specifically, in the object position of another triple. This use represents a reference to a proposition,
and, importantly, a triple term does not by itself imply assertion; that is, the proposition it denotes
is not necessarily a fact asserted by the RDF graph. This is only the case if that triple is also
asserted in the RDF graph — that is, if it is a direct element of that set of triples.
Otherwise, it remains unasserted and serves primarily as a reference.
This enables the representation of metadata or commentary about triples that may or may not be part
of the asserted graph content, including potentially contradictory relationships.

RDF terms that appear in a triple term have the same denotation as when they appear in an asserted
triple in the graph. For this reason, triple terms are said to be *transparent*.

A triple term can be the object of a triple whose predicate is `rdf:reifies` (§5.2). In such cases, the resulting triple is referred
to as a *[reifying triple](https://www.w3.org/TR/rdf12-concepts/#dfn-reifying-triple)*, and its subject is
termed a *[reifier](https://www.w3.org/TR/rdf12-concepts/#dfn-reifier)*.
When the triple term of a reifying triple also appears in the same graph as an asserted triple,
the subset of triples that share the same
reifier as subject is called a *[triple annotation](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-annotation)*.

Triple terms always denote abstract, logical propositions, while reifiers may denote a variety of
things related to these propositions (such as a statement or belief that the proposition holds, or
an event or circumstance that makes the proposition true). It is therefore expected that triple
terms are commonly used as objects of reifying triples, and that reifiers (rather than the triple
terms) are used in further descriptions. Because of the diversity of use cases that reifiers aim to
serve, the meaning of the `rdf:reifies` property is deliberately generic. Multiple,
distinct reifiers may exist for the same proposition (e.g., from different sources or contexts), and,
conversely, one reifier may be used for several propositions.

### 5.1 `rdfs:Proposition`

`rdfs:Proposition` is the class of propositions, simple logical expressions describing a relationship between two entities. `rdfs:Proposition` is an instance of `rdfs:Class` (§2.1.2) and a subclass of `rdfs:Resource` (§2.1.1).

### 5.2 `rdf:reifies`

`rdf:reifies` is an instance of `rdf:Property` (§2.1.5) that is used to associate a resource with a proposition.

The `rdfs:domain` (§2.2.2) of `rdf:reifies` is `rdfs:Resource` (§2.1.1).
The `rdfs:range` (§2.2.1) of `rdf:reifies` is `rdfs:Proposition` (§5.1).

## 6. Utility Properties

The following utility classes and properties are defined in the RDF
core
namespaces.

### 6.1 `rdf:value`

`rdf:value` is an instance of `rdf:Property` (§2.1.5) that may be used in
describing structured values.

`rdf:value` has no meaning on its own. It is provided as a piece of
vocabulary that may be used in idioms such as illustrated
in example below:
> **Example:**
>
> Example 1
>
>
>
> ```
> <http://www.example.com/2002/04/products#item10245>
>     <http://www.example.org/terms/weight> [
>        rdf:value 2.4 ;
>        <http://www.example.org/terms/units> <http://www.example.org/units/kilograms>
>        ] .
> ```

Despite
the lack of formal specification of the meaning of this property,
there is
value in defining it to encourage the use of a common idiom in
examples of
this kind.

The `rdfs:domain` (§2.2.2) of `rdf:value` is `rdfs:Resource` (§2.1.1).
The `rdfs:range` (§2.2.1) of `rdf:value` is `rdfs:Resource` (§2.1.1).

## 7. Legacy vocabularies

*This section is non-normative.*

This section describes vocabularies defined in earlier versions of
RDF and RDF Schema. These vocabularies remain in use in certain
applications and data sets for historical and compatibility reasons.
However, the vocabularies and constructs presented in the preceding
sections of this document are generally recommended as preferable
alternatives for new developments and modern RDF-based systems.

### 7.1 Containers

*This section is non-normative.*

RDF containers are resources that are used to represent collections.
The same resource may appear in a container more than
once. Unlike containment in the physical world, a container may be
contained in itself.

Three different kinds of container are defined. Whilst the formal
semantics [RDF12-SEMANTICS] of all three classes of container are
identical,
different classes may be used to indicate informally further
information. An `rdf:Bag` is used to indicate that the container is
intended to be unordered. An `rdf:Seq` is used to indicate that the
order indicated by the numerical order of the container membership properties (§7.1.5) of the container is intended to be significant. An `rdf:Alt` container
is used
to indicate that typical processing of the container will be to select
one of
the members.

Just as a hen house may have the property that it is made of wood,
that
does not mean that all the hens it contains are made of wood, a
property of a
container is not necessarily a property of all of its members.

RDF provides vocabularies for describing three classes of
containers. Containers have a type, and their members can
be enumerated by using a fixed set of *container membership
properties*. These properties are indexed by integers to
provide a way to distinguish the members from each other, but these
indices should not necessarily be thought of as defining an
ordering of the container itself; some containers are considered to be unordered.

The RDFS vocabulary adds a generic membership
property which holds regardless of position, and classes containing
all the containers and all the membership properties.

One should understand this vocabulary as *describing* containers, rather than as a tool for constructing them, as
would typically be supplied by a programming language. The actual containers are entities in the semantic universe,
and RDF graphs which use the vocabulary simply provide very basic
information about these entities, enabling an RDF graph to
characterize the container type and give partial information about
the members of a container. Since the RDF container vocabulary is
so limited, many natural assumptions concerning RDF containers
cannot be formally sanctioned by the RDF formal semantics. This should not be taken as
meaning that these assumptions are false, but only that RDF does
not formally entail that they must be true.

There are no special semantic conditions on the container
vocabulary: the only structure which RDF presumes its containers
to have is what can be inferred from the use of this vocabulary and
the general RDF semantic conditions. This amounts to knowing the type of a container, and having a partial
enumeration
of the items in the container. The intended mode of use is that things
of type `rdf:Bag` are considered to be unordered but to allow duplicates; things of
type `rdf:Seq` are considered to be ordered, and things
of type `rdf:Alt` are considered to represent a
collection of alternatives, possibly with a preference ordering.
If the container is of an ordered type, then the ordering of items in the container is intended to be
indicated by the numerical ordering of the container membership
properties, which are assumed to be single-valued.
However, these informal conditions are not reflected in any formal RDF
entailments.

The RDF semantics does not support any entailments which could arise from enumerating
the elements of an unordered `rdf:Bag` in a different order. For example,

`_:xxx rdf:type rdf:Bag .`
`        _:xxx rdf:_1 ex:a .`
`        _:xxx rdf:_2 ex:b .`

does not entail

`_:xxx rdf:_1 ex:b .`
`        _:xxx rdf:_2 ex:a .`

(If this c> valid, then the result of
adding it to the original graph would be entailed by the graph, and this would assert that both elements were in both
positions. This is a consequence of the fact that RDF is a purely
assertional language.)

There is no assumption that a property of a container applies to
any of the elements of the container, or vice versa.

There is no formal requirement that
the three container classes are disjoint, so that for example
it is consistent to assert that something is both an `rdf:Bag` and an `rdf:Seq`.
There is no assumption that containers are gap-free, so that for example

`_:xxx rdf:type rdf:Seq.`
`        _:xxx rdf:_1 ex:a .`
`        _:xxx rdf:_3 ex:c .`

does not entail

`_:xxx rdf:_2 _:yyy .`

There is no way in RDF to assert
that a container contains only a fixed number of members. This is a
reflection of the fact that it is always consistent to add a triple
to a graph asserting a membership property of any container. And
finally, there is no built-in assumption that an RDF container has
only finitely many members.

RDF containers are defined by the following classes and properties.

#### 7.1.1 `rdfs:Container`

The `rdfs:Container` class is a super-class of the RDF
Container classes, i.e. `rdf:Bag` (§7.1.2), `rdf:Seq` (§7.1.3), `rdf:Alt` (§7.1.4).

#### 7.1.2 `rdf:Bag`

The `rdf:Bag` class is the class of RDF 'Bag'
containers. It is
a subclass of `rdfs:Container` (§7.1.1).
Whilst formally it is no
different from an `rdf:Seq` (§7.1.3) or an `rdf:Alt` (§7.1.4), the `rdf:Bag` class is used
conventionally to indicate to a human reader that the container is
intended
to be unordered.

#### 7.1.3 `rdf:Seq`

The `rdf:Seq` class is the class of RDF 'Sequence'
containers.
It is a subclass of `rdfs:Container` (§7.1.1).
Whilst formally it is no
different from an `rdf:Bag` (§7.1.2) or an `rdf:Alt` (§7.1.4), the `rdf:Seq` class is used
conventionally to indicate to a human reader that the numerical
ordering of
the container membership properties (§7.1.5) of the container is intended to be significant.

#### 7.1.4 `rdf:Alt`

The `rdf:Alt` class is the class of RDF 'Alternative'
containers. It is a subclass of `rdfs:Container` (§7.1.1). Whilst formally
it is no
different from an `rdf:Seq` (§7.1.3) or an `rdf:Bag` (§7.1.2), the `rdf:Alt` class is used
conventionally to indicate to a human reader that typical processing
will be
to select one of the members of the container. The first member of
the
container, i.e. the value of the `rdf:_1` (§7.1.5) property, is the
default choice.

#### 7.1.5 `rdfs:ContainerMembershipProperty`

The `rdfs:ContainerMembershipProperty` class has as
instances
the properties `rdf:_1, rdf:_2, rdf:_3 ...` that are
used to state
that a resource is a member of a container. `rdfs:ContainerMembershipProperty` is a subclass of `rdf:Property` (§2.1.5). Each
instance of `rdfs:ContainerMembershipProperty` is an `rdfs:subPropertyOf` (§2.2.5) the `rdfs:member` (§7.1.6) property.

Given a container *C*, a triple of the form:
> `C rdf:_nnn O`

where `nnn` is the decimal representation of an integer
greater than 0 with
no leading zeros, states that *O* is a member of the container *C*.

Container membership properties may be applied to resources other
than containers.

#### 7.1.6 `rdfs:member`

`rdfs:member` is an instance of `rdf:Property` (§2.1.5) that is a super-property of all
the container membership properties i.e. each container membership
property
has an `rdfs:subPropertyOf` (§2.2.5) relationship to the property `rdfs:member`.

The `rdfs:domain` (§2.2.2) of `rdfs:member` is `rdfs:Resource` (§2.1.1).
The `rdfs:range` (§2.2.1) of `rdfs:member` is `rdfs:Resource` (§2.1.1).

### 7.2 "Old-style" Reification

*This section is non-normative.*

The intended meaning of this vocabulary is to allow an RDF graph to act as metadata describing other RDF triples.

Consider an example graph containing a single triple:

`ex:a ex:b ex:c .`

and suppose that IRI `ex:graph1` is used to identify this graph.
Exactly how this identification is achieved is external to the RDF model,
but it might be by the IRI resolving to a concrete syntax document describing the graph,
or by the IRI being the associated name of a named graph in a dataset.
Assuming that the IRI can be used to denote the triple,
then the reification vocabulary allows us to describe the first graph in another graph:

`ex:graph1 rdf:type rdf:Statement .`
`       ex:graph1 rdf:subject ex:a .`
`       ex:graph1 rdf:predicate ex:b .`
`       ex:graph1 rdf:object ex:c .`

The second graph is called a reification of the triple in the first graph.

Reification is not a form of quotation. Rather, the reification describes the
relationship between a token of a triple and the resources that the triple denotes.
The value of the `rdf:subject` property is not the
subject IRI itself but the thing it denotes, and similarly for `rdf:predicate` and `rdf:object`.
For example, if the referent of `ex:a` is Mount Everest,
then the subject of the reified triple is also the mountain, not the IRI which denotes it.

Reifications can be written with a blank node as subject,
or with an IRI subject which does not identify any concrete realization of a triple,
in both of which cases they simply assert the existence of the described triple.

The subject of a reification is intended to denote a concrete realization of an RDF triple, such as a document in a surface syntax, rather than a triple considered as an abstract object. This supports use cases where properties such as dates of
composition or provenance information are applied to the
reified triple, which are meaningful only when thought of as
denoting a particular instance or token of a triple.

A reification of a triple does not entail the triple, and is not entailed by it.
The reification only says that the triple token exists and what it is about,
not that it is true, so it does not entail the triple.
On the other hand, asserting a triple does not automatically imply that any
triple tokens exist in the universe being described by the triple.
For example, the triple might be part of an ontology describing
animals, which could be satisfied by an interpretation in which the
universe contained only animals, and in which a reification of it was therefore
false.

Since the relation between triples and reifications of triples
in any RDF graph or graphs need not be one-to-one, asserting a
property about some entity described by a reification need not
entail that the same property holds of another such entity, even if
it has the same components. For example,

`_:xxx rdf:type rdf:Statement .`
`       _:xxx rdf:subject ex:subject .`
`       _:xxx rdf:predicate ex:predicate .`
`       _:xxx rdf:object ex:object .`
`       _:yyy rdf:type rdf:Statement .`
`       _:yyy rdf:subject ex:subject .`
`       _:yyy rdf:predicate ex:predicate .`
`       _:yyy rdf:object ex:object .`
`       _:xxx ex:property ex:foo .`

does not entail

`_:yyy ex:property ex:foo .`

#### 7.2.1 `rdf:Statement`

`rdf:Statement` is an instance of `rdfs:Class` (§2.1.2).
It is intended to represent the class of RDF statements. An RDF
statement is the statement made by a token of an RDF triple. The
subject of an RDF statement is the instance of `rdfs:Resource` (§2.1.1) identified by the subject of the triple. The predicate of an RDF
statement is the instance of `rdf:Resource` (§2.1.1) identified by the predicate of the triple. The object of an RDF
statement is the instance of `rdfs:Resource` (§2.1.1) identified by the object of the triple. `rdf:Statement` is in the domain of the properties `rdf:predicate` (§7.2.3), `rdf:subject` (§7.2.2) and `rdf:object` (§7.2.4). Different
individual `rdf:Statement` instances may have the same
values for their `rdf:predicate` (§7.2.3), `rdf:subject` (§7.2.2) and `rdf:object` (§7.2.4) properties.

RDF statements are not triples in an RDF graph so their values
for `rdf:predicate` (§7.2.3) do not need to be instances of `rdf:Property` (§2.1.5) in that graph,
although in most cases they will be.

#### 7.2.2 `rdf:subject`

`rdf:subject` is an instance of `rdf:Property` (§2.1.5) that is used to state the
subject of a statement.

A triple of the form:
> `S rdf:subject R`

states that *S* is an instance of `rdf:Statement` (§7.2.1) and that the subject of *S* is
R.

The `rdfs:domain` (§2.2.2) of `rdf:subject` is `rdf:Statement` (§7.2.1). The `rdfs:range` (§2.2.1) of `rdf:subject` is `rdfs:Resource` (§2.1.1).

#### 7.2.3 `rdf:predicate`

`rdf:predicate` is an instance of `rdf:Property` (§2.1.5) that is used to state the
predicate of a statement.

A triple of the form:
> `S rdf:predicate P`

states that *S* is an instance of `rdf:Statement` (§7.2.1),
that *P* is an instance of `rdfs:Resource` (§2.1.1) and that the
predicate
of *S* is *P*.

The `rdfs:domain` (§2.2.2) of `rdf:predicate` is `rdf:Statement` (§7.2.1) and the `rdfs:range` (§2.2.1) is `rdfs:Resource` (§2.1.1).

#### 7.2.4 `rdf:object`

`rdf:object` is an instance of `rdf:Property` (§2.1.5) that is used to state the
object of a statement.

A triple of the form:
> `S rdf:object O`

states that *S* is an instance of `rdf:Statement` (§7.2.1) and that the object of *S* is *O*.

The `rdfs:domain` (§2.2.2) of `rdf:object` is `rdf:Statement` (§7.2.1).
The `rdfs:range` (§2.2.1) of `rdf:object` is `rdfs:Resource` (§2.1.1).

## 8. RDF Schema summary

*This section is non-normative.*

The tables in this section provide an overview of the RDF Schema vocabulary.

### 8.1 RDF classes

| Class name                                                                                               | comment                                                                                                             |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `rdfs:Resource` (§2.1.1)                                       | The class resource, everything.                                                                                     |
| `rdfs:Literal` (§2.1.3)                                         | The class of literal values, e.g. textual strings and integers.                                                     |
| `rdf:langString` (§3.1)                                    | The class of language-tagged string literal values.                                                                 |
| `rdf:dirLangString` (§3.2)                              | The class of directional language-tagged string literal values.                                                     |
| `rdf:HTML` (§3.3)                                                | The class of HTML literal values.                                                                                   |
| `rdf:XMLLiteral` (§3.4)                                    | The class of XML literal values.                                                                                    |
| `rdf:JSON` (§3.5)                                                | The class of JSON literal values.                                                                                   |
| `rdfs:Class` (§2.1.2)                                             | The class of classes.                                                                                               |
| `rdf:Property` (§2.1.5)                                        | The class of RDF properties.                                                                                        |
| `rdfs:Proposition` (§5.1)                                 | The class of reified triples.                                                                                       |
| `rdfs:Datatype` (§2.1.4)                                       | The class of RDF datatypes.                                                                                         |
| `rdf:Statement` (§7.2.1)                                      | The class of RDF statements.                                                                                        |
| `rdf:Bag` (§7.1.2)                                                  | The class of unordered containers.                                                                                  |
| `rdf:Seq` (§7.1.3)                                                  | The class of ordered containers.                                                                                    |
| `rdf:Alt` (§7.1.4)                                                  | The class of containers of alternatives.                                                                            |
| `rdfs:Container` (§7.1.1)                                     | The class of RDF containers.                                                                                        |
| `rdfs:ContainerMembershipProperty` (§7.1.5) | The class of container membership properties, `rdf:_1`, `rdf:_2`, ..., all of which are sub-properties of 'member'. |
| `rdf:List` (§4.1)                                                | The class of RDF Lists.                                                                                             |

### 8.2 RDF properties

| Property name                                                                | comment                                                | domain          | range              |
| ---------------------------------------------------------------------------- | ------------------------------------------------------ | --------------- | ------------------ |
| `rdf:type` (§2.2.3)                    | The subject is an instance of a class.                 | `rdfs:Resource` | `rdfs:Class`       |
| `rdf:reifies` (§5.2)              | Associates a resource with a reified triple.           | `rdfs:Resource` | `rdfs:Proposition` |
| `rdfs:subClassOf` (§2.2.4)       | The subject is a subclass of a class.                  | `rdfs:Class`    | `rdfs:Class`       |
| `rdfs:subPropertyOf` (§2.2.5) | The subject is a subproperty of a property.            | `rdf:Property`  | `rdf:Property`     |
| `rdfs:domain` (§2.2.2)               | A domain of the subject property.                      | `rdf:Property`  | `rdfs:Class`       |
| `rdfs:range` (§2.2.1)                 | A range of the subject property.                       | `rdf:Property`  | `rdfs:Class`       |
| `rdfs:label` (§2.3.1)                 | A human-readable name for the subject.                 | `rdfs:Resource` | `rdfs:Literal`     |
| `rdfs:comment` (§2.3.2)             | A description of the subject resource.                 | `rdfs:Resource` | `rdfs:Literal`     |
| `rdfs:member` (§7.1.6)               | A member of the subject resource.                      | `rdfs:Resource` | `rdfs:Resource`    |
| `rdf:first` (§4.2)                  | The first item in the subject RDF list.                | `rdf:List`      | `rdfs:Resource`    |
| `rdf:rest` (§4.3)                    | The rest of the subject RDF list after the first item. | `rdf:List`      | `rdf:List`         |
| `rdfs:seeAlso` (§2.3.3)             | Further information about the subject resource.        | `rdfs:Resource` | `rdfs:Resource`    |
| `rdfs:isDefinedBy` (§2.3.4)     | The definition of the subject resource.                | `rdfs:Resource` | `rdfs:Resource`    |
| `rdf:value` (§6.1)                  | Idiomatic property used for structured values.         | `rdfs:Resource` | `rdfs:Resource`    |
| `rdf:subject` (§7.2.2)              | The subject of the subject RDF statement.              | `rdf:Statement` | `rdfs:Resource`    |
| `rdf:predicate` (§7.2.3)          | The predicate of the subject RDF statement.            | `rdf:Statement` | `rdfs:Resource`    |
| `rdf:object` (§7.2.4)                | The object of the subject RDF statement.               | `rdf:Statement` | `rdfs:Resource`    |

In addition to these classes and properties, RDF uses properties
called `rdf:_1`, `rdf:_2`, `rdf:_3`, etc.,
each of which is both a sub-property of `rdfs:member` and
an
instance of the class `rdfs:ContainerMembershipProperty`.
There is
also an instance of `rdf:List` called `rdf:nil` that is
an empty `rdf:List`.

## A. Vocabulary Registry

*This section is non-normative.*

This section defines a registry for the vocabulary in the RDF core namespaces
in accordance with [§ 6.5 The Registry Track](https://www.w3.org/policies/process/#registries) of the W3C Process [W3C-PROCESS].

The purpose of this registry is to provide a central index where anyone can
find out what vocabulary entries exist in the RDF core namespaces and where
they are formally defined, to avoid collisions and duplication.

Each registry table has the following three fields: an IRI, the governing
specification, and any relevant notes (such as applicable scope).

The policy for changes to existing entries is as follows:

- Entries can be marked as deprecated but not deleted.
- Entries can be updated to reflect any changes to the governing specification or the notes.

The custodian for all registry tables is the RDF & SPARQL Working Group.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 81](https://github.com/w3c/rdf-schema/issues/81): Custodian of the vocabulary registry should be defined more robustly
>
> Rather than "the RDF & SPARQL Working Group", I would identity the custodian of the registry as "the Working Group in charge of this document". This is more future proof.
>
> It might also be useful to identify a fallback in case such a Working Group does not exist.
> The RDF-Dev CG could be one? The team?
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 80](https://github.com/w3c/rdf-schema/issues/80): Criteria for inclusion in the vocabulary registry should be described
>
> The §A Vocabulary Registry defined in RDF 1.2 Schema should define criteria for including new entries.
>
> I propose that new entries should
>
> - be defined by W3C REC-track specifications, and
> - be of general utility for RDF (otherwise they belong to their own separate vocabulary)

### A.1 `rdf:` Namespace

*This section is non-normative.*

The following registry table lists all the IRIs defined in the `rdf:` namespace.

A machine-readable version of this table is available at [`http://www.w3.org/1999/02/22-rdf-syntax-ns`](https://www.w3.org/1999/02/22-rdf-syntax-ns).

| IRI                            | Specification                                                                                                                                           | Notes                                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rdf:Alt`                      | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:Bag`                      | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:Seq`                      | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:HTML`                     | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:JSON `                    | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:XMLLiteral`               | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:List`                     | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:Property`                 | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:Statement`                | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:nil`                      | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:rest`                     | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:dirLangString`            | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:first`                    | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:langString`               | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:object`                   | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:predicate`                | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:subject`                  | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:reifies`                  | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:type`                     | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:value`                    | This document                                                                                                                                           |                                                                                                                                                            |
| `rdf:CompoundLiteral`          | [JSON-LD11]                                                                          | Consideration should be given to the use of `rdf:dirLangString`. This term is considered archaic but retained for compatibility with JSON-LD.              |
| `rdf:direction`                | [JSON-LD11]                                                                          | Consideration should be given to the use of `rdf:dirLangString`. This term is considered archaic but retained for compatibility with JSON-LD.              |
| `rdf:language`                 | [JSON-LD11]                                                                          | Consideration should be given to the use of `rdf:dirLangString`. This term is considered archaic but retained for compatibility with JSON-LD.              |
| `rdf:PlainLiteral`             | [RDF-PLAIN-LITERAL] | Only used in OWL [OWL2-OVERVIEW] |
| `rdf:langRange`                | [RDF-PLAIN-LITERAL] | Only used in OWL [OWL2-OVERVIEW] |
| `rdf:PropositionForm`          | [RDF-INTEROP]                                                         | Reserved for basic encoding of propositions.                                                                                                               |
| `rdf:propositionFormSubject`   | [RDF-INTEROP]                                                         | Reserved for basic encoding of propositions.                                                                                                               |
| `rdf:propositionFormPredicate` | [RDF-INTEROP]                                                         | Reserved for basic encoding of propositions.                                                                                                               |
| `rdf:propositionFormObject`    | [RDF-INTEROP]                                                         | Reserved for basic encoding of propositions.                                                                                                               |

### A.2 `rdfs:` Namespace

*This section is non-normative.*

The following registry table lists all the IRIs defined in the `rdfs:` namespace.
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 82](https://github.com/w3c/rdf-schema/issues/82): The vocabulary registry should not cover rdfs:, only rdf:
>
> I don't think that the rdfs: namespace should be open for extension.
>
> For me, the rdfs: vocabulary should be restricted to terms that have a specific semantics under RDFS entailmenent, and therefore are the prerogative of the WG maintaining RDF.
>
> (I know that this is not entirely true today, for historical reason, but that should be the criteria for adding new terms in `rdfs:` rather than in `rdf:`, anyway...).

A machine-readable version of this table is available at [`http://www.w3.org/2000/01/rdf-schema`](https://www.w3.org/2000/01/rdf-schema).

| IRI                                | Specification |
| ---------------------------------- | ------------- |
| `rdfs:Class`                       | This document |
| `rdfs:Container`                   | This document |
| `rdfs:ContainerMembershipProperty` | This document |
| `rdfs:Datatype`                    | This document |
| `rdfs:Literal`                     | This document |
| `rdfs:Proposition`                 | This document |
| `rdfs:Resource`                    | This document |
| `rdfs:comment`                     | This document |
| `rdfs:domain`                      | This document |
| `rdfs:isDefinedBy`                 | This document |
| `rdfs:label`                       | This document |
| `rdfs:member`                      | This document |
| `rdfs:range`                       | This document |
| `rdfs:seeAlso`                     | This document |
| `rdfs:subClassOf`                  | This document |
| `rdfs:subPropertyOf`               | This document |

## B. Privacy Considerations

*This section is non-normative.*

See [Privacy Considerations](https://www.w3.org/TR/rdf12-concepts/#privacy) in [RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/) [RDF12-CONCEPTS].

## C. Security Considerations

*This section is non-normative.*

See [Security Considerations](https://www.w3.org/TR/rdf12-concepts/#security) in [RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/) [RDF12-CONCEPTS].

## E. Change since 2004 Recommendation

*This section is non-normative.*

Changes for RDF 1.1 Recommendation

- Conversion to ReSpec, including formatting of examples and notes.
- References to RDF 1.0 documents where appropriate
  replaced by references to RDF 1.1 documents.
- Replaced the term "URI Reference" with the term "IRI".
- Removed discussion about distinction between plain and typed
  literals, as this distinction is absent in RDF 1.1 and has no
  technical bearing on RDF Schema.
- Removed the introductory paragraph of Sec. "Reification Vocabulary" (§7.2), as this discussion is not related to the
  technical content and is irrelevant and confusing now.
- Update of affiliation of the editors.
- Added RDF WG to the Acknowledgments section.
- Renamed the document from "RDF Vocabulary Description Language
  1.0: RDF Schema" to "RDF Schema 1.1", as the term Vocabulary
  Description Language has led to confusion.
- Three paragraphs of the Introduction were left out. These
  paragraphs described the things that RDF Schema does not do and are
  now much less relevant than in 2004.
- Added the datatypes `rdf:langString` and `rdf:HTML`.
- Removed Appendix "RDF Schema in RDF/XML". It was informative, but
  now out of date, in terms of content and in terms of
  syntax.
- Marked `rdf:HTML` and `rdf:XMLLiteral` as non-normative.
- Removed references to 2004 Primer from Secs. 5.1, 5.2
  and 5.4.3. In the latter case the example referred to was
  moved into this document for readability purposes.

## F. Changes between RDF 1.1 and RDF 1.2

*This section is non-normative.*

- Added the datatype `rdf:dirLangString`.
- Added the datatype `rdf:JSON`.
- Added the class `rdfs:Proposition` and the property `rdf:reifies`.
- Reorganization of the document structure.
- Added the vocabulary registry.
- Added the Privacy Considerations and Security Considerations.

## G. Index

### G.1 Terms defined by this specification

### G.2 Terms defined by reference

- [RDF12-CONCEPTS] defines the following:
  * directional language-tagged string values
  * HTML literal values
  * IRIs
  * JSON literal values
  * language-tagged string values
  * literal
  * Privacy Considerations
  * RDF datatype
  * reifier
  * reifying triple
  * Security Considerations
  * triple annotation
  * XML literal values
- [RDF12-SEMANTICS] defines the following:
  * semantic extension
- [RDF12-TURTLE] defines the following:
  * shorthand notation

## H. References

### H.1 Informative references

[JSON-LD11]

[JSON-LD 1.1](https://www.w3.org/TR/json-ld11/). Gregg Kellogg; Pierre-Antoine Champin; Dave Longley. W3C. 16 July 2020. W3C Recommendation. URL: <https://www.w3.org/TR/json-ld11/>

[OWL2-OVERVIEW]

[OWL 2 Web Ontology Language Document Overview (Second Edition)](https://www.w3.org/TR/owl2-overview/). W3C OWL Working Group. W3C. 11 December 2012. W3C Recommendation. URL: <https://www.w3.org/TR/owl2-overview/>

[RDF-INTEROP]

[RDF 1.2 Interoperability](https://www.w3.org/TR/rdf12-interop/). Pierre-Antoine Champin. W3C. 23 July 2026. DNOTE. URL: <https://www.w3.org/TR/rdf12-interop/>

[RDF-NOT]

[What the Semantic Web can represent](https://www.w3.org/DesignIssues/RDFnot.html). Tim Berners-Lee. W3C. 17 September 1998. W3C-Internal Document. URL: <https://www.w3.org/DesignIssues/RDFnot.html>

[RDF-PLAIN-LITERAL]

[rdf:PlainLiteral: A Datatype for RDF Plain Literals (Second Edition)](https://www.w3.org/TR/rdf-plain-literal/). Jie Bao; Sandro Hawke; Boris Motik; Peter Patel-Schneider; Axel Polleres. W3C. 11 December 2012. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-plain-literal/>

[RDF11-SCHEMA]

[RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/). Dan Brickley; Ramanathan Guha. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-schema/>

[RDF12-CONCEPTS]

[RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/). Andy Seaborne; Gregg Kellogg; Olaf Hartig; Pierre-Antoine Champin. W3C. 7 April 2026. W3C Candidate Recommendation. URL: <https://www.w3.org/TR/rdf12-concepts/>

[RDF12-N-QUADS]

[RDF 1.2 N-Quads](https://www.w3.org/TR/rdf12-n-quads/). Gregg Kellogg; Dominik Tomaszuk. W3C. 8 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-n-quads/>

[RDF12-N-TRIPLES]

[RDF 1.2 N-Triples](https://www.w3.org/TR/rdf12-n-triples/). Gregg Kellogg; Dominik Tomaszuk. W3C. 7 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-n-triples/>

[RDF12-NEW]

[What’s New in RDF 1.2](https://w3c.github.io/rdf-new/spec/). The W3C RDF & SPARQL Working Group. W3C. W3C Editor's Draft. URL: <https://w3c.github.io/rdf-new/spec/>

[RDF12-PRIMER]

[RDF 1.2 Primer](https://www.w3.org/TR/rdf12-primer/). Pierre-Antoine Champin; Niklas Lindström. W3C. 17 September 2026. DNOTE. URL: <https://www.w3.org/TR/rdf12-primer/>

[RDF12-SEMANTICS]

[RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/). Peter Patel-Schneider; Dörthe Arndt; Enrico Franconi. W3C. 24 September 2026. CRD. URL: <https://www.w3.org/TR/rdf12-semantics/>

[RDF12-TRIG]

[RDF 1.2 TriG](https://www.w3.org/TR/rdf12-trig/). Gregg Kellogg; Dominik Tomaszuk. W3C. 7 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-trig/>

[RDF12-TURTLE]

[RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/). Gregg Kellogg; Andy Seaborne; Dominik Tomaszuk. W3C. 7 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-turtle/>

[RDF12-XML]

[RDF 1.2 XML Syntax](https://www.w3.org/TR/rdf12-xml/). Gregg Kellogg; Jerven Bolleman. W3C. 9 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-xml/>

[SPARQL12-CONCEPTS]

[SPARQL 1.2 Concepts](https://w3c.github.io/sparql-concepts/spec/). The W3C RDF & SPARQL Working Group. W3C. W3C Editor's Draft. URL: <https://w3c.github.io/sparql-concepts/spec/>

[SPARQL12-ENTAILMENT]

[SPARQL 1.2 Entailment Regimes](https://www.w3.org/TR/sparql12-entailment/). Peter Patel-Schneider. W3C. 9 April 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-entailment/>

[SPARQL12-FEDERATED-QUERY]

[SPARQL 1.2 Federated Query](https://www.w3.org/TR/sparql12-federated-query/). Ruben Taelman; Gregory Williams. W3C. 23 April 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-federated-query/>

[SPARQL12-GRAPH-STORE-PROTOCOL]

[SPARQL 1.2 Graph Store Protocol](https://www.w3.org/TR/sparql12-graph-store-protocol/). Andy Seaborne; Thomas Pellissier Tanon. W3C. 24 September 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-graph-store-protocol/>

[SPARQL12-NEW]

[What’s New in SPARQL 1.2](https://w3c.github.io/sparql-new/spec/). The W3C RDF & SPARQL Working Group. W3C. W3C Editor's Draft. URL: <https://w3c.github.io/sparql-new/spec/>

[SPARQL12-PROTOCOL]

[SPARQL 1.2 Protocol](https://www.w3.org/TR/sparql12-protocol/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 23 July 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-protocol/>

[SPARQL12-QUERY]

[SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/). Olaf Hartig; Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 8 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-query/>

[SPARQL12-RESULTS-CSV-TSV]

[SPARQL 1.2 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql12-results-csv-tsv/). Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 23 July 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-csv-tsv/>

[SPARQL12-RESULTS-JSON]

[SPARQL 1.2 Query Results JSON Format](https://www.w3.org/TR/sparql12-results-json/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 13 August 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-json/>

[SPARQL12-RESULTS-XML]

[SPARQL 1.2 Query Results XML Format](https://www.w3.org/TR/sparql12-results-xml/). Ruben Taelman; Dominik Tomaszuk; Thomas Pellissier Tanon. W3C. 27 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-xml/>

[SPARQL12-SERVICE-DESCRIPTION]

[SPARQL 1.2 Service Description](https://www.w3.org/TR/sparql12-service-description/). Ruben Taelman; Gregory Williams. W3C. 23 April 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-service-description/>

[SPARQL12-UPDATE]

[SPARQL 1.2 Update](https://www.w3.org/TR/sparql12-update/). Ruben Taelman; Andy Seaborne; Thomas Pellissier Tanon. W3C. 12 June 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-update/>

[W3C-PROCESS]

[W3C Process Document](https://www.w3.org/policies/process/). Elika J. Etemad (fantasai); Florian Rivoal. W3C. 18 August 2025. URL: <https://www.w3.org/policies/process/>

[XMLSCHEMA11-2]

[W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/). David Peterson; Sandy Gao; Ashok Malhotra; Michael Sperberg-McQueen; Henry Thompson; Paul V. Biron et al. W3C. 5 April 2012. W3C Recommendation. URL: <https://www.w3.org/TR/xmlschema11-2/>

Permalink

**Referenced in:**

- § 3.2 rdf:dirLangString

Permalink

**Referenced in:**

- § 3.3 rdf:HTML

Permalink

**Referenced in:**

- § 2.1 Classes

Permalink

**Referenced in:**

- § 3.5 rdf:JSON

Permalink

**Referenced in:**

- § 3.1 rdf:langString

Permalink

**Referenced in:**

- § 2.1.3 rdfs:Literal
- § 2.3.1 rdfs:label
- § 2.3.2 rdfs:comment

Permalink

**Referenced in:**

- § B. Privacy Considerations

Permalink

**Referenced in:**

- § 2.1 Classes
- § 2.1.4 rdfs:Datatype

Permalink

**Referenced in:**

- § 5. Triple-term based reification

Permalink

**Referenced in:**

- § 5. Triple-term based reification

Permalink

**Referenced in:**

- § C. Security Considerations

Permalink

**Referenced in:**

- § 5. Triple-term based reification

Permalink

**Referenced in:**

- § 3.4 rdf:XMLLiteral

Permalink

**Referenced in:**

- § 1. Introduction

Permalink

**Referenced in:**

- § 4. RDF Collections
