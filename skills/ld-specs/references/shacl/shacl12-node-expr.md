---
title: "SHACL 1.2 Node Expressions"
source: https://www.w3.org/TR/shacl12-node-expr/
family: shacl
version: "1.2"
status: W3C Working Draft
spec_date: 2026-07-21
fetched: 2026-10-21
---

# SHACL 1.2 Node Expressions

> Graph expressions computing nodes dynamically.

## Contents

- Abstract
- SHACL Specifications
- 1 Introduction
  - 1.1 Terminology
  - 1.2 Document Conventions
  - 1.3 Conformance
- 2 Getting started with Node Expressions
- 3 Node Expression Syntax
  - 3.1 Constant Node Expressions
    - 3.1.1 IRI Expressions
    - 3.1.2 Literal Expressions
    - 3.1.3 Triple Term Expressions
  - 3.2 Node Expressions based on Blank Nodes
    - 3.2.1 Named Parameter Functions
    - 3.2.2 List Parameter Functions
  - 3.3 Handling of Failures
  - 3.4 The Shapes Graph
- 4 Node Expressions Library
  - 4.1 Basic Node Expressions
    - 4.1.1 Empty Expressions
    - 4.1.2 Var Expressions
    - 4.1.3 List Expressions
    - 4.1.4 Path Values Expressions
    - 4.1.5 Exists Expressions
    - 4.1.6 If Expressions
  - 4.2 List Operator Expressions
    - 4.2.1 Distinct Expressions
    - 4.2.2 Intersection Expressions
    - 4.2.3 Concat Expressions
    - 4.2.4 Remove Expressions
    - 4.2.5 Filter Shape Expressions
    - 4.2.6 Limit Expressions
    - 4.2.7 Offset Expressions
    - 4.2.8 OrderBy Expressions
  - 4.3 Advanced Sequence Operations
    - 4.3.1 FlatMap Expressions
    - 4.3.2 FindFirst Expressions
    - 4.3.3 MatchAll Expressions
  - 4.4 Aggregation Expressions
    - 4.4.1 Count Expressions
    - 4.4.2 Min Expressions
    - 4.4.3 Max Expressions
    - 4.4.4 Sum Expressions
  - 4.5 Miscellaneous Node Expressions
    - 4.5.1 InstancesOf Expressions
    - 4.5.2 Nodes Matching Expressions
    - 4.5.3 ConformsToShape Expressions
- 5 SPARQL Functions
- 6 Custom Node Expressions
  - 6.1 Custom Named Parameter Functions
  - 6.2 Custom List Parameter Functions
  - 6.3 Arg Expressions
- 7 Constraint Components
  - 7.1 sh:expression
  - 7.2 sh:nodeByExpression
- 8 Dynamic SHACL
  - 8.1 Example: Dynamic Minimum Age of Presidents
  - 8.2 Example: Dynamic Enumerations
- 9 Security and Privacy Considerations
- B Index
  - B.1 Terms defined by this specification
  - B.2 Terms defined by reference
- D References
  - D.1 Normative references

---

## Abstract

This document defines SHACL 1.2 Node Expressions.

SHACL, the Shapes Constraint Language, is a language for describing the structure of RDF graphs.
The Core of SHACL can be used to define classes and the properties that instances of these classes can have.
More general than classes and instances, SHACL introduces the notion of shapes
that can formally specify constraints on the structure of RDF nodes and edges.

Node Expressions extend SHACL Core primarily to dynamically derive property values
and to compute target nodes of a shape.
To implement these computations, this document defines a library of node expression functions,
including functions from the SPARQL specification, for common use cases.

## SHACL Specifications

This specification is part of the SHACL 1.2 family of specifications. See the [SHACL 1.2 Overview](https://w3c.github.io/data-shapes/shacl12-overview/) for a more detailed introduction to them.

The specifications are as follows:

**Working Drafts:**

[SHACL 1.2 Core](https://www.w3.org/TR/shacl12-core/)

defines the Core of SHACL

[SHACL 1.2 SPARQL Extensions](https://www.w3.org/TR/shacl12-sparql/)

defines SPARQL-related extensions of SHACL

[SHACL 1.2 Node Expressions](https://www.w3.org/TR/shacl12-node-expr/)

defines expressions used to derive focus nodes and value nodes in SHACL

[SHACL 1.2 Rules](https://www.w3.org/TR/shacl12-rules/)

defines SHACL's methods of rule-based inference

[SHACL 1.2 UI](https://w3c.github.io/data-shapes/shacl12-ui/)

defines SHACL's use for User Interface generation

[SHACL 1.2 Profiling](https://w3c.github.io/data-shapes/shacl12-profiling/)

defines the use of SHACL for profiling data, including SHACL data

**Working Group Note Drafts:**

[SHACL 1.2 Overview](https://w3c.github.io/data-shapes/shacl12-overview/)

overviews the set of SHACL specifications

[SHACL 1.2 Compact Syntax](https://w3c.github.io/data-shapes/shacl12-cs/)

defines an RDF syntax for expressing SHACL concepts
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Implementers can partially check their level of conformance with the above specifications by successfully passing
> the test cases of the [SHACL 1.2 test suite](https://github.com/w3c/data-shapes/tree/gh-pages/shacl12-test-suite).
> Note, however, that passing all the tests in the test suite does not imply complete conformance to the specifications.
> It only implies that the implementation conforms to the aspects tested by the test suite.

## 1. Introduction

This document specifies SHACL Node Expressions.
This section introduces the key terminology and document conventions.

### 1.1 Terminology

Basic RDF Terminology

This document uses the terms *[RDF graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph)*, *[RDF triple](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple)*, *[IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri)*, *[literal](https://www.w3.org/TR/rdf12-concepts/#dfn-literal)*, *[blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node)*, *[node](https://www.w3.org/TR/rdf12-concepts/#dfn-node)* of an RDF graph, *[datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype)*, *[RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term)*, and *[term equality](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term-equality)*, and *[subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject)*, *[predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate)*, and *[object](https://www.w3.org/TR/rdf12-concepts/#dfn-object)* of RDF triples
as defined in RDF 1.2 Concepts and Abstract Syntax [rdf12-concepts].

Basic SHACL Terminology

This document uses the terms *[focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node)*, *[value](https://www.w3.org/TR/shacl12-core/#dfn-value)*, *[value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node)*, *[constraint](https://www.w3.org/TR/shacl12-core/#dfn-constraint)*, *[constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component)*, *[parameter](https://www.w3.org/TR/shacl12-core/#dfn-parameter)*, *[mandatory parameter](https://www.w3.org/TR/shacl12-core/#dfn-mandatory-parameter)*, *[optional parameter](https://www.w3.org/TR/shacl12-core/#dfn-optional-parameter)*, *[parameter value](https://www.w3.org/TR/shacl12-core/#dfn-parameter-value)*, *[shape](https://www.w3.org/TR/shacl12-core/#dfn-shape)*, *[node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape)*, *[property shape](https://www.w3.org/TR/shacl12-core/#dfn-property-shape)*, *[SHACL property path](https://www.w3.org/TR/shacl12-core/#dfn-shacl-property-path)*, *[data graph](https://www.w3.org/TR/shacl12-core/#dfn-data-graph)*, *[shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph)*, *[target](https://www.w3.org/TR/shacl12-core/#dfn-target)*, *[validator](https://www.w3.org/TR/shacl12-core/#dfn-validators)*, *[validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result)*, *[node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression)*, *[node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function)*, *[function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name)*, *[output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes)*, *[focus graph](https://www.w3.org/TR/shacl12-core/#dfn-focus-graph)*, *[evaluation](https://www.w3.org/TR/shacl12-core/#dfn-evaluation)*, *[evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure)*, *[conforms](https://www.w3.org/TR/shacl12-core/#dfn-conform)*, *[conformance checking](https://www.w3.org/TR/shacl12-core/#dfn-conformance-checking)*, *[failure](https://www.w3.org/TR/shacl12-core/#dfn-failure)*, *[validation](https://www.w3.org/TR/shacl12-core/#dfn-validation)*, *[SHACL instance](https://www.w3.org/TR/shacl12-core/#dfn-shacl-instance)*, *[SHACL subclass](https://www.w3.org/TR/shacl12-core/#dfn-shacl-subclass)*, *[SHACL type](https://www.w3.org/TR/shacl12-core/#dfn-shacl-type)*, *[SHACL list](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list)*, *[members](https://www.w3.org/TR/shacl12-core/#dfn-members)*, *[well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed)*, *[deep copy](https://www.w3.org/TR/shacl12-core/#dfn-deep-copy)*,
as defined in the SHACL 1.2 Core specification [shacl12-core].

### 1.2 Document Conventions

Some examples in this document use Turtle [rdf12-turtle].
The reader is expected to be familiar with SHACL [shacl12-core] and SPARQL
[sparql12-query].

Within this document, the following namespace prefix bindings are used:

| Prefix    | Namespace                                     |
| --------- | --------------------------------------------- |
| `rdf:`    | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs:`   | `http://www.w3.org/2000/01/rdf-schema#`       |
| `sh:`     | `http://www.w3.org/ns/shacl#`                 |
| `shnex:`  | `http://www.w3.org/ns/shacl-node-expr#`       |
| `skos:`   | `http://www.w3.org/2004/02/skos/core#`        |
| `sparql:` | `http://www.w3.org/ns/sparql#`                |
| `xsd:`    | `http://www.w3.org/2001/XMLSchema#`           |
| `ex:`     | `http://example.com/ns#`                      |

Grey boxes such as this include syntax rules that apply to the shapes graph.

`true` denotes the RDF term `"true"^^xsd:boolean` . `false` denotes the RDF term `"false"^^xsd:boolean` .

### 1.3 Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY* and *MUST* in this document
are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all
capitals, as shown here.

This document defines the **SHACL Node Expressions** language that extends [SHACL 1.2 Core](https://www.w3.org/TR/shacl12-core/) [shacl12-core].
This specification describes conformance criteria for:

- **SHACL Node Expressions processors** as processors that support the evaluation of SHACL Node Expressions,
  in particular as part of SHACL validation

Also see the discussion of well-formedness in the [Conformance section of SHACL Core](https://www.w3.org/TR/shacl12-core/#conformance).

## 2. Getting started with Node Expressions

*This section is non-normative.*

A SHACL [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) can declare node expressions as values of various properties where dynamic computation is useful,
such as `sh:targetNode`, `sh:values`, and `sh:deactivated`.
A node expression is represented by an RDF node and can be evaluated to produce a list of [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes).
For example, when used at `sh:targetNode`, a node expression produces the list
of target nodes of a [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape).
When used at `sh:values`, a node expression produces the derived values for the property specified by `sh:path`.

The following example contains a node expression that states that the [target](https://www.w3.org/TR/shacl12-core/#dfn-target) nodes of
the shape `ex:EstonianCompanyShape` are the instances of `ex:Company` where
the `ex:headQuarterCountry` is `ex:Estonia`.
> **Example:**
>
> Example 1: A node expression used to compute the target nodes of a shape.
>
> ex:EstonianCompanyShape
> a sh:NodeShape ;
> sh:targetNode **[
> shnex:nodes [
> shnex:instancesOf ex:Company ;
> ] ;
> shnex:filterShape [
> sh:property [
> sh:path ex:headQuarterCountry ;
> sh:hasValue ex:Estonia ;
> ]
> ]
> ]** .

The following diagram illustrates how this node expression is interpreted, from a logical point of view.
During validation, a SHACL processor will determine the [target](https://www.w3.org/TR/shacl12-core/#dfn-target) nodes of the shape
by evaluating the filter shape expression.
However, the filter shape expression first evaluates its input expression, which is specified via `sh:nodes` and is an instancesOf expression.
This will produce all instances of the given class, `ex:Company`.
The `shnex:filterShape` is then applied to all of these instances, to keep only the companies
that [conform](https://www.w3.org/TR/shacl12-core/#dfn-conform) to the provided [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape), by having their headquarters in Estonia.

![Illustration of the data flow between node expressions](https://www.w3.org/TR/shacl12-node-expr/images/FilterShapeExampleDiagram.png)

The scenario above can also be expressed using SPARQL *[select expressions](https://www.w3.org/TR/shacl12-sparql/#SelectExpression)*.
For performance reasons, for example, specific implementations of SHACL node expressions might
internally convert node expressions such as the `shnex:filterShape` above to SPARQL.
> **Example:**
>
> Example 2: A SPARQL select expression used to compute the target nodes of a shape.
>
> ex:EstonianCompanyShape
> a sh:NodeShape ;
> sh:targetNode **[
> sh:select """
> SELECT ?company
> WHERE {
> ?company rdf:type/rdfs:subClassOf* ex:Company .
> ?company ex:headQuarterCountry ex:Estonia .
> }
> """
> ]** .

The next example uses a node expression to compute the values of the property `ex:employeeCount` as the number of values of the property `ex:employee` at each instance of `ex:Company`.
> **Example:**
>
> Example 3: A node expression used to compute the values of a derived property.
>
> ex:Company
> a sh:ShapeClass ;
> sh:property ex:Company-employee ;
> sh:property ex:Company-employeeCount .
>
> ex:Company-employee
> a sh:PropertyShape ;
> sh:name "employees" ;
> sh:description "The company's employee(s)." ;
> sh:path ex:employee ;
> sh:class ex:Person .
>
> ex:Company-employeeCount
> a sh:PropertyShape ;
> sh:name "employee count" ;
> sh:description "The number of employees, automatically computed." ;
> sh:path ex:employeeCount ;
> sh:datatype xsd:integer ;
> sh:values **[
> shnex:count [
> shnex:pathValues ex:employee ;
> ]
> ]** .

![Illustration of the data flow between node expressions computing the employee count](https://www.w3.org/TR/shacl12-node-expr/images/CountExampleDiagram.png)

One difference between this example and the previous examples about `sh:targetNode` is that these node expressions are evaluated against a given [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node).
This means that when a data visualization needs to render an instance of `ex:Company`,
the currently displayed company is the [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node), for which the number of employees
will be fetched.

Note that derived properties, such as `ex:employeeCount` from the example above,
do not lead to the creation of triples in the [data graph](https://www.w3.org/TR/shacl12-core/#dfn-data-graph) or [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph).
Tools that use these `sh:values` expressions typically compute the values only on
demand; for example, whenever an instance of `ex:Company` is displayed or queried.

## 3. Node Expression Syntax

This section introduces the general syntax of SHACL [node expressions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression).

The term [node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) refers to the *kind* or *type* of a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression).
For example, `sh:FilterShapeExpression` is a [node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function),
while a specific instance of this function in the [graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph) is the [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) itself.

The most basic node expression functions are constant node expressions, which are either [literals](https://www.w3.org/TR/rdf12-concepts/#dfn-literal), [IRIs](https://www.w3.org/TR/rdf12-concepts/#dfn-iri), or [triple terms](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term), and simply evaluate to these constants.
All other node expressions are represented by [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node), and come in the following two variations:

- A named parameter function is represented by a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the subject of one or more
  triples, including the key parameter of the node expression function.
- A list parameter function is comparable to a traditional function in SPARQL, for example,
  and is represented by a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the subject of a single triple with a SHACL list as its object.

### 3.1 Constant Node Expressions

The [node expression functions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) in this section are called *constant node expressions*.
Two of them were already introduced in the SHACL Core specification and are repeated here to keep this document self-contained.

#### 3.1.1 IRI Expressions

A [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) is called an *IRI expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `sh:IRIExpression`.

A node in an RDF graph is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) IRI expression if it is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri).

EVALUATION OF IRI EXPRESSIONS

The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of an IRI expression are the list consisting of exactly the [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) itself:

`evalExpr(expr, focusGraph, focusNode, scope) -> [expr]`

#### 3.1.2 Literal Expressions

A [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-literal) is called a *literal expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `sh:LiteralExpression`.

A node in an RDF graph is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) literal expression if it is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-literal).

EVALUATION OF LITERAL EXPRESSIONS

The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of a literal expression are the list consisting of exactly the [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) itself:

`evalExpr(expr, focusGraph, focusNode, scope) -> [expr]`

#### 3.1.3 Triple Term Expressions

A [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that is a [triple term](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term) is called a *triple term expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `sh:TripleTermExpression`.

A node in an RDF graph is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) triple term expression if it is a [triple term](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term).

EVALUATION OF TRIPLE TERM EXPRESSIONS

The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of a triple term expression are the list consisting of exactly the [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) itself:

`evalExpr(expr, focusGraph, focusNode, scope) -> [expr]`

### 3.2 Node Expressions based on Blank Nodes

#### 3.2.1 Named Parameter Functions

A *named parameter function* is a [node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) that is represented by a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of at least
one [triple](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple) where the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) can be used to uniquely identify the function,
which is known as the *key parameter*.

The evaluation of a named parameter function can produce any of the following:

- zero [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes),
  i.e., an empty list
- one or more [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes),
  i.e., a list of one or more nodes
- an [evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure),
  i.e., an (unexpected) error during the evaluation

For example, the named parameter function `shnex:FilterShapeExpression` (§4.2.5) has `shnex:filterShape` as its key parameter.
In this document, key parameters are marked in **bold face**.

Expressions based on named parameter functions often
take other [node expressions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) as arguments,
evaluate those input node expressions,
and then produce a different list of [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) as [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes).

*The remainder of this section is non-normative.*

This document includes many examples of named parameter functions, such as
the Estonian Company Shape example.

#### 3.2.2 List Parameter Functions

A *list parameter function* is a [node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) that is represented by a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of a single [triple](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple) where the [object](https://www.w3.org/TR/rdf12-concepts/#dfn-object) `o` is conforming to one of the following syntax rules, in order:

1. If `o` is the empty [SHACL list](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list) `rdf:nil` (written as `()` in Turtle)
   then the arguments are the empty list.
   Example: `[ sparql:now () ]`
2. If `o` is a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [SHACL list](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list) where all [members](https://www.w3.org/TR/shacl12-core/#dfn-members) are [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expressions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression),
   then the arguments are the [members](https://www.w3.org/TR/shacl12-core/#dfn-members) of that list.
   Examples: `[ sparql:plus ( 38 4 ) ]` and `[ sparql:abs ( -42 ) ]`
3. If the function call has one argument,
   and the argument is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression),
   then the argument can be given without the list.
   It is equivalent to a function call with a list of one element.
   Example: `[ sparql:abs -42 ]`, which is equivalent to `[ sparql:abs ( -42 ) ]`.

The [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) of this [triple](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple) is called the *list parameter property*.

The [evaluation](https://www.w3.org/TR/shacl12-core/#dfn-evaluation) of a list parameter function can produce any of the following:

- one [output node](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes), i.e., a list of one [node](https://www.w3.org/TR/rdf12-concepts/#dfn-node)
- zero [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes), i.e., an empty list
- an [evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure), i.e., an (unexpected) error during the evaluation

Furthermore, each argument of a list parameter function must evaluate to an individual, single [node](https://www.w3.org/TR/rdf12-concepts/#dfn-node),
not to a list of nodes.
If an argument is a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression), then this [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) must evaluate to
a maximum of one [output node](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes).
An [evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure) must be produced if there is more than one [output node](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes).
This is different from named parameter functions, where arguments may produce lists of multiple nodes.

*The remainder of this section is non-normative.*

Note that some named parameter functions — such as `shnex:IntersectionExpression` —
also use a [SHACL list](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list) as an object of the key parameter, similar to list parameter functions which always have a [SHACL list](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list) as the object of their list parameter property.
However, these may produce more than one [output node](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes), and also accept lists as input nodes.

The following example uses two list parameter functions —
the (hypothetical) `ex:coalesce` and the SPARQL-based `sparql:concat` —
to compute the `ex:displayName` of a person either as the value of `ex:fullName` or (if that doesn't exist)
as a concatenation of `ex:firstName`, a space, and `ex:lastName`.
> **Example:**
>
> Example 4: A complex node expression based on list parameter functions.
>
> ex:Person-displayName
> a sh:PropertyShape ;
> sh:name "display name" ;
> sh:path ex:displayName ;
> sh:datatype xsd:string ;
> sh:values **[
> ex:coalesce (
> [
> # This is a path values expression that is expected to return zero or one values
> shnex:pathValues ex:fullName ;
> ]
> [
> sparql:concat (
> [ shnex:pathValues ex:firstName ] # Path values expression with at most one value
> " " # A constant literal expression
> [ shnex:pathValues ex:lastName ] # Path values expression with at most one value
> )
> ]
> )
> ]** .

### 3.3 Handling of Failures

Node expressions may produce a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) instead of a list of [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes).
Some node expressions evaluate other, nested node expressions.
For example, §4.1.6 If Expressions evaluate nested expressions for `shnex:if`, `shnex:then` and `shnex:else`.
In general, if any such nested expressions produce a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) then the surrounding
expression also produces the same [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure).

*The remainder of this section is non-normative.*

Note that this policy impacts the evaluation order of node expressions.
For example, `shnex:if` expressions are evaluated first and `shnex:then` will be evaluated only if the `shnex:if` has returned `( true )`.
Even if the `shnex:else` branch would produce a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure), the output would
still only be the output nodes of the `shnex:then` branch.

### 3.4 The Shapes Graph

Some node expression functions — such as 4.2.5 Filter Shape Expressions (§4.2.5) and 4.5.3 ConformsToShape Expressions (§4.5.3) —
perform SHACL [validation](https://www.w3.org/TR/shacl12-core/#dfn-validation) to determine whether a [node](https://www.w3.org/TR/rdf12-concepts/#dfn-node) [conforms](https://www.w3.org/TR/shacl12-core/#dfn-conform) to a [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape).
The [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) used for this [validation](https://www.w3.org/TR/shacl12-core/#dfn-validation) is not explicitly stated for each function.
Instead, it is derived from the context:

1. When a node expression is evaluated as part of another SHACL process
   (e.g., computing value nodes using `sh:values` or target nodes using `sh:targetNode`),
   the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) is reused from the surrounding SHACL process.
2. Otherwise, the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) may be passed into the node expression evaluation process as a parameter.
3. In the absence of such a parameter, the [focus graph](https://www.w3.org/TR/shacl12-core/#dfn-focus-graph) is used as the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph).

## 4. Node Expressions Library

This section defines all [node expression functions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) that are built into SHACL engines
that implement this specification.

The syntax definitions of node expression functions that are based on [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) typically use a table of properties that these blank nodes can or must have.
Such blank nodes are only [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) when they are not the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of any other
triples, and when none of these properties is used more than once.
The tables may also list SHACL constraints with which the property values are required to conform.
In the tables, mandatory properties are rendered in **bold face**.

### 4.1 Basic Node Expressions

#### 4.1.1 Empty Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is not the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of any triple is called an *empty expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:EmptyExpression`.

EVALUATION OF EMPTY EXPRESSIONS

An empty expression has the empty list `[]` as its [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes).

*The remainder of this section is non-normative.*

This node expression function is written in Turtle as `[]` and must not be confused with
the empty SHACL list `()` which is the [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) `rdf:nil`.

#### 4.1.2 Var Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *var expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:VarExpression`:

| Property        | Constraints                             | Description                            |
| --------------- | --------------------------------------- | -------------------------------------- |
| **`shnex:var`** | `sh:datatype xsd:string sh:minLength 1` | The variable name, e.g. `"focusNode"`. |

EVALUATION OF VAR EXPRESSIONS

Let `var` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:var` in the var expression.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the var expression are computed as follows, in order:

1. if `var` is `"focusNode"` then `evalExpr(expr, focusGraph, focusNode, scope) -> [focusNode]`
2. if `var` is in the `scope` then `evalExpr(expr, focusGraph, focusNode, scope) -> [ scope[var] ]`
3. otherwise `evalExpr(expr, focusGraph, focusNode, scope) -> []`

*The remainder of this section is non-normative.*

The following example illustrates the use of a var expression pointing at the current [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node) to state that the default value of the `ex:loves` relationship is the current instance of `ex:Person`,
creating a self-reference.
> **Example:**
>
> Example 5: A var expression stating that any Person loves him or herself by default.
>
> ex:Person
> a sh:ShapeClass ;
> sh:property ex:Person-loves .
>
> ex:Person-loves
> a sh:PropertyShape ;
> sh:path ex:loves ;
> sh:defaultValue **[ shnex:var "focusNode" ] .**

#### 4.1.3 List Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *list expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:ListExpression`:

| Property        | Constraints                                                                                                                                                                                              | Description                            |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **`rdf:first`** | *MUST* be a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-literal) or an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri).                                                                     | The first member of the list.          |
| **`rdf:rest`**  | Must be a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [SHACL list](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list), where each [member](https://www.w3.org/TR/shacl12-core/#dfn-members) is either a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-literal) or an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri). | The rest of the list, e.g., `rdf:nil`. |

EVALUATION OF LIST EXPRESSIONS

The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of a list expression are the [members](https://www.w3.org/TR/shacl12-core/#dfn-members) of the list expression,
in the same order as in the list.

*The remainder of this section is non-normative.*

Note that `rdf:nil` itself is not a list expression because it will be interpreted
as a IRI expression.
As a result, all [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) list expressions have at least one [member](https://www.w3.org/TR/shacl12-core/#dfn-members).

The following example declares a property for instances of `rdfs:Class` where the values are derived from the values of the path `rdfs:subClassOf*` but with the constants from the list `( owl:Thing rdfs:Resource )` removed using `shnex:remove` (§4.2.4).
> **Example:**
>
> Example 6: A list expression that is used to enumerate the values of a shnex:remove expression.
>
> ex:ClassShape
> a sh:NodeShape ;
> sh:targetClass rdfs:Class ;
> sh:property ex:ClassShape-superClassesExceptRoots .
>
> ex:ClassShape-superClassesExceptRoots
> a sh:PropertyShape ;
> sh:path ex:superClassesExceptRoots ;
> sh:description "The superclasses of this, except for owl:Thing and rdfs:Resource." ;
> sh:values [
> shnex:nodes [
> # This returns all transitive superclasses of the current focus node
> shnex:pathValues [ sh:zeroOrMorePath rdfs:subClassOf ] ;
> ] ;
> # This removes any superclasses that are in the list below
> shnex:remove **( owl:Thing rdfs:Resource )** ;
> ] .

#### 4.1.4 Path Values Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *path values expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:PathValuesExpression`:

| Property               | Constraints                                                                                                                                                        | Description                                                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`shnex:pathValues`** | Must be a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [SHACL property path](https://www.w3.org/TR/shacl12-core/#dfn-shacl-property-path).   | The path to get the values from.                                                                                                                                    |
| `shnex:focusNode`      | Optional, must be a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | A node expression producing the [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node), defaulting to the current focus node from the evaluation context. |

EVALUATION OF PATH VALUES EXPRESSIONS

Let `$pathValues` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:pathValues`,
and `$focusNode` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:focusNode` in a path values expression.
If `shnex:focusNode` is not given, `$focusNode` is the list consisting of exactly the [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node) from the evaluation context.

Let `N` be the nodes produced by `evalExpr($focusNode, focusGraph, focusNode, scope)`.
If `N` has 0 members, then the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) are the empty list.
If `N` has more than 1 member, an [evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure) is reported.
Otherwise, the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the path values expression are the list of [value nodes](https://www.w3.org/TR/shacl12-core/#dfn-value-node) of the `path` for the (only) member of `N`.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> **Important:** Note the distinction between `sh:path` and `shnex:pathValues`:
>
> - `sh:path` is used in **property shapes** to specify the property path that will be constrained during validation. It defines the property or path to which the shape's constraints apply.
> - `shnex:pathValues` is used in **node expressions** to specify the property path that will be traversed to generate a sequence of values. It produces the actual values found by following the path.
> For example, `sh:path ex:name` in a property shape constrains the values of the `ex:name` property, while `shnex:pathValues ex:name` in a node expression generates a sequence containing all values of the `ex:name` property.

*The remainder of this section is non-normative.*

Note that by definition, the [value nodes](https://www.w3.org/TR/shacl12-core/#dfn-value-node) of a property shape may be derived properties,
based on `sh:values` or `sh:defaultValue` expressions.
This means that if the provided `shnex:pathValues` path is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri), then a path values expression
may cause the evaluation of other node expressions, as a simple kind of rule chaining.

The following example illustrates the use of a path values expression to compute the value
of the property `ex:topConceptCount`.
The expression returns the values of `skos:hasTopConcept` for the current `skos:ConceptScheme` and these values are processed by the `shnex:count` (§4.4.1) to return the
number of top concepts.
> **Example:**
>
> Example 7: A path values expression computing the number of top concepts in a scheme
>
> skos:ConceptScheme
> a sh:ShapeClass ;
> sh:property skos:ConceptScheme-topConceptCount .
>
> skos:ConceptScheme-topConceptCount
> a sh:PropertyShape ;
> sh:path ex:topConceptCount ;
> sh:datatype xsd:integer ;
> sh:description "The number of top concepts in this scheme." ;
> sh:maxCount 1 ;
> sh:name "top concept count" ;
> sh:values [
> shnex:count **[
> shnex:pathValues skos:hasTopConcept ;
> ]** ;
> ] .

The next example illustrates the use of a path values expression together with a specific focus node
(instead of the default focus node provided by the evaluation context).
The shape targets all [subjects](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) that have `skos:Concept` as their `rdf:type` with a dynamically computed `sh:targetNode` expression.
In other words, the target nodes are the direct instances of `skos:Concept` based on asserted `rdf:type` triples, not including the subclasses of `skos:Concept`.
> **Example:**
>
> Example 8: A shape that targets the direct instances of skos:Concept, using a path values expression
>
> ex:DirectInstancesOfConceptShape
> a sh:NodeShape ;
> sh:targetNode **[
> shnex:pathValues [ sh:inversePath rdf:type ] ;
> shnex:focusNode skos:Concept ;
> ]** .

#### 4.1.5 Exists Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called an *exists expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:ExistsExpression`:

| Property           | Constraints                                                                                                                                      | Description                                                                                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`shnex:exists`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | A node expression. If this evaluates to a list with at least one member then the output nodes are `( true )`; otherwise, the output nodes are `( false )`. |

EVALUATION OF EXISTS EXPRESSIONS

Let `exists` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:exists` in the exists expression.
Let `N` be the list of nodes produced by `evalExpr(exists, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the exists expression are `( true )` if and only if `N` has at least one member; otherwise, the output nodes are `( false )`.

*The remainder of this section is non-normative.*

The Example for `shnex:if` uses `shnex:exists`.

#### 4.1.6 If Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called an *if expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:IfExpression`:

| Property       | Constraints                                                                                                                                                                                              | Description                                                                                                                                                                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`shnex:if`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression).                                                         | A node expression. The `shnex:then` branch is returned when the `shnex:if` expression returns `true` as its only [output node](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes), in all other cases `shnex:else`. |
| `shnex:then`   | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). Optional but at least one of `shnex:then` or `shnex:else` is required. | The [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that is returned when the `shnex:if` evaluated to `[true]`.                                                               |
| `shnex:else`   | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). Optional but at least one of `shnex:then` or `shnex:else` is required. | The [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that is returned when the `shnex:if` did not evaluate to `[true]`.                                                        |

EVALUATION OF IF EXPRESSIONS

Let `if` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:if`, `then` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:then`, and `else` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:else` for the if expression.
Let `IFs` be the nodes produced by `evalExpr(if, focusGraph, focusNode, scope)`.
If `IFs` is the list `( true )`, then the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the if expression are the nodes produced by `evalExpr(then, focusGraph, focusNode, scope)`, or the empty list if `then` has no value.
Otherwise, the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) are the nodes produced by `evalExpr(else, focusGraph, focusNode, scope)`, or the empty list if `else` has no value.
Implementations *MUST* apply lazy evaluation techniques, so the `shnex:then` or `shnex:else` branches are only evaluated when necessary.

*The remainder of this section is non-normative.*

The following example illustrates the use of `shnex:if` to compute the
values of a derived property `ex:fillColor` that may be queried to
compute the colors of cities on a map.
In the example, instances of `ex:City` that have a value for `ex:capitalOf` will be displayed in `"blue"`, while the others will be `"red"`.
> **Example:**
>
> Example 9: An example "if" expression computing the fill color of a city
>
> ex:City
> a sh:ShapeClass ;
> sh:property ex:City-fillColor .
>
> ex:City-fillColor
> a sh:PropertyShape ;
> sh:path ex:fillColor ;
> sh:datatype xsd:string ;
> sh:name "fill color" ;
> sh:values **[
> shnex:if [
> shnex:exists [
> shnex:pathValues ex:capitalOf ;
> ] ;
> ] ;
> shnex:then "blue" ;
> shnex:else "red" ;
> ]** .

### 4.2 List Operator Expressions

#### 4.2.1 Distinct Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *distinct expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:DistinctExpression`:

| Property             | Constraints                                                                                                                                      | Description                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| **`shnex:distinct`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The node expression that shall be reduced to its distinct members. |

EVALUATION OF DISTINCT EXPRESSIONS

Let `distinct` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:distinct` in the distinct expression.
Let `input` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(distinct, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the distinct expression are the list of [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) in `input` in the same order but with duplicates eliminated (the first occurences of each node shall be kept, the others removed).
Nodes are compared using [term equality](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term-equality), i.e. `"01"^^xsd:integer` is distinct from `"1"^^xsd:integer`.

*The remainder of this section is non-normative.*

The following example declares a derived property `ex:superClassesIncludingRoot` that is computed as the concat (§4.2.3) of the (transitive) values of `rdfs:subClassOf` and the list expression (§4.1.3) `( rdfs:Resource )`.
Since the asserted values of `rdfs:subClassOf` may already include `rdfs:Resource` (for example, due to an active inference engine on the data graph), `shnex:distinct` will make
sure that the output nodes do not include `rdfs:Resource` twice.
> **Example:**
>
> Example 10: Using shnex:distinct to return a list of superclasses including rdfs:Resource but not including duplicates
>
> ex:ClassShape
> a sh:NodeShape ;
> sh:targetClass rdfs:Class ;
> sh:property ex:ClassShape-superClassesIncludingRoot .
>
> ex:ClassShape-superClassesIncludingRoot
> a sh:PropertyShape ;
> sh:path ex:superClassesIncludingRoot ;
> sh:description "The superclasses of this, always including rdfs:Resource." ;
> sh:values **[
> shnex:distinct [
> shnex:concat (
> [
> shnex:pathValues [ sh:zeroOrMorePath rdfs:subClassOf ] ;
> ]
> ( rdfs:Resource )
> )
> ]** ;
> ] .

#### 4.2.2 Intersection Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called an *intersection expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:IntersectionExpression`:

| Property                 | Constraints                                                                                                                                                                                              | Description                                     |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **`shnex:intersection`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [SHACL list](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list) where each [member](https://www.w3.org/TR/shacl12-core/#dfn-members) is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The node expressions that shall be intersected. |

EVALUATION OF INTERSECTION EXPRESSIONS

Let `members` be the [members](https://www.w3.org/TR/shacl12-core/#dfn-members) of the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:intersection` in the intersection expression.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the intersection expression are the [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) that form the intersection of the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) produced by each [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) `NE` in `members`, using `evalExpr(NE, focusGraph, focusNode, scope)`.
Nodes must be equal using [term equality](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term-equality), e.g., `"01"^^xsd:integer` is distinct from `"1"^^xsd:integer`.
The intersection does not include duplicates and the order is undefined.

*The remainder of this section is non-normative.*

The following example uses `shnex:intersection` as a `sh:targetNode` node expression.
This shape will target all nodes that are [SHACL instances](https://www.w3.org/TR/shacl12-core/#dfn-shacl-instance) of `ex:Australian` and `ex:German` at the same time.
> **Example:**
>
> Example 11: Using shnex:intersection to compute the target nodes of a shape
>
> ex:DualCitizenShape
> a sh:NodeShape ;
> sh:targetNode **[
> shnex:intersection (
> [ shnex:instancesOf ex:Australian ]
> [ shnex:instancesOf ex:German ]
> )
> ]** .
>
> **Evaluation trace:**
>
> The evaluation proceeds as follows:
>
> 1. `shnex:instancesOf ex:Australian` produces: `[ex:Person1, ex:Person2, ex:Person3, ex:Person4]`
> 2. `shnex:instancesOf ex:German` produces: `[ex:Person2, ex:Person4, ex:Person5]`
> 3. Compute the intersection (nodes appearing in both lists): `[ex:Person2, ex:Person4]`
> More abstractly, the intersection of `[1, 2, 3, 4]` and `[2, 4, 5]` results in `[2, 4]`,
> containing only the elements that appear in both lists.

#### 4.2.3 Concat Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *concat expression*, with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:ConcatExpression`:

| Property           | Constraints                                                                                                                                                                                              | Description                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **`shnex:concat`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [SHACL list](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list) where each [member](https://www.w3.org/TR/shacl12-core/#dfn-members) is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The node expressions that shall be concatenated. |

EVALUATION OF CONCAT EXPRESSIONS

Let `members` be the [members](https://www.w3.org/TR/shacl12-core/#dfn-members) of the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:concat` in the concat expression.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the concat expression are the concatenation of all [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) for each [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) `NE` in `members`, using `evalExpr(NE, focusGraph, focusNode, scope)`.
The order is preserved, evaluating the `members` from left to right and keeping the order of each list of output nodes.

*The remainder of this section is non-normative.*

Note that a concat expression may produce duplicate [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) if the individual output nodes overlap.
Use shnex:distinct (§4.2.1) to eliminate duplicates.

The following example declares a derived property `ex:allRelatives` that concatenates the values of `ex:parent` and `ex:sibling`.
The `shnex:concat` expression takes a list of node expressions and returns
all nodes from each expression in sequence from left to right.
> **Example:**
>
> Example 12: Using shnex:concat to combine results from multiple node expressions
>
> ex:PersonShape
> a sh:NodeShape ;
> sh:targetClass ex:Person ;
> sh:property ex:PersonShape-allRelatives .
>
> ex:PersonShape-allRelatives
> a sh:PropertyShape ;
> sh:path ex:allRelatives ;
> sh:class ex:Person ;
> sh:name "all relatives" ;
> sh:values **[
> shnex:concat (
> [ shnex:pathValues ex:parent ]
> [ shnex:pathValues ex:sibling ]
> )
> ]** .
>
> **Evaluation trace:**
>
> The evaluation proceeds as follows:
>
> 1. `shnex:pathValues ex:parent` with focus node `ex:Person1` produces: `[ex:Parent1, ex:Parent2]`
> 2. `shnex:pathValues ex:sibling` with focus node `ex:Person1` produces: `[ex:Sibling1, ex:Sibling2, ex:Sibling3]`
> 3. Concatenate the results in order: `[ex:Parent1, ex:Parent2, ex:Sibling1, ex:Sibling2, ex:Sibling3]`
> More abstractly, concatenating `[1, 2]` and `[3, 4, 5]` results in `[1, 2, 3, 4, 5]` with all elements preserved in order from left to right.

#### 4.2.4 Remove Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *remove expression*, with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:RemoveExpression`:

| Property           | Constraints                                                                                                                                      | Description                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| **`shnex:remove`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The nodes that shall be removed from the `shnex:nodes`. |
| **`shnex:nodes`**  | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes.                                        |

EVALUATION OF REMOVE EXPRESSIONS

Let `remove` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:remove` and `nodes` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:nodes` in the remove expression.
Let `M` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(remove, focusGraph, focusNode, scope)`.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(nodes, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the remove expression are the [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) in `N` except those that are also in `M`, preserving the order of `N`.
Nodes must be equal using [term equality](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term-equality), i.e., `"01"^^xsd:integer` is distinct from `"1"^^xsd:integer`.

*The remainder of this section is non-normative.*

The following example declares a derived property, `ex:availableAuthors`,
that returns all persons who are authors, except those who are currently on leave.
The `shnex:remove` expression takes the nodes from `shnex:nodes` (all authors)
and removes the nodes returned by the `shnex:remove` expression (authors on leave).
> **Example:**
>
> Example 13: Using shnex:remove to exclude unavailable authors from a list
>
> ex:PublisherShape
> a sh:NodeShape ;
> sh:targetClass ex:Publisher ;
> sh:property ex:PublisherShape-availableAuthors .
>
> ex:PublisherShape-availableAuthors
> a sh:PropertyShape ;
> sh:path ex:availableAuthors ;
> sh:class ex:Person ;
> sh:description "Authors who are currently available (not on leave)." ;
> sh:values **[
> shnex:nodes [ shnex:pathValues ex:author ] ;
> shnex:remove [ shnex:pathValues ex:authorOnLeave ] ;
> ]** .
>
> **Evaluation trace:**
>
> The evaluation proceeds as follows:
>
> 1. `shnex:nodes [shnex:pathValues ex:author]` with focus node `ex:PublisherA` produces: `[ex:Author1, ex:Author1, ex:Author1, ex:Author2, ex:Author2]`
> 2. `shnex:remove [shnex:pathValues ex:authorOnLeave]` with focus node `ex:PublisherA` produces: `[ex:Author1, ex:Author1]`
> 3. Remove all occurrences of `ex:Author1` from the nodes list, preserving order: `[ex:Author2, ex:Author2]`
> More abstractly, removing `[1, 1]` from `[1, 1, 1, 2, 2]` results in `[2, 2]` because all instances of `1` are removed (not just the first occurrence).

#### 4.2.5 Filter Shape Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *filter shape expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:FilterShapeExpression`:

| Property                | Constraints                                                                                                                                      | Description                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| **`shnex:filterShape`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape).                     | The shape that all input nodes need to conform to.        |
| **`shnex:nodes`**       | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | A node expression producing the nodes that are validated. |

EVALUATION OF FILTER SHAPE EXPRESSIONS

Let `filterShape` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:filterShape`,
and `nodes` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:nodes` in a filter shape expression.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the filter shape expression are the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(nodes, focusGraph, focusNode, scope)` except those that do not [conform](https://www.w3.org/TR/shacl12-core/#dfn-conform) to
the [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) `filterShape`, preserving the order in the list.

*The remainder of this section is non-normative.*

The following example illustrates the use of `shnex:filterShape` to return a subset
of values of the `ex:child` property where the `ex:gender` property
has the value `"male"`.
> **Example:**
>
> Example 14: Using shnex:filterShape to compute the children that are male
>
> ex:Person
> a sh:ShapeClass ;
> sh:property ex:Person-maleChildren .
>
> ex:Person-maleChildren
> a sh:PropertyShape ;
> sh:path ex:maleChildren ;
> sh:class ex:Person ;
> sh:values **[
> shnex:nodes [
> shnex:pathValues ex:child ;
> ] ;
> shnex:filterShape [
> sh:property [
> sh:path ex:gender ;
> sh:hasValue "male" ;
> ]
> ] ;
> ]** .

#### 4.2.6 Limit Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *limit expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:LimitExpression`:

| Property          | Constraints                                                                                                                                      | Description                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| **`shnex:limit`** | `sh:datatype xsd:integer sh:minInclusive 0`                                                                                                      | The maximum number of nodes that shall be returned. |
| **`shnex:nodes`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes.                                    |

EVALUATION OF LIMIT EXPRESSIONS

Let `limit` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:limit` and `nodes` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:nodes` in the limit expression.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(nodes, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the limit expression are the first `limit` [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) in `N` from left to right, in the same order.

*The remainder of this section is non-normative.*

The following example illustrates the use of `shnex:limit` to compute the
values of a derived property `ex:oldestChildren` to be a sub-list of
values of `ex:child` at the current [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node) (which is an instance of
the class `ex:Person`).
The values are computed by first fetching the values of `ex:child`, then
ordering them by their `ex:dateOfBirth`, and finally getting only `2` of these children at most.
> **Example:**
>
> Example 15: Using shnex:limit and shnex:orderBy to compute the oldest two children
>
> ex:PersonShape
> a sh:NodeShape ;
> sh:targetClass ex:Person ;
> sh:property ex:PersonShape-oldestTwoChildren .
>
> ex:PersonShape-oldestTwoChildren
> a sh:PropertyShape ;
> sh:path ex:oldestTwoChildren ;
> sh:class ex:Person ;
> sh:values **[
> shnex:nodes [
> shnex:nodes [
> shnex:pathValues ex:child ;
> ] ;
> shnex:orderBy [
> shnex:pathValues ex:dateOfBirth ;
> ] ;
> ] ;
> shnex:limit 2 ;
> ]** .

#### 4.2.7 Offset Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called an *offset expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:OffsetExpression`:

| Property           | Constraints                                                                                                                                      | Description                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| **`shnex:offset`** | `sh:datatype xsd:integer sh:minInclusive 0`                                                                                                      | The number of nodes that shall be skipped from the `shnex:nodes`. |
| **`shnex:nodes`**  | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes.                                                  |

EVALUATION OF OFFSET EXPRESSIONS

Let `offset` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:offset` and `nodes` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:nodes` in the offset expression.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(nodes, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the offset expression are the [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) in `N` except for the first `offset` nodes from left to right, in the same order.

*The remainder of this section is non-normative.*

The following example illustrates the use of `shnex:offset` to compute the
values of a derived property `ex:remainingChildren` to be a sub-list of
values of `ex:child` at the current [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node) (which is an instance of
the class `ex:Person`).
The values are computed by first fetching the values of `ex:child`, then
ordering them by their `ex:dateOfBirth`, and finally skipping the first
of these children.
> **Example:**
>
> Example 16: Using shnex:offset to compute all but the oldest child
>
> ex:PersonShape
> a sh:NodeShape ;
> sh:targetClass ex:Person ;
> sh:property ex:PersonShape-remainingChildren .
>
> ex:PersonShape-remainingChildren
> a sh:PropertyShape ;
> sh:path ex:remainingChildren ;
> sh:class ex:Person ;
> sh:values **[
> shnex:nodes [
> shnex:nodes [
> shnex:pathValues ex:child ;
> ] ;
> shnex:orderBy [
> shnex:pathValues ex:dateOfBirth ;
> ] ;
> ] ;
> shnex:offset 1 ;
> ]** .

#### 4.2.8 OrderBy Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called an *order by expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:OrderByExpression`:

| Property            | Constraints                                                                                                                                      | Description                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **`shnex:nodes`**   | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes.                                         |
| **`shnex:orderBy`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The node expression that is applied to each input node.  |
| `shnex:desc`        | `sh:datatype xsd:boolean`                                                                                                                        | `true` to produce descending order, defaults to `false`. |

EVALUATION OF ORDER BY EXPRESSIONS

Let `orderBy` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:orderBy`, `nodes` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:nodes` and `desc` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:desc` in the order by expression.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(nodes, focusGraph, focusNode, scope)`.
Let `c(n)` be the first output node of `evalExpr(orderBy, focusGraph, n, scope)` for each `n` in `N`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the order by expression are the [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) in `N` sorted by `c(n)` using the same logic as *[SPARQL ORDER BY](https://www.w3.org/TR/sparql12-query/#modOrderBy)*.
Nodes where `c(n)` is unbound are considered smaller than those that have any value.
If `desc` is `true` then the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) are returned in the reverse order.

*The remainder of this section is non-normative.*

The Example of `shnex:limit` also illustrates `shnex:orderBy`.

### 4.3 Advanced Sequence Operations

#### 4.3.1 FlatMap Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *flat map expression*,
with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:FlatMapExpression`:

| Property            | Constraints                                                                                                                                      | Description                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| **`shnex:flatMap`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that is applied to each input node. |
| **`shnex:nodes`**   | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes. If omitted, defaults to the focus node.                                                           |

EVALUATION OF FLAT MAP EXPRESSIONS

Let `flatMap` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:flatMap` and `nodes` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:nodes` in a flat map expression.
If `shnex:nodes` is not specified, let `nodes` be the focus node.

Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(nodes, focusGraph, focusNode, scope)`.

For each node `n` in `N`, let `Mn` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(flatMap, focusGraph, n, scope)`.

The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the flat map expression are produced by concatenating all sequences `Mn` in the order of the corresponding nodes `n` in `N`.

*The remainder of this section is non-normative.*

The `shnex:flatMap` operation applies an expression to each input node and flattens the results
into a single sequence. This is particularly useful when combining results from multiple path traversals
or when working with nested structures.

A key aspect of `shnex:flatMap` is that the focus node changes for each iteration.
For each node produced by the `shnex:nodes` expression, that node becomes the focus node
when evaluating the `shnex:flatMap` expression. This allows relative path expressions to work correctly
at each level of nesting. The output sequences are then concatenated in order, preserving both the order
of input nodes and the order of results within each output sequence.

Unlike operations that remove duplicates, `shnex:flatMap` preserves all results, including duplicates.
If duplicate elimination is desired, use `shnex:distinct` to post-process the results.

The following example illustrates the use of `shnex:flatMap` to derive a property `ex:allSkills` that collects all skills from all employees of a company.
For each employee of the company, the flatMap operation applies a path expression to retrieve their skills,
and flattens the resulting skill sequences into a single comprehensive list.
> **Example:**
>
> Example 17: Using shnex:flatMap to collect skills from all employees
>
> ex:CompanyShape
> a sh:NodeShape ;
> sh:targetClass ex:Company ;
> sh:property ex:CompanyShape-allSkills .
>
> ex:CompanyShape-allSkills
> a sh:PropertyShape ;
> sh:path ex:allSkills ;
> sh:name "all skills" ;
> sh:values **[
> shnex:nodes [
> shnex:pathValues ex:employee ;
> ] ;
> shnex:flatMap [
> shnex:pathValues ex:skill ;
> ] ;
> ]** .
>
> ex:CompanyA
> ex:employee ex:Employee1 ;
> ex:employee ex:Employee2 ;
> ex:employee ex:Employee3 .
>
> ex:Employee1
> ex:skill "Java"@en ;
> ex:skill "Python"@en ;
> ex:skill "SQL"@en .
>
> ex:Employee2
> ex:skill "Python"@en ;
> ex:skill "JavaScript"@en .
>
> ex:Employee3
> ex:skill "Java"@en ;
> ex:skill "DevOps"@en .
>
> **Evaluation trace:**
>
> 1. `shnex:nodes [shnex:pathValues ex:employee]` with focus node `ex:CompanyA` produces: `[ex:Employee1, ex:Employee2, ex:Employee3]`
> 2. For each employee `n`, evaluate `shnex:flatMap [shnex:pathValues ex:skill]` with focus node `n`:
>    - `ex:Employee1` → `["Java", "Python", "SQL"]`
>    - `ex:Employee2` → `["Python", "JavaScript"]`
>    - `ex:Employee3` → `["Java", "DevOps"]`
> 3. Combine all results in order: `["Java", "Python", "SQL", "Python", "JavaScript", "Java", "DevOps"]`
> 4. Optional: Refine the resulting sequence using for example:
>    - `shnex:distinct` to remove duplicates from the flattened result.
>    - `shnex:filterShape` to apply an additional shape constraint to the
>      flattened nodes.
>    - `shnex:limit` to restrict the flattened result to the first N nodes.

#### 4.3.2 FindFirst Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *find first expression*,
with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:FindFirstExpression`:

| Property              | Constraints                                                                                                                                      | Description                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **`shnex:findFirst`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape).                     | The shape that the matching node must conform to.        |
| **`shnex:nodes`**     | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes. If omitted, defaults to the focus node. |

EVALUATION OF FIND FIRST EXPRESSIONS

Let `shape` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:findFirst` and `nodes` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:nodes` in a find first expression.
If `shnex:nodes` is not specified, let `nodes` be the focus node.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(nodes, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the find first expression contain exactly the first node `n` in `N` that [conforms](https://www.w3.org/TR/shacl12-core/#dfn-conform) to the [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) `shape`,
or an empty sequence if no such node exists.

*The remainder of this section is non-normative.*

The `shnex:findFirst` operation finds the first node in a sequence that conforms to a given shape.

The following example illustrates the use of `shnex:findFirst` to derive a property `ex:seniorEmployee` that finds the first employee with more than five years of experience.
The `shnex:findFirst` operation tests each employee against a shape that validates their years of service.
> **Example:**
>
> Example 18: Using shnex:findFirst to find the first senior employee
>
> ex:CompanyShape
> a sh:NodeShape ;
> sh:targetClass ex:Company ;
> sh:property ex:CompanyShape-seniorEmployee .
>
> ex:CompanyShape-seniorEmployee
> a sh:PropertyShape ;
> sh:path ex:seniorEmployee ;
> sh:class ex:Employee ;
> sh:maxCount 1 ;
> sh:name "senior employee" ;
> sh:values **[
> shnex:nodes [
> shnex:pathValues ex:employee ;
> ] ;
> shnex:findFirst ex:SeniorEmployeeShape ;
> ]** .
>
> ex:SeniorEmployeeShape
> a sh:NodeShape ;
> sh:property [
> sh:path ex:yearsOfService ;
> sh:datatype xsd:integer ;
> sh:minInclusive 5 ;
> ] .

#### 4.3.3 MatchAll Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *match all expression*,
with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:MatchAllExpression`:

| Property             | Constraints                                                                                                                                      | Description                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **`shnex:matchAll`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape).                     | The shape that all input nodes must conform to.          |
| **`shnex:nodes`**    | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes. If omitted, defaults to the focus node. |

EVALUATION OF MATCH ALL EXPRESSIONS

Let `shape` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:matchAll` and `nodes` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:nodes` in the match all expression.
If `shnex:nodes` is not specified, let `nodes` be the focus node.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(nodes, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the match all expression are `( true )` if
every node `n` in `N` [conforms](https://www.w3.org/TR/shacl12-core/#dfn-conform) to the [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) `shape`;
otherwise the output nodes are `( false )`.

*The remainder of this section is non-normative.*

The `shnex:matchAll` operation returns `true` if all nodes in a sequence conform to a given shape, `false` otherwise.

The following example illustrates the use of `shnex:matchAll` to derive a property `ex:allEmployeesActive` that checks whether all employees of a company are currently active.
The match all operation tests each employee against a shape that validates their active status.
> **Example:**
>
> Example 19: Using shnex:matchAll to verify all employees are active
>
> ex:CompanyShape
> a sh:NodeShape ;
> sh:targetClass ex:Company ;
> sh:property ex:CompanyShape-allEmployeesActive .
>
> ex:CompanyShape-allEmployeesActive
> a sh:PropertyShape ;
> sh:path ex:allEmployeesActive ;
> sh:datatype xsd:boolean ;
> sh:maxCount 1 ;
> sh:name "all employees active" ;
> sh:values **[
> shnex:nodes [
> shnex:pathValues ex:employee ;
> ] ;
> shnex:matchAll ex:ActiveEmployeeShape ;
> ]** .
>
> ex:ActiveEmployeeShape
> a sh:NodeShape ;
> sh:property [
> sh:path ex:isActive ;
> sh:hasValue true ;
> ] .

### 4.4 Aggregation Expressions

#### 4.4.1 Count Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *count expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:CountExpression`:

| Property          | Constraints                                                                                                                                      | Description                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| **`shnex:count`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes that shall be counted. |

EVALUATION OF COUNT EXPRESSIONS

Let `count` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:count` in the count expression.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(count, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the count expression is the list consisting of exactly one `xsd:integer` [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-literal) that is computed as the length of `N`.

*The remainder of this section is non-normative.*

The following example illustrates the use of `shnex:count` to derive a property `ex:topConceptCount` as the number of values of the `skos:hasTopConcept` property in a `skos:ConceptScheme`.
> **Example:**
>
> Example 20: Using shnex:count to compute the number of values of another property
>
> skos:ConceptScheme
> a rdfs:Class, sh:NodeShape ;
> sh:property skos:ConceptScheme-topConceptCount .
>
> skos:ConceptScheme-topConceptCount
> a sh:PropertyShape ;
> sh:path ex:topConceptCount ;
> sh:datatype xsd:integer ;
> sh:description "The number of top concepts in this scheme." ;
> sh:maxCount 1 ;
> sh:name "top concept count" ;
> sh:values **[
> shnex:count [
> shnex:pathValues skos:hasTopConcept ;
> ] ;
> ]** .

#### 4.4.2 Min Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *min expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:MinExpression`:

| Property        | Constraints                                                                                                                                      | Description                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| **`shnex:min`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes from which the minimum value shall be returned. |

EVALUATION OF MIN EXPRESSIONS

Let `min` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:min` in the min expression.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(min, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the min expression is the list consisting of at most one [node](https://www.w3.org/TR/rdf12-concepts/#dfn-node) that is computed as the minimum value from `N`,
see *[SPARQL MIN](https://www.w3.org/TR/sparql12-query/#aggMin)*.

*The remainder of this section is non-normative.*

The following example illustrates the use of `shnex:min` to derive a property `ex:minStartDate` as the smallest value of the values that can be reached using the
property path `ex:exployee/ex:startDate`.
In other words, it walks through all employees of the given company and returns the earliest
date on which an employee started.
> **Example:**
>
> Example 21: Using shnex:min to compute the smallest value in a property path
>
> ex:CompanyShape
> a sh:NodeShape ;
> sh:targetClass ex:Company ;
> sh:property ex:CompanyShape-minStartDate .
>
> ex:CompanyShape-minStartDate
> a sh:PropertyShape ;
> sh:path ex:minStartDate ;
> sh:datatype xsd:date ;
> sh:maxCount 1 ;
> sh:name "min start date" ;
> sh:values **[
> shnex:min [
> shnex:pathValues ( ex:employee ex:startDate ) ;
> ] ;
> ]** .

#### 4.4.3 Max Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *max expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:MaxExpression`:

| Property        | Constraints                                                                                                                                      | Description                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| **`shnex:max`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes from which the maximum value shall be returned. |

EVALUATION OF MAX EXPRESSIONS

Let `max` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:max` in the max expression.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(max, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the max expression is the list consisting of at most one [node](https://www.w3.org/TR/rdf12-concepts/#dfn-node) that is computed as the maximum value from `N`,
see *[SPARQL MAX](https://www.w3.org/TR/sparql12-query/#aggMax)*.

*The remainder of this section is non-normative.*

The Example for `shnex:min` can be easily adapted
for `shnex:max`.

#### 4.4.4 Sum Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *sum expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:SumExpression`:

| Property        | Constraints                                                                                                                                      | Description                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| **`shnex:sum`** | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). | The input nodes from which the sum shall be returned. |

EVALUATION OF SUM EXPRESSIONS

Let `sum` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:sum` in the sum expression.
Let `N` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(sum, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the sum expression is the list consisting of exactly one [node](https://www.w3.org/TR/rdf12-concepts/#dfn-node) that is computed as the sum of all [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) from `N`,
see *[SPARQL SUM](https://www.w3.org/TR/sparql12-query/#aggSum)*.

*The remainder of this section is non-normative.*

Note that `shnex:sum` needs to be used with care and may be misunderstood,
when used with property paths.
The problem is that when a path values expression is used as input to a sum expression,
the path values expression will have eliminated duplicates before they can be processed by the `shnex:sum`.
As a result, only the distinct values will be added up.
To work around this, one option is to use *[SPARQL-based node expressions](https://www.w3.org/TR/shacl12-sparql/#sparql-node-expressions)*.
Another alternative is illustrated in the following example.
> **Example:**
>
> Example 22: Using shnex:sum to compute the sum of the revenues of all departments
>
> ex:CompanyShape
> a sh:NodeShape ;
> sh:targetClass ex:Company ;
> sh:property ex:CompanyShape-totalRevenue .
>
> ex:CompanyShape-totalRevenue
> a sh:PropertyShape ;
> sh:path ex:totalRevenue ;
> sh:datatype xsd:decimal ;
> sh:maxCount 1 ;
> sh:name "total revenue" ;
> sh:values **[
> shnex:sum [
> shnex:nodes [
> shnex:pathValues ex:department ;
> ] ;
> shnex:flatMap [
> shnex:pathValues ex:revenue ;
> ] ;
> ] ;
> ]** .
>
> For the following data graph, the sum will be `42.0`.
>
> ex:MyCompany
> a ex:Company ;
> ex:department [
> ex:revenue 2.1 ;
> ] ;
> ex:department [
> ex:revenue 37.8 ;
> ] ;
> ex:department [
> ex:revenue 2.1 ;
> ] .
>
> In this example, the system will first fetch all values of `ex:department` for the current company.
> Then, for each of these departments, it will get the values for `ex:revenue` via a flat map expression and finally return the sum of those numbers.

### 4.5 Miscellaneous Node Expressions

This section enumerates node expression functions that did not fit into other categories.

#### 4.5.1 InstancesOf Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called an *instancesOf expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:InstancesOfExpression`:

| Property                | Constraints          | Description                                                                                                   |
| ----------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------- |
| **`shnex:instancesOf`** | `sh:nodeKind sh:IRI` | The class that the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) must be instances of. |

EVALUATION OF INSTANCESOF EXPRESSIONS

Let `type` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:instancesOf` in an instancesOf expression.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the instancesOf expression are the [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) that are [SHACL instances](https://www.w3.org/TR/shacl12-core/#dfn-shacl-instance) of `type` in the [focus graph](https://www.w3.org/TR/shacl12-core/#dfn-focus-graph).

*The remainder of this section is non-normative.*

Note that the definition of `SHACL instance` includes instances of subclasses of the given class.
So if the [focus graph](https://www.w3.org/TR/shacl12-core/#dfn-focus-graph) contains `ex:SubClass rdfs:subClassOf ex:SuperClass` and `ex:SubInstance a ex:SubClass` then `ex:SubInstance` will also be returned as instance of `ex:SuperClass`.

The interpretation of `shnex:instancesOf` is similar to `sh:targetClass` and `sh:class`.

Users of this node expression function should be aware that the list of output nodes may be very large.

The Example for `shnex:intersection` uses `shnex:instanceOf`.

#### 4.5.2 Nodes Matching Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called a *nodes matching expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:NodesMatchingExpression`:

| Property                  | Constraints                                                                                                                                                          | Description                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **`shnex:nodesMatching`** | `sh:nodeKind sh:BlankNodeOrIRI` Must be a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape). | The shape that the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) must conform to. |

EVALUATION OF NODES MATCHING EXPRESSIONS

Let `shape` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:nodesMatching` in a nodes matching expression.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the nodes matching expression are the [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) in the [focus graph](https://www.w3.org/TR/shacl12-core/#dfn-focus-graph) that [conform](https://www.w3.org/TR/shacl12-core/#dfn-conform) to `shape`.

*The remainder of this section is non-normative.*

Users of this node expression function should be aware that the list of output nodes may be very large
and that some implementations may not be able to efficiently process it.

The following example illustrates the use of `shnex:nodesMatching` to compute all instances of `ex:Company` that have at least 100 employees.
> **Example:**
>
> Example 23
>
> ex:LargeCompanyShape
> a sh:NodeShape ;
> sh:targetNode **[
> shnex:nodesMatching [
> sh:class ex:Company ;
> sh:property [
> sh:path ex:employee ;
> sh:minCount 100 ;
> ]
> ]
> ]** .

The interpretation of `shnex:nodesMatching` is similar to `sh:targetWhere`.
The main differences are that `sh:targetWhere` is part of SHACL Core and that `shnex:nodesMatching` can be used in arbitrary node expressions.

#### 4.5.3 ConformsToShape Expressions

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that has a [SHACL list](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list) with two [members](https://www.w3.org/TR/shacl12-core/#dfn-members) as its [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for `shnex:conformsToShape` is called a *conformsToShape expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:conformsToShape`.
The two members are as follows:

| Argument    | Constraints                                                                                                                                                               | Description                                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **`node`**  |                                                                                                                                                                           | A node expression producing the [node](https://www.w3.org/TR/rdf12-concepts/#dfn-node) that is validated.                  |
| **`shape`** | `sh:nodeKind sh:IRI` Must produce the IRI of a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape). | A node expression producing the [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) that the node is validated against. |

> **Note:**
>
> > **Note:**
> >
> > Note
>
> Note that `shnex:conformsToShape` is a list parameter function which means that
> it returns at most one output node and
> the members of the arguments list are node expressions that must produce at most one output node each.
> Consequently, if the `shape` argument is a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node), then it will be interpreted as
> a node expression, not as a shape.

EVALUATION OF CONFORMSTOSHAPE EXPRESSIONS

Let `nodeExpr` be the first argument of a conformsToShape expression.
Let `node` be the (single) result of `evalExpr(nodeExpr, focusGraph, focusNode, scope)`.
Let `shapeExpr` be the second argument of a conformsToShape expression.
Let `shape` be the (single) result of `evalExpr(shapeExpr, focusGraph, focusNode, scope)`.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the conformsToShape expression are the empty list
if either `node` or `shape` have no value.
Otherwise, the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) are `( true )` if and only if `node` [conforms](https://www.w3.org/TR/shacl12-core/#dfn-conform) to `shape` (using the derived shapes graph (§3.4) for the shape definition and the [focus graph](https://www.w3.org/TR/shacl12-core/#dfn-focus-graph) as the [data graph](https://www.w3.org/TR/shacl12-core/#dfn-data-graph)),
and `( false )` otherwise.
An [evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure) is produced if the [validation](https://www.w3.org/TR/shacl12-core/#dfn-validation) of the [node](https://www.w3.org/TR/rdf12-concepts/#dfn-node) against the [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) causes a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure).

*The remainder of this section is non-normative.*
> **Example:**
>
> Example 24: Using shnex:conformsToShape to derive a boolean property
>
> ex:HasDirectorShape
> a sh:NodeShape ;
> sh:property [
> sh:path ex:director ;
> sh:minCount 1 ;
> ] .
>
> ex:CompanyShape
> a sh:NodeShape ;
> sh:targetClass ex:Company ;
> sh:property ex:CompanyShape-hasDirector .
>
> ex:CompanyShape-hasDirector
> a sh:PropertyShape ;
> sh:path ex:hasDirector ;
> sh:datatype xsd:boolean ;
> sh:maxCount 1 ;
> sh:name "has director" ;
> sh:values **[
> shnex:conformsToShape ( [ shnex:var "focusNode" ] ex:HasDirectorShape )
> ]** .
>
> For the following data graph, the value of `ex:hasDirector` is `false` because `ex:MyCompany` lacks a value for `ex:director`.
>
> ex:MyCompany
> a ex:Company .

## 5. SPARQL Functions

This section introduces SHACL SPARQL function expressions based on [sparql12-query] that can be used in node expressions.

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that uses a SPARQL function URI `sparql:<NAME>` as its predicate with an `rdf:List` of arguments as its object
is called a *SHACL SPARQL function expression* with the corresponding SPARQL [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name).

EVALUATION OF SPARQL FUNCTION EXPRESSIONS

The evaluation follows the SPARQL semantics for the corresponding SPARQL function.
Each item in the `rdf:List` is evaluated as a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) to produce argument values,
which are then passed to the SPARQL function implementation.
If the SPARQL function produces a single result value, it is wrapped as a singleton list containing that output node.
If the SPARQL function produces no result or an error, the expression produces an empty list or an [evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure), respectively.

Filter by category:

*SPARQL functions usable in SHACL node expressions*

| Function name                                                         | Description and Example                                                                                                                                                                                  | Category  |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [abs](https://www.w3.org/TR/sparql12-query/#func-abs)                 | This function returns the absolute value of a numeric argument. Example: `[ sparql:abs ( -42 ) ]`                                                                                                        | numeric   |
| [bnode](https://www.w3.org/TR/sparql12-query/#func-bnode)             | This function returns a blank node. Example: `[ sparql:bnode () ]`                                                                                                                                       | other     |
| [bound](https://www.w3.org/TR/sparql12-query/#func-bound)             | This form checks whether a variable is bound (assigned a value) in the current solution. Example: `[ sparql:bound ( [ shnex:var "var" ] ) ]`                                                             | other     |
| [ceil](https://www.w3.org/TR/sparql12-query/#func-ceil)               | This function returns the smallest integer greater than or equal to the numeric argument. Example: `[ sparql:ceil ( 3.2 ) ]`                                                                             | numeric   |
| [coalesce](https://www.w3.org/TR/sparql12-query/#func-coalesce)       | This form returns the first non-error, non-unbound value from a sequence of expressions. Example: `[ sparql:coalesce ( [ shnex:var "optionalValue" ] "default" ) ]`                                      | other     |
| [concat](https://www.w3.org/TR/sparql12-query/#func-concat)           | This function concatenates two or more string literals into one continuous string. Example: `[ sparql:concat ( "hello" " " "world" ) ]`                                                                  | string    |
| [contains](https://www.w3.org/TR/sparql12-query/#func-contains)       | This function returns true if the first string argument contains the second string argument as a substring, and false otherwise. Example: `[ sparql:contains ( "hello world" "lo wo" ) ]`                | string    |
| [datatype](https://www.w3.org/TR/sparql12-query/#func-datatype)       | This function returns the datatype IRI of a literal term. Example: `[ sparql:datatype ( "42"^^xsd:integer ) ]`                                                                                           | other     |
| [day](https://www.w3.org/TR/sparql12-query/#func-day)                 | This function returns the day component of an xsd:dateTime or xsd:date. Example: `[ sparql:day ( "2023-12-25T10:30:00"^^xsd:dateTime ) ]`                                                                | date      |
| [divide](https://www.w3.org/TR/sparql12-query/)                       | This operator divides the first numeric expression by the second and returns the result. Example: `[ sparql:divide ( 84 2 ) ]`                                                                           | algebraic |
| [encode](https://www.w3.org/TR/sparql12-query/#func-encode)           | This function encodes a string using a specified method (e.g., URI-encoding), returning the encoded version. Example: `[ sparql:encode ( "hello world" "UTF-8" ) ]`                                      | string    |
| [equals](https://www.w3.org/TR/sparql12-query/)                       | This operator compares two expressions for equality. Example: `[ sparql:equals ( "hello" "hello" ) ]`                                                                                                    | other     |
| [floor](https://www.w3.org/TR/sparql12-query/#func-floor)             | This function returns the greatest integer less than or equal to the numeric argument. Example: `[ sparql:floor ( 3.8 ) ]`                                                                               | numeric   |
| [greater than](https://www.w3.org/TR/sparql12-query/)                 | This operator tests whether the first RDF term is greater than the second RDF term. Example: `[ sparql:greater-than ( 10 5 ) ]`                                                                          | other     |
| [greater than or equal](https://www.w3.org/TR/sparql12-query/)        | This operator tests whether the first RDF term is greater than or equal to the second RDF term. Example: `[ sparql:greater-than-or-equal ( 10 10 ) ]`                                                    | other     |
| [has lang](https://www.w3.org/TR/sparql12-query/#func-haslang)        | This function returns true if the given RDF literal has a specified language, matching the literal’s language tag. Example: `[ sparql:hasLang ( "hello"@en "en" ) ]`                                     | string    |
| [has langdir](https://www.w3.org/TR/sparql12-query/#func-haslangdir)  | This function returns true if the given RDF literal has an initial text direction. Example: `[ sparql:hasLangdir ( "hello"@en--ltr ) ]`                                                                  | string    |
| [hours](https://www.w3.org/TR/sparql12-query/#func-hours)             | This function returns the hour component (0–23) of an xsd:dateTime value. Example: `[ sparql:hours ( "2023-12-25T10:30:00"^^xsd:dateTime ) ]`                                                            | date      |
| [if](https://www.w3.org/TR/sparql12-query/#func-if)                   | This conditional form evaluates a test expression and returns one of two provided expressions based on the boolean outcome of the test. Example: `[ sparql:if ( [ sparql:greater-than ( 10 5 ) ] "big" "small" ) ]` | other     |
| [iri](https://www.w3.org/TR/sparql12-query/#func-iri)                 | This function returns an IRI with the given string. Example: `[ sparql:iri ( "http://example.com/ns#resource" ) ]`                                                                                       | other     |
| [is blank](https://www.w3.org/TR/sparql12-query/#func-isBlank)        | This function returns true if the provided term is a blank node, and false otherwise. Example: `[ sparql:isBlank ( [ sparql:bnode () ] ) ]`                                                              | other     |
| [is iri](https://www.w3.org/TR/sparql12-query/#func-isIRI)            | This function returns true if the provided term is an IRI, and false otherwise. Example: `[ sparql:isIRI ( ex:resource ) ]`                                                                              | other     |
| [is literal](https://www.w3.org/TR/sparql12-query/#func-isLiteral)    | This function returns true if the provided term is an RDF literal, and false otherwise. Example: `[ sparql:isLiteral ( "hello world" ) ]`                                                                | other     |
| [is numeric](https://www.w3.org/TR/sparql12-query/#func-isNumeric)    | This function returns true if the provided term is a numeric literal (e.g., xsd:integer, xsd:decimal, xsd:float, or xsd:double), and false otherwise. Example: `[ sparql:isNumeric ( 42 ) ]`             | other     |
| [is triple](https://www.w3.org/TR/sparql12-query/#func-isTriple)      | This function returns true if the argument is a triple term, and false otherwise. Example: `[ sparql:isTriple ( <<( ex:s ex:p ex:o )>> ) ]`                                                              | other     |
| [is uri](https://www.w3.org/TR/sparql12-query/#func-isIRI)            | This function returns true if the provided term is an IRI, and false otherwise. Example: `[ sparql:isURI ( ex:resource ) ]`                                                                              | other     |
| [lang](https://www.w3.org/TR/sparql12-query/#func-lang)               | This function returns the language tag of a literal, or an empty string if no language tag is present or the term is not a literal. Example: `[ sparql:lang ( "hello"@en ) ]`                            | string    |
| [langdir](https://www.w3.org/TR/sparql12-query/#func-langdir)         | This function returns the initial text direction of a literal. Example: `[ sparql:langdir ( "hello"@en--ltr ) ]`                                                                                         | string    |
| [langmatches](https://www.w3.org/TR/sparql12-query/#func-langMatches) | This function checks whether a given language tag matches a specified language range. Example: `[ sparql:langMatches ( "en-US" "en" ) ]`                                                                 | string    |
| [lcase](https://www.w3.org/TR/sparql12-query/#func-lcase)             | This function transforms all alphabetic characters in the input string to lowercase, according to Unicode case-folding rules. Example: `[ sparql:lcase ( "HELLO" ) ]`                                    | string    |
| [less than](https://www.w3.org/TR/sparql12-query/)                    | This operator tests whether the first RDF term is less than the second RDF term. Example: `[ sparql:less-than ( 5 10 ) ]`                                                                                | other     |
| [less than or equal](https://www.w3.org/TR/sparql12-query/)           | This operator tests whether the first RDF term is less than or equal to the second RDF term. Example: `[ sparql:less-than-or-equal ( 5 5 ) ]`                                                            | other     |
| [logical and](https://www.w3.org/TR/sparql12-query/#func-logical-and) | This form computes the logical AND of two boolean expressions. Example: `[ sparql:logical-and ( true true ) ]`                                                                                           | other     |
| [logical not](https://www.w3.org/TR/sparql12-query/)                  | This form computes the logical NOT of a boolean expression. Example: `[ sparql:logical-not ( true ) ]`                                                                                                   | other     |
| [logical or](https://www.w3.org/TR/sparql12-query/#func-logical-or)   | This form computes the logical OR of two boolean expressions. Example: `[ sparql:logical-or ( true false ) ]`                                                                                            | other     |
| [md5](https://www.w3.org/TR/sparql12-query/#func-md5)                 | This function computes the MD5 hash of the lexical form of a string, returning a hexadecimal string representation of the hash. Example: `[ sparql:md5 ( "hello" ) ]`                                    | other     |
| [minutes](https://www.w3.org/TR/sparql12-query/#func-minutes)         | This function returns the minute component (0–59) of an xsd:dateTime value. Example: `[ sparql:minutes ( "2023-12-25T10:30:00"^^xsd:dateTime ) ]`                                                        | date      |
| [month](https://www.w3.org/TR/sparql12-query/#func-month)             | This function returns the month component of an xsd:dateTime or xsd:date. Example: `[ sparql:month ( "2023-12-25T10:30:00"^^xsd:dateTime ) ]`                                                            | date      |
| [multiply](https://www.w3.org/TR/sparql12-query/)                     | This operator multiplies two numeric expressions and returns the product. Example: `[ sparql:multiply ( 6 7 ) ]`                                                                                         | algebraic |
| [not equals](https://www.w3.org/TR/sparql12-query/)                   | This operator tests two expressions for inequality. Example: `[ sparql:not-equals ( "hello" "world" ) ]`                                                                                                 | other     |
| [now](https://www.w3.org/TR/sparql12-query/#func-now)                 | This function returns the current dateTime (with or without a timezone) at the moment of query execution. Example: `[ sparql:now () ]`                                                                   | date      |
| [object](https://www.w3.org/TR/sparql12-query/#func-object)           | This function returns the object of a triple term. Example: `[ sparql:object ( <<( ex:s ex:p ex:o )>> ) ]`                                                                                               | other     |
| [plus](https://www.w3.org/TR/sparql12-query/)                         | This operator adds two numeric expressions and returns their sum. Example: `[ sparql:plus ( 38 4 ) ]`                                                                                                    | algebraic |
| [predicate](https://www.w3.org/TR/sparql12-query/#func-predicate)     | This function returns the predicate of a triple term. Example: `[ sparql:predicate ( <<( ex:s ex:p ex:o )>> ) ]`                                                                                         | other     |
| [rand](https://www.w3.org/TR/sparql12-query/#func-rand)               | This function returns a random number between 0 and 1. Example: `[ sparql:rand () ]`                                                                                                                     | numeric   |
| [regex](https://www.w3.org/TR/sparql12-query/#func-regex)             | This function tests whether a string matches a regular expression pattern, optionally with a specified flag (e.g., i for case-insensitive). Example: `[ sparql:regex ( "hello123" "[0-9]+" ) ]`          | string    |
| [replace](https://www.w3.org/TR/sparql12-query/#func-replace)         | This function performs a regular expression search-and-replace on a string, returning the modified string. Example: `[ sparql:replace ( "hello world" "world" "universe" ) ]`                            | string    |
| [round](https://www.w3.org/TR/sparql12-query/#func-round)             | This function rounds a numeric argument to the nearest integer. Example: `[ sparql:round ( 3.7 ) ]`                                                                                                      | numeric   |
| [same term](https://www.w3.org/TR/sparql12-query/#func-sameTerm)      | This function checks whether two RDF terms are the same in the strict sense, including their lexical forms, datatypes, and language tags for literals. Example: `[ sparql:sameTerm ( "hello" "hello" ) ]` | other     |
| [same value](https://www.w3.org/TR/sparql12-query/#func-sameValue)    | This function compares two RDF terms for equivalent RDF values, potentially considering numeric type equivalencies and other canonical forms beyond strict term identity. Example: `[ sparql:sameValue ( 42 "42"^^xsd:integer ) ]` | other     |
| [seconds](https://www.w3.org/TR/sparql12-query/#func-seconds)         | This function returns the seconds component of a valid xsd:dateTime or xsd:dateTimeStamp value. Example: `[ sparql:seconds ( "2023-12-25T10:30:00"^^xsd:dateTime ) ]`                                    | date      |
| [sha1](https://www.w3.org/TR/sparql12-query/#func-sha1)               | This function computes the SHA-1 hash of the lexical form of a string, returning a hexadecimal string representation of the result. Example: `[ sparql:sha1 ( "hello" ) ]`                               | other     |
| [sha256](https://www.w3.org/TR/sparql12-query/#func-sha256)           | This function computes the SHA-256 hash of the lexical form of a string, returning the resulting hash as a hexadecimal string. Example: `[ sparql:sha256 ( "hello" ) ]`                                  | other     |
| [sha384](https://www.w3.org/TR/sparql12-query/#func-sha384)           | This function computes the SHA-384 hash of the lexical form of a string, returning the resulting hexadecimal string. Example: `[ sparql:sha384 ( "hello" ) ]`                                            | other     |
| [sha512](https://www.w3.org/TR/sparql12-query/#func-sha512)           | This function computes the SHA-512 hash of the lexical form of a string, returning the result as a hexadecimal string. Example: `[ sparql:sha512 ( "hello" ) ]`                                          | other     |
| [str](https://www.w3.org/TR/sparql12-query/#func-str)                 | This function returns the lexical form of an RDF term, which for IRIs is the IRI string, and for literals is the lexical representation. Example: `[ sparql:str ( 42 ) ]`                                | string    |
| [strafter](https://www.w3.org/TR/sparql12-query/#func-strafter)       | This function returns the substring of the first argument that follows the first occurrence of the second argument. Example: `[ sparql:strafter ( "hello world" " " ) ]`                                 | string    |
| [strbefore](https://www.w3.org/TR/sparql12-query/#func-strbefore)     | This function returns the substring of the first argument that precedes the first occurrence of the second argument. Example: `[ sparql:strbefore ( "hello world" " " ) ]`                               | string    |
| [strdt](https://www.w3.org/TR/sparql12-query/#func-strdt)             | This function creates a typed literal from a string and a datatype IRI, returning an RDF literal with the specified lexical form and datatype. Example: `[ sparql:strdt ( "42" xsd:integer ) ]`          | string    |
| [strends](https://www.w3.org/TR/sparql12-query/#func-strends)         | This function returns true if the first string argument ends with the second string argument, and false otherwise. Example: `[ sparql:strends ( "hello world" "world" ) ]`                               | string    |
| [strlang](https://www.w3.org/TR/sparql12-query/#func-strlang)         | This function creates an RDF literal with the specified lexical form and language tag. Example: `[ sparql:strlang ( "hello" "en" ) ]`                                                                    | string    |
| [strlangdir](https://www.w3.org/TR/sparql12-query/#func-strlangdir)   | This function creates an RDF literal with language tag and initial text direction. Example: `[ sparql:strlangdir ( "hello" "en" "ltr" ) ]`                                                               | string    |
| [strlen](https://www.w3.org/TR/sparql12-query/#func-strlen)           | This function returns the length of the lexical form of a string literal, measured in characters. Example: `[ sparql:strlen ( "hello" ) ]`                                                               | string    |
| [strstarts](https://www.w3.org/TR/sparql12-query/#func-strstarts)     | This function returns true if the first string argument begins with the second string argument, and false otherwise. Example: `[ sparql:strstarts ( "hello world" "hello" ) ]`                           | string    |
| [struuid](https://www.w3.org/TR/sparql12-query/#func-struuid)         | This function generates a UUID as a string. Example: `[ sparql:struuid () ]`                                                                                                                             | string    |
| [subject](https://www.w3.org/TR/sparql12-query/#func-subject)         | This function returns the subject of a triple term. Example: `[ sparql:subject ( <<( ex:s ex:p ex:o )>> ) ]`                                                                                             | other     |
| [substr](https://www.w3.org/TR/sparql12-query/#func-substr)           | This function returns the substring of the given string starting at a specified position and optionally limited to a given length. Example: `[ sparql:substr ( "hello world" 2 5 ) ]`                    | string    |
| [subtract](https://www.w3.org/TR/sparql12-query/)                     | This operator subtracts the second numeric expression from the first and returns the result. Example: `[ sparql:subtract ( 42 7 ) ]`                                                                     | algebraic |
| [timezone](https://www.w3.org/TR/sparql12-query/#func-timezone)       | This function returns the timezone component as an xsd:dayTimeDuration for an xsd:dateTime value with a specified time zone, or an empty value if none. Example: `[ sparql:timezone ( "2023-12-25T10:30:00+02:00"^^xsd:dateTime ) ]` | date      |
| [triple](https://www.w3.org/TR/sparql12-query/#func-triple)           | This function constructs a triple term. Example: `[ sparql:triple ( ex:s ex:p ex:o ) ]`                                                                                                                  | other     |
| [tz](https://www.w3.org/TR/sparql12-query/#func-tz)                   | This function returns the timezone component as a string in ISO 8601 format if present in the xsd:dateTime value, or an empty string otherwise. Example: `[ sparql:tz ( "2023-12-25T10:30:00+02:00"^^xsd:dateTime ) ]` | date      |
| [ucase](https://www.w3.org/TR/sparql12-query/#func-ucase)             | This function transforms all alphabetic characters in the input string to uppercase, following Unicode case-folding conventions. Example: `[ sparql:ucase ( "hello" ) ]`                                 | string    |
| [unary minus](https://www.w3.org/TR/sparql12-query/)                  | This unary operator returns the negation of a numeric expression. Example: `[ sparql:unary-minus ( 42 ) ]`                                                                                               | algebraic |
| [unary plus](https://www.w3.org/TR/sparql12-query/)                   | This unary operator returns the numeric expression unchanged, acting primarily as a syntactic indicator. Example: `[ sparql:unary-plus ( 42 ) ]`                                                         | algebraic |
| [uri](https://www.w3.org/TR/sparql12-query/#func-uri)                 | This function returns an IRI with the given string. Example: `[ sparql:uri ( "http://example.com/ns#resource" ) ]`                                                                                       | other     |
| [uuid](https://www.w3.org/TR/sparql12-query/#func-uuid)               | This function generates a UUID as an IRI. Example: `[ sparql:uuid () ]`                                                                                                                                  | other     |
| [year](https://www.w3.org/TR/sparql12-query/#func-year)               | This function returns the year component of an xsd:dateTime or xsd:date. Example: `[ sparql:year ( "2023-12-25T10:30:00"^^xsd:dateTime ) ]`                                                              | date      |

## 6. Custom Node Expressions

SHACL includes vocabulary terms that can be used to define new [node expression functions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) by wrapping other (parameterized) [node expressions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression).
This makes it possible to extend the library of available SHACL node expressions without having to
hard-code changes to an engine.

### 6.1 Custom Named Parameter Functions

A *custom named parameter function* is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) in a [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) that is a [SHACL instance](https://www.w3.org/TR/shacl12-core/#dfn-shacl-instance) of `sh:NamedParameterExpressionFunction` and
a [SHACL subclass](https://www.w3.org/TR/shacl12-core/#dfn-shacl-subclass) of `sh:NamedParameterExpression`.
It has a single [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for `sh:bodyExpression` that is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression).

A custom named parameter function declares one or more [parameters](https://www.w3.org/TR/shacl12-core/#dfn-parameter) as [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:parameter`, where each such [parameter](https://www.w3.org/TR/shacl12-core/#dfn-parameter) has exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for `sh:path` and that value is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri).
At least one of the parameters has `sh:keyParameter true`, declaring the key parameters for the function.
The key parameters of all [node expression functions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) (including the built-in ones from the `shnex:` namespace) must be disjoint.

Custom named parameter functions can reference the declared [parameters](https://www.w3.org/TR/shacl12-core/#dfn-parameter) using an arg expression such as `[ shnex:arg ex:param ]`, where the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:arg` matches the [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) of the [parameter](https://www.w3.org/TR/shacl12-core/#dfn-parameter)'s `sh:path`.

A *custom named parameter expression* is a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) represented by a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that has exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for at least one of
the key parameters.

EVALUATION OF CUSTOM NAMED PARAMETER EXPRESSIONS

Let `expr` be a custom named parameter expression with the custom named parameter function `f`.
Let `body` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:bodyExpression` at `f` in the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph).

Let `argScope` be a map of (parameter) [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) as keys and (argument) [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) as values, so that each [parameter](https://www.w3.org/TR/shacl12-core/#dfn-parameter) of `f` has the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of the parameter's `sh:path` from `expr`.
For example, if `f` declares just one [parameter](https://www.w3.org/TR/shacl12-core/#dfn-parameter) with `sh:path` `ex:param` and `expr` is `[ ex:param 42 ]` then `argScope` is `{ ex:param : 42 }`.

The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `expr` are computed using `evalExpr(expr, focusGraph, focusNode, scope) -> evalExpr(body, focusGraph, focusNode, argScope)`

*The remainder of this section is non-normative.*

The following example defines a new [node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) `ex:AverageExpression` that takes another node expression as input using the key parameter `ex:average` and then calculates the sum of all input nodes and divides it by the number of nodes,
returning the average value of these nodes.
> **Example:**
>
> Example 25
>
> ex:AverageExpression
> a sh:NamedParameterExpressionFunction ;
> rdfs:label "Average expression"@en ;
> rdfs:comment "Computes the average of the nodes provided by ex:average." ;
> rdfs:subClassOf sh:NamedParameterExpression ;
> sh:parameter ex:AverageExpression-average ;
> sh:bodyExpression [
> sparql:divide (
> [ shnex:sum [ shnex:arg ex:average ] ]
> [ shnex:count [ shnex:arg ex:average ] ]
> )
> ] ;
> .
> ex:AverageExpression-average
> a sh:Parameter ;
> sh:path ex:average ;
> sh:name "average" ;
> sh:description "The nodes of which the average shall be computed." ;
> sh:keyParameter true ;
> .

This new node expression function can the be used as follows:
> **Example:**
>
> Example 26
>
> ex:CompanyShape-averageIncome
> a sh:PropertyShape ;
> sh:path ex:averageIncome ;
> sh:datatype xsd:decimal ;
> sh:values [ **ex:average [
> shnex:pathValues ( ex:employee ex:income )
> ]** ] .

### 6.2 Custom List Parameter Functions

A *custom list parameter function* is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) in a [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) that is a [SHACL instance](https://www.w3.org/TR/shacl12-core/#dfn-shacl-instance) of `sh:ListParameterExpressionFunction` and
a [SHACL subclass](https://www.w3.org/TR/shacl12-core/#dfn-shacl-subclass) of `sh:ListParameterExpression`.
The [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) of a custom list parameter function is its list parameter property.
It has a single [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for `sh:bodyExpression` that is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression).

Custom list parameter functions can reference the arguments using an arg expression such as `[ shnex:arg 0 ]` and `[ shnex:arg 1 ]` where the `xsd:integer` `n` corresponds to the `n`th [member](https://www.w3.org/TR/shacl12-core/#dfn-members) of the arguments list, starting with `0` as the first member.

A *custom list parameter expression* is a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) represented by a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of exactly one [triple](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple) and the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) of that triple is the list parameter property of a custom list parameter function in the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph).

EVALUATION OF CUSTOM LIST PARAMETER EXPRESSIONS

Let `expr` be a custom list parameter expression with the custom list parameter function `f`.
Let `body` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:bodyExpression` at `f` in the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph).

Let `argScope` be a map of (parameter index) [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) as keys and (argument) [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) as values, so that each list argument of `expr` has the index of the argument as an `xsd:integer` as key, starting with `0` for the first argument.
For example, if `expr` has arguments `( 38 4 )` then the `argScope` is `{ 0 : 38, 1 : 4 }`.

The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `expr` are computed using `evalExpr(expr, focusGraph, focusNode, scope) -> evalExpr(body, focusGraph, focusNode, argScope)` where an [evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure) is reported when there is more than 1 output node.

*The remainder of this section is non-normative.*

The following example defines a new [node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) `ex:spacedConcat` that takes two nodes as input and returns a string concatenating the two nodes with a space in between.
> **Example:**
>
> Example 27
>
> ex:spacedConcat
> a sh:ListParameterExpressionFunction ;
> rdfs:label "Spaced concat expression"@en ;
> rdfs:subClassOf sh:ListParameterExpression ;
> sh:bodyExpression [
> sparql:concat (
> [ shnex:arg 0 ]
> " "
> [ shnex:arg 1 ]
> )
> ] .

This new node expression function can the be used as follows:
> **Example:**
>
> Example 28
>
> ex:Person-fullName
> a sh:PropertyShape ;
> sh:path ex:fullName ;
> sh:datatype xsd:string ;
> sh:values [ **ex:spacedConcat (
> [ shnex:pathValues ex:firstName ]
> [ shnex:pathValues ex:lastName ]
> )** ] .

### 6.3 Arg Expressions

Custom node expressions can use `shnex:arg` to access the arguments.

A [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that is the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the following properties
is called an *arg expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `shnex:ArgExpression`:

| Property        | Constraints                                                                                                               | Description                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **`shnex:arg`** | ` 										sh:or (  										  [ sh:nodeKind sh:IRI ]  										  [ sh:datatype xsd:integer ]  										) 										` | The argument key, e.g. `ex:myParameter` or `1`. |

EVALUATION OF ARG EXPRESSIONS

Let `arg` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `shnex:arg` in the arg expression.
The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of the var expression are computed as follows, in order:

1. if `arg` is in the `scope` and has the value `a` then `evalExpr(expr, focusGraph, focusNode, scope) -> evalExpr(a, focusGraph, focusNode, {})`
2. otherwise `evalExpr(expr, focusGraph, focusNode, scope) -> []`

*The remainder of this section is non-normative.*

Both `shnex:arg` and `shnex:var` access values from the scope.
The difference is that `shnex:arg` interprets the values as node expressions, while `shnex:var` treats the values as individual nodes.
As a result, a custom node expression can evaluate nested node expressions that are passed in as arguments.

Examples of `shnex:arg` can be found in Example 25 and Example 27.

## 7. Constraint Components

This section introduces SHACL [constraint components](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) that operate on node expressions.

### 7.1 sh:expression

Based on [node expressions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression), this section introduces a [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) called *expression constraints*.
Expression constraints can be used in any [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) to declare the condition that the [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) specified via `sh:expression` has `true` as its only output node.
The evaluation of these node expressions is repeated for all [value nodes](https://www.w3.org/TR/shacl12-core/#dfn-value-node) of the [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) as the [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node).

Constraint Component IRI: `sh:ExpressionConstraintComponent`

Parameters:

| Property        | Summary and Syntax Rules                                                                                                                                                                                 |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sh:expression` | The [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that must return `true`. The [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:expression` at a [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) must be well-formed [node expressions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). |

TEXTUAL DEFINITION

Let `$expr` be a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:expression`.
For each [value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node) `v` where `evalExpr(expr, data graph, focusNode, {value: v})` does not return the list consisting of exactly `true` as its [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes),
there is a [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) that has `v` as its `sh:value` and a [deep copy](https://www.w3.org/TR/shacl12-core/#dfn-deep-copy) of `$expr` in the results graph as its `sh:sourceConstraint`.

*The remainder of this section is non-normative.*

Note that the `scope` in the evaluation of expression constraints maps `value` to the current [value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node).

The following example uses some SPARQL-based node expressions to declare
the constraint that the values of `ex:ibanNumber` must start with the same two (upper-case) letters as
the values of the path `ex:country/ex:code`.
> **Example:**
>
> Example 29
>
> ex:AccountShape
> a sh:NodeShape ;
> sh:targetClass ex:Account ;
> sh:property ex:AccountShape-ibanNumber .
>
> ex:AccountShape-ibanNumber
> a sh:PropertyShape ;
> sh:path ex:ibanNumber ;
> sh:datatype xsd:string ;
> sh:message "IBAN numbers must start with the country code, in upper-case letters." ; **sh:expression [
> sparql:strstarts (
> [ shnex:var "value" ]
> [
> sparql:ucase (
> [
> shnex:pathValues ( ex:country ex:code )
> shnex:nodes [ shnex:var "focusNode" ]
> ]
> )
> ]
> )
> ]** .
>
> ex:ValidGermanAccount
> a ex:Account ;
> ex:ibanNumber "DE123456..." ;
> ex:country ex:Germany .
>
> ex:InvalidGermanAccount a ex:Account ;
> ex:ibanNumber "DE987654..." ;
> ex:country ex:Estonia .
>
> ex:Estonia
> a ex:Country ;
> ex:code "ee" .
>
> ex:Germany
> a ex:Country ;
> ex:code "de" .

### 7.2 sh:nodeByExpression

`sh:nodeByExpression` specifies the condition that each [value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node) conforms to the [node shapes](https://www.w3.org/TR/shacl12-core/#dfn-node-shape) produced by a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression).
The evaluation of these node expressions is repeated for all [value nodes](https://www.w3.org/TR/shacl12-core/#dfn-value-node) of the [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) as the [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node).

Constraint Component IRI: `sh:NodeByExpressionConstraintComponent`

Parameters:

| Property              | Summary and Syntax Rules                                                                                                                                                                                 |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sh:nodeByExpression` | The [node shapes](https://www.w3.org/TR/shacl12-core/#dfn-node-shape) that all value nodes need to conform to. The [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:nodeByExpression` in a shape must be [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) [node expressions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression). |

TEXTUAL DEFINITION

Let `$expr` be a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:nodeByExpression`.
For each [value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node) `v`: perform a [conformance check](https://www.w3.org/TR/shacl12-core/#dfn-conformance-checking) of `v` against each [output node](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(expr, 						data graph, v, {})` `s`. A [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) *MUST* be produced if the [conformance check](https://www.w3.org/TR/shacl12-core/#dfn-conformance-checking) of `v` against `s` produces a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure). Otherwise, if `v` does
not [conform](https://www.w3.org/TR/shacl12-core/#dfn-conform) to `s`, there is a [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) with `v` as `sh:value` and a [deep copy](https://www.w3.org/TR/shacl12-core/#dfn-deep-copy) of `s` as `sh:sourceConstraint`.

*The remainder of this section is non-normative.*

`sh:nodeByExpression` functions similarly to `sh:node`, but instead of referencing a fixed [node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape),
a referenced [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) is used to dynamically compute the set of [node shapes](https://www.w3.org/TR/shacl12-core/#dfn-node-shape) to which each [value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node) must conform.

There are three key differences between `sh:nodeByExpression` and *[`sh:node`](https://www.w3.org/TR/shacl12-core/#NodeConstraintComponent)*:

1. `sh:nodeByExpression` references a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) instead of a fixed [node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape) as `sh:node` does.
2. `sh:nodeByExpression` cannot reference a [node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape) that is a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) as a value like `sh:node` can,
   as a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) would be interpreted as a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression).
3. [Results](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) generated by `sh:nodeByExpression` additionally include a value for `sh:sourceConstraint`.

Note that `sh:node` and `sh:nodeByExpression` exhibit the same behavior when given a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) that is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) of a [node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape).
In this case, `sh:node` directly validates against the specified [node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape), whereas `sh:nodeByExpression` interprets the [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) as an IRI expression that evaluates to a set containing the same [node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape).

The following example demonstrates how `sh:nodeByExpression` could be used in the context of the [W3C Data Cube Vocabulary](https://www.w3.org/TR/vocab-data-cube/).
Building upon examples 5 and 6 from the Data Cube Vocabulary documentation, Data Structure Definition is extended with the property `eg:hasShape`,
which links to an associated [node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape) to which relevant `qb:Observation` instances must conform.
To validate that every `qb:Observation` instance conforms to the appropriate shape, `sh:nodeByExpression` with a path values expression is used to locate the shape at the property path `qb:dataSet/qb:structure/eg:hasShape` from each `qb:Observation` instance.
> **Example:**
>
> Example 30
>
> eg:dsd1-shape
> a sh:NodeShape ;
> sh:property [ # _:b1
> sh:path sdmx-dimension:refTime ;
> sh:datatype xsd:date ;
> sh:minCount 1 ;
> sh:maxCount 1 ;
> ] ;
> sh:property [ # _:b2
> sh:path eg-measure:quantity ;
> sh:datatype xsd:integer ;
> sh:minCount 1 ;
> sh:maxCount 1 ;
> sh:minInclusive 0 ;
> ] ;
> sh:property [ # _:b3
> sh:path eg-measure:weight ;
> sh:datatype xsd:decimal ;
> sh:minCount 1 ;
> sh:maxCount 1 ;
> sh:minInclusive 0.0 ;
> ] .
>
> eg:ObservationShape
> a sh:NodeShape ;
> sh:targetClass qb:Observation ;
> sh:nodeByExpression [
> shnex:pathValues (qb:dataSet qb:structure eg:hasShape) ;
> ] .
>
> ```
> {
> 	"@graph": [
> 		{
> 			"@id": "eg:dsd1-shape",
> 			"@type": "sh:NodeShape",
> 			"sh:property": [
> 				{
> 					"@id": "_:b1",
> 					"sh:path": {
> 						"@id": "sdmx-dimension:refTime"
> 					},
> 					"sh:datatype": {
> 						"@id": "xsd:date"
> 					},
> 					"sh:minCount": {
> 						"@type": "xsd:integer",
> 						"@value": "1"
> 					},
> 					"sh:maxCount": {
> 						"@type": "xsd:integer",
> 						"@value": "1"
> 					}
> 				},
> 				{
> 					"@id": "_:b2",
> 					"sh:path": {
> 						"@id": "eg-measure:quantity"
> 					},
> 					"sh:datatype": {
> 						"@id": "xsd:integer"
> 					},
> 					"sh:minCount": {
> 						"@type": "xsd:integer",
> 						"@value": "1"
> 					},
> 					"sh:maxCount": {
> 						"@type": "xsd:integer",
> 						"@value": "1"
> 					},
> 					"sh:minInclusive": {
> 						"@type": "xsd:integer",
> 						"@value": "0"
> 					}
> 				},
> 				{
> 					"@id": "_:b3",
> 					"sh:path": {
> 						"@id": "eg-measure:weight"
> 					},
> 					"sh:datatype": {
> 						"@id": "xsd:decimal"
> 					},
> 					"sh:minCount": {
> 						"@type": "xsd:integer",
> 						"@value": "1"
> 					},
> 					"sh:maxCount": {
> 						"@type": "xsd:integer",
> 						"@value": "1"
> 					},
> 					"sh:minInclusive": {
> 						"@type": "xsd:decimal",
> 						"@value": "0.0"
> 					}
> 				}
> 			]
> 		},
> 		{
> 			"@id": "eg:ObservationShape",
> 			"@type": "sh:NodeShape",
> 			"sh:targetClass": {
> 				"@id": "qb:Observation"
> 			},
> 			"sh:nodeByExpression": {
> 				"shnex:pathValues": {
> 					"@list": [
> 						{
> 							"@id": "qb:dataSet"
> 						},
> 						{
> 							"@id": "qb:structure"
> 						},
> 						{
> 							"@id": "eg:hasShape"
> 						}
> 					]
> 				}
> 			}
> 		}
> 	]
> }
> ```
>
> eg:dataset1
> a qb:DataSet ;
> qb:structure eg:dsd1 .
>
> eg:dsd1
> a qb:DataStructureDefinition ;
> rdfs:comment "shipments by time (multiple measures approach)"@en ;
> eg:hasShape eg:dsd1-shape ;
> qb:component [
> qb:dimension sdmx-dimension:refTime;
> ] ;
> qb:component [
> qb:measure eg-measure:quantity ;
> ] ;
> qb:component [
> qb:measure eg-measure:weight ;
> ] .
>
> eg:obs1a
> a qb:Observation;
> qb:dataSet eg:dataset1;
> sdmx-dimension:refTime "2010-07-30"^^xsd:date;
> eg-measure:weight 1.3 ;
> eg-measure:quantity 42 .
>
> eg:obs1b a qb:Observation;
> qb:dataSet eg:dataset1;
> sdmx-dimension:refTime "2010-07-31T12:00:00"^^xsd:dateTime;
> eg-measure:weight 1.4 .
>
> ```
> {
> 	"@graph": [
> 		{
> 			"@id": "eg:dataset1",
> 			"@type": "qb:DataSet",
> 			"qb:structure": {
> 				"@id": "eg:dsd1"
> 			}
> 		},
> 		{
> 			"@id": "eg:dsd1",
> 			"@type": "qb:DataStructureDefinition",
> 			"rdfs:comment": {
> 				"@language": "en",
> 				"@value": "shipments by time (multiple measures approach)"
> 			}
> 			"eg:hasShape": {
> 				"@id": "eg:dsd1-shape"
> 			},
> 			"qb:component": [
> 				{
> 					"qb:dimension": {
> 						"@id": "sdmx-dimension:refTime"
> 					}
> 				},
> 				{
> 					"qb:measure": {
> 						"@id": "eg-measure:quantity"
> 					}
> 				},
> 				{
> 					"qb:measure": {
> 						"@id": "eg-measure:weight"
> 					}
> 				}
> 			]
> 		},
> 		{
> 			"@id": "eg:obs1a",
> 			"@type": "qb:Observation",
> 			"qb:dataSet": {
> 				"@id": "eg:dataset1"
> 			},
> 			"sdmx-dimension:refTime": {
> 				"@type": "xsd:date",
> 				"@value": "2010-07-30"
> 			},
> 			"eg-measure:quantity": {
> 				"@type": "xsd:integer",
> 				"@value": "42"
> 			},
> 			"eg-measure:weight": {
> 				"@type": "xsd:decimal",
> 				"@value": "1.3"
> 			}
> 		},
> 		{
> 			"@id": "eg:obs1b",
> 			"@type": "qb:Observation",
> 			"qb:dataSet": {
> 				"@id": "eg:dataset1"
> 			},
> 			"sdmx-dimension:refTime": {
> 				"@type": "xsd:dateTime",
> 				"@value": "2010-07-31T12:00:00"
> 			}
> 			"eg-measure:weight": {
> 				"@type": "xsd:decimal",
> 				"@value": "1.4"
> 			},
> 		}
> 	]
> }
> ```
>
> [ a sh:ValidationReport ;
> sh:conforms false ;
> sh:result [
> a sh:ValidationResult ;
> sh:resultSeverity sh:Violation ;
> sh:focusNode eg:obs1b;
> sh:value eg:obs1b ;
> sh:resultMessage "Value does not conform to shape eg:dsd1-shape." ;
> sh:sourceConstraint eg:dsd1-shape ;
> sh:sourceConstraintComponent sh:NodeByExpressionConstraintComponent ;
> sh:sourceShape eg:ObservationShape ;
> sh:detail [
> a sh:ValidationResult ;
> sh:resultSeverity sh:Violation ;
> sh:focusNode eg:obs1b ;
> sh:resultPath sdmx-dimension:refTime ;
> sh:value "2010-07-31T12:00:00"^^xsd:dateTime ;
> sh:resultMessage "Value does not have datatype xsd:date" ;
> sh:sourceConstraintComponent sh:DatatypeConstraintComponent ;
> sh:sourceShape _:b1 ;
> ] ;
> sh:detail [
> a sh:ValidationResult ;
> sh:resultSeverity sh:Violation ;
> sh:focusNode eg:obs1b ;
> sh:resultPath eg-measure:quantity ;
> sh:resultMessage "Less than 1 values" ;
> sh:sourceConstraintComponent sh:MinCountConstraintComponent ;
> sh:sourceShape _:b2 ;
> ] ;
> ] ;
> ] .
>
> ```
> {
> 	"@type": "sh:ValidationReport",
> 	"sh:conforms": {
> 		"@type": "xsd:boolean",
> 		"@value": "false"
> 	},
> 	"sh:result": {
> 		"@type": "sh:ValidationResult",
> 		"sh:resultSeverity": {
> 			"@id": "sh:Violation"
> 		},
> 		"sh:focusNode": {
> 			"@id": "eg:obs1b"
> 		},
> 		"sh:value": {
> 			"@id": "eg:obs1b"
> 		},
> 		"sh:resultMessage": "Value does not conform to shape eg:dsd1-shape.",
> 		"sh:sourceConstraint": {
> 			"@id": "eg:dsd1-shape"
> 		},
> 		"sh:sourceConstraintComponent": {
> 			"@id": "sh:NodeByExpressionConstraintComponent"
> 		},
> 		"sh:sourceShape": {
> 			"@id": "eg:ObservationShape"
> 		},
> 		"sh:detail": [
> 			{
> 				"@type": "sh:ValidationResult",
> 				"sh:resultSeverity": {
> 					"@id": "sh:Violation"
> 				},
> 				"sh:focusNode": {
> 					"@id": "eg:obs1b"
> 				},
> 				"sh:resultPath": {
> 					"@id": "sdmx-dimension:refTime"
> 				},
> 				"sh:value": {
> 					"@type": "xsd:dateTime",
> 					"@value": "2010-07-31T12:00:00"
> 				},
> 				"sh:resultMessage": "Value does not have datatype xsd:date",
> 				"sh:sourceConstraintComponent": {
> 					"@id": "sh:DatatypeConstraintComponent"
> 				},
> 				"sh:sourceShape": {
> 					"@id": "_:b1"
> 				}
> 			},
> 			{
> 				"@type": "sh:ValidationResult",
> 				"sh:resultSeverity": {
> 					"@id": "sh:Violation"
> 				},
> 				"sh:focusNode": {
> 					"@id": "eg:obs1b"
> 				},
> 				"sh:resultPath": {
> 					"@id": "eg-measure:quantity"
> 				},
> 				"sh:resultMessage": "Less than 1 values",
> 				"sh:sourceConstraintComponent": {
> 					"@id": "sh:MinCountConstraintComponent"
> 				},
> 				"sh:sourceShape": {
> 					"@id": "_:b2"
> 				}
> 			}
> 		]
> 	}
> }
> ```

## 8. Dynamic SHACL

This section defines *Dynamic SHACL* as a dialect of SHACL that some implementations *MAY* support.

In Dynamic SHACL any [parameter](https://www.w3.org/TR/shacl12-core/#dfn-parameter) of a [constraint](https://www.w3.org/TR/shacl12-core/#dfn-constraint) can be computed using a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression),
excluding those that do *not* allow [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) (such as `sh:node`)
but including those that take [SHACL lists](https://www.w3.org/TR/shacl12-core/#dfn-shacl-list) as values (such as `sh:class`, `sh:datatype`, and `sh:in`).
During [validation](https://www.w3.org/TR/shacl12-core/#dfn-validation), such [node expressions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) are evaluated in the [data graph](https://www.w3.org/TR/shacl12-core/#dfn-data-graph),
using the current [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node).
The resulting [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-node) will be used as [parameters](https://www.w3.org/TR/shacl12-core/#dfn-parameter) for the [constraint](https://www.w3.org/TR/shacl12-core/#dfn-constraint).

### 8.1 Example: Dynamic Minimum Age of Presidents

*This section is non-normative.*

As a use case of Dynamic SHACL, assume we want to express that the legal minimum age
of a president is 18 unless the country is USA, where it is 35.
> **Example:**
>
> Example 31: Example of Dynamic SHACL using a node expression at sh:minInclusive
>
> ex:PresidentShape
> a sh:NodeShape ;
> sh:targetClass ex:President ;
> sh:property ex:PresidentShape-age ;
> .
> ex:PresidentShape-age
> a sh:PropertyShape ;
> sh:path ex:age ; **sh:minInclusive [
> shnex:if [
> sparql:eq (
> [ shnex:pathValues ex:country ]
> ex:USA
> )
> ]
> shnex:then 35 ;
> shnex:else 18 ;
> ]** .

### 8.2 Example: Dynamic Enumerations

*This section is non-normative.*

As a use case of Dynamic SHACL, assume the following [data graph](https://www.w3.org/TR/shacl12-core/#dfn-data-graph).
> **Example:**
>
> Example 32: Example data graph with addresses
>
> ex:ArizonaAddress1
> a ex:Address ;
> ex:street "123 John Muir Ave" ;
> ex:country ex:USA ;
> ex:state "AZ" ;
> .
> ex:QueenslandAddress1
> a ex:Address ;
> ex:street "123 Bob Katter Cl" ;
> ex:country ex:Australia ;
> ex:state "QLD" ;
> .

We want to express that the valid values of `ex:state` depend on the value of `ex:country` at the given focus node.
For example, the valid values for country `ex:USA` would be `( "AL" "AK" "AZ" ... )` while valid values for country `ex:Australia` would be `( "ACT" "NSW" "NT" "QLD" "SA" "TAS" "VIC" "WA" )`.
This fact can be represented as part of the data:
> **Example:**
>
> Example 33: The valid states can be attached to each country
>
> ex:Australia
> a ex:Country ;
> ex:stateCode "ACT",
> "NSW",
> "NT",
> "QLD",
> "SA",
> "TAS",
> "VIC",
> "WA" ;
> .
> ex:USA
> a ex:Country ;
> ex:stateCode "AL",
> "AK",
> "AZ",
> "AR" ; # ...
> .

Using this extra information, we can now define a `sh:in` constraint using a path values expression:
> **Example:**
>
> Example 34: Example of Dynamic SHACL using a node expression at sh:in
>
> ex:Address
> a sh:ShapeClass ;
> sh:property ex:Address-state ;
> .
> ex:Address-state
> a sh:PropertyShape ;
> sh:path ex:state ; **sh:in [
> shnex:pathValues ( ex:country ex:stateCode )
> ]** .

During validation, a Dynamic SHACL engine will evaluate the path values expression at `sh:in` and use the resulting nodes as members of the allowed values.
Thus, when the value of `ex:country` is `ex:USA`, it will look up the
state codes that are linked to `ex:USA`.

## 9. Security and Privacy Considerations

Security considerations of SHACL Node Expressions include all the [security considerations of SHACL Core](https://www.w3.org/TR/shacl12-core/#security).

## B. Index

### B.1 Terms defined by this specification

- arg expression §6.3
- concat expression §4.2.3
- conformsToShape expression §4.5.3
- constant node expressions §3.1
- count expression §4.4.1
- custom list parameter expression §6.2
- custom list parameter function §6.2
- custom named parameter expression §6.1
- custom named parameter function §6.1
- distinct expression §4.2.1
- Dynamic SHACL §8.
- empty expression §4.1.1
- exists expression §4.1.5
- expression constraints §7.1
- filter shape expression §4.2.5
- find first expression §4.3.2
- flat map expression §4.3.1
- if expression §4.1.6
- instancesOf expression §4.5.1
- intersection expression §4.2.2
- IRI expression §3.1.1
- key parameter §3.2.1
- limit expression §4.2.6
- list expression §4.1.3
- list parameter function §3.2.2
- list parameter property §3.2.2
- literal expression §3.1.2
- match all expression §4.3.3
- max expression §4.4.3
- min expression §4.4.2
- named parameter function §3.2.1
- nodes matching expression §4.5.2
- offset expression §4.2.7
- order by expression §4.2.8
- path values expression §4.1.4
- remove expression §4.2.4
- SHACL SPARQL function expression §5.
- sum expression §4.4.4
- triple term expression §3.1.3
- var expression §4.1.2

### B.2 Terms defined by reference

- [RDF12-CONCEPTS] defines the following:
  * blank node
  * datatype
  * IRI
  * literal
  * node
  * object type
  * predicate
  * RDF graph
  * RDF term
  * RDF triple
  * subject
  * term equality
  * triple terms
- [SHACL12-CORE] defines the following:
  * conformance checking
  * Conformance section of SHACL Core
  * conforms
  * constraint
  * constraint component
  * data graph
  * deep copy
  * evaluation
  * evaluation failure
  * failure
  * focus graph
  * focus node
  * function name
  * mandatory parameter
  * members
  * node expression
  * node expression function
  * node shape
  * optional parameter
  * output nodes
  * parameter
  * parameter value
  * property shape
  * security considerations of SHACL Core
  * sh:node
  * SHACL instance
  * SHACL list
  * SHACL property path
  * SHACL subclass
  * SHACL type
  * shape
  * shapes graph
  * target
  * validation
  * validation result
  * validator
  * value
  * value node
  * well-formed
- [SHACL12-SPARQL] defines the following:
  * select expressions
  * SPARQL-based node expressions
- [SPARQL12-QUERY] defines the following:
  * SPARQL MAX
  * SPARQL MIN
  * SPARQL ORDER BY
  * SPARQL SUM

## D. References

### D.1 Normative references

[rdf12-concepts]

[RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/). Andy Seaborne; Gregg Kellogg; Olaf Hartig; Pierre-Antoine Champin. W3C. 7 April 2026. W3C Candidate Recommendation. URL: <https://www.w3.org/TR/rdf12-concepts/>

[rdf12-turtle]

[RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/). Gregg Kellogg; Andy Seaborne; Dominik Tomaszuk. W3C. 12 June 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-turtle/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/info/rfc2119/). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc2119/>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/info/rfc8174/). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc8174/>

[shacl12-core]

[SHACL 1.2 Core](https://www.w3.org/TR/shacl12-core/). Holger Knublauch; Thomas Bergwinkl; Yousouf Taghzouti; Jesse Wright. W3C. 20 July 2026. W3C Working Draft. URL: <https://www.w3.org/TR/shacl12-core/>

[shacl12-sparql]

[SHACL 1.2 SPARQL Extensions](https://www.w3.org/TR/shacl12-sparql/). Holger Knublauch; Matt Goldberg; Scott Henninger; Livio Robaldo. W3C. 17 July 2026. W3C Working Draft. URL: <https://www.w3.org/TR/shacl12-sparql/>

[sparql12-query]

[SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/). Olaf Hartig; Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 25 June 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-query/>

Permalink

**Referenced in:**

- § 3. Node Expression Syntax

Permalink

**Referenced in:**

- § 3.1.1 IRI Expressions (2)
- § 4.1.3 List Expressions
- § 7.2 sh:nodeByExpression

Permalink

**Referenced in:**

- § 3.1.2 Literal Expressions (2)

Permalink

**Referenced in:**

- § 3.1.3 Triple Term Expressions (2)

Permalink

**Referenced in:**

- § 3. Node Expression Syntax
- § 3.2.1 Named Parameter Functions (2) (3) (4)
- § 3.2.2 List Parameter Functions (2)

Permalink

**Referenced in:**

- § 3. Node Expression Syntax
- § 3.2.1 Named Parameter Functions
- § 3.2.2 List Parameter Functions
- § 6.1 Custom Named Parameter Functions (2) (3) (4)

Permalink

**Referenced in:**

- § 3. Node Expression Syntax
- § 3.2.2 List Parameter Functions (2) (3) (4)
- § 4.5.3 ConformsToShape Expressions

Permalink

**Referenced in:**

- § 3.2.2 List Parameter Functions
- § 6.2 Custom List Parameter Functions (2)

Permalink

**Referenced in:**

- § 4.1.1 Empty Expressions

Permalink

**Referenced in:**

- § 4.1.2 Var Expressions (2) (3)
- § 6.3 Arg Expressions

Permalink

**Referenced in:**

- § 4.1.3 List Expressions (2) (3)

Permalink

**Referenced in:**

- § 4.1.4 Path Values Expressions (2) (3) (4)
- § 4.4.4 Sum Expressions
- § 7.2 sh:nodeByExpression
- § 8.2 Example: Dynamic Enumerations

Permalink

**Referenced in:**

- § 4.1.5 Exists Expressions (2)

Permalink

**Referenced in:**

- § 4.1.6 If Expressions (2)

Permalink

**Referenced in:**

- § 4.2.1 Distinct Expressions (2)

Permalink

**Referenced in:**

- § 4.2.2 Intersection Expressions (2)

Permalink

**Referenced in:**

- § 4.2.3 Concat Expressions (2) (3)

Permalink

**Referenced in:**

- § 4.2.4 Remove Expressions (2)

Permalink

**Referenced in:**

- § 2. Getting started with Node Expressions
- § 4.2.5 Filter Shape Expressions (2)

Permalink

**Referenced in:**

- § 4.2.6 Limit Expressions (2)

Permalink

**Referenced in:**

- § 4.2.7 Offset Expressions (2)

Permalink

**Referenced in:**

- § 4.2.8 OrderBy Expressions (2)

Permalink

**Referenced in:**

- § 4.3.1 FlatMap Expressions (2)
- § 4.4.4 Sum Expressions

Permalink

**Referenced in:**

- § 4.3.2 FindFirst Expressions (2)

Permalink

**Referenced in:**

- § 4.3.3 MatchAll Expressions (2)

Permalink

**Referenced in:**

- § 4.4.1 Count Expressions (2)

Permalink

**Referenced in:**

- § 4.4.2 Min Expressions (2)

Permalink

**Referenced in:**

- § 4.4.3 Max Expressions (2)

Permalink

**Referenced in:**

- § 4.4.4 Sum Expressions (2) (3)

Permalink

**Referenced in:**

- § 2. Getting started with Node Expressions
- § 4.5.1 InstancesOf Expressions (2)

Permalink

**Referenced in:**

- § 4.5.2 Nodes Matching Expressions (2)

Permalink

**Referenced in:**

- § 4.5.3 ConformsToShape Expressions (2) (3)

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 6.1 Custom Named Parameter Functions (2) (3)

Permalink

**Referenced in:**

- § 6.1 Custom Named Parameter Functions

Permalink

**Referenced in:**

- § 6.2 Custom List Parameter Functions (2) (3) (4)

Permalink

**Referenced in:**

- § 6.2 Custom List Parameter Functions

Permalink

**Referenced in:**

- § 6.1 Custom Named Parameter Functions
- § 6.2 Custom List Parameter Functions
- § 6.3 Arg Expressions

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 8.1 Example: Dynamic Minimum Age of Presidents
- § 8.2 Example: Dynamic Enumerations

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3. Node Expression Syntax (2) (3)
- § 3.2.1 Named Parameter Functions
- § 3.2.2 List Parameter Functions (2)
- § 4. Node Expressions Library
- § 4.1.1 Empty Expressions
- § 4.1.2 Var Expressions
- § 4.1.3 List Expressions
- § 4.1.4 Path Values Expressions
- § 4.1.5 Exists Expressions
- § 4.1.6 If Expressions
- § 4.2.1 Distinct Expressions
- § 4.2.2 Intersection Expressions
- § 4.2.3 Concat Expressions
- § 4.2.4 Remove Expressions
- § 4.2.5 Filter Shape Expressions
- § 4.2.6 Limit Expressions
- § 4.2.7 Offset Expressions
- § 4.2.8 OrderBy Expressions
- § 4.3.1 FlatMap Expressions
- § 4.3.2 FindFirst Expressions
- § 4.3.3 MatchAll Expressions
- § 4.4.1 Count Expressions
- § 4.4.2 Min Expressions
- § 4.4.3 Max Expressions
- § 4.4.4 Sum Expressions
- § 4.5.1 InstancesOf Expressions
- § 4.5.2 Nodes Matching Expressions
- § 4.5.3 ConformsToShape Expressions (2)
- § 5. SPARQL Functions
- § 6.1 Custom Named Parameter Functions
- § 6.2 Custom List Parameter Functions
- § 6.3 Arg Expressions
- § 7.2 sh:nodeByExpression (2)
- § 8. Dynamic SHACL

Permalink

**Referenced in:**

- § 1.1 Terminology

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3. Node Expression Syntax
- § 3.1.1 IRI Expressions (2)
- § 4.1.1 Empty Expressions
- § 4.1.3 List Expressions (2)
- § 4.1.4 Path Values Expressions
- § 6.1 Custom Named Parameter Functions (2) (3)
- § 6.2 Custom List Parameter Functions (2)
- § 7.2 sh:nodeByExpression (2)

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3. Node Expression Syntax
- § 3.1.2 Literal Expressions (2)
- § 4.1.3 List Expressions (2)
- § 4.4.1 Count Expressions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.1 Named Parameter Functions
- § 3.2.2 List Parameter Functions (2)
- § 3.4 The Shapes Graph
- § 4.2.1 Distinct Expressions
- § 4.2.2 Intersection Expressions
- § 4.2.4 Remove Expressions
- § 4.2.6 Limit Expressions
- § 4.2.7 Offset Expressions
- § 4.2.8 OrderBy Expressions
- § 4.4.2 Min Expressions
- § 4.4.3 Max Expressions
- § 4.4.4 Sum Expressions (2)
- § 4.5.1 InstancesOf Expressions
- § 4.5.2 Nodes Matching Expressions
- § 4.5.3 ConformsToShape Expressions (2)
- § 6.1 Custom Named Parameter Functions (2)
- § 6.2 Custom List Parameter Functions (2)
- § 8. Dynamic SHACL

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.2 List Parameter Functions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.1 Named Parameter Functions
- § 3.2.2 List Parameter Functions
- § 6.2 Custom List Parameter Functions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3. Node Expression Syntax

Permalink

**Referenced in:**

- § 1.1 Terminology

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.1 Named Parameter Functions
- § 3.2.2 List Parameter Functions (2)
- § 6.2 Custom List Parameter Functions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.1 Named Parameter Functions
- § 3.2.2 List Parameter Functions
- § 4. Node Expressions Library
- § 4.1.1 Empty Expressions
- § 4.1.2 Var Expressions
- § 4.1.3 List Expressions
- § 4.1.4 Path Values Expressions (2)
- § 4.1.5 Exists Expressions
- § 4.1.6 If Expressions
- § 4.2.1 Distinct Expressions
- § 4.2.2 Intersection Expressions
- § 4.2.3 Concat Expressions
- § 4.2.4 Remove Expressions
- § 4.2.5 Filter Shape Expressions
- § 4.2.6 Limit Expressions
- § 4.2.7 Offset Expressions
- § 4.2.8 OrderBy Expressions
- § 4.3.1 FlatMap Expressions
- § 4.3.2 FindFirst Expressions
- § 4.3.3 MatchAll Expressions
- § 4.4.1 Count Expressions
- § 4.4.2 Min Expressions
- § 4.4.3 Max Expressions
- § 4.4.4 Sum Expressions
- § 4.5.1 InstancesOf Expressions
- § 4.5.2 Nodes Matching Expressions
- § 6.2 Custom List Parameter Functions
- § 6.3 Arg Expressions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 4.2.1 Distinct Expressions
- § 4.2.2 Intersection Expressions
- § 4.2.4 Remove Expressions

Permalink

**Referenced in:**

- § 3. Node Expression Syntax
- § 3.1.3 Triple Term Expressions (2)

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 7.2 sh:nodeByExpression (2)

Permalink

**Referenced in:**

- § 1.3 Conformance

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 2. Getting started with Node Expressions
- § 3.4 The Shapes Graph
- § 4.2.5 Filter Shape Expressions
- § 4.3.2 FindFirst Expressions
- § 4.3.3 MatchAll Expressions
- § 4.5.2 Nodes Matching Expressions
- § 4.5.3 ConformsToShape Expressions
- § 7.2 sh:nodeByExpression

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 8. Dynamic SHACL (2)

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 7. Constraint Components
- § 7.1 sh:expression

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 2. Getting started with Node Expressions
- § 4.5.3 ConformsToShape Expressions
- § 7.1 sh:expression
- § 7.2 sh:nodeByExpression
- § 8. Dynamic SHACL
- § 8.2 Example: Dynamic Enumerations

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 7.1 sh:expression
- § 7.2 sh:nodeByExpression

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.2 List Parameter Functions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.1 Named Parameter Functions
- § 3.2.2 List Parameter Functions (2)
- § 4.1.4 Path Values Expressions
- § 4.5.3 ConformsToShape Expressions
- § 5. SPARQL Functions
- § 6.2 Custom List Parameter Functions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.3 Handling of Failures (2) (3) (4)
- § 4.5.3 ConformsToShape Expressions
- § 7.2 sh:nodeByExpression (2)

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.4 The Shapes Graph
- § 4.5.1 InstancesOf Expressions (2)
- § 4.5.2 Nodes Matching Expressions
- § 4.5.3 ConformsToShape Expressions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 2. Getting started with Node Expressions (2)
- § 4.1.2 Var Expressions
- § 4.1.4 Path Values Expressions (2)
- § 4.2.6 Limit Expressions
- § 4.2.7 Offset Expressions
- § 7.1 sh:expression
- § 7.2 sh:nodeByExpression
- § 8. Dynamic SHACL

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.1.1 IRI Expressions
- § 3.1.2 Literal Expressions
- § 3.1.3 Triple Term Expressions
- § 4.1.1 Empty Expressions
- § 4.1.2 Var Expressions
- § 4.1.3 List Expressions
- § 4.1.4 Path Values Expressions
- § 4.1.5 Exists Expressions
- § 4.1.6 If Expressions
- § 4.2.1 Distinct Expressions
- § 4.2.2 Intersection Expressions
- § 4.2.3 Concat Expressions
- § 4.2.4 Remove Expressions
- § 4.2.5 Filter Shape Expressions
- § 4.2.6 Limit Expressions
- § 4.2.7 Offset Expressions
- § 4.2.8 OrderBy Expressions
- § 4.3.1 FlatMap Expressions
- § 4.3.2 FindFirst Expressions
- § 4.3.3 MatchAll Expressions
- § 4.4.1 Count Expressions
- § 4.4.2 Min Expressions
- § 4.4.3 Max Expressions
- § 4.4.4 Sum Expressions
- § 4.5.1 InstancesOf Expressions
- § 4.5.2 Nodes Matching Expressions
- § 4.5.3 ConformsToShape Expressions
- § 5. SPARQL Functions
- § 6.3 Arg Expressions

Permalink

**Referenced in:**

- § 1.1 Terminology

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.2 List Parameter Functions (2)
- § 4.1.3 List Expressions (2) (3)
- § 4.2.2 Intersection Expressions (2)
- § 4.2.3 Concat Expressions (2)
- § 4.5.3 ConformsToShape Expressions
- § 6.2 Custom List Parameter Functions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3. Node Expression Syntax (2) (3)
- § 3.1.1 IRI Expressions (2)
- § 3.1.2 Literal Expressions (2)
- § 3.1.3 Triple Term Expressions (2)
- § 3.2.1 Named Parameter Functions
- § 3.2.2 List Parameter Functions (2) (3) (4)
- § 4.1.4 Path Values Expressions
- § 4.1.5 Exists Expressions
- § 4.1.6 If Expressions (2) (3) (4) (5)
- § 4.2.1 Distinct Expressions
- § 4.2.2 Intersection Expressions (2)
- § 4.2.3 Concat Expressions (2)
- § 4.2.4 Remove Expressions (2)
- § 4.2.5 Filter Shape Expressions
- § 4.2.6 Limit Expressions
- § 4.2.7 Offset Expressions
- § 4.2.8 OrderBy Expressions (2)
- § 4.3.1 FlatMap Expressions (2) (3)
- § 4.3.2 FindFirst Expressions
- § 4.3.3 MatchAll Expressions
- § 4.4.1 Count Expressions
- § 4.4.2 Min Expressions
- § 4.4.3 Max Expressions
- § 4.4.4 Sum Expressions
- § 5. SPARQL Functions
- § 6. Custom Node Expressions
- § 6.1 Custom Named Parameter Functions (2)
- § 6.2 Custom List Parameter Functions (2)
- § 7.1 sh:expression (2) (3) (4)
- § 7.2 sh:nodeByExpression (2) (3) (4) (5)
- § 8. Dynamic SHACL (2)

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3. Node Expression Syntax (2)
- § 3.1 Constant Node Expressions
- § 3.2.1 Named Parameter Functions
- § 3.2.2 List Parameter Functions
- § 4. Node Expressions Library
- § 6. Custom Node Expressions
- § 6.1 Custom Named Parameter Functions (2)
- § 6.2 Custom List Parameter Functions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 7.2 sh:nodeByExpression (2) (3) (4) (5) (6) (7) (8) (9) (10)

Permalink

**Referenced in:**

- § 1.1 Terminology

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 2. Getting started with Node Expressions
- § 3.1.1 IRI Expressions
- § 3.1.2 Literal Expressions
- § 3.1.3 Triple Term Expressions
- § 3.2.1 Named Parameter Functions (2) (3)
- § 3.2.2 List Parameter Functions (2) (3) (4) (5)
- § 3.3 Handling of Failures
- § 4.1.1 Empty Expressions
- § 4.1.2 Var Expressions
- § 4.1.3 List Expressions
- § 4.1.4 Path Values Expressions (2)
- § 4.1.5 Exists Expressions
- § 4.1.6 If Expressions (2) (3)
- § 4.2.1 Distinct Expressions (2)
- § 4.2.2 Intersection Expressions (2)
- § 4.2.3 Concat Expressions (2) (3)
- § 4.2.4 Remove Expressions (2) (3)
- § 4.2.5 Filter Shape Expressions (2)
- § 4.2.6 Limit Expressions (2)
- § 4.2.7 Offset Expressions (2)
- § 4.2.8 OrderBy Expressions (2) (3)
- § 4.3.1 FlatMap Expressions (2) (3)
- § 4.3.2 FindFirst Expressions (2)
- § 4.3.3 MatchAll Expressions (2)
- § 4.4.1 Count Expressions (2)
- § 4.4.2 Min Expressions (2)
- § 4.4.3 Max Expressions (2)
- § 4.4.4 Sum Expressions (2)
- § 4.5.1 InstancesOf Expressions (2)
- § 4.5.2 Nodes Matching Expressions (2)
- § 4.5.3 ConformsToShape Expressions (2)
- § 6.1 Custom Named Parameter Functions
- § 6.2 Custom List Parameter Functions
- § 6.3 Arg Expressions
- § 7.1 sh:expression
- § 7.2 sh:nodeByExpression

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 6.1 Custom Named Parameter Functions (2) (3) (4) (5) (6)
- § 8. Dynamic SHACL (2)

Permalink

**Referenced in:**

- § 1.1 Terminology

Permalink

**Referenced in:**

- § 1.1 Terminology

Permalink

**Referenced in:**

- § 9. Security and Privacy Considerations

Permalink

**Referenced in:**

- § 7.2 sh:nodeByExpression

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 4.2.2 Intersection Expressions
- § 4.5.1 InstancesOf Expressions
- § 6.1 Custom Named Parameter Functions
- § 6.2 Custom List Parameter Functions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.2.2 List Parameter Functions (2) (3) (4)
- § 4.1.3 List Expressions
- § 4.2.2 Intersection Expressions
- § 4.2.3 Concat Expressions
- § 4.5.3 ConformsToShape Expressions
- § 8. Dynamic SHACL

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 4.1.4 Path Values Expressions

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 6.1 Custom Named Parameter Functions
- § 6.2 Custom List Parameter Functions

Permalink

**Referenced in:**

- § 1.1 Terminology

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 2. Getting started with Node Expressions (2)
- § 3.4 The Shapes Graph
- § 4.2.5 Filter Shape Expressions (2)
- § 4.3.2 FindFirst Expressions (2)
- § 4.3.3 MatchAll Expressions (2)
- § 4.5.2 Nodes Matching Expressions
- § 4.5.3 ConformsToShape Expressions (2) (3)
- § 7.1 sh:expression (2) (3)
- § 7.2 sh:nodeByExpression

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 2. Getting started with Node Expressions (2)
- § 3.4 The Shapes Graph (2) (3) (4)
- § 6.1 Custom Named Parameter Functions (2)
- § 6.2 Custom List Parameter Functions (2) (3)

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 2. Getting started with Node Expressions (2)

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.4 The Shapes Graph (2)
- § 4.5.3 ConformsToShape Expressions
- § 8. Dynamic SHACL

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 7.1 sh:expression
- § 7.2 sh:nodeByExpression (2)

Permalink

**Referenced in:**

- § 1.1 Terminology

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 4.1.2 Var Expressions
- § 4.1.4 Path Values Expressions (2)
- § 4.1.5 Exists Expressions
- § 4.1.6 If Expressions (2) (3)
- § 4.2.1 Distinct Expressions
- § 4.2.2 Intersection Expressions
- § 4.2.3 Concat Expressions
- § 4.2.4 Remove Expressions (2)
- § 4.2.5 Filter Shape Expressions (2)
- § 4.2.6 Limit Expressions (2)
- § 4.2.7 Offset Expressions (2)
- § 4.2.8 OrderBy Expressions (2) (3)
- § 4.3.1 FlatMap Expressions (2)
- § 4.3.2 FindFirst Expressions (2)
- § 4.3.3 MatchAll Expressions (2)
- § 4.4.1 Count Expressions
- § 4.4.2 Min Expressions
- § 4.4.3 Max Expressions
- § 4.4.4 Sum Expressions
- § 4.5.1 InstancesOf Expressions
- § 4.5.2 Nodes Matching Expressions
- § 4.5.3 ConformsToShape Expressions
- § 6.1 Custom Named Parameter Functions (2) (3) (4) (5) (6) (7)
- § 6.2 Custom List Parameter Functions (2)
- § 6.3 Arg Expressions
- § 7.1 sh:expression (2)
- § 7.2 sh:nodeByExpression (2) (3)

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 4.1.4 Path Values Expressions (2)
- § 7.1 sh:expression (2) (3)
- § 7.2 sh:nodeByExpression (2) (3) (4)

Permalink

**Referenced in:**

- § 1.1 Terminology
- § 3.1.1 IRI Expressions
- § 3.1.2 Literal Expressions
- § 3.1.3 Triple Term Expressions
- § 3.2.2 List Parameter Functions (2) (3)
- § 4. Node Expressions Library
- § 4.1.3 List Expressions (2)
- § 4.1.4 Path Values Expressions (2)
- § 4.1.5 Exists Expressions
- § 4.1.6 If Expressions (2) (3)
- § 4.2.1 Distinct Expressions
- § 4.2.2 Intersection Expressions (2)
- § 4.2.3 Concat Expressions (2)
- § 4.2.4 Remove Expressions (2)
- § 4.2.5 Filter Shape Expressions (2)
- § 4.2.6 Limit Expressions
- § 4.2.7 Offset Expressions
- § 4.2.8 OrderBy Expressions (2)
- § 4.3.1 FlatMap Expressions (2)
- § 4.3.2 FindFirst Expressions (2)
- § 4.3.3 MatchAll Expressions (2)
- § 4.4.1 Count Expressions
- § 4.4.2 Min Expressions
- § 4.4.3 Max Expressions
- § 4.4.4 Sum Expressions
- § 4.5.2 Nodes Matching Expressions
- § 4.5.3 ConformsToShape Expressions
- § 6.1 Custom Named Parameter Functions
- § 6.2 Custom List Parameter Functions
- § 7.2 sh:nodeByExpression

Permalink

**Referenced in:**

- § 2. Getting started with Node Expressions

Permalink

**Referenced in:**

- § 4.4.4 Sum Expressions

Permalink

**Referenced in:**

- § 4.4.3 Max Expressions

Permalink

**Referenced in:**

- § 4.4.2 Min Expressions

Permalink

**Referenced in:**

- § 4.2.8 OrderBy Expressions

Permalink

**Referenced in:**

- § 4.4.4 Sum Expressions
