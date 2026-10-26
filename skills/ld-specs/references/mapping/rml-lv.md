---
title: "RML Logical Views"
source: https://w3id.org/rml/lv/spec
family: mapping
spec_date: 2026-10-12
fetched: 2026-10-26
---

# RML Logical Views

> Format-agnostic flattened views over nested inputs (W3C CG draft).

## Contents

- Abstract
- 1 Overview
  - 1.1 Document conventions
  - 1.2 Conformance
- 2 Problem
  - 2.1 Nested data structures
  - 2.2 Mixed data formats
  - 2.3 Joining of data sources
- 3 Logical views
  - 3.1 Logical view iterator
  - 3.2 Logical view expressions
- 4 Fields
  - 4.1 Field parents
  - 4.2 Field names
  - 4.3 Field records
  - 4.4 Field reference formulations
- 5 Logical view joins
  - 5.1 Join types
  - 5.2 Logical view join examples
    - 5.2.1 Left join
    - 5.2.2 Inner join
    - 5.2.3 Two left joins
- 6 Structural Annotations
  - 6.1 Invariance Principle
  - 6.2 IriSafe
  - 6.3 PrimaryKey
  - 6.4 Unique
  - 6.5 NotNull
  - 6.6 ForeignKey
  - 6.7 Inclusion
- A References
  - A.1 Normative references

---

## Abstract

RML logical views is an extension of the RDF Mapping Language (RML) that increases the language's capability to
construct RDF datasets from nested input data, to join data sources (also across data hierarchies),
and to handle data sources that mix source formats,
by allowing to specify a logical view: a flattened, source format-agnostic view
over one or more existing data sources.
Additionally, it provides a mechanism to express relationships between data sources,
as well as additional information about their fields, through structural annotations.

This document describes RML logical views through definitions and examples.

The version of this document is *DRAFT*.

## 1. Overview

*This section is non-normative.*

### 1.1 Document conventions

We assume readers have basic familiarity with RDF and RML concepts.

In this document, examples assume
the following namespace prefix bindings unless otherwise stated:

| Prefix | Namespace                           |
| ------ | ----------------------------------- |
| `rml:` | <http://w3id.org/rml/>              |
| `xsd:` | <http://www.w3.org/2001/XMLSchema#> |
| `:`    | <http://example.org/>               |

The examples are contained in color-coded boxes. We use the Turtle syntax [turtle] to write RDF.

\# This box contains an example input

\# This box contains an example mapping

\# This box contains the example intermediate representation

\# This box contains the example output

### 1.2 Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY* and *MUST* in this document
are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all
capitals, as shown here.

## 2. Problem

*This section is non-normative.*

RML Logical Views aims to resolve challenges such as handling hierarchy of nested data, more flexible joining (also across data hierarchies), and handling data sources that mix source formats.

### 2.1 Nested data structures

References to nested data structures, like JSON or XML, may return multiple values. These values can be composite: they may again contain multiple values.
[RML-Core] defines mapping constructs that produce results by combining the results of other mapping constructs in a specific order.
For example, a [triples map](https://w3id.org/rml/core/spec#dfn-triples-map) combines the results of a [subject map](https://w3id.org/rml/core/spec#dfn-subject-map) and a [predicate-object map](https://w3id.org/rml/core/spec#dfn-predicate-object-map) in that order.
Another example is a [template expression](https://w3id.org/rml/core/spec#dfn-template-expression),
which combines character strings and zero or more [reference expressions](https://w3id.org/rml/core/spec#dfn-reference-expression) in declared order.
When mapping constructs produce multiple results, the combining mapping constructs will apply an [n-ary Cartesian product](https://w3id.org/rml/core/spec#dfn-n-ary-cartesian-product) over the sets of results, maintaining the order of the mapping constructs. In the case of nested data structures, this may cause the generation of results that do not match the source hierarchy, i.e. do not follow the root-to-leaf paths in the source data, since values are combined irrespective of it.

Furthermore, there is varying expressiveness in data source expression and query languages, and many languages have limited support for hierarchy traversal. For example, JSONPath has no operator to refer to an ancestor in the document hierarchy [RFC9535].

This limits the ability of [RML-Core](https://kg-construct.github.io/rml-core/spec/docs/) to map nested data.
> **Example:**
>
> Example 1
>
> It is not possible to declare the construction of below output triples from below data source with RML-Core.
>
> ```
> {
>   "people": [
>     {
>       "name": "alice",
>       "items": [
>         {
>           "type": "sword",
>           "weight": 1500
>         },
>         {
>           "type": "shield",
>           "weight": 2500
>         }
>       ]
>     },
>     {
>       "name": "bob",
>       "items": [
>         {
>           "type": "flower",
>           "weight": 15
>         }
>       ]
>     }
>   ]
> }
> ```
>
> ```
> :person/alice/item/sword :hasName "sword" ;
>   :hasWeight 1500 .
> :person/alice/item/shield :hasName "shield" ;
>   :hasWeight 2500 .
> :person/bob/item/flower :hasName "flower" ;
>   :hasWeight 15 .
> ```

### 2.2 Mixed data formats

Data in one format can contain multiple or composite values stored in another format, e.g. a CSV dataset could contain columns containing JSON values. To define the expected form of references to input data [RML-Core](https://kg-construct.github.io/rml-core/spec/docs/) employs the notion of a [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation). A [logical source](https://w3id.org/rml/io/spec###dfn-dfn-logical-source) is limited to having a single reference formulation, meaning mixed format data can only be referenced using a query language that supports just one of the formats.
> **Example:**
>
> Example 2
>
> It is not possible to declare the construction of below output triples from below data source with RML-Core and RML-IO.
>
> ```
> name,item
> alice,"{""type"":""sword"",""weight"": 2500}"
> alice,"{""type"":""shield"",""weight"": 1500}"
> bob,"{""type"":""flower"",""weight"": 15 }"
> ```
>
> ```
> :person/alice :hasItem "sword" , "shield" .
> :person/bob :hasItem "flower" .
> ```

### 2.3 Joining of data sources

[RML-Core](https://kg-construct.github.io/rml-core/spec/docs/) restricts join operations to [referencing object maps](https://w3id.org/rml/core/spec#referencing-object-map). Since a referencing object map can only generate an object that is an IRI or blank node subject as specified by a parent triples map, it is not possible to combine data from two sources in one term, use data from a join on another position than the object, or generate a literal using data from a join.
Moreover, [RML-Core](https://kg-construct.github.io/rml-core/spec/docs/) cannot declare join operations correctly across hierarchies.
> **Example:**
>
> Example 3
>
> It is not possible to declare the construction of below output triples from below two data sources with RML-Core.
>
> ```
> name,id
> alice,123
> bob,456
> tobias,789
> ```
>
> ```
> name,item_type
> alice,sword
> alice,shield
> bob,flower
> ```
>
> ```
> :person/123 :hasItem "sword", "shield" .
> :person/456 :hasItem "flower" .
> ```

## 3. Logical views

A *logical view* is a type of [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) that is derived from another [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) by defining fields with data from said [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source).

A logical view (`rml:LogicalView`) is represented by a resource that *MUST* contain:

- exactly one view on property (`rml:viewOn`), whose value is a [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) (`rml:AbstractLogicalSource`),
- at least one field property (`rml:field`), whose value is a field (`rml:Field`).
- zero or more join properties (`rml:leftJoin`, `rml:innerJoin`), whose value is a logical view join (`rml:LogicalViewJoin`).

A logical view (`rml:LogicalView`) has an implicit default [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) (`rml:referenceFormulation`) and [logical iterator](https://w3id.org/rml/core/spec#dfn-iterator) (`rml:iterator`), which *MUST* not be overwritten.

| Property        | Domain                           | Range                       |
| --------------- | -------------------------------- | --------------------------- |
| `rml:viewOn`    | `rml:LogicalView`                | `rml:AbstractLogicalSource` |
| `rml:field`     | `rml:LogicalView` or `rml:Field` | `rml:Field`                 |
| `rml:leftJoin`  | `rml:LogicalView`                | `rml:LogicalViewJoin`       |
| `rml:innerJoin` | `rml:LogicalView`                | `rml:LogicalViewJoin`       |

### 3.1 Logical view iterator

The [logical iterator](https://w3id.org/rml/core/spec#dfn-iterator) of a logical view produces a *logical view iteration sequence*, i.e. an ordered sequence of sets of key-value pairs.
Each set of key-value pairs represents a [logical iteration](https://w3id.org/rml/core/spec#dfn-iteration) of the logical view, called a *logical view iteration*.

Each key in a logical view iteration sequence is a string and each value is a record or a non-negative integer.
A *record* is either an iterable record or an expression record.

An *iterable record* is a [logical iteration](https://w3id.org/rml/core/spec#dfn-iteration), i.e. an item on which expressions can be evaluated.

An *expression record* is one element of an [expression evaluation result](https://w3id.org/rml/core//kg-construct.github.io/rml-core/spec/docs/#https://kg-construct.github.io/rml-core/spec/docs/#dfn-expression-evaluation-result).

A *record key* has a record as value.
Each record key is accompanied with an index key.

An *index key* has a non-negative integer as value, indicating the zero-based position of the corresponding record.

- For iterable records, the index value denotes the position in the sequence of the [logical iteration](https://w3id.org/rml/core/spec#dfn-iteration). For example: the second CSV row will be denoted with index value `1`.
- For expression records, the index value denotes the position of the element in the [expression evaluation result](https://w3id.org/rml/core//kg-construct.github.io/rml-core/spec/docs/#https://kg-construct.github.io/rml-core/spec/docs/#dfn-expression-evaluation-result). For example, JSON object `{"elements": ["a", "b", "c"]}` with JSONPath expression `$.elements[*]` will return `"a"`, `"b"`, and `"c"` as [expression evaluation result](https://w3id.org/rml/core//kg-construct.github.io/rml-core/spec/docs/#https://kg-construct.github.io/rml-core/spec/docs/#dfn-expression-evaluation-result) elements. Element `"c"` will be denoted with index value `2`.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The order of logical view iterations produced, may differ between RML processors.
> Implementations are not required to guarantee a specific or stable iteration order.
> This may result in differences in the index values of fields across different mapping executions.
> Furthermore, other [reference formulations](https://w3id.org/rml/core/spec#dfn-reference-formulation), e.g., `rml:SQLQuery`, may not have a deterministic logical iteration order, potentially leading to differences in index values across mapping executions.

A logical view iteration sequence *MUST* have a finite set of keys that appear in each logical view iteration.
In any particular logical view iteration, the value of a key *MAY* be a null value.

Each logical view iteration has at least the following keys:

- A "root" record key `<it>` with as corresponding values the iterable records produced by the [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) in the sequence defined by the [logical iterator](https://w3id.org/rml/core/spec#dfn-iterator) of the logical view.
- An accompanying "root" index key `#`.

Additional keys-value pairs with custom record keys can be defined by the fields of the logical view,
which is further detailed in 4. Fields (§4).

### 3.2 Logical view expressions

A *logical view reference* is a [reference expression](https://w3id.org/rml/core/spec#dfn-reference-expression) that references a defined referenceable key in a logical view iteration.
A *referenceable key* is either

- a record key of an expression record, or
- an index key.

A record key of an iterable record (including the record key `<it>`) cannot be referenced.

The [expression evaluation result](https://w3id.org/rml/core/spec#dfn-expression-evaluation-result) of a logical view reference is the value corresponding to the referenced key.

The [natural RDF datatype](https://w3id.org/rml/core/spec#dfn-natural-rdf-datatype) of an index key's values is [xsd:integer](https://www.w3.org/TR/xmlschema11-2/#integer).
The [natural RDF datatype](https://w3id.org/rml/core/spec#dfn-natural-rdf-datatype) of an expression record is obtained by applying the [natural mapping](https://w3id.org/rml/core/spec#dfn-natural-mapping) of the [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) used to retrieve the record.

A logical view reference can be used in [expression maps](https://w3id.org/rml/core/spec#dfn-expression-map) just as any other [reference expression](https://w3id.org/rml/core/spec#dfn-reference-expression).

When a non-existing or a non-referenceable key is referenced, RML processors should report an error.
> **Example:**
>
> Example 4
>
> ```
> :jsonView a rml:LogicalView ;
>   rml:viewOn :jsonSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name" ;
>     rml:reference "$.name" ;
>   ] ;
>   rml:field [
>     a rml:IterableField ;
>     rml:fieldName "item" ;
>     rml:iterator "$.items[*]" ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "type" ;
>       rml:reference "$.type" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "weight" ;
>       rml:reference "$.weight" ;
>     ] ;
>   ] .
> ```
>
> Note some columns in the table below have been shortened for brevity.
>
> | # | `<it>`  | name.# | name  | item.# | item                                       | item.type.# | item.type | item.weight.# | item.weight |
> | --- | ------- | ------ | ----- | ------ | ------------------------------------------ | ----------- | --------- | ------------- | ----------- |
> | 0 | `{...}` | 0      | alice | 0      | `{   "type": "sword",   "weight": 1500 }`  | 0           | sword     | 0             | 1500        |
> | 0 | `{...}` | 0      | alice | 1      | `{   "type": "shield",   "weight": 2500 }` | 0           | shield    | 0             | 2500        |
> | 1 | `{...}` | 0      | bob   | 0      | `{   "type": "flower",   "weight": 15 }`   | 0           | flower    | 0             | 15          |
>
> > **Note:**
> >
> > > **Note:**
> > >
> > > Note
> >
> > Note that this tabular representation of the logical view iteration sequence is just one possible way of representing a logical view iteration sequence.
> > The underlined keys represent referenceable keys.
>
> ```
> :triplesMapPerson a rml:TriplesMap ;
>   rml:logicalSource :jsonView ;
>   rml:subjectMap [
>     rml:template "http://example.org/person/{name}" ;
>   ] ;
>   rml:predicateObjectMap [
>     rml:predicate :hasName ;
>     rml:objectMap [
>       rml:reference "name" ;
>     ] ;
>   ] ;
>   rml:predicateObjectMap [
>     rml:predicate :hasItem ;
>     rml:objectMap [
>       rml:parentTriplesMap :triplesMapItem ;
>     ] ;
>   ] .
>
> :triplesMapItem a rml:TriplesMap ;
>   rml:logicalSource :jsonView ;
>   rml:subjectMap [
>     rml:template "http://example.org/person/{name}/item/{item.#}" ;
>   ] ;
>   rml:predicateObjectMap [
>     rml:predicate :hasName ;
>     rml:objectMap [
>       rml:reference "item.type" ;
>     ] ;
>   ] ;
>   rml:predicateObjectMap [
>     rml:predicate :hasWeight ;
>     rml:objectMap [
>       rml:reference "item.weight" ;
>     ] ;
>   ] .
> ```
>
> ```
> <http://example.org/person/alice> :hasName "alice" ;
>   :hasItem <http://example.org/person/alice/item/0> ,
>            <http://example.org/person/alice/item/1> .
>
> <http://example.org/person/bob> :hasName "bob" ;
>   :hasItem <http://example.org/person/bob/item/0> .
>
> <http://example.org/person/alice/item/0> :hasName "sword" ;
>   :hasWeight 1500 .
>
> <http://example.org/person/alice/item/1> :hasName "shield" ;
>   :hasWeight 2500 .
>
> <http://example.org/person/bob/item/0> :hasName "flower" ;
>   :hasWeight 15 .
> ```

## 4. Fields

A *field* gives a name to data derived from the [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) on which the logical view is defined.

A field (`rml:Field`) is represented by a resource that *MUST* contain:

- exactly one field name property (`rml:fieldName`), that specifies the declared name of the field
- zero or more field properties (`rml:field`), to describe nested field, also of the type `rml:Field`

| Property        | Domain                           | Range        |
| --------------- | -------------------------------- | ------------ |
| `rml:fieldName` | `rml:Field`                      | `xsd:string` |
| `rml:field`     | `rml:LogicalView` or `rml:Field` | `rml:Field`  |

There are two types of fields: an expression field and an iterable field.

An *expression field* (`rml:ExpressionField`) is a type of [expression map](https://w3id.org/rml/core/spec#dfn-expression-map).
Consequently, an expression field *MUST* have an [expression](https://w3id.org/rml/core/spec#dfn-expressions).

An *iterable field* (`rml:IterableField`) is a type of [iterable](https://w3id.org/rml/core/spec#dfn-iterable).
Consequently, an iterable field *MUST* have a [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) and a [logical iterator](https://w3id.org/rml/core/spec#dfn-iterator).
If no reference formulation is declared for an iterable field, the reference formulation of the field's parent is implied.

### 4.1 Field parents

A field *MUST* have a *parent* that is either the [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) of the logical view or another field. The parent relation *MUST* not contain cycles: it is tree-shaped with a logical view as its root. The transitive parents of a field, i.e., the field's parent, the parent of the field's parent, etcetera, are fittingly called the field's *ancestors*.
A field's *parent records* are the records defined by the field's parent.

### 4.2 Field names

A field *MUST* have a *declared name* that is an alphanumerical string. Fields with the same parent *MUST* have different declared names.
We distinguish between the field's declared name and the field's absolute name.
If a field's parent is another field, the field's *absolute name* is the concatenation of the name of the parent field, a dot `.`, and the field's declared name.
Otherwise, the field's absolute name equals its declared name.
> **Example:**
>
> Example 5
>
> In this example a field with declared name "name" is declared and added to the logical view. The parent of the field with declared name "name" is the [logical source](https://w3id.org/rml/core/spec#dfn-logical-source) `:jsonSource`.
>
> ```
> {
>   "people": [
>     {
>       "name": "alice",
>       "items": [
>         {
>           "type": "sword",
>           "weight": 1500
>         },
>         {
>           "type": "shield",
>           "weight": 2500
>         }
>       ]
>     },
>     {
>       "name": "bob",
>       "items": [
>         {
>           "type": "flower",
>           "weight": 15
>         }
>       ]
>     }
>   ]
> }
> ```
>
> ```
> :jsonSource a rml:LogicalSource ;
>   rml:source :jsonFile ;
>   rml:referenceFormulation rml:JSONPath ;
>   rml:iterator "$.people[*]" .
>
> :jsonView a rml:LogicalView ;
>   rml:viewOn :jsonSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name" ;
>     rml:reference "$.name" ;
>   ] .
> ```
>
> | # | <it>                                                                                                                                                        | name.# | name  |
> | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----- |
> | 0 | `{   "name": "alice",   "items": [     {       "type": "sword",       "weight": 1500     },     {       "type": "shield",       "weight": 2500     }   ] }` | 0      | alice |
> | 1 | `{   "name": "bob",   "items": [     {       "type": "flower",       "weight": 15     }   ] }`                                                              | 0      | bob   |

### 4.3 Field records

A field defines records:

- iterable records obtained by consecutively applying the iterable field's [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) and [logical iterator](https://w3id.org/rml/core/spec#dfn-iterator) on the parent records, or
- expression records obtained by consecutively applying the expression field's [expression](https://w3id.org/rml/core/spec#dfn-expressions) on the parent records.

A field adds following keys and corresponding values to the logical view iteration sequence:

- a record key `{absoluteFieldName}` with as values the records defined by the field.
- an accompanying index key `{absoluteFieldName}.#` with as values the position of the current record in the sequence of records derived from its parent record.

> **Example:**
>
> Example 6
>
> In this example a field with declared name "item" is added to the logical view from Example 5. Additionally a nested field "type" and a nested field "weight" are added to the "item" field.
>
> ```
> :jsonView a rml:LogicalView ;
>   rml:viewOn :jsonSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name" ;
>     rml:reference "$.name" ;
>   ] ;
>   rml:field [
>     a rml:IterableField ;
>     rml:fieldName "item" ;
>     rml:iterator "$.items[*]" ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "type" ;
>       rml:reference "$.type" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "weight" ;
>       rml:reference "$.weight" ;
>     ] ;
>   ] .
> ```
>
> Note some columns in the table below have been shortened for brevity.
>
> | # | <it>    | name.# | name  | item.# | item                                       | item.type.# | item.type | item.weight.# | item.weight |
> | --- | ------- | ------ | ----- | ------ | ------------------------------------------ | ----------- | --------- | ------------- | ----------- |
> | 0 | `{...}` | 0      | alice | 0      | `{   "type": "sword",   "weight": 1500 }`  | 0           | sword     | 0             | 1500        |
> | 0 | `{...}` | 0      | alice | 1      | `{   "type": "shield",   "weight": 2500 }` | 0           | shield    | 0             | 2500        |
> | 1 | `{...}` | 0      | bob   | 0      | `{   "type": "flower",   "weight": 15 }`   | 0           | flower    | 0             | 15          |

### 4.4 Field reference formulations

For the evaluation of the expression of an expression field (`rml:ExpressionField`) on the records of the field's parent, the parent's [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) is used.
Consequently, the parent of an expression field *MUST* be an [iterable](https://w3id.org/rml/core/spec#dfn-iterable), i.e. an [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) or iterable field.

The default [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) of an iterable field (`rml:IterableField`) is the [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) of the field's parent.
If the iterable field's parent is an expression field, a [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) *MUST* be declared for the iterable field.
Declaring a new [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation), i.e. a [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) that is different from the [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) of the field's parent, is only allowed when the field's parent is an expression field.
> **Example:**
>
> Example 7
>
> In this example a logical view is defined on a [logical source](https://w3id.org/rml/core/spec#dfn-logical-source) with reference formulation `rml:JSONPath`.
> The field with declared name "items" is evaluated using this [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation).
> The nested field with declared name "item" has a declared [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) `rml:CSV` and CSV row as implicit iterator.
> Its records are a sequence of logical iterations defined by its iterator.
> The nested fields with declared name "type" and "weight" are evaluated using the reference formulation `rml:CSV` from their parent field with declared name "item".
>
> ```
> {
>   "people": [
>     {
>       "name": "alice",
>       "items": "type,weight\nsword,1500\nshield,2500"
>     },
>     {
>       "name": "bob",
>       "items": "type,weight\nflower,15"
>     }
>   ]
> }
> ```

```
:mixedJSONSource a rml:LogicalSource ;
  rml:source :mixedJSONFile ;
  rml:referenceFormulation rml:JSONPath ;
  rml:iterator "$.people[*]" .

:mixedJSONView a rml:LogicalView ;
  rml:viewOn :mixedJSONSource ;
  rml:field [
    a rml:ExpressionField ;
    rml:fieldName "items" ;
    rml:reference "$.items" ;
    rml:field [
      a rml:IterableField ;
      rml:referenceFormulation rml:CSV;
      rml:field [
        a rml:ExpressionField ;
        rml:fieldName "type" ;
        rml:reference "type" ;
      ] ;
      rml:field [
        a rml:ExpressionField;
        rml:fieldName "weight" ;
        rml:reference "weight" ;
      ] ;
    ] ;
  ] .
```

Note some columns in the table below have been shortened for brevity.

| # | <it>    | items                                | items.# | item        | item.# | item.type | item.type.# | item.weight | item.weight.# |
| --- | ------- | ------------------------------------ | ------- | ----------- | ------ | --------- | ----------- | ----------- | ------------- |
| 0 | `{...}` | type,weight\nsword,1500\nshield,2500 | 0       | sword,1500  | 0      | sword     | 0           | 1500        | 0             |
| 0 | `{...}` | type,weight\nsword,1500\nshield,2500 | 0       | shield,2500 | 1      | shield    | 0           | 2500        | 0             |
| 1 | `{...}` | type,weight\nflower,15               | 0       | flower,15   | 0      | flower    | 0           | 15          | 0             |
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Declaring a new [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) within an iterable field affects all aspects of that [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation). For example, the `rml:namespace` of `rml:XPath` can be (re)declared in an iterable field. However, it is not possible to redeclare properties defined at the [source](https://w3id.org/rml/io/spec#dfn-source) level, such as `rml:null`, `rml:compression`, or `rml:encoding`. Those properties are inherited from the [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) of the logical view.

## 5. Logical view joins

A *logical view join* (`rml:LogicalViewJoin`) is an operation that extends the logical iteration of one logical view (the child logical view) with fields derived from another logical view (the parent logical view),
using a [join condition](https://w3id.org/rml/core/spec#dfn-join).

A logical view join *MUST* contain:

- exactly one parent logical view property (`rml:parentLogicalView`), whose value is a logical view (`rml:LogicalView`) that supplies the additional fields. This is referred to as the *parent logical view*.
- at least one join condition property (`rml:joinCondition`), whose value is a [join condition](https://w3id.org/rml/core/spec#dfn-join-condition).
- at least one field property (`rml:field`), whose value is a *leaf expression field*, i.e., an expression field (`rml:ExpressionField`) without nested fields.
  This field *MUST* contain only logical view references that can be evaluated on the parent logical view.
  The declared name of this field *MUST* be different from the absolute name of every other field in the child logical view.

Similar to how [joins are defined in RML-Core](https://w3id.org/rml/core/spec#joins),
the logical view in the subject position of the join property fulfills the role of [child logical source](https://w3id.org/rml/core/spec#child-logical-source) in the [join condition(s)](https://w3id.org/rml/core/spec#dfn-join-condition), but of the logical view join, and is referred to as *child logical view*.
The parent logical view fulfills the role of the [parent logical source](https://w3id.org/rml/core/spec#parent-logical-source) in the [join condition(s)](https://w3id.org/rml/core/spec#dfn-join-condition), but of the logical view join.

| Property                | Domain                | Range                 |
| ----------------------- | --------------------- | --------------------- |
| `rml:parentLogicalView` | `rml:LogicalViewJoin` | `rml:LogicalView`     |
| `rml:joinCondition`     | `rml:LogicalViewJoin` | `rml:Join`            |
| `rml:field`             | `rml:LogicalViewJoin` | `rml:ExpressionField` |

### 5.1 Join types

The *join property* specifies the join type of the logical view join, i.e. a left join or an inner join.

A *left join* (`rml:leftJoin`) is the equivalent of a left (outer) join in SQL, where the child logical view is the left part of the join, and the parent logical view is the right part of the join. If any of the [join conditions](https://w3id.org/rml/core/spec#dfn-join-condition) evaluates to `false`, the fields from the logical view join in the extended logical iteration contain a null value.

An *inner join* (`rml:innerJoin`) is the equivalent of an inner join in SQL. If any of the [join conditions](https://w3id.org/rml/core/spec#dfn-join-condition) evaluates to `false`, the logical iteration is removed from the child logical view.

### 5.2 Logical view join examples

#### 5.2.1 Left join
> **Example:**
>
> Example 8
>
> In this example a logical view with fields built with data from the logical source `:csvSource` is joined with the logical view from Example 6.
> In case of a left join (as in the example), this results in 4 logical iterations in the logical view.
> If an inner joins would have been used, the logical view would have only 3 logical iterations.
>
> ```
> name,birthyear
> alice,1995
> bob,1999
> tobias,2005
> ```
>
> ```
> :csvSource a rml:LogicalSource ;
>   rml:source :csvFile ;
>   rml:referenceFormulation rml:CSV .
>
> :csvView a rml:LogicalView ;
>   rml:viewOn :csvSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name" ;
>     rml:reference "name" ;
>   ] ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "birthyear" ;
>     rml:reference "birthyear" ;
>   ] ;
>   rml:leftJoin [
>     rml:parentLogicalView :jsonView ;
>     rml:joinCondition [
>       rml:parent "name" ;
>       rml:child "name" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "itemType" ;
>       rml:reference "item.type" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "itemWeight" ;
>       rml:reference "item.weight" ;
>     ] ;
>   ] .
> ```
>
> | # | <it>  | name.# | name   | birthyear.# | birthyear | itemType.# | itemType | itemWeight.# | itemWeight |
> | --- | ----- | ------ | ------ | ----------- | --------- | ---------- | -------- | ------------ | ---------- |
> | 0 | (row) | 0      | alice  | 0           | 1995      | 0          | sword    | 0            | 1500       |
> | 0 | (row) | 0      | alice  | 0           | 1995      | 1          | shield   | 1            | 2500       |
> | 1 | (row) | 0      | bob    | 0           | 1999      | 0          | flower   | 0            | 15         |
> | 2 | (row) | 0      | tobias | 0           | 2005      | null       | null     | null         | null       |

#### 5.2.2 Inner join
> **Example:**
>
> Example 9
>
> When an inner join is used, the resulting logical view has only 3 logical iterations.
>
> ```
> :csvView a rml:LogicalView ;
>   rml:viewOn :csvSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name" ;
>     rml:reference "name" ;
>   ] ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "birthyear" ;
>     rml:reference "birthyear" ;
>   ] ;
>   rml:innerJoin [
>     rml:parentLogicalView :jsonView
>     rml:joinCondition [
>       rml:parent "name" ;
>       rml:child "name" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "itemType" ;
>       rml:reference "item.type" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "itemWeight" ;
>       rml:reference "item.weight" ;
>     ] ;
>   ] .
> ```
>
> | # | <it>  | name.# | name  | birthyear.# | birthyear | itemType.# | itemType | itemWeight.# | itemWeight |
> | --- | ----- | ------ | ----- | ----------- | --------- | ---------- | -------- | ------------ | ---------- |
> | 0 | (row) | 0      | alice | 0           | 1995      | 0          | sword    | 0            | 1500       |
> | 0 | (row) | 0      | alice | 0           | 1995      | 1          | shield   | 1            | 2500       |
> | 1 | (row) | 0      | bob   | 0           | 1999      | 0          | flower   | 0            | 15         |

#### 5.2.3 Two left joins
> **Example:**
>
> Example 10
>
> In this example a second logical view join is added to the logical view from Example 8. The parent logical view of this second join is derived from logical source `:additionalCsvSource` with below input data.
>
> ```
> name,id
> alice,123
> bob,456
> tobias,789
> ```
>
> ```
> :additionalCsvView a rml:LogicalView ;
>   rml:viewOn :additioncalCsvSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name" ;
>     rml:reference "name" ;
>   ] ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "id" ;
>     rml:reference "id" ;
>   ] .
>
> :csvView a rml:LogicalView ;
>   rml:viewOn :csvSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name" ;
>     rml:reference "name" ;
>   ] ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "birthyear" ;
>     rml:reference "birthyear" ;
>   ] ;
>   rml:leftJoin [
>     rml:parentLogicalView :jsonView ;
>     rml:joinCondition [
>       rml:parent "name" ;
>       rml:child "name" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "itemType" ;
>       rml:reference "item.type" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "itemWeight" ;
>       rml:reference "item.weight" ;
>     ] ;
>   ] ;
>   rml:leftJoin [
>     rml:parentLogicalView :additionalCsvView ;
>     rml:joinCondition [
>       rml:parent "name" ;
>       rml:child "name" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "id" ;
>       rml:reference "id" ;
>     ] ;
>   ] .
> ```
>
> | # | <<it> | name.# | name   | birthyear.# | birthyear | itemType.# | itemType | itemWeight.# | itemWeight | id.# | id  |
> | --- | ----- | ------ | ------ | ----------- | --------- | ---------- | -------- | ------------ | ---------- | ---- | --- |
> | 0 | (row) | 0      | alice  | 0           | 1995      | 0          | sword    | 0            | 1500       | 0    | 123 |
> | 0 | (row) | 0      | alice  | 0           | 1995      | 1          | shield   | 1            | 2500       | 0    | 123 |
> | 1 | (row) | 0      | bob    | 0           | 1999      | 0          | flower   | 0            | 15         | 0    | 456 |
> | 2 | (row) | 0      | tobias | 0           | 2005      | null       | null     | null         | null       | 0    | 789 |

## 6. Structural Annotations

*Structural annotations* provide a mechanism to express relationships between logical views, as well as additional information about fields.

Each logical view *MAY* have zero or more structural annotation properties (`rml:structuralAnnotation`), connecting the logical view to a structural annotation object (i.e., of type `rml:StructuralAnnotation`).

| Property                   | Domain            | Range                      |
| -------------------------- | ----------------- | -------------------------- |
| `rml:structuralAnnotation` | `rml:LogicalView` | `rml:StructuralAnnotation` |

Following structural annotations *MAY* be defined:

- Unique annotation (`rml:UniqueAnnotation`)
- ForeignKey annotation (`rml:ForeignKeyAnnotation`)
- NotNull annotation (`rml:NotNullAnnotation`)
- IriSafe annotation (`rml:IriSafeAnnotation`)
- PrimaryKey annotation (`rml:PrimaryKeyAnnotation`)
- Inclusion annotation (`rml:InclusionAnnotation`)

All structural annotations of a logical view *lv* *MUST* have an *on fields* property (`rml:onFields`), linking the structural annotation to a list of field names occurring in *lv*. Intuitively, property on fields specifies the fields in *lv* that are involved by the structural annotation. The semantics of this involvement depends on the specific annotation.

| Property       | Domain                     | Range      |
| -------------- | -------------------------- | ---------- |
| `rml:onFields` | `rml:StructuralAnnotation` | `rdf:List` |

### 6.1 Invariance Principle

Structural annotations provide additional information about the data that might be used by the RML processor to optimize the KG construction process. If this additional information is incorrect, then the RML processor might either fail or produce wrong results. When using structural annotations, users should make sure that the following invariance principle is satisfied:

*For any source instances, the RDF graph produced by the RML engine using an [RML mapping](https://w3id.org/rml/core/spec#dfn-rml-mapping) with annotations, and the same [RML mapping](https://w3id.org/rml/core/spec#dfn-rml-mapping) where annotations have been removed, *MUST* be the same.*

We emphasize that RML engines might exploit structural annotations, as they could totally ignore them. It is responsibility of the user to make sure that the annotations provided are indeed correct (that is, the data complies with the annotations). Sanity checks *MAY* be provided by the RML engines themselves, but this is not mandatory. Note that providing wrong annotations to an engine that takes annotations into account, for instance for applying optimizations, could result in a violation of the invariance principle, with unpredictable results.

### 6.2 IriSafe

An *IriSafe structural annotation* (`rml:IriSafeAnnotation`) on fields *F* indicates that the content of each field in *F* is [IRI safe](https://www.w3.org/TR/r2rml/#dfn-iri-safe), that is, each field in *F* does not contain any character that is not in the [`iunreserved` production](http://tools.ietf.org/html/rfc3987#section-2.2) in [RFC3987](http://tools.ietf.org/html/rfc3987).

### 6.3 PrimaryKey

A *PrimaryKey structural annotation* (`rml:PrimaryKeyAnnotation`) on fields *(f1, ..., fn)* imposes two conditions:

- no duplicate record sequences are present over the list of fields *(f1, ..., fn)*;
- No `NULL` value is admitted in any of the field *f1, ..., fn*.

Each logical view *MAY* specify AT MOST ONE PrimaryKey annotation.
> **Example:**
>
> Example 11
>
> Consider the following CSV file containing birthdays of people:
>
> ```
> name,birthyear
> alice,1995
> bob,1999
> tobias,2005
> lukas, 1986
> ```
>
> Now, assume that we know:
>
> - Attribute `name` in the CSV is "UNIQUE" and "NOT NULL";
> Such a constraint naturally corresponds to the notion of `PRIMARY KEY` from the world of relational databases. This fact could be valuable information for the RML engine, especially in the virtual setting. However, CSV files do not support the definition of constraints. This limitation can be addressed by using structural annotations to inform the RML engine about the presence of such constraints. We illustrate this approach with a concrete example below.
>
> First, we specify the logical source corresponding to the CSV file:
>
> ```
> :csvSource a rml:LogicalSource ;
>   rml:source :csvFile ;
>   rml:referenceFormulation rml:CSV .
> ```
>
> We are now ready to specify our logical view and associated `rml:primaryKeyAnnotation`.
>
> ```
> :csvSource a rml:LogicalView ;
>   rml:viewOn :csvSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name";
>     rml:reference "name"
>  ];
>  rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "birthday";
>     rml:reference "birthday"
>  ];
>  rml:structuralAnnotation [
>     a rml:primaryKeyAnnotation;
>     rml:onFields ("name")
>  ].
> ```

### 6.4 Unique

The *Unique structural annotation* (`rml:UniqueAnnotation`) is analogous to the notion of *UNIQUE constraints* in databases. Specifically, a Unique annotation on fields *(f1, ..., fn)* imposes the following condition:

- no duplicate record sequences are present over the list of fields *(f1, ..., fn)*.

Note that every PrimaryKey annotation is, as a matter of fact, also a Unique annotation.

### 6.5 NotNull

The *NotNull structural annotation* (`rml:NotNullAnnotation`) is analogous to the notion of *NOT NULL constraints* in databases. Specifically, a NotNull annotation on fields *F* imposes that each field in *F* does not contain NULL values.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Note that every PrimaryKey annotation is, as a matter of fact, also a NotNull annotation.

### 6.6 ForeignKey

The *ForeignKey structural annotation* (`rml:ForeignKeyAnnotation`) is analogous to the notion of *foreign key constraint* in databases. Specifically, a ForeignKey annotation on fields *(f1, ..., fn)* , target view *lv*, and target fields *(tf1,...,tfn)* imposes the following conditions:

- each NULL-free record sequence over the list of fields *(f1, ..., fn)* occurs also as a record sequence in *(tf1,...,tfn)*;
- Target view *lv* defines a Unique annotation on fields *(tf1,...,tfn)*.

The *target view* is a logical view specified through the property `rml:targetView`, whereas the *target fields* are an RDF list of field names specified through the property `rml:targetFields`. These two properties are specified as follows:

| Property           | Domain                     | Range             |
| ------------------ | -------------------------- | ----------------- |
| `rml:targetView`   | `rml:ForeignKeyAnnotation` | `rml:LogicalView` |
| `rml:targetFields` | `rml:ForeignKeyAnnotation` | `rdf:List`        |

Therefore, each ForeignKey annotation *MUST* specify (additionally to the inherited `rml:onFields` property):

- Exactly one `rml:targetView` property
- Exactly one `rml:targetFields` property.

> **Example:**
>
> Example 12
>
> Consider the following JSON file containing information about warriors.
>
> ```
> {
>   "people": [
>     {
>       "name": "alice",
>       "items": [
>         {
>           "type": "sword",
>           "weight": 1500
>         },
>         {
>           "type": "shield",
>           "weight": 2500
>         }
>       ]
>     },
>     {
>       "name": "bob",
>       "items": [
>         {
>           "type": "flower",
>           "weight": 15
>         }
>       ]
>     }
>   ]
> }
> ```
>
> Now, assume that we know:
>
> - Attribute `name` in the CSV of Example 11 is "UNIQUE" and "NOT NULL";
> - All warriors in our domain are contained in the JSON of Example 12.
> The first constraint naturally corresponds to the notion of `PRIMARY KEY` from the world of relational databases. This fact could be valuable information for the RML engine, especially in the virtual setting. However, note that constraints cannot be expressed on CSV files.
>
> The second constraint naturally corresponds to a `FOREIGN KEY` constraint from the world of relational databases. However, as the involved values spread across different (and diverse) sources, it cannot be expressed as such. Also this one could provide valuable information for the RML engine.
>
> We can exploit the mechanism of structural annotations to inform the RML engine about the existence of such "relational-like" constraint. We here work out an example.
>
> First, we need to specify the logical sources. The logical source corresponding to the CSV of Example 11:
>
> ```
> :csvSource a rml:LogicalSource ;
>   rml:source :csvFile ;
>   rml:referenceFormulation rml:CSV .
> ```
>
> The logical source corresponding to the JSON of Example 12:
>
> ```
> :jsonSource a rml:LogicalSource ;
>   rml:source :jsonFile ;
>   rml:referenceFormulation rml:JSONPath ;
>   rml:iterator "$.people[*]" .
> ```
>
> We are now ready to specify our logical views, and associated structural annotations. The first logical view is the one corresponding to `:csvSource`.
>
> ```
> :csvSource a rml:LogicalView ;
>   rml:viewOn :csvSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name";
>     rml:reference "name"
>  ];
>  rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "birthday";
>     rml:reference "birthday"
>  ];
>  rml:structuralAnnotation [
>     a rml:PrimaryKeyAnnotation;
>     rml:onFields ("name");
>  ].
> ```
>
> Now, we declare the logical view corresponding to `:jsonSource`. Note that this view contains a `rml:ForeignKeyAnnotation`:
>
> ```
> :jsonView a rml:LogicalView ;
>   rml:viewOn :jsonSource ;
>   rml:field [
>     a rml:ExpressionField ;
>     rml:fieldName "name" ;
>     rml:reference "$.name" ;
>   ] ;
>   rml:field [
>     a rml:IterableField ;
>     rml:fieldName "item" ;
>     rml:iterator "$.items[*]" ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "type" ;
>       rml:reference "$.type" ;
>     ] ;
>     rml:field [
>       a rml:ExpressionField ;
>       rml:fieldName "weight" ;
>       rml:reference "$.weight" ;
>     ]
>   ] ;
>   rml:structuralAnnotation [
>     a rml:ForeignKeyAnnotation;
>     rml:onFields ("name");
>     rml:targetView :csvView;
>     rml:targetFields ("name")
>   ].
> ```

### 6.7 Inclusion

The *Inclusion structural annotation* (`rml:InclusionAnnotation`) is analogous to the notion of *inclusion dependency* in databases. Specifically, an Inclusion annotation on fields *(f1, ..., fn)* , target view *lv*, and target fields *(tf1,...,tfn)* imposes the following condition:

- each NULL-free record sequence over the list of fields *(f1, ..., fn)* occurs also as a record sequence in *(tf1,...,tfn)*;

As for ForeignKey annotation, the target view *MUST* be a logical view specified through the property `rml:targetView`, whereas the target fields *MUST* be an RDF list of field names specified through the property `rml:targetFields`.

Therefore, each inclusion annotation *MUST* specify (additionally to the inherited `rml:onFields` property):

- Exactly one `rml:targetView` property
- Exactly one `rml:targetFields` property.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> Note that every ForeignKey annotation is also an Inclusion annotation.

## A. References

### A.1 Normative references

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/info/rfc2119/). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc2119/>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/info/rfc8174/). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc8174/>

[RFC9535]

[JSONPath: Query Expressions for JSON](https://www.rfc-editor.org/info/rfc9535/). S. Gössner, Ed.; G. Normington, Ed.; C. Bormann, Ed. IETF. February 2024. Proposed Standard. URL: <https://www.rfc-editor.org/info/rfc9535/>

[RML-Core]

[RML-Core](https://w3id.org/rml/core/spec). W3C. 16 February 2024. Draft Community Group Report. URL: <https://w3id.org/rml/core/spec>

[RML-IO]

[RML-IO](https://w3id.org/rml/io/spec). W3C. 27 September 2023. Draft Community Group Report. URL: <https://w3id.org/rml/io/spec>

[turtle]

[RDF 1.1 Turtle](https://www.w3.org/TR/turtle/). Eric Prud'hommeaux; Gavin Carothers. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/turtle/>

Permalink

**Referenced in:**

- § 3. Logical views (2)
- § 3.1 Logical view iterator (2) (3) (4)
- § 4. Fields
- § 4.1 Field parents (2)
- § 4.2 Field names
- § 4.3 Field records
- § 4.4 Field reference formulations (2)
- § 5. Logical view joins (2)
- § 5.2.1 Left join
- § 5.2.3 Two left joins
- § 6. Structural Annotations
- § 6.3 PrimaryKey
- § 6.6 ForeignKey
- § 6.7 Inclusion

Permalink

**Referenced in:**

- § 3.1 Logical view iterator (2)
- § 3.2 Logical view expressions (2)
- § 4.3 Field records

Permalink

**Referenced in:**

- § 3.1 Logical view iterator (2) (3)
- § 3.2 Logical view expressions

Permalink

**Referenced in:**

- § 3.1 Logical view iterator (2)
- § 3.2 Logical view expressions
- § 4.1 Field parents
- § 4.3 Field records (2) (3) (4)

Permalink

**Referenced in:**

- § 3.1 Logical view iterator (2) (3)
- § 3.2 Logical view expressions
- § 4.3 Field records

Permalink

**Referenced in:**

- § 3.1 Logical view iterator (2)
- § 3.2 Logical view expressions (2)
- § 4.3 Field records

Permalink

**Referenced in:**

- § 3.1 Logical view iterator (2) (3)
- § 3.2 Logical view expressions (2) (3)
- § 4.3 Field records

Permalink

**Referenced in:**

- § 3.1 Logical view iterator (2)
- § 3.2 Logical view expressions (2)
- § 4.3 Field records

Permalink

**Referenced in:**

- § 3.2 Logical view expressions (2)
- § 5. Logical view joins

Permalink

**Referenced in:**

- § 3.2 Logical view expressions (2)

Permalink

**Referenced in:**

- § 3. Logical views (2)
- § 3.1 Logical view iterator
- § 4. Fields (2)
- § 4.1 Field parents (2) (3) (4) (5) (6) (7)
- § 4.2 Field names (2) (3) (4) (5) (6) (7) (8) (9) (10)
- § 4.3 Field records (2) (3) (4) (5) (6)
- § 4.4 Field reference formulations (2)

Permalink

**Referenced in:**

- § 4. Fields (2)
- § 4.3 Field records
- § 4.4 Field reference formulations (2) (3) (4)
- § 5. Logical view joins

Permalink

**Referenced in:**

- § 4. Fields (2) (3)
- § 4.3 Field records
- § 4.4 Field reference formulations (2) (3) (4) (5) (6)

Permalink

**Referenced in:**

- § 4. Fields
- § 4.1 Field parents
- § 4.2 Field names
- § 4.4 Field reference formulations (2) (3) (4) (5)

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 4.3 Field records (2) (3)

Permalink

**Referenced in:**

- § 4. Fields
- § 4.2 Field names (2) (3) (4)
- § 4.3 Field records
- § 4.4 Field reference formulations (2) (3) (4)
- § 5. Logical view joins

Permalink

**Referenced in:**

- § 4.2 Field names (2)
- § 5. Logical view joins

Permalink

**Referenced in:**

- § 3. Logical views
- § 5. Logical view joins (2) (3)
- § 5.1 Join types (2)
- § 5.2.3 Two left joins

Permalink

**Referenced in:**

- § 5. Logical view joins (2)
- § 5.1 Join types
- § 5.2.3 Two left joins

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 5. Logical view joins (2)
- § 5.1 Join types (2)

Permalink

**Referenced in:**

- § 5. Logical view joins

Permalink

**Referenced in:**

- § 5.1 Join types

Permalink

**Referenced in:**

- § 5.1 Join types

Permalink

**Referenced in:**

- § 6. Structural Annotations (2)

Permalink

**Referenced in:**

- § 6. Structural Annotations
- § 6.2 IriSafe
- § 6.3 PrimaryKey
- § 6.4 Unique
- § 6.5 NotNull
- § 6.6 ForeignKey (2)
- § 6.7 Inclusion

Permalink

**Referenced in:**

- § 6. Structural Annotations

Permalink

**Referenced in:**

- § 6. Structural Annotations
- § 6.3 PrimaryKey
- § 6.4 Unique
- § 6.5 NotNull

Permalink

**Referenced in:**

- § 6. Structural Annotations
- § 6.4 Unique (2)
- § 6.6 ForeignKey

Permalink

**Referenced in:**

- § 6. Structural Annotations
- § 6.5 NotNull (2)

Permalink

**Referenced in:**

- § 6. Structural Annotations
- § 6.6 ForeignKey
- § 6.7 Inclusion (2)

Permalink

**Referenced in:**

- § 6.6 ForeignKey
- § 6.7 Inclusion (2)

Permalink

**Referenced in:**

- § 6.6 ForeignKey
- § 6.7 Inclusion

Permalink

**Referenced in:**

- § 6. Structural Annotations
- § 6.7 Inclusion (2)
