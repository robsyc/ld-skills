---
title: "SPARQL 1.2 RL"
source: https://www.w3.org/TR/shacl12-rules/
family: shacl
version: "1.2"
status: W3C Working Draft
spec_date: 2026-10-21
fetched: 2026-10-26
---

# SPARQL 1.2 RL

> Inferencing rules deriving new triples from shapes.

## Contents

- Abstract
- 1 Introduction
  - 1.1 Terminology
  - 1.2 Document Conventions
- 2 Conformance
- 3 SPARQL-RL Overview
  - 3.1 Triple Patterns
  - 3.2 Recursion
  - 3.3 Filtering
  - 3.4 Negation
  - 3.5 Assignment and Creating RDF Terms
  - 3.6 Grouping and Aggregation
  - 3.7 Importing Rule Sets
  - 3.8 Data Blocks
  - 3.9 Matching Base Data
  - 3.10 Evaluating a Rule Set
- 4 SPARQL-RL Abstract Syntax
  - 4.1 Elements of the Abstract Syntax
  - 4.2 Well-formedness Conditions
  - 4.3 Rule Dependency
    - 4.3.1 Dependency Graph
    - 4.3.2 Dependency Graph Algorithm
  - 4.4 Stratification
    - 4.4.1 Stratification Condition
    - 4.4.2 Stratification Algorithm
  - 4.5 Processing Imports
- 5 Relationship between SPARQL-RL and SPARQL
- 6 Rule Set Evaluation
  - 6.1 Evaluation Definitions
  - 6.2 Preparation for Evaluation
  - 6.3 Evaluation of an Expression
  - 6.4 Evaluation of a Rule
  - 6.5 Evaluation of a Rule Set
  - 6.6 Worked Example
    - 6.6.1 Determining the Dependencies
    - 6.6.2 Calculating the Stratification
    - 6.6.3 Evaluating the Strata
- 7 SPARQL-RL Grammar
  - 7.1 Version Announcement
  - 7.2 White Space
  - 7.3 Comments
  - 7.4 IRI References
  - 7.5 Escape Sequences
  - 7.6 Grammar
  - 7.7 Selected Terminal Literal Strings
- A Translation of SPARQL-RL to SPARQL
- B Example Imports Algorithm
- C Internet Media Type and File Extension
- D Security Considerations
- E Privacy Considerations
- G Index
  - G.1 Terms defined by this specification
  - G.2 Terms defined by reference
- I References
  - I.1 Normative references
  - I.2 Informative references

---

## Abstract

This document defines *SPARQL-RL*, a [Datalog](https://en.wikipedia.org/wiki/Datalog)-style rules language for RDF.

SPARQL-RL generates new RDF data by evaluating a set of declarative
rules against an input RDF graph. Rules are written in a
SPARQL-like text syntax.

This specification is published by the [W3C Data Shapes Working Group](https://www.w3.org/groups/wg/data-shapes/).

## 1. Introduction

This document introduces SPARQL-RL. It is a mechanism for
deriving new RDF triples from existing RDF data through declarative rules.
The document defines the syntax and semantics of rule-based inference.

Implementations of SPARQL-RL provide one or both of the operations *infer* and *query*.
The *infer* operation applies the rules to a given *base graph* and produces an *inference graph* containing the
RDF triples derived by rule evaluation that do not appear in the base graph.
Combining the inference graph with the base graph is optional and
left to users.
The *query* operation determines whether and how a
given goal pattern can be derived from the *base graph* using the rules.

SPARQL-RL allows the creation of new RDF terms, including blank nodes,
that can be used in triple templates in the head of rules.

SPARQL-RL supports negation as failure, which could lead to
different inference graphs depending on the order in which rules are
evaluated. To avoid this, rules are evaluated using the technique
of *stratification*, which establishes an ordering among rules,
ensuring that the same inference graph is always produced.

SPARQL-RL provides grouping and aggregation, with assignment of the
aggregation function result to a variable in the body of a rule.

SPARQL-RL can be referred to as *SRL* when the context is clear.

### 1.1 Terminology

The following specifications provide fundamental terminology
used in this document:

- [RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/) [RDF12-CONCEPTS]
- [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/) [SPARQL12-QUERY]

### 1.2 Document Conventions

Examples of RDF data in this document use [RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/) [RDF12-TURTLE].

Within this document, the following namespace prefix bindings are used:

| Prefix | Namespace                                     |
| ------ | --------------------------------------------- |
| `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#`           |
| `:`    | `http://example/`                             |

Throughout the document, color-coded boxes contain rules in SPARQL-RL syntax
or contain RDF graphs in Turtle syntax.

```
# This box represents rules
```

```
# This box represents input data
```

```
# This box represents inferred data
```

## 2. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, and *MUST NOT* in this document
are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all
capitals, as shown here.

This specification defines conformance criteria for:

- SPARQL-RL Rule Set evaluation (§6)
- SPARQL-RL syntax (§7)

A *conforming SPARQL-RL document* is an [RDF string](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-string), encoded in UTF-8 [RFC3629],
and that conforms to the grammar and
additional constraints defined in 7.6 Grammar (§7.6).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This specification does not define how a SPARQL-RL processor handles non-conforming SPARQL-RL documents.

## 3. SPARQL-RL Overview

*This section is non-normative.*

SPARQL-RL infers new triples given a base graph and a rule set.
The output of evaluation is an inference graph containing the derived
triples that do not appear in the base graph.

Each rule has a pattern, called the body, and a result
template, called the head.
A rule is executed by finding the values for variables in the body
so that the body matches the combined base graph and
any inferred triples from the execution up to this point.
These values are then used to instantiate the triple templates
in the rule head to produce new inferred triples.

The rules are executed until no more triples are inferred,
and rules may be executed more than once as new inferred triples
become available.

SPARQL-RL execution is defined so that the order of rule execution
does not lead to different outcomes when creating new RDF terms,
including new blank nodes, or when testing for the absence of a
pattern. In other words, the same inference graph is produced
regardless of the order of rule execution.

SPARQL-RL has a human-friendly syntax inspired by [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/).
Rule set evaluation contains elements similar to SPARQL, with differences
in the details to ensure that the same inference graph is produced
regardless of the order of rule execution.

The examples in this section describe software components and
their dependencies: a frontend calls an application server, and
the application server queries a database that has a known
vulnerability.

### 3.1 Triple Patterns

A triple pattern is matched against triple data to give
values to variables. The pattern has
three elements, each of which is an RDF term, a variable,
or is a pattern for a [triple term](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term) containing variables.

In this first example, we have the following data in the base graph and rule set:
> **Example:**
>
> Example 1: Basic Example
>
> ```
> :frontend :callsService :app .
> :app      :queriesDatabase :db .
> :db       :hasVulnerability :vuln1 .
> ```
>
> ```
> RULE { ?x :dependsOn ?y } WHERE { ?x :callsService ?y }
> RULE { ?x :dependsOn ?y } WHERE { ?x :queriesDatabase ?y }
> ```
>
> ```
> :frontend :dependsOn :app .
> :app      :dependsOn :db .
> ```

The above rules, applied to the data, will conclude that `:frontend` depends on `:app`, and that `:app` depends on `:db`, whatever the kind of dependency.

We can then derive `:exposedTo` relationships by adding a rule that depends
on `:dependsOn` triples produced by the other rules
(see also 4.3 Rule Dependency (§4.3) below):
> **Example:**
>
> Example 2: Depending on inferred triples
>
> ```
> :frontend :callsService :app .
> :app      :queriesDatabase :db .
> :db       :hasVulnerability :vuln1 .
> ```
>
> ```
> RULE { ?x :dependsOn ?y } WHERE { ?x :callsService ?y }
> RULE { ?x :dependsOn ?y } WHERE { ?x :queriesDatabase ?y }
> RULE { ?x :exposedTo ?v } WHERE { ?x :dependsOn ?y . ?y :hasVulnerability ?v }
> ```
>
> ```
> :app      :exposedTo :vuln1 .
> :frontend :dependsOn :app .
> :app      :dependsOn :db .
> ```

### 3.2 Recursion

The `:exposedTo` rule of the previous section only reaches direct
dependencies: `:frontend` does not depend directly on `:db`, so
no `:exposedTo` triple is inferred for `:frontend`.
To propagate exposure along dependency chains of any length, we
replace that rule with two rules: a component is exposed to a
vulnerability it has, and a component is exposed to any
vulnerability that its direct dependencies are exposed to:
> **Example:**
>
> Example 3: Rule Recursion
>
> ```
> :frontend :callsService :app .
> :app      :queriesDatabase :db .
> :db       :hasVulnerability :vuln1 .
> ```
>
> ```
> RULE { ?x :dependsOn ?y } WHERE { ?x :callsService ?y }
> RULE { ?x :dependsOn ?y } WHERE { ?x :queriesDatabase ?y }
> RULE { ?x :exposedTo ?v } WHERE { ?x :hasVulnerability ?v }
> RULE { ?x :exposedTo ?v } WHERE { ?x :dependsOn ?y . ?y :exposedTo ?v }
> ```
>
> ```
> :db       :exposedTo :vuln1 .
> :app      :exposedTo :vuln1 .
> :frontend :exposedTo :vuln1 .
> :frontend :dependsOn :app .
> :app      :dependsOn :db .
> ```

Compared with the previous example, this adds `:db :exposedTo :vuln1` — the database is exposed to its
own vulnerability — and `:frontend :exposedTo :vuln1`:
the exposure reaches `:frontend` through the chain of
dependencies, however long the chain.

This last rule is a *recursive* rule: the body of the rule
depends on the head of the rule.

### 3.3 Filtering

We can use expressions in the body of rules to restrict the values of variables
in the matching of the body.
For example, given the severity of each vulnerability,
we can give a status to components that are exposed to a severe
vulnerability:
> **Example:**
>
> Example 4: Filtering
>
> ```
> :app1 :exposedTo :vuln1 .
> :app2 :exposedTo :vuln2 .
> :vuln1 :severity 9.1 .
> :vuln2 :severity 4.3 .
> ```
>
> ```
> RULE { ?x :status :criticallyExposed }
> WHERE {
>     ?x :exposedTo ?v .
>     ?v :severity ?s .
>     FILTER(?s >= 9.0)
> }
> ```
>
> ```
> :app1 :status :criticallyExposed .
> ```

`FILTER` evaluates an expression and keeps the current
set of variable bindings if the expression evaluates to true, and it discards the
current set of variable bindings if the expression evaluates to false.
This is the same as the [`FILTER` operation of SPARQL](https://www.w3.org/TR/sparql12-query/#termConstraint) and SPARQL-RL provides many of the same functions and operators as SPARQL.

### 3.4 Negation

Negation is used to specify a pattern that must not match.
This is called "negation as failure".

In order to evaluate a negation element, the rule set evaluation algorithm
ensures that all the rules that could produce triples matching the pattern
in the negation element have been completed. This is called *stratification* and ensures that the negation is based
on all the relevant possible triples, whether from the data or
from other rules. The rule containing the negation is
said to *depend* on the rules generating these triples
(see 4.3 Rule Dependency (§4.3) below).
> **Example:**
>
> Example 5: Negation as failure
>
> ```
> :app rdf:type :Component ;
>     :status :criticallyExposed .
>
> :logger rdf:type :Component .
> ```
>
> ```
> RULE { ?x :status :safeToDeploy }
> WHERE {
>     ?x rdf:type :Component .
>     NOT { ?x :status :criticallyExposed }
> }
> ```
>
> ```
> :logger :status :safeToDeploy .
> ```

### 3.5 Assignment and Creating RDF Terms

Assignment allows a rule to assign the result of an expression to a variable
in the body of a rule. This can be used to create new RDF terms based
on the data.
> **Example:**
>
> Example 6: Assignment
>
> ```
> RULE { ?v :riskScore ?r }
> WHERE {
>     ?v :severity ?s .
>     ?v :exploitLikelihood ?p .
>     SET ( ?r := ?s * ?p )
> }
> ```

Blank nodes can be used in the rule head, and each generates a fresh blank node
each time rule evaluation generates triples.
> **Example:**
>
> Example 7: Blank node in the rule head
>
> ```
> RULE { [] rdf:type :Notification ; :concerns ?x }
> WHERE { ?x :status :criticallyExposed }
> ```

Rules involving assignments, rules that create blank nodes
from evaluation of the rule head and rules with a template
that involves a [triple term](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term) containing [variables](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable) are run-once rules.
Such rules are run after all the rules that could produce data that they depend on,
and before any rules that depend on the data they produce.

This condition ensures that such rules do not loop back to themselves
and cause the creation of an unbounded number of RDF terms.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> A constant [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term) in a rule head does not make a rule a run-once rule, even when the term does not occur in the base graph: the rule contributes the same term each time it is
> evaluated, so it can only add a bounded number of terms.

If evaluating the expression in an assignment causes an error,
then the current solution mapping is rejected by the assignment.

### 3.6 Grouping and Aggregation

Rules with a group element are run-once rules.
Such rules are run after all the rules that could produce data that they
depend on, and before any rules that depend on the data they produce.
A group element consumes the complete collection of solution sequences of preceding rule elements in the rule body, collects them into groups based on group keys, then evaluates aggregation assignments.

The output is a solution sequence where each [solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping) is the current solution mapping extended with the group keys and
the values of the aggregation variables.

@@ example

### 3.7 Importing Rule Sets

A SPARQL-RL rule set can incorporate other rule sets by
including their URLs in the rule set imports of the rule set.
This allows rules to be structured into libraries shared between rule sets.

The `IMPORTS` statements of a rule set are processed before any of the rules
in the rule set are evaluated. During the importing step, if an imported rule set
has its own imports, those are also processed recursively.
Traversing `IMPORTS` statements during the processing of rule sets may
encounter cyclic imports. A rule set is imported only once;
cycles in the import statements graph do not lead to infinite loops.

Support for importing rule sets is optional for SPARQL-RL processors.
See 4.5 Processing Imports (§4.5) for further details.

### 3.8 Data Blocks

Data blocks provide RDF triples directly to the rule set evaluation.
Triples in data blocks are added to the inference graph and are available for
matching in the body of rules.

For example, a rule set can ship with known facts asserted
directly, rather than derived from data:
> **Example:**
>
> Example 8: Include data in a rule set
>
> ```
> DATA {
>     # Versions 2.0.0 and earlier suffer a known vulnerability
>     # and are assumed critically exposed.
>     :appV2 rdf:type :Component ;
>            :version "2.0.0" ;
>            :status :criticallyExposed .
> }
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> A data block is equivalent to a rule with an empty body:
> its triples are part of the inference graph without any rule
> being evaluated.

### 3.9 Matching Base Data

During §6 Rule Set Evaluation it may be
necessary to pattern match only on the original base graph,
not on any inferred triples.

An example of this is setting a default value.
The rule must test whether the base graph already contains a value and, if not,
the rule can then calculate a default value.
> **Example:**
>
> Example 9: Base Data with NOT
>
> ```
> :A :distanceMiles 5 .
> :A :distanceKilometers 8 .
> :B :distanceMiles 10 .
> ```
>
> ```
> RULE  { ?x :distanceKilometers ?kilometers }
> WHERE {
>     ?x :distanceMiles ?miles .
>     NOT DATA { ?x :distanceKilometers ?km }
>     SET ( ?kilometers := xsd:integer(?miles * 1.60934))
> }
> ```
>
> ```
> :B :distanceKilometers 16 .
> ```

Using `NOT DATA` allows other parts of the rule body to match inferred triples.
It is also possible to perform all rule body matching against the base graph by
using `WHERE DATA`.
Such rules then only rely on matching from the base graph.
> **Example:**
>
> Example 10: Base Data with WHERE
>
> ```
> RULE  { ?x :distanceKilometers ?kilometers }
> WHERE DATA {
>     ?x :distanceMiles ?miles .
>     NOT { ?x :distanceKilometers ?km }
>     SET ( ?kilometers := xsd:integer(?miles * 1.60934))
> }
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The matching in this section is on the base graph.
> It does not include triples added by rule set evaluation (§6.5) from the rule set `DATA` blocks
> (3.8 Data Blocks (§3.8)).

### 3.10 Evaluating a Rule Set

Rules are organized into rule sets.
A rule set and a data graph (the base graph) are inputs to evaluation.
The output is a graph, called the inference graph,
which is the set of triples produced by the evaluation process
that do not appear in the base graph.

During evaluation, triples inferred based on one rule are
available for matching in other rules.
Rule set evaluation proceeds until
no further triples can be inferred
from the inputs of the rule set and the base graph.

Evaluation starts with steps to prepare a rule set (§6.2) before the rules themselves are evaluated:

1. Where supported, the imports of the input rule set are resolved to form a
   rule set that includes all the rules of all
   imported rule sets.
   A processor signals an error if any import is not acceptable
   to the processor (4.5 Processing Imports (§4.5)).
2. Check that each rule is a well-formed rule.
3. Calculate the dependency graph.
4. A stratification is calculated
   (4.4 Stratification (§4.4))
   so that negation elements and run-once rules produce consistent,
   predictable outcomes. Stratification involves inspecting the dependencies
   between rules
   (4.3.1 Dependency Graph (§4.3.1)).

Once a rule set has been prepared, evaluation proceeds
by taking each layer from the stratification, in order,
evaluating the rules in that layer to completion,
and then moving on to the next layer.
When triples are inferred by execution of a rule, they are immediately
available to other rules as those rules are executed.

## 4. SPARQL-RL Abstract Syntax

The SPARQL-RL Abstract Syntax is the logical structure of SPARQL-RL.
It is used to define the execution algorithm of SPARQL-RL.

### 4.1 Elements of the Abstract Syntax

*[Variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable)*

A [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable) represents a possible [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term) in a triple pattern.
Variables are also used in expressions.

*Expression*

An expression is an [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term), a [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable),
or the application of a function or a functional form to arguments,
where each argument is itself an expression.
An expression is evaluated with respect to a [solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping), giving
an [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term) as the result, or evaluation results in an error. Expressions are compatible with [SPARQL expressions](https://www.w3.org/TR/sparql12-query/#expressions).

*Data block*

A data block is a set of triples.
These triples are added to the inference graph as additional facts and are
included in the inference process.

*Triple pattern*

A triple pattern is a 3-tuple where each element is
a [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable), an [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term), or a pattern for a [triple term](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term) with [variables](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable).
The second element of the tuple is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or a [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable). Triple patterns appear in the body of a rule and are used to match [RDF triples](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple).

*Triple template*

A triple template is a 3-tuple where each element is
a [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable), an [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term), or a template for a [triple term](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term) with [variables](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable).
The second element of the tuple is an [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri) or a [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable). Triple templates appear in the head of a rule and
are used to generate [RDF triples](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> A pattern or template for a [triple term](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term) in which no [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable) occurs is a [triple term](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term), and therefore also
> an [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term).

*Triple pattern element*

A triple pattern element is a triple pattern that appears as a rule element.

*Filter element*

A filter element is an expression that appears as a rule element.
It is used to restrict the values of variables
in pattern matching.

*Negation element*

A negation element is a rule element.
It has a *negation element body* composed of a sequence of triple pattern elements and filter elements.
A negation element has a flag, `.evaldata`,
to indicate which graph to use for matching
the negation element body.

*Assignment element*

An assignment element is a rule element that is
a pair consisting
of a [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable), called the *assignment variable*,
and an expression, called the *assignment expression*.

*Group element*

A group element is a rule element with a set of variables, called the *group keys*,
a *group pattern*, and a set of *aggregation assignments*.
Each aggregation assignment is a pair consisting of
a [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable), called the *aggregation variable*,
and an *aggregation function*.
The group pattern is composed
of a sequence of triple pattern elements and filter elements.

*Rule element*

A rule element is any one of triple pattern element, filter element, negation element, assignment element, or group element.

*Rule head*

A rule head is a sequence of triple templates.

*Rule body*

A rule body is a sequence of rule elements;
that is, each sequence element is one of
a triple pattern element,
a filter element,
a negation element,
an assignment element, or
a group element.

*Rule set imports*

Rule set imports (often just "imports") are
the collection of URLs
from the `IMPORTS` statements
for other rule sets that will be included during evaluation.

*Rule*

A rule contains a rule head (often just "head"),
a rule body (often just "body"),
and a flag `.evaldata` to indicate which
graph to use for matching triple patterns in the body.
A rule can be given a URI or a blank node to help identify it.

*Run-once rule*

A run-once rule is a rule that is run exactly once at a
particular point in the evaluation of a rule set.
A rule is a run-once rule if any of the following hold:

- the rule body has an assignment element;
- the rule body has a group element;
- a triple template of the rule head has a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node);
- a triple template of the rule head has a template for a [triple term](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term) in which a [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable) occurs.

*General rule*

A general rule is a rule that is not a run-once rule.
General rules may run more than once during rule set evaluation.

*Rule set*

A rule set is a collection of zero or more rules,
a collection of zero or more data blocks,
and a collection of zero or more rule set imports.
A *resolved rule set* is a rule set that has no imports.
A resolved rule set is created from another rule set by applying the imports process (§4.5).

*Base graph*

A base graph is the [RDF graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph) given as input to the
evaluation process.

*Inference graph*

An inference graph is an [RDF graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph) produced by
a rule set evaluation.
It contains all inferred triples not present in the base graph that are inferred by applying the rule set to the base graph.

*Rule set evaluation*

A rule set evaluation is the process of applying a rule set to a base graph to produce an inference graph.
A *rule evaluation* is the process of evaluating a rule once.
Evaluating a rule produces all the triples given by the rule head by the evaluation of the rule body, regardless of whether a
triple is in the base graph, already inferred during rule set evaluation,
or is a new inferred triple.
During rule set evaluation, a rule may be evaluated more than once.

SPARQL-RL provides two operations, infer and query.

*Infer*

Infer is the operation that applies a rule set to a given base graph and produces an inference graph containing inferred
triples. It applies the full rule set evaluation.

*Query*

Query is the operation that determines whether a given pattern
can be derived from a base graph using the rule set and
returns a solution sequence in which each [solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping) gives RDF terms for variables.

Query has the effect of performing an infer operation,
followed by matching the goal pattern to the combined base graph and inference graph.

The query operation may not evaluate all rules; instead, it
may only evaluate rules that are necessary to answer the query
goal.

*SPARQL-RL processor*

A SPARQL-RL processor is a system that implements the SPARQL-RL
specification, can evaluate rule sets, and provides one or both
of the operations infer and query.

In a triple pattern or a triple template,
position 1 of the tuple is informally called the *subject*,
position 2 is informally called the *predicate*, and
position 3 is informally called the *object*.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The elements of a sequence of rule elements are labeled starting at 1.

The following notation is used for the various components of rule sets and rules.

*Component Notation*

| Component              | Usage                                                                                                                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ruleset.rules`        | The rules of a rule set.                                                                                                            |
| `ruleset.data`         | The [RDF graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph) formed by the union of the data blocks in the rule set.      |
| `ruleset.imports`      | The set of imports of a rule set.                                            |
| `rule.head`            | The triple templates of the rule head.                                   |
| `rule.body`            | The rule elements of the rule.                                                   |
| `rule.evaldata`        | A boolean flag; if *false*, the rule body is matched against the base graph.  |
| `rule.id`              | An identifier for the rule, which is a [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) or [IRI](https://www.w3.org/TR/rdf12-concepts/#dfn-iri).                     |
| `filter.expr`          | The expression of a filter element.                                      |
| `assign.var`           | The assignment variable of the assignment element.          |
| `assign.expr`          | The assignment expression.                                                                                             |
| `negation.inner`       | The negation element body of a negation element.            |
| `negation.evaldata`    | A boolean flag; if *false*, the `negation.inner` is matched against the base graph.                                               |
| `group.keys`           | The set of group keys of a group element.                                 |
| `group.pattern`        | The group pattern of a group element.                                  |
| `group.aggregations`   | The aggregation assignments of a group element.               |
| `aggregation.variable` | The aggregation variable of an aggregation assignment. |
| `aggregation.function` | The aggregation function of an aggregation assignment. |

### 4.2 Well-formedness Conditions

*Well-formedness* is a set of conditions on the abstract syntax of
a rule set. Together, these conditions ensure
that a [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable) in the head of a rule has a value defined in the body of the rule;
that each variable in a filter element or assignment expression has a value at the point of evaluation;
and that each assignment variable and aggregation variable in a rule is new and has not been used earlier in the rule body.

Let *S* be a sequence of rule elements.

Let *elti* be the i-th element of *S*,
and let *N* be the length of the sequence.

Let *V0* be a set of variables, called the initial
variables of the sequence *S*.

Define *vars(S, i, V0)* as the set of variables
that are in scope after the i-th element of the sequence *S*,
given the initial variables *V0*. *vars(S, i, V0)* is defined inductively:

- Let *vars(S, 0, V0)* be *V0*.
- Let *vars(S, i, V0)*, for each i from 1 to *N* be
  * if *elti* is a triple pattern element and *X* is the set of variables that occur in the triple pattern element then
    + *vars(S, i, V0)* is the set *X* ∪ *vars(S, i-1, V0)*.
  * if *elti* is an assignment element with assignment variable *avar* then
    + *vars(S, i, V0)* is the set `{` *avar* `}` ∪ *vars(S, i-1, V0)*.
  * if *elti* is a group element, *GRP*,
    where the set *aggVars* is the set of aggregation variables of *GRP* then
    + *vars(S, i, V0)* is the set *vars(S, i-1, V0)* ∪ *GRP.keys* ∪ *aggVars*.
  * otherwise,
    + *vars(S, i, V0)* is equal to the set *vars(S, i-1, V0)*.

Define *vars(S, V0)*, the set of variables in-scope for *S* as *vars(S, N, V0)*, the set of variables in-scope
after the last element of the sequence.

A sequence of rule elements, *S*,
is a *well-formed sequence*,
given a set of variables *V0*,
if the following conditions are met for each *i*,
from 1 to *N*:

- if *elti* is a filter element then
  * every [variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable) mentioned in the filter element is an element of *vars(S, i-1, V0)*.
- if *elti* is an assignment element then
  * every variable mentioned in the assignment expression is an element of *vars(S, i-1, V0)*
  * the assignment variable is not an element of *vars(S, i-1, V0)*.
- if *elti* is a negation element with negation element body *P* then
  * the sequence of rule elements in the negation element body is a well-formed sequence,
    with initial variables *vars(S, i-1, V0)*.
- if *elti* is a group element, where *P* is the group pattern of the group element *elti* then
  * the sequence of rule elements in the group pattern given initial variables *vars(S, i-1, V0)* is a well-formed sequence.
  * each member of the group keys is an element of *vars(S, i-1, V0)* ∪ *vars(P, vars(S, i-1, V0))*.
  * none of the aggregation variables occur in the set of
    variables *vars(P, vars(S, i-1, V0))*.
  * the aggregation variables are distinct.
  * the [variables](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable) in aggregation functions appear
    in *vars(P, vars(S, i-1, V0))*.

A rule is a *well-formed rule* if the sequence of rule elements of the rule body is a well-formed sequence, starting with *V0* being the empty set,
and if each variable in a triple template of the rule head is an element of *vars(S, V0)*.

A rule set is a *well-formed rule set* if and only if all
rules of the rule set are well-formed rules.

### 4.3 Rule Dependency

A rule `R1` depends on a rule `R2` if the output of the second rule
affects the evaluation of the body of the first rule. That is, the head of `R2` has a triple template that can generate a triple that matches
a triple pattern in the body of `R1`,
either as a triple pattern element, or inside a negation element or a group pattern.

There are two kinds of dependency: closed dependencies and open dependencies.
A *closed dependency* ensures that rule `R2` has generated all its possible output before rule `R1` is executed.
If a rule dependency is not closed, it is an *open dependency*.
It allows the first rule `R1` to be executed
while the rule `R2` might be run again to generate further triples
which can then cause `R1` to be reevaluated with the new triples from `R2`.

A rule with flag `.evaldata` set to `false` matches using the base graph and the rule has no dependencies.

In this first example, the first rule has an open dependency
on the second rule.
> **Example:**
>
> Example 11: Open Dependency
>
> ```
> RULE { ?x :exposedTo ?v } WHERE { ?x :dependsOn ?y . ?y :hasVulnerability ?v }
> RULE { ?x :dependsOn ?y } WHERE { ?x :callsService ?y }
> ```

In this second example, the first rule has a closed dependency
on the second rule: the triple pattern `?x :status :criticallyExposed` occurs inside a negation element of the first rule and
matches the triple template in the head of the second rule.
The first rule cannot be evaluated until the second rule
has generated all its possible output.
> **Example:**
>
> Example 12: Closed Dependency
>
> ```
> RULE { ?x :status :safeToDeploy }
> WHERE { ?x rdf:type :Component . NOT { ?x :status :criticallyExposed } }
>
> RULE { ?x :status :criticallyExposed } WHERE { ?x :exposedTo ?v }
> ```

*Triple pattern matching*

A triple pattern matches a triple template if
the triple template can generate a triple that matches the triple pattern.

*Triple pattern dependency*

A triple pattern *depends on* a triple template if the triple pattern can match the triple template.

*Rule dependency*

Rule `R1` *depends on* rule `R2` if `R1.evaldata` is `true` and any triple pattern in the body of `R1`,
whether as a triple pattern element, inside a negation element `neg` where `neg.evaldata` is `true`,
or inside a group pattern, depends on a triple template in the head of `R2`.

*Closed dependency*

A rule dependency of rule `R1` on rule `R2` is a closed dependency if any of the following conditions hold:

- A triple pattern occurring inside a negation element of `R1` where the negation element flag `.evaldata` is `true` matches a triple template in the rule head of `R2`.
- Rule `R1` depends on rule `R2` and `R1` is a run-once rule.

*Open dependency*

A rule dependency of rule `R1` on rule `R2` is an open dependency if the dependency is not a closed dependency.

A triple template can *generate* an [RDF triple](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple) `T1` if there are values for the variables of the triple template such that replacing variables by values
in the template gives a triple `T2` where `T2` [equals](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-equality) `T1`.

Similarly, a triple pattern *matches* a triple `T1` if there are values for the variables of the triple pattern such that replacing variables, including
treating blank nodes as variables,
in the pattern by the values gives a triple `T2` where `T2` [equals](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-equality) `T1`.

If a variable is used more than once in a triple template or triple pattern, then the same RDF term
is used as the replacement.

Replacing variables by RDF terms in a triple pattern
includes replacing variables inside [triple terms](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term).

#### 4.3.1 Dependency Graph

The dependencies between rules are represented as a directed graph,
called the dependency graph.
The vertices of the graph are the rules of the rule set, and the edges
are labeled either *open* or *closed* according to
whether the dependency is an open dependency or a closed dependency.

*Dependency graph*

A dependency graph of a rule set is a directed graph where each
vertex is a rule in the rule set, and an edge exists from rule `R1` to rule `R2` if `R1` depends on `R2`.
The edge is labeled either *open* or *closed* according to whether the dependency
is an open dependency or a closed dependency.

*Transitive rule dependency*

A rule `R1` has a transitive dependency on rule `R2` if there is a path in the dependency graph from `R1` to `R2`.

*Recursive rule dependency*

A rule `R` has a recursive dependency if there is a cyclic path
in the dependency graph involving `R`.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The dependency graph is not affected by the base graph.

#### 4.3.2 Dependency Graph Algorithm

The following algorithm gives one
possible method for constructing the dependency graph from a rule set. Conformance depends on producing a dependency graph
that meets the definitions of a dependency graph,
not on the use of this procedure.

```
define mergeLabel(oldLabel, newLabel):
    # Closed dependency overrides open dependency.
    if oldLabel == "open" and newLabel == "open":
        the result is "open"
    else:
        the result is "closed"
    endif
enddefine

# output -- Dependency graph with rule vertices and labeled edges.
define buildDependencyGraph(ruleSet):
    # edgeLabelMap maps (R1, R2) to "open" or "closed"
    let edgeLabelMap be a map from pair (rule, rule) to label

    foreach rule R1 in ruleSet.rules:
        let bodyDependencies = {}

        if R1.evaldata then:
            # Classify each triple pattern TP in the rule as requiring "open" or "closed"
            # depending on whether it is in a negation element or a group pattern, or not.
            foreach rule element RBE in R1.body:
                if RBE is a triple pattern element of triple pattern TP:
                    let item be a pair (TP, "open")
                    add item to bodyDependencies
                else if RBE is a filter element:
                    # Do nothing
                else if RBE is a negation element:
                    if RBE.evaldata then:
                        foreach triple pattern TP in RBE.inner:
                            let item be a pair (TP, "closed")
                            add item to bodyDependencies
                        endfor
                    endif
                else if RBE is an assignment element:
                    # Do nothing
                else if RBE is a group element:
                    foreach triple pattern TP in RBE.pattern:
                        let item be a pair (TP, "closed")
                        add item to bodyDependencies
                    endfor
                endif
            endfor
        endif

        foreach pair (triple pattern TP, depLabel) in bodyDependencies:
            if R1 is a run-once rule:
                set depLabel to "closed"
            endif
            # Find dependencies for this triple pattern element or negation element.
            foreach rule R2 in ruleSet.rules:
                foreach triple template TT in R2.head:
                    if triple pattern TP matches triple template TT:
                        let key = (R1, R2)
                        if edgeLabelMap contains key:
                            let oldLabel = edgeLabelMap.get(key)
                            let merged = mergeLabel(oldLabel, depLabel)
                            edgeLabelMap.set(key, merged)
                        else:
                            edgeLabelMap.set(key, depLabel)
                        endif
                    endif
                endfor
            endfor
        endfor
    endfor

    let DP = { }
    foreach entry ((R1, R2), label) in edgeLabelMap:
        add an edge (R1 -> R2) labeled with label to DP
    endfor

    the result is DP
enddefine
```

### 4.4 Stratification

Stratification is the process of partitioning a rule set into an ordered sequence of stratification layers (also known
as "strata", singular "stratum"). Rules in lower strata are
evaluated before rules in higher strata.

Stratification imposes constraints on dependencies between rules to ensure that negation elements, group elements,
and run-once rules depend only
on results computed using earlier (lower) strata and the base graph.
This guarantees a single, well-defined, and finite
outcome from the evaluation of a rule set over a given base graph.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> A stratification process may also be used to make other evaluation
> decisions. This document describes the necessary conditions for
> consistent evaluation and gives one possible way to form a
> stratification. Implementations need to meet the conditions
> described here in order to get compatible behavior, but they are not
> required to implement the algorithm as presented.

*Stratification layer*

A stratification layer `SL` is a pair of disjoint sets of
rules (`SL.once`, `SL.general`). `SL.once` is exactly the run-once rules of the layer;
these rules are each evaluated
exactly once at the start of evaluation of the stratification layer. `SL.general` is the set of remaining rules of the layer,
which are evaluated repeatedly until no new triples are inferred.

*Stratification*

A stratification of a rule set is a sequence of stratification layers.
Each rule in a rule set appears in exactly one of the sets of one of
the stratification layers.

The stratification layers of a stratification are numbered
from zero. The *stratum number* of a rule is the number
of the stratification layer that contains the rule.
A rule with a smaller stratum number is in a *lower* stratum;
one with a larger stratum number is in a *higher* stratum.

For every edge from rule `R1` to rule `R2` in the dependency graph of the rule set:

- if the edge is labeled *closed*, the stratum number of `R1` is strictly greater than the stratum number of `R2`.
- if the edge is labeled *open*, the stratum number of `R1` is greater than or equal to the stratum number of `R2`.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> A rule set can have more than one stratification.
> An implementation can use any stratification of the rule set.

#### 4.4.1 Stratification Condition

Stratification is only defined when the following condition is
satisfied. If a rule set does not meet this condition, then this
specification does not define an outcome for the evaluation of
such a rule set.

*Stratification condition*

The stratification condition requires that
there is no recursive dependency involving a closed dependency in the dependency graph for a rule set.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The stratification condition is exactly the condition for a stratification to exist: a stratification of a rule set can
> be formed if and only if no cyclic path in the dependency graph of
> the rule set contains a closed dependency.

#### 4.4.2 Stratification Algorithm

The following algorithm gives one possible stratification based solely
on the rule set.

```
define stratification(ruleSet):

    let DP = Dependency graph for the rule set.
    let stratumMap be a map from rule to integer

    # The dependency graph should satisfy the stratification condition.
    # The check for unbounded stratification is a guard
    # due to a violation of the stratification condition.
    let limit = num rules + 1
    let maxStratum = 0

    # initialize stratumMap
    foreach rule in ruleSet.rules:
        stratumMap.set(rule, 0)
    endfor

    let changed = true
    while changed:
        changed = false
        foreach edge E in DP:
            # Edge from pRule to qRule with a label
            let pRule = source of edge
            let qRule = destination of the edge
            let label = edge label

            if label == "open":
                if stratumMap.get(pRule) < stratumMap.get(qRule):
                    stratumMap.set(pRule, stratumMap.get(qRule))
                    changed = true
                endif
            endif
            if label == "closed":
                if stratumMap.get(pRule) <= stratumMap.get(qRule):
                    let xStratum = 1 + stratumMap.get(qRule)
                    if xStratum > limit:
                        # Stratification requirement violated
                        error "Stratification error"
                    endif
                    stratumMap.set(pRule, xStratum)
                    maxStratum = max(maxStratum, xStratum)
                    changed = true
                endif
            endif
        endfor
    endwhile

    # Initialize the result map.
    let stratumRules be a map from integer to rules
    foreach i = 0 to maxStratum:
        stratumRules.set(i, {})
    endfor

    # Gather rules in stratumMap with the same level number
    foreach rule R in map stratumMap:
        let stratumNum = stratumMap.get(R)
        add R to stratumRules.get(stratumNum)
    endfor

    # Partition each level into once and general
    let stratumLevels be a sequence of pairs of sets of rules
    foreach i = 0 to maxStratum:
        let rules = stratumRules.get(i)
        let once = { R in rules | R is a run-once rule }
        let general = rules \ once
        stratumLevels.set(i, pair(once, general))
    endfor

    the result is stratumLevels
enddefine
```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> A consequence of the stratification condition is that once a run-once rule is evaluated (§6.4),
> the data used to determine the outcome of the rule will not
> change during further evaluation.

A step-by-step application of dependency analysis and
stratification to a complete rule set, followed through to
evaluation, is given in 6.6 Worked Example (§6.6).

### 4.5 Processing Imports

Reading documents from the web has security implications.
Support for importing rule sets is optional for SPARQL-RL processors.
Further, implementations *MAY* provide partial support,
such as supporting imports of certain rule sets and not others,
and possibly from a verified copy.

The following conditions apply to imports processing:

- Implementations that do not support importing rule sets *MUST* reject
  a rule set that contains `IMPORTS` statements and signal an error.
- An implementation that provides partial support *MUST* signal an error if it encounters an import
  that it does not support.
- An implementation *MUST* signal an error if it cannot resolve the import document,
  or if the document is not syntactically valid.
- Processors *MUST* import a rule set only once to avoid infinite loops
  when processing `IMPORTS` statements.

A resolved rule set is produced from another rule set by
recursively reading all rule sets mentioned
in the imports of that other rule set.

An example algorithm is provided in B. Example Imports Algorithm (§B).

## 5. Relationship between SPARQL-RL and SPARQL

*This section is non-normative.*

SRL and SPARQL have a close relationship. SRL is designed to be compatible
with SPARQL, and many of the constructs in SRL are taken from, or inspired by,
SPARQL pattern matching. However, there are some differences.

In SRL, `RULE` variables are always bound before use, whether used in an
expression of `FILTER` or `SET`, or used in triple templates of the rule head. SPARQL `CONSTRUCT` queries and `INSERT` updates will
produce partial results if a variable occurs in the `CONSTRUCT` or `INSERT` template but is not given a value in the `WHERE` clause.

- §4.2 Well-formedness Conditions ensure that
  variables appear in at least one triple pattern element,
  or as an assignment variable,
  before use in a filter element or assignment element within the rule body.
- The SRL `SET` form and SPARQL `BIND` form have different
  error-handling behavior. An error encountered in `SET` causes the
  current solution to be filtered out, whereas `BIND` does not
  set the variable in the current solution but passes on the solution. `SET(?var := expr)` would be the same as
  SPARQL with `BIND(expr AS ?var)` followed by `FILTER(BOUND(?var))`.
- The syntax of a rule body `WHERE` clause
  does not include `UNION` or `OPTIONAL` syntax.
  These SPARQL elements can lead to unbound variables.
  The effect of `UNION` or `OPTIONAL` can be achieved using well-formed rules.

Other differences include:

- The syntax of `NOT` limits the inner body to triple
  patterns and filters, and does not allow nested patterns. `NOT` executes as a filter at the point in the rule body
  where it is written, unlike SPARQL `FILTER NOT EXISTS`.

- Property path syntax only covers paths with `/` and `^`.
  These can be expanded into triple patterns.
  It does not allow the arbitrary length operators `*` and `+`.
  Arbitrary length paths can be expressed in SPARQL-RL
  with recursion as a more general approach.

- Some functions are not included in the SRL syntax. There is no `COALESCE` or `BOUND`. There are no hash functions. There
  is no `RAND`, because it has different results each time it is
  called.
  > **Note:**
  >
  > > **Note:**
  > >
  > > Note
  >
  > `NOW()` is permitted and is defined to return the same
  > point in time throughout a rule set evaluation.

- Using `BNODE` produces different blank nodes on each call. The
  result of rule set evaluation will produce inference graphs that are [graph isomorphic](https://www.w3.org/TR/rdf12-concepts/#graph-isomorphism).

- `UUID` and `STRUUID` can be used to generate unique identifiers.
  Rules should not inspect these generated identifiers, only use them
  to generate triples.

  Specialized generators can be used for testing reproducibility,
  similar to testing the outcome of `NOW`.

## 6. Rule Set Evaluation

This section defines the outcome of evaluating a rule set on given data.
Implementations are not required to use this algorithm.
An implementation can use any algorithm that generates the same outcome.

```
Inputs: graph G, called the base graph, and a rule set RS.
Output: an RDF graph GI of inferred triples
```

The inferred triples do not include triples present in
the base graph.

### 6.1 Evaluation Definitions

*[Solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping)*

A [solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping), *μ*, is a partial function `μ : V → T`,
where *V* is the set of all variables
and *T* is the set of all [RDF terms](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term).
The domain of *μ* is denoted
by `dom(μ)`, and it is the subset
of *V* for which *μ* is defined. The term [solution](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping) can be used when it is clear that a [solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping) is meant.
Write *μ0* for the solution mapping, such that `dom(μ0)` is the empty set.

*Substitution function*

The substitution function, or just a *substitution*,
is a function `subst(μ, triple pattern)` that returns a triple pattern where each occurrence in the triple pattern of a variable *var* that is in the `dom(μ)` is replaced by the [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term) given by the [solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping) for *var*.
If the triple pattern result has no variables, then it is an [RDF triple](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-triple).

The function `subst(μ, triple template)` is similarly defined. Each occurrence of a variable in the triple template is replaced by the [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term) given by the [solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping) for *var*.

*Template instance function*

The template instance function is a function `replaceBlankNodes(list of triple templates)` that
returns a list of triple templates where each [blank node](https://www.w3.org/TR/rdf12-concepts/#dfn-blank-node) in the argument is replaced by a fresh blank node.
Multiple occurrences of the same blank node
are replaced by the same fresh blank node.

*Evaluation graph*

An evaluation graph is an [RDF graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph) that combines the base graph and all triples produced during the evaluation of a rule set.

*Graph match*

A graph match finds the ways to
map a triple pattern onto triples in an [RDF graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph).

Let *G* be an [RDF graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph) and *TP* be a triple pattern.
The function `graphMatch(G, TP)` returns a set of all possible [solutions](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping) that,
when applied to the triple pattern, produce a triple that is in
graph `G`.

Let *G* be an [RDF graph](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-graph), *TP* be a triple pattern,
and *V* be the set of variables occurring in *TP*.

```
graphMatch(G, TP) = { μ | dom(μ) = V and subst(μ, TP) is a triple in G }
```

*Solution compatible*

Two solutions S1 and S2 are compatible if they agree on the variables in common.

Let S1 and S2 be solutions.

```
compatible(μ1, μ2) = true
                      if forall v in dom(μ1) intersection dom(μ2)
                          μ1(v) = μ2(v)
compatible(μ1, μ2) = false otherwise
```

*Solution sequence*

A solution sequence is a multi-set of solutions.
There is no defined order to the sequence.
It is equivalent to an unordered list and it can contain duplicates.

*Solution merge*

If two solutions are compatible, the merge of two solutions is the solution
that maps variables of each solution to the [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term) from one or other of the solutions.

Let *μ*1, *μ*2 be solution mappings, and S1 and S2 be solution sequences.

```
merge(μ1, μ2) = μ such that
                    μ(v) = μ1(v) if v in dom(μ1)
                    μ(v) = μ2(v) otherwise
```

```
merge(S1, S2) = { μ |
                    μ1 in S1, μ2 in S2
                    and compatible(μ1, μ2)
                    μ = merge(μ1, μ2) }
```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The domain of `merge(μ1, μ2)` is `domain(μ1) ∪ domain(μ2)`.
>
> If the two solutions have no variables in common, then they are compatible,
> and the merge of the two solutions is the union of *μ*1 and *μ*2.

*[Effective boolean value](https://www.w3.org/TR/sparql12-query/#ebv)*

The function `EBV(x)` returns the effective boolean value
for an [RDF term](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term).

### 6.2 Preparation for Evaluation

Evaluation of a rule set involves collecting all imported rule sets,
building a single, combined rule set as described in 4.5 Processing Imports (§4.5).

Next, the combined rule set is prepared
for evaluation with the following steps.

1. Check that each rule is a well-formed rule, as described in 4.2 Well-formedness Conditions (§4.2).
2. Calculate the dependency graph, as described in 4.3.2 Dependency Graph Algorithm (§4.3.2).
3. Calculate a stratification of the combined rule set, as described in 4.4 Stratification (§4.4). 4.4.2 Stratification Algorithm (§4.4.2) gives one way to calculate a stratification.

### 6.3 Evaluation of an Expression

An expression, whether used in a filter element or
an assignment element, is evaluated with
respect to a [solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping). The solution mapping provides the
RDF term values for each variable in the expression.
The well-formedness requirements of 4.2 Well-formedness Conditions (§4.2) ensure that all variables in the expression
appear in the solution mapping.

```
define evalFunction(F, μ):
    # F is an expression: an RDF term, a variable, or op(expr1, ..., exprN)
    #   where op is a function or a functional form.
    # μ is a solution mapping

    # Any error during evaluation causes evalFunction to return an error.
    if F is an error:
        return error
    endif
    if F is an RDF term:
        return F
    endif
    if F is a variable:
        # By well-formedness, F ∈ dom(μ).
        return μ(F)
    endif
    # F is of the form F = op(expr1, ..., exprN)
    if op is a functional form (e.g., IF, logical-or):
        # Evaluated specifically for op; op may evaluate only some arguments.
        # For example, IF(c, t, f) evaluates c, then exactly
        # one of t or f is evaluated.
        return the value defined for op over expr1, ..., exprN under μ
    endif
    # op is an ordinary function: evaluate all arguments first.
    return op(evalFunction(expr1, μ), ..., evalFunction(exprN, μ))
enddefine
```

```
define evalAggregate(AGGF, SEQ):
@@
    # AGGF is an aggregation function, which has an argument of a variable
    # and a solution sequence. It returns an RDF term value.

    # Noting that DISTINCT is only permitted for COUNT
    # Special case COUNT(*).
enddefine
```

*Aggregation functions*

| Aggregation Function | SPARQL equivalent                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------ |
| `COUNT`              | [SPARQL COUNT](https://www.w3.org/TR/sparql12-query/#aggCount) with *distinct* set `false` |
| `COUNT DISTINCT`     | [SPARQL COUNT](https://www.w3.org/TR/sparql12-query/#aggCount) with *distinct* set `true`  |
| `MIN`                | [SPARQL MIN](https://www.w3.org/TR/sparql12-query/#aggMin)                                 |
| `MAX`                | [SPARQL MAX](https://www.w3.org/TR/sparql12-query/#aggMax)                                 |
| `SUM`                | [SPARQL SUM](https://www.w3.org/TR/sparql12-query/#aggSum)                                 |

> **Note:**
>
> > **Note:**
> >
> > Editor's note
>
> Any error in calculating an aggregate function causes an
> evaluation error and that group is not added to the results.

### 6.4 Evaluation of a Rule

A rule is evaluated by calculating a solution sequence from the rule body and then using each [solution mapping](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping) of the solution sequence to
generate triples using the rule head.

Within the body of a rule, blank nodes in triple patterns behave like variables.
This is compatible with [SPARQL graph pattern matching](https://www.w3.org/TR/sparql12-query/#BGPsparql).

*Treating blank nodes as variables*

Blank nodes are treated as variables within triple patterns of a rule body by replacing each blank node by a variable which is
not used in the rule.
This includes replacing blank nodes inside [triple terms](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-term).
The same variable is used for each occurrence of
the same blank node, and a different variable is used for each
different blank node.

```
# Evaluate rule body
# This function returns a sequence of solutions

define evalRuleElements(B, SEQ, G, GD):
    where
        B is a sequence of rule elements
        SEQ is a solution sequence
        G and GD are RDF graphs

    foreach rule element rElt in B:

        if rElt is a triple pattern element TP:
            X = graphMatch(G, TP)
            SEQ1 = {}
            foreach μ1 in X:
                foreach μ2 in SEQ:
                    if compatible(μ1, μ2):
                        μ3 = merge(μ1, μ2)
                        add μ3 to SEQ1
                    endif
                endfor
            endfor
        endif

        if rElt is a filter element F:
            SEQ1 = {}
            foreach solution μ in SEQ:
                let x = evalFunction(F.expr, μ)
                if x is not an error and EBV(x) is true:
                    add μ to SEQ1
                endif
            endfor
        endif

        if rElt is a negation element N:
            SEQ1 = {}
            foreach solution μ in SEQ:
                S = sequence{ μ }
                if N.evaldata:
                    NEG = evalRuleElements(N.inner, S, G, GD)
                else:
                    NEG = evalRuleElements(N.inner, S, GD, GD)
                endif
                if NEG is empty:
                    add μ to SEQ1
                endif
            endfor
        endif

        if rElt is an assignment element A:
            SEQ1 = {}
            foreach solution μ in SEQ:
                let x = evalFunction(A.expr, μ)
                if x is not an error:
                    # Add mapping A.var -> x to solution μ
                    let μ2 be a solution mapping μ ∪ { (A.var, x) }
                    add μ2 to SEQ1
                else:
                    # Error: drop solution μ
                endif
            endfor
        endif

        ## What about COUNT(*)?
        if rElt is a group element GRP:
            SEQ1 = {}
            foreach solution μ in SEQ:
                let μp be the restriction of μ to GRP.keys
                let SEQX = evalRuleElements(GRP.pattern, { μp }, G, GD)
                # Allocate solution mappings to groups.
                let KGRP = empty map of solution mappings to solution sequences
                foreach solution μx in SEQX:
                    let μk be the restriction of μx to GRP.keys
                    if KGRP[μk] is defined:
                        add μx to the solution sequence KGRP[μk]
                    else:
                        KGRP[μk] = solution sequence of one element μx
                    endif
                endfor
                # For each group, calculate the aggregate functions and extend
                # the current solution mapping μ with the group keys
                # and the results of the aggregation assignments.
                foreach key K of map KGRP:
                    let X be the solution sequence of KGRP[K]
                    let Z be an empty solution mapping
                    foreach aggregation function F in GRP.aggregations:
                        let V = calculate F.function(X)
                        add solution mapping (F.var, V) to Z
                    endfor
                    Z = merge(Z, K)
                    Z = merge(Z, μ)
                    add Z to SEQ1
                endfor
            endfor
        endif
        SEQ = SEQ1
    endfor

    return SEQ
enddefine

define evalRule(R, G, GD):
    where
        R is a well-formed rule
        G and GD are RDF graphs
    let B be R.body
        treating blank nodes as variables.

    # Solution sequence of one solution that does not map any variables.
    let SEQ0 be the solution sequence { μ0 }

    if R.evaldata:
        let SEQ = evalRuleElements(B, SEQ0, G, GD)
    else:
        let SEQ = evalRuleElements(B, SEQ0, GD, GD)
    endif

    # Evaluate rule head
    let OUT = empty set
    foreach μ in SEQ:
        let S = {}
        # Rule head with each blank node replaced by a fresh blank node
        let HT = replaceBlankNodes(R.head)
        foreach triple template TT in HT:
            let triple = subst(μ, TT)
            add triple to S
        endfor
        OUT = OUT ∪ S
    endfor
    return OUT
enddefine
```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> `OUT` may contain triples that are also in the base graph.

### 6.5 Evaluation of a Rule Set

Evaluation of a rule set is defined as the execution of each stratum of a stratification of the rule set, where each stratum is executed completely
and in order before moving on to the next stratum.
A stratum is evaluated by first evaluating
each of the run-once rules of that stratum, and then evaluating general rules of the stratum repeatedly until no new triples are produced.

```
let G0 be the input base graph
let RS be the rule set
let D be the graph of all DATA triples in RS

Apply stratification to RS

let LS be the sequence of layers after stratification

# Inference graph
let GI = { t ∈ D | t ∉ G0 }

# Evaluation graph: base graph and data blocks
let GE = G0 ∪ D

foreach stratum ST in LS:
    foreach rule R in ST.once:
        let X = evalRule(R, GE, G0)
        let Y = { t ∈ X | t ∉ GE }
        GI = GI ∪ Y
        GE = GE ∪ Y
    endfor

    let finished = false
    while ! finished:
        finished = true
        foreach rule R in ST.general:
            let X = evalRule(R, GE, G0)
            let Y = { t ∈ X | t ∉ GE }
            if Y is not empty:
                finished = false
                GI = GI ∪ Y
                GE = GE ∪ Y
            endif
        endfor
    endwhile
endfor
the result is GI
```

### 6.6 Worked Example

*This section is non-normative.*

This section steps through the evaluation of a complete rule set: determining the rule dependencies
(4.3 Rule Dependency (§4.3)),
calculating a stratification
(4.4 Stratification (§4.4)),
and evaluating each stratum in turn to produce the inference graph (6.5 Evaluation of a Rule Set (§6.5)).

The example describes software components and their dependencies:
a frontend depends on an application server, which depends on a
database and on a logging library. The database has a known
vulnerability. The rules propagate exposure to vulnerabilities
along the dependency chain, give components exposed to a severe
vulnerability the status `:criticallyExposed`, give components that are
not critical the status `:safeToDeploy`, and create a
notification for each critically exposed component.
(In practice, whether a vulnerability affects a component
depends on the deployed version; the example elides versions and
states the vulnerability directly.)
For brevity, the base graph states `:dependsOn` triples directly,
rather than deriving them from more specific relations as in 3.1 Triple Patterns (§3.1).
> **Example:**
>
> Example 13: Worked example: data and rules
>
> ```
> :frontend rdf:type :Component ;
>           :dependsOn :app .
> :app      rdf:type :Component ;
>           :dependsOn :db ;
>           :dependsOn :logger .
> :db       rdf:type :Component ;
>           :hasVulnerability :vuln1 .
> :logger   rdf:type :Component .
> :vuln1    :severity 9.1 .
> ```
>
> ```
> # R1
> RULE { ?x :exposedTo ?v } WHERE { ?x :hasVulnerability ?v }
>
> # R2
> RULE { ?x :exposedTo ?v } WHERE { ?x :dependsOn ?y . ?y :exposedTo ?v }
>
> # R3
> RULE { ?x :status :criticallyExposed }
> WHERE { ?x :exposedTo ?v . ?v :severity ?s . FILTER(?s >= 9.0) }
>
> # R4
> RULE { ?x :status :safeToDeploy }
> WHERE { ?x rdf:type :Component . NOT { ?x :status :criticallyExposed } }
>
> # R5
> RULE { [] rdf:type :Notification ; :concerns ?x }
> WHERE { ?x :status :criticallyExposed }
> ```

The rules are labeled `R1` to `R5` in comments and are referred
to by these labels in the rest of this section.
They are the rules introduced in 3.2 Recursion (§3.2) through 3.5 Assignment and Creating RDF Terms (§3.5).
The rule set has no `IMPORTS`, so import processing
leaves it unchanged, and no `DATA` blocks, so evaluation starts
from the base graph alone.

#### 6.6.1 Determining the Dependencies

Each triple pattern in each rule body is compared with the
triple templates in every rule head, to determine which rules
depend on which
(4.3 Rule Dependency (§4.3)).

- The body of `R1` is the single triple pattern `?x :hasVulnerability ?v`. No rule head has a triple template
  that can generate a triple with predicate `:hasVulnerability`,
  so this pattern can only match the data. `R1` has no dependencies.
- The body of `R2` has two triple patterns. `?x :dependsOn ?y` cannot match any rule head, so it matches
  only the data. `?y :exposedTo ?v` matches the head template `?x :exposedTo ?v` of `R1`, and also matches the head of `R2` itself. Both occurrences are triple pattern elements (they do not occur inside a negation element, and `R2` is
  not a run-once rule), so `R2` has an *open* dependency on `R1` and an *open* dependency on itself.
  The dependency of `R2` on itself makes `R2` a recursive rule.
- In the body of `R3`, the pattern `?x :exposedTo ?v` matches
  the heads of `R1` and `R2`, giving `R3` an *open* dependency on each. The pattern `?v :severity ?s` matches no
  rule head.
- In the body of `R4`, the pattern `?x rdf:type :Component` matches no rule head: the only head template with predicate `rdf:type` is in `R5`, and its object `:Notification` is
  a different RDF term from `:Component`, so no generated
  triple can match.
  The pattern `?x :status :criticallyExposed` occurs inside the negation element `NOT { ?x :status :criticallyExposed }` and
  matches the head template of `R3`. Because the pattern
  occurs in a negation element, `R4` has a *closed* dependency on `R3`.
- In the body of `R5`, the pattern `?x :status :criticallyExposed` matches the head of `R3`. The head of `R5` contains a
  blank node, so its dependency on `R3` is a *closed* dependency, even though the pattern is an ordinary triple pattern element.
  No pattern in any rule body matches the head templates of `R5`, so no rule depends on `R5`.

The dependency graph therefore has five vertices and six
edges:

- `R2 → R1` (open)
- `R2 → R2` (open)
- `R3 → R1` (open)
- `R3 → R2` (open)
- `R4 → R3` (closed)
- `R5 → R3` (closed)

Although `R4` and `R5` have no direct dependency on `R1` or `R2`, each has a transitive dependency on both, through `R3`.

![Dependency graph of the worked example rule set Five vertices labeled R1, R2, R3, R4, and R5. Dashed arrows mark open dependencies: from R2 to R1, from R2 to itself, from R3 to R1, and from R3 to R2. Solid arrows mark closed dependencies: from R4 to R3 and from R5 to R3. R2 R1 R3 R4 R5 open dependency closed dependency](data:image/svg+xml;base64,PHN2ZyBhcmlhLWxhYmVsbGVkYnk9ImRlcGdyYXBoLXRpdGxlIGRlcGdyYXBoLWRlc2MiIHJvbGU9ImltZyIgc3R5bGU9Im1heC13aWR0aDogNDgwcHg7IGhlaWdodDogYXV0bzsiIHZpZXdCb3g9IjAgMCA0ODAgMzUwIiB3aWR0aD0iNDgwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8dGl0bGUgaWQ9ImRlcGdyYXBoLXRpdGxlIj5EZXBlbmRlbmN5IGdyYXBoIG9mIHRoZSB3b3JrZWQgZXhhbXBsZSBydWxlIHNldDwvdGl0bGU+CjxkZXNjIGlkPSJkZXBncmFwaC1kZXNjIj4KICAgICAgICAgICAgICAgIEZpdmUgdmVydGljZXMgbGFiZWxlZCBSMSwgUjIsIFIzLCBSNCwgYW5kIFI1LgogICAgICAgICAgICAgICAgRGFzaGVkIGFycm93cyBtYXJrIG9wZW4gZGVwZW5kZW5jaWVzOiBmcm9tIFIyIHRvIFIxLAogICAgICAgICAgICAgICAgZnJvbSBSMiB0byBpdHNlbGYsIGZyb20gUjMgdG8gUjEsIGFuZCBmcm9tIFIzIHRvIFIyLgogICAgICAgICAgICAgICAgU29saWQgYXJyb3dzIG1hcmsgY2xvc2VkIGRlcGVuZGVuY2llczogZnJvbSBSNCB0byBSMwogICAgICAgICAgICAgICAgYW5kIGZyb20gUjUgdG8gUjMuCiAgICAgICAgICAgICAgPC9kZXNjPgo8ZGVmcz4KPG1hcmtlciBpZD0iZGVwLWFycm93IiBtYXJrZXJIZWlnaHQ9IjciIG1hcmtlcldpZHRoPSI3IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSIgcmVmWD0iOSIgcmVmWT0iNSIgdmlld0JveD0iMCAwIDEwIDEwIj4KPHBhdGggZD0iTSAwIDAgTCAxMCA1IEwgMCAxMCB6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+CjwvbWFya2VyPgo8L2RlZnM+CjxnIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSI+CjxnIG1hcmtlci1lbmQ9InVybCgjZGVwLWFycm93KSIgc3Ryb2tlLWRhc2hhcnJheT0iNiA0Ij4KPGxpbmUgeDE9IjIyMy42IiB4Mj0iMTU2LjQiIHkxPSIxMzUuMyIgeTI9Ijc0LjciIC8+CjxsaW5lIHgxPSIyNTYuNCIgeDI9IjMyMy42IiB5MT0iMTM1LjMiIHkyPSI3NC43IiAvPgo8bGluZSB4MT0iMTYyIiB4Mj0iMzE2IiB5MT0iNjAiIHkyPSI2MCIgLz4KPHBhdGggZD0iTSAxMjQuNCA0NC40IEMgNjAgMTUsIDYwIDEwNSwgMTI0LjQgNzUuNiIgLz4KPC9nPgo8ZyBtYXJrZXItZW5kPSJ1cmwoI2RlcC1hcnJvdykiPgo8bGluZSB4MT0iMTU2LjQiIHgyPSIyMjMuNiIgeTE9IjIyNS4zIiB5Mj0iMTY0LjciIC8+CjxsaW5lIHgxPSIzMjMuNiIgeDI9IjI1Ni40IiB5MT0iMjI1LjMiIHkyPSIxNjQuNyIgLz4KPC9nPgo8Y2lyY2xlIGN4PSIxNDAiIGN5PSI2MCIgcj0iMjIiIC8+CjxjaXJjbGUgY3g9IjM0MCIgY3k9IjYwIiByPSIyMiIgLz4KPGNpcmNsZSBjeD0iMjQwIiBjeT0iMTUwIiByPSIyMiIgLz4KPGNpcmNsZSBjeD0iMTQwIiBjeT0iMjQwIiByPSIyMiIgLz4KPGNpcmNsZSBjeD0iMzQwIiBjeT0iMjQwIiByPSIyMiIgLz4KPC9nPgo8ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGZvbnQtc2l6ZT0iMTUiIGZvbnQtd2VpZ2h0PSJib2xkIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj4KPHRleHQgeD0iMTQwIiB5PSI2NSI+UjI8L3RleHQ+Cjx0ZXh0IHg9IjM0MCIgeT0iNjUiPlIxPC90ZXh0Pgo8dGV4dCB4PSIyNDAiIHk9IjE1NSI+UjM8L3RleHQ+Cjx0ZXh0IHg9IjE0MCIgeT0iMjQ1Ij5SNDwvdGV4dD4KPHRleHQgeD0iMzQwIiB5PSIyNDUiPlI1PC90ZXh0Pgo8L2c+CjxnIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSI+CjxsaW5lIHN0cm9rZS1kYXNoYXJyYXk9IjYgNCIgeDE9IjU1IiB4Mj0iMTA1IiB5MT0iMzI1IiB5Mj0iMzI1IiAvPgo8bGluZSB4MT0iMjQ1IiB4Mj0iMjk1IiB5MT0iMzI1IiB5Mj0iMzI1IiAvPgo8L2c+CjxnIGZpbGw9ImN1cnJlbnRDb2xvciIgZm9udC1zaXplPSIxNCI+Cjx0ZXh0IHg9IjExMyIgeT0iMzMwIj5vcGVuIGRlcGVuZGVuY3k8L3RleHQ+Cjx0ZXh0IHg9IjMwMyIgeT0iMzMwIj5jbG9zZWQgZGVwZW5kZW5jeTwvdGV4dD4KPC9nPgo8L3N2Zz4=)

*Figure 1 The dependency graph of the worked example rule set.
Open dependencies are drawn as dashed arrows and closed
dependencies as solid arrows. Each edge points from the
rule whose body contains the matching triple pattern to the
rule whose head could generate the matching triples.*

The only cycle in the graph is the self-edge `R2 → R2`,
which is an open dependency. No cycle involves a closed
dependency, so the stratification condition is satisfied
and the rule set has a well-defined outcome.

#### 6.6.2 Calculating the Stratification

Following the §4.4.2 Stratification Algorithm,
every rule starts in stratum 0. The edges are then inspected
repeatedly until nothing changes:

- An *open* edge requires the source rule to be in the
  same stratum as its target or higher. All four open edges
  already satisfy this with every rule at stratum 0, so they
  cause no changes.
- A *closed* edge requires the source rule to be in a
  strictly higher stratum than its target, because the target
  must run to completion first. The edge `R4 → R3` (closed) finds `R4` and `R3` both at stratum 0, so `R4` is
  moved to stratum 1. Likewise the edge `R5 → R3` (closed) moves `R5` to stratum 1.

A further pass over the edges makes no changes, so the strata
are final. Each stratum is then partitioned into run-once rules and general rules. `R5` has a blank
node in its head, so it is a run-once rule; no other rule
of the rule set is a run-once rule.
The stratification is:

- Stratum 0: general `R1`, `R2`, `R3`; no run-once rules
- Stratum 1: run-once `R5`; general `R4`

This ordering captures the intent of the rules in the higher
stratum. Whether a component is safe to deploy, and which
components need a notification, can only be decided after *all* `:status :criticallyExposed` triples have been derived
— and the rule that derives them, `R3`, completes in the
stratum below, together with the rules `R1` and `R2` that
feed it.

#### 6.6.3 Evaluating the Strata

Evaluation follows the algorithm of 6.5 Evaluation of a Rule Set (§6.5).
The evaluation graph `GE` starts as the base graph and the
inference graph `GI` starts empty. Each stratum is evaluated to
completion in order: the rules of the stratum are evaluated in
passes, and passes repeat until a pass produces no new triples.
The algorithm does not fix the order in which the rules of a
stratum are evaluated within a pass; this trace uses the order `R1`, `R2`, `R3`. A different order can spread the same
inferences across a different number of passes but, because
stratum 0 runs to completion, it produces the same final graph.

Because this rule set has no `DATA` blocks, `GE` is `G0` plus `GI` at every point in the evaluation. The trace therefore
tracks only `GI`, showing its state as evaluation proceeds and
marking each new triple with the rule that produced it.

**Stratum 0, first pass.**

- `R1`: the body matches `:db :hasVulnerability :vuln1`, binding `?x = :db` and `?v = :vuln1`.
  The head produces `:db :exposedTo :vuln1`.
  The triple is not in `GE`, so it is added to `GE` and `GI`.
- `R2`: the body joins `?x :dependsOn ?y` with `?y :exposedTo ?v`. `GE` now contains `:db :exposedTo :vuln1`, so the join yields one solution: `?x = :app`, `?y = :db`, and `?v = :vuln1` (from `:app :dependsOn :db`).
  The head produces `:app :exposedTo :vuln1`, which is new and
  is added. There is no solution for `:frontend` yet, because `:app :exposedTo :vuln1` was not in `GE` when this
  evaluation of `R2` started.
- `R3`: `?x :exposedTo ?v` now matches for `:db` and `:app`;
  joining with `:vuln1 :severity 9.1` and applying `FILTER(?s >= 9.0)` keeps both solutions.
  The head produces `:db :status :criticallyExposed` and `:app :status :criticallyExposed`, both new.

```
# GI after stratum 0, first pass
:db  :exposedTo :vuln1 .                    # new (R1)
:app :exposedTo :vuln1 .                    # new (R2)
:db  :status :criticallyExposed .           # new (R3)
:app :status :criticallyExposed .           # new (R3)
```

New triples were produced, so evaluation of stratum 0
continues with another pass.

**Stratum 0, second pass.**

- `R1`: matches as before; `:db :exposedTo :vuln1` is already
  in `GE`, so nothing new is produced.
- `R2`: the join now also yields `?x = :frontend`, `?y = :app`, and `?v = :vuln1`, producing
  the new triple `:frontend :exposedTo :vuln1`.
  The exposure has taken two passes to travel two steps along
  the dependency chain.
- `R3`: produces the new triple `:frontend :status :criticallyExposed`.

```
# GI after stratum 0, second pass
:db       :exposedTo :vuln1 .
:app      :exposedTo :vuln1 .
:frontend :exposedTo :vuln1 .               # new (R2)
:db       :status :criticallyExposed .
:app      :status :criticallyExposed .
:frontend :status :criticallyExposed .      # new (R3)
```

**Stratum 0, third pass.** Every solution of every rule now produces only triples already
in `GE`. `GI` is unchanged.
No new triples means stratum 0 is complete: every `:exposedTo` triple and every `:status :criticallyExposed` triple that
can ever be derived has been derived.

**Stratum 1, run-once rules.** The run-once rules of the stratum are evaluated first,
each exactly once.

- `R5`: the body matches the three `:status :criticallyExposed` triples, giving the solutions `?x = :db`, `?x = :app`, and `?x = :frontend`. For each solution, instantiating the head
  creates a *fresh* blank node, producing two triples
  per solution which are notifications for each critical
  component. `R5` is not evaluated again, even though the
  general rules of the stratum will now be evaluated
  repeatedly.

**Stratum 1, first pass of the general rules.**

- `R4`: the pattern `?x rdf:type :Component` matches `:frontend`, `:app`, `:db`, and `:logger`.
  (It does not match the `rdf:type :Notification` triples
  just created by `R5`.)
  The negation element `NOT { ?x :status :criticallyExposed }` rejects
  the solutions for `:frontend`, `:app`, and `:db`, because `GE` contains a `:status :criticallyExposed` triple for each of them.
  Only the solution `?x = :logger` survives, producing the new
  triple `:logger :status :safeToDeploy`.

```
# GI after stratum 1
:db       :exposedTo :vuln1 .
:app      :exposedTo :vuln1 .
:frontend :exposedTo :vuln1 .
:db       :status :criticallyExposed .
:app      :status :criticallyExposed .
:frontend :status :criticallyExposed .
_:n1      rdf:type :Notification .          # new (R5)
_:n1      :concerns :db .                   # new (R5)
_:n2      rdf:type :Notification .          # new (R5)
_:n2      :concerns :app .                  # new (R5)
_:n3      rdf:type :Notification .          # new (R5)
_:n3      :concerns :frontend .             # new (R5)
:logger   :status :safeToDeploy .           # new (R4)
```

**Stratum 1, second pass of the general rules.** No new triples. Evaluation is complete, and `GI` as shown
above is the resulting inference graph.

The stratification is what makes this outcome reliable.
Evaluated during the first pass of stratum 0, before `:frontend :status :criticallyExposed` was derived, `R4` would have
incorrectly concluded `:frontend :status :safeToDeploy`, and `R5` would have created notifications for `:db` and `:app` but none for `:frontend`.
Deferring both to stratum 1 means they see the complete set of `:status :criticallyExposed` triples, so the order in which
rules are evaluated within each stratum does not affect the
final outcome.

## 7. SPARQL-RL Grammar

A *SPARQL-RL document* is an [RDF string](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-string), encoded in UTF-8 [RFC3629],
and that conforms to the grammar and
additional constraints defined in 7.6 Grammar (§7.6). Only [Unicode scalar values](https://www.w3.org/TR/i18n-glossary/#dfn-scalar-value),
in the ranges `U+0000` to `U+D7FF` and `U+E000` to `U+10FFFF`,
are allowed.
This excludes [surrogate code points](https://www.w3.org/TR/i18n-glossary/#dfn-surrogate),
the range `U+D800` to `U+DFFF`.

### 7.1 Version Announcement

A *version label* is a string that identifies the syntax and semantics
conformance for SPARQL-RL.

*Version Labels*

| Version Label |
| ------------- |
| "1.2"         |

The version announcement is a hint. It should be made early in the
document and before any feature depending on that version.

Multiple `VERSION` directives
can appear in a SPARQL-RL document.
Each directive applies to the part of the document following the directive,
until another directive is encountered or the end of the document is reached.

Version labels can also be given by the `version` parameter of the Media Type (§C). In the absence of a current `VERSION` directive, the
version specified as part of the Media Type is considered.

### 7.2 White Space

White space
(production `WS`) is used
to separate two terminals that would otherwise be incorrectly
recognized as one terminal.
Rule names in capitals below indicate where white space is
significant; these form a possible choice of terminals for constructing a
SPARQL-RL parser.

White space is significant in the production `String`.

### 7.3 Comments

Comments start with a `#` outside an `IRIREF`, `STRING_LITERAL1`, `STRING_LITERAL2`, `STRING_LITERAL_LONG1`, or `STRING_LITERAL_LONG2`,
and continue to the end of line (marked by `LF`, or `CR`),
or end of file if there is no end of line after the comment marker.
Comments are treated as white space.

### 7.4 IRI References

[Relative IRI references](https://www.w3.org/TR/rdf12-concepts/#dfn-relative-iri) are resolved with base IRIs
as per [Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/info/rfc3986/) [RFC3986] using only the basic algorithm in section 5.2.
Neither Syntax-Based Normalization nor Scheme-Based Normalization
(described in sections 6.2.2 and 6.2.3 of RFC3986) is performed.
Characters additionally allowed in IRI references are treated in the same way that
unreserved characters are treated in URI references, per section 6.5 of [Internationalized Resource Identifiers (IRIs)](https://www.rfc-editor.org/info/rfc3987/) [RFC3987].

The `BASE` directive defines the Base IRI used to resolve [relative IRI references](https://www.w3.org/TR/rdf12-concepts/#dfn-relative-iri) per [RFC3986] [section 5.1.1, "Base URI Embedded in Content"](https://www.rfc-editor.org/info/rfc3986/#section-5.1.1). [section 5.1.2, "Base URI from the Encapsulating Entity"](https://www.rfc-editor.org/info/rfc3986/#section-5.1.2) defines how the In-Scope Base IRI may come from an encapsulating document,
such as a SOAP envelope with an `xml:base` directive or a MIME multipart document with a `Content-Location` header.
The "Retrieval URI" identified in [5.1.3, Base "URI from the Retrieval URI"](https://www.rfc-editor.org/info/rfc3986/#section-5.1.3),
is the URL from which a particular SPARQL-RL document was retrieved.
If none of the above specifies the Base URI, the default
Base URI ([section 5.1.4, "Default Base URI"](https://www.rfc-editor.org/info/rfc3986/#section-5.1.4)) is used.
Each `BASE` directive sets a new In-Scope Base URI,
relative to the previous one.

### 7.5 Escape Sequences

There are three forms of escapes used in SPARQL-RL documents:

- A *numeric escape sequence* represents the value of
  a [Unicode code point](https://www.w3.org/TR/i18n-glossary/#dfn-code-point).

  A numeric escape sequence *MUST NOT* produce a code point value
  in the range `U+D800` to `U+DFFF`,
  which is the range for
  Unicode [surrogates](https://www.w3.org/TR/i18n-glossary/#dfn-surrogate).

    | Escape sequence                                                                                                                                                                                          | Unicode code point                                                                                                                                                                                       |
    | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `\u` `hex` `hex` `hex` `hex` | A [Unicode code point](https://www.w3.org/TR/i18n-glossary/#dfn-code-point) in the ranges `U+0000` to `U+D7FF` and `U+E000` to `U+FFFF`, corresponding to the value encoded by the four hexadecimal digits interpreted from most significant to least significant digit. |
    | `\U` `hex` `hex` `hex` `hex` `hex` `hex` `hex` `hex` | A [Unicode code point](https://www.w3.org/TR/i18n-glossary/#dfn-code-point) in the ranges `U+0000` to `U+D7FF` and `U+E000` to `U+10FFFF`, corresponding to the value encoded by the eight hexadecimal digits interpreted from most significant to least significant digit. |

  where `hex` is a hexadecimal character

  `HEX ::= [0-9] | [A-F] | [a-f]`

- A *string escape sequence* represents a character traditionally escaped in string literals:

    | Escape sequence | Unicode code point |
    | --------------- | ------------------ |
    | `\t`            | `U+0009`           |
    | `\b`            | `U+0008`           |
    | `\n`            | `U+000A`           |
    | `\r`            | `U+000D`           |
    | `\f`            | `U+000C`           |
    | `\"`            | `U+0022`           |
    | `\'`            | `U+0027`           |
    | `\\`            | `U+005C`           |

- A *reserved character escape sequence* consists of a `\` followed by
  one of these characters `~.-!$&'()*+,;=/?#@%_`, and
  represents the character to the right of
  the `\`.

*Context where each kind of escape sequence can be used*

|                                                                                                                                                                                                          | numeric escapes | string escapes | reserved character escapes |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| IRIs, used as [RDF terms](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term), `PREFIX`, or `BASE` declarations | yes                                                                               | no                                                                              | no                                                                                                      |
| local names                                                                                                                                              | no                                                                                | no                                                                              | yes                                                                                                     |
| Strings                                                                                                                                                                                                  | yes                                                                               | yes                                                                             | no                                                                                                      |

> **Note:**
>
> > **Note:**
> >
> > Note
>
> %-encoded sequences are in the character range for IRIs and are explicitly allowed in local names.
> These appear as a `%` followed by two hex characters and represent that
> same sequence of three characters. These sequences are *not* decoded during processing.
> A term written as `<http://a.example/%66oo-bar>` designates the IRI `http://a.example/%66oo-bar` and not IRI `http://a.example/foo-bar`.
> A term written as `ex:%66oo-bar` with a prefix `PREFIX ex: <http://a.example/>` also designates the IRI `http://a.example/%66oo-bar`.

### 7.6 Grammar

The EBNF used here is defined in XML 1.0
[EBNF-NOTATION].

Notes:

1. The entry point of the grammar is `RuleSet`.
2. Keywords are case-insensitive except for
   '`a`',
   which is case-sensitive.
3. Escape sequences `UCHAR` and `ECHAR` are case-sensitive.
4. Variables are not allowed in a `DATA` block.
5. When tokenizing the input and choosing grammar rules, the longest match is chosen.
6. The SPARQL-RL grammar is LL(1) and LALR(1) when the rules with uppercased names are
   used as terminals.

| `[1]`   | `RuleSet`                       | ::= | `RuleOrDataBlock`                                                                                                                                                                                        |
| ------- | ------------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[2]`   | `RuleOrDataBlock`               | ::= | `Prologue ( RuleOrData+ ( Prologue1 RuleOrData* )* )?`                                                                                                                                                   |
| `[3]`   | `RuleOrData`                    | ::= | `Rule \| Data`                                                                                                                                                                                           |
| `[4]`   | `Prologue`                      | ::= | `Prologue1*`                                                                                                                                                                                             |
| `[5]`   | `Prologue1`                     | ::= | `BaseDecl \| PrefixDecl \| VersionDecl \| ImportsDecl`                                                                                                                                                   |
| `[6]`   | `BaseDecl`                      | ::= | `'BASE' IRIREF`                                                                                                                                                                                          |
| `[7]`   | `PrefixDecl`                    | ::= | `'PREFIX' PNAME_NS IRIREF`                                                                                                                                                                               |
| `[8]`   | `VersionDecl`                   | ::= | `'VERSION' VersionSpecifier`                                                                                                                                                                             |
| `[9]`   | `VersionSpecifier`              | ::= | `STRING_LITERAL1 \| STRING_LITERAL2`                                                                                                                                                                     |
| `[10]`  | `ImportsDecl`                   | ::= | `'IMPORTS' iri`                                                                                                                                                                                          |
| `[11]`  | `Rule`                          | ::= | `'RULE' iri? HeadTemplate 'WHERE' 'DATA'? BodyPattern`                                                                                                                                                   |
| `[12]`  | `Data`                          | ::= | `'DATA' '{' DataTriplesBlock? '}'`                                                                                                                                                                       |
| `[13]`  | `HeadTemplate`                  | ::= | `'{' HeadTemplateBlock? '}'`                                                                                                                                                                             |
| `[14]`  | `BodyPattern`                   | ::= | `'{' BodyTriplesBlock? ( BodyNotTriples '.'? BodyTriplesBlock? )* '}'`                                                                                                                                   |
| `[15]`  | `BodyNotTriples`                | ::= | `Filter \| Negation \| Assignment \| GroupAggregate`                                                                                                                                                     |
| `[16]`  | `Filter`                        | ::= | `'FILTER' Constraint`                                                                                                                                                                                    |
| `[17]`  | `Constraint`                    | ::= | `BrackettedExpression \| BuiltInCall \| FunctionCall`                                                                                                                                                    |
| `[18]`  | `Negation`                      | ::= | `'NOT' 'DATA'? '{' NegationPattern '}'`                                                                                                                                                                  |
| `[19]`  | `NegationPattern`               | ::= | `BodyTriplesBlock? ( NegationPatternNotTriples '.'? BodyTriplesBlock? )*`                                                                                                                                |
| `[20]`  | `NegationPatternNotTriples`     | ::= | `Filter`                                                                                                                                                                                                 |
| `[21]`  | `Assignment`                    | ::= | `'SET' '(' Var ':=' Expression ')'`                                                                                                                                                                      |
| `[22]`  | `GroupAggregate`                | ::= | `'GROUP' ( 'BY' ListVars )? '{' GroupPattern '}' ( ANON \| '[' AggregationAssignment+ ']' )`                                                                                                             |
| `[23]`  | `GroupPattern`                  | ::= | `BodyTriplesBlock? ( GroupPatternNotTriples '.'? BodyTriplesBlock? )*`                                                                                                                                   |
| `[24]`  | `GroupPatternNotTriples`        | ::= | `Filter \| Assignment`                                                                                                                                                                                   |
| `[25]`  | `ListVars`                      | ::= | `Var+`                                                                                                                                                                                                   |
| `[26]`  | `AggregationAssignment`         | ::= | `Var ':=' AggregationFunction`                                                                                                                                                                           |
| `[27]`  | `AggregationFunction`           | ::= | `( 'COUNT' '(' DISTINCT? VarOrStar ')' \| 'MIN' '(' Var ')' \| 'MAX' '(' Var ')' \| 'SUM' '(' Var ')' )`                                                                                                 |
| `[28]`  | `VarOrStar`                     | ::= | `Var \| '*'`                                                                                                                                                                                             |
| `[29]`  | `DataTriplesBlock`              | ::= | `TriplesSameSubjectData ( '.' DataTriplesBlock? )?`                                                                                                                                                      |
| `[30]`  | `TriplesSameSubjectData`        | ::= | `RDFTermData PropertyListNotEmptyData \| TriplesNodeData PropertyListData \| ReifiedTripleBlockData`                                                                                                     |
| `[31]`  | `PropertyListData`              | ::= | `PropertyListNotEmptyData?`                                                                                                                                                                              |
| `[32]`  | `PropertyListNotEmptyData`      | ::= | `VerbData ObjectListData ( ';' ( VerbData ObjectListData )? )*`                                                                                                                                          |
| `[33]`  | `VerbData`                      | ::= | `iri \| 'a'`                                                                                                                                                                                             |
| `[34]`  | `ObjectListData`                | ::= | `ObjectData ( ',' ObjectData )*`                                                                                                                                                                         |
| `[35]`  | `ObjectData`                    | ::= | `GraphNodeData AnnotationData`                                                                                                                                                                           |
| `[36]`  | `GraphNodeData`                 | ::= | `RDFTermData \| TriplesNodeData \| ReifiedTripleData`                                                                                                                                                    |
| `[37]`  | `TriplesNodeData`               | ::= | `CollectionData \| BlankNodePropertyListData`                                                                                                                                                            |
| `[38]`  | `BlankNodePropertyListData`     | ::= | `'[' PropertyListNotEmptyData ']'`                                                                                                                                                                       |
| `[39]`  | `CollectionData`                | ::= | `'(' GraphNodeData+ ')'`                                                                                                                                                                                 |
| `[40]`  | `AnnotationData`                | ::= | `( ReifierData \| AnnotationBlockData )*`                                                                                                                                                                |
| `[41]`  | `AnnotationBlockData`           | ::= | `'{\|' PropertyListNotEmptyData '\|}'`                                                                                                                                                                   |
| `[42]`  | `ReifierData`                   | ::= | `'~' ReifierIdData?`                                                                                                                                                                                     |
| `[43]`  | `ReifierIdData`                 | ::= | `iri \| BlankNode`                                                                                                                                                                                       |
| `[44]`  | `ReifiedTripleBlockData`        | ::= | `ReifiedTripleData PropertyListData`                                                                                                                                                                     |
| `[45]`  | `ReifiedTripleData`             | ::= | `'<<' ReifiedTripleSubjectData VerbData ReifiedTripleObjectData ReifierData? '>>'`                                                                                                                       |
| `[46]`  | `ReifiedTripleSubjectData`      | ::= | `iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| ReifiedTripleData \| TripleTermData`                                                                                              |
| `[47]`  | `ReifiedTripleObjectData`       | ::= | `iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| ReifiedTripleData \| TripleTermData`                                                                                              |
| `[48]`  | `TripleTermData`                | ::= | `'<<(' TripleTermSubjectData VerbData TripleTermObjectData ')>>'`                                                                                                                                        |
| `[49]`  | `TripleTermSubjectData`         | ::= | `iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| TripleTermData`                                                                                                                   |
| `[50]`  | `TripleTermObjectData`          | ::= | `iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| TripleTermData`                                                                                                                   |
| `[51]`  | `HeadTemplateBlock`             | ::= | `TriplesBlockTemplate`                                                                                                                                                                                   |
| `[52]`  | `TriplesBlockTemplate`          | ::= | `TriplesSameSubjectTemplate ( '.' TriplesBlockTemplate? )?`                                                                                                                                              |
| `[53]`  | `TriplesSameSubjectTemplate`    | ::= | `VarOrRDFTerm PropertyListNotEmptyTemplate \| TriplesNodeTemplate PropertyListTemplate \| ReifiedTripleBlockTemplate`                                                                                    |
| `[54]`  | `PropertyListTemplate`          | ::= | `PropertyListNotEmptyTemplate?`                                                                                                                                                                          |
| `[55]`  | `PropertyListNotEmptyTemplate`  | ::= | `Verb ObjectListTemplate ( ';' ( Verb ObjectListTemplate )? )*`                                                                                                                                          |
| `[56]`  | `ObjectListTemplate`            | ::= | `ObjectTemplate ( ',' ObjectTemplate )*`                                                                                                                                                                 |
| `[57]`  | `ObjectTemplate`                | ::= | `GraphNodeTemplate AnnotationTemplate`                                                                                                                                                                   |
| `[58]`  | `GraphNodeTemplate`             | ::= | `VarOrRDFTerm \| TriplesNodeTemplate \| ReifiedTriple`                                                                                                                                                   |
| `[59]`  | `TriplesNodeTemplate`           | ::= | `CollectionTemplate \| BlankNodePropertyListTemplate`                                                                                                                                                    |
| `[60]`  | `BlankNodePropertyListTemplate` | ::= | `'[' PropertyListNotEmptyTemplate ']'`                                                                                                                                                                   |
| `[61]`  | `CollectionTemplate`            | ::= | `'(' GraphNodeTemplate+ ')'`                                                                                                                                                                             |
| `[62]`  | `AnnotationTemplate`            | ::= | `( Reifier \| AnnotationBlockTemplate )*`                                                                                                                                                                |
| `[63]`  | `AnnotationBlockTemplate`       | ::= | `'{\|' PropertyListNotEmptyTemplate '\|}'`                                                                                                                                                               |
| `[64]`  | `ReifiedTripleBlockTemplate`    | ::= | `ReifiedTriple PropertyListTemplate`                                                                                                                                                                     |
| `[65]`  | `BodyTriplesBlock`              | ::= | `TriplesBlockPattern`                                                                                                                                                                                    |
| `[66]`  | `TriplesBlockPattern`           | ::= | `TriplesSameSubjectPattern ( '.' TriplesBlockPattern? )?`                                                                                                                                                |
| `[67]`  | `ReifiedTripleBlockPattern`     | ::= | `ReifiedTriple PropertyListPattern`                                                                                                                                                                      |
| `[68]`  | `TriplesSameSubjectPattern`     | ::= | `VarOrRDFTerm PropertyListNotEmptyPattern \| TriplesNodePattern PropertyListPattern \| ReifiedTripleBlockPattern`                                                                                        |
| `[69]`  | `PropertyListPattern`           | ::= | `PropertyListNotEmptyPattern?`                                                                                                                                                                           |
| `[70]`  | `PropertyListNotEmptyPattern`   | ::= | `( VerbPath \| Var ) ObjectListPattern ( ';' ( ( VerbPath \| Var ) ObjectListPattern )? )*`                                                                                                              |
| `[71]`  | `ObjectListPattern`             | ::= | `ObjectPattern ( ',' ObjectPattern )*`                                                                                                                                                                   |
| `[72]`  | `ObjectPattern`                 | ::= | `GraphNodePattern AnnotationPattern`                                                                                                                                                                     |
| `[73]`  | `TriplesNodePattern`            | ::= | `CollectionPattern \| BlankNodePropertyListPattern`                                                                                                                                                      |
| `[74]`  | `BlankNodePropertyListPattern`  | ::= | `'[' PropertyListNotEmptyPattern ']'`                                                                                                                                                                    |
| `[75]`  | `CollectionPattern`             | ::= | `'(' GraphNodePattern+ ')'`                                                                                                                                                                              |
| `[76]`  | `AnnotationPattern`             | ::= | `( Reifier \| AnnotationBlockPattern )*`                                                                                                                                                                 |
| `[77]`  | `AnnotationBlockPattern`        | ::= | `'{\|' PropertyListNotEmptyPattern '\|}'`                                                                                                                                                                |
| `[78]`  | `GraphNodePattern`              | ::= | `VarOrRDFTerm \| TriplesNodePattern \| ReifiedTriple`                                                                                                                                                    |
| `[79]`  | `Reifier`                       | ::= | `'~' ReifierId?`                                                                                                                                                                                         |
| `[80]`  | `ReifierId`                     | ::= | `Var \| iri \| BlankNode`                                                                                                                                                                                |
| `[81]`  | `ReifiedTriple`                 | ::= | `'<<' ReifiedTripleSubject Verb ReifiedTripleObject Reifier? '>>'`                                                                                                                                       |
| `[82]`  | `ReifiedTripleSubject`          | ::= | `Var \| iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| ReifiedTriple \| TripleTerm`                                                                                               |
| `[83]`  | `ReifiedTripleObject`           | ::= | `Var \| iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| ReifiedTriple \| TripleTerm`                                                                                               |
| `[84]`  | `TripleTerm`                    | ::= | `'<<(' TripleTermSubject Verb TripleTermObject ')>>'`                                                                                                                                                    |
| `[85]`  | `TripleTermSubject`             | ::= | `Var \| iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| TripleTerm`                                                                                                                |
| `[86]`  | `TripleTermObject`              | ::= | `Var \| iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| TripleTerm`                                                                                                                |
| `[87]`  | `Verb`                          | ::= | `VarOrIri \| 'a'`                                                                                                                                                                                        |
| `[88]`  | `VerbPath`                      | ::= | `Path`                                                                                                                                                                                                   |
| `[89]`  | `Path`                          | ::= | `PathSequence`                                                                                                                                                                                           |
| `[90]`  | `PathSequence`                  | ::= | `PathEltOrInverse ( '/' PathEltOrInverse )*`                                                                                                                                                             |
| `[91]`  | `PathEltOrInverse`              | ::= | `PathElt \| '^' PathElt`                                                                                                                                                                                 |
| `[92]`  | `PathElt`                       | ::= | `( iri \| 'a' \| '(' Path ')' )`                                                                                                                                                                         |
| `[93]`  | `RDFTermData`                   | ::= | `iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| NIL \| TripleTermData`                                                                                                            |
| `[94]`  | `VarOrRDFTerm`                  | ::= | `Var \| iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| BlankNode \| NIL \| TripleTerm`                                                                                                         |
| `[95]`  | `VarOrIri`                      | ::= | `Var \| iri`                                                                                                                                                                                             |
| `[96]`  | `Var`                           | ::= | `VAR1 \| VAR2`                                                                                                                                                                                           |
| `[97]`  | `RDFLiteral`                    | ::= | `String ( LANG_DIR \| '^^' iri )?`                                                                                                                                                                       |
| `[98]`  | `NumericLiteral`                | ::= | `NumericLiteralUnsigned \| NumericLiteralPositive \| NumericLiteralNegative`                                                                                                                             |
| `[99]`  | `NumericLiteralUnsigned`        | ::= | `INTEGER \| DECIMAL \| DOUBLE`                                                                                                                                                                           |
| `[100]` | `NumericLiteralPositive`        | ::= | `INTEGER_POSITIVE \| DECIMAL_POSITIVE \| DOUBLE_POSITIVE`                                                                                                                                                |
| `[101]` | `NumericLiteralNegative`        | ::= | `INTEGER_NEGATIVE \| DECIMAL_NEGATIVE \| DOUBLE_NEGATIVE`                                                                                                                                                |
| `[102]` | `BooleanLiteral`                | ::= | `'true' \| 'false'`                                                                                                                                                                                      |
| `[103]` | `String`                        | ::= | `STRING_LITERAL1 \| STRING_LITERAL2 \| STRING_LITERAL_LONG1 \| STRING_LITERAL_LONG2`                                                                                                                     |
| `[104]` | `iri`                           | ::= | `IRIREF \| PrefixedName`                                                                                                                                                                                 |
| `[105]` | `PrefixedName`                  | ::= | `PNAME_LN \| PNAME_NS`                                                                                                                                                                                   |
| `[106]` | `BlankNode`                     | ::= | `BLANK_NODE_LABEL \| ANON`                                                                                                                                                                               |
| `[107]` | `Expression`                    | ::= | `ConditionalOrExpression`                                                                                                                                                                                |
| `[108]` | `ConditionalOrExpression`       | ::= | `ConditionalAndExpression ( '\|\|' ConditionalAndExpression )*`                                                                                                                                          |
| `[109]` | `ConditionalAndExpression`      | ::= | `ValueLogical ( '&&' ValueLogical )*`                                                                                                                                                                    |
| `[110]` | `ValueLogical`                  | ::= | `RelationalExpression`                                                                                                                                                                                   |
| `[111]` | `RelationalExpression`          | ::= | `NumericExpression ( '=' NumericExpression \| '!=' NumericExpression \| '<' NumericExpression \| '>' NumericExpression \| '<=' NumericExpression \| '>=' NumericExpression \| 'IN' ExpressionList \| 'NOT' 'IN' ExpressionList )?` |
| `[112]` | `NumericExpression`             | ::= | `AdditiveExpression`                                                                                                                                                                                     |
| `[113]` | `AdditiveExpression`            | ::= | `MultiplicativeExpression ( '+' MultiplicativeExpression \| '-' MultiplicativeExpression \| ( NumericLiteralPositive \| NumericLiteralNegative ) ( ( '*' UnaryExpression ) \| ( '/' UnaryExpression ) )* )*` |
| `[114]` | `MultiplicativeExpression`      | ::= | `UnaryExpression ( '*' UnaryExpression \| '/' UnaryExpression )*`                                                                                                                                        |
| `[115]` | `UnaryExpression`               | ::= | `'!' PrimaryExpression \| '+' PrimaryExpression \| '-' PrimaryExpression \| PrimaryExpression`                                                                                                           |
| `[116]` | `PrimaryExpression`             | ::= | `BrackettedExpression \| BuiltInCall \| iriOrFunction \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| Var \| ExprTripleTerm`                                                                        |
| `[117]` | `FunctionCall`                  | ::= | `iri ArgList`                                                                                                                                                                                            |
| `[118]` | `ArgList`                       | ::= | `NIL \| '(' Expression ( ',' Expression )* ')' `                                                                                                                                                         |
| `[119]` | `ExpressionList`                | ::= | `NIL \| '(' Expression ( ',' Expression )* ')' `                                                                                                                                                         |
| `[120]` | `iriOrFunction`                 | ::= | `iri ArgList?`                                                                                                                                                                                           |
| `[121]` | `ExprTripleTerm`                | ::= | `'<<(' ExprTripleTermSubject Verb ExprTripleTermObject ')>>'`                                                                                                                                            |
| `[122]` | `ExprTripleTermSubject`         | ::= | `iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| Var`                                                                                                                                           |
| `[123]` | `ExprTripleTermObject`          | ::= | `iri \| RDFLiteral \| NumericLiteral \| BooleanLiteral \| Var \| ExprTripleTerm`                                                                                                                         |
| `[124]` | `BrackettedExpression`          | ::= | `'(' Expression ')'`                                                                                                                                                                                     |
| `[125]` | `BuiltInCall`                   | ::= | `'STR' '(' Expression ')' \| 'LANG' '(' Expression ')' \| 'LANGMATCHES' '(' Expression ',' Expression ')' \| 'LANGDIR' '(' Expression ')' \| 'DATATYPE' '(' Expression ')' \| 'IRI' '(' Expression ')' \| 'URI' '(' Expression ')' \| 'BNODE' ( '(' Expression ')' \| NIL ) \| 'ABS' '(' Expression ')' \| 'CEIL' '(' Expression ')' \| 'FLOOR' '(' Expression ')' \| 'ROUND' '(' Expression ')' \| 'CONCAT' ExpressionList \| 'SUBSTR' '(' Expression ',' Expression ( ',' Expression )? ')' \| 'STRLEN' '(' Expression ')' \| 'REPLACE' '(' Expression ',' Expression ',' Expression ( ',' Expression )? ')' \| 'UCASE' '(' Expression ')' \| 'LCASE' '(' Expression ')' \| 'ENCODE_FOR_URI' '(' Expression ')' \| 'CONTAINS' '(' Expression ',' Expression ')' \| 'STRSTARTS' '(' Expression ',' Expression ')' \| 'STRENDS' '(' Expression ',' Expression ')' \| 'STRBEFORE' '(' Expression ',' Expression ')' \| 'STRAFTER' '(' Expression ',' Expression ')' \| 'YEAR' '(' Expression ')' \| 'MONTH' '(' Expression ')' \| 'DAY' '(' Expression ')' \| 'HOURS' '(' Expression ')' \| 'MINUTES' '(' Expression ')' \| 'SECONDS' '(' Expression ')' \| 'TIMEZONE' '(' Expression ')' \| 'TZ' '(' Expression ')' \| 'NOW' NIL \| 'UUID' NIL \| 'STRUUID' NIL \| 'IF' '(' Expression ',' Expression ',' Expression ')' \| 'STRLANG' '(' Expression ',' Expression ')' \| 'STRLANGDIR' '(' Expression ',' Expression ',' Expression ')' \| 'STRDT' '(' Expression ',' Expression ')' \| 'sameTerm' '(' Expression ',' Expression ')' \| 'isIRI' '(' Expression ')' \| 'isURI' '(' Expression ')' \| 'isBLANK' '(' Expression ')' \| 'isLITERAL' '(' Expression ')' \| 'isNUMERIC' '(' Expression ')' \| 'hasLANG' '(' Expression ')' \| 'hasLANGDIR' '(' Expression ')' \| 'REGEX' '(' Expression ',' Expression ( ',' Expression )? ')' \| 'isTRIPLE' '(' Expression ')' \| 'TRIPLE' '(' Expression ',' Expression ',' Expression ')' \| 'SUBJECT' '(' Expression ')' \| 'PREDICATE' '(' Expression ')' \| 'OBJECT' '(' Expression ')'` |

Productions for terminals:

| `[126]` | `IRIREF`               | ::= | ``'<' ([^<>"{}\|^`\]-[#x00-#x20] \| UCHAR )* '>'``                                                                                                                                                       |
| ------- | ---------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[127]` | `PNAME_NS`             | ::= | `PN_PREFIX? ':'`                                                                                                                                                                                         |
| `[128]` | `PNAME_LN`             | ::= | `PNAME_NS PN_LOCAL`                                                                                                                                                                                      |
| `[129]` | `BLANK_NODE_LABEL`     | ::= | `'_:' ( PN_CHARS_U \| [0-9] ) ((PN_CHARS\|'.')* PN_CHARS)?`                                                                                                                                              |
| `[130]` | `VAR1`                 | ::= | `'?' VARNAME`                                                                                                                                                                                            |
| `[131]` | `VAR2`                 | ::= | `'$' VARNAME`                                                                                                                                                                                            |
| `[132]` | `LANG_DIR`             | ::= | `'@' [a-zA-Z]+ ('-' [a-zA-Z0-9]+)* ('--' [a-zA-Z]+)?`                                                                                                                                                    |
| `[133]` | `INTEGER`              | ::= | `[0-9]+`                                                                                                                                                                                                 |
| `[134]` | `DECIMAL`              | ::= | `[0-9]* '.' [0-9]+`                                                                                                                                                                                      |
| `[135]` | `DOUBLE`               | ::= | `( ([0-9]+ ('.'[0-9]*)? ) \| ( '.' ([0-9])+ ) ) [eE][+-]?[0-9]+`                                                                                                                                         |
| `[136]` | `INTEGER_POSITIVE`     | ::= | `'+' INTEGER`                                                                                                                                                                                            |
| `[137]` | `DECIMAL_POSITIVE`     | ::= | `'+' DECIMAL`                                                                                                                                                                                            |
| `[138]` | `DOUBLE_POSITIVE`      | ::= | `'+' DOUBLE`                                                                                                                                                                                             |
| `[139]` | `INTEGER_NEGATIVE`     | ::= | `'-' INTEGER`                                                                                                                                                                                            |
| `[140]` | `DECIMAL_NEGATIVE`     | ::= | `'-' DECIMAL`                                                                                                                                                                                            |
| `[141]` | `DOUBLE_NEGATIVE`      | ::= | `'-' DOUBLE`                                                                                                                                                                                             |
| `[142]` | `STRING_LITERAL1`      | ::= | `"'" ( ([^#x27#x5C#xA#xD]) \| ECHAR \| UCHAR )* "'"`                                                                                                                                                     |
| `[143]` | `STRING_LITERAL2`      | ::= | `'"' ( ([^#x22#x5C#xA#xD]) \| ECHAR \| UCHAR )* '"'`                                                                                                                                                     |
| `[144]` | `STRING_LITERAL_LONG1` | ::= | `"'''" ( ( "'" \| "''" )? ( [^'\] \| ECHAR \| UCHAR ) )* "'''"`                                                                                                                                          |
| `[145]` | `STRING_LITERAL_LONG2` | ::= | `'"""' ( ( '"' \| '""' )? ( [^"\] \| ECHAR \| UCHAR ) )* '"""'`                                                                                                                                          |
| `[146]` | `ECHAR`                | ::= | `'\' [tbnrf\"']`                                                                                                                                                                                         |
| `[147]` | `UCHAR`                | ::= | `('\u' HEX HEX HEX HEX) \| ('\U' HEX HEX HEX HEX HEX HEX HEX HEX)`                                                                                                                                       |
| `[148]` | `NIL`                  | ::= | `'(' WS* ')'`                                                                                                                                                                                            |
| `[149]` | `WS`                   | ::= | `#x20 \| #x9 \| #xD \| #xA`                                                                                                                                                                              |
| `[150]` | `ANON`                 | ::= | `'['  WS* ']'`                                                                                                                                                                                           |
| `[151]` | `PN_CHARS_BASE`        | ::= | `[A-Z] \| [a-z] \| [#x00C0-#x00D6] \| [#x00D8-#x00F6] \| [#x00F8-#x02FF] \| [#x0370-#x037D] \| [#x037F-#x1FFF] \| [#x200C-#x200D] \| [#x2070-#x218F] \| [#x2C00-#x2FEF] \| [#x3001-#xD7FF] \| [#xF900-#xFDCF] \| [#xFDF0-#xFFFD] \| [#x10000-#xEFFFF]` |
| `[152]` | `PN_CHARS_U`           | ::= | `PN_CHARS_BASE \| '_'`                                                                                                                                                                                   |
| `[153]` | `VARNAME`              | ::= | `( PN_CHARS_U  \| [0-9] ) ( PN_CHARS_U \| [0-9] \| #x00B7 \| [#x0300-#x036F] \| [#x203F-#x2040] )*`                                                                                                      |
| `[154]` | `PN_CHARS`             | ::= | `PN_CHARS_U \| '-' \| [0-9] \| #x00B7 \| [#x0300-#x036F] \| [#x203F-#x2040]`                                                                                                                             |
| `[155]` | `PN_PREFIX`            | ::= | `PN_CHARS_BASE ((PN_CHARS\|'.')* PN_CHARS)?`                                                                                                                                                             |
| `[156]` | `PN_LOCAL`             | ::= | `(PN_CHARS_U \| ':' \| [0-9] \| PLX ) ((PN_CHARS \| '.' \| ':' \| PLX)* (PN_CHARS \| ':' \| PLX) )?`                                                                                                     |
| `[157]` | `PLX`                  | ::= | `PERCENT \| PN_LOCAL_ESC`                                                                                                                                                                                |
| `[158]` | `PERCENT`              | ::= | `'%' HEX HEX`                                                                                                                                                                                            |
| `[159]` | `HEX`                  | ::= | `[0-9] \| [A-F] \| [a-f]`                                                                                                                                                                                |
| `[160]` | `PN_LOCAL_ESC`         | ::= | `'\' ( '_' \| '~' \| '.' \| '-' \| '!' \| '$' \| '&' \| "'" \| '(' \| ')' \| '*' \| '+' \| ',' \| ';' \| '=' \| '/' \| '?' \| '#' \| '@' \| '%' )`                                                       |

A text version of this grammar is available in `sparql-rl-grammar.bnf`.

### 7.7 Selected Terminal Literal Strings

This document uses some terminal literal strings
[EBNF-NOTATION]. To clarify the Unicode code points used for these
terminal literal strings, the following table describes the specific
characters used.

| Code     | Glyph | Description     |
| -------- | ----- | --------------- |
| `U+000A` | `LF`  | Line feed       |
| `U+000D` | `CR`  | Carriage return |
| `U+0023` | `#`   | Number sign     |
| `U+0025` | `%`   | Percent sign    |
| `U+005C` | `\`   | Backslash       |

## A. Translation of SPARQL-RL to SPARQL
> **Issue:**
>
> > **Issue:**
> >
> > [Issue 1303](https://github.com/w3c/data-shapes/issues/1303): SRL: Provide an algorithm to show a translation of SRL to SPARQL Query [SPARQL-RL](https://github.com/w3c/data-shapes/issues/?q=is%3Aissue+is%3Aopen+label%3A%22SPARQL-RL%22)
>
> Provide an algorithm to show a translation of SPARQL-RL to SPARQL Query.

## B. Example Imports Algorithm

*This section is non-normative.*

The following algorithm shows one way to resolve `IMPORTS` statements by
visiting all the referenced documents recursively.

The *rule set merge* of two rule sets, `RS1` and `RS2`,
produces a rule set, `MR`, defined as follows:

```
let RS be a rule set
let V = {}
if RS has a location:
    V = { location of RS }
endif

define ruleSetMerge(rule set RS1, rule set RS2):
    let MR be a rule set
    MR.rules = RS1.rules ∪ RS2.rules
    MR.data = rdf_merge(RS1.data, RS2.data)
    MR.imports = {}
    the result is MR
enddefine

define imports(rule set RS):
    let RS2 be a rule set formed from RS.rules and RS.data
    foreach URL x in RS.imports:
        if x ∉ V:
            V = V ∪ { x }
            read rule set RS3 from URL x
            RS2 = ruleSetMerge(RS2, imports(RS3))
        endif
    endfor
    the result is RS2
enddefine

result is imports(RS)
```

where `rdf_merge` is the [RDF merge](https://www.w3.org/TR/rdf12-semantics/#dfn-rdf-graph-merge) operation.

## C. Internet Media Type and File Extension

The Internet Media Type (formerly known as MIME Type) for
SPARQL-RL is "`application/sparql-rl`".

The information that follows has been submitted to the Internet Engineering
Steering Group (IESG) for review, approval, and registration with IANA.

Type name:

application

Subtype name:

sparql-rl

Required parameters:

None

Optional parameters:

`version`

This parameter is optional.
If present, acceptable values of `version` are defined in Version Labels.

`profile`

This parameter is optional and is used to include additional information.
It does not change the semantics of the resource representation when
processed without knowledge of the profile. The value of a `profile` parameter is a non-empty list of space-separated URIs.
For more information and background, please refer to [RFC6906].

Encoding considerations:

The syntax of SPARQL-RL is expressed over code points in Unicode
[UNICODE]. The encoding is always UTF-8 [RFC3629].

Unicode code points may also be expressed using an \uXXXX (U+0 to
U+FFFF) or \UXXXXXXXX syntax (for U+10000 onward)
where X is a hexadecimal digit [0-9A-Fa-f],
excluding U+D800 to U+DFFF,
the [surrogate code points](https://www.w3.org/TR/i18n-glossary/#dfn-surrogate).

Security considerations:

See D. Security Considerations (§D) as well as [UTF-8, a transformation format of ISO 10646](https://www.rfc-editor.org/info/rfc3629/) [RFC3629] section 7, Security Considerations.

Interoperability considerations:

There are no known interoperability issues.

Published specification:

This specification.

Additional information:

Magic number(s):

A SPARQL-RL file may have the string 'PREFIX'
(case independent) near the beginning
of the document.

File extension(s):

".srl"

Base URI:

The SPARQL-RL 'BASE <IRIref>' term can change the
current base URI for resolving IRIrefs in the language.

Email address to contact for further information:

Data Shapes Working Group <public-shacl@w3.org>

Intended usage:

COMMON

Restrictions on usage:

None

Author/Change controller:

The SPARQL-RL specification is a work product of the
World Wide Web Consortium's Data Shapes Working Group.
The W3C has change control over this specification.

## D. Security Considerations

*This section is non-normative.*

SPARQL-RL documents may contain `IMPORTS` statements that reference other SPARQL-RL documents and import their contents into the current document.
If an imported document itself contains its own `IMPORTS` statements,
those documents are also imported.

While useful for modularizing rule sets, the use of `IMPORTS` statements can
introduce security risks.
Risks include, but are not limited to, rule sets causing excessive computation, whether maliciously or accidentally, while being evaluated;
and HTTP requests being intercepted and a different document being returned,
including out-of-date copies.

Applying a SPARQL-RL rule set to an RDF graph can result in
significant computation and memory usage, which may be exploited
to cause denial of service.
Applications should take care to limit the amount of computation and
memory usage that can be caused by applying a SPARQL-RL rule set.

The SPARQL-RL syntax is encoded in UTF-8 [RFC3629] and allows
the use of unescaped control characters in string data.
Although this specification does not directly expose this content to an end user,
it might be presented through a user agent, which may cause the presented text to
be misleading due to such characters.

SPARQL-RL can be used to process and create arbitrary application data;
security considerations will vary by domain of use.
Security tools and protocols applicable to text
(for example, PGP encryption, checksum validation, password-protected compression)
may also be used on SPARQL-RL documents.
Security/privacy protocols must be imposed to reflect the sensitivity of the
information in the outcome of SPARQL-RL rule set evaluation.

The security considerations of SPARQL-RL include those of [RDF data](https://www.w3.org/TR/rdf12-concepts/#security) and formats such as [RDF Turtle](https://www.w3.org/TR/rdf12-turtle/#security).

## E. Privacy Considerations

*This section is non-normative.*

A SPARQL-RL document can contain additional application data
which may include the expression of personally identifiable information (PII)
or other information which could be considered sensitive.
Authors publishing rule sets with such information are advised to carefully
consider the needs and use of publishing such information,
as well as the applicable regulations for the regions where the data is
expected to be consumed and potentially revealed (e.g., [GDPR](https://gdpr.eu/), [CCPA](https://oag.ca.gov/privacy/ccpa), [others](https://termly.io/resources/infographics/privacy-laws-around-the-world/)),
particularly whether authorization measures are needed for access to the data.

## G. Index

### G.1 Terms defined by this specification

- aggregation assignments §4.1
- aggregation function §4.1
- aggregation variable §4.1
- Assignment element §4.1
- assignment expression §4.1
- assignment variable §4.1
- Base graph §4.1
- Closed dependency §4.3
- conforming SPARQL-RL document §2.
- Data block §4.1
- Dependency graph §4.3.1
- depends on
  * definition of §4.3
  * definition of §4.3
- Evaluation graph §6.1
- Expression §4.1
- Filter element §4.1
- General rule §4.1
- generate §4.3
- Graph match §6.1
- Group element §4.1
- group keys §4.1
- group pattern §4.1
- Infer §4.1
- Inference graph §4.1
- matches §4.3
- Negation element §4.1
- negation element body §4.1
- numeric escape sequence §7.5
- Open dependency §4.3
- Query §4.1
- Recursive rule dependency §4.3.1
- reserved character escape sequence §7.5
- resolved rule set §4.1
- Rule §4.1
- Rule body §4.1
- Rule dependency §4.3
- Rule element §4.1
- rule evaluation §4.1
- Rule head §4.1
- Rule set §4.1
- Rule set evaluation §4.1
- Rule set imports §4.1
- rule set merge §B.
- Run-once rule §4.1
- Solution compatible §6.1
- Solution merge §6.1
- Solution sequence §6.1
- SPARQL-RL document §7.
- SPARQL-RL processor §4.1
- Stratification §4.4
- Stratification condition §4.4.1
- Stratification layer §4.4
- stratum number §4.4
- string escape sequence §7.5
- Substitution function §6.1
- Template instance function §6.1
- Transitive rule dependency §4.3.1
- Treating blank nodes as variables §6.4
- Triple pattern §4.1
- Triple pattern dependency §4.3
- Triple pattern element §4.1
- Triple pattern matching §4.3
- Triple template §4.1
- version label §7.1
- well-formed rule §4.2
- well-formed rule set §4.2
- well-formed sequence §4.2
- Well-formedness §4.2

### G.2 Terms defined by reference

- [I18N-GLOSSARY] defines the following:
  * surrogate code points
  * Unicode code point
  * Unicode scalar values
- [RDF12-CONCEPTS] defines the following:
  * blank node
  * equals
  * graph isomorphic
  * IRI
  * RDF data
  * RDF graph
  * RDF string
  * RDF term
  * RDF triples
  * Relative IRI references
  * triple term
- [RDF12-SEMANTICS] defines the following:
  * RDF merge
- [RDF12-TURTLE] defines the following:
  * RDF Turtle
- [RFC3986] defines the following:
  * 5.1.3, Base "URI from the Retrieval URI"
  * section 5.1.1, "Base URI Embedded in Content"
  * section 5.1.2, "Base URI from the Encapsulating Entity"
  * section 5.1.4, "Default Base URI"
- [SPARQL12-QUERY] defines the following:
  * Effective boolean value
  * FILTER operation of SPARQL
  * solution mapping
  * SPARQL COUNT
  * SPARQL expressions
  * SPARQL graph pattern matching
  * SPARQL MAX
  * SPARQL MIN
  * SPARQL SUM
  * variables

## I. References

### I.1 Normative references

[EBNF-NOTATION]

[EBNF Notation](https://www.w3.org/TR/xml/#sec-notation). Tim Bray; Jean Paoli; Michael Sperberg-McQueen; Eve Maler; François Yergeau et al. W3C. W3C Recommendation. URL: <https://www.w3.org/TR/xml/#sec-notation>

[I18N-GLOSSARY]

[Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/). Richard Ishida; Addison Phillips. W3C. 17 October 2024. W3C Working Group Note. URL: <https://www.w3.org/TR/i18n-glossary/>

[RDF12-CONCEPTS]

[RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/). Andy Seaborne; Gregg Kellogg; Olaf Hartig; Pierre-Antoine Champin. W3C. 7 April 2026. W3C Candidate Recommendation. URL: <https://www.w3.org/TR/rdf12-concepts/>

[RDF12-TURTLE]

[RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/). Gregg Kellogg; Andy Seaborne; Dominik Tomaszuk. W3C. 7 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-turtle/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/info/rfc2119/). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc2119/>

[RFC3629]

[UTF-8, a transformation format of ISO 10646](https://www.rfc-editor.org/info/rfc3629/). F. Yergeau. IETF. November 2003. Internet Standard. URL: <https://www.rfc-editor.org/info/rfc3629/>

[RFC3986]

[Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/info/rfc3986/). T. Berners-Lee; R. Fielding; L. Masinter. IETF. January 2005. Internet Standard. URL: <https://www.rfc-editor.org/info/rfc3986/>

[RFC3987]

[Internationalized Resource Identifiers (IRIs)](https://www.rfc-editor.org/info/rfc3987/). M. Duerst; M. Suignard. IETF. January 2005. Proposed Standard. URL: <https://www.rfc-editor.org/info/rfc3987/>

[RFC6906]

[The 'profile' Link Relation Type](https://www.rfc-editor.org/info/rfc6906/). E. Wilde. IETF. March 2013. Informational. URL: <https://www.rfc-editor.org/info/rfc6906/>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/info/rfc8174/). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/info/rfc8174/>

[SPARQL12-QUERY]

[SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/). Olaf Hartig; Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 11 October 2026. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-query/>

[UNICODE]

[The Unicode Standard](https://www.unicode.org/versions/latest/). Unicode Consortium. URL: <https://www.unicode.org/versions/latest/>

### I.2 Informative references

[RDF12-SEMANTICS]

[RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/). Peter Patel-Schneider; Dörthe Arndt; Enrico Franconi. W3C. 24 September 2026. CRD. URL: <https://www.w3.org/TR/rdf12-semantics/>

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6) (7)

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3)

Permalink

**Referenced in:**

- § 3.1 Triple Patterns
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5)
- § 4.3 Rule Dependency (2) (3) (4) (5) (6) (7) (8) (9)
- § 6.1 Evaluation Definitions (2) (3) (4) (5)
- § 6.4 Evaluation of a Rule (2)

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6) (7)
- § 4.2 Well-formedness Conditions
- § 4.3 Rule Dependency (2) (3) (4) (5) (6) (7) (8) (9)
- § 5. Relationship between SPARQL-RL and SPARQL
- § 6.1 Evaluation Definitions (2) (3) (4)

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5)
- § 4.2 Well-formedness Conditions (2)
- § 4.3 Rule Dependency (2)
- § 5. Relationship between SPARQL-RL and SPARQL
- § 6.6.1 Determining the Dependencies (2)

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6)
- § 4.2 Well-formedness Conditions (2) (3)
- § 5. Relationship between SPARQL-RL and SPARQL
- § 6.3 Evaluation of an Expression

Permalink

**Referenced in:**

- § 3.10 Evaluating a Rule Set
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5)
- § 4.2 Well-formedness Conditions
- § 4.3 Rule Dependency (2) (3) (4) (5)
- § 4.4 Stratification
- § 6.6.1 Determining the Dependencies (2)

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2)
- § 4.2 Well-formedness Conditions (2)

Permalink

**Referenced in:**

- § 3.5 Assignment and Creating RDF Terms (2) (3)
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5)
- § 4.2 Well-formedness Conditions (2)
- § 5. Relationship between SPARQL-RL and SPARQL
- § 6.3 Evaluation of an Expression

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax
- § 4.2 Well-formedness Conditions (2) (3)
- § 5. Relationship between SPARQL-RL and SPARQL

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax
- § 4.2 Well-formedness Conditions (2)

Permalink

**Referenced in:**

- § 3.6 Grouping and Aggregation (2)
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6) (7)
- § 4.2 Well-formedness Conditions (2)
- § 4.4 Stratification

Permalink

**Referenced in:**

- § 3.6 Grouping and Aggregation (2)
- § 4.1 Elements of the Abstract Syntax
- § 4.2 Well-formedness Conditions

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2)
- § 4.2 Well-formedness Conditions (2)
- § 4.3 Rule Dependency (2)

Permalink

**Referenced in:**

- § 3.6 Grouping and Aggregation
- § 4.1 Elements of the Abstract Syntax (2) (3) (4)

Permalink

**Referenced in:**

- § 3.6 Grouping and Aggregation
- § 4.1 Elements of the Abstract Syntax
- § 4.2 Well-formedness Conditions (2) (3) (4)

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax

Permalink

**Referenced in:**

- § 3.6 Grouping and Aggregation
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6) (7) (8) (9)
- § 4.2 Well-formedness Conditions (2) (3) (4) (5)

Permalink

**Referenced in:**

- § 3. SPARQL-RL Overview
- § 3.5 Assignment and Creating RDF Terms (2)
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6) (7)
- § 4.2 Well-formedness Conditions (2)
- § 4.3 Rule Dependency
- § 5. Relationship between SPARQL-RL and SPARQL
- § 6.4 Evaluation of a Rule

Permalink

**Referenced in:**

- § 3. SPARQL-RL Overview
- § 3.6 Grouping and Aggregation
- § 3.9 Matching Base Data
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6) (7)
- § 4.2 Well-formedness Conditions (2)
- § 5. Relationship between SPARQL-RL and SPARQL
- § 6.4 Evaluation of a Rule (2)

Permalink

**Referenced in:**

- § 3.7 Importing Rule Sets
- § 4.1 Elements of the Abstract Syntax (2) (3)

Permalink

**Referenced in:**

- § 3. SPARQL-RL Overview
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6)
- § 4.2 Well-formedness Conditions
- § 4.3.1 Dependency Graph
- § 4.4 Stratification (2)
- § 6.4 Evaluation of a Rule

Permalink

**Referenced in:**

- § 3.5 Assignment and Creating RDF Terms (2)
- § 3.6 Grouping and Aggregation
- § 3.10 Evaluating a Rule Set
- § 4.1 Elements of the Abstract Syntax (2) (3)
- § 4.3 Rule Dependency
- § 4.4 Stratification (2)
- § 4.4.2 Stratification Algorithm
- § 6.5 Evaluation of a Rule Set
- § 6.6.1 Determining the Dependencies
- § 6.6.2 Calculating the Stratification (2) (3)
- § 6.6.3 Evaluating the Strata

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax
- § 6.5 Evaluation of a Rule Set
- § 6.6.2 Calculating the Stratification

Permalink

**Referenced in:**

- § 3. SPARQL-RL Overview
- § 3.7 Importing Rule Sets
- § 3.9 Matching Base Data
- § 3.10 Evaluating a Rule Set (2) (3)
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6) (7) (8) (9) (10)
- § 4.2 Well-formedness Conditions (2)
- § 4.3.1 Dependency Graph
- § 4.3.2 Dependency Graph Algorithm
- § 4.4 Stratification (2) (3) (4) (5) (6) (7)
- § 4.4.1 Stratification Condition (2) (3) (4)
- § 4.5 Processing Imports (2)
- § 6.5 Evaluation of a Rule Set
- § 6.6 Worked Example
- § D. Security Considerations (2)

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax
- § 4.5 Processing Imports

Permalink

**Referenced in:**

- § 3. SPARQL-RL Overview
- § 3.5 Assignment and Creating RDF Terms
- § 3.9 Matching Base Data (2) (3)
- § 3.10 Evaluating a Rule Set (2) (3)
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6) (7) (8) (9) (10)
- § 4.3 Rule Dependency
- § 4.3.1 Dependency Graph
- § 4.4 Stratification (2)
- § 6. Rule Set Evaluation
- § 6.1 Evaluation Definitions
- § 6.4 Evaluation of a Rule

Permalink

**Referenced in:**

- § 3. SPARQL-RL Overview
- § 3.10 Evaluating a Rule Set
- § 4.1 Elements of the Abstract Syntax (2) (3) (4)
- § 6.6 Worked Example
- § 6.6.3 Evaluating the Strata

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5)

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3) (4)

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5)

Permalink

**Referenced in:**

- § 2. Conformance
- § 3.7 Importing Rule Sets
- § 4.1 Elements of the Abstract Syntax
- § 4.5 Processing Imports

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 4.2 Well-formedness Conditions (2) (3)

Permalink

**Referenced in:**

- § 3.10 Evaluating a Rule Set
- § 4.2 Well-formedness Conditions
- § 5. Relationship between SPARQL-RL and SPARQL
- § 6.2 Preparation for Evaluation

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 4.3 Rule Dependency

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 4.3 Rule Dependency

Permalink

**Referenced in:**

- § 4.3 Rule Dependency (2)

Permalink

**Referenced in:**

- § 4.3 Rule Dependency

Permalink

**Referenced in:**

- § 4.3 Rule Dependency (2) (3)
- § 4.3.1 Dependency Graph (2)
- § 4.4.1 Stratification Condition (2)

Permalink

**Referenced in:**

- § 4.3 Rule Dependency (2)
- § 4.3.1 Dependency Graph (2)

Permalink

**Referenced in:**

- § 4.3 Rule Dependency

Permalink

**Referenced in:**

- § 4.3 Rule Dependency

Permalink

**Referenced in:**

- § 3.10 Evaluating a Rule Set
- § 4.3.1 Dependency Graph (2) (3) (4)
- § 4.3.2 Dependency Graph Algorithm
- § 4.4 Stratification
- § 4.4.1 Stratification Condition (2)
- § 6.2 Preparation for Evaluation
- § 6.6.1 Determining the Dependencies

Permalink

**Referenced in:**

- § 4.3.1 Dependency Graph
- § 6.6.1 Determining the Dependencies

Permalink

**Referenced in:**

- § 4.3.1 Dependency Graph
- § 4.4.1 Stratification Condition

Permalink

**Referenced in:**

- § 3.10 Evaluating a Rule Set
- § 4.4 Stratification (2) (3) (4) (5) (6) (7) (8) (9) (10)
- § 6.5 Evaluation of a Rule Set (2) (3)

Permalink

**Referenced in:**

- § 3.4 Negation
- § 3.10 Evaluating a Rule Set (2)
- § 4.4 Stratification (2) (3) (4) (5) (6)
- § 4.4.1 Stratification Condition (2) (3)
- § 6.2 Preparation for Evaluation (2)
- § 6.5 Evaluation of a Rule Set

Permalink

**Referenced in:**

- § 4.4 Stratification (2) (3) (4) (5) (6)

Permalink

**Referenced in:**

- § 4.4.1 Stratification Condition (2)
- § 4.4.2 Stratification Algorithm
- § 6.6.1 Determining the Dependencies

Permalink

**Referenced in:**

- § 6.1 Evaluation Definitions

Permalink

**Referenced in:**

- § 6.1 Evaluation Definitions

Permalink

**Referenced in:**

- § 6.1 Evaluation Definitions

Permalink

**Referenced in:**

- § 6.1 Evaluation Definitions

Permalink

**Referenced in:**

- § 6.1 Evaluation Definitions

Permalink

**Referenced in:**

- § 3.6 Grouping and Aggregation (2)
- § 4.1 Elements of the Abstract Syntax
- § 6.1 Evaluation Definitions
- § 6.4 Evaluation of a Rule (2)

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 4.3 Rule Dependency
- § 6.4 Evaluation of a Rule

Permalink

**Referenced in:**

- § 2. Conformance
- § 7.1 Version Announcement
- § 7.4 IRI References
- § 7.5 Escape Sequences
- § D. Security Considerations (2)

Permalink

**Referenced in:**

- § 7.1 Version Announcement

Permalink

**Referenced in:**

- § 7.5 Escape Sequences (2)

Permalink

**Referenced in:**

- § 7.5 Escape Sequences

Permalink

**Referenced in:**

- § 7.5 Escape Sequences

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 7. SPARQL-RL Grammar
- § 7.5 Escape Sequences
- § C. Internet Media Type and File Extension

Permalink

**Referenced in:**

- § 7.5 Escape Sequences (2) (3)

Permalink

**Referenced in:**

- § 7. SPARQL-RL Grammar

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2)
- § 6.1 Evaluation Definitions

Permalink

**Referenced in:**

- § 4.3 Rule Dependency (2)

Permalink

**Referenced in:**

- § 5. Relationship between SPARQL-RL and SPARQL

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3)

Permalink

**Referenced in:**

- § D. Security Considerations

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2) (3)
- § 6.1 Evaluation Definitions (2) (3) (4)

Permalink

**Referenced in:**

- § 2. Conformance
- § 7. SPARQL-RL Grammar

Permalink

**Referenced in:**

- § 3.5 Assignment and Creating RDF Terms
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6)
- § 6.1 Evaluation Definitions (2) (3) (4) (5)
- § 7.5 Escape Sequences

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax (2)
- § 4.3 Rule Dependency
- § 6.1 Evaluation Definitions

Permalink

**Referenced in:**

- § 7.4 IRI References (2)

Permalink

**Referenced in:**

- § 3.1 Triple Patterns
- § 3.5 Assignment and Creating RDF Terms
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5)
- § 4.3 Rule Dependency
- § 6.4 Evaluation of a Rule

Permalink

**Referenced in:**

- § B. Example Imports Algorithm

Permalink

**Referenced in:**

- § D. Security Considerations

Permalink

**Referenced in:**

- § 7.4 IRI References

Permalink

**Referenced in:**

- § 7.4 IRI References

Permalink

**Referenced in:**

- § 7.4 IRI References

Permalink

**Referenced in:**

- § 7.4 IRI References

Permalink

**Referenced in:**

- § 6.1 Evaluation Definitions

Permalink

**Referenced in:**

- § 3.3 Filtering

Permalink

**Referenced in:**

- § 3.6 Grouping and Aggregation
- § 4.1 Elements of the Abstract Syntax (2)
- § 6.1 Evaluation Definitions (2) (3) (4) (5) (6) (7)
- § 6.3 Evaluation of an Expression
- § 6.4 Evaluation of a Rule

Permalink

**Referenced in:**

- § 6.3 Evaluation of an Expression (2)

Permalink

**Referenced in:**

- § 4.1 Elements of the Abstract Syntax

Permalink

**Referenced in:**

- § 6.4 Evaluation of a Rule

Permalink

**Referenced in:**

- § 6.3 Evaluation of an Expression

Permalink

**Referenced in:**

- § 6.3 Evaluation of an Expression

Permalink

**Referenced in:**

- § 6.3 Evaluation of an Expression

Permalink

**Referenced in:**

- § 3.5 Assignment and Creating RDF Terms
- § 4.1 Elements of the Abstract Syntax (2) (3) (4) (5) (6) (7) (8) (9) (10) (11) (12) (13)
- § 4.2 Well-formedness Conditions (2) (3)
