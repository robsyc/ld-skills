---
title: "SHACL 1.2 User Interfaces"
source: https://w3c.github.io/data-shapes/shacl12-ui/
family: shacl
version: "1.2"
fetched: 2026-11-02
---

# SHACL 1.2 User Interfaces

> Generating user interfaces from shapes.

## Contents

- SHACL Specifications
- Document Outline
- 1 Introduction
  - 1.1 Scope
  - 1.2 Terminology
  - 1.3 Document Conventions
- 2 RDF Abstract Model Compatibility
- 3 Getting Started with SHACL UI
  - 3.1 Data Graph Only
  - 3.2 Adding a Shapes Graph
  - 3.3 Computed Resource Labels
  - 3.4 Nested Resource Forms
  - 3.5 Summary and Next Steps
- 4 Rendering Concepts
  - 4.1 SHACL Renderer
  - 4.2 Node UI Component
  - 4.3 Property UI Component
  - 4.4 Global Configuration
- 5 Scoring System
  - 5.1 Introduction
  - 5.2 Score Conventions
  - 5.3 Scoring Graph Preparation
  - 5.4 Validation Function
  - 5.5 Matcher Function
  - 5.6 Score Function
    - 5.6.1 Processing
  - 5.7 Accept Function
  - 5.8 Widget Selection
  - 5.9 Widget Matcher Validation
- 6 Widgets
  - 6.1 Editors
  - 6.2 Viewers
- 7 Core Constraints
- 8 Property Paths
  - 8.1 View Mode
    - 8.1.1 Predicate and Inverse Paths
    - 8.1.2 Complex Paths
  - 8.2 Edit Mode
    - 8.2.1 Predicate and Inverse Paths
    - 8.2.2 Alternative Paths
    - 8.2.3 Other Complex Paths
- 9 Label and Language Resolution
  - 9.1 Language Resolution
  - 9.2 Label Resolution
    - 9.2.1 Label Property Resolution
    - 9.2.2 Property Labels
    - 9.2.3 Value Node Labels
    - 9.2.4 Local Name Resolution
- 10 Patterns
  - 10.1 Root Shapes and Entry-Point Forms
  - 10.2 Conditional Shape Selection
  - 10.3 Enumerations, Select Lists, and Autocomplete
    - 10.3.1 Fetching values from named graphs
  - 10.4 Grouping, Ordering, and Layout Hints
  - 10.5 Role-Based Shapes
  - 10.6 Default Namespace and Local Name Generation
  - 10.7 Form Messages and Error Handling
    - 10.7.1 Displaying Validation Results
- 11 Search Query
  - 11.1 shui:searchQuery
  - 11.2 Validation of Search Query Results
- 12 Built-in Widgets
  - 12.1 Editors
    - 12.1.1 shui:AutoCompleteEditor
    - 12.1.2 shui:BlankNodeEditor
    - 12.1.3 shui:BooleanEditor
    - 12.1.4 shui:DatePickerEditor
    - 12.1.5 shui:DateTimePickerEditor
    - 12.1.6 shui:DetailsEditor
    - 12.1.7 shui:EnumSelectEditor
    - 12.1.8 shui:InstancesSelectEditor
    - 12.1.9 shui:IRIEditor
    - 12.1.10 shui:NumberFieldEditor
    - 12.1.11 shui:RichTextEditor
    - 12.1.12 shui:SubClassEditor
    - 12.1.13 shui:TextAreaEditor
    - 12.1.14 shui:TextAreaWithLangEditor
    - 12.1.15 shui:TextFieldEditor
    - 12.1.16 shui:TextFieldWithLangEditor
  - 12.2 Viewers
    - 12.2.1 shui:BlankNodeViewer
    - 12.2.2 shui:DetailsViewer
    - 12.2.3 shui:HTMLViewer
    - 12.2.4 shui:HyperlinkViewer
    - 12.2.5 shui:ImageViewer
    - 12.2.6 shui:IRIViewer
    - 12.2.7 shui:LabelViewer
    - 12.2.8 shui:LangStringViewer
    - 12.2.9 shui:LiteralViewer
    - 12.2.10 shui:ValueTableViewer
- 13 Property Roles
  - 13.1 Direct Role Annotation
  - 13.2 Qualified Role Annotation
  - 13.3 Built-in Property Roles
    - 13.3.1 shui:LabelRole
    - 13.3.2 shui:DepictionRole
    - 13.3.3 shui:ClassificationRole
    - 13.3.4 shui:DescriptionRole
    - 13.3.5 shui:IconRole
  - 13.4 Definitions
    - 13.4.1 shui:PropertyRole Class
    - 13.4.2 shui:propertyRole Property
- 14 Registries
  - 14.1 Community Widget Registry
- 15 Summary of Syntax Rules from this Specification
- 16 Security Considerations
- 17 Privacy Considerations
- 18 Internationalization Considerations
- 19 Summary of SHACL Core Syntax to SHACL UI Index

---

This specification describes Shapes Constraint Language (SHACL) User
Interfaces.

This specification is published by the [Data Shapes Working Group](https://www.w3.org/groups/wg/data-shapes).

### SHACL Specifications

This specification is part of the SHACL 1.2 family of specifications. See the [SHACL 1.2 Overview](https://w3c.github.io/data-shapes/shacl12-overview/) for a more detailed introduction to them.

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

[SHACL 1.2 Compact Syntax](https://w3c.github.io/data-shapes/shacl12-cs/)

defines an RDF syntax for expressing SHACL concepts

Implementers can partially check their level of conformance with the above specifications by testing themselves
with the test cases each presents, linked to in their metadata.
Note, however, that passing all the tests in a test suite does not imply complete conformance to the specifications,
it only implies that the implementation conforms to the aspects tested by the test suite.

### Document Outline

Content.

### Introduction

RDF applications commonly provide user interfaces that allow users to view and edit RDF resources.
SHACL Core, together with vocabularies such as DASH, has often been used for this purpose by
describing the structure, constraints, labels, and presentation-relevant metadata associated with
RDF data.

SHACL User Interfaces are defined by this specification as a complementary vocabulary and rendering model for
generating forms from SHACL shapes. It introduces UI-specific concepts and processing rules for
determining widgets, resolving labels, and grouping and ordering the form components used to manage
RDF resources.

Existing SHACL shapes and RDF data can be used to generate functional forms without additional
SHACL UI annotations. SHACL UI annotations allow authors to provide more specific rendering
information, enabling implementations to generate more tailored and consistent forms.
The goal is to improve interoperability between SHACL-based form generation systems
by defining common behavior across implementations.

This specification is intended for RDF application developers, RDF data editors, and authors of SHACL
shapes who wish to generate forms for their data.

#### Scope

The scope of this specification is limited to form rendering for viewing and editing RDF resources
using SHACL Core concepts such as shapes, constraints, and property paths. It defines processing
behavior for label and language resolution, field grouping and ordering, and widget determination
for value nodes.

This specification does not define the visual styling of the user interface, including the styling of individual widgets or the form as a whole.
Although it addresses some presentation-adjacent aspects, such as field grouping through `sh:PropertyGroup` and label handling, it defines how these are processed rather than how they are displayed.

This specification also does not define broader application-level user interface features such as search, filtering, or navigation.
It does not define a protocol for updating data stores, nor does it define form submission handling, validation behavior, or error handling.
Accessibility requirements for implementations and rendered interfaces are also out of scope, though implementations are encouraged to follow relevant accessibility guidelines.

#### Terminology

Link to definitions and concepts from other docs, such as SHACL Core, RDF 1.2, etc.

Terminology used throughout this specification is taken from several
sources:

[SHACL 1.2 Core](https://w3c.github.io/data-shapes/shacl12-core/) specification

technical terms for SHACL and RDF, the latter from
[rdf12-concepts]

The SHACL & RDF terms include: *[binding](https://www.w3.org/TR/shacl/#dfn-binding)* , *[blank node](https://www.w3.org/TR/shacl/#dfn-blank-node)* , *[conformance](https://www.w3.org/TR/shacl/#dfn-conforms)* , *[constraint](https://www.w3.org/TR/shacl/#dfn-constraint)* , *[constraint component](https://www.w3.org/TR/shacl/#dfn-constraint-component)* , *[data graph](https://www.w3.org/TR/shacl/#dfn-data-graph)* , *[datatype](https://www.w3.org/TR/shacl/#dfn-datatype)* , *[failure](https://www.w3.org/TR/shacl/#dfn-failure)* , *[focus node](https://www.w3.org/TR/shacl/#dfn-focus-node)* , *[RDF graph](https://www.w3.org/TR/shacl/#dfn-rdf-graph)* , *[ill-formed](https://www.w3.org/TR/shacl/#dfn-ill-formed)* , *[IRI](https://www.w3.org/TR/shacl/#dfn-iri)* , *[literal](https://www.w3.org/TR/shacl/#dfn-literal)* , *[local name](https://www.w3.org/TR/shacl/#dfn-local-name)* , *[member](https://www.w3.org/TR/shacl/#dfn-members)* , *[node](https://www.w3.org/TR/shacl/#dfn-node)* , *[node shape](https://www.w3.org/TR/shacl/#dfn-node-shape)* , *[object](https://www.w3.org/TR/shacl/#dfn-object)* , *[parameter](https://www.w3.org/TR/shacl/#dfn-parameters)* , *[pre-binding](https://www.w3.org/TR/shacl/#pre-binding)* , *[predicate](https://www.w3.org/TR/shacl/#dfn-predicate)* , *[property path](https://www.w3.org/TR/shacl/#dfn-shacl-property-path)* , *[property shape](https://www.w3.org/TR/shacl/#dfn-property-shape)* , *[RDF term](https://www.w3.org/TR/shacl/#dfn-rdf-term)* , *[SHACL instance](https://www.w3.org/TR/shacl/#dfn-shacl-instance)* , *[SHACL list](https://www.w3.org/TR/shacl/#dfn-shacl-list)* , *[SHACL subclass](https://www.w3.org/TR/shacl/#dfn-shacl-subclass)* , *[shape](https://www.w3.org/TR/shacl/#dfn-shape)* , *[shapes graph](https://www.w3.org/TR/shacl/#dfn-shapes-graph)* , *[solution](https://www.w3.org/TR/shacl/#dfn-solution)* , *[subject](https://www.w3.org/TR/shacl/#dfn-subject)* , *[target](https://www.w3.org/TR/shacl/#dfn-target)* , *[triple](https://www.w3.org/TR/shacl/#dfn-rdf-triple)* , *[validation](https://www.w3.org/TR/shacl/#dfn-validation)* , *[validation report](https://www.w3.org/TR/shacl/#dfn-validation-report)* , *[validation result](https://www.w3.org/TR/shacl/#dfn-validation-results)* , *[validator](https://www.w3.org/TR/shacl/#dfn-validators)* , *[value](https://www.w3.org/TR/shacl/#dfn-value)* , *[value node](https://www.w3.org/TR/shacl/#dfn-value-nodes)* , *§4.4 Global Configuration* .

Language Resolution

*Language Resolution* is the process of determining and ordering the
values associated with a given subject-predicate pair, prioritizing the preferred or most relevant language
value for display.

Label Property Resolution

*Label Property Resolution* is the process of determining and ordering the
label property IRIs for label resolution, prioritizing the preferred or most relevant property
IRI for retrieval. It generates a default IRI when no suitable value exists.

Label Resolution

*Label Resolution* is the process of selecting the most appropriate
display label for an RDF resource, or generating a fallback value when no suitable value exists. It
applies to both value nodes and properties identified by `sh:path`, the latter of which is commonly used to label form elements.

The process includes label property resolution and language resolution, and considers labeling-related annotations from the shapes graph, data graph, application environment, and user preferences, to determine the best label for UI presentation.

#### Document Conventions

Within this specification, the following namespace prefix definitions
are used:

| Prefix    | Namespace                                     |
| --------- | --------------------------------------------- |
| `foaf:`   | `http://xmlns.com/foaf/0.1/`                  |
| `rdf:`    | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs:`   | `http://www.w3.org/2000/01/rdf-schema#`       |
| `schema:` | `http://schema.org/`                          |
| `sh:`     | `http://www.w3.org/ns/shacl#`                 |
| `shnex:`  | `http://www.w3.org/ns/shacl-node-expr#`       |
| `shui:`   | `http://www.w3.org/ns/shacl-ui/`              |
| `shuic:`  | `http://www.w3.org/ns/shacl-ui-community/`    |
| `skos:`   | `http://www.w3.org/2004/02/skos/core#`        |
| `sparql:` | `http://www.w3.org/ns/sparql#`                |
| `xsd:`    | `http://www.w3.org/2001/XMLSchema#`           |
| `ex:`     | `http://example.com/ns#`                      |
| `dct:`    | `http://purl.org/dc/terms/`                   |

Within this specification, the following JSON-LD context is used:

```
{
  "@context": {
    "foaf": "http://xmlns.com/foaf/0.1/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "schema": "http://schema.org/",
    "sh": "http://www.w3.org/ns/shacl#",
    "shnex": "http://www.w3.org/ns/shacl-node-expr#",
    "shui": "http://www.w3.org/ns/shacl-ui/",
    "shuic": "http://www.w3.org/ns/shacl-ui-community/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "sparql": "http://www.w3.org/ns/sparql#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "http://example.com/ns#",
    "dct": "http://purl.org/dc/terms/"
  }
}
```

Note that the URI of the graph defining the SHACL vocabulary itself is
equivalent to the namespace above, i.e., it includes the `#`. References to the SHACL vocabulary, e.g., via `owl:imports` should include the `#`.

The [Turtle serialization of the SHACL UI vocabulary](https://w3c.github.io/data-shapes/shacl12-vocabularies/shacl-ui.ttl) contains the complete SHACL UI vocabulary.

Throughout the specification, color-coded boxes containing RDF graphs
in Turtle and JSON-LD will appear. The color and title of a box
indicate whether it is a Shapes graph, a Data graph, or something
else. The Turtle specification fragments use the prefix bindings given
above. The JSON-LD specification fragments use the context given
above. Only the Turtle specifications will have parts highlighted.

\# This box represents an input shapes graph
<s> <p> <o> .

```
// This box represents an input shapes graph
```

```
{
  "@id": "ex:s",
  "ex:p": {
    "@id": "ex:o"
  }
}
```

\# This box represents an input data graph.
## When highlighting is used in the examples:
## Elements highlighted in blue are focus nodes ex:Bob a ex:Person .
## Elements highlighted in red are focus nodes that fail validation ex:Alice a ex:Person .

```
// This box represents an input data graph
```

```
{
	"@graph": [
		{
			"@id": "ex:Alice",
			"@type": "ex:Person"
		},
		{
			"@id": "ex:Bob",
			"@type": "ex:Person"
		}
	]
}
```

\# This box represents an input scoring graph

```
// This box represents an input scoring graph
```

\# This box represents an output results graph

```
// This box represents an output results graph
```

Grey boxes such as this include syntax rules that apply to the shapes graph.

`true` denotes the RDF term `"true"^^xsd:boolean`. `false` denotes the RDF
term `"false"^^xsd:boolean`.

TODO: define conformance criteria for SHACL UI implementations.

### RDF Abstract Model Compatibility

At the time of writing, RDF 1.2 is a Working Draft. This section will be reviewed and updated when RDF 1.2 becomes a W3C Recommendation.

SHACL Renderers implementing this specification MUST support RDF 1.1 and SHOULD support RDF 1.2. When RDF 1.2 is supported, and unless
stated otherwise in this document, implementations SHOULD prefer RDF 1.2 syntax and data model features over their RDF 1.1 counterparts.

When RDF 1.2 is supported, wherever this specification refers to `rdf:langString`, a SHACL Renderer also accepts an `rdf:dirLangString` value in its place. This acceptance is a SHACL UI convenience that applies to widget selection and form
input only; it does not establish an RDF subtype relationship between the two datatypes, whose value spaces (and lexical spaces) are
disjoint. Validation via `sh:datatype` remains strict: the value a widget writes back MUST conform to the datatype declared
for the property, and a property shape that admits both datatypes for validation expresses this using a list of datatypes, for example `sh:datatype ( rdf:langString rdf:dirLangString )`.

### Getting Started with SHACL UI

This section introduces the basics of SHACL UI through a simple example.
By the end, you will understand how a SHACL Renderer uses SHACL Core
concepts to generate user interface forms, and how SHACL UI annotations
can tailor those forms to your use case.

One goal of SHACL UI is to provide users with a simple way to generate
usable forms from a shapes graph and a data graph. This allows SHACL
shapes authors who are not necessarily software developers to inspect
how their shapes are interpreted as user interface forms, gather
feedback from collaborators, and prototype ideas without requiring
extensive software development effort.

#### Data Graph Only

Let's start with defining a simple data graph that we'll use
throughout this section.
> **Example:**
>
> ex:TimBL a schema:Person ;
> schema:honorificPrefix "Sir" ;
> schema:givenName "Tim" ;
> schema:additionalName "John" ;
> schema:familyName "Berners-Lee" ;
> schema:birthDate "1955-06-08"^^xsd:date ;
> .
>
> The data graph describes Sir Tim Berners-Lee using the schema.org
> vocabulary.

With just the data graph, we have enough information for a SHACL
Renderer to generate a simple editable form.

![A diagram of ex:TimBL as a form in a SHACL Renderer.](https://w3c.github.io/data-shapes/shacl12-ui/images/diagrams/shacl-renderer-data-graph.drawio.svg)

There are a few SHACL UI concepts working together to render this
form. First, the labels in the form for the resource name and its
properties use Label Resolution to generate human-readable
labels. Second, the §5 Scoring System determines the most suitable editor widgets to render, selecting `shui:DatePickerEditor` (§12.1.4) for the birth date field and `shui:TextFieldEditor` (§12.1.15) for
the remaining fields.

Here is how the SHACL Renderer applies the SHACL UI concepts in this
editable form:

- The resource `ex:TimBL` is displayed as **Tim B L**.
- The resource's properties are inherently unordered, so the
  application has chosen to display them alphabetically.
  In the next example, we will use SHACL annotations to define a more
  logical ordering.
- Given that the value of the birth date field is an `xsd:date`, the Scoring System has determined that the `shui:DatePickerEditor` widget is the most appropriate.
  Note that date widgets may display the ISO 8601 lexical value `1955-06-08` using localized date formatting. For
  example, an application configured for Australian users may choose
  to display the value as `08-06-1955`.
- All other values are `xsd:string`, so the Scoring System
  has selected `shui:TextFieldEditor` as the most
  suitable widget for them.

#### Adding a Shapes Graph

Now that we've seen how a SHACL Renderer can produce an editable form
from only a data graph, let's see how adding a shapes graph that
targets the resource affects the result.
> **Example:**
>
> ex:PersonShape a sh:NodeShape ;
> sh:targetClass schema:Person ;
> sh:property [
> sh:path schema:honorificPrefix ;
> sh:datatype xsd:string ; sh:order 0 ; sh:group ex:PersonShapeNameGroup ; sh:maxCount 1 ; ],
> [
> sh:path schema:givenName ;
> sh:datatype xsd:string ; sh:order 1 ; sh:group ex:PersonShapeNameGroup ; sh:minCount 1 ; sh:maxCount 1 ; ],
> [
> sh:path schema:additionalName ;
> sh:datatype xsd:string ; sh:order 2 ; sh:group ex:PersonShapeNameGroup ; ],
> [
> sh:path schema:familyName ;
> sh:datatype xsd:string ; sh:order 3 ; sh:group ex:PersonShapeNameGroup ; sh:minCount 1 ; sh:maxCount 1 ; ],
> [
> sh:path schema:birthDate ;
> sh:datatype xsd:date ; sh:order 4 ; sh:maxCount 1 ; ] ;
> .
>
> ex:PersonShapeNameGroup a sh:PropertyGroup ; sh:order 0 ; rdfs:label "Name" ; .
>
> This shapes graph contains a single node shape that targets the `schema:Person` class. The node shape defines nested
> property shapes with datatype constraints, cardinality constraints,
> and display ordering hints using `sh:order` and `sh:group`.

With both the data graph and shapes graph provided to the SHACL
Renderer, the editable form can use shape constraints for input
validation; see the related §10.7.1 Displaying Validation Results pattern. The renderer also uses `sh:group` and `sh:order` annotations to
control the form layout, as defined in the related §10.4 Grouping, Ordering, and Layout Hints pattern. In this example, the name-related properties
are grouped into a **Name** section and ordered
according to their `sh:order` values, while the birth
date is rendered separately because it does not belong to a group.

The same shape also introduces simple cardinality constraints. `sh:minCount 1` marks the given name and family name as
required fields, while `sh:maxCount 1` tells the renderer
that those fields and the birth date should be edited as single values.
Properties without `sh:minCount` remain optional, and
properties without `sh:maxCount 1` may be rendered with
controls for adding more than one value.

![A diagram of ex:TimBL as a form in a SHACL Renderer.](https://w3c.github.io/data-shapes/shacl12-ui/images/diagrams/shacl-renderer-shapes-graph-01.drawio.svg)

#### Computed Resource Labels

The data graph for a person contains enough information to derive a
more meaningful label. Instead of rendering the resource as **Tim B L** using local name resolution, the shapes graph
can define a node expression that computes an `rdfs:label` value from properties of the `schema:Person` instance.
Label Resolution then uses that computed value as the resource's
label.
> **Example:**
>
> ex:PersonShape a sh:NodeShape ;
> sh:targetClass schema:Person ;
> sh:property [
> sh:path schema:honorificPrefix ;
> sh:datatype xsd:string ;
> sh:order 0 ;
> sh:group ex:PersonShapeNameGroup ;
> sh:maxCount 1 ;
> ],
> [
> sh:path schema:givenName ;
> sh:datatype xsd:string ;
> sh:order 1 ;
> sh:group ex:PersonShapeNameGroup ;
> sh:minCount 1 ;
> sh:maxCount 1 ;
> ],
> [
> sh:path schema:additionalName ;
> sh:datatype xsd:string ;
> sh:order 2 ;
> sh:group ex:PersonShapeNameGroup ;
> ],
> [
> sh:path schema:familyName ;
> sh:datatype xsd:string ;
> sh:order 3 ;
> sh:group ex:PersonShapeNameGroup ;
> sh:minCount 1 ;
> sh:maxCount 1 ;
> ],
> [
> sh:path schema:birthDate ;
> sh:datatype xsd:date ;
> sh:order 4 ;
> sh:maxCount 1 ;
> ], [ sh:path rdfs:label ; sh:values [ sparql:concat ( [ shnex:pathValues schema:honorificPrefix ] " " [ shnex:pathValues schema:givenName ] " " [ shnex:pathValues schema:familyName ] ) ] ; ] ; . ex:PersonShapeNameGroup a sh:PropertyGroup ;
> sh:order 0 ;
> rdfs:label "Name" ;
> .
>
> This shapes graph now contains a new property shape with a node
> expression to compute the value for `rdfs:label`.

Note that `schema:honorificPrefix` has no `sh:minCount`, so it is
optional. The `rdfs:label` node expression should therefore handle
missing values. For brevity, this example assumes that
`schema:honorificPrefix` is always present.

The rendered form now uses the computed `rdfs:label` as
the resource label, so the resource is displayed by its full name
rather than its local name.

![A diagram of ex:TimBL as a form in a SHACL Renderer.](https://w3c.github.io/data-shapes/shacl12-ui/images/diagrams/shacl-renderer-shapes-graph-02.drawio.svg)

#### Nested Resource Forms

RDF data commonly contains relationships between resources. So far,
we have shown how a SHACL Renderer generates a form for a single
resource. In some cases, however, editing a resource is easier when
the form also includes contextual information from related resources.
The following example demonstrates this pattern.
> **Example:**
>
> ex:TimBL a schema:Person ;
> schema:honorificPrefix "Sir" ;
> schema:givenName "Tim" ;
> schema:additionalName "John" ;
> schema:familyName "Berners-Lee" ;
> schema:birthDate "1955-06-08"^^xsd:date ; schema:affiliation ex:W3C ; .
>
> ex:W3C a schema:Organization ; schema:name "World Wide Web Consortium"@en , "Consorcio World Wide Web"@es ; schema:foundingDate "1994-10-01"^^xsd:date ; schema:url <https://www.w3.org> ; .
>
> The data graph describes Sir Tim Berners-Lee and the W3C using the
> schema.org vocabulary. Because the organization name is
> language-tagged, Language Resolution can select the most
> appropriate label for the user's locale.

![A diagram of ex:TimBL as a form in a SHACL Renderer.](https://w3c.github.io/data-shapes/shacl12-ui/images/diagrams/shacl-renderer-timbl-w3c.drawio.svg)

When rendering the form for the resource `ex:TimBL`, a
property shape for `schema:affiliation` can identify the
value as an IRI using `sh:nodeKind sh:IRI`. Without an
explicit details-editor preference, the Scoring System can then render
the value using a `shui:IRIEditor` (§12.1.9), allowing the
user to reference another resource without displaying its properties.
However, it can be useful to show the `ex:W3C` resource
nested in the same view. To do this, we can configure the same
property shape to prefer the details editor.
> **Example:**
>
> ex:PersonShape a sh:NodeShape ;
> sh:targetClass schema:Person ;
> sh:property [
> sh:path schema:honorificPrefix ;
> sh:datatype xsd:string ;
> sh:order 0 ;
> sh:group ex:PersonShapeNameGroup ;
> sh:maxCount 1 ;
> ],
> [
> sh:path schema:givenName ;
> sh:datatype xsd:string ;
> sh:order 1 ;
> sh:group ex:PersonShapeNameGroup ;
> sh:minCount 1 ;
> sh:maxCount 1 ;
> ],
> [
> sh:path schema:additionalName ;
> sh:datatype xsd:string ;
> sh:order 2 ;
> sh:group ex:PersonShapeNameGroup ;
> ],
> [
> sh:path schema:familyName ;
> sh:datatype xsd:string ;
> sh:order 3 ;
> sh:group ex:PersonShapeNameGroup ;
> sh:minCount 1 ;
> sh:maxCount 1 ;
> ],
> [
> sh:path schema:birthDate ;
> sh:datatype xsd:date ;
> sh:order 4 ;
> sh:maxCount 1 ;
> ],
> [
> sh:path rdfs:label ;
> sh:values [
> sparql:concat (
> [ shnex:pathValues schema:honorificPrefix ]
> " "
> [ shnex:pathValues schema:givenName ]
> " "
> [ shnex:pathValues schema:familyName ]
> )
> ] ;
> ] ; [ sh:path schema:affiliation ; sh:nodeKind sh:IRI ; shui:editor shui:DetailsEditor ; ] ; .
>
> ex:PersonShapeNameGroup a sh:PropertyGroup ;
> sh:order 0 ;
> rdfs:label "Name" ;
> .
>
> This shapes graph now contains a new property shape for `schema:affiliation` with an IRI node kind constraint and
> a preference for the `shui:DetailsEditor` (§12.1.6) widget.

With the new property shape, the SHACL Renderer now nests the `ex:W3C` resource in the same form as the `ex:TimBL` resource.

![A diagram of ex:TimBL as a form in a SHACL Renderer.](https://w3c.github.io/data-shapes/shacl12-ui/images/diagrams/shacl-renderer-timbl-w3c-nested.drawio.svg)

#### Summary and Next Steps

This section has shown that a data graph and a SHACL Renderer are
enough to produce a usable editable form. Adding a shapes graph,
including constraints also used in ordinary SHACL validation,
allows the SHACL Renderer to use those semantics to produce more
meaningful forms.

We have only briefly touched on cardinality constraints. Other useful
but more complex topics include logical constraints and using [Dynamic SHACL](https://w3c.github.io/data-shapes/shacl12-node-expr/#dfn-dynamic-shacl) to populate the values for the enum and autocomplete editors.
You can find these in the §10 Patterns section.

### Rendering Concepts

Add conceptual model diagram on rendering concepts and how they relate
to each other as well as other concepts such as widgets.

This section explains the UI concepts and how they work together.

#### SHACL Renderer

A *SHACL Renderer* is software that processes SHACL shapes and data and dynamically generates a user-interface using one
or more node UI components. Implementations may add supplementary UI elements, such as a submit
button to save changes, controls to toggle between edit and view modes, selectors for focus node and node shape, or visualizations of validation report messages.

They may also provide:

- State management for editing, viewing, and tracking data changes
- Widget management, including widget selection strategies
- Logic for determining the initial focus node (target) and the best suited node shape
- An interface to interact with the data layer

A SHACL Renderer operates on a data graph and a shapes graph, and may also take a focus node and a node shape. When all four inputs are provided, the renderer
operates in **manual mode**. When the focus node or node shape is not provided,
the renderer may operate in **automatic mode**, in which case the application determines
appropriate values for the missing inputs.

TODO: review SHACL Renderer definition, particularly the manual and automatic mode, now that we have the scoring system defined.
> **Issue:**

#### Node UI Component

A *Node UI Component* is generated from a single focus node,
typically containing one or more property UI components. It is often derived from one or more node shapes that apply to the focus node.

#### Property UI Component

A *Property UI Component* is a combination of constraints across multiple property shapes that share the same focus node and property path.

#### Global Configuration

A shapes graph may contain a SHACL instance of the class `shui:Configuration` to define global configuration properties for rendering the UI. `sh:Graph` is a SHACL subclass of `shui:Configuration`.
The following properties can be defined for a `shui:Configuration` instance.

Parameters:

| Property                  | Summary and Syntax Rules                                                                                                                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `shui:defaultNamespace`   | The default namespace used to construct fresh user-added nodes. The value of `shui:defaultNamespace` is a Literal whose value is a valid IRI.                                                            |
| `shui:languagePreference` | The language selection for displaying labels in widgets. The value of `shui:languagePreference` is a well-formed SHACL list where all members are language tags. The preferred language is determined according to the order of priority in the list from beginning (highest) to end (lowest). An empty literal (`""`) represents no language, i.e., a string literal with no language tag. |
| `shui:timeZone`           | The time zone used to construct new terms with datatype `xsd:dateTime`. The value of `shui:timeZone` is of datatype `xsd:string` and SHOULD be an IANA time-zone identifier.                             |
| `shui:labelPreference`    | The label properties used to determine the labels to display in widgets and labels to represent node values in the widgets. The value of `shui:labelPreference` is a well-formed SHACL list where all members are [SHACL Property Paths](https://w3c.github.io/data-shapes/shacl12-core/#property-paths). The preferred label property is determined according to the order of priority in the list from beginning (highest) to end (lowest). |
| `shui:readOnlyGraph`      | The graphs that contain read-only triples. The value of `shui:readOnlyGraph` is a well-formed SHACL list where all members are IRIs. Triples contained in a read-only graph cannot be edited, e.g. because they were inferred by a reasoner. A SHACL Renderer MUST respect the read-only state of triples, indicate it accordingly in the user interface and thereby distinguish editable data from read-only data. |

> **Example:**
>
> ex:config a shui:Configuration ;
> shui:defaultNamespace "http://example.com/ns#" ;
> shui:languagePreference ("" "en" "de") ;
> shui:timeZone "Europe/Vienna" ;
> shui:labelPreference (skos:prefLabel dcterms:title rdfs:label) .

TODO: Describe the constraint collection/aggregation behaviour here for both Node and Property UI Component.

### Scoring System

#### Introduction

When generating user interfaces, it is often necessary to determine the most suitable user interface *widget* (e.g., a text input, a date picker, a checkbox) for a given value or SHACL constraint.
To achieve this, SHACL UI defines a scoring system built on top of SHACL's validation process,
providing a flexible and extensible mechanism that implementers and applications can use to determine which widgets are applicable.

Common use cases for the scoring system include:

- **Selecting widgets based on the types of value nodes** — for
  example, preferring a Date Picker widget when the value is a literal
  of type `xsd:date`.
- **Selecting widgets based on the shape's constraints** — for
  example, prefer a Boolean Select widget when the shape requires a
  boolean value via a `sh:datatype` constraint.

The scoring graph is populated with instances of `shui:WidgetMatcher`. A
`shui:WidgetMatcher` associates a widget (via `shui:widget`) with the
conditions under which it applies, expressed as SHACL shapes referenced through
`shui:shapesGraphShape` (validated against the shape node in the shapes graph)
and `shui:dataGraphShape` (validated against the focus node in the data graph).
Two kinds of matcher are defined:

- **`shui:WidgetScore`** — a matcher that additionally carries a
  `shui:score`. When its shapes match, its widget is recorded with that score
  by the §5.6 Score Function.
- **`shui:WidgetAcceptMatcher`** — a matcher used by the §5.7 Accept Function to decide whether a
  widget is applicable at all. A widget without a `shui:WidgetAcceptMatcher` is
  accepted unconditionally.

The §5.6 Score Function is the entry point to the scoring system.
It combines both kinds of matcher: a widget is returned only if one of its `shui:WidgetScore` instances
matches and the widget is accepted according to its `shui:WidgetAcceptMatcher` instances.

A widget can also be attached to a shape directly, using `shui:editor` or `shui:viewer`. Such a widget
takes part in scoring like any other: the scoring graph is expected to contain a `shui:WidgetScore`
whose `shui:shapesGraphShape` matches shapes that declare the widget in this way. §5.3 Scoring Graph Preparation supplies such a
`shui:WidgetScore` for declared widgets that have none, so that a widget attached to a shape is never
silently ignored.

#### Score Conventions

A `shui:score` is any `xsd:integer` or `xsd:decimal`. The §5.6 Score Function simply orders widgets by descending score. The absolute value of a score has no meaning of its own.

The built-in widgets nevertheless follow a small set of conventional *bands*, described below, so that the
relative order of widgets is predictable. Third-party widget authors SHOULD reuse these bands so that their
widgets interleave with the built-in ones as intended. A widget that should win over a built-in in some situation
uses a score in the same band as, or a higher band than, that built-in.

Scores are compared **globally** across the whole scoring graph, not per widget. Two widgets whose
matching `shui:WidgetScore` instances carry the same score are ordered lexicographically by the Unicode code point
values of their `shui:widget` IRIs, as defined in the §5.6 Score Function.
A band is therefore a shared frame of reference, not a guarantee of a unique position.

| Band   | Meaning                                                                                                                                                                                                  |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **40** | The shape explicitly declares this widget with `shui:editor` or `shui:viewer`. This is also the default value of `shui:defaultWidgetScore` used by §5.3 Scoring Graph Preparation for a declared widget that has no `shui:WidgetScore` of its own, so a declared widget always competes at the top of the ladder. |
| **30** | Native match: the value's datatype or node kind is exactly what the widget is designed for and the widget is the canonical choice for such values — for example an `xsd:string` value for a text field, an `xsd:date` value for a date picker, or a blank node for the blank-node viewer. |
| **20** | Strong but secondary match: a good fit for the value or shape that is not the single canonical widget for it — for example a text area for an arbitrary string, or a widget selected from the value's datatype where a more specific widget may also apply. |
| **10** | Shape-constraint match: the shape constrains the datatype or node kind (for example with `sh:datatype` or `sh:nodeKind`) even though the value itself may be absent or not yet of that type.             |
| **1**  | Last-resort fallback: the widget can technically present or edit the value but is rarely the best choice. It is offered so that some widget is always available.                                         |
| **0**  | Applicable but discouraged: the widget is included for completeness or manual override and should never be chosen as the default.                                                                        |

The built-in widgets occasionally use an intermediate score, such as `5`, to break a tie between two widgets that
would otherwise share a band. Such values are fine-tuning between the bands above and are not themselves bands.

To declare that a widget is *not* applicable under some condition, give the widget a
`shui:WidgetAcceptMatcher` whose shapes match the applicable case, rather than a `shui:WidgetScore` with a low or
negative score.

#### Scoring Graph Preparation

A widget can be attached to a shape directly, with `shui:editor` or `shui:viewer`, without the **scoring graph** saying anything about that widget. Scoring graph preparation extends the **scoring graph** with a `shui:WidgetScore` for each such widget, so that it participates in
the §5.6 Score Function like any other widget.

A scoring graph MUST be prepared by this function before it is passed to the §5.6 Score Function. Without preparation, a widget that is only
attached to a shape with `shui:editor` or `shui:viewer` is never returned.

Inputs:

- **Shapes graph** — The RDF graph containing the SHACL shapes.
- **Scoring graph** — The RDF graph containing the `shui:WidgetMatcher` definitions
  (`shui:WidgetScore` and `shui:WidgetAcceptMatcher`).

Output:

- A **prepared scoring graph** — the **scoring graph** extended with a
  `shui:WidgetScore` for each explicitly declared widget that has none.

Steps:

1. Initialize the **prepared scoring graph** as a copy of the **scoring graph**.
2. Let `D` be the value of the global configuration property `shui:defaultWidgetScore`.
   If no such value is given, let `D` be `40`, which is the score conventionally used by the
   `shui:WidgetScore` instances of the §12 Built-in Widgets that match an explicitly
   declared widget.
3. For each property `P` in `shui:editor` and `shui:viewer`
   1. Collect the set of IRI values `W` of the property `P` of the shapes in the **shapes graph**. These are the widgets that are explicitly declared on a shape. A value of `P` at a node that is not a shape does not declare a widget and is ignored. A value of `P` that is not an IRI is also ignored: a widget is identified by an IRI, and a non-IRI value
      such as a blank node cannot be matched reliably with `sh:hasValue` across graphs.
   2. For each `W`
      1. If the **scoring graph** contains an instance of `shui:WidgetScore` whose `shui:widget`
         value is `W`, continue with the next `W`. The **scoring graph** already defines how `W` is scored.
      2. Otherwise, add an instance of `shui:WidgetScore` to the **prepared scoring graph** with
         the following:
         - `W` as `shui:widget`.
         - `D` as `shui:score`.
         - As `shui:shapesGraphShape`, a `sh:NodeShape` with a single property shape whose `sh:path` is `P` and whose `sh:hasValue` is `W`.
4. Return the **prepared scoring graph**.

> **Example:**
>
> ex:PersonShapeName
> a sh:PropertyShape ;
> sh:path ex:name ;
> shui:editor ex:MyCustomEditor ;
> .
>
> The scoring graph says nothing about `ex:MyCustomEditor`, so preparation adds the following `shui:WidgetScore`, which matches exactly those shapes that declare that widget with `shui:editor`:
>
> [] a shui:WidgetScore ;
> shui:widget ex:MyCustomEditor ;
> shui:score 40 ;
> shui:shapesGraphShape [
> a sh:NodeShape ;
> sh:property [
> sh:path shui:editor ;
> sh:hasValue ex:MyCustomEditor ;
> ] ;
> ] ;
> .

The global configuration is defined by [PR #900](https://github.com/w3c/data-shapes/pull/900), which is not merged yet.
Add `shui:defaultWidgetScore` to its property table once it is.

Scoring graph preparation depends only on the **shapes graph** and the **scoring graph**,
not on a focus node or a shape node. It is therefore the same for every call of the score function over those two
graphs, and implementations MAY perform it once and reuse the result. Applying it to an already prepared scoring
graph makes no further changes.

A widget that the **scoring graph** already scores is left untouched, even when the existing
`shui:WidgetScore` instances do not cover the declared case. A scoring graph that scores a widget is expected to
also define how that widget is scored when a shape declares it, conventionally with a `shui:WidgetScore` whose
`shui:shapesGraphShape` tests the `shui:editor` or `shui:viewer` property.

#### Validation Function

The validation function used by the §5.5 Matcher Function to validate the focus node against a list of shape nodes.

Inputs:

- **Focus node** — The node to validate.
- **Target graph** — The RDF graph containing the focus node.
- **Shape node** — The SHACL shape IRI.
- **Shapes graph** — RDF graph containing the list of SHACL shapes.

Steps:

1. If **shape node** is empty, return `true`.
2. If the **focus node** is not a literal and is not a subject in the **target
   graph**, return `false`.
3. Validate the **focus node** according to standard SHACL validation with the following:
   - **Focus node** as **focus node**.
   - **Target graph** as **data graph**.
   - **Shape node** as **shape node**.
   - **Shapes graph** as **shapes graph**.
4. If the validation produces violations, return `false`.
5. If the validation conforms, return `true`.

If any SHACL validation fails due to malformed shapes, the validation function should log a warning and return `false`.
Shape validation errors should not cause the Matcher function to fail.

#### Matcher Function

The matcher function used by the §5.6 Score Function and
the §5.7 Accept Function to validate whether a widget score
applies to a given focus node and shape node.

Inputs:

- **Focus node** — The node to validate.
- **Data graph** — The RDF graph containing the focus node.
- **Shape node** — The SHACL shape IRI.
- **Shapes graph** — The RDF graph containing the list of SHACL shapes.
- **Scoring graph** — The RDF graph containing the `shui:WidgetMatcher` definitions
  (`shui:WidgetScore` and `shui:WidgetAcceptMatcher`).
- **Matcher node** — The RDF node containing the widget matcher definition, an instance of
  `shui:WidgetMatcher` (for example a `shui:WidgetScore` or a `shui:WidgetAcceptMatcher`).

Steps:

1. If no **focus node** is given, a value for the `shui:dataGraphShape` property
   is present, and no value for the `shui:shapesGraphShape` is present, return `false`.
2. Call the validation function with the following:
   - **Shape node** as **focus node**.
   - **Shapes graph** as **target graph**.
   - The value of the `shui:shapesGraphShape` property of **matcher node** as **shape node**.
   - **Scoring graph** as **shapes graph**.
3. If the function returns `false`, return `false`.
4. If no focus node is given, return `true`.
5. Call the validation function with the following:
   - **Focus node** as **focus node**.
   - **Data graph** as **target graph**.
   - The value of the `shui:dataGraphShape` property of **matcher node** as **shape node**.
   - **Scoring graph** as **shapes graph**.
6. If the function returns `false`, return `false`.
7. Otherwise, return `true`.

#### Score Function

The score function determines which widgets should be used for a given combination of a focus node and a
shape node. It is the entry point to the scoring system: it returns the widgets whose `shui:WidgetScore` matches and that are accepted according to their `shui:WidgetAcceptMatcher` instances, ordered from best to worst match.

Inputs:

- **Focus node** — The node to validate, may also be `undefined`.
- **Data graph** — The RDF graph containing the focus node.
- **Shape node** — The SHACL shape IRI.
- **Shapes graph** — The RDF graph containing the list of SHACL shapes.
- **Scoring graph** — The RDF graph containing the `shui:WidgetMatcher` definitions
  (`shui:WidgetScore` and `shui:WidgetAcceptMatcher`). It MUST be a scoring graph that has been prepared
  according to §5.3 Scoring Graph Preparation.

Output:

- An ordered sequence of **widget results**, sorted by descending `shui:score` so that
  the best match comes first. The sequence is empty if no widget matches and is accepted.

A **widget result** holds the `shui:widget` of a matching `shui:WidgetScore`,
the IRI of that `shui:WidgetScore`, and its `shui:score`.

Steps:

1. Initialize an empty ordered sequence `results`.
2. Collect instances of `shui:WidgetScore` in the **scoring graph**, sorted by `shui:score` in descending order and then lexicographically by the Unicode codepoint values of `shui:widget`.
3. For each instance `S` of type `shui:WidgetScore`, in that order
   1. Call the matcher function with the following:
      - **Focus node** as **focus node**.
      - **Data graph** as **data graph**.
      - **Shape node** as **shape node**.
      - **Shapes graph** as **shapes graph**.
      - `S` as **matcher node**.
      - **Scoring graph** as **scoring graph**.
   2. If the matcher function returns `false`, continue with the next instance.
   3. Call the accept function with the following:
      - **Focus node** as **focus node**.
      - **Data graph** as **data graph**.
      - **Shape node** as **shape node**.
      - **Shapes graph** as **shapes graph**.
      - The `shui:widget` of `S` as **widget node**.
      - **Scoring graph** as **scoring graph**.
   4. If the accept function returns `false`, continue with the next instance.
   5. Let `R` be the widget result with the following:
      - The `shui:widget` of `S`.
      - The IRI of `S`.
      - The `shui:score` of `S`.
   6. Record the widget score by appending `R` to `results`.
4. Return `results`.

A caller that only needs the best matching widget takes the first result of the sequence.
The order of the results is fixed by the `shui:score` values and `shui:widget` IRIs alone,
which are known before any widget matcher is evaluated. The score function therefore does not need to evaluate
every widget matcher in order to produce its first result, and implementations MAY produce `results` lazily — for example as an iterator or a generator — evaluating the matchers for each `shui:WidgetScore` only when the caller requests the next result. Only the matchers up to and including the first accepted widget then
have to be evaluated: if the best scoring widget is rejected by its `shui:WidgetAcceptMatcher`, the next
best is evaluated, and so on. Because widget matchers are evaluated independently of one another, lazy and eager
evaluation produce the same sequence.

Several `shui:WidgetScore` instances may share the same `shui:widget`, in which case the accept
function is called more than once for that widget with the same inputs. The accept function is deterministic for a
given focus node and shape node, so implementations MAY evaluate it once per widget and reuse the result.

##### Processing

The score function MUST raise an error and terminate the algorithm in the following scenarios:

- Any mandatory inputs are missing.
- Widget Score instances are malformed.

#### Accept Function

The accept function used by the §5.6 Score Function to check if a
widget is applicable.

Inputs:

- **Focus node** — The node to validate.
- **Data graph** — The RDF graph containing the focus node.
- **Shape node** — The SHACL shape IRI.
- **Shapes graph** — The RDF graph containing the list of SHACL shapes.
- **Widget node** — The IRI of the widget to check acceptance for.
- **Scoring graph** — The RDF graph containing the `shui:WidgetMatcher` definitions
  (`shui:WidgetScore` and `shui:WidgetAcceptMatcher`).

Steps:

1. Find the `shui:WidgetAcceptMatcher` instance `M` with a matching `shui:widget` value.
2. If no such instance `M` exists, return `true`.
3. Call the matcher function with the following:
   - **Focus node** as **focus node**.
   - **Data graph** as **data graph**.
   - **Shape node** as **shape node**.
   - **Shapes graph** as **shapes graph**.
   - `M` as **matcher node**.
   - **Scoring graph** as **scoring graph**.
4. Return the return value of the matcher function.

#### Widget Selection

The widget with the highest score SHOULD be selected as the default widget from the Scoring Algorithm results.
Implementations MAY allow users to switch to any widget included in the results.

Since multiple score entries may reference the same widget,
a post-processing step SHOULD be performed to normalize the score results (for example,
by aggregating or de-duplicating entries by widget) before presenting the widget choices to the user.

#### Widget Matcher Validation

Widget matchers are malformed if they fail to validate against the [matcher validation shapes graph](https://w3c.github.io/data-shapes/shacl12-ui/widgets/score-validator.ttl). That graph defines two shapes:

- `shui:ScoreShape` targets `shui:WidgetScore`. A well-formed `shui:WidgetScore` has exactly one
  `shui:widget` (an IRI), exactly one `shui:score` (an `xsd:decimal` or `xsd:integer`), and any
  `shui:dataGraphShape` or `shui:shapesGraphShape` it declares references a valid node.
- `shui:AcceptMatcherShape` targets `shui:WidgetAcceptMatcher`. A well-formed
  `shui:WidgetAcceptMatcher` has exactly one `shui:widget` (an IRI), no `shui:score`, and any
  `shui:dataGraphShape` or `shui:shapesGraphShape` it declares references a valid node.

### Widgets

TODO: consider moving this section under "SHACL UI Concepts".

#### Editors

The following sub-sections enumerate the currently defined instances of `shui:Editor` from the SHACL UI namespace.
Property shapes can explicitly specify the preferred editor for its values using `shui:editor`.
If no such value has been specified, the system should pick a suitable default viewer based on the §5 Scoring System outlined for each widget.

#### Viewers

The following sub-sections enumerate the currently defined instances of `shui:Viewer` from the SHACL UI namespace.
A property shape can have an explicitly specified preferred viewer for its values in `shui:viewer`.
If no such value has been specified, the system should pick a suitable default viewer based on the §5 Scoring System outlined for each widget.

Most viewers render a single RDF value on the screen, typically as a single widget.
Form editors offer buttons to edit individual values and to add or delete values.
However, some viewers need to take more complete control over how multiple values of a property at a focus node are rendered.
The only example of such a viewer in SHACL UI is `shui:ValueTableViewer` (§12.2.10), which displays
all values of a property as an HTML table.
In such cases, the notions of generic add and delete buttons do not apply.
Such viewers are called *Multi Viewers* and are declared instances of `shui:MultiViewer` instead of `shui:SingleViewer`.
The equivalent classes for editors are `shui:MultiEditor` and `shui:SingleEditor`.

### Core Constraints

TODO: This section may not be needed if we decide to fold in the use of different constraints for common form scenarios under the Patterns section.

### Property Paths

[SHACL Property Paths](https://w3c.github.io/data-shapes/shacl12-core/#property-paths) can be used to render a SHACL shape as a
user interface.
Property paths define how data values are accessed or modified relative to a focus node.

The following subsections outline the scenarios in which SHACL UI implementations are expected to
support different kinds of property paths for viewing and editing operations.

#### View Mode

In view mode, property paths are used to retrieve and display data values associated with a shape.
A SHACL UI implementation must provide mechanisms to resolve these paths for visualization.

##### Predicate and Inverse Paths

SHACL UI implementations MUST support both [predicate paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-predicate) and [inverse paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-inverse) in view mode.
This ensures that values reachable via simple forward or inverse relationships can be displayed to
the user.

The following example illustrates how predicate and inverse paths are used in view mode to access
and display values, either directly from the focus node or through incoming relationships from other
nodes.
> **Example:**
>
> ex:PersonShape
> a sh:NodeShape ;
> sh:property [
> sh:path foaf:name ;
> sh:name "Name" ;
> sh:datatype xsd:string ;
> ] ;
> sh:property [
> sh:path [ sh:inversePath ex:member ] ;
> sh:name "Department" ;
> ] .
>
> ex:alice a ex:Person ;
> foaf:name "Alice" .
>
> ex:researchDept a ex:Department ;
> ex:member ex:alice ;
> rdfs:label "Research Department" .
>
> A SHACL UI could display the person’s `foaf:name` as text and list departments that
> reference the person via `ex:member`.

##### Complex Paths

SHACL UI implementations SHOULD support other complex property paths besides [inverse paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-inverse) in view mode as well.
These complex paths include [sequence paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-sequence), [alternative paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-alternative), [zero-or-more paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-zero-or-more), [one-or-more paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-one-or-more),
and [zero-or-one paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-zero-or-one) as defined in SHACL
Core.

Support for these complex paths is recommended, but optional, and can be left out in cases where the implementation aims
to provide symmetry between view and edit modes, and such paths are not supported in edit mode.

The following examples illustrate a sequence path and an alternative path, both of which may be used
for richer data traversal in view mode.
> **Example:**
>
> ex:PersonShape
> a sh:NodeShape ;
> sh:property [
> sh:path ( ex:address ex:cityName ) ;
> sh:name "City" ;
> sh:datatype xsd:string ;
> ] .
>
> ex:BookShape
> a sh:NodeShape ;
> sh:property [
> sh:path [
> sh:alternativePath ( dct:title rdfs:label )
> ] ;
> sh:name "Title" ;
> sh:datatype xsd:string ;
> ] .
>
> ex:alice a ex:Person ;
> ex:address ex:aliceAddress .
>
> ex:aliceAddress ex:cityName "Ghent" .
>
> ex:book1 a ex:Book ;
> dct:title "Linked Data Design" .
>
> A SHACL UI could display Alice’s city as "Ghent" by traversing the `ex:address` node,
> and display the title of `ex:book1` as “Linked Data Design”.

#### Edit Mode

In edit mode, property paths determine how changes to data and the creation of new data are applied
through the user interface.

##### Predicate and Inverse Paths

SHACL UI implementations MUST support [predicate paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-predicate) and [inverse paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-inverse) in edit mode.
This allows users to modify data linked by simple properties or inverse properties.

The following example illustrates how predicate and inverse paths can be used in edit mode to modify
a person’s name and manage their membership in departments.
> **Example:**
>
> ex:PersonShape
> a sh:NodeShape ;
> sh:property [
> sh:path foaf:name ;
> sh:name "Name" ;
> sh:datatype xsd:string ;
> ] ;
> sh:property [
> sh:path [ sh:inversePath ex:member ] ;
> sh:name "Department" ;
> sh:class ex:Department ;
> ] .
>
> ex:bob a ex:Person ;
> foaf:name "Bob" .
>
> ex:engDept a ex:Department ;
> ex:member ex:bob ;
> rdfs:label "Engineering Department" .
>
> A SHACL UI might render a text input for `foaf:name` and a selector for the
> departments.
> Editing inverse paths requires the UI to ensure consistent updates on the related nodes.

##### Alternative Paths

SHACL UI implementations SHOULD support [alternative paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-alternative) in edit mode.
This enables editing where a shape can constrain multiple potential properties, and the UI can allow
users to choose which alternative to use when entering or modifying data.

When editing existing or newly created statements, the UI SHOULD provide a mechanism to update the
predicate to one of the enumerated paths in the `sh:alternativePath` list, but only if
those paths are either [predicate paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-predicate) or [inverse paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-inverse). This restriction is necessary
because the object of `sh:alternativePath` is a SHACL list that may contain any valid
property path expression, including complex path types that are not generally feasible to edit
directly through a user interface.

Although redundant, SHACL permits nesting of `sh:alternativePath` expressions.
Such nesting simply flattens to a single list of predicate or inverse paths and does not alter the
effective set of alternatives available for editing.

The following example illustrates how an alternative path can be used in edit mode to allow a book's
title to be provided through either `dct:title` or `rdfs:label`.
> **Example:**
>
> ex:BookShape
> a sh:NodeShape ;
> sh:property [
> sh:path [
> sh:alternativePath ( dct:title rdfs:label )
> ] ;
> sh:name "Title" ;
> sh:datatype xsd:string ;
> ] .
>
> ex:book2 a ex:Book ;
> rdfs:label "Semantic Web Foundations" .
>
> A SHACL UI could show the existing title “Semantic Web Foundations” and allow the user to choose
> whether
> to edit it via `dct:title` or `rdfs:label`.

##### Other Complex Paths

SHACL UI implementations MAY support the other complex paths (i.e., [sequence paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-sequence), [zero-or-more paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-zero-or-more), [one-or-more paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-one-or-more), and [zero-or-one paths](https://w3c.github.io/data-shapes/shacl12-core/#property-path-zero-or-one))
in edit mode.

Implementers are encouraged to support these when their use cases require advanced
data navigation or editing patterns, but such support is not mandatory as the complexity of editing
through these paths may not be feasible in all user interface contexts.

Supporting complex property paths in edit mode introduces challenges related to ambiguity and the
generation of intermediate data structures. Even when a path is used for view-only purposes,
implementations must ensure that restrictions are in place to prevent ambiguous traversal results.
SHACL property paths allow navigation across multiple steps in a graph, which can lead to
situations where a single value is reachable through multiple distinct paths.
> **Example:**
>
> The following shape and data graph illustrate how a node can be reachable via a complex path
> expression, making editing operations ambiguous.
>
> ex:CompoundThingShape
> a sh:NodeShape ;
> sh:property [
> sh:path [
> sh:zeroOrMorePath ex:hasPart
> ] ;
> sh:name "All Descendant Parts" ;
> sh:description "Traverses all parts and sub-parts using a zero-or-more path of hasPart relationships." ;
> ] .
>
> ex:compounded-thing
> ex:hasPart ex:part-a ;
> ex:hasPart ex:part-b .
>
> ex:part-a
> ex:hasPart ex:screw .
>
> ex:part-b
> ex:hasPart ex:screw .
>
> In this example, the node `ex:screw` can be reached from `ex:compounded-thing` through two distinct paths:
>
> - `ex:compounded-thing → ex:hasPart → ex:part-a → ex:hasPart → ex:screw`
> - `ex:compounded-thing → ex:hasPart → ex:part-b → ex:hasPart → ex:screw`
> This illustrates why editing along complex property paths is non-trivial: it can be unclear
> which intermediate nodes or triples correspond to a user’s intended modification.

### Label and Language Resolution

UI literals — such as labels, descriptions, and other human-readable strings required for
rendering a user interface — are selected based on language tags. This section defines how
an application determines which language to use when multiple language-tagged literals are
available for a given property.

#### Language Resolution

When selecting a UI literal, the preferred language is determined according to the following order of
priority. Each option itself provides an ordered list of languages where earlier entries are preferred over
later ones:

1. A list of languages selected in the application. How this language preference list is configured or
   expressed is up to the implementation. Possible approaches include but are not limited to:
   - A UI feature that allows the user to select a preferred display language or languages priorities.
   - A global configuration using the property `shui:languagePreference`.
2. The list of preferred languages declared in the user's browser, as expressed through the `Accept-Language` HTTP header or the `navigator.languages` Web API. These SHOULD be
   used as the default values when no application-level language preference has been configured.

Language tags are matched according to the basic filtering scheme defined in [RFC4647] section 3.3.1.
In particular, a language tag such as `en-US` SHOULD be considered a match for a preferred
language of `en`.

If no literal matching the preferred language is available, implementations MAY fall back to a literal in
another available language (or without a declared language) or apply the label resolution fallback strategy as defined for the relevant context.

#### Label Resolution

Label resolution determines the most appropriate human-readable string to display for an
RDF resource in a user interface. This section defines the algorithm for determining that
label, considering annotations in the shapes graph, values in the data graph,
and fallback strategies when no suitable label is found.

Label resolution is applied in two contexts:

- **Property labels**: the label used for the field or column heading of a property UI component, derived from the property shape or from the predicate
  identified by `sh:path`.
- **Value node labels**: the label used to represent a value node (e.g.,
  an IRI or blank node) when it appears in a UI form or list.

##### Label Property Resolution

Label property resolution (i.e., determining the label properties for retrieving label values) is done according to the preferred property IRIs listed in the global configuration property `shui:labelPreference`.
Preferred labels default to `sh:name` for Property Labels and `rdfs:label` for Value Node Labels.

##### Property Labels

To determine the label for a property UI component whose property shape has
a `sh:path` pointing to a property path *P*, implementations MUST
apply the following steps in order, stopping at the first step that yields a result:

1. If the property shape has one or more values for the configured property path for
   properties determined by label property resolution, select the best
   matching value using language resolution.
   If a match is found, use that literal as the label.
2. If *P* is a predicate IRI and the data graph contains one or more triples with properties determined by label property resolution and with subject *P*, select
   the best matching value using language resolution.
   If a match is found, use that literal as the label.
3. If *P* is a predicate IRI and the shapes graph contains one or more triples with properties determined by label property resolution and with subject *P*, select
   the best matching value using language resolution.
   If a match is found, use that literal as the label.
4. If *P* is a predicate IRI, use the local name resolution of *P* as the label.
5. Otherwise, an implementation-specific translation algorithm should be applied to convert the complex property path *P* into a human-readable string representation.

##### Value Node Labels

To determine the label for a single value node *V*, implementations MUST
apply the following steps in order, stopping at the first step that yields a result:

1. If *V* is a literal, use its lexical form as the label.
2. If the applicable node shape for *V* contains a property shape whose `sh:path` is annotated with `shui:propertyRole shui:LabelRole`, retrieve the values of that path from
   the data graph for subject *V*. Select the best matching value using language resolution.
   If a match is found, use that literal as the label.
3. If the data graph contains one or more values for the configured property path for
   the value node determined by label property resolution for *V*,
   select the best matching value using language resolution.
   If a match is found, use that literal as the label.
4. If the shapes graph contains one or more values for the configured property path for
   the value node determined by label property resolution for *V*,
   select the best matching value using language resolution.
   If a match is found, use that literal as the label.
5. If *V* is an IRI, use the local name resolution of *V* as the
   label.
6. If *V* is a blank node, use an implementation-specific placeholder string
   (e.g., an empty string or an identifier derived from the blank node identifier) as
   the label.

##### Local Name Resolution

To determine the label for an IRI, the local name *L* of the IRI SHOULD be
used; this process is called *local name resolution*. Implementations SHOULD transform
the local name into a human-friendly form, for example, by splitting camel case identifiers into words.
> **Example:**
>
> ex:PersonShape
> a sh:NodeShape ;
> sh:targetClass ex:Person ;
> sh:property [
> sh:path foaf:firstName ;
> sh:name "First Name"@en ;
> sh:name "Vorname"@de ;
> ] ;
> sh:property [
> sh:path ex:employer ;
> sh:name "Employer"@en ;
> sh:class ex:Organization ;
> ] .
>
> ex:alice a ex:Person ;
> foaf:firstName "Alice" ;
> ex:employer ex:acme .
>
> ex:acme a ex:Organization ;
> rdfs:label "ACME Corp"@en ;
> rdfs:label "ACME GmbH"@de .
>
> When rendering with a German language preference, the `foaf:firstName` field
> label is resolved to `"Vorname"@de` from `sh:name`. The label
> for the value node `ex:acme` is resolved to `"ACME GmbH"@de` from `rdfs:label` in the data graph.
> **Example:**
>
> ex:BookShape
> a sh:NodeShape ;
> sh:targetClass ex:Book ;
> sh:property [
> sh:path dct:creator ;
> ] .
>
> ex:book1 a ex:Book ;
> dct:creator ex:author1 .
>
> Since the property shape for `dct:creator` has no `sh:name` and
> no `rdfs:label` is available for the `dct:creator` predicate,
> the label falls back to the local name `"creator"`, which a renderer might
> display as `"Creator"` after capitalizing the first letter. The value node `ex:author1` has no `rdfs:label` in the data graph, so its label
> falls back to the local name `"author1"`. A renderer might further transform
> this by splitting on the digit boundary and capitalizing, yielding `"Author 1"`.

### Patterns

Add common UI form patterns here, e.g., error handling and validation, conditional rendering, etc. For each section, clearly state whether it's normative or informative and describe its use case.

TODO: consider removing the explicit "patterns" section and move these topics under §3 Getting Started with SHACL UI

#### Root Shapes and Entry-Point Forms

TODO: Add a pattern describing how applications choose the initial node shape and focus node for rendering.
This pattern should explain that applications may nominate one or more root node shapes for entry-point forms.

#### Conditional Shape Selection

Add a pattern for conditional or dynamic sub-forms. Consider how the following constraints would work here. sh:class, sh:node, sh:or, sh:qualifiedValueShape.

#### Enumerations, Select Lists, and Autocomplete

Add a pattern for select widgets. This should cover common sources for option lists: sh:in, class-based instance selection,
SKOS concepts, node expressions, and implementation-provided query services. It should distinguish static enumerations from dynamic lookups.

Some of the UI meetings have discussed using node expressions, dynamic SHACL, and SPARQL with the SERVICE clause.
> **Issue:**

##### Fetching values from named graphs
> **Issue:**

#### Grouping, Ordering, and Layout Hints

*This section is normative, except for the part explicitly marked as non-normative below.*

SHACL Renderers MUST determine the presentation order of property shapes and
property groups using the value of `sh:order`. At each level of rendering,
property groups and ungrouped property shapes MUST be treated as members of a single
ordered sequence.

For a property shape that specifies `sh:group`, the position of the
property shape in the top-level sequence MUST be determined by the `sh:order` of
the referenced property group. The property shape's own `sh:order` MUST be used
only to determine its position within that property group. Within a property group, property shapes MUST be ordered according to their own `sh:order` values.
The same ordering rules MUST be applied recursively to nested property groups, if supported
by the renderer.

The *effective order* of a property shape or
property group is the value of its `sh:order`. Where `sh:order` is not
specified, the effective order is the value of `shui:defaultOrder` in the global configuration, if present. Otherwise, the property shape or property group has
no effective order.

Renderers MUST order the members of an ordered sequence by the ascending numeric value of
their effective order. Members that have no effective order MUST be placed
after all members that have one.

The global configuration property `shui:defaultOrder` declares the effective order assumed for property shapes and property groups that do not
specify `sh:order`. Its value is a literal with datatype `xsd:decimal` or `xsd:integer`, which are the datatypes that `sh:order` permits.

Renderers MUST apply a deterministic tie-breaking algorithm whenever two or more members of
an ordered sequence have the same effective order, or whenever two or more members
have no effective order. Renderers SHOULD apply the following tie-breaking algorithm:

1. Members are ordered by their resolved label, as determined by label resolution.
2. Members that have the same resolved label are ordered lexicographically by the identifier
   of the resource on which the `sh:order` is defined, that is, its IRI or blank
   node identifier.

Renderers MAY use an alternative tie-breaking algorithm, provided that the algorithm yields
deterministic results within that implementation.

*The remainder of this section is non-normative.*

Deterministic interoperability is guaranteed only when all property groups and property
shapes participating in an ordered sequence explicitly specify `sh:order`, or
when the shapes graph declares `shui:defaultOrder`.

Presenting property shapes and property groups without `sh:order` last reflects
the behaviour of existing renderers, which append properties that carry no ordering hint to
the end of the form. Shape authors who prefer a numeric default can declare one explicitly
with `shui:defaultOrder`. Setting `shui:defaultOrder 0`, for example,
allows authors to assign negative `sh:order` values to elements that should
always be rendered before otherwise unordered elements, while positive values can be used to
position elements after them. Because the global configuration is part of the shapes graph, this choice travels with the shapes, so interoperability across
implementations is preserved.

The following example illustrates the interpretation of a missing `sh:order` value.
> **Example:**
>
> ex:PersonShape
> a sh:NodeShape ;
> sh:property ex:description ;
> sh:property ex:identifier ;
> sh:property ex:name .
>
> ex:description
> sh:path dct:description ;
> sh:order 5 .
>
> ex:identifier
> sh:path ex:id ;
> sh:order -10 .
>
> ex:name
> sh:path rdfs:label .
>
> No `shui:defaultOrder` is declared, so `ex:name` has no effective
> order and is rendered last. The properties are rendered in the order `ex:identifier` (effective order -10), `ex:description` (effective
> order 5), and `ex:name`.
> **Example:**
>
> ex:config
> a shui:Configuration ;
> shui:defaultOrder 0 .
>
> Adding this global configuration to the previous shapes graph gives `ex:name` an effective order of 0, so the properties are rendered in the order `ex:identifier`, `ex:name`, `ex:description`. This
> demonstrates that assigning a negative `sh:order` value allows a property to be
> rendered before properties that rely on the declared default.
> **Issue:**
> **Issue:**

#### Role-Based Shapes

The section should explain that a single shapes graph may contain shapes used for different purposes, and implementations may need to
distinguish validation shapes and UI rendering shapes.

#### Default Namespace and Local Name Generation

We may need a more broader set of patterns documented for creating, updating, and deleting data via SHACL UI.
> **Issue:**

#### Form Messages and Error Handling

The pattern should describe how renderers may handle and display form errors, including validation errors and submission errors.
> **Issue:**
> **Issue:**

##### Displaying Validation Results

This sub-section should address the *"Mapping validation results to the form"* mentioned in [ISSUE 823](https://github.com/w3c/data-shapes/issues/823).

The pattern should describe how renderers may associate `sh:ValidationResult` entries with property UI components or node UI components,
using `sh:focusNode`, `sh:resultPath`, `sh:value`, `sh:sourceShape`, `sh:resultSeverity`, and `sh:resultMessage`. It should avoid defining when validation
runs or how an applications prevents malformed submissions.

### Search Query

This section defines `shui:searchQuery`, an optional property of a property shape that lets shape authors provide a dedicated SPARQL `SELECT` query for retrieving candidate
value nodes from live, user-provided search input, for example within an AutoCompleteEditor (§12.1.1).

#### shui:searchQuery

A well-formed value of `shui:searchQuery` is a literal of datatype `xsd:string`, appearing directly on a property shape, and containing a SPARQL `SELECT` query conforming to the constraints below. A property shape has at most
one value for `shui:searchQuery`.

When an end user enters or changes search input for a property rendered with a widget that consumes
candidate value nodes, a SHACL Renderer that supports this extension MAY evaluate the query given by `shui:searchQuery` to retrieve the candidate value nodes offered to the user.

The query MUST expect the following variables to be pre-bound by the renderer before evaluation:

| Variable      | Description                                                                                                                                                                                              |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$searchTerm` | An `xsd:string` literal containing the current search input entered by the end user.                                                                                                                     |
| `$uiLanguage` | An `xsd:string` literal containing the BCP47 language tag identifying the user's current UI language preference, as determined by §9.1 Language Resolution. |

Implementations MAY pre-bind additional implementation-specific variables.

Using the [prefix handling rules](https://w3c.github.io/data-shapes/shacl12-sparql/#sparql-prefixes), the SPARQL query derived
from the value of `shui:searchQuery` MUST project at least one variable in its `SELECT` clause. A SHACL Renderer only depends on the first variable of the `SELECT` clause's projection,
which represents the matching IRIs or literals for each candidate value node. The query MAY project
additional variables beyond the first, and a SHACL Renderer MAY add bindings for such additional variables
to the candidate value nodes it offers to the end user, for example to carry a label or other data
associated with each candidate value node. The query MAY include a `LIMIT` or `OFFSET` solution modifier; if present, the renderer MAY use it to limit the number of candidate value nodes
returned to the user.

A property shape with a `shui:searchQuery` signals that a live search widget is
appropriate for that property, even without an explicit `shui:editor` statement. Accordingly, the
presence of `shui:searchQuery` raises the AutoCompleteEditor (§12.1.1)'s
score, as described in its Score rules.

This specification does not define how §13 Property Roles, such as `shui:LabelRole`, are resolved or auto-injected into the search query. Renderers MAY combine
value filtering and label retrieval in a single query, using the additional bindings beyond the first
described above, or retrieve them via different mechanisms.
> **Example:**
>
> ex:TaskShape
> a sh:NodeShape ;
> sh:targetClass ex:Task ;
> sh:property [
> sh:name "Assignee" ;
> sh:path ex:assignee ;
> sh:class ex:Person ; shui:searchQuery """
> PREFIX ex: <http://example.com/>
> PREFIX text: <http://jena.apache.org/text#>
> SELECT ?value WHERE {
> ?value text:query ($searchTerm $uiLanguage) .
> ?value a ex:Person .
> }
> """ ;
> ] .
>
> As the user types into the AutoCompleteEditor (§12.1.1) rendered for `ex:TaskShape`'s `Assignee` property, the renderer binds the typed text to `$searchTerm` and the current UI language to `$uiLanguage`, then evaluates `shui:searchQuery` to query a local full-text index of `ex:Person` instances.

A property shape's permissible value nodes can also be computed dynamically using a [select expression](https://w3c.github.io/data-shapes/shacl12-sparql/#SelectExpression) (`sh:select`) inside `sh:in`, including a SPARQL `SERVICE` clause against an external endpoint, as
described in [Dynamic SHACL](https://w3c.github.io/data-shapes/shacl12-node-expr/#dfn-dynamic-shacl). Such a query resolves the
full candidate set and cannot be parameterized with a user's live search input, nor can it take advantage
of vendor-specific full-text search (FTS) extensions. When a property shape combines `sh:in` with `shui:searchQuery`, a renderer that supports `shui:searchQuery` evaluates it in place of the `sh:in`-derived query while the user is searching. A renderer that
does not support `shui:searchQuery` but does support Dynamic SHACL MAY fall back to the
baseline query given by `sh:in`'s `sh:select` instead.
> **Example:**
>
> ex:BookShape
> a sh:NodeShape ;
> sh:targetClass ex:Book ;
> sh:property [
> sh:name "Author" ;
> sh:path dct:creator ;
> sh:in [
> sh:select """
> PREFIX ex: <http://example.com/>
> SELECT ?value WHERE {
> SERVICE <http://example.com/sparql> {
> ?value a ex:Person .
> }
> }
> """ ;
> ] ; shui:searchQuery """
> PREFIX ex: <http://example.com/>
> PREFIX text: <http://jena.apache.org/text#>
> SELECT ?value WHERE {
> SERVICE <http://example.com/sparql> {
> ?value text:query ($searchTerm $uiLanguage) .
> ?value a ex:Person .
> }
> }
> """ ;
> ] .
>
> As the user types into the AutoCompleteEditor (§12.1.1) rendered for `ex:BookShape`'s `Author` property, the renderer binds the typed text to `$searchTerm` and the current UI language to `$uiLanguage`, then evaluates `shui:searchQuery` to query the Apache Jena Text index via the `SERVICE` clause.
> If the renderer does not support `shui:searchQuery` but does support Dynamic SHACL,
> the baseline `sh:select` query is used instead, returning all instances of `ex:Person`.

#### Validation of Search Query Results

Shape authors SHOULD write `shui:searchQuery` so that its result set, for any given `$searchTerm`, is a subset of the value nodes permitted by the other constraints on the property shape (such as `sh:class`, `sh:node`, or `sh:in`), or
exactly that same set. A `shui:searchQuery` that returns value nodes outside that set risks
offering end users candidate values that do not conform to the property shape.

Because a value node returned by `shui:searchQuery` is offered to the end user as though it
were drawn from `sh:in`, implementations MAY apply SHACL validation to the outcomes of `shui:searchQuery`, where the outcomes are value nodes of the property shape.

Such validation runs the property shape in isolation once for each value node returned by the
query, using that value node as the sole value for the property shape's property path, and checks
whether the result conforms to the surrounding property shape.

For a property shape such as `ex:BookShape`'s `Author` property above, where `sh:in` itself contains a `sh:select` [select expression](https://w3c.github.io/data-shapes/shacl12-sparql/#SelectExpression) with a SPARQL `SERVICE` clause, checking whether a value node conforms to the surrounding property shape requires
re-evaluating that `sh:in` constraint. This requires a SHACL validation engine that supports
federated SHACL validation — at minimum, the piece of [Dynamic SHACL](https://w3c.github.io/data-shapes/shacl12-node-expr/#dfn-dynamic-shacl) that allows `sh:in` to contain
a `sh:select` [select expression](https://w3c.github.io/data-shapes/shacl12-sparql/#SelectExpression).

For such federated validation, the isolated property shape used to check a value node SHOULD
contain only the `sh:in` constraint, and no other constraints from the surrounding property shape. A value node retrieved via `SERVICE` generally has no corresponding
triples in the local data graph, so a validation engine evaluating any other constraint (such as `sh:class` or `sh:node`) as part of the same isolated run would evaluate it against
the local data graph and likely report a spurious violation.

### Built-in Widgets

This section enumerates the *built-in* widgets defined in the SHACL UI namespace. Additional
widgets may be defined by the community; see §14 Registries.

#### Editors

The following subsections enumerate the currently built-in instances of `shui:Editor` from the
SHACL UI namespace.

##### shui:AutoCompleteEditor

**Score:**

- `40` if the property indicates its preference for `shui:AutoCompleteEditor` using a `shui:editor` statement and has a `sh:class` constraint, and the value is an IRI.
- `20` if the property has `shui:searchQuery`.
- `10` if the property has a `sh:nodeKind sh:IRI` and a `sh:class` constraint.

**Rendering:** An auto-complete field to enter the label of instances of the class specified for the property.
For example, if the `sh:class` of the property is `ex:Country` and the user starts
typing "Nig", then "Niger" and "Nigeria" would show up as possible choices.

![Example of a rendered AutoCompleteEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/AutoCompleteEditor.png)

```
ex:Person-bornIn
	a sh:PropertyShape ;
	sh:path ex:bornIn ;
	sh:class ex:Country ;
	...
```

Implementations may want to also support the combination of `sh:class` with `sh:node`
constraints to further narrow the set of valid values.
In this case, the component would filter out any instances of the class that do not conform to the specified node shape.
In the following example, the auto-complete would only show countries that have `true` as their value
for `ex:sovereign`.

```
ex:Person-bornIn
	a sh:PropertyShape ;
	sh:path ex:bornIn ;
	sh:class ex:Country ;
	sh:node [
		sh:property [
			sh:path ex:sovereign ;
			sh:hasValue true ;
		]
	] ; ...
```

##### shui:BlankNodeEditor

**Score:**

- `40` if the property indicates its preference for `shui:BlankNodeEditor` using a `shui:editor` statement, and the value is a blank node.
- `1` if the value is a blank node.

**Rendering:** A read-only editor that displays the blank node, similar to §12.2.1 shui:BlankNodeViewer,
yet allows the surrounding user interface to at least provide a delete button.

##### shui:BooleanEditor

**Score:**

- `40` if the property indicates its preference for `shui:BooleanEditor` using a `shui:editor`
  statement, and the value is an `xsd:boolean` literal.
- `20` if the value is an `xsd:boolean` literal.
- `10` if the property has a `sh:datatype xsd:boolean` constraint.

**Rendering:** A widget for editing boolean values, typically rendered as a checkbox, toggle switch, or select dropdown
offering true and false, and, where the property is optional, optionally an additional control state
representing the absence of a value.

The exact rendering of the `BooleanEditor` may vary between implementations depending on the complexity and
requirements of the use case. In particular, implementations should carefully distinguish between optional
and required boolean properties: for optional properties, the absence of a value is semantically different
from the value `false`, and an implementation may therefore render a select dropdown with three choices
(e.g., `true`, `false`, and `none`) where `none` represents no value; for required properties, where a value
must always be present, a checkbox or toggle switch may be appropriate. Implementations may choose the most
suitable rendering approach, provided this semantic distinction is preserved.

![Example of a BooleanEditor rendered as select dropdown](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/BooleanSelectEditor.png)

```
ex:Person-married
	a sh:PropertyShape ;
	sh:path ex:married ;
	sh:datatype xsd:boolean ;
	...
```

##### shui:DatePickerEditor

**Score:**

- `40` if the property indicates its preference for `shui:DatePickerEditor` using a `shui:editor` statement, and the value is an `xsd:date` literal.
- `20` if the value is an `xsd:date` literal.
- `10` if the property has a `sh:datatype xsd:date` constraint.

**Rendering:** A calendar-like date picker.

![Example of a rendered DatePickerEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/DatePickerEditor.png)

```
ex:Person-dateOfBirth
	a sh:PropertyShape ;
	sh:path ex:dateOfBirth ;
	sh:datatype xsd:date ;
	...
```

##### shui:DateTimePickerEditor

**Score:**

- `40` if the property indicates its preference for `shui:DateTimePickerEditor` using a `shui:editor` statement, and the value is an `xsd:dateTime` literal.
- `20` for `xsd:dateTime` literals.
- `10` if the property has a `sh:datatype xsd:dateTime` constraint.

**Rendering:** A calendar-like date picker including a time selector.

![Example of a rendered DateTimePickerEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/DateTimePickerEditor.png)

```
ex:Customer-lastVisitTime
	a sh:PropertyShape ;
	sh:path ex:lastVisitTime ;
	sh:datatype xsd:dateTime ;
	...
```

##### shui:DetailsEditor

**Score:**

- `40` if the property indicates its preference for `shui:DetailsEditor` using a `shui:editor` statement, and the value is an IRI or a blank node.
- `0` if the value is an IRI or a blank node.

**Rendering:** Typically rendered as a nested form that allows editing the properties of the value node inline within the surrounding form.
The fields of the nested form are determined by the shape that applies to the value node.
This shape may be specified explicitly (e.g., via `sh:node` or other mechanisms that associate a shape with the value),
or implicitly via constraints such as `sh:class`.
Alternatively, nested fields may be defined directly on the surrounding property shape using `sh:property`.

When rendered as a nested form, the implementation recursively evaluates the applicable shape of the value node
and renders its declared property shapes as sub-fields.
Implementations may alternatively render the details in a separate dialog or dedicated view,
provided that the editing semantics remain equivalent.

This editor is particularly useful for blank nodes or tightly coupled resources
that are typically created and edited only in the context of their parent resource.
However, it may also be used for IRIs referencing other resources.

![Example of a rendered DetailsEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/DetailsEditor.png)

```
ex:Product
	a owl:Class ;
	a sh:NodeShape ;
	rdfs:label "Product" ;
	rdfs:subClassOf owl:Thing ;
	sh:property ex:Product-weight .

ex:Product-weight
	a sh:PropertyShape ;
	sh:path ex:weight ;
	shui:editor shui:DetailsEditor ;
	shui:viewer shui:DetailsViewer ;
	sh:description "A blank node with a numeric field and a unit which is one of the QUDT mass units." ;
	sh:maxCount 1 ;
	sh:name "weight" ;
	sh:node ex:ValueWithWeight ;
	sh:nodeKind sh:BlankNode .

ex:ValueWithWeight
	a sh:NodeShape ;
	rdfs:label "Value with weight" ;
	sh:property ex:ValueWithWeight-numericValue ;
	sh:property ex:ValueWithWeight-unit .

ex:ValueWithWeight-numericValue
	a sh:PropertyShape ;
	sh:path ex:numericValue ;
	sh:datatype xsd:decimal ;
	sh:maxCount 1 ;
	sh:minCount 1 ;
	sh:name "numeric value" .

ex:ValueWithWeight-unit
	a sh:PropertyShape ;
	sh:path ex:unit ;
	sh:class <http://qudt.org/schema/qudt/Unit> ;
	sh:maxCount 1 ;
	sh:minCount 1 ;
	sh:name "unit" ;
	sh:node [
		rdfs:label "Permissible values must have quantity kind Mass." ;
		sh:property [
			sh:path <http://qudt.org/schema/qudt/hasQuantityKind> ;
			sh:hasValue <http://qudt.org/vocab/quantitykind/Mass> ;
		] ;
	] .
```

This widget requires that the surrounding property (`ex:weight`, above) declares `sh:nodeKind sh:BlankNode`
and also has a `sh:node` constraint that points at a node shape that declares the properties that shall be editable.

##### shui:EnumSelectEditor

**Score:**

- `40` if the property indicates its preference for `shui:EnumSelectEditor` using a `shui:editor` statement and has a `sh:in` constraint.
- `30` if the property has a `sh:in` constraint.

**Rendering:** A drop-down editor for enum fields (based on the `sh:in` list, in that order).

![Example of a rendered EnumSelectEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/EnumSelectEditor.png)

```
ex:AustralianAddressShape-addressRegion
	a sh:PropertyShape ;
	sh:path schema:addressRegion ;
	sh:in ( "ACT" "NSW" "NT" "QLD" "SA" "TAS" "VIC" "WA" ) ;
	...
```

##### shui:InstancesSelectEditor

**Score:**

- `40` if the property indicates its preference for `shui:InstancesSelectEditor` using a `shui:editor` statement and has a `sh:class` constraint, and the value is an IRI.
- `0` if the property has a `sh:class` constraint.

**Rendering:** A drop-down editor for all instances of the target class (based on `sh:class` of the property).
Typically only used for classes that have few instances.

```
ex:Person-homeCountry
	a sh:PropertyShape ;
	sh:path ex:homeCountry ;
	sh:class ex:Country ;
	shui:editor shui:InstancesSelectEditor ;
	...
```

##### shui:IRIEditor

**Score:**

- `40` if the property indicates its preference for `shui:IRIEditor` using a `shui:editor` statement, and the value is an IRI.
- `20` if the value is an IRI, and the property has a `sh:nodeKind sh:IRI` and no `sh:class` constraint.
- `10` if the property has a `sh:nodeKind sh:IRI` constraint and no `sh:class` constraint.
- `0` if the value is an IRI.

**Rendering:** An input field to enter the IRI of a resource, e.g., as value of `rdfs:seeAlso` or to enter the URL of an image on the web.

![Example of a rendered IRIEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/IRIEditor.png)

```
ex:Thing-seeAlso
	a sh:PropertyShape ;
	sh:path rdfs:seeAlso ;
	sh:nodeKind sh:IRI ;
	shui:editor shui:IRIEditor ;
	...
```

##### shui:NumberFieldEditor

**Score:**

- `40` if the property indicates its preference for `shui:NumberFieldEditor` using a `shui:editor`
  statement, and the value is an `xsd:decimal`, `xsd:integer`, `xsd:double`, or `xsd:float` literal.
- `20` if the value is an `xsd:decimal`, `xsd:integer`, `xsd:double`, or `xsd:float` literal.
- `10` if the property has a `sh:datatype xsd:decimal`, `xsd:integer`, `xsd:double`, or `xsd:float`
  constraint.

**Rendering:** An input field to enter numeric values. The field should only allow entering valid numeric values according
to the specified datatype. If no `sh:datatype` constraint is specified, `xsd:decimal` is assumed to be the
default numeric datatype.

```
ex:Product-price
    a sh:PropertyShape ;
    sh:path ex:price ;
    sh:datatype xsd:decimal ;
    shui:editor shui:NumberFieldEditor ;
    ...
```

##### shui:RichTextEditor

**Score:**

- `40` if the property indicates its preference for `shui:RichTextEditor` using a `shui:editor` statement, and the value is an `rdf:HTML` literal.
- `20` if the value is an `rdf:HTML` literal.
- `10` if the property has a `sh:datatype rdf:HTML` constraint.

**Rendering:** A rich text editor to enter the lexical value of a literal and a drop-down to select language.
The selected language is stored in the HTML `lang` attribute of the root node in the HTML DOM tree.

![Example of a rendered RichTextEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/RichTextEditor.png)

```
ex:Concept-definition
	a sh:PropertyShape ;
	sh:path skos:definition ;
	sh:datatype rdf:HTML ;
	...
```

##### shui:SubClassEditor

**Score:**

- `40` if the property indicates its preference for `shui:SubClassEditor` using a `shui:editor` statement and has a [`sh:rootClass`](https://w3c.github.io/data-shapes/shacl12-core/#RootClassConstraintComponent) constraint, and the value is an IRI.

**Rendering:** This can be an auto-complete widget to select a class, a class hierarchy widget, or a combination thereof.
The permissible values are a given class or its subclasses, defaulting to `rdfs:Resource`.
This is typically used with `sh:rootClass` to allow the user to select a subclass of the given root class.

```
ex:Drug-impactedCell
	a sh:PropertyShape ;
	sh:path ex:impactedCell ;
	sh:rootClass obo:CL_0000000 ;
	shui:editor shui:SubClassEditor ;
	...
```

##### shui:TextAreaEditor

**Accept matcher:** Offered only if the property does not have a `sh:singleLine true` constraint,
expressed with a `shui:WidgetAcceptMatcher`.

**Score:**

- `40` if the property indicates its preference for `shui:TextAreaEditor` using a `shui:editor` statement.
- `30` if the value is an `xsd:string` literal and the property has a `sh:singleLine false` constraint.
- `20` if the value is an `xsd:string` literal.
- `5` if the property has `xsd:string` among the permissible datatypes.
- `0` if the property has a `sh:singleLine false` constraint.
- ~~0 otherwise.~~

**Rendering:** A multi-line text area to enter the value of a literal.

![Example of a rendered TextAreaEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/TextAreaEditor.png)

```
ex:Country-description
	a sh:PropertyShape ;
	sh:path ex:description ;
	sh:datatype xsd:string ;
	sh:singleLine false ;
	...
```

##### shui:TextAreaWithLangEditor

**Accept matcher:** Offered only if the property does not have a `sh:singleLine true` constraint,
expressed with a `shui:WidgetAcceptMatcher`.

**Score:**

- `40` if the property indicates its preference for `shui:TextAreaWithLangEditor` using a `shui:editor` statement.
- `30` if the value is an `rdf:langString` or `rdf:dirLangString` literal and the property has a `sh:singleLine false` constraint.
- `20` if the value is an `rdf:langString` or `rdf:dirLangString` literal.
- `5` if the property has `rdf:langString` or `rdf:dirLangString` among the permissible datatypes.
- `0` if the property has `xsd:string` among the permissible datatypes.

**Rendering:** A multi-line text area to enter the value of a literal and a drop-down to select a language.
For an `rdf:dirLangString` value, it also provides a base-direction selector.

![Example of a rendered TextAreaWithLangEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/TextAreaWithLangEditor.png)

```
ex:Country-description
	a sh:PropertyShape ;
	sh:path ex:description ;
	sh:datatype rdf:langString ;
	sh:singleLine false ;
	...
```

##### shui:TextFieldEditor

**Accept matcher:** Offered only if the property does not have a `sh:singleLine false` constraint,
expressed with a `shui:WidgetAcceptMatcher`.

**Score:**

- `40` if the property indicates its preference for `shui:TextFieldEditor` using a `shui:editor` statement.
- `30` if the value is an `xsd:string` literal.
- `10` if the property has `xsd:string` among the permissible datatypes.
- `0` if the property has a custom datatype (not from `xsd` or `rdf` namespaces but for example `geo:wktLiteral`), or if the property has a `sh:nodeKind sh:Literal` constraint.

**Rendering:** An input field to enter the value of a literal, without the ability to change language or datatype.

![Example of a rendered TextFieldEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/TextFieldEditor.png)

```
ex:Country-code
	a sh:PropertyShape ;
	sh:path ex:code ;
	sh:datatype xsd:string ;
	...
```

##### shui:TextFieldWithLangEditor

**Accept matcher:** Offered only if the property does not have a `sh:singleLine false` constraint,
expressed with a `shui:WidgetAcceptMatcher`.

**Score:**

- `40` if the property indicates its preference for `shui:TextFieldWithLangEditor` using a `shui:editor` statement.
- `30` if the value is an `rdf:langString` or `rdf:dirLangString` literal.
- `10` if the property has `rdf:langString` or `rdf:dirLangString` among the permissible datatypes.
- `1` if the property has `xsd:string` among the permissible datatypes.

**Rendering:** A single-line input field to enter the value of a literal and a drop-down to select language,
which is mandatory unless `xsd:string` is among the permissible datatypes.
For an `rdf:dirLangString` value, it also provides a base-direction selector.

![Example of a rendered TextFieldWithLangEditor](https://w3c.github.io/data-shapes/shacl12-ui/images/editors/TextFieldWithLangEditor.png)

```
ex:Concept-prefLabel
	a sh:PropertyShape ;
	sh:path skos:prefLabel ;
	sh:datatype rdf:langString ;
	...
```

#### Viewers

The following subsections enumerate the currently built-in instances of `shui:Viewer` from the SHACL UI namespace.

##### shui:BlankNodeViewer

**Score:**

- `40` if the property indicates its preference for `shui:BlankNodeViewer` using a `shui:viewer` statement, and the value is a blank node.
- `1` if the value is a blank node.

**Rendering:** A human-readable label of the blank node.
For example, if the blank node is an OWL restriction, then Manchester Syntax could be used.
If the blank node is a SPIN RDF expression, then a SPARQL string could be produced.
This rendering may include hyperlinks to other resources that can be reached from the blank node.

##### shui:DetailsViewer

**Score:**

- `40` if the property indicates its preference for `shui:DetailsViewer` using a `shui:viewer` statement, and the value is an IRI or a blank node.
- `0` if the value is an IRI or a blank node.

**Rendering:** Displays the details of the value node as a nested, form-like structure within the surrounding view.
The properties shown are determined by the shape that applies to the value node.
This may be specified explicitly (e.g., via `sh:node` or other mechanisms that associate a shape with the value),
inferred via constraints such as `sh:class`,
or defined directly as nested `sh:property` declarations on the property shape.

When rendered as a nested display, the implementation recursively evaluates the applicable shape
and presents its property shapes as structured subsections of the parent form.
Implementations may vary in layout and visual styling,
but the logical grouping and recursive traversal of the applicable shape SHOULD be preserved.

##### shui:HTMLViewer

**Score:**

- `40` if the property indicates its preference for `shui:HTMLViewer` using a `shui:viewer` statement, and the value is an `rdf:HTML` or `xsd:string` literal.
- `20` if the value is an `rdf:HTML` literal.

**Rendering:** The literal parsed into HTML DOM elements.
Hyperlinks in the HTML may get redirected to select resources within the same application.
Also displays the language if the HTML has a `lang` attribute on its root DOM element.

##### shui:HyperlinkViewer

**Score:**

- `40` if the property indicates its preference for `shui:HyperlinkViewer` using a `shui:viewer` statement, and the value is an `xsd:anyURI` or `xsd:string` literal.
- `20` if the value is an `xsd:anyURI` literal.
- `0` if the value is an `xsd:string` literal.

**Rendering:** A clickable hyperlink to the specified URI/URL.

##### shui:ImageViewer

**Score:**

- `40` if the property indicates its preference for `shui:ImageViewer` using a `shui:viewer` statement.
- `20` if the value is an IRI or a literal that has a case-insensitive recognized image file extension ending such as `.png`, `.jpg`, `.jpeg`, `.gif`, or `.svg`.

**Rendering:** The image at the given URL, using `<img>` in HTML.

##### shui:IRIViewer

**Score:**

- `40` if the property indicates its preference for `shui:IRIViewer` using a `shui:viewer` statement, and the value is an IRI.
- `1` if the value is an IRI.

**Rendering:** As a hyperlink to that IRI.
Also includes other ways of interacting with the IRI, such as opening a nested summary display.

##### shui:LabelViewer

**Score:**

- `40` if the property indicates its preference for `shui:LabelViewer` using a `shui:viewer` statement, and the value is an IRI.
- `10` if the value is an IRI.

**Rendering:** As a hyperlink to that URI based on the display label of the resource.
The display label is typically based on the most suitable `rdfs:label` or
`skos:prefLabel` for the current user, based on their language preferences.
Also includes other ways of interacting with the URI, such as opening a nested summary display.

##### shui:LangStringViewer

**Score:**

- `40` if the property indicates its preference for `shui:LangStringViewer` using a `shui:viewer` statement.
- `20` if the value is an `rdf:langString` or `rdf:dirLangString` literal.

**Rendering:** As the text plus a language indicator (flag or language tag).
For an `rdf:dirLangString` value, the base direction is applied to the rendered text and indicated as well.

##### shui:LiteralViewer

**Score:**

- `40` if the property indicates its preference for `shui:LiteralViewer` using a `shui:viewer` statement.
- `1` if the value is a literal.

**Rendering:** The lexical form of the value.

##### shui:ValueTableViewer

This is a Multi Viewer.

**Score:**

- `40` if the property indicates its preference for `shui:ValueTableViewer` using a `shui:viewer` statement.

**Rendering:** All values of the property at the focus node are rendered into a single (HTML) table that can be scrolled
and paged independently of the rest of the form.
Each value becomes one row.
The columns of the table are derived from the node shape specified using `sh:node` for the property,
in the order specified using `sh:order`, as defined in §10.4 Grouping, Ordering, and Layout Hints.

![Example of a rendered ValueTableViewer](https://w3c.github.io/data-shapes/shacl12-ui/images/viewers/ValueTableViewer.png)

In this example, we have used a `sh:values` rule to infer the values of the first column.
In this case, the values are simply pointing back to the focus node of each row, using `sh:this`.
Note that `sh:targetClass` is needed to get this inference correctly.

```
skos:Concept
    sh:property ex:Concept-broader-inverse .

ex:Concept-broader-inverse
    a sh:PropertyShape ;
    sh:path [ sh:inversePath skos:broader ] ;
    sh:group skos:HierarchicalRelationships ;
    sh:name "narrower (table)" ;
    shui:viewer shui:ValueTableViewer ;
    sh:node ex:ConceptTableShape .

ex:ConceptTableShape
    a sh:NodeShape ;
    sh:targetClass skos:Concept ;
    rdfs:comment "A node shape defining the columns for a shui:ValueTableViewer." ;
    rdfs:label "Concept table shape" ;
    sh:property ex:ConceptTableShape-self ;
    sh:property ex:ConceptTableShape-type ;
    sh:property ex:ConceptTableShape-altLabel .

ex:ConceptTableShape-self
    a sh:PropertyShape ;
    sh:path ex:self ;
    sh:description "This column is used to render the (narrower) concept itself." ;
    sh:name "narrower concept" ;
    sh:nodeKind sh:IRI ;
    sh:order "0"^^xsd:decimal ;
    sh:values sh:this .

ex:ConceptTableShape-type
    a sh:PropertyShape ;
    sh:path rdf:type ;
    sh:description "The second column shows the type of each value." ;
    sh:name "type" ;
    sh:nodeKind sh:IRI ;
    sh:order "1"^^xsd:decimal .

ex:ConceptTableShape-altLabel
    a sh:PropertyShape ;
    sh:path skos:altLabel ;
    sh:description "The third column shows the alternative labels." ;
    sh:name "alt labels" ;
    sh:datatype ( xsd:string rdf:langString ) ;
    sh:order "2"^^xsd:decimal .
```

### Property Roles

RDF resources commonly use properties to specify labels, descriptions, and other information needed for rendering, which user-interface engines depend on to render structured content.
However, the vocabularies defining these properties vary across domains and communities. To ensure consistent interpretation, property shapes can
be annotated with explicit roles for elements such as labels, descriptions, and other rendering properties.

This section introduces Property Roles for annotating SHACL property shapes, along with several built-in property roles defined in the SHUI namespace.
Property Roles are defined in the SHUI namespace and define the class `shui:PropertyRole` and the property `shui:propertyRole`.

#### Direct Role Annotation

Property roles can be annotated on property shapes by using the shui:propertyRole predicate and linking directly to a property role instance.
SHACL renderers may use such direct annotations to drive the way specific user-interface elements are displayed.

It is possible but not recommended to assign the same property role to multiple property shapes that apply to the same focus node using the direct role annotation form.
When this is done, the resulting behavior is undefined.

The example below illustrates the common case where a property shape is directly annotated with shui:LabelRole. This informs user-interfaces that the shape's value nodes
represent human-readable labels for resources.
> **Example:**
>
> ex:Label a sh:PropertyShape ;
> sh:path skos:prefLabel ;
> shui:propertyRole shui:LabelRole ;
> .
>
> This example illustrates the common case where a property shape is directly annotated with `shui:LabelRole`.
> This informs user-interfaces that the shape's value nodes represent human-readable labels for resources.

#### Qualified Role Annotation

When multiple predicates serve the same role in the data but require a defined precedence, the qualified role annotation should be used.

If multiple property shapes share the same role, they must be sorted in ascending order of their `sh:order` values, and any
property shape using a qualified role annotation comes before a shape using a direct, unqualified role annotation. For roles that render
a single value, such as `shui:LabelRole`, this order determines precedence, and user interfaces should prefer the first shape
that yields a value. For roles that render all values, such as `shui:ClassificationRole`, all shapes contribute, and this order
only determines the display order of their values. The order of the values within a single shape is left to the implementation.
In both cases, this use of `sh:order` is unrelated to the presentation order defined in §10.4 Grouping, Ordering, and Layout Hints.
> **Example:**
>
> ex:PrefLabel a sh:PropertyShape ;
> sh:path skos:prefLabel ;
> shui:propertyRole [
> shui:propertyRole shui:LabelRole ;
> sh:order 0
> ]
> .
>
> ex:Name a sh:PropertyShape ;
> sh:path schema:name ;
> shui:propertyRole [
> shui:propertyRole shui:LabelRole ;
> sh:order 1
> ]
> .
>
> The following example demonstrates two property shapes with qualified role annotations ordered by `sh:order`.

The qualified role annotation can also be expressed using triple annotations. SHACL Renderers that support RDF 1.2
should support the triple annotation syntax in addition to the RDF 1.1-compatible qualified role annotation syntax.
> **Example:**
>
> ex:PrefLabel a sh:PropertyShape ;
> sh:path skos:prefLabel ;
> shui:propertyRole shui:LabelRole {| sh:order 0 |}
> .
>
> ex:Name a sh:PropertyShape ;
> sh:path schema:name ;
> shui:propertyRole shui:LabelRole {| sh:order 1 |}
> .
>
> This example demonstrates two property shapes with qualified role annotations ordered by `sh:order` using RDF 1.2 triple annotations.

#### Built-in Property Roles

The following sections define the instances of `shui:PropertyRole` in the SHUI namespace. Additional property roles may be defined in other namespaces.

##### shui:LabelRole

The `shui:LabelRole` is used to identify properties whose values serve as human-readable display labels.
Common examples of display label predicates include `rdfs:label`, `skos:prefLabel`, and `schema:name`.

When displaying a resource, SHACL Renderers SHOULD apply Label Resolution to the values of these properties and render a single label.

![Example of a selected resource rendered with its display label instead of its IRI](https://w3c.github.io/data-shapes/shacl12-ui/images/property-roles/label-role.png)

##### shui:DepictionRole

Properties marked with the property role `shui:DepictionRole` provide images that depict the individual resource, such as a photo of a person.
Common examples include `schema:image` and `foaf:depiction`. These depictions SHOULD be distinct for each resource.
Values SHOULD be IRIs or literals with datatype `xsd:anyURI` or `xsd:string` that hold the URL of an image,
with a case-insensitive recognized image file extension ending such as `.png`, `.jpg`, `.jpeg`, `.gif`, or `.svg`.

SHACL Renderers SHOULD render a single depiction for a resource. When multiple values are available, the selection
of the depiction to render is left to the implementation.

Depictions are typically rendered larger than icons and are not constrained to a square box. In contrast to `shui:IconRole`, a depiction is expected to be specific to the individual resource rather than shared across instances.

![Example of a selected resource rendered with its depiction as a thumbnail next to its label](https://w3c.github.io/data-shapes/shacl12-ui/images/property-roles/label-and-depiction-roles.png)

> **Example:**
>
> ex:PersonImage a sh:PropertyShape ;
> sh:path schema:image ;
> sh:nodeKind sh:IRI ;
> sh:description "An image of the item." ;
> sh:name "image" ;
> shui:propertyRole shui:DepictionRole ;
> .
>
> This example illustrates a property shape directly annotated with `shui:DepictionRole`, indicating that its values are URLs of
> images that depict the resource.

##### shui:ClassificationRole

Properties marked with the property role `shui:ClassificationRole` indicate the kind or group that the resource belongs to.
Common examples of classification predicates include `rdf:type`, `skos:inScheme`, and `schema:category`.
User interfaces commonly render classification values near a resource's label, for example as a type badge.

SHACL Renderers SHOULD render all classification values of a resource.

![Example of classification values rendered as badges next to the label of a selected resource](https://w3c.github.io/data-shapes/shacl12-ui/images/property-roles/classification-role.png)

> **Example:**
>
> ex:PersonType a sh:PropertyShape ;
> sh:path rdf:type ;
> sh:nodeKind sh:IRI ;
> sh:description "The type of the resource." ;
> sh:name "type" ;
> shui:propertyRole shui:ClassificationRole ;
> .
>
> This example illustrates a property shape directly annotated with `shui:ClassificationRole`, indicating that its `rdf:type` values
> classify the resource.
> **Example:**
>
> ex:ConceptScheme a sh:PropertyShape ;
> sh:path skos:inScheme ;
> sh:nodeKind sh:IRI ;
> sh:description "The concept scheme that the concept belongs to." ;
> sh:name "scheme" ;
> shui:propertyRole shui:ClassificationRole ;
> .
>
> This example illustrates a property shape annotated with `shui:ClassificationRole`, indicating that its `skos:inScheme` values classify a SKOS concept by the concept scheme it belongs to.

##### shui:DescriptionRole

Properties marked with the property role `shui:DescriptionRole` provide textual descriptions that typically summarize or introduce the resource.
Common examples include `rdfs:comment`, `skos:definition`, and `schema:description`.
Values SHOULD have datatype `xsd:string`, `rdf:langString`, `rdf:dirLangString`, or `rdf:HTML`.

SHACL Renderers SHOULD render a single description for a resource, selected using §9.1 Language Resolution when multiple language-tagged values are available. When multiple candidate values remain, the selection of the description to render
is left to the implementation.

![Example of a list of countries rendered as cards, each showing a short description below its label](https://w3c.github.io/data-shapes/shacl12-ui/images/property-roles/description-role.png)

> **Example:**
>
> ex:Comment a sh:PropertyShape ;
> sh:path rdfs:comment ;
> sh:name "comments" ;
> sh:description "The comments of this resource, possibly in multiple languages." ;
> sh:datatype ( xsd:string rdf:langString rdf:dirLangString rdf:HTML ) ;
> shui:propertyRole shui:DescriptionRole ;
> .
>
> This example illustrates a property shape directly annotated with `shui:DescriptionRole`, indicating that its values are
> textual descriptions of the resource.

##### shui:IconRole

Properties marked with the property role `shui:IconRole` produce small images that may be displayed next to a resource's label,
for example in the corner of a card or to the left of a label in a tree view. Instances of the same class often share the same icon, which
may be computed using `sh:values` or supplied via `sh:defaultValue`.

Common examples include `schema:logo` and `foaf:logo`. Values SHOULD be IRIs or literals with datatype `xsd:anyURI` or `xsd:string` that hold the URL of an image, with a case-insensitive recognized image file extension ending such as `.png`, `.jpg`, `.jpeg`, `.gif`, or `.svg`.

SHACL Renderers SHOULD render a single icon for a resource.

Icons are typically rendered at small sizes and are often reused across many resources. Scalable formats such as SVG are therefore
usually a good choice. In contrast to `shui:DepictionRole`, icon values are not expected to be distinct per resource.

![Example of a list of islands, each rendered with a small icon to the left of its label](https://w3c.github.io/data-shapes/shacl12-ui/images/property-roles/icon-role.png)

> **Example:**
>
> ex:IslandShape
> a sh:NodeShape ;
> sh:targetClass ex:Island ;
> sh:property ex:Island-icon .
>
> ex:Island-icon
> a sh:PropertyShape ;
> sh:path ex:islandIcon ;
> sh:name "island icon" ;
> sh:nodeKind sh:IRI ;
> sh:maxCount 1 ;
> sh:defaultValue <https://example.org/icons/island.svg> ;
> shui:propertyRole shui:IconRole ;
> .
>
> This example uses `sh:defaultValue` so that every instance of `ex:Island` without its own `ex:islandIcon` value is represented by the same icon.

#### Definitions

##### shui:PropertyRole Class

The class of roles that a property shape may take with respect to its focus nodes. It is not required, but recommended, that roles
defined in other namespaces subclass `shui:PropertyRole`.

##### shui:propertyRole Property

The property used to annotate property shapes with roles. Its value is expected to be either an instance of `shui:PropertyRole` or a
resource that itself declares a `shui:propertyRole` and an associated `sh:order` value.

### Registries

SHACL UI is designed to be extensible. Beyond the §12 Built-in Widgets,
additional widgets may be published in community-maintained *registries* that continue to
evolve after this specification has been published and the Working Group's charter has ended.

#### Community Widget Registry

The [community widget registry](https://github.com/w3c/shacl-resources/tree/main/shacl-ui) collects additional viewers and editors that extend the built-in widgets. It is
hosted in the `shacl-ui/` directory of the [w3c/shacl-resources](https://github.com/w3c/shacl-resources) repository, where it is
documented and maintained independently of this specification. Registered widgets are instances
of the widget classes (§6) defined here, identified in the `shuic` namespace (`http://www.w3.org/ns/shacl-ui-community/`) to keep them separate from the built-in `shui` namespace. Adding a widget requires no change to this specification.

Other extension points, such as §13 Property Roles, may be organized
into registries following the same approach.

### Summary of Syntax Rules from this Specification

### Security Considerations

TODO

### Privacy Considerations

TODO

### Internationalization Considerations

TODO

### Summary of SHACL Core Syntax to SHACL UI Index

This section enumerates the SHACL Core syntax elements and links to their corresponding SHACL UI representations.

|                                               | Section used                                                                                                |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Shapes                                        | |
| sh:NodeShape                                  |                                                                                                             |
| sh:PropertyShape                              |                                                                                                             |
| Constraint Components                         | |
| Value Type Constraint Components              | |
| sh:class                                      |                                                                                                             |
| sh:datatype                                   |                                                                                                             |
| sh:nodeKind                                   |                                                                                                             |
| Cardinality Constraint Components             | |
| sh:minCount                                   |                                                                                                             |
| sh:maxCount                                   |                                                                                                             |
| Value Range Constraint Components             | |
| sh:minExclusive                               |                                                                                                             |
| sh:minInclusive                               |                                                                                                             |
| sh:maxExclusive                               |                                                                                                             |
| sh:maxInclusive                               |                                                                                                             |
| String-based Constraint Components            | |
| sh:minLength                                  |                                                                                                             |
| sh:maxLength                                  |                                                                                                             |
| sh:pattern                                    |                                                                                                             |
| sh:singleLine                                 |                                                                                                             |
| sh:languageIn                                 |                                                                                                             |
| sh:uniqueLang                                 |                                                                                                             |
| List Constraint Components                    | |
| sh:memberShape                                |                                                                                                             |
| sh:minListLength                              |                                                                                                             |
| sh:maxListLength                              |                                                                                                             |
| sh:uniqueMembers                              |                                                                                                             |
| Property Pair Constraint Components           | |
| sh:equals                                     |                                                                                                             |
| sh:disjoint                                   |                                                                                                             |
| sh:subsetOf                                   |                                                                                                             |
| sh:lessThan                                   |                                                                                                             |
| sh:lessThanOrEquals                           |                                                                                                             |
| Logical Constraint Components                 | |
| sh:not                                        |                                                                                                             |
| sh:and                                        |                                                                                                             |
| sh:or                                         |                                                                                                             |
| sh:xone                                       |                                                                                                             |
| Shape-based Constraint Components             | |
| sh:node                                       |                                                                                                             |
| sh:property                                   |                                                                                                             |
| sh:someValue                                  |                                                                                                             |
| sh:qualifiedValueShape                        |                                                                                                             |
| sh:qualifiedMinCount                          |                                                                                                             |
| sh:qualifiedMaxCount                          |                                                                                                             |
| sh:reifierShape                               |                                                                                                             |
| sh:reificationRequired                        |                                                                                                             |
| Other Constraint Components                   | |
| sh:closed                                     |                                                                                                             |
| sh:ignoredProperties                          |                                                                                                             |
| sh:hasValue                                   |                                                                                                             |
| sh:in                                         |                                                                                                             |
| sh:rootClass                                  |                                                                                                             |
| Non-Validating Property Shape Characteristics | |
| sh:order                                      | §10.4 Grouping, Ordering, and Layout Hints |
| sh:group                                      | §10.4 Grouping, Ordering, and Layout Hints |
| sh:PropertyGroup                              | §10.4 Grouping, Ordering, and Layout Hints |
