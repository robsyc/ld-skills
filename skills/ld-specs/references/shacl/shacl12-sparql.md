---
title: "SHACL 1.2 SPARQL-Related Features"
source: https://www.w3.org/TR/shacl12-sparql/
family: shacl
version: "1.2"
status: W3C Working Draft
spec_date: 2026-10-22
fetched: 2026-11-02
---

# SHACL 1.2 SPARQL-Related Features

> SPARQL-based constraints and targets.

## Contents

- Abstract
- SHACL Specifications
- 1 Introduction
  - 1.1 Terminology
  - 1.2 Document Conventions
  - 1.3 Conformance
- 2 Prefix Declarations for SPARQL Queries
- 3 SPARQL-based Constraints
  - 3.1 An Example SPARQL-based Constraint
  - 3.2 Syntax of SPARQL-based Constraints
  - 3.3 Validation with SPARQL-based Constraints
    - 3.3.1 Pre-bound variable $this in SPARQL Constraints
    - 3.3.2 Mapping of Solution Bindings to Result Properties
- 4 SPARQL-based Constraint Components
  - 4.1 An Example SPARQL-based Constraint Component
  - 4.2 Syntax of SPARQL-based Constraint Components
    - 4.2.1 Parameter Declarations (sh:parameter)
    - 4.2.2 Label Templates (sh:labelTemplate)
    - 4.2.3 Validators
  - 4.3 Validation with SPARQL-based Constraint Components
- 5 Annotation Properties
- 6 SPARQL-based Node Expressions
  - 6.1 Select Expressions
  - 6.2 SPARQL Expr Expressions
- 7 Declaring SPARQL Functions based on Node Expressions
  - 7.1 Example SPARQL Function using general Node Expressions
  - 7.2 Example SPARQL Functions using SPARQL-based Node Expressions
  - 7.3 Evaluation of Custom SPARQL Functions
- 8 Appendix
- A Pre-binding of Variables in SPARQL Queries
- B Summary of Syntax Rules
- C Potential SPARQL Definitions of SHACL Core Constraint Validators
  - C.1 sh:targetClass
  - C.2 sh:targetSubjectsOf
  - C.3 sh:targetObjectsOf
  - C.4 sh:class
  - C.5 sh:nodeKind
  - C.6 sh:minExclusive (etc)
  - C.7 sh:minLength
  - C.8 sh:maxLength
  - C.9 sh:pattern
  - C.10 sh:disjoint
  - C.11 sh:lessThan
  - C.12 sh:lessThanOrEquals
- D Security and Privacy Considerations
- F Changes between the original SHACL specifications and SHACL 1.2 SPARQL-Related Features
- G References
  - G.1 Normative references
  - G.2 Informative references

---

### Abstract

This document defines SPARQL-related features of the SHACL Shapes Constraint Language.
While the Core part of SHACL defines the basic syntax of shapes and the most common constraint components
supported by SHACL, the SPARQL-related features extend the expressiveness of Core by means of SPARQL.
In particular, this document defines how constraints and constraint components can be defined using SPARQL.
Furthermore, this document introduces SPARQL-based node expressions that can be used to derive lists of nodes.
Finally, this document defines a declarative mechanism to define new SPARQL functions based on SHACL node expressions.

### SHACL Specifications

This specification is part of the SHACL 1.2 family of specifications. See the [SHACL 1.2 Overview](https://w3c.github.io/data-shapes/shacl12-overview/) for a more detailed introduction to them.

The specifications are as follows:

**Working Drafts:**

[SHACL 1.2 Core](https://www.w3.org/TR/shacl12-core/)

defines the Core of SHACL

[SHACL 1.2 Node Expressions](https://www.w3.org/TR/shacl12-node-expr/)

defines expressions used to derive focus nodes and value nodes in SHACL

[SHACL 1.2 SPARQL-Related Features](https://www.w3.org/TR/shacl12-sparql/)

defines SPARQL-related extensions of SHACL

[SHACL 1.2 Inference Rules](https://www.w3.org/TR/shacl12-inference-rules/)

defines SHACL's framework of rule-based inference

[SHACL 1.2 Profiling](https://www.w3.org/TR/shacl12-profiling/)

defines the use of SHACL for profiling data, including SHACL data

[SHACL 1.2 User Interfaces](https://www.w3.org/TR/shacl12-ui/)

defines SHACL's use for User Interface generation

[SPARQL 1.2 RL](https://www.w3.org/TR/sparql12-rl/)

defines a Datalog-style rules language for RDF that can be used with SHACL 1.2 Inference Rules

**Editor's Drafts:**

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
> Implementers can partially check their level of conformance with the above specifications by testing themselves
> with the test cases each presents, linked to in their metadata.
> Note, however, that passing all the tests in a test suite does not imply complete conformance to the specifications,
> it only implies that the implementation conforms to the aspects tested by the test suite.

### 1. Introduction

This document specifies the SPARQL-related features of the Shapes Constraint Language (SHACL).

#### 1.1 Terminology

Throughout this document, the following terminology is used.

The SPARQL-related features of SHACL defined in this document are sometimes called SHACL-SPARQL.

Terminology that is linked to portions of RDF 1.2 Concepts and Abstract Syntax is used in SHACL-SPARQL as defined there.
Terminology that is linked to portions of SPARQL 1.2 Query Language is used in SHACL-SPARQL as defined there.
Terminology that is linked to portions of SHACL 1.2 Core is used in SHACL-SPARQL as defined there.
A single linkage is sufficient to provide a definition for all occurrences of a particular term in this document.

Definitions are complete within this document, i.e., if there is no rule to
make some situation true in this document then the situation is false.

Basic RDF Terminology

This document uses the terms *[RDF graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph)*, *[RDF triple](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple)*, *[IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri)*, *[literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal)*, *[blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node)*, *[node](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-node)* of an RDF graph, *[datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype)*, *[reifier](https://www.w3.org/TR/rdf12-concepts/#dfn-reifier)*, *[RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term)*, and *[subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject)*, *[predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate)*, and *[object](https://www.w3.org/TR/rdf12-concepts/#dfn-object)* of RDF triples
as defined in RDF 1.2 Concepts and Abstract Syntax [rdf12-concepts].

Basic SHACL Terminology

This document uses the terms *[focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node)*, *[value](https://www.w3.org/TR/shacl12-core/#dfn-value)*, *[value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node)*, *[constraint](https://www.w3.org/TR/shacl12-core/#dfn-constraint)*, *[constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component)*, *[parameter](https://www.w3.org/TR/shacl12-core/#dfn-parameter)*, *[mandatory parameter](https://www.w3.org/TR/shacl12-core/#dfn-mandatory-parameter)*, *[optional parameter](https://www.w3.org/TR/shacl12-core/#dfn-optional-parameter)*, *[parameter value](https://www.w3.org/TR/shacl12-core/#dfn-parameter-value)*, *[shape](https://www.w3.org/TR/shacl12-core/#dfn-shape)*, *[node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape)*, *[property shape](https://www.w3.org/TR/shacl12-core/#dfn-property-shape)*, *[SHACL property path](https://www.w3.org/TR/shacl12-core/#dfn-shacl-property-path)*, *[SPARQL property path](https://www.w3.org/TR/shacl12-core/#dfn-sparql-property-path)*, *[data graph](https://www.w3.org/TR/shacl12-core/#dfn-data-graph)*, *[shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph)*, *[target](https://www.w3.org/TR/shacl12-core/#dfn-target)*, *[validator](https://www.w3.org/TR/shacl12-core/#dfn-validators)*, *[node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression)*, *[node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function)*, *[function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name)*, *[output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes)*, *[evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure)*, *[focus graph](https://www.w3.org/TR/shacl12-core/#dfn-focus-graph)*, *[conform](https://www.w3.org/TR/shacl12-core/#dfn-conform)*, *[failure](https://www.w3.org/TR/shacl12-core/#dfn-failure)*, *[validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result)*, *[SHACL instance](https://www.w3.org/TR/shacl12-core/#dfn-shacl-instance)*, *[SHACL subclass](https://www.w3.org/TR/shacl12-core/#dfn-shacl-subclass)*, *[SHACL superclass](https://www.w3.org/TR/shacl12-core/#dfn-shacl-superclass)*, *[SHACL type](https://www.w3.org/TR/shacl12-core/#dfn-shacl-type)*, *[well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed)*, *[ill-formed](https://www.w3.org/TR/shacl12-core/#dfn-ill-formed)*,
as defined in the SHACL 1.2 Core specification [shacl12-core].

Binding, Solution

A *binding* is a pair ([variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable), [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term)), consistent with the term's use in [sparql12-query].
A *solution* is a set of bindings where each variable must be unique.
Informally, a solution is often understood as one row in the body of the result table of a SPARQL query.

#### 1.2 Document Conventions

The syntax of SHACL is RDF.
The examples in this document use Turtle [rdf12-turtle].
Other RDF serializations such as RDF/XML may be used in practice.
The reader should be familiar with basic RDF concepts [rdf12-concepts] such as triples and with SPARQL [sparql12-query].

Within this document, the following namespace prefix bindings are used:

| Prefix    | Namespace                                     |
| --------- | --------------------------------------------- |
| `owl:`    | `http://www.w3.org/2002/07/owl#`              |
| `rdf:`    | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs:`   | `http://www.w3.org/2000/01/rdf-schema#`       |
| `sh:`     | `http://www.w3.org/ns/shacl#`                 |
| `xsd:`    | `http://www.w3.org/2001/XMLSchema#`           |
| `ex:`     | `http://example.com/ns#`                      |
| `shnex:`  | `http://www.w3.org/ns/shacl-node-expr#`       |
| `sparql:` | `http://www.w3.org/ns/sparql#`                |

Within this document, the following JSON-LD context is used:

```
{
  "@context": {
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "sh": "http://www.w3.org/ns/shacl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "http://example.com/ns#",
    "shnex": "http://www.w3.org/ns/shacl-node-expr#",
    "sparql": "http://www.w3.org/ns/sparql#"
  }
}
```

Note that the URI of the graph defining the SHACL vocabulary itself is equivalent to
the namespace above, i.e. it includes the `#`.
References to the SHACL vocabulary, e.g. via `owl:imports` should include the `#`.

Throughout the document, color-coded boxes containing RDF graphs in Turtle will appear.
These fragments of Turtle documents use the prefix bindings given above.

\# This box represents an input shapes graph

<s> ex:p <o> .

```
// This box represents an input shapes graph
```

```
{
	"@id": "s",
	"ex:p": {
		"@id": "o"
	}
}
```

\# This box represents an input data graph.

```
{
	"@graph": [
	]
}
```

\# This box represents an output results graph

```
// This box represents an output results graph
```

```
{}
```

SHACL Definitions appear in blue boxes:

SPARQL or TEXTUAL DEFINITIONS

```
# This box contains SPARQL or textual definitions.
```

Grey boxes such as this include syntax rules that apply to the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph).

SPARQL variables using the `$` marker represent external bindings that are pre-bound or, in the case of `$PATH`, substituted in the SPARQL query before execution (as explained in 3.3 Validation with SPARQL-based Constraints (§3.3)).

`true` denotes the RDF term `"true"^^xsd:boolean`. `false` denotes the RDF term `"false"^^xsd:boolean`.

#### 1.3 Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, *OPTIONAL*, and *SHOULD* in this document
are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all
capitals, as shown here.

This document defines the **SHACL-SPARQL** language that extends SHACL Core.
This specification describes conformance criteria for:

- **SHACL-SPARQL validation processors** as processors that support SHACL validation using 3. SPARQL-based Constraints (§3) and 4. SPARQL-based Constraint Components (§4) (identified as `SPARQLValidation` in the test suite).
  Such processors *MAY* additionally support 5. Annotation Properties (§5);
  processors that do *MUST* follow the rules of that section.
- **SPARQL node expression processors** as processors that can evaluate 6. SPARQL-based Node Expressions (§6) (`SPARQLNodeExpr` in the test suite)
- **SPARQL custom function processors** as processors that can evaluate 7. Declaring SPARQL Functions based on Node Expressions (§7) (`SPARQLCustomFunctions` in the test suite)

Also see the discussion of well-formedness in the [Conformance section of SHACL Core](https://www.w3.org/TR/shacl12-core/#conformance).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The SHACL 1.2 Inference Rules specification [shacl12-inference-rules] defines additional SPARQL-based features for SHACL.

### 2. Prefix Declarations for SPARQL Queries

This section introduces the mechanisms that are used throughout this document to declare namespace prefixes
for SPARQL queries.

A [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) may include declarations of namespace prefixes so that these prefixes can be used to abbreviate the SPARQL queries derived from the same shapes graph.
The syntax of such prefix declarations is illustrated by the following example.
> **Example:**
>
> Example 1: Prefix declarations in a shapes graph
>
> ex:
> sh:declare [
> sh:prefix "ex" ;
> sh:namespace "http://example.com/ns#"^^xsd:anyURI ;
> ] ;
> sh:declare [
> sh:prefix "schema" ;
> sh:namespace "http://schema.org/" ;
> ] ;
> a sh:ShapesGraph ; # Optional
> owl:imports sh: . # Optional
>
> ```
> {
> 	"@id": "http://example.com/ns#",
> 	"@type": "sh:ShapesGraph",
> 	"owl:imports": {
> 		"@id": "http://www.w3.org/ns/shacl#"
> 	},
> 	"sh:declare": [
> 		{
> 			"sh:namespace": {
> 				"@type": "xsd:anyURI",
> 				"@value": "http://example.com/ns#"
> 			},
> 			"sh:prefix": "ex"
> 		},
> 		{
> 			"sh:namespace": "http://schema.org/",
> 			"sh:prefix": "schema"
> 		}
> 	]
> }
> ```

[IRIs](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that have [values](https://www.w3.org/TR/shacl12-core/#dfn-value) for both `sh:prefix` and `sh:namespace` are called *prefix declarations*.
The SHACL vocabulary includes the class `sh:PrefixDeclaration` as type for such prefix declarations although no `rdf:type` triple is required for them. Prefix declarations have exactly one value for the property `sh:prefix`. The values of `sh:prefix` are [literals](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) of datatype `xsd:string`. Prefix declarations have exactly one value for the property `sh:namespace`. The values of `sh:namespace` are [literals](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) of datatype `xsd:anyURI` or `xsd:string`. Such a pair of values specifies a single mapping of a prefix to a namespace. The [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of the property `sh:declare` are prefix declarations.

The recommended [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) for values of `sh:declare` is the IRI of the named graph containing the shapes that use the prefixes.
These IRIs are often declared as an instance of `sh:ShapesGraph` or `owl:Ontology`, but this is not required.

Among others, Prefix declarations can be used by SPARQL-based constraints,
the [validators](https://www.w3.org/TR/shacl12-core/#dfn-validators) of §4 SPARQL-based Constraint Components, §6 SPARQL-based Node Expressions, and [SPARQL-based inference rules](https://www.w3.org/TR/shacl12-inference-rules/#SPARQLRule).
These nodes can use the property `sh:prefixes` to specify a set of prefix mappings.
An example use of the `sh:prefixes` property can be found in this example (§3.1).

The values of `sh:prefixes` are either [IRIs](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node). A SHACL processor collects a set of prefix mappings as the union of all
individual prefix mappings that are [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of the [SPARQL property path](https://www.w3.org/TR/shacl12-core/#dfn-sparql-property-path) `sh:prefixes/(^owl:versionIRI)?/(owl:imports/(^owl:versionIRI)?)*/sh:declare` of the SPARQL-based constraint, [validator](https://www.w3.org/TR/shacl12-core/#dfn-validators) or SPARQL-based node expression (§6).
The `(^owl:versionIRI)?` elements support graphs that are referenced by their [`owl:versionIRI`](https://www.w3.org/TR/owl2-syntax/#Ontology_IRI_and_Version_IRI),
either directly as a value of `sh:prefixes` or via `owl:imports`:
they navigate from the version IRI to the shapes graph IRI before the prefix declarations are collected
and further `owl:imports` are followed. If such a collection of prefix declarations contains multiple different namespaces for the same [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:prefix`,
then the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) is [ill-formed](https://www.w3.org/TR/shacl12-core/#dfn-ill-formed). (Note that SHACL processors *MAY* ignore prefix declarations that are never reached).

If a SPARQL-based constraint, [validator](https://www.w3.org/TR/shacl12-core/#dfn-validators) or SPARQL-based node expression (§6) has no [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for `sh:prefixes` then the SHACL processor uses those prefix declarations from the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) that are [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:declare` at a [SHACL instance](https://www.w3.org/TR/shacl12-core/#dfn-shacl-instance) of `owl:Ontology`, `sh:DataGraph`, `sh:ShapesGraph`,
or `sh:RulesGraph` (which is a subclass of `sh:ShapesGraph`).

A SHACL processor transforms the values of `sh:select` (and similar properties such as `sh:ask` and `sh:construct`)
into SPARQL by prepending [`PREFIX`](https://www.w3.org/TR/sparql12-query/#rPrefixDecl) declarations
for all prefix mappings.
Each value of `sh:prefix` is turned into the `PNAME_NS`, while each value of `sh:namespace` is turned
into the `IRIREF` in the `PREFIX` declaration.
For the example shapes graph above, a SHACL-SPARQL processor would produce lines such as `PREFIX ex: <http://example.com/ns#>`.
The SHACL-SPARQL processor *MUST* produce a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) if the resulting query string cannot be parsed into a valid SPARQL 1.2 query.

In the rest of this document, the `sh:prefixes` statements may have been omitted for brevity.

### 3. SPARQL-based Constraints

SHACL-SPARQL supports a [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) that can be used to express restrictions based on a SPARQL SELECT query.

Constraint Component IRI: `sh:SPARQLConstraintComponent`

Parameters:

| Property    | Summary                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `sh:sparql` | A SPARQL-based constraint declaring the SPARQL query to evaluate. |

The syntax rules (§3.2) and validation process (§3.3) for SPARQL-based constraints are defined in the rest of this section.

#### 3.1 An Example SPARQL-based Constraint

*This section is non-normative.*

The following example illustrates the syntax of a SPARQL-based constraint.
> **Example:**
>
> Example 2: A SPARQL-based constraint
>
> ex:LanguageExampleShape
> a sh:NodeShape ;
> sh:targetClass ex:Country ;
> sh:sparql [
> a sh:SPARQLConstraint ; # This triple is optional
> sh:message "Values are literals with German language tag." ;
> sh:prefixes ex: ;
> sh:select """
> SELECT $this (ex:germanLabel AS ?path) ?value
> WHERE {
> $this ex:germanLabel ?value .
> FILTER (!isLiteral(?value) || !langMatches(lang(?value), "de"))
> }
> """ ;
> ] .
>
> ex:
> sh:declare [] . # See prefix declarations
>
> ```
> {
> 	"@graph": [
> 		{
> 			"@id": "ex:LanguageExampleShape",
> 			"@type": "sh:NodeShape",
> 			"sh:sparql": {
> 				"@type": "sh:SPARQLConstraint",
> 				"sh:message": "Values are literals with German language tag.",
> 				"sh:prefixes": {
> 					"@id": "http://example.com/ns#"
> 				},
> 				"sh:select": "\n\t\t\tSELECT $this (ex:germanLabel AS ?path) ?value\n\t\t\tWHERE {\n\t\t\t\t$this ex:germanLabel ?value .\n\t\t\t\tFILTER (!isLiteral(?value) || !langMatches(lang(?value), \"de\"))\n\t\t\t}\n\t\t\t"
> 			},
> 			"sh:targetClass": {
> 				"@id": "ex:Country"
> 			}
> 		},
> 		{
> 			"@id": "http://example.com/ns#",
> 			"sh:declare": {
> 				"@id": "_:b1"
> 			}
> 		}
> 	]
> }
> ```
>
> The target of the shape above includes all [SHACL instances](https://www.w3.org/TR/shacl12-core/#dfn-shacl-instance) of `ex:Country`.
> For those nodes (represented by the variable `this`), the SPARQL query walks through the values of `ex:germanLabel` and verifies that they are literals with a German language code.
>
> ex:ValidCountry a ex:Country ;
> ex:germanLabel "Spanien"@de .
>
> ex:InvalidCountry a ex:Country ;
> ex:germanLabel "Spain"@en .
>
> ```
> {
> 	"@graph": [
> 		{
> 			"@id": "ex:InvalidCountry",
> 			"@type": "ex:Country",
> 			"ex:germanLabel": {
> 				"@language": "en",
> 				"@value": "Spain"
> 			}
> 		},
> 		{
> 			"@id": "ex:ValidCountry",
> 			"@type": "ex:Country",
> 			"ex:germanLabel": {
> 				"@language": "de",
> 				"@value": "Spanien"
> 			}
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
> sh:focusNode ex:InvalidCountry ;
> sh:resultPath ex:germanLabel ;
> sh:value "Spain"@en ;
> sh:sourceConstraintComponent sh:SPARQLConstraintComponent ;
> sh:sourceShape ex:LanguageExampleShape ;
> # ...
> ]
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
> 		"sh:focusNode": {
> 			"@id": "ex:InvalidCountry"
> 		},
> 		"sh:resultPath": {
> 			"@id": "ex:germanLabel"
> 		},
> 		"sh:resultSeverity": {
> 			"@id": "sh:Violation"
> 		},
> 		"sh:sourceConstraintComponent": {
> 			"@id": "sh:SPARQLConstraintComponent"
> 		},
> 		"sh:sourceShape": {
> 			"@id": "ex:LanguageExampleShape"
> 		},
> 		"sh:value": {
> 			"@language": "en",
> 			"@value": "Spain"
> 		}
> 	}
> }
> ```

The SPARQL query returns result set solutions for all bindings of the variable `value` that violate the constraint.
There is a [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) for each solution in that result set, applying the mapping rules (§3.3) explained later.
In this example, each [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) will have the binding for the variable `this` as the `sh:focusNode`, `ex:germanLabel` as `sh:resultPath` and the violating value as `sh:value`.

The following example illustrates a similar scenario as above, but with a [property shape](https://www.w3.org/TR/shacl12-core/#dfn-property-shape).
> **Example:**
>
> Example 3: A SPARQL-based constraint in a property shape
>
> ex:LanguageExamplePropertyShape
> a sh:PropertyShape ;
> sh:targetClass ex:Country ;
> sh:path ex:germanLabel ;
> sh:sparql [
> a sh:SPARQLConstraint ; # This triple is optional
> sh:message "Values are literals with German language tag." ;
> sh:prefixes ex: ;
> sh:select """
> SELECT $this ?value
> WHERE {
> $this $PATH ?value .
> FILTER (!isLiteral(?value) || !langMatches(lang(?value), "de"))
> }
> """ ;
> ] .
>
> ex:
> sh:declare [] . # See prefix declarations
>
> ```
> {
> 	"@graph": [
> 		{
> 			"@id": "ex:LanguageExamplePropertyShape",
> 			"@type": "sh:PropertyShape",
> 			"sh:path": {
> 				"@id": "ex:germanLabel"
> 			},
> 			"sh:sparql": {
> 				"@type": "sh:SPARQLConstraint",
> 				"sh:message": "Values are literals with German language tag.",
> 				"sh:prefixes": {
> 					"@id": "http://example.com/ns#"
> 				},
> 				"sh:select": "\n\t\t\tSELECT $this ?value\n\t\t\tWHERE {\n\t\t\t\t$this $PATH ?value .\n\t\t\t\tFILTER (!isLiteral(?value) || !langMatches(lang(?value), \"de\"))\n\t\t\t}\n\t\t\t"
> 			},
> 			"sh:targetClass": {
> 				"@id": "ex:Country"
> 			}
> 		},
> 		{
> 			"@id": "http://example.com/ns#",
> 			"sh:declare": {
> 				"@id": "_:b1"
> 			}
> 		}
> 	]
> }
> ```

#### 3.2 Syntax of SPARQL-based Constraints

Shapes may have values for the property `sh:sparql`, and these values are either [IRIs](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node). These values are called *SPARQL-based constraints*.

SPARQL-based constraints have exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:select`. The value of `sh:select` is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) of datatype `xsd:string`. The class `sh:SPARQLConstraint` is defined in the SHACL vocabulary and may be used as the [type](https://www.w3.org/TR/vc-data-model-2.0/#dfn-type) of these constraints (although no type is required). Using the prefix handling rules (§2), the value of `sh:select` is a valid SPARQL 1.2 SELECT query. The SPARQL query derived from the value of `sh:select` [projects](https://www.w3.org/TR/sparql12-query/#selectproject) the variable `this` in the SELECT clause.

The following two properties are similar to their use in [shapes](https://www.w3.org/TR/shacl12-core/#dfn-shape):

SPARQL-based constraints may have values for the property `sh:message` and these are [literals](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype) `xsd:string`, `rdf:dirLangString`, `rdf:langString`, or `rdf:HTML`.
There should neither be more than one value for `sh:message` with the same language tag, nor multiple values with datatype `xsd:string`. SPARQL-based constraints may have at most one value for the property `sh:deactivated` and this value is a [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that must have either `true` or `false` as its (only) [output node](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes),
as for [shapes](https://www.w3.org/TR/shacl12-core/#deactivated). SPARQL-based constraints may have at most one value for the property `sh:severity` and this value is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri).

SELECT queries used in the context of [property shapes](https://www.w3.org/TR/shacl12-core/#dfn-property-shape) use a special variable named `PATH` as a placeholder for the path used by the shape.

The only legal use of the variable `PATH` in the SPARQL queries of SPARQL-based constraints and SELECT-based validators is in the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) position of a [triple pattern](https://www.w3.org/TR/sparql12-query/#QSynTriples). A query that uses the variable `PATH` in any other position is [ill-formed](https://www.w3.org/TR/shacl12-core/#dfn-ill-formed).

The variable `PATH` is only substituted for [property shapes](https://www.w3.org/TR/shacl12-core/#dfn-property-shape).
In the SPARQL queries of [node shapes](https://www.w3.org/TR/shacl12-core/#dfn-node-shape) it remains an unbound variable.

#### 3.3 Validation with SPARQL-based Constraints

This section explains the [validator](https://www.w3.org/TR/shacl12-core/#dfn-validators) of `sh:SPARQLConstraintComponent`.
Note that this validator only explains one possible implementation strategy, and
SHACL processors may choose alternative approaches as long as the outcome is equivalent.

TEXTUAL DEFINITION

Let `$sparql` be a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:sparql`.
If `$sparql` has a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) `expr` for the property `sh:deactivated` and `evalExpr(expr, data graph, focus node, {})` produces `true` as its only [output node](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes),
then the constraint is deactivated and there are no [validation results](https://www.w3.org/TR/shacl12-core/#dfn-validation-result).
Otherwise, execute the SPARQL query specified by the SPARQL-based constraint `$sparql` pre-binding the variable `this` as described in 3.3.1 Pre-bound variable $this in SPARQL Constraints (§3.3.1).
If the [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) is a [property shape](https://www.w3.org/TR/shacl12-core/#dfn-property-shape), then prior to execution *substitute* the variable `PATH` where it appears in the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) position of a [triple pattern](https://www.w3.org/TR/sparql12-query/#QSynTriples) with a valid SPARQL surface syntax string of the [SHACL property path](https://www.w3.org/TR/shacl12-core/#dfn-shacl-property-path) specified via `sh:path` at the [property shape](https://www.w3.org/TR/shacl12-core/#dfn-property-shape). There is one [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) for each solution that does not have `true` as the binding for the variable `failure`.
These [validation results](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) *MUST* have the property values explained in 3.3.2 Mapping of Solution Bindings to Result Properties (§3.3.2).
If `$sparql` has a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for `sh:severity` then the [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) *MUST* have that value as its (only) `sh:resultSeverity`.
A [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) *MUST* be produced if and only if one of the solutions has `true` as the binding for `failure`.

##### 3.3.1 Pre-bound variable $this in SPARQL Constraints

When the SPARQL queries of SPARQL-based constraints and the [validators](https://www.w3.org/TR/shacl12-core/#dfn-validators) of SPARQL-based constraint components are [processed](https://www.w3.org/TR/shacl12-core/#validation-definition),
the SHACL-SPARQL processor pre-binds values for the variable `$this` to the current [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node).

##### 3.3.2 Mapping of Solution Bindings to Result Properties

The property [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of the [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) nodes are derived by the following rules, through a combination of result solutions and the values of the constraint itself.
The rules are meant to be executed from top to bottom, so that the first bound value will be used.

| Property              | Production Rules                                                                                                                                                                                         |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sh:focusNode`        | The binding for the variable `this`                                                                                                                                                                      |
| `sh:resultPath`       | The binding for the variable `path`, if that is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) For results produced by a [property shape](https://www.w3.org/TR/shacl12-core/#dfn-property-shape), a [SHACL property path](https://www.w3.org/TR/shacl12-core/#dfn-shacl-property-path) that is equivalent to the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:path` of the shape |
| `sh:value`            | The binding for the variable `value` The [value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node)                                                                                                |
| `sh:resultMessage`    | The binding for the variable `message` For SPARQL-based constraints: The values of `sh:message` of the SPARQL-based constraint. For SPARQL-based constraint components: The values of `sh:message` of the [validator](https://www.w3.org/TR/shacl12-core/#dfn-validators) of the SPARQL-based constraint component. For SPARQL-based constraint components: The values of `sh:message` of the SPARQL-based constraint component. The default mechanisms for [declaring messages](https://www.w3.org/TR/shacl12-core/#message) at the shape or constraint apply otherwise. These message literals may include the names of any SELECT result variables via `{?varName}` or `{$varName}`. If the constraint is based on a SPARQL-based constraint component (§4), then the component's parameter names can also be used. These `{?varName}` and `{$varName}` blocks *SHOULD* be replaced with suitable string representations of the values of said variables. |
| `sh:sourceConstraint` | The SPARQL-based constraint, i.e. the value of `sh:sparql`                                                                          |

The variable `failure` is reserved and is not mapped to a result property:
as defined above, a solution that has `true` as the binding for `failure` produces a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) instead of a [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result).

### 4. SPARQL-based Constraint Components

SPARQL-based constraints provide a lot of flexibility
but may be hard to understand for some people or lead to repetition.
This section introduces SPARQL-based constraint components as a way to abstract the complexity of SPARQL
and to declare high-level reusable components similar to the [Core constraint components](https://www.w3.org/TR/shacl12-core/#core-components).
Such constraint components can be declared using the SHACL RDF vocabulary and thus shared and reused.

#### 4.1 An Example SPARQL-based Constraint Component

*This section is non-normative.*

The following example demonstrates how SPARQL can be used to specify new constraint components using the SHACL-SPARQL language.
The example implements [`sh:pattern` and `sh:flags`](https://www.w3.org/TR/shacl12-core/#PatternConstraintComponent) using a SPARQL ASK (§4.2.3.2) query to validate that each [value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node) matches a given regular expression.
Note that this is only an example implementation and should not be considered normative.
> **Example:**
>
> Example 4: Constraint component based on SPARQL
>
> sh:PatternConstraintComponent
> a sh:ConstraintComponent ;
> sh:parameter [
> sh:path sh:pattern ;
> ] ;
> sh:parameter [
> sh:path sh:flags ;
> sh:optional true ;
> ] ;
> sh:validator ex:hasPattern .
>
> ex:hasPattern
> a sh:SPARQLAskValidator ;
> sh:message "Value does not match pattern {$pattern}" ;
> sh:ask """
> ASK {
> FILTER (!isBlank($value) &&
> IF(bound($flags), regex(str($value), $pattern, $flags), regex(str($value), $pattern)))
> }""" .
>
> ```
> {
> 	"@graph": [
> 		{
> 			"@id": "ex:hasPattern",
> 			"@type": "sh:SPARQLAskValidator",
> 			"sh:ask": "\n\t\tASK {\n\t\t\tFILTER (!isBlank($value) &&\n\t\t\t\tIF(bound($flags), regex(str($value), $pattern, $flags), regex(str($value), $pattern)))\n\t\t}",
> 			"sh:message": "Value does not match pattern {$pattern}"
> 		},
> 		{
> 			"@id": "sh:PatternConstraintComponent",
> 			"@type": "sh:ConstraintComponent",
> 			"sh:parameter": [
> 				{
> 					"sh:path": {
> 						"@id": "sh:pattern"
> 					}
> 				},
> 				{
> 					"sh:optional": {
> 						"@type": "xsd:boolean",
> 						"@value": "true"
> 					},
> 					"sh:path": {
> 						"@id": "sh:flags"
> 					}
> 				}
> 			],
> 			"sh:validator": {
> 				"@id": "ex:hasPattern"
> 			}
> 		}
> 	]
> }
> ```

Once the constraint component has been declared, its parameters can be used in a shape as illustrated in the following example.
> **Example:**
>
> Example 5: Constraint component based on SPARQL
>
> ex:CaseInsensitiveSearch
> a sh:NodeShape ;
> sh:property [
> sh:path ex:code ;
> sh:pattern "^[A-Z]{3}[0-9]{2}$" ;
> sh:flags "i" ; # case-insensitive match
> ] .
>
> ```
> {
> 	"@id": "ex:CaseInsensitiveSearch",
> 	"@type": "sh:NodeShape",
> 	"sh:property": {
> 		"sh:flags": "i",
> 		"sh:path": {
> 			"@id": "ex:code"
> 		},
> 		"sh:pattern": "^[A-Z]{3}[0-9]{2}$"
> 	}
> }
> ```

Constraint components provide instructions to validation engines on how to identify and validate [constraints](https://www.w3.org/TR/shacl12-core/#dfn-constraint) within a [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape).
In general, if a [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) `S` has a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for a property `p`, and there is a [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) `C` that specifies `p` as a parameter, and `S` has values for all [mandatory parameters](https://www.w3.org/TR/shacl12-core/#dfn-mandatory-parameter) of `C`,
then the set of these parameter values (including the [optional parameters](https://www.w3.org/TR/shacl12-core/#dfn-optional-parameter)) declare a [constraint](https://www.w3.org/TR/shacl12-core/#dfn-constraint) and the validation engine uses a suitable [validator](https://www.w3.org/TR/shacl12-core/#dfn-validators) from `C` to perform the validation of this constraint.
In the example above, `sh:PatternConstraintComponent` declares the mandatory parameter `sh:pattern`,
the optional parameter `sh:flags`,
and a [validator](https://www.w3.org/TR/shacl12-core/#dfn-validators) that can be used to perform validation against either [node shapes](https://www.w3.org/TR/shacl12-core/#dfn-node-shape) or [property shapes](https://www.w3.org/TR/shacl12-core/#dfn-property-shape).

#### 4.2 Syntax of SPARQL-based Constraint Components

A *SPARQL-based constraint component* is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) that has [SHACL type](https://www.w3.org/TR/shacl12-core/#dfn-shacl-type) `sh:ConstraintComponent` in the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph).

The mechanism to declare new [constraint components](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) in this document is limited to those based on SPARQL.
However, the general syntax of declaring parameters and validators has been designed to also work for other extension languages such as JavaScript.

##### 4.2.1 Parameter Declarations (sh:parameter)

The [parameters](https://www.w3.org/TR/shacl12-core/#dfn-parameter) of a [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) are declared via the property `sh:parameter`.
The values of `sh:parameter` are called *parameter declarations*.
The class `sh:Parameter` may be used as [type](https://www.w3.org/TR/vc-data-model-2.0/#dfn-type) of parameter declarations but no such triple is required. Each parameter declaration has exactly one value for the property `sh:path`. At parameter declarations, the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:path` is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri).

The *local name* of an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) is defined as the longest [NCNAME](https://www.w3.org/TR/xml-names/#NT-NCName) at the end of the [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri), not immediately preceded by the first colon in the [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri).
The *parameter name* of a parameter declaration is defined as the local name of the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:path`.
To ensure that a correct mapping from parameters into SPARQL variables is possible, the following syntax rules apply:

Every parameter name is a valid [SPARQL VARNAME](https://www.w3.org/TR/sparql12-query/#rVARNAME). Parameter names must not be one of the following: `this`, `path`, `PATH`, `value`, `message`, `failure`. A constraint component where two or more parameter declarations use the same parameter names is [ill-formed](https://www.w3.org/TR/shacl12-core/#dfn-ill-formed).

The values of `sh:optional` must be literals with datatype `xsd:boolean`. A parameter declaration can have at most one value for the property `sh:optional`. If set to `true` then the parameter declaration declares an [optional parameter](https://www.w3.org/TR/shacl12-core/#dfn-optional-parameter). Every [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) has at least one non-optional parameter.

The class `sh:Parameter` is defined as a [SHACL subclass](https://www.w3.org/TR/shacl12-core/#dfn-shacl-subclass) of `sh:PropertyShape`,
and all properties that are applicable to property shapes may also be used for parameters.
This includes descriptive properties such as `sh:name` and `sh:description` but also constraint parameters such as `sh:class`. Shapes that do not [conform](https://www.w3.org/TR/shacl12-core/#dfn-conform) with the constraints declared for the parameters are [ill-formed](https://www.w3.org/TR/shacl12-core/#dfn-ill-formed). Some implementations *MAY* use these constraint parameters to prevent the execution of constraint components with invalid parameter values.

##### 4.2.2 Label Templates (sh:labelTemplate)

The property `sh:labelTemplate` can be used at any [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) to suggest how [constraints](https://www.w3.org/TR/shacl12-core/#dfn-constraint) could be rendered to humans. The values of `sh:labelTemplate` are [literals](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype) `xsd:string`, `rdf:langString` or `rdf:dirLangString` and
are called *label templates*.

*The remainder of this section is non-normative.*

Label templates can include the names of the parameters that are declared for the constraint component
using the syntaxes `{?varName}` or `{$varName}`,
where `varName` is the name of the parameter name.
At display time, these `{?varName}` and `{$varName}` blocks should be replaced with the actual parameter values.
There may be multiple label templates for the same subject, but they should not have the same language tags
and there should not be more than one template with datatype `xsd:string`.

##### 4.2.3 Validators

For every supported shape type (i.e., [property shape](https://www.w3.org/TR/shacl12-core/#dfn-property-shape) or [node shape](https://www.w3.org/TR/shacl12-core/#dfn-node-shape))
the constraint component declares a suitable [validator](https://www.w3.org/TR/shacl12-core/#dfn-validators).
For a given constraint, a validator is selected from the constraint component using the following rules, in order:

1. For [node shapes](https://www.w3.org/TR/shacl12-core/#dfn-node-shape), use one of the values of `sh:nodeValidator`, if present.
2. For [property shapes](https://www.w3.org/TR/shacl12-core/#dfn-property-shape), use one of the values of `sh:propertyValidator`, if present.
3. Otherwise, use one of the values of `sh:validator`.

If no suitable validator can be found, a SHACL-SPARQL processor ignores the constraint.

SHACL-SPARQL includes two types of validators, based on SPARQL SELECT (§4.2.3.1) (for `sh:nodeValidator` and `sh:propertyValidator`)
or SPARQL ASK (§4.2.3.2) queries (for `sh:validator`).

###### 4.2.3.1 SELECT-based Validators

[Validators](https://www.w3.org/TR/shacl12-core/#dfn-validators) with [SHACL type](https://www.w3.org/TR/shacl12-core/#dfn-shacl-type) `sh:SPARQLSelectValidator` are called *SELECT-based validators*. The values of `sh:nodeValidator` must be SELECT-based validators. The values of `sh:propertyValidator` must be SELECT-based validators. SELECT-based validators have exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:select`. The value of `sh:select` is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) of datatype `xsd:string`. Using the prefix handling rules (§2), the value of `sh:select` is a valid SPARQL 1.2 SELECT query. The SPARQL query derived from the value of `sh:select` [projects](https://www.w3.org/TR/sparql12-query/#selectproject) the variable `this` in its SELECT clause.

*The remainder of this section is non-normative.*

The following example illustrates the declaration of a constraint component based on a SPARQL SELECT query.
It is a generalized variation of the example from 3.1 An Example SPARQL-based Constraint (§3.1).
Where that SPARQL query included two constants: the specific property `ex:germanLabel` and the language tag `de`,
this example generalizes the constraint so that any property can be defined with a language tag. In practice, the constraint component is applied
by adding the parameter predicate(s) to a shape (e.g., ex:lang "de"), which a SHACL-SPARQL processor pre-binds to the corresponding SPARQL
variable(s) (e.g., `$lang`) before executing the SELECT validator.
Constraint components make it possible to generalize such scenarios, so that constants get pre-bound with [parameters](https://www.w3.org/TR/shacl12-core/#dfn-parameter).
This allows the query logic to be reused in multiple places, without having to write any new SPARQL.
> **Example:**
>
> Example 6: Constraint component based on SPARQL
>
> ex:LanguageConstraintComponentUsingSELECT
> a sh:ConstraintComponent ;
> rdfs:label "Language constraint component" ;
> sh:parameter [
> sh:path ex:lang ;
> sh:datatype xsd:string ;
> sh:minLength 2 ;
> sh:name "language" ;
> sh:description "The language tag, e.g. \\"de\\"." ;
> ] ;
> sh:labelTemplate "Values are literals with language \\"{$lang}\\"" ;
> sh:propertyValidator [
> a sh:SPARQLSelectValidator ;
> sh:message "Values are literals with language \\"{?lang}\\"" ;
> sh:select """
> SELECT DISTINCT $this ?value
> WHERE {
> $this $PATH ?value .
> FILTER (!isLiteral(?value) || !langMatches(lang(?value), $lang))
> }
> """
> ] .
>
> ```
> {
> 	"@id": "ex:LanguageConstraintComponentUsingSELECT",
> 	"@type": "sh:ConstraintComponent",
> 	"rdfs:label": "Language constraint component",
> 	"sh:labelTemplate": "Values are literals with language \"{$lang}\"",
> 	"sh:parameter": {
> 		"sh:datatype": {
> 			"@id": "xsd:string"
> 		},
> 		"sh:description": "The language tag, e.g. \"de\".",
> 		"sh:minLength": {
> 			"@type": "xsd:integer",
> 			"@value": "2"
> 		},
> 		"sh:name": "language",
> 		"sh:path": {
> 			"@id": "ex:lang"
> 		}
> 	},
> 	"sh:propertyValidator": {
> 		"@type": "sh:SPARQLSelectValidator",
> 		"sh:message": "Values are literals with language \"{?lang}\"",
> 		"sh:select": "\n\t\t\tSELECT DISTINCT $this ?value\n\t\t\tWHERE {\n\t\t\t\t$this $PATH ?value .\n\t\t\t\tFILTER (!isLiteral(?value) || !langMatches(lang(?value), $lang))\n\t\t\t}\n\t\t\t"
> 	}
> }
> ```

Once a constraint component has been declared (in a [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph)), its parameters can be used as illustrated in the following example. Any property shape
that includes `ex:lang` is interpreted as using `ex:LanguageConstraintComponentUsingSELECT` (binding `$lang` to that value).
> **Example:**
>
> Example 7: Shape declaration using ex:LanguageConstraintComponentUsingSELECT
>
> ex:LanguageExampleShape
> a sh:NodeShape ;
> sh:targetClass ex:Country ;
> sh:property [
> sh:path ex:germanLabel ;
> ex:lang "de" ;
> ] ;
> sh:property [
> sh:path ex:englishLabel ;
> ex:lang "en" ;
> ] .
>
> ```
> {
> 	"@id": "ex:LanguageExampleShape",
> 	"@type": "sh:NodeShape",
> 	"sh:property": [
> 		{
> 			"ex:lang": "de",
> 			"sh:path": {
> 				"@id": "ex:germanLabel"
> 			}
> 		},
> 		{
> 			"ex:lang": "en",
> 			"sh:path": {
> 				"@id": "ex:englishLabel"
> 			}
> 		}
> 	],
> 	"sh:targetClass": {
> 		"@id": "ex:Country"
> 	}
> }
> ```

The example shape above specifies the condition that all values of `ex:germanLabel` carry the language tag `de` while all values of `ex:englishLabel` have `en` as their language.
These details are specified via two property shapes that have values for the `ex:lang` parameter required by the constraint component.

###### 4.2.3.2 ASK-based Validators

Many constraint components are of the form in which all [value nodes](https://www.w3.org/TR/shacl12-core/#dfn-value-node) are tested individually against some boolean condition.
Writing SELECT queries for these becomes burdensome, especially if a constraint component can be
used for both [property shapes](https://www.w3.org/TR/shacl12-core/#dfn-property-shape) and [node shapes](https://www.w3.org/TR/shacl12-core/#dfn-node-shape).
SHACL-SPARQL provides an alternative, more compact syntax for validators based on ASK queries.

[Validators](https://www.w3.org/TR/shacl12-core/#dfn-validators) with [SHACL type](https://www.w3.org/TR/shacl12-core/#dfn-shacl-type) `sh:SPARQLAskValidator` are called *ASK-based validators*. The values of `sh:validator` must be ASK-based validators. ASK-based validators have exactly one value for the property `sh:ask`. The value of `sh:ask` must be a literal with datatype `xsd:string`. The value of `sh:ask` must be a valid SPARQL ASK query using the aforementioned prefix handling rules (§2).

*The remainder of this section is non-normative.*

The ASK queries return `true` if and only if a given [value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node) (represented by the pre-bound variable `value`) conforms to the constraint.

The following example declares a constraint component using an ASK query.
> **Example:**
>
> Example 8: Constraint component based on SPARQL
>
> ex:LanguageConstraintComponentUsingASK
> a sh:ConstraintComponent ;
> rdfs:label "Language constraint component" ;
> sh:parameter [
> sh:path ex:lang ;
> sh:datatype xsd:string ;
> sh:minLength 2 ;
> sh:name "language" ;
> sh:description "The language tag, e.g. \\"de\\"." ;
> ] ;
> sh:labelTemplate "Values are literals with language \\"{$lang}\\"" ;
> sh:validator ex:hasLang .
>
> ex:hasLang
> a sh:SPARQLAskValidator ;
> sh:message "Values are literals with language \\"{$lang}\\"" ;
> sh:ask """
> ASK {
> FILTER (isLiteral($value) && langMatches(lang($value), $lang))
> }
> """ .
>
> ```
> {
> 	"@graph": [
> 		{
> 			"@id": "ex:hasLang",
> 			"@type": "sh:SPARQLAskValidator",
> 			"sh:ask": "\n\t\tASK {\n\t\t\tFILTER (isLiteral($value) && langMatches(lang($value), $lang))\n\t\t}\n\t\t",
> 			"sh:message": "Values are literals with language \"{$lang}\""
> 		},
> 		{
> 			"@id": "ex:LanguageConstraintComponentUsingASK",
> 			"@type": "sh:ConstraintComponent",
> 			"rdfs:label": "Language constraint component",
> 			"sh:labelTemplate": "Values are literals with language \"{$lang}\"",
> 			"sh:parameter": {
> 				"sh:datatype": {
> 					"@id": "xsd:string"
> 				},
> 				"sh:description": "The language tag, e.g. \"de\".",
> 				"sh:minLength": {
> 					"@type": "xsd:integer",
> 					"@value": "2"
> 				},
> 				"sh:name": "language",
> 				"sh:path": {
> 					"@id": "ex:lang"
> 				}
> 			},
> 			"sh:validator": {
> 				"@id": "ex:hasLang"
> 			}
> 		}
> 	]
> }
> ```

Note that the validation condition implemented by an ASK query is "in the inverse direction" from its SELECT counterpart:
ASK queries return `true` for value nodes that conform to the constraint, while SELECT queries return those value nodes that do not conform.

#### 4.3 Validation with SPARQL-based Constraint Components

This section defines the [validator](https://www.w3.org/TR/shacl12-core/#dfn-validators) of SPARQL-based constraint components.
Note that this validator only explains one possible implementation strategy, and
SHACL processors may choose alternative approaches as long as the outcome is equivalent.

As the first step, a [validator](https://www.w3.org/TR/shacl12-core/#dfn-validators) *MUST* be selected based on the rules outlined
in 4.2.3 Validators (§4.2.3).
Then the following rules apply, producing a set of solutions of SPARQL queries:

- For ASK-based validators:
  For each [value node](https://www.w3.org/TR/shacl12-core/#dfn-value-node) `v` where the SPARQL ASK query returns `false` with `v` pre-bound to the variable `value`,
  create one solution consisting of the bindings
  (`$this`, [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node)) and (`$value`, `v`).
  Let `QS` be a list of these solutions.
- For SELECT-based validators:
  If the [shape](https://www.w3.org/TR/shacl12-core/#dfn-shape) is a [property shape](https://www.w3.org/TR/shacl12-core/#dfn-property-shape), then prior to execution substitute the variable `PATH` where it appears in the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) position of a [triple pattern](https://www.w3.org/TR/sparql12-query/#QSynTriples) with a valid SPARQL surface syntax string of the [SHACL property path](https://www.w3.org/TR/shacl12-core/#dfn-shacl-property-path) specified via `sh:path` at the [property shape](https://www.w3.org/TR/shacl12-core/#dfn-property-shape).
  Let `QS` be the solutions produced by executing the SPARQL query.

The SPARQL query executions above *MUST* pre-bind the variable `this` as described in 3.3.1 Pre-bound variable $this in SPARQL Constraints (§3.3.1).
In addition, each [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of a [parameter](https://www.w3.org/TR/shacl12-core/#dfn-parameter) of the [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) in the [constraint](https://www.w3.org/TR/shacl12-core/#dfn-constraint) *MUST* be pre-bound as a variable that has the parameter name as its name.

The production rules for the [validation results](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) are identical to those for SPARQL-based constraints,
using the solutions `QS` as produced above.

### 5. Annotation Properties

This section extends the general mechanism (§3.3.2) to produce [validation results](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) using §3 SPARQL-based Constraints or constraint components (§4).

Support for this feature is *OPTIONAL* for SHACL-SPARQL validation processors, see 1.3 Conformance (§1.3).
Processors that support it make it possible to inject *annotation properties* into the [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) nodes created for each solution produced by the `SELECT` queries of a
SPARQL-based [constraint](https://www.w3.org/TR/shacl12-core/#dfn-constraint) or [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component).
Any such annotation property needs to be declared via a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:resultAnnotation` at
the [subject](https://www.w3.org/TR/rdf12-concepts/#dfn-subject) of the `sh:select` or `sh:ask` [triple](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple).

The [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:resultAnnotation` are
called *result annotations* and are either [IRIs](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node).

Result annotations have the following properties:

| Property                | Summary and Syntax Rules                                                                                                                                                                                 |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sh:annotationProperty` | The property that shall be set. Each result annotation has exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:annotationProperty` and this value is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri). |
| `sh:annotationVarName`  | The name of the SPARQL variable to take the annotation values from. Each result annotation has at most 1 [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:annotationVarName` and this [value](https://www.w3.org/TR/shacl12-core/#dfn-value) is [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype) `xsd:string`. |
| `sh:annotationValue`    | Constant [RDF terms](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term) that shall be used as default values.                                                                                           |

For each solution of a `SELECT` result set, a SHACL processor that supports annotations
walks through the declared result annotations.
The mapping from result annotations to SPARQL variables uses the following rules:

1. Use the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of the property `sh:annotationVarName`
2. If no such [value](https://www.w3.org/TR/shacl12-core/#dfn-value) exists, use the local name of the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:annotationProperty` as the variable name.

If a variable name could be determined, then the SHACL processor copies the binding for the given variable
as a value for the property specified using `sh:annotationProperty` into the [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result) that is being produced for the current solution.
If the variable has no binding in the result set solution,
then the [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:annotationValue` are used, if present.
> **Example:**
>
> Example 9: Example of using result annotations
>
> ex:AnnotationExample
> a sh:NodeShape ;
> sh:targetNode ex:ExampleResource ;
> sh:sparql [ # _:b1
> sh:resultAnnotation [
> sh:annotationProperty ex:time ;
> sh:annotationVarName "time" ;
> ] ;
> sh:select """
> SELECT $this ?message ?time
> WHERE {
> BIND (CONCAT("The ", "message.") AS ?message) .
> BIND (NOW() AS ?time) .
> }
> """ ;
> ] .
>
> ```
> {
> 	"@id": "ex:AnnotationExample",
> 	"@type": "sh:NodeShape",
> 	"sh:sparql": {
> 		"sh:resultAnnotation": {
> 			"sh:annotationProperty": {
> 				"@id": "ex:time"
> 			},
> 			"sh:annotationVarName": "time"
> 		},
> 		"sh:select": "\n\t\t\tSELECT $this ?message ?time\n\t\t\tWHERE {\n\t\t\t\tBIND (CONCAT(\"The \", \"message.\") AS ?message) .\n\t\t\t\tBIND (NOW() AS ?time) .\n\t\t\t}\n\t\t\t"
> 	},
> 	"sh:targetNode": {
> 		"@id": "ex:ExampleResource"
> 	}
> }
> ```
>
> [ a sh:ValidationReport ;
> sh:conforms false ;
> sh:result [
> a sh:ValidationResult ;
> sh:focusNode ex:ExampleResource ;
> sh:resultMessage "The message." ;
> sh:resultSeverity sh:Violation ;
> sh:sourceConstraint _:b1 ;
> sh:sourceConstraintComponent sh:SPARQLConstraintComponent ;
> sh:sourceShape ex:AnnotationExample ;
> ex:time "2015-03-27T10:58:00"^^xsd:dateTime ; # Example
> ]
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
> 		"ex:time": {
> 			"@type": "xsd:dateTime",
> 			"@value": "2015-03-27T10:58:00"
> 		},
> 		"sh:focusNode": {
> 			"@id": "ex:ExampleResource"
> 		},
> 		"sh:resultMessage": "The message.",
> 		"sh:resultSeverity": {
> 			"@id": "sh:Violation"
> 		},
> 		"sh:sourceConstraint": {
> 			"@id": "_:b1"
> 		},
> 		"sh:sourceConstraintComponent": {
> 			"@id": "sh:SPARQLConstraintComponent"
> 		},
> 		"sh:sourceShape": {
> 			"@id": "ex:AnnotationExample"
> 		}
> 	}
> }
> ```

### 6. SPARQL-based Node Expressions

This section introduces [node expression functions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) based on SPARQL.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The node expression functions in this section embed complete SPARQL queries or SPARQL expressions.
> Node expression functions for individual SPARQL functions such as `sparql:concat`,
> which are evaluated without a SPARQL query, are defined in [SHACL 1.2 Node Expressions](https://www.w3.org/TR/shacl12-node-expr/#sparql-functions).

#### 6.1 Select Expressions

A [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that has a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the [key parameter](https://www.w3.org/TR/shacl12-node-expr/#NamedParameterFunctions) `sh:select` is called a *select expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `sh:SelectExpression`.

A node in an RDF graph is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) select expression if it is a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that has exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) `sh:select` and this [value](https://www.w3.org/TR/shacl12-core/#dfn-value) is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype) `xsd:string`. A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) select expression can have at most one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:prefixes` and this value can only be an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node).

Using the prefix handling rules (§2), the value of `sh:select` is a valid SPARQL 1.2 SELECT query. The SPARQL query derived from the value of `sh:select` [projects](https://www.w3.org/TR/sparql12-query/#selectproject) exactly one variable in the SELECT clause.

EVALUATION OF SELECT EXPRESSIONS

The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of a select expression are the list `resultNodes` consisting of exactly the bindings of the (only)
variable that is projected from the `SELECT` clause when the query is evaluated against the [focus graph](https://www.w3.org/TR/shacl12-core/#dfn-focus-graph).
The value of `focusNode` is pre-bound as the value of the SPARQL variable `this`.
The value of each scope variable is pre-bound as a SPARQL variable with the same name and value.
If the name of a variable in scope is not a string literal, use `"arg" + str(name)`.
For example, if the variable name is `"0"^^xsd:integer`, use `arg0`.
A [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) is produced when one of the scope variables is called `this` or when a variable name derived in this way is not a valid [SPARQL VARNAME](https://www.w3.org/TR/sparql12-query/#rVARNAME).

`evalExpr(expr, focusGraph, focusNode, scope) -> resultNodes`

*The remainder of this section is non-normative.*
> **Example:**
>
> Example 10: A dynamically computed property using a node expression based on a SPARQL query
>
> Here is an example use of a select expression, computing the values of a property shape for the property
> "full name" as the concatenation of the `ex:firstName`, a space, and the `ex:lastName`.
>
> ex:Person-fullName
> a sh:PropertyShape ;
> sh:name "full name" ;
> sh:path ex:fullName ;
> sh:values **[
> sh:prefixes ex: ;
> sh:select """
> SELECT ?fullName
> WHERE {
> $this ex:firstName ?firstName .
> $this ex:lastName ?lastName .
> BIND (CONCAT(?firstName, " ", ?lastName) AS ?fullName) .
> }
> """
> ]** ;
> sh:datatype xsd:string .
>
> ex:
> a owl:Ontology ;
> sh:declare [
> sh:prefix "ex" ;
> sh:namespace "http://example.com/ns#"^^xsd:anyURI ;
> ] .
>
> ```
> {
> 	"@graph": [
> 		{
> 			"@id": "ex:Person-fullName",
> 			"@type": "sh:PropertyShape",
> 			"sh:datatype": {
> 				"@id": "xsd:string"
> 			},
> 			"sh:name": "full name",
> 			"sh:path": {
> 				"@id": "ex:fullName"
> 			},
> 			"sh:values": {
> 				"sh:prefixes": {
> 					"@id": "http://example.com/ns#"
> 				},
> 				"sh:select": "\n\t\t\tSELECT ?fullName\n\t\t\tWHERE {\n\t\t\t\t$this ex:firstName ?firstName .\n\t\t\t\t$this ex:lastName ?lastName .\n\t\t\t\tBIND (CONCAT(?firstName, \" \", ?lastName) AS ?fullName) .\n\t\t\t}\n\t\t"
> 			}
> 		},
> 		{
> 			"@id": "http://example.com/ns#",
> 			"@type": "owl:Ontology",
> 			"sh:declare": {
> 				"sh:namespace": {
> 					"@type": "xsd:anyURI",
> 					"@value": "http://example.com/ns#"
> 				},
> 				"sh:prefix": "ex"
> 			}
> 		}
> 	]
> }
> ```
>
> This example also illustrates the use of `sh:prefixes` to insert PREFIX declarations into the beginning of the query before parsing.
> Note that the query is executed with the current [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node) pre-bound to the variable `this`.
> **Example:**
>
> Example 11: Dynamically computed target nodes using a node expression based on a SPARQL query
>
> Here is an example use of a select expression, computing the target nodes of a shape to consist of all instances of `ex:Person` where the `ex:age` is less than `18`.
>
> ex:ChildShape
> a sh:NodeShape ;
> rdfs:label "Child shape" ;
> rdfs:comment "This shape applies to all persons under 18 years of age." ;
> sh:targetNode **[
> sh:select """
> PREFIX ex: <http://example.com/ns#>
> SELECT ?person
> WHERE {
> ?person a/rdfs:subClassOf* ex:Person .
> ?person ex:age ?age .
> FILTER (?age < 18) .
> }
> """
> ]** .
>
> ```
> {
> 	"@id": "ex:ChildShape",
> 	"@type": "sh:NodeShape",
> 	"rdfs:comment": "This shape applies to all persons under 18 years of age.",
> 	"rdfs:label": "Child shape",
> 	"sh:targetNode": {
> 		"sh:select": "\n\t\t\tPREFIX ex: <http://example.com/ns#>\n\t\t\tSELECT ?person\n\t\t\tWHERE {\n\t\t\t\t?person a/rdfs:subClassOf* ex:Person .\n\t\t\t\t?person ex:age ?age .\n\t\t\t\tFILTER (?age < 18) .\n\t\t\t}\n\t\t"
> 	}
> }
> ```
>
> From the following data graph, only `ex:Benjamin` is a target node.
>
> ex:Benjamin a ex:Person ;
> ex:age 17 .
>
> ex:Klaus
> a ex:Person ;
> ex:age 48 .
>
> ex:Bernd
> a ex:Person .
>
> ```
> {
> 	"@graph": [
> 		{
> 			"@id": "ex:Benjamin",
> 			"@type": "ex:Person",
> 			"ex:age": {
> 				"@type": "xsd:integer",
> 				"@value": "17"
> 			}
> 		},
> 		{
> 			"@id": "ex:Bernd",
> 			"@type": "ex:Person"
> 		},
> 		{
> 			"@id": "ex:Klaus",
> 			"@type": "ex:Person",
> 			"ex:age": {
> 				"@type": "xsd:integer",
> 				"@value": "48"
> 			}
> 		}
> 	]
> }
> ```

#### 6.2 SPARQL Expr Expressions

A [node expression](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) that has a [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the [key parameter](https://www.w3.org/TR/shacl12-node-expr/#NamedParameterFunctions) `sh:sparqlExpr` is called a *SPARQL expr expression* with the [function name](https://www.w3.org/TR/shacl12-core/#dfn-function-name) `sh:SPARQLExprExpression`.

A node in an RDF graph
is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) SPARQL expr expression if it is a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that has exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) `sh:sparqlExpr` and that [value](https://www.w3.org/TR/shacl12-core/#dfn-value) is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype) `xsd:string`. A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) SPARQL expr expression can have at most one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:prefixes` and this value is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node).

Let `$EXPR$` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:sparqlExpr` and `$PREFIXES$` be the SPARQL prefixes block resulting from the prefix handling rules (§2) using the value of `sh:prefixes`;
then `select` is defined as the string where `$EXPR$` and `$PREFIXES$` are inserted as into

`$PREFIXES$ SELECT ($EXPR$ AS ?result) WHERE {}`

`select` is a valid SPARQL 1.2 SELECT query.

EVALUATION OF SPARQL EXPR EXPRESSIONS

The [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of an SPARQL expr expression are the list `resultNodes` consisting of exactly the bindings of the (only)
variable that is projected from the `SELECT` clause of the `select` query as defined above when the query is evaluated against the [focus graph](https://www.w3.org/TR/shacl12-core/#dfn-focus-graph).
The value of `focusNode` is pre-bound as the value of the SPARQL variable `this`.
The value of each scope variable is pre-bound as a SPARQL variable with the same name and value.
If the name of a variable in scope is not a string literal, use `"arg" + str(name)`.
For example, if the variable name is `"0"^^xsd:integer`, use `arg0`.
A [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) is produced when one of the scope variables is called `this` or when a variable name derived in this way is not a valid [SPARQL VARNAME](https://www.w3.org/TR/sparql12-query/#rVARNAME).

`evalExpr(expr, focusGraph, focusNode, scope) -> resultNodes`

*The remainder of this section is non-normative.*
> **Example:**
>
> Example 12: A dynamically computed property using a SPARQL expr expression
>
> Here is an example use of an SPARQL expr expression, computing the values of a property shape for the property
> "uri length" as the length of the IRI of the focus node.
>
> ex:Resource-uriLength
> a sh:PropertyShape ;
> sh:name "uri length" ;
> sh:path ex:uriLength ;
> sh:values **[
> sh:sparqlExpr "STRLEN(STR($this))" ;
> ]** ;
> sh:datatype xsd:integer .
>
> ```
> {
> 	"@id": "ex:Resource-uriLength",
> 	"@type": "sh:PropertyShape",
> 	"sh:datatype": {
> 		"@id": "xsd:integer"
> 	},
> 	"sh:name": "uri length",
> 	"sh:path": {
> 		"@id": "ex:uriLength"
> 	},
> 	"sh:values": {
> 		"sh:sparqlExpr": "STRLEN(STR($this))"
> 	}
> }
> ```
>
> When applied to a focus node with URI `http://example.com/ns#Test` the result will be `26`.
> This produces the same results as this variation:
>
> ex:Resource-uriLength
> a sh:PropertyShape ;
> sh:name "uri length" ;
> sh:path ex:uriLength ;
> sh:values **[
> sh:select """
> SELECT (STRLEN(STR($this)) AS ?result)
> WHERE {
> }
> """ ;
> ]** ;
> sh:datatype xsd:integer .
>
> ```
> {
> 	"@id": "ex:Resource-uriLength",
> 	"@type": "sh:PropertyShape",
> 	"sh:datatype": {
> 		"@id": "xsd:integer"
> 	},
> 	"sh:name": "uri length",
> 	"sh:path": {
> 		"@id": "ex:uriLength"
> 	},
> 	"sh:values": {
> 		"sh:select": "\n\t\t\tSELECT (STRLEN(STR($this)) AS ?result)\n\t\t\tWHERE {\n\t\t\t}\n\t\t"
> 	}
> }
> ```
>
> Note that the query is executed with the current [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node) pre-bound to the variable `this`.

### 7. Declaring SPARQL Functions based on Node Expressions

[SHACL 1.2 Node Expressions](https://www.w3.org/TR/shacl12-node-expr/) defines [Custom List Parameter Functions](https://www.w3.org/TR/shacl12-node-expr/#custom-node-expressions) as a mechanism to declare new node expression functions.
These can be evaluated as part of other SHACL node expressions, but may also be useful to other engines
that support function-like execution.

The SPARQL specification defines an [extension point](https://www.w3.org/TR/sparql12-query/#extensionFunctions) that
enables certain SPARQL engines to provide additional SPARQL functions.
This section introduces a declarative mechanism allowing SPARQL processors to make SHACL list parameter functions
available as SPARQL functions using that extension point.

#### 7.1 Example SPARQL Function using general Node Expressions
> **Example:**
>
> Example 13: An example custom function using shnex: node expressions
>
> This function takes a class as its (only) parameter and returns the number of instances of that class.
>
> ex:instanceCount
> a sh:ListParameterExpressionFunction ;
> rdfs:label "instance count"@en ;
> rdfs:subClassOf sh:ListParameterExpression ;
> sh:bodyExpression [
> shnex:count [
> shnex:instancesOf [
> shnex:arg 0
> ]
> ]
> ] ;
> sh:parameter [
> a sh:Parameter ;
> sh:path shnex:arg0 ;
> sh:name "class" ;
> sh:description "The class to count the instances of." ;
> sh:nodeKind sh:IRI ;
> ] .
>
> ```
> {
> 	"@id": "ex:instanceCount",
> 	"@type": "sh:ListParameterExpressionFunction",
> 	"rdfs:label": {
> 		"@language": "en",
> 		"@value": "instance count"
> 	},
> 	"rdfs:subClassOf": {
> 		"@id": "sh:ListParameterExpression"
> 	},
> 	"sh:bodyExpression": {
> 		"shnex:count": {
> 			"shnex:instancesOf": {
> 				"shnex:arg": {
> 					"@type": "xsd:integer",
> 					"@value": "0"
> 				}
> 			}
> 		}
> 	},
> 	"sh:parameter": {
> 		"@type": "sh:Parameter",
> 		"sh:description": "The class to count the instances of.",
> 		"sh:name": "class",
> 		"sh:nodeKind": {
> 			"@id": "sh:IRI"
> 		},
> 		"sh:path": {
> 			"@id": "shnex:arg0"
> 		}
> 	}
> }
> ```
>
> A SPARQL engine that supports SPARQL functions based on node expressions is able
> to process a SPARQL query such as the following:
>
> ```
> SELECT ?class ?count
> WHERE {
> 	?class a owl:Class .
> 	BIND (ex:instanceCount(?class) AS ?count) .
> }
> ```

#### 7.2 Example SPARQL Functions using SPARQL-based Node Expressions

The following custom list parameter functions use "nested" SPARQL queries at evaluation time.
> **Example:**
>
> Example 14: An example custom function using sh:sparqlExpr
>
> This function takes two parameters and uses a SPARQL expr expression as its body expression.
> In that SPARQL expression, the variables `$arg0` and `$arg1` are used to access the list parameter values.
> It is a variation of the `ex:spacedConcat` example of [shacl12-node-expr], which uses the `sparql:concat` node expression function instead of a SPARQL expression.
>
> ex:spacedConcat
> a sh:ListParameterExpressionFunction ;
> rdfs:label "spaced concat"@en ;
> rdfs:subClassOf sh:ListParameterExpression ;
> sh:bodyExpression [
> sh:sparqlExpr "CONCAT($arg0, ' ', $arg1)"
> ] ;
> sh:parameter [
> a sh:Parameter ;
> sh:path shnex:arg0 ;
> sh:name "first string" ;
> sh:description "The first string to concatenate." ;
> sh:datatype xsd:string ;
> ] ;
> sh:parameter [
> a sh:Parameter ;
> sh:path shnex:arg1 ;
> sh:name "second string" ;
> sh:description "The second string to concatenate." ;
> sh:datatype xsd:string ;
> ] .
>
> ```
> {
> 	"@id": "ex:spacedConcat",
> 	"@type": "sh:ListParameterExpressionFunction",
> 	"rdfs:label": {
> 		"@language": "en",
> 		"@value": "spaced concat"
> 	},
> 	"rdfs:subClassOf": {
> 		"@id": "sh:ListParameterExpression"
> 	},
> 	"sh:bodyExpression": {
> 		"sh:sparqlExpr": "CONCAT($arg0, ' ', $arg1)"
> 	},
> 	"sh:parameter": [
> 		{
> 			"@type": "sh:Parameter",
> 			"sh:datatype": {
> 				"@id": "xsd:string"
> 			},
> 			"sh:description": "The first string to concatenate.",
> 			"sh:name": "first string",
> 			"sh:path": {
> 				"@id": "shnex:arg0"
> 			}
> 		},
> 		{
> 			"@type": "sh:Parameter",
> 			"sh:datatype": {
> 				"@id": "xsd:string"
> 			},
> 			"sh:description": "The second string to concatenate.",
> 			"sh:name": "second string",
> 			"sh:path": {
> 				"@id": "shnex:arg1"
> 			}
> 		}
> 	]
> }
> ```
>
> A SPARQL engine that supports SPARQL functions based on node expressions is able
> to process a SPARQL query such as the following:
>
> ```
> SELECT ?person ?fullName
> WHERE {
> 	?person a ex:Person .
> 	?person ex:firstName ?firstName .
> 	?person ex:lastName ?lastName .
> 	BIND (ex:spacedConcat(?firstName, ?lastName) AS ?fullName) .
> }
> ```

The following example uses a `sh:select` node expression as its body.
> **Example:**
>
> Example 15: An example custom function using sh:select
>
> This function takes two parameters, the second of which is optional, and uses a select expression as its body expression.
> In that SPARQL query, the variables `$arg0` and `$arg1` are used to access the list parameter values.
>
> ex:langLabelCount
> a sh:ListParameterExpressionFunction ;
> rdfs:label "lang label count"@en ;
> rdfs:subClassOf sh:ListParameterExpression ;
> sh:bodyExpression [
> sh:select """
> PREFIX ex: <http://example.com/ns#>
> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
> SELECT (COUNT(?label) AS ?result)
> WHERE {
> ?predicate rdfs:subPropertyOf* rdfs:label .
> $arg0 ?predicate ?label .
> BIND (COALESCE($arg1, 'en') AS ?matchLang) .
> FILTER langMatches(lang(?label), ?matchLang) .
> }
> """ ;
> ] ;
> sh:parameter [
> a sh:Parameter ;
> sh:path shnex:arg0 ;
> sh:name "subject" ;
> sh:description "The subject node to get the label count of." ;
> sh:nodeKind sh:IRI ;
> ] ;
> sh:parameter [
> a sh:Parameter ;
> sh:path shnex:arg1 ;
> sh:name "match language" ;
> sh:description "The language to filter, defaulting to 'en'." ;
> sh:datatype xsd:string ;
> sh:defaultValue "en" ;
> sh:optional true ;
> ] .
>
> ```
> {
> 	"@id": "ex:langLabelCount",
> 	"@type": "sh:ListParameterExpressionFunction",
> 	"rdfs:label": {
> 		"@language": "en",
> 		"@value": "lang label count"
> 	},
> 	"rdfs:subClassOf": {
> 		"@id": "sh:ListParameterExpression"
> 	},
> 	"sh:bodyExpression": {
> 		"sh:select": "\n\t\t\tPREFIX ex: <http://example.com/ns#>\n\t\t\tPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n\t\t\tSELECT (COUNT(?label) AS ?result)\n\t\t\tWHERE {\n\t\t\t\t?predicate rdfs:subPropertyOf* rdfs:label .\n\t\t\t\t$arg0 ?predicate ?label .\n\t\t\t\tBIND (COALESCE($arg1, 'en') AS ?matchLang) .\n\t\t\t\tFILTER langMatches(lang(?label), ?matchLang) .\n\t\t\t}\n\t\t"
> 	},
> 	"sh:parameter": [
> 		{
> 			"@type": "sh:Parameter",
> 			"sh:description": "The subject node to get the label count of.",
> 			"sh:name": "subject",
> 			"sh:nodeKind": {
> 				"@id": "sh:IRI"
> 			},
> 			"sh:path": {
> 				"@id": "shnex:arg0"
> 			}
> 		},
> 		{
> 			"@type": "sh:Parameter",
> 			"sh:datatype": {
> 				"@id": "xsd:string"
> 			},
> 			"sh:defaultValue": "en",
> 			"sh:description": "The language to filter, defaulting to 'en'.",
> 			"sh:name": "match language",
> 			"sh:optional": {
> 				"@type": "xsd:boolean",
> 				"@value": "true"
> 			},
> 			"sh:path": {
> 				"@id": "shnex:arg1"
> 			}
> 		}
> 	]
> }
> ```
>
> This function accepts an optional parameter for the match language, as declared using the `sh:optional true` triple.
> However, note that the SHACL constraints from the `sh:parameter` declarations are
> not automatically enforced, nor will the declared `sh:defaultValue` be used at runtime.
> Apart from `sh:optional`, which determines how errors in the arguments are handled
> (see 7.3 Evaluation of Custom SPARQL Functions (§7.3)), these declarations serve documentation purposes.
>
> ex:Cougar
> rdfs:label "Cougar"@en ;
> rdfs:label "Mountain Lion"@en-US ;
> rdfs:label "Puma"@de .
>
> # Example SPARQL function calls:
> # ex:langLabelCount(ex:Cougar, 'en') = 2
> # ex:langLabelCount(ex:Cougar) = 2
> # ex:langLabelCount(ex:Cougar, 'de') = 1
> # ex:langLabelCount(?unbound, 'en') = SPARQL error
>
> ```
> {
> 	"@id": "ex:Cougar",
> 	"rdfs:label": [
> 		{
> 			"@language": "en",
> 			"@value": "Cougar"
> 		},
> 		{
> 			"@language": "en-US",
> 			"@value": "Mountain Lion"
> 		},
> 		{
> 			"@language": "de",
> 			"@value": "Puma"
> 		}
> 	]
> }
> ```

#### 7.3 Evaluation of Custom SPARQL Functions

This document does not define exact constraints on how and when such custom SPARQL functions are added.
The recommendation is that SPARQL engines *SHOULD* register a function for any [SHACL instance](https://www.w3.org/TR/shacl12-core/#dfn-shacl-instance) of `sh:ListParameterExpressionFunction` from any provided [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph).
If a function with the same [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) is already registered as a built-in or other non-custom function,
SPARQL engines *MUST* ignore the attempt to redefine it.
If the registered function is itself a custom SPARQL function, for example from a previously provided [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph),
the new declaration replaces it.
A SPARQL engine *MUST NOT* modify the registered SPARQL functions while it is executing any SPARQL query.

EVALUATION OF CUSTOM SPARQL FUNCTIONS

Let `f` be the `iri` of a SPARQL [function call](https://www.w3.org/TR/sparql12-query/#ririOrFunction) and `args` be the list of `Expression` arguments.
Let `function` be the corresponding custom list parameter function in the [graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph) where it has been defined, with `f` as its [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri).

Evaluate each SPARQL expression from `args`, yielding a new list of [nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-node) `nodesList`.
Where the evaluation has caused an [error](https://www.w3.org/TR/sparql12-query/#sparql-error),
the result of the SPARQL function call is also an error,
unless the corresponding `sh:parameter` for the argument has `sh:optional true`.
In that case, the argument will be unbound in the scope.
Note that [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) cannot be passed as arguments: they are not constant node expressions,
so an argument that evaluates to a blank node leads to an [evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure) and thus an error.

Let `rs` be the [output nodes](https://www.w3.org/TR/shacl12-core/#dfn-output-nodes) of `evalExpr(function, focusGraph, f, scope)` where `focusGraph` is the
currently active query graph from the SPARQL context, and `scope` is the map of evaluated
arguments from `nodesList` with the index of the argument as the variable name (map key).

If the list of output nodes `rs` has exactly one member, then return that node.
Otherwise, or if the evaluation produces an [evaluation failure](https://www.w3.org/TR/shacl12-core/#dfn-evaluation-failure),
the result of the SPARQL function call is an error.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> During the evaluation of SPARQL queries, there is no dedicated [focus node](https://www.w3.org/TR/shacl12-core/#dfn-focus-node).
> Instead, the `focusNode` passed into a custom SPARQL function based on a node expression
> is the [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) of the function itself.

## Appendix

### A. Pre-binding of Variables in SPARQL Queries

Some features of SHACL-SPARQL rely on the concept of pre-binding of variables as defined in this section.

The definition of pre-binding used by SHACL requires the following restrictions on SPARQL queries.
SHACL-SPARQL processors *MUST* report a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) when operating on a [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) that contains SHACL-SPARQL queries (via `sh:ask`, `sh:construct`, `sh:select` and `sh:sparqlExpr`)
that are executed with pre-bound variables and violate any of these "*MUST*" restrictions.
Note that the term *potentially pre-bound variables* includes the variables `this`, `value` (for ASK queries),
any variables that represent the [parameters](https://www.w3.org/TR/shacl12-core/#dfn-parameter) of the [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) that uses the query,
and the variables that represent the scope variables of §6 SPARQL-based Node Expressions (such as `arg0`).

- SPARQL queries *MUST* not contain a `MINUS` clause
- SPARQL queries *MUST* not contain a `VALUES` clause that mentions any potentially pre-bound variable
- SPARQL queries *MUST* not use the syntax form `AS ?var` for any potentially pre-bound variable

Furthermore, SPARQL queries *SHOULD* not contain a federated query (`SERVICE`).
Implementations that do not permit `SERVICE` *MUST* report a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) as mentioned above.
However, it is acknowledged that some SPARQL implementations use the `SERVICE` keyword as a syntax for
specific (typically local) operations and therefore the keyword is not generally disallowed.

DEFINITION: *Values Insertion*

For solution mapping `μ`, define `Table(μ)` to be the multiset formed from `μ`.

`Table(μ) = { μ }`
`Card[μ] = 1`

Define the *Values Insertion* function `Replace(X, μ)` to
replace each occurrence `Y` of a [Basic Graph Pattern](https://www.w3.org/TR/sparql12-query/#sparqlTranslateBasicGraphPatterns), [Property Path Expression](https://www.w3.org/TR/sparql12-query/#sparqlTranslatePathExpressions), [`Graph(Var, pattern)`](https://www.w3.org/TR/sparql12-query/#sparqlTranslateGraphPatterns) in `X` with `join(Y, Table(μ))`.

DEFINITION: *Pre-binding of variables*

The evaluation of the [SPARQL Query](https://www.w3.org/TR/sparql12-query/#idp2427544) `Q = (E, DS, QF)` with *pre-bound* variables `μ` is defined as the evaluation of SPARQL query `Q' = (Replace(E, μ), DS, QF)`.

### B. Summary of Syntax Rules

This section enumerates all normative syntax rules of this document.
This section is automatically generated from other parts of this spec and hyperlinks are provided back
into the prose if the context of the rule in unclear.
Nodes that violate these rules in a [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) are [ill-formed](https://www.w3.org/TR/shacl12-core/#dfn-ill-formed).

| Syntax Rule Id                                                                                                                         | Syntax Rule Text                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| prefix-count                                                         | Prefix declarations have exactly one value for the property `sh:prefix`                                                                  |
| prefix-datatype                                                   | The values of `sh:prefix` are [literals](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) of datatype `xsd:string`.                                                                                |
| namespace-count                                                   | Prefix declarations have exactly one value for the property `sh:namespace`.                                                              |
| namespace-datatype                                             | The values of `sh:namespace` are [literals](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) of datatype `xsd:anyURI` or `xsd:string`.                                                             |
| declare-nodeKind                                                 | The [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of the property `sh:declare` are prefix declarations                         |
| prefixes-nodeKind                                               | The values of `sh:prefixes` are either [IRIs](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node).                                     |
| prefixes-duplicates                                           | If such a collection of prefix declarations contains multiple different namespaces for the same [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:prefix`, then the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) is [ill-formed](https://www.w3.org/TR/shacl12-core/#dfn-ill-formed). |
| sparql-nodeKind                                                   | Shapes may have values for the property `sh:sparql`, and these values are either [IRIs](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node). |
| SPARQLConstraint-select-count                       | SPARQL-based constraints have exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:select`       |
| SPARQLConstraint-select-datatype                 | The value of `sh:select` is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) of datatype `xsd:string`.                                                                                 |
| select-query-valid                                             | Using the prefix handling rules (§2), the value of `sh:select` is a valid SPARQL 1.2 SELECT query.                                                   |
| select-query-this                                               | The SPARQL query derived from the value of `sh:select` [projects](https://www.w3.org/TR/sparql12-query/#selectproject) the variable `this` in the SELECT clause.                                         |
| SPARQLConstraint-message-datatype               | SPARQL-based constraints may have values for the property `sh:message xsd:string` and these are [literals](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype), `rdf:dirLangString`, `rdf:langString`, or `rdf:HTML`. There should neither be more than one value for `sh:message` with the same language tag, nor multiple values with datatype `xsd:string`. |
| SPARQLConstraint-deactivated-maxCount       | SPARQL-based constraints may have at most one value for the property `sh:deactivated`                                               |
| SPARQLConstraint-severity                               | SPARQL-based constraints may have at most one value for the property `sh:severity` and this value is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri). |
| PATH-position                                                       | The only legal use of the variable `PATH` in the SPARQL queries of SPARQL-based constraints and SELECT-based validators is in the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) position of a [triple pattern](https://www.w3.org/TR/sparql12-query/#QSynTriples). |
| ConstraintComponent                                           | A SPARQL-based constraint component is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) that has [SHACL type](https://www.w3.org/TR/shacl12-core/#dfn-shacl-type) `sh:ConstraintComponent` in the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph). |
| Parameter-predicate-count                               | Each parameter declaration has exactly one value for the property `sh:path`                                                           |
| Parameter                                                               | At parameter declarations, the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:path` is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri). |
| parameter-name-VARNAME                                     | Every parameter name is a valid [SPARQL VARNAME](https://www.w3.org/TR/sparql12-query/#rVARNAME).                                           |
| parameter-name-not-in                                       | Parameter names must not be one of the following: `this`, `path`, `PATH`, `value`, `message`, `failure`.                                    |
| parameter-name-unique                                       | A constraint component where two or more parameter declarations use the same parameter names is [ill-formed](https://www.w3.org/TR/shacl12-core/#dfn-ill-formed). |
| optional-datatype                                               | The values of `sh:optional` must be literals with datatype `xsd:boolean`.                                                                                                                                |
| optional-maxCount                                               | A parameter declaration can have at most one value for the property `sh:optional`.                                                    |
| ConstraintComponent-parameter                       | Every [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) has at least one non-optional parameter.                                                                      |
| Parameter-conformance                                       | Shapes that do not [conform](https://www.w3.org/TR/shacl12-core/#dfn-conform) with the constraints declared for the parameters are [ill-formed](https://www.w3.org/TR/shacl12-core/#dfn-ill-formed).     |
| labelTemplate-datatype                                     | The values of `sh:labelTemplate xsd:string` are [literals](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype), `rdf:langString` or `rdf:dirLangString` |
| nodeValidator-class                                           | The values of `sh:nodeValidator` must be SELECT-based validators.                                                                   |
| propertyValidator-class                                   | The values of `sh:propertyValidator` must be SELECT-based validators.                                                               |
| SPARQLSelectValidator-select-count             | SELECT-based validators have exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:select`.       |
| SPARQLSelectValidator-select-datatype       | The value of `sh:select` is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) of datatype `xsd:string`.                                                                                 |
| SPARQLSelectValidator-select-query-valid | Using the prefix handling rules (§2), the value of `sh:select` is a valid SPARQL 1.2 SELECT query.                                                   |
| SPARQLSelectValidator-select-query-this   | The SPARQL query derived from the value of `sh:select` [projects](https://www.w3.org/TR/sparql12-query/#selectproject) the variable `this` in its SELECT clause.                                         |
| validator-class                                                   | The values of `sh:validator` must be ASK-based validators.                                                                             |
| ask-count                                                               | ASK-based validators have exactly one value for the property `sh:ask`                                                                  |
| ask-datatype                                                         | The value of `sh:ask` must be a literal with datatype `xsd:string`.                                                                                                                                      |
| ask-sparql                                                             | The value of `sh:ask` must be a valid SPARQL ASK query using the aforementioned prefix handling rules (§2).                                          |
| resultAnnotation-nodeKind                               | The [values](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:resultAnnotation` are called result annotations and are either [IRIs](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or [blank nodes](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) |
| annotationProperty                                             | Each result annotation has exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:annotationProperty` and this value is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri). |
| annotationVarName                                               | Each result annotation has at most 1 [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:annotationVarName xsd:string` and this [value](https://www.w3.org/TR/shacl12-core/#dfn-value) is [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype). |
| SelectExpression-syntax                                   | A node in an RDF graph is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) select expression if it is a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that has exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) `sh:select xsd:string` and this [value](https://www.w3.org/TR/shacl12-core/#dfn-value) is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype). |
| SelectExpression-syntax-prefixes                 | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) select expression can have at most one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:prefixes` and this value can only be an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node). |
| SelectExpression-query-valid                         | Using the prefix handling rules (§2), the value of `sh:select` is a valid SPARQL 1.2 SELECT query.                                                   |
| SelectExpression-query-output-nodes           | The SPARQL query derived from the value of `sh:select` [projects](https://www.w3.org/TR/sparql12-query/#selectproject) exactly one variable in the SELECT clause.                                        |
| SPARQLExprExpression-syntax-eval                 | A node in an RDF graph is a [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) SPARQL expr expression if it is a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) that has exactly one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the [predicate](https://www.w3.org/TR/rdf12-concepts/#dfn-predicate) `sh:sparqlExpr xsd:string` and that [value](https://www.w3.org/TR/shacl12-core/#dfn-value) is a [literal](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-literal) with [datatype](https://www.w3.org/TR/rdf12-concepts/#dfn-datatype). |
| SPARQLExprExpression-syntax-prefixes         | A [well-formed](https://www.w3.org/TR/shacl12-core/#dfn-well-formed) SPARQL expr expression can have at most one [value](https://www.w3.org/TR/shacl12-core/#dfn-value) for the property `sh:prefixes` and this value is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node). |
| SPARQLExprExpression-template                       | Let `$EXPR$` be the [value](https://www.w3.org/TR/shacl12-core/#dfn-value) of `sh:sparqlExpr` and `$PREFIXES$` be the SPARQL prefixes block resulting from the prefix handling rules (§2) using the value of `sh:prefixes`; then `select` is defined as the string where `$EXPR$` and `$PREFIXES$` are inserted as into `$PREFIXES$ SELECT ($EXPR$ AS ?result) WHERE {}` |
| SPARQLExprExpression-query-valid                 | `select` is a valid SPARQL 1.2 SELECT query.                                                                                                                                                             |
| pre-binding-limitations                                   | The definition of pre-binding used by SHACL requires the following restrictions on SPARQL queries. SHACL-SPARQL processors *MUST* report a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) when operating on a [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) that contains SHACL-SPARQL queries (via `sh:ask`, `sh:construct`, `sh:select` and `sh:sparqlExpr`) that are executed with pre-bound variables and violate any of these "*MUST*" restrictions. Note that the term *potentially pre-bound variables* includes the variables `this`, `value` (for ASK queries), any variables that represent the [parameters](https://www.w3.org/TR/shacl12-core/#dfn-parameter) of the [constraint component](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) that uses the query, and the variables that represent the scope variables of §6 SPARQL-based Node Expressions (such as `arg0`). SPARQL queries *MUST* not contain a `MINUS` clause SPARQL queries *MUST* not contain a `VALUES` clause that mentions any potentially pre-bound variable SPARQL queries *MUST* not use the syntax form `AS ?var` for any potentially pre-bound variable Furthermore, SPARQL queries *SHOULD* not contain a federated query (`SERVICE`). Implementations that do not permit `SERVICE` *MUST* report a [failure](https://www.w3.org/TR/shacl12-core/#dfn-failure) as mentioned above. However, it is acknowledged that some SPARQL implementations use the `SERVICE` keyword as a syntax for specific (typically local) operations and therefore the keyword is not generally disallowed. |

### C. Potential SPARQL Definitions of SHACL Core Constraint Validators

*This section is non-normative.*

This appendix uses parts of SPARQL 1.2 in non-normative alternative definitions of the semantics of [constraint components](https://www.w3.org/TR/shacl12-core/#dfn-constraint-component) and [targets](https://www.w3.org/TR/shacl12-core/#dfn-target) from [shacl12-core].
While these may help some implementers, SPARQL is not required for the implementation of the SHACL Core language.

The definitions for `sh:targetClass` and `sh:class` look up `rdfs:subClassOf` triples
in the [data graph](https://www.w3.org/TR/shacl12-core/#dfn-data-graph) only. If the processor parameter [`subClassOfInShapesGraph`](https://www.w3.org/TR/shacl12-core/#subClassOfInShapesGraph) is set,
the `rdfs:subClassOf` triples of the [shapes graph](https://www.w3.org/TR/shacl12-core/#dfn-shapes-graph) also need to be taken into account.

SPARQL variables using the `$` marker represent external bindings that are pre-bound or, in the case of `$PATH`, substituted in the SPARQL query before execution (as explained in 3.3 Validation with SPARQL-based Constraints (§3.3)).

#### C.1 sh:targetClass

The following query expresses a potential definition of [class targets](https://www.w3.org/TR/shacl12-core/#targetClass) in SPARQL.
The variable `targetClass` will be pre-bound to the given value of `sh:targetClass`.
All bindings of the variable `this` from the solutions become focus nodes.

POTENTIAL DEFINITION IN SPARQL

```
SELECT DISTINCT ?this    # ?this is the focus node
WHERE {
	?this rdf:type/rdfs:subClassOf* $targetClass .
}
```

#### C.2 sh:targetSubjectsOf

The following query expresses a potential definition of [subjects-of targets](https://www.w3.org/TR/shacl12-core/#targetSubjectsOf) in SPARQL.
The variable `targetSubjectsOf` will be pre-bound to the given value of `sh:targetSubjectsOf`.
All bindings of the variable `this` from the solutions become focus nodes.

POTENTIAL DEFINITION IN SPARQL

```
SELECT DISTINCT ?this    # ?this is the focus node
WHERE {
	?this $targetSubjectsOf ?any .
}
```

#### C.3 sh:targetObjectsOf

The following query expresses a potential definition of [objects-of targets](https://www.w3.org/TR/shacl12-core/#targetObjectsOf) in SPARQL.
The variable `targetObjectsOf` will be pre-bound to the given value of `sh:targetObjectsOf`.
All bindings of the variable `this` from the solutions become focus nodes.

POTENTIAL DEFINITION IN SPARQL

```
SELECT DISTINCT ?this    # ?this is the focus node
WHERE {
	?any $targetObjectsOf ?this .
}
```

#### C.4 sh:class

The following query expresses a potential SPARQL-based validator for [sh:class](https://www.w3.org/TR/shacl12-core/#ClassConstraintComponent).

POTENTIAL DEFINITION IN SPARQL (Must evaluate to true for each value node $value)

```
ASK {
	$value rdf:type/rdfs:subClassOf* $class .
}
```

#### C.5 sh:nodeKind

The following query expresses a potential SPARQL-based validator for [sh:nodeKind](https://www.w3.org/TR/shacl12-core/#NodeKindConstraintComponent).

POTENTIAL DEFINITION IN SPARQL (Must evaluate to true for each value node $value)

```
ASK {
	FILTER ((isIRI($value) && $nodeKind IN ( sh:IRI, sh:BlankNodeOrIRI, sh:IRIOrLiteral ) ) ||
		(isLiteral($value) && $nodeKind IN ( sh:Literal, sh:BlankNodeOrLiteral, sh:IRIOrLiteral ) ) ||
		(isBlank($value)   && $nodeKind IN ( sh:BlankNode, sh:BlankNodeOrIRI, sh:BlankNodeOrLiteral ) )) .
}
```

#### C.6 sh:minExclusive (etc)

The following query expresses a potential SPARQL-based validator for [sh:minExclusive](https://www.w3.org/TR/shacl12-core/#MinExclusiveConstraintComponent).
The SPARQL expression produces an error if the value node cannot be compared to the specified range,
for example when someone compares a string with an integer.
If the comparison cannot be performed, then there is a [validation result](https://www.w3.org/TR/shacl12-core/#dfn-validation-result).
This is different from, say, a plain SPARQL query, in which such errors would silently not lead to any results.

POTENTIAL DEFINITION IN SPARQL (Must evaluate to true for each value node $value)

```
ASK {
	FILTER ($minExclusive < $value)
}
```

Similar definitions are possible for:

- [sh:minInclusive](https://www.w3.org/TR/shacl12-core/#MinInclusiveConstraintComponent): <=
- [sh:maxExclusive](https://www.w3.org/TR/shacl12-core/#MaxExclusiveConstraintComponent): >
- [sh:maxInclusive](https://www.w3.org/TR/shacl12-core/#MaxInclusiveConstraintComponent): >=

#### C.7 sh:minLength

The following query expresses a potential SPARQL-based validator for [sh:minLength](https://www.w3.org/TR/shacl12-core/#MinLengthConstraintComponent).

POTENTIAL DEFINITION IN SPARQL (Must evaluate to true for each value node $value)

```
ASK {
	FILTER (STRLEN(str($value)) >= $minLength) .
}
```

#### C.8 sh:maxLength

The following query expresses a potential SPARQL-based validator for [sh:maxLength](https://www.w3.org/TR/shacl12-core/#MaxLengthConstraintComponent).

POTENTIAL DEFINITION IN SPARQL (Must evaluate to true for each value node $value)

```
ASK {
	FILTER (STRLEN(str($value)) <= $maxLength) .
}
```

#### C.9 sh:pattern

The following query expresses a potential SPARQL-based validator for [sh:pattern](https://www.w3.org/TR/shacl12-core/#PatternConstraintComponent).

POTENTIAL DEFINITION IN SPARQL (Must evaluate to true for each value node $value)

```
ASK {
	FILTER (!isBlank($value) && IF(bound($flags), regex(str($value), $pattern, $flags), regex(str($value), $pattern)))
}
```

#### C.10 sh:disjoint

The following query expresses a potential SPARQL-based validator for [sh:disjoint](https://www.w3.org/TR/shacl12-core/#DisjointConstraintComponent).

POTENTIAL DEFINITION IN SPARQL (Must return no results for the given $PATH)

```
SELECT DISTINCT $this ?value
WHERE {
	$this $PATH ?value .
	$this $disjoint ?value .
}
```

#### C.11 sh:lessThan

The following query expresses a potential SPARQL-based validator for [sh:lessThan](https://www.w3.org/TR/shacl12-core/#LessThanConstraintComponent).

POTENTIAL DEFINITION IN SPARQL (Must return no results for the given $PATH)

```
SELECT $this ?value
WHERE {
	$this $PATH ?value .
	$this $lessThan ?otherValue .
	BIND (?value < ?otherValue AS ?result) .
	FILTER (!bound(?result) || !(?result)) .
}
```

#### C.12 sh:lessThanOrEquals

The following query expresses a potential SPARQL-based validator for [sh:lessThanOrEquals](https://www.w3.org/TR/shacl12-core/#LessThanOrEqualsConstraintComponent).

POTENTIAL DEFINITION IN SPARQL (Must return no results for the given $PATH)

```
SELECT $this ?value
WHERE {
	$this $PATH ?value .
	$this $lessThanOrEquals ?otherValue .
	BIND (?value <= ?otherValue AS ?result) .
	FILTER (!bound(?result) || !(?result)) .
}
```

### D. Security and Privacy Considerations

*This section is non-normative.*

Note that SPARQL key words such as `GRAPH` and `FROM` may provide access to
graphs other than the active data graph in the dataset.
A SHACL-SPARQL engine should ensure that the SPARQL engine does not provide access to
named graphs which the user who has triggered the validation is not permitted to access.

Security considerations of SHACL-SPARQL include all the
security considerations of [SPARQL](https://www.w3.org/TR/sparql12-query/#security), [SPARQL Federated Query](https://www.w3.org/TR/sparql12-federated-query/#security) (`SERVICE`) and [SHACL Core](https://www.w3.org/TR/shacl12-core/#security).

### F. Changes between the original SHACL specifications and SHACL 1.2 SPARQL-Related Features

*This section is non-normative.*

- SPARQL-based targets (`sh:target` with `sh:SPARQLTarget` and `sh:SPARQLTargetType`) are no longer defined;
  their use cases are covered by [node expressions](https://www.w3.org/TR/shacl12-core/#dfn-node-expression) at `sh:targetNode`, see 6.1 Select Expressions (§6.1)
- SPARQL functions declared with `sh:SPARQLFunction` (from SHACL Advanced Features) have been replaced by 7. Declaring SPARQL Functions based on Node Expressions (§7)
- SPARQL-based inference rules (`sh:SPARQLRule`) are now defined in [shacl12-inference-rules]
- Messages (`sh:message`) may also use the datatypes `rdf:HTML` and `rdf:dirLangString`
- Added the [node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) `sh:SelectExpression` (§6.1), see [Issue 288](https://github.com/w3c/data-shapes/issues/288)
- Added support for annotation properties, see [Issue 327](https://github.com/w3c/data-shapes/issues/327)
- Added the [node expression function](https://www.w3.org/TR/shacl12-core/#dfn-node-expression-function) `sh:SPARQLExprExpression` (§6.2), see [Issue 315](https://github.com/w3c/data-shapes/issues/315)
- Clarified that VALUES clauses are only disallowed when they mention pre-bound variables (§A) and removed the restriction on sub-SELECTs, see [Issue 159](https://github.com/w3c/data-shapes/issues/159)
- SERVICE clauses are conditionally permitted, see [Issue 374](https://github.com/w3c/data-shapes/issues/374)
- Removed support for the optional pre-bound variables `shapesGraph` and `currentShape`, see [Issue 426](https://github.com/w3c/data-shapes/issues/426)
- SPARQL constraints can now directly specify a `sh:severity`, see [Issue 573](https://github.com/w3c/data-shapes/issues/573)
- If no `sh:prefixes` are present, the system will use any `sh:prefix`/`sh:namespace` pair declared in any `sh:ShapesGraph`, see [Issue 176](https://github.com/w3c/data-shapes/issues/176)

### G. References

#### G.1 Normative references

[owl2-syntax]

[OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition)](https://www.w3.org/TR/owl2-syntax/). Boris Motik; Peter Patel-Schneider; Bijan Parsia. W3C. 11 December 2012. W3C Recommendation. URL: <https://www.w3.org/TR/owl2-syntax/>

[rdf12-concepts]

[RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/). Andy Seaborne; Gregg Kellogg; Olaf Hartig; Pierre-Antoine Champin. W3C. 7 April 2026. W3C Candidate Recommendation. URL: <https://www.w3.org/TR/rdf12-concepts/>

[rdf12-turtle]

[RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/). Gregg Kellogg; Andy Seaborne; Dominik Tomaszuk. W3C. 7 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-turtle/>

[REC-xml-names]

[Namespaces in XML 1.0 (Third Edition)](https://www.w3.org/TR/xml-names/). Tim Bray; Dave Hollander; Andrew Layman; Richard Tobin; Henry Thompson et al. W3C. 8 December 2009. W3C Recommendation. URL: <https://www.w3.org/TR/xml-names/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/info/rfc2119/). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc2119/>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/info/rfc8174/). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc8174/>

[shacl12-core]

[SHACL 1.2 Core](https://www.w3.org/TR/shacl12-core/). Holger Knublauch; Thomas Bergwinkl; Yousouf Taghzouti; Jesse Wright. W3C. 14 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/shacl12-core/>

[shacl12-inference-rules]

[SHACL 1.2 Inference Rules](https://www.w3.org/TR/shacl12-inference-rules/). Holger Knublauch; Simon Steyskal; Scott Henninger; Livio Robaldo; Matt Goldberg. W3C. 17 September 2026. FPWD. URL: <https://www.w3.org/TR/shacl12-inference-rules/>

[shacl12-node-expr]

[SHACL 1.2 Node Expressions](https://www.w3.org/TR/shacl12-node-expr/). Robert David; Holger Knublauch; Simon Steyskal. W3C. 21 July 2026. W3C Working Draft. URL: <https://www.w3.org/TR/shacl12-node-expr/>

[sparql12-query]

[SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/). Olaf Hartig; Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 11 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-query/>

[vc-data-model]

[Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/). Ivan Herman; Michael Jones; Manu Sporny; Ted Thibodeau Jr; Gabe Cohen. W3C. 15 May 2025. W3C Recommendation. URL: <https://www.w3.org/TR/vc-data-model-2.0/>

#### G.2 Informative references

[shacl12-profiling]

[SHACL 1.2 Profiling](https://www.w3.org/TR/shacl12-profiling/). Nicholas Car; Scott Henninger; Yousouf Taghzouti; Alexander Nelson; Matt Goldberg. W3C. 2 July 2026. FPWD. URL: <https://www.w3.org/TR/shacl12-profiling/>

[shacl12-sparql]

[SHACL 1.2 SPARQL-Related Features](https://www.w3.org/TR/shacl12-sparql/). Holger Knublauch; Matt Goldberg; Scott Henninger; Livio Robaldo. W3C. 11 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/shacl12-sparql/>

[shacl12-ui]

[SHACL 1.2 User Interfaces](https://www.w3.org/TR/shacl12-ui/). Thomas Bergwinkl; Edmond Chuc; Ieben Smessaert; Daniël Beeke. W3C. 26 May 2026. FPWD. URL: <https://www.w3.org/TR/shacl12-ui/>

[sparql12-federated-query]

[SPARQL 1.2 Federated Query](https://www.w3.org/TR/sparql12-federated-query/). Ruben Taelman; Gregory Williams. W3C. 23 April 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-federated-query/>

[sparql12-rl]

[SPARQL 1.2 RL](https://www.w3.org/TR/sparql12-rl/). Robert David; David Habgood; Andy Seaborne; Simon Steyskal. W3C. 21 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-rl/>

Permalink

**Referenced in:**

- § 1.2 Document Conventions
- § 3.1 An Example SPARQL-based Constraint
- § 3.3 Validation with SPARQL-based Constraints (2)
- § 3.3.2 Mapping of Solution Bindings to Result Properties
- § 5. Annotation Properties (2)
- § C. Potential SPARQL Definitions of SHACL Core Constraint Validators
- § C.1 sh:targetClass
- § C.2 sh:targetSubjectsOf
- § C.3 sh:targetObjectsOf

Permalink

**Referenced in:**

- § 3.1 An Example SPARQL-based Constraint (2)
- § 3.3 Validation with SPARQL-based Constraints (2)
- § 3.3.2 Mapping of Solution Bindings to Result Properties
- § 4.3 Validation with SPARQL-based Constraint Components (2) (3) (4) (5)
- § 5. Annotation Properties (2) (3) (4)
- § C.1 sh:targetClass
- § C.2 sh:targetSubjectsOf
- § C.3 sh:targetObjectsOf

Permalink

**Referenced in:**

- § 2. Prefix Declarations for SPARQL Queries (2) (3) (4) (5) (6)
- § B. Summary of Syntax Rules (2) (3)

Permalink

**Referenced in:**

- § 2. Prefix Declarations for SPARQL Queries (2) (3)
- § 3. SPARQL-based Constraints
- § 3.1 An Example SPARQL-based Constraint
- § 3.2 Syntax of SPARQL-based Constraints (2) (3) (4) (5)
- § 3.3 Validation with SPARQL-based Constraints
- § 3.3.1 Pre-bound variable $this in SPARQL Constraints
- § 3.3.2 Mapping of Solution Bindings to Result Properties (2)
- § 4. SPARQL-based Constraint Components
- § B. Summary of Syntax Rules (2) (3) (4) (5)

Permalink

**Referenced in:**

- § 1.2 Document Conventions
- § 3.2 Syntax of SPARQL-based Constraints
- § 4.3 Validation with SPARQL-based Constraint Components
- § C. Potential SPARQL Definitions of SHACL Core Constraint Validators

Permalink

**Referenced in:**

- § 3.3.1 Pre-bound variable $this in SPARQL Constraints
- § 3.3.2 Mapping of Solution Bindings to Result Properties (2)
- § 4. SPARQL-based Constraint Components
- § 4.3 Validation with SPARQL-based Constraint Components
- § B. Summary of Syntax Rules

Permalink

**Referenced in:**

- § 4.2.1 Parameter Declarations (sh:parameter) (2) (3) (4) (5) (6)
- § B. Summary of Syntax Rules (2) (3) (4)

Permalink

**Referenced in:**

- § 4.2.1 Parameter Declarations (sh:parameter)
- § 5. Annotation Properties

Permalink

**Referenced in:**

- § 3.3.2 Mapping of Solution Bindings to Result Properties
- § 4.2.1 Parameter Declarations (sh:parameter) (2) (3)
- § 4.2.2 Label Templates (sh:labelTemplate)
- § 4.3 Validation with SPARQL-based Constraint Components
- § B. Summary of Syntax Rules (2) (3)

Permalink

**Referenced in:**

- § 4.2.2 Label Templates (sh:labelTemplate)

Permalink

**Referenced in:**

- § 3.2 Syntax of SPARQL-based Constraints
- § 4.2.3.1 SELECT-based Validators (2) (3)
- § 4.3 Validation with SPARQL-based Constraint Components
- § B. Summary of Syntax Rules (2) (3) (4)

Permalink

**Referenced in:**

- § 4.2.3.2 ASK-based Validators (2)
- § 4.3 Validation with SPARQL-based Constraint Components
- § B. Summary of Syntax Rules (2)

Permalink

**Referenced in:**

- § F. Changes between the original SHACL specifications and SHACL 1.2 SPARQL-Related Features

Permalink

**Referenced in:**

- § 5. Annotation Properties (2) (3)
- § B. Summary of Syntax Rules (2) (3)

Permalink

**Referenced in:**

- § 6.1 Select Expressions (2) (3) (4) (5)
- § 7.2 Example SPARQL Functions using SPARQL-based Node Expressions
- § B. Summary of Syntax Rules (2)

Permalink

**Referenced in:**

- § 6.2 SPARQL Expr Expressions (2) (3) (4)
- § 7.2 Example SPARQL Functions using SPARQL-based Node Expressions
- § B. Summary of Syntax Rules (2)

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 1.2 Document Conventions
- § 3.3 Validation with SPARQL-based Constraints
- § 3.3.1 Pre-bound variable $this in SPARQL Constraints
- § 4.2.3.1 SELECT-based Validators
- § 4.3 Validation with SPARQL-based Constraint Components (2) (3)
- § 6.1 Select Expressions (2) (3)
- § 6.2 SPARQL Expr Expressions (2) (3)
- § A. Pre-binding of Variables in SPARQL Queries
- § C. Potential SPARQL Definitions of SHACL Core Constraint Validators
- § C.1 sh:targetClass
- § C.2 sh:targetSubjectsOf
- § C.3 sh:targetObjectsOf
