---
title: "What’s New in RDF 1.2"
source: https://w3c.github.io/rdf-new/spec/
family: rdf
version: "1.2"
fetched: 2026-10-26
---

# What’s New in RDF 1.2

> Summary of changes from RDF 1.1 to 1.2.

## Contents

- 1 Introduction
- 2 Abstract Syntax
- 3 New Serialization Formats
- 4 Semantics

---

This document provides the reader with a summary
of changes to RDF introduced in RDF version 1.2.

## Introduction

This document is informative in nature. Its
purpose is to provide a summary of differences between RDF versions 1.1
and 1.2 and to introduce new additions in a very brief manner.

Readers new to RDF should start with the [RDF12-PRIMER] [RDF12-PRIMER]
and then move on to the specifications in which they are
most interested. This document is meant to serve as a guide for those
already familiar with RDF 1.1 who wish to understand changes in version
1.2.

Normative specifications of RDF can be found in the
following documents:

- A document describing the basic concepts underlying RDF, as
  well as abstract syntax ([RDF12-CONCEPTS]) [RDF12-CONCEPTS]
- A document describing the formal model-theoretic semantics
  of RDF ([RDF12-SEMANTICS]) [RDF12-SEMANTICS]
- Specifications of concrete syntaxes for RDF, such as Turtle
  [RDF12-TURTLE], TriG [RDF12-TRIG], N-Triples [RDF12-N-TRIPLES],
  N-Quads [RDF12-N-QUADS] and JSON-LD [JSON-LD11].
  RDFa [RDFA-PRIMER] is also a concrete syntax for RDF, but it was not defined
  by the RDF Working Group.
  The 2004 RDF/XML syntax was updated to be in line with the RDF 1.2
  specifications [RDF12-XML].
- A document describing RDF Schema [RDF12-SCHEMA], which
  provides a data-modeling vocabulary for RDF data.

The following prefixes are used in this document:

*Prefixes and IRIs*

| Namespace prefix | Namespace IRI                                 | RDF vocabulary                               |
| ---------------- | --------------------------------------------- | -------------------------------------------- |
| rdf              | <http://www.w3.org/1999/02/22-rdf-syntax-ns#> | The RDF built-in vocabulary [RDF12-SCHEMA] |
| xsd              | <http://www.w3.org/2001/XMLSchema#>           | The RDF-compatible XML Schema datatypes      |

## Abstract Syntax

## New Serialization Formats

RDF 1.1 introduces a number of new serialization formats. RDF 1.1 Concepts and
Abstract Syntax makes it clear that RDF/XML is no longer the only recommended serialization
format; RDF itself should be considered to be the data model (the
abstract syntax), not any particular serialization.

!

*RDF 1.0 and 1.1 serialization formats*

## Semantics

Most of the changes between RDF and RDF 1.1 do not have any effect on
implementations of entailment.

Datatype entailment formally refers to a set of 'recognized' datatypes,
replacing datatype maps in RDF 1.0 Semantics, but this does not have any
effect on implementation.

Datatype entailment formally refers to a set of 'recognized' datatype IRIs.
The RDF 1.0 Semantics used the concept of a datatype map: in the new semantic
description, this is the mapping from recognized IRIs to the datatypes they
identify. This change does not have any effect on implementation or semantic
entailments.

RDF entailment has two required datatypes `xsd:string` and `rdf:langString` which must be recognized, but this doesn't appreciably add to RDF
entailment as these two datatypes replace plain literals.

One change that does affect entailment is that graphs containing invalid
literals (e.g., `"a"^^xsd:integer`) are immediately inconsistent for
recognized datatypes, even in sub-RDFS entailment regimes.

RDF 1.1 includes RDF Datasets. However, the semantics of RDF Datasets in
RDF 1.1 is minimal and entailment per se is only defined on RDF graphs so
there are no changes here.
