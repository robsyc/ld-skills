---
title: "RML-FNML"
source: https://w3id.org/rml/fnml/spec
family: mapping
spec_date: 2026-03-16
fetched: 2026-10-21
---

# RML-FNML

> Declarative execution of functions in mappings (W3C CG draft).

## Contents

- Abstract
- 1 Conformance
- 2 The Problem
- 3 Definitions
  - 3.1 Generic
  - 3.2 RML
  - 3.3 FNML
- 4 Link to FnO: Overview
  - 4.1 Function Example
  - 4.2 FNML Example - shortcuts
  - 4.3 FNML Example - no shortcuts
- 5 FNML
  - 5.1 Function-valued Expression Map
  - 5.2 rml:ReturnMap
  - 5.3 rml:FunctionExecution
  - 5.4 rml:FunctionMap
  - 5.5 rml:Input
  - 5.6 rml:ParameterMap
  - 5.7 rml:functionExecution
  - 5.8 rml:returnMap
    - 5.8.1 rml:return
  - 5.9 rml:functionMap
    - 5.9.1 rml:function
  - 5.10 rml:input
  - 5.11 rml:parameterMap
    - 5.11.1 rml:parameter
  - 5.12 rml:inputValueMap
    - 5.12.1 rml:inputValue
- 6 Advanced usage
  - 6.1 Multivalue processing
  - 6.2 Nested functions
  - 6.3 Conditions
    - 6.3.1 Multivalue Conditions - example
- A References
  - A.1 Normative references
  - A.2 Informative references

---

Permalink

**Referenced in:**

- § 3.1 Generic (2) (3) (4) (5)
- § 3.3 FNML (2) (3) (4) (5) (6)
- § 4. Link to FnO: Overview (2)
- § 5.1 Function-valued Expression Map (2)
- § 5.9 rml:functionMap

Permalink

**Referenced in:**

- § 3.1 Generic (2) (3)
- § 3.3 FNML (2) (3) (4)
- § 4. Link to FnO: Overview

Permalink

**Referenced in:**

- § 3.1 Generic (2)
- § 3.3 FNML
- § 5.1 Function-valued Expression Map (2)

Permalink

**Referenced in:**

- § 3.3 FNML (2)
- § 4. Link to FnO: Overview (2)
- § 5.1 Function-valued Expression Map
- § 5.10 rml:input

Permalink

**Referenced in:**

- § 2. The Problem

Permalink

**Referenced in:**

- § 3.3 FNML (2) (3)
- § 4. Link to FnO: Overview

Permalink

**Referenced in:**

- § 3.3 FNML (2) (3) (4) (5) (6) (7) (8)
- § 4. Link to FnO: Overview
- § 5.1 Function-valued Expression Map
- § 5.12 rml:inputValueMap

Permalink

**Referenced in:**

- § 3.2 RML (2)
- § 3.3 FNML
- § 5.1 Function-valued Expression Map
- § 6.2 Nested functions

Permalink

**Referenced in:**

- § 3.3 FNML (2) (3)
- § 5.8.1 rml:return
- § 5.9.1 rml:function
- § 5.11.1 rml:parameter
- § 5.12.1 rml:inputValue

Permalink

**Referenced in:**

- § 3.3 FNML
- § 4. Link to FnO: Overview (2)
- § 4.2 FNML Example - shortcuts
- § 5.1 Function-valued Expression Map (2) (3) (4)
- § 5.7 rml:functionExecution
- § 5.8 rml:returnMap

Permalink

**Referenced in:**

- § 3.3 FNML
- § 4. Link to FnO: Overview
- § 5.2 rml:ReturnMap
- § 5.8 rml:returnMap

Permalink

**Referenced in:**

- § 3.3 FNML
- § 4. Link to FnO: Overview (2)
- § 5.3 rml:FunctionExecution
- § 5.7 rml:functionExecution
- § 5.9 rml:functionMap

Permalink

**Referenced in:**

- § 3.3 FNML
- § 4. Link to FnO: Overview
- § 5.4 rml:FunctionMap

Permalink

**Referenced in:**

- § 3.3 FNML
- § 4. Link to FnO: Overview
- § 5.5 rml:Input
- § 5.10 rml:input
- § 5.11 rml:parameterMap
- § 5.12 rml:inputValueMap

Permalink

**Referenced in:**

- § 3.3 FNML
- § 4. Link to FnO: Overview
- § 5.6 rml:ParameterMap
- § 5.11 rml:parameterMap

## Abstract

RML+FnO is an approach to provide for data transformations when generating knowledge graphs
from (semi-)structured data using the [RDF Mapping Language (RML)](https://rml.io/specs/rml/).

In RML+FnO, data transformations are defined declaratively,
supporting the [Function Ontology (FnO)](https://w3id.org/function/spec/).

This approach is not case-specific:
data transformations are independent of their implementation and thus interoperable,
while the functions are decoupled and reusable.
This allows developers to improve the generation framework
independent from the contributors that focus on generating the knowledge graphs.

## 1. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY* and *MUST* in this document
are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all
capitals, as shown here.

## 2. The Problem

Mapping languages allow us to define how knowledge graphs are generated from (semi-)structured data,
but only if the original data values can be used as-is.
Complex data transformations in mapping languages typically are
either implemented as custom solutions,
or are done by systems separate from the mapping process.
The former data transformations remain case-specific, often coupled with the mapping,
whereas the latter is not reusable across systems.

For example, we have a data source where all names are lowercase,
but we want the resulting knowledge to have uppercase values.
The following RML Mapping contains the descriptions to generate a knowledge graph from a data source,
but no data transformations.
> **Example:**
>
> Example 1: RML Mapping without data transformations
>
> ```
> @prefix rml: <http://w3id.org/rml/> .
> @prefix ex: <http://example.com/> .
>
> <#Person_Mapping>
>     rml:logicalSource <#LogicalSource> ; # Specify the data source
>     rml:subjectMap <#SubjectMap> ;       # Specify the subject
>     rml:predicateObjectMap [             # Specify the predicate-object-map
>         rml:predicate ex:title ;         # Specify the predicate
>         rml:objectMap [                  # Specify the object-map
>             rml:reference "name"         # Specify the reference within the data source
>         ]
>     ] .
> ```

## 3. Definitions

### 3.1 Generic

[RML]-independent defintions:

- A *Function*: an implementation-independent declaration of a function,
  specified using multiple parameters and multiple returns.
  For example, a Function can be declared as follows: `function int sum(int a, int b) throws StackOverFlowException`, namely,
  the Function `sum` has two input parameters, `int a` and `int b`, and returns an `int` or throws a `StackOverFlowException`.
- A *Parameter*: an input parameter of a Function.
- A *Return*: an output return of a Function.
- An *Execution*: an invocation of a Function.
  Concrete values are bound to the input Parameters,
  and concrete values are bound to the Returns after execution.
  For example, `sum(2, 4) = 6` is an execution,
  where `2` is bound to the `a` Parameter, `4` is bound to the `b` Parameter, and `6` is bound as Return value.

### 3.2 RML

Definitions taken from [RML] or [R2RML: RDB to RDF Mapping Language](https://www.w3.org/TR/r2rml/):

- An *RML mapping*: defined in [RML] at <http://w3id.org/rml/core/spec/>.
- A *Triples Map*: defined in [RML] at <http://w3id.org/rml/core/spec/>.
- A *Term Map*: defined in [RML] at <http://w3id.org/rml/core/spec/>.
- a *Expression Map*: defined in [RML] at <http://w3id.org/rml/core/spec/>.
- A *constant expression shortcut property*: defined in [RML] at <http://w3id.org/rml/core/spec/>.

Within this specification, the Expression Map definition is extended by adding new possible properties and thus also a new type of Expression Map.
The change is included below with changes highlighted in bold.

---

An Expression Map can have the following properties:

- 0 or 1 rml:constant
- 0 or 1 rml:reference
- 0 or 1 rml:template
- **0 or 1 rml:functionExecution**

---

### 3.3 FNML

- A *Function-valued Expression Map*: an Expression Map, where the generated term is one specific returned output (of an Execution).
  * This allows to reuse the same execution in different locations of the Triples Map, and potentially use different outputs of the same execution.
  * It links to a Function Execution and a Return Map.
- A *Return Map*: a Term Map that *MUST* generate a named node. That named node specifies the Return of the referenced Function.
  * This can also be specified using a constant expression shortcut property.
  * This can also be omitted, if so, the first return value as specified in the Function is used.
- A *Function Execution*: a construct that provides a way to bind concrete values to Parameters of a Function.
  The Function is specified using an Function Map and the Parameters are specified using Inputs.
  * As such, an Function Execution can be seen as a way to describe Executions.
- An *Function Map*: a Term Map that *MUST* generate a named node. That named node specifies the referenced Function.
  * This can also be specified using a constant expression shortcut property.
- An *Input*: a construct to pairwise connect a value (via a Term Map) to a Parameter Map.
  * This Term Map generates the input value that should be bound to the Parameter of the referenced Function.
  * This Term Map refers to values from the Triples Maps iteration.
    Note that these Term Maps are handled just like regular Term Maps within a Triples Map: [The references of all Term Maps of a Triples Map (Subject Map, Predicate Maps, Object Maps, Graph Maps) must be references to records that exist in the Triples Map's logical source](http://w3id.org/rml/core/spec/).
- A *Parameter Map*: a Term Map that *MUST* generate a named node. That named node specifies the referenced Parameter.
  * This can also be specified using a constant expression shortcut property.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> It is currently assumed that a Function-valued Expression Map always returns an RDF term [rdf-concepts].
> How a list of RDF terms is handled, is out of scope of this spec, but discussed at [Collections and Containers in RML](https://w3id.org/kg-construct/collections-containers).

## 4. Link to FnO: Overview

Instead of integrating a specific set of functions in [RML],
we combine [RML] with declarative function descriptions in [FnO].

Within [FnO], Functions and Executions are described.
Within FNML, we refer to Executions that link to specific Functions.

Triples Maps generate output triples from input data.
We use an intermediate Function-valued Expression Map to use a specific output (via a Return Map) of a Function Execution.
That Function Execution specifies which [FnO] function to use (via a Function Map)
and uses Inputs to link input data (via regular [RML] Term Maps)
to Parameters (via Parameter Maps).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> If an execution returns multiple returning outputs (eg, a result and a status code),
> by referring to the same execution,
> you can use both outputs in different locations of the same mapping.
> If you leave out the intermediate Function-valued Expression Map, you don't allow for reuse,
> which means that you cannot specify the difference between
> 'using 2 outputs from one execution' vs 'use a different output from 2 different executions'.

### 4.1 Function Example

We use Example 1,
where we want to perform an uppercase operation to a set of fields.

The FnO description of the function [toUppercase](https://openrefine.org/docs/manual/grelfunctions#touppercases) is as follows:
> **Example:**
>
> Example 2: toUppercase FnO description
>
> ```
> @prefix dcterms: <http://purl.org/dc/terms/> .
> @prefix fno:     <https://w3id.org/function/ontology#> .
> @prefix grel:    <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
> @prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
>
> grel:toUpperCase
>     a                   fno:Function ;
>     fno:name            "to Uppercase" ;
>     rdfs:label          "to Uppercase" ;
>     dcterms:description "Returns the input with all letters in upper case." ;
>     fno:expects         ( grel:valueParam ) ;
>     fno:returns         ( grel:stringOut ) .
>
> grel:valueParam
>     a             fno:Parameter ;
>     fno:name      "input value" ;
>     rdfs:label    "input value" ;
>     fno:predicate grel:valueParameter ;
>     fno:type      xsd:string ;
>     fno:required  "true"^^xsd:boolean .
>
> grel:stringOut
>     a             fno:Output ;
>     fno:name      "output string" ;
>     rdfs:label    "output string" ;
>     fno:predicate grel:stringOutput ;
>     fno:type      xsd:string .
> ```

The execution of such a function converts a string to its uppercase sibling,
so `test` becomes `TEST` and `This is an input STRING.` becomes `THIS IS AN INPUT STRING.`.
The latter would be described as follows using an FnO Execution description:
> **Example:**
>
> Example 3: toUppercase FnO execution description
>
> ```
> @prefix fno:     <https://w3id.org/function/ontology#> .
> @prefix grel:    <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
> @prefix :        <http://example.com/> .
>
> :exe a fno:Execution ;
>     fno:executes grel:toUppercase ;
>     grel:valueParameter "This is an input STRING." ;
>     grel:stringOutput "THIS IS AN INPUT STRING." .
> ```

### 4.2 FNML Example - shortcuts

To connect this function with the RML mapping document, we make use of FNML, see below for an example, which makes maximal use of shortcuts.

```
predicateObjectMap subjectMap predicate objectMap execution return function input parameter valueMap template triples map predicate-object map function-valued expression map Function Execution grel:stringOut grel:toUpperCase Input grel:valueParam term map {lastname}
```

*Figure 1 Visual overview of connections FNML*
> **Example:**
>
> Example 4: using toUppercase in an RML mapping
>
> ```
> @prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
> @prefix rml: <http://w3id.org/rml/> .
> @prefix ex: <http://example.com/> .
>
> <#Person_Mapping>
>     rml:logicalSource <#LogicalSource> ;
>     rml:subjectMap <#SubjectMap> ;
>     rml:predicateObjectMap <#NameMapping> .
>
> <#NameMapping>
>     rml:predicate ex:title ;
>     rml:objectMap [                          # A function-valued expression map
>         rml:functionExecution <#Execution> ; # Link to a Function Execution
>         rml:return grel:stringOut            # Specify which return of the referenced function to use, if omitted, the first specified return is used
>     ] .
>
> <#Execution> a rml:FunctionExecution ;       # A new class
>     rml:function grel:toUppercase ;          # Specify which FnO function
>     rml:input [                              # Specify the inputs
>         a rml:Input ;                        # A new class
>         rml:parameter grel:valueParam ;      # Specify this specific parameter
>         rml:inputValueMap [                  # Link to the term map that creates the input value
>             rml:reference "name"             # Specify the reference within the data source
>         ]
>     ] .
> ```

The `name`-value is not referenced directly,
instead, its value is used as `grel:valueParam`-parameter
for the `grel:toUppercase`-function.
After execution, the `grel:stringOut` result of that function is returned to generate the object
within the `<#NameMapping>`.
We make use of an intermediate Function-valued Expression Map so that we can reuse the returning output of an execution in multiple TermMaps.

### 4.3 FNML Example - no shortcuts

The same example, but written without shortcuts, is as follows:
> **Example:**
>
> Example 5: using toUppercase in an RML mapping without shortcuts
>
> ```
> @prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
> @prefix rml: <http://w3id.org/rml/> .
> @prefix ex: <http://example.com/> .
>
> <#Person_Mapping>
>     rml:logicalSource <#LogicalSource> ;       # Specify the data source
>     rml:subjectMap <#SubjectMap> ;             # Specify the subject
>     rml:predicateObjectMap <#NameMapping> .    # Specify the predicate-object-map
>
> <#NameMapping>
>     rml:predicate ex:title ;                   # Specify the predicate
>     rml:objectMap [                            # Specify the object-map: a function-valued expression map
>         rml:functionExecution <#Execution> ;   # Link to a Function Execution
>         rml:returnMap [
>             a rml:ReturnMap ;
>             rml:constant grel:stringOut        # Specify which return of the referenced function to use
>         ]
>     ] .
>
> <#Execution> a rml:FunctionExecution ;         # A new class
>     rml:functionMap [
>         a rml:FunctionMap ;
>         rml:constant grel:toUppercase          # Specify which FnO function
>     ] ;
>     rml:input                                  # Specify the inputs
>         [
>             a rml:Input ;                      # A new class
>             rml:parameterMap [
>                 a rml:ParameterMap ;
>                 rml:constant grel:valueParam ; # Specify this specific parameter
>             ] ;
>             rml:inputValueMap [                # Link to the term map that creates the input value
>                 a rml:TermMap ;
>                 rml:reference "name"           # Specify the reference within the data source
>             ]
>         ] .
> ```

## 5. FNML

We use terms defined in the FNML ontology to link [RML] with [FNO].

The ontology namespace is <http://w3id.org/rml/>,
the preferred prefix is `rml:`.
See below for how FNML introduced terms align with RML Core.

![FNML diagram](https://kg-construct.github.io/rml-fnml/spec/docs/resources/diagram.png)

*Figure 2 Visual overview of how FNML introduced terms align with RML Core*

### 5.1 Function-valued Expression Map

A Function-valued Expression Map is an Expression Map that is represented by a resource that has exactly one `rml:functionExecution`.
The value of the `rml:functionExecution` property must be a valid Execution.

As a consequence, the default [RML] processing **is extended**,
specifically concerning the [default term type depending on whether the Term Map is an Object Map or not](https://w3id.org/rml/core/spec),
namely, the Function-valued Expression Maps default [term type](http://w3id.org/rml/core/spec) is `rml:Literal`.
The change is included below with changes highlighted in bold.

---

If the Term Map does not have a `rml:termType` property, then its [term type](http://w3id.org/rml/core/spec) is:

- `rml:Literal`, if it is an [Object Map](http://w3id.org/rml/core/) and at least one of the following conditions is true:
  * It is a [reference-valued Term Map](http://w3id.org/rml/core/spec), **or a Function-valued Expression Map**
  * It has a `rml:languageMap` and/or `rml:language` property (and thus a [Language Map](http://w3id.org/rml/core/spec) and/or a [specified language tag](http://w3id.org/rml/core)).
  * It has a `rml:datatype` property (and thus a [specified datatype](http://w3id.org/rml/core/spec)).
- `rml:IRI`, otherwise.

---

A Function-valued Expression Map *MUST* have exactly one `rml:functionExecution` relation.
Further, it *MAY* have following relations specified:

- `rml:termType`: for processing, see paragraph above
- `rml:language` OR `rml:languageMap` OR `rml:datatype`: for processing, see [RML Language Tags](http://w3id.org/rml/core/spec/) and [RML Typed Literals](http://w3id.org/rml/core/spec/)
- `rml:return`: this relationship *MUST* refer to exactly one of the Returns as specified by the Function. This signifies which result of the execution to use. The default value is the first Return value as specified by the Function.

> **Issue:**
>
> > **Issue:**
> >
> > Issue
>
> A [proper term map definition in RML is pending](https://github.com/kg-construct/rml-core/issues/12).
> For now, we refer to the R2RML spec, but it is assumed these references will be updated based on the evolution of RML.
> This also means that all changes to existing definitions such as `term type` etc. are complementary to this specification.

### 5.2 rml:ReturnMap

See Return map.

### 5.3 rml:FunctionExecution

See Function Execution.

### 5.4 rml:FunctionMap

See Function map.

### 5.5 rml:Input

See Input.

### 5.6 rml:ParameterMap

See Parameter map.

### 5.7 rml:functionExecution

Links function-valued expression map with Function Execution.

Domain: rml:ExpressionMap

Range: rml:FunctionExecution

### 5.8 rml:returnMap

Links function-valued expression map with Return map.

Domain: rml:ExpressionMap

Range: rml:ReturnMap

#### 5.8.1 rml:return

constant expression shortcut property of rml:returnMap.

### 5.9 rml:functionMap

Links a Function Execution with Function.

Domain: rml:FunctionExecution

Range: rml:FunctionMap

#### 5.9.1 rml:function

constant expression shortcut property of rml:functionMap.

### 5.10 rml:input

Links Execution with Inputs

### 5.11 rml:parameterMap

Links Input with Parameter map.

Domain: rml:Input

Range: rml:ParameterMap

#### 5.11.1 rml:parameter

constant expression shortcut property of rml:parameterMap

### 5.12 rml:inputValueMap

Links Input with a term map.

Domain: rml:Input

Range: rml:TermMap

#### 5.12.1 rml:inputValue

constant expression shortcut property of rml:inputValueMap
> **Advisement:**
>
> Best Practice 1: Joining using data transformations
>
> When you specifically want to have join conditions, you should use functions within [rml:joinCondition](https://www.w3.org/TR/r2rml/#foreign-key),
> see, e.g. test case [RMLFNOTC0019](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0019-CSV).

## 6. Advanced usage

### 6.1 Multivalue processing

Aligned with the other RML specifications,
multivalue expression evaluation results are processed in sequence.
So, if a multivalue expression evaluation contains the multivalue `"a"`, `"b"`, and `"c"`,
the function is applied to each individual value in that order.

### 6.2 Nested functions

As the values of a function are represented using Expression Maps,
it is possible to nest functions: you generate a term in a first function, and that term is used as an parameter value in a second function.
> **Issue:**
>
> > **Issue:**
> >
> > Issue
>
> For an old example, see [RMLFNOTC0018](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0018-CSV).
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 3](https://github.com/kg-construct/rml-fnml/issues/3): Feature: how to nest a joincondition inside a function?
>
> For now, it is unclear how to handle a nested function where that nested Triples Map contains a join condition.
> **Example:**
>
> Example 6: usage of nested function
>
> ```
> @prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
> @prefix rml: <http://w3id.org/rml/> .
> @prefix ex: <http://example.com/> .
>
> <#Person_Mapping>
>     rml:logicalSource <#LogicalSource> ;
>     rml:subjectMap <#SubjectMap> ;
>     rml:predicateObjectMap <#NameMapping> .
>
> <#NameMapping>
>     rml:predicate ex:title ;
>     rml:objectMap [
>         rml:functionExecution <#Execution> ;
>         rml:return grel:stringOut
>     ] ;
>     .
>
> <#Execution> a rml:FunctionExecution ;
>     rml:function grel:toUppercase ;
>     rml:input
>         [
>             a rml:Input ;
>             rml:parameter grel:valueParam ;
>             rml:inputValueMap [
>                 rml:functionExecution <#Execution2> ; # Link to another function-valued expression map to nest functions
>                 rml:return grel:stringOut
>             ]
>         ] .
>
> <#Execution2> a rml:FunctionExecution ;               # First, replace spaces with dashes from the `name` reference
>     rml:function grel:string_replace ;
>     rml:input
>         [
>             a rml:Input ;
>             rml:parameter grel:valueParam ;
>             rml:inputValueMap [
>                 rml:reference "name"
>             ]
>         ] ,
>         [
>             a rml:Input ;
>             rml:parameter grel:param_find ;
>             rml:inputValue " "
>         ] ,
>         [
>             a rml:Input ;
>             rml:parameter grel:param_replace  ;
>             rml:inputValue "-"
>         ] .
> ```

### 6.3 Conditions

Conditions are a shortcut to make RML mappings more intuitive, but rely on existing FNML functionality.
It is a shortcut that is applied using the `rml:condition`: an additional ExpressionMap predicate.
To be able to use this shortcut, conforming mapping engines *MUST* support following functions:

- isNull
- isNotNull
- equals: see the [SPARQL specification for definition](https://www.w3.org/TR/sparql11-query/#OperatorMapping)
- notEquals: see the [SPARQL specification for definition](https://www.w3.org/TR/sparql11-query/#OperatorMapping)
- IF

> **Note:**
>
> > **Note:**
> >
> > Note: Condition function definitions
>
> isNotNull and IF are defined below, rest is an excercise for the reader.
> The actual FnO definitions are TODO.
> **Example:**
>
> Example 7: usage of condition
>
> ```
> @prefix fns: <http://example.com/fns#> .
> @prefix rml: <http://w3id.org/rml/> .
> @prefix ex: <http://example.com/> .
>
> <#Person_Mapping>
>     rml:logicalSource <#LogicalSource> ;
>     rml:subjectMap <#SubjectMap> ;
>     rml:predicateObjectMap <#NameMapping> .
>
> <#NameMapping>
>     rml:predicate ex:title ;
>     # A condition can be defined in any expression map
>     rml:objectMap [
>         # new predicate that links to a function-valued expression map,
>         # that function MUST return a boolean
>         rml:condition [
>             rml:functionExecution [
>                 # isNotNull(parameter: X) / definition: X != NULL ? TRUE : FALSE ;
>                 rml:function fns:isNotNull ;
>                 rml:input [
>                     # The parameter that is checked for NULL
>                     rml:parameter fns:parameter ;
>                     rml:inputValueMap [
>                         rml:reference "name"
>                     ]
>                 ]
>             ] ;
>             rml:return fns:boolOut # if fno:boolOut is the first specified return, this triple can be ommitted.
>         ] ;
>         # The actual expression used if the condition returns TRUE
>         rml:constant "[a filled in title]"
>     ] .
> ```
>
> This is actually a shortcut to the following
>
> ```
> @prefix fns: <http://example.com/fns#> .
> @prefix rml: <http://w3id.org/rml/> .
> @prefix ex: <http://example.com/> .
>
> <#Person_Mapping>
>     rml:logicalSource <#LogicalSource> ;
>     rml:subjectMap <#SubjectMap> ;
>     rml:predicateObjectMap <#NameMappingExtended> .
>
> <#NameMappingExtended>
>     rml:predicate ex:title ;
>     rml:objectMap [
>         rml:functionExecution [
>             # IF(bool: X, expression: Y)
>             # Function definition: X === TRUE ? Y : NULL
>             rml:function fns:IF ;
>             rml:input [
>                 # = original condition function
>                 rml:parameter fns:boolParameter ;
>                 rml:inputValueMap [
>                     rml:functionExecution [
>                         rml:function fns:isNotNull ;
>                         rml:input [
>                             rml:parameter fns:parameter ;
>                             rml:inputValueMap [
>                                 rml:reference "name"
>                             ]
>                         ]
>                     ]
>                 ]
>             ] , [
>                 # = original expression
>                 rml:parameter fns:expressionParameter ;
>                 rml:inputValueMap [
>                     rml:constant "[a filled in title]"
>                 ]
>             ]
>         ] ;
>     ] .
> # Any custom function can be used,
> # or nested functions (eg AND/OR),
> # depending on what the engines support
> ```

#### 6.3.1 Multivalue Conditions - example

Let's take following example data

```
[
    {
        "conditionValue": [1, 0, 5],
        "values": ["a", "b", "c"]
    }
]
```

If we execute following RML mapping
> **Example:**
>
> Example 8: usage of conditions in multivalues
>
> ```
> @prefix fns: <http://example.com/fns#> .
> @prefix rml: <http://w3id.org/rml/> .
> @prefix ex: <http://example.com/> .
>
> <#Person_Mapping>
>     rml:logicalSource <#LogicalSource> ;
>     rml:subjectMap <#SubjectMap> ;
>     rml:predicateObjectMap <#NameMapping> .
>
> # Suggestion: add rml:condition predicate to expression map,
> # and conforming mapping engines MUST support following functions:
> # - isNull, isNotNull, equals, noEquals, IF
> # (isNotNull and IF are defined below, rest is an excercise for the reader)
> <#NameMapping>
>     rml:predicate ex:id ;
>     # A condition can be defined in any expression map
>     rml:objectMap [
>         # new predicate that links to a function-valued expression map,
>         # that function MUST return a boolean
>         rml:condition [
>             rml:functionExecution [
>                 # notEquals(parameter: X, compared: Y) / definition: X != Y ? TRUE : FALSE ;
>                 rml:function fns:notEquals ;
>                 rml:input [
>                     # The parameter that is checked
>                     rml:parameter fns:parameter ;
>                     rml:inputValueMap [
>                         rml:reference "conditionValue"
>                     ]
>                 ] , [
>                     # The parameter that is compared to
>                     rml:parameter fns:compared ;
>                     rml:input "0"
>                 ]
>             ] ;
>             rml:return fns:boolOut # if fno:boolOut is the first specified return, this triple can be ommitted.
>         ] ;
>         # The actual expression used if the condition returns TRUE,
>         # In this case a UUID generator function is used.
>         rml:objectMap <#ANestedFunctionThatReturnsAUUIDv4> ;
>     ] .
> ```

This will result in two triples, because in `conditionValue` you have two valid condition executions

```
<subject> ex:id "df2c61cc-6fad-435d-aa95-10761840478b" .
<subject> ex:id "44d01ee9-448f-4804-acc8-3272939494b0" .
```

## A. References

### A.1 Normative references

[FnO]

[Function Ontology (FnO)](https://w3id.org/function/spec/). IDLab - imec - Ghent University. 10 November 2021. Unofficial Draft. URL: <https://w3id.org/function/spec/>

[R2RML]

[R2RML: RDB to RDF Mapping Language](https://www.w3.org/TR/r2rml/). Souripriya Das; Seema Sundara; Richard Cyganiak. W3C. 27 September 2012. W3C Recommendation. URL: <https://www.w3.org/TR/r2rml/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

[RML]

[RDF Mapping Language (RML)](https://rml.io/specs/rml/). IDLab - imec - Ghent University. 08 October 2020. Unofficial Draft. URL: <https://rml.io/specs/rml/>

### A.2 Informative references

[CollectionsContainers]

[Collections and Containers in RML](https://w3id.org/kg-construct/collections-containers). Knowledge Graph Construction W3C Community Group. 16 August 2022. Unofficial Draft. URL: <https://w3id.org/kg-construct/collections-containers>

[rdf-concepts]

[Resource Description Framework (RDF): Concepts and Abstract Syntax](https://www.w3.org/TR/rdf-concepts/). Graham Klyne; Jeremy Carroll. W3C. 10 February 2004. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-concepts/>
