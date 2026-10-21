---
title: "A Direct Mapping of Relational Data to RDF"
source: https://www.w3.org/TR/rdb-direct-mapping/
family: mapping
status: W3C Recommendation
spec_date: 2012-09-27
fetched: 2026-10-21
---

# A Direct Mapping of Relational Data to RDF

> Default lossless mapping of relational schemas.

## Contents

- Abstract
- 1 Introduction
- 2 Direct Mapping Description (Informative)
  - 2.1 Direct Mapping Example
  - 2.2 Foreign keys referencing candidate keys
  - 2.3 Multi-column primary keys
  - 2.4 Empty (non-existent) primary keys
  - 2.5 Referencing tables with empty primary keys
- 3 Direct Graph Definition
- 4 References
- A Direct Mapping Algebra (Informative)
  - A.1 Notations
  - A.2 Relational Data Model
    - A.2.1 RDB Abstract Data Type
    - A.2.2 RDB accessor functions
  - A.3 RDF Data Model
  - A.4 Denotational semantics
- B Direct Mapping as Rules (Informative)
  - B.1 Generating Row Type Triples
    - B.1.1 Table has a primary key
    - B.1.2 Table does not have a primary key
  - B.2 Generating Literal Triples
    - B.2.1 Table has a primary key
    - B.2.2 Table does not have a primary key
  - B.3 Generating Reference Triples
    - B.3.1 Table r1 has a primary key and table r2 has a primary key
    - B.3.2 Table r1 has a primary key and table r2 does not have a primary key
    - B.3.3 Table r1 does not have primary key and table r2 has a primary key
    - B.3.4 Table r1 does not have primary key and table r2 does not have a primary key

---

---

## Abstract

The need to share data with collaborators motivates custodians and users of relational databases (RDB) to expose relational data on the Web of Data. This document defines a *direct mapping* from relational data to RDF. This definition provides extension points for refinements within and outside of this document.

*This section describes the status of this document at the time of its
publication. Other documents may supersede this document. A list of current W3C
publications and the latest revision of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at
http://www.w3.org/TR/.*

This document has been reviewed by W3C Members, by software developers,
and by other W3C groups and interested parties, and is endorsed by the
Director as a [W3C Recommendation](https://www.w3.org/2004/02/Process-20040205/tr.html#RecsW3C). It is a stable document and may be used as reference
material or cited from another document. W3C's role in making the
Recommendation is to draw attention to the specification and to promote
its widespread deployment. This enhances the functionality and
interoperability of the Web.

This document was published by the [RDB2RDF Working Group](https://www.w3.org/2001/sw/rdb2rdf/).
Comments on this document should be sent to <public-rdb2rdf-comments@w3.org>,
a mailing list with a [public archive](http://lists.w3.org/Archives/Public/public-rdb2rdf-comments/).
The following related documents have been made available:

- A [wiki page](https://www.w3.org/2001/sw/wiki/RDB2RDF) with additional information for users and implementers of R2RML,
- a [color-coded diff](https://www.w3.org/TR/rdb-direct-mapping/PR-to-REC) of all changes since the previous draft,
- the [implementation report](https://www.w3.org/TR/2012/NOTE-rdb2rdf-implementations-20120814/) used by the director to transition to W3C Recommendation.

This document was produced by a group operating under the [5 February 2004 W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy-20040205/). W3C maintains a [public list of any patent disclosures](https://www.w3.org/2004/01/pp-impl/43889/status) made in connection with the deliverables of the group; that page also
includes instructions for disclosing a patent. An individual who has actual knowledge
of a patent which the individual believes contains [Essential Claim(s)](https://www.w3.org/Consortium/Patent-Policy-20040205/#def-essential) must disclose the information in accordance with [section 6 of the W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy-20040205/#sec-Disclosure).

---

## 1 Introduction

Relational databases proliferate both because of their efficiency and their precise definitions, allowing for tools like SQL [SQLFN](https://www.w3.org/TR/rdb-direct-mapping/#SQLFN) to manipulate and examine the contents predictably and efficiently. Resource Description Framework (RDF) [RDF-concepts](https://www.w3.org/TR/rdb-direct-mapping/#RDF-concepts) is a data format based on a web-scalable architecture for identification and interpretation of terms. This document defines a mapping from relational representation to an RDF representation.

Strategies for mapping relational data to RDF abound.
The *direct mapping* defines a simple transformation, providing a basis for defining and comparing more intricate transformations.
It can also be used to materialize RDF graphs or define virtual graphs, which can be queried by SPARQL or traversed by an RDF graph API.
This document includes an informal and a formal description of the transformation.

This specification has a companion, the [R2RML](https://www.w3.org/TR/2012/REC-r2rml-20120927/) mapping language [R2RML](https://www.w3.org/TR/rdb-direct-mapping/#R2RML), that allows the creation of customized mapping from relational data to RDF.
R2RML defines a [relaxed variant](https://www.w3.org/TR/2012/REC-r2rml-20120927/#dfn-duplicate-row-preservation) of the Direct Mapping intended as a [default mapping](https://www.w3.org/TR/2012/REC-r2rml-20120927/#default-mappings) for further customization.

## 2 Direct Mapping Description (Informative)

The direct mapping defines an [RDF Graph](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-rdf-graph) [RDF-concepts](https://www.w3.org/TR/rdb-direct-mapping/#RDF-concepts) representation of the data in a relational database. The direct mapping takes as input a relational database (data and schema), and generates an RDF graph that is called the *direct graph*. The algorithms in this document compose a graph of relative IRIs which must be resolved against a *base* IRI [RFC3987](https://www.w3.org/TR/rdb-direct-mapping/#RFC3987) to form an RDF graph.

Foreign keys in relational databases establish a reference from any row in a table to exactly one row in a (potentially different) table. The direct graph conveys these references, as well as each value in the row.

### 2.1 Direct Mapping Example

The concepts in direct mapping can be introduced with an example RDF graph produced by a relational database. Following is SQL (DDL) to create a simple example with two tables with single-column primary keys and one foreign key reference between them:

```
CREATE TABLE "Addresses" (
	"ID" INT, PRIMARY KEY("ID"),
	"city" CHAR(10),
	"state" CHAR(2)
)

CREATE TABLE "People" (
	"ID" INT, PRIMARY KEY("ID"),
	"fname" CHAR(10),
	"addr" INT,
	FOREIGN KEY("addr") REFERENCES "Addresses"("ID")
)

INSERT INTO "Addresses" ("ID", "city", "state") VALUES (18, 'Cambridge', 'MA')
INSERT INTO "People" ("ID", "fname", "addr") VALUES (7, 'Bob', 18)
INSERT INTO "People" ("ID", "fname", "addr") VALUES (8, 'Sue', NULL)

```

HTML tables will be used in this document to convey SQL tables. The primary key of these tables will be marked with the `PK` class to convey an SQL primary key such as `ID` in `CREATE TABLE "Addresses" ("ID" INT, ... PRIMARY KEY("ID"))`. Foreign keys will be illustrated with a notation like "`→ Address(ID)`" to convey an SQL foreign key such as `CREATE TABLE "People" (... "addr" INT, FOREIGN KEY("addr") REFERENCES "Addresses"("ID"))`.

*People*

| PK |       | → Address(ID)                                                   |
| --- | ----- | --------------------------------------------------------------- |
| ID | fname | addr                                                            |
| 7  | Bob   | 18 |
| 8  | Sue   | *NULL*                                                          |

*Addresses*

| PK |           | |
| --- | --------- | ----- |
| ID | city      | state |
| 18 | Cambridge | MA    |

Given a base IRI `http://foo.example/DB/`, the direct mapping of this database produces a direct graph:

```
@base <http://foo.example/DB/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<People/ID=7> rdf:type <People> .
<People/ID=7> <People#ID> 7 .
<People/ID=7> <People#fname> "Bob" .
<People/ID=7> <People#addr> 18 .
<People/ID=7> <People#ref-addr> <Addresses/ID=18> .
<People/ID=8> rdf:type <People> .
<People/ID=8> <People#ID> 8 .
<People/ID=8> <People#fname> "Sue" .

<Addresses/ID=18> rdf:type <Addresses> .
<Addresses/ID=18> <Addresses#ID> 18 .
<Addresses/ID=18> <Addresses#city> "Cambridge" .
<Addresses/ID=18> <Addresses#state> "MA" .

```

In this expression, each row, e.g. `(7, "Bob", 18)`, produces a set of triples with a common subject. The subject is an IRI formed from the concatenation of the base IRI, table name (`People`), primary key column name (`ID`) and primary key value (`7`). The predicate for each column is an IRI formed from the concatenation of the base IRI, table name and the column name. The values are RDF literals formed from the lexical form of the column value. Each foreign key produces a triple with a predicate composed from the foreign key column names, the referenced table, and the referenced column names. The object of these triples is the row identifier (`<Addresses/ID=18>`) for the referenced triple. Note that these reference row identifiers must coincide with the subject used for the triples generated from the referenced row. The direct mapping does not generate triples for NULL values. Note that it is not known how to relate the behavior of the obtained RDF graph with the standard SQL semantics of the NULL values of the source RDB.

### 2.2 Foreign keys referencing candidate keys

More complex schemas include composite keys. In this example, the columns *deptName* and *deptCity* in the *People* table reference *name* and *city* in the *Department* table:

```
CREATE TABLE "Addresses" (
	"ID" INT,
	"city" CHAR(10),
	"state" CHAR(2),
	PRIMARY KEY("ID")
)

CREATE TABLE "Department" (
	"ID" INT,
	"name" CHAR(10),
	"city" CHAR(10),
	"manager" INT,
	PRIMARY KEY("ID"),
	UNIQUE ("name", "city")
)

CREATE TABLE "People" (
	"ID" INT,
	"fname" CHAR(10),
	"addr" INT,
	"deptName" CHAR(10),
	"deptCity" CHAR(10),
	PRIMARY KEY("ID"),
	FOREIGN KEY("addr") REFERENCES "Addresses"("ID"),
	FOREIGN KEY("deptName", "deptCity") REFERENCES "Department"("name", "city")
)

ALTER TABLE "Department" ADD FOREIGN KEY("manager") REFERENCES "People"("ID")

```

Following is an instance of this schema:

*People*

| PK |       | → Addresses(ID)                                                  | → Department(name, city)                                                  | |
| --- | ----- | ---------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| ID | fname | addr                                                             | deptName                                                                  | deptCity                                                                 |
| 7  | Bob   | 18 | accounting | Cambridge |
| 8  | Sue   | *NULL*                                                           | *NULL*                                                                    | *NULL*                                                                   |

*Addresses*

| PK |           | |
| --- | --------- | ----- |
| ID | city      | state |
| 18 | Cambridge | MA    |

*Department*

| PK | Unique Key | | → People(ID)                                                  |
| --- | ---------- | --------- | ------------------------------------------------------------- |
| ID | name       | city      | manager                                                       |
| 23 | accounting | Cambridge | 8 |

Per the *People* table's compound foreign key to Department:

- The row in *People* with `deptName="accounting"` and `deptCity="Cambridge"` references a row in *Department* with a primary key of `ID=23`.
- The predicate for this key is formed from "`deptName`" and "`deptCity`", reflecting the order of the column names in the foreign key.
- The object of the above predicate is formed from the base IRI, the table name "`Department`" and the primary key value "`ID=23`".

Note: The order of a primary key constraint's columns is determined by the DDL statement used to create it. In SQL implementations that support the information schema, this order can be accessed through the `INFORMATION_SCHEMA.KEY_COLUMN_USAGE.ORDINAL_POSITION` column.

In this example, the direct mapping generates the following triples:

```
@base <http://foo.example/DB/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<People/ID=7> rdf:type <People> .
<People/ID=7> <People#ID> 7 .
<People/ID=7> <People#fname> "Bob" .
<People/ID=7> <People#addr> 18 .
<People/ID=7> <People#ref-addr> <Addresses/ID=18> .
<People/ID=7> <People#deptName> "accounting" .
<People/ID=7> <People#deptCity> "Cambridge" .
<People/ID=7> <People#ref-deptName;deptCity> <Department/ID=23> .
<People/ID=8> rdf:type <People> .
<People/ID=8> <People#ID> 8 .
<People/ID=8> <People#fname> "Sue" .

<Addresses/ID=18> rdf:type <Addresses> .
<Addresses/ID=18> <Addresses#ID> 18 .
<Addresses/ID=18> <Addresses#city> "Cambridge" .
<Addresses/ID=18> <Addresses#state> "MA" .

<Department/ID=23> rdf:type <Department> .
<Department/ID=23> <Department#ID> 23 .
<Department/ID=23> <Department#name> "accounting" .
<Department/ID=23> <Department#city> "Cambridge" .
<Department/ID=23> <Department#manager> 8 .
<Department/ID=23> <Department#ref-manager> <People#ID=8> .

```

The green triples above are generated by considering the new elements in the augmented database. Note:

- The Reference Triple `<People/ID=7> <People#ref-deptName;deptCity> <Department/ID=23>` is generated by considering a foreign key referencing a candidate key (different from the primary key).

### 2.3 Multi-column primary keys

Primary keys may also be composite. If, in the above example (§2.2), the primary key for *Department* were (*name*, *city*) instead of *ID*, the identifier for the only row in this table would be `<Department/name=accounting;city=Cambridge>`. The triples involving `<Department/ID=23>` would be replaced with the following triples:

```
<People/ID=7> <People#ref-deptName;deptCity> <Department/name=accounting;city=Cambridge> .
<Department/name=accounting;city=Cambridge> rdf:type <Department> .
<Department/name=accounting;city=Cambridge> <Department#ID> 23 .
<Department/name=accounting;city=Cambridge> <Department#name> "accounting" .
<Department/name=accounting;city=Cambridge> <Department#city> "Cambridge" .

```

### 2.4 Empty (non-existent) primary keys

If there is no primary key, each row implies a set of triples with a shared subject, but that subject is a blank node. A *Tweets* table can be added to the above example (§2.2) to keep track of employees' tweets in Twitter:

```
CREATE TABLE "Tweets" (
	"tweeter" INT,
	"when" TIMESTAMP,
	"text" CHAR(140),
	FOREIGN KEY("tweeter") REFERENCES "People"("ID")
)

```

The following is an instance of table *Tweets*:

*Tweets*

| → People(ID)                                                  |                  | |
| ------------------------------------------------------------- | ---------------- | ---------------------- |
| tweeter                                                       | when             | text                   |
| 7 | 2010-08-30T01:33 | I really like lolcats. |
| 7 | 2010-08-30T09:01 | I take it back.        |

Given that table *Tweets* does not have a primary key, each row in this table is identified by a Blank Node. In fact, when translating the above table the direct mapping generates the following triples:

```
@base <http://foo.example/DB/>
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

_:a rdf:type <Tweets> .
_:a <Tweets#tweeter> "7" .
_:a <Tweets#ref-tweeter> <People/ID=7> .
_:a <Tweets#when> "2010-08-30T01:33"^^xsd:dateTime .
_:a <Tweets#text> "I really like lolcats." .

_:b rdf:type <Tweets> .
_:b <Tweets#tweeter> "7" .
_:b <Tweets#ref-tweeter> <People/ID=7> .
_:b <Tweets#when> "2010-08-30T09:01"^^xsd:dateTime .
_:b <Tweets#text> "I take it back." .

```

### 2.5 Referencing tables with empty primary keys

Rows in tables with no primary key may still be referenced by foreign keys. (Relational database theory tells us that these rows must be unique as foreign keys reference candidate keys and candidate keys are unique across all the rows in a table.) References to rows in tables with no primary key are expressed as RDF triples with blank nodes for objects, where that blank node is the same node used for the subject in the referenced row.

Here is DDL for a schema with references to a `Projects` table which has no primary key:

```
CREATE TABLE "Projects" (
	"lead" INT,
	FOREIGN KEY ("lead") REFERENCES "People"("ID"),
	"name" VARCHAR(50),
	UNIQUE ("lead", "name"),
	"deptName" VARCHAR(50),
	"deptCity" VARCHAR(50),
	UNIQUE ("name", "deptName", "deptCity"),
	FOREIGN KEY ("deptName", "deptCity") REFERENCES "Department"("name", "city")
)

CREATE TABLE "TaskAssignments" (
	"worker" INT,
	FOREIGN KEY ("worker") REFERENCES "People"("ID"),
	"project" VARCHAR(50),
	PRIMARY KEY ("worker", "project"),
	"deptName" VARCHAR(50),
	"deptCity" VARCHAR(50),
	FOREIGN KEY ("worker") REFERENCES "People"("ID"),
	FOREIGN KEY ("project", "deptName", "deptCity") REFERENCES "Projects"("name", "deptName", "deptCity"),
	FOREIGN KEY ("deptName", "deptCity") REFERENCES "Department"("name", "city")
)

```

The following is an instance of the preceding schema:

*Projects*

| Unique key                                                    | |                          | |
| ------------------------------------------------------------- | ------------- | ------------------------ | --------- |
|                                                               | Unique key    | | |
| → People(ID)                                                  |               | → Department(name, city) | |
| lead                                                          | name          | deptName                 | deptCity  |
| 8 | pencil survey | accounting               | Cambridge |
| 8 | eraser survey | accounting               | Cambridge |

*TaskAssignments*

| PK                                                            | |                           | |
| ------------------------------------------------------------- | ------------------------------------ | ------------------------- | --------- |
|                                                               | → Projects(name, deptName, deptCity) | | |
| → People(ID)                                                  |                                      | → Departments(name, city) | |
| worker                                                        | project                              | deptName                  | deptCity  |
| 7 | pencil survey                        | accounting                | Cambridge |

In this case, the direct mapping generates the following triples from the preceding tables:

```
@base <http://foo.example/DB/>
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

_:c rdf:type <Projects> .
_:c <Projects#lead> <People/ID=8> .
_:c <Projects#name> "pencil survey" .
_:c <Projects#deptName> "accounting" .
_:c <Projects#deptCity> "Cambridge" .
_:c <Projects#ref-deptName;deptCity> <Department/ID=23> .

_:d rdf:type <Projects> .
_:d <Projects#lead> <People/ID=8> .
_:d <Projects#name> "eraser survey" .
_:d <Projects#deptName> "accounting" .
_:d <Projects#deptCity> "Cambridge" .
_:d <Projects#ref-deptName;deptCity> <Department/ID=23> .

<TaskAssignments/worker=7.project=pencil%20survey> rdf:type <TaskAssignments> .
<TaskAssignments/worker=7.project=pencil%20survey> <TaskAssignments#worker> 7 .
<TaskAssignments/worker=7.project=pencil%20survey> <TaskAssignments#ref-worker> <People/ID=7> .
<TaskAssignments/worker=7.project=pencil%20survey> <TaskAssignments#project> "pencil survey" .
<TaskAssignments/worker=7.project=pencil%20survey> <TaskAssignments#deptName> "accounting" .
<TaskAssignments/worker=7.project=pencil%20survey> <TaskAssignments#deptCity> "Cambridge" .
<TaskAssignments/worker=7.project=pencil%20survey> <TaskAssignments#ref-deptName;deptCity> <Department/ID=23> .
<TaskAssignments/worker=7.project=pencil%20survey> <TaskAssignments#ref-project;deptName;deptCity> _:c .

```

The absence of a primary key forces the generation of blank nodes, but does not change the structure of the direct graph or names of the predicates in that graph.

## 3 Direct Graph Definition

The Direct Graph is a formula for creating an RDF graph from the rows of each table and view in a database schema. A base IRI defines a web space for the IRIs in this graph; for the purposes of this specification, all IRIs are generated by appending to a base. Terms enclosed in <> are defined in the SQL specification [SQLFN](https://www.w3.org/TR/rdb-direct-mapping/#SQLFN).

An SQL table has a set of uniquely-named columns and has a set of foreign keys, each mapping a <column name list> to a <unique column list> (a list of columns in some table).

SQL table and column identifiers compose RDF IRIs in the direct graph.
These identifiers are separated by the punctuation characters '#', ';', '/' and '='. All SQL identifiers are escaped following R2RML's escaping rules.

Definition *percent-encode*:

- Replace the string with the [IRI-safe](https://www.w3.org/TR/2012/REC-r2rml-20120927/#dfn-iri-safe) form per section 7.3 of [R2RML](https://www.w3.org/TR/rdb-direct-mapping/#R2RML).

There is either a blank node or IRI assigned to each each row in a table:

Definition *row node*:

- If the table has a primary key, the row node is a relative IRI obtained by concatenating:
  * the percent-encoded form of the table name,
  * the SOLIDUS character '/',
  * for each column in the primary key, in order:
    + the percent-encoded form of the column name,
    + a EQUALS SIGN character '=',
    + the percent-encoded lexical form of the [canonical RDF literal](https://www.w3.org/TR/2012/REC-r2rml-20120927/#dfn-canonical-rdf-lexical-form) representation of the column value as defined in [R2RML section 10.2 Natural Mapping of SQL Values](https://www.w3.org/TR/2012/REC-r2rml-20120927/#natural-mapping) [R2RML](https://www.w3.org/TR/rdb-direct-mapping/#R2RML),
    + if it is not the last column in the primary key, a SEMICOLON character ';'
- If the table has no primary key, the row node is a fresh blank node that is unique to this row.

A table forms a table IRI:

Definition *table IRI*: the relative IRI consisting of the percent-encoded form of the table name.

A column in a table forms a literal property IRI:

Definition *literal property IRI*: the concatenation of:

- the percent-encoded form of the table name,
- the hash character '#',
- the percent-encoded form of the column name.

A foreign key in a table forms a reference property IRI:

Definition *reference property IRI*: the concatenation of:

- the percent-encoded form of the table name,
- the string '#ref-',
- for each column in the foreign key, in order:
  * the percent-encoded form of the column name,
  * if it is not the last column in the foreign key, a SEMICOLON character ';'

Any input database with a given schema has a *direct graph* defined as:

Definition *direct graph*: the union of the table graphs for each table in a database schema.

Definition *table graph*: the union of the row graphs for each row in a table.

Definition *row graph*: an RDF graph consisting of the following triples:

- the row type triple.
- a reference triple for each <column name list> in a table's foreign keys where none of the column values is NULL.
- a literal triple for each column in a table where the column value is non-NULL.

Definition *row type triple*: an RDF triple with:

- subject: the row node for the row.
- predicate: the RDF IRI `rdf:type`.
- object: the table IRI for the table name.

Definition *literal triple*: an RDF triple with:

- subject: the row node for the row.
- predicate: the literal property IRI for the column.
- object: the [R2RML natural RDF literal](https://www.w3.org/TR/2012/REC-r2rml-20120927/#dfn-natural-rdf-literal) representation of the column value as defined in [R2RML section 10.2 Natural Mapping of SQL Values](https://www.w3.org/TR/2012/REC-r2rml-20120927/#natural-mapping).

Definition *reference triple*: an RDF triple with:

- subject: the row node for the row.
- predicate: the reference property IRI for the columns.
- object: the row node for the referenced row.

## 4 References

R2RML

[R2RML: RDB to RDF Mapping Language](https://www.w3.org/TR/2012/REC-r2rml-20120927/) , Souripriya Das, Seema Sundara, Richard Cyganiak, Editors.
World Wide Web Consortium, 27 September 2012.
This version is http://www.w3.org/TR/2012/REC-r2rml-20120927/.
The latest version is http://www.w3.org/TR/r2rml/.
This document is work in progress.

SPARQL

SPARQL Query Language for RDF, Eric Prud'hommeaux and Andy Seaborne 2008. (See http://www.w3.org/TR/rdf-sparql-query/.)

SQLFW

SQL. ISO/IEC 9075-1:2008 SQL – Part 1: Framework (SQL/Framework) International Organization for Standardization, 27 January 2009.

SQLFN

ISO/IEC 9075-2:2008 SQL – Part 2: Foundation (SQL/Foundation) International Organization for Standardization, 27 January 2009.

RDF-concepts

Resource Description Framework (RDF): Concepts and Abstract Syntax, G. Klyne, J. J. Carroll, Editors, W3C Recommendation, 10 February 2004 (See http://www.w3.org/TR/2004/REC-rdf-concepts-20040210/.)

ReuseableIDs

Reusable Identifiers in the RDB2RDF mapping language, Michael Hausenblas and Themis Palpanas, 2009. (See http://esw.w3.org/topic/Rdb2RdfXG/ReusableIdentifier.)

URI

RFC3986 - Uniform Resource Identifier (URI): Generic Syntax (See http://tools.ietf.org/html/rfc3986.)

RFC3987

RFC3987 - Internationalized Resource Identifier (IRIs) (See http://tools.ietf.org/html/rfc3987.)

SQL2SW

Translating SQL Applications to the Semantic Web. Syed Hamid Tirmizi, Juan Sequeda and Daniel Miranker. 2008 (See http://www.springerlink.com/content/mv58805364k31734/.)

DMSurvey

Survey of directly mapping SQL databases to the Semantic Web. Juan Sequeda, Syed Hamid Tirmizi, Oscar Corcho, Daniel P. Miranker. 2011 (See http://journals.cambridge.org/abstract_S0269888911000208.)

## A Direct Mapping Algebra (Informative)

### A.1 Notations

The RDB and RDF data models make use of the commonly defined [Abstract Data Types](https://en.wikipedia.org/wiki/Abstract_data_type) [Set](https://en.wikipedia.org/wiki/Set_(computer_science)), [List](https://en.wikipedia.org/wiki/List_(computer_science)) and [MultiSet](https://en.wikipedia.org/wiki/Set_(computer_science)#Multiset), used here as type constructors. For example, `Set(A)` denotes the type for the sets of elements of type `A`. We assume that they come with their common operations, such as the function `size : Set → Int`.

The definitions follow a type-as-specification approach; thus the models are based on [dependent types](https://en.wikipedia.org/wiki/Dependent_type). For example, `{ s:Set(A) | size(s) ≤ 1 }` is a type denoting the sets for elements of type A, such that those sets have at most one element.

The denotational RDF semantics makes use of the [set-builder notation](https://en.wikipedia.org/wiki/Set-builder_notation) for building the RDF sets.

The buttons below can be used to show or hide the available syntaxes.

### A.2 Relational Data Model

#### A.2.1 RDB Abstract Data Type

| [1]                                                                                                                                                                                                      | `Database`     | ::= | `Set(Table)`                                                                                                        |  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --- | ------------------------------------------------------------------------------------------------------------------- | --- |
| [1]                                                                                                                                                                                                      | `Database`     | ::= | `{ Table }`                                                                                                         |  |
| A *relational database* is a set of tables.                                                                                                                                                              | | | | |
| [2]                                                                                                                                                                                                      | `Table`        | ::= | `(TableName, Set((ColumnName, Datatype)), Set(CandidateKey), Set(PrimaryKey) \| size() ≤ 1, Set(ForeignKey), Body)` |  |
| [2]                                                                                                                                                                                                      | `Table`        | ::= | `( TableName, { ColumnName → Datatype }, { CandidateKey }, PrimaryKey?, { ForeignKey }, Body )`                     |  |
| A *relation* has a name uniquely defining this table in the database; an [associative array](https://en.wikipedia.org/wiki/Associative_array) mapping each column to a SQL datatype; a potentially empty list of candidate keys, possibly including a primary key; a potentially empty set of foreign keys; a body containing the rows of data. | | | | |
| [3]                                                                                                                                                                                                      | `Body`         | ::= | `MultiSet(Row)`                                                                                                     |  |
| [3]                                                                                                                                                                                                      | `Body`         | ::= | `[ Row ]`                                                                                                           |  |
| A *body* is a set of potentially duplicate rows.                                                                                                                                                         | | | | |
| [4]                                                                                                                                                                                                      | `Row`          | ::= | `Set((ColumnName, CellValue))`                                                                                      |  |
| [4]                                                                                                                                                                                                      | `Row`          | ::= | `{ ColumnName → CellValue }`                                                                                        |  |
| A *row* is a [associative array](https://en.wikipedia.org/wiki/Associative_array) mapping each column in a row to a value.                                                                               | | | | |
| [5]                                                                                                                                                                                                      | `CellValue`    | ::= | `Value \| NULL`                                                                                                     |  |
| [5]                                                                                                                                                                                                      | `CellValue`    | ::= | `Value \| Null`                                                                                                     |  |
| A *cell value* is either a lexical value or NULL, denoting the absence of value.                                                                                                                         | | | | |
| [6]                                                                                                                                                                                                      | `ForeignKey`   | ::= | `(List(ColumnName), Table, CandidateKey)`                                                                           |  |
| [6]                                                                                                                                                                                                      | `ForeignKey`   | ::= | `{ [ColumnName] → ( Table, [ColumnName] ) }`                                                                        |  |
| A *foreign key* constrains the values of a <column name list> to be equivalent (by the SQL `=` operator) to the values of a <unique column list> in some row of the referenced table.                    | | | | |
| [7]                                                                                                                                                                                                      | `PrimaryKey`   | ::= | `CandidateKey`                                                                                                      |  |
| [7]                                                                                                                                                                                                      | `PrimaryKey`   | ::= | `CandidateKey`                                                                                                      |  |
| A *primary key* is a candidate key with the additional constraint that none of the columns can have a NULL value.                                                                                        | | | | |
| [8]                                                                                                                                                                                                      | `CandidateKey` | ::= | `List(ColumnName)`                                                                                                  |  |
| [8]                                                                                                                                                                                                      | `CandidateKey` | ::= | `[ ColumnName ]`                                                                                                    |  |
| A *candidate key* is an SQL <unique column list> in some table. This constrains that no two rows in the table have values for the <unique column list> which are *all* equivalent (by the SQL `=` operator). | | | | |
| [9]                                                                                                                                                                                                      | `Datatype`     | ::= | `Int \| Float \| Date \| …`                                                                                         |  |
| [9]                                                                                                                                                                                                      | `Datatype`     | ::= | `{ INT \| FLOAT \| DATE \| TIME \| TIMESTAMP \| CHAR \| VARCHAR \| STRING }`                                        |  |
| A *datatype* is a common SQL datatype.                                                                                                                                                                   | | | | |
| [10]                                                                                                                                                                                                     | `TableName`    | ::= | `String`                                                                                                            |  |
| [10]                                                                                                                                                                                                     | `TableName`    | ::= | `String`                                                                                                            |  |
| A *table name* is a string.                                                                                                                                                                              | | | | |
| [11]                                                                                                                                                                                                     | `ColumnName`   | ::= | `String`                                                                                                            |  |
| [11]                                                                                                                                                                                                     | `ColumnName`   | ::= | `String`                                                                                                            |  |
| A *column name* is a string.                                                                                                                                                                             | | | | |

#### A.2.2 RDB accessor functions

| [12]                                                                                                                                                                                                     | `tablename`     | : | `Table → TableName`                                                                                                                                                                                      |  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| Given a table, *tablename* returns its name.                                                                                                                                                             | | | | |
| [13]                                                                                                                                                                                                     | `header`        | : | `Table → Set((ColumnName, Datatype))`                                                                                                                                                                    |  |
| Given a table, *header* returns its header.                                                                                                                                                              | | | | |
| [14]                                                                                                                                                                                                     | `candidateKeys` | : | `Table → List(CandidateKey)`                                                                                                                                                                             |  |
| Given a table, *candidateKeys* returns the list of candidate keys.                                                                                                                                       | | | | |
| [15]                                                                                                                                                                                                     | `primaryKey`    | : | `Table → { s:Set(CandidateKey) \| size(s) ≤ 1 }`                                                                                                                                                         |  |
| Given a table, *primaryKey* returns a set containing the primary key if it exists, otherwise it returns an empty set.                                                                                    | | | | |
| [16]                                                                                                                                                                                                     | `foreignKeys`   | : | `Table → Set(ForeignKey)`                                                                                                                                                                                |  |
| Given a table, *foreignKeys* returns the set of foreign keys.                                                                                                                                            | | | | |
| [17]                                                                                                                                                                                                     | `unary`         | : | `ForeignKey → Boolean`                                                                                                                                                                                   |  |
| Given a foreign key, *unary* tells if this is a unary foreign key, meaning it has exactly one column.                                                                                                    | | | | |
| [18]                                                                                                                                                                                                     | `lexicals`      | : | `Table → Set({ c:ColumnName \| ! unary(c) })`                                                                                                                                                            |  |
| Given a table, *lexicals* returns the set of columns that do not constitute a unary foreign key.                                                                                                         | | | | |
| [19]                                                                                                                                                                                                     | `body`          | : | `Table → Body`                                                                                                                                                                                           |  |
| Given a table, *body* returns its body.                                                                                                                                                                  | | | | |
| [20]                                                                                                                                                                                                     | `datatype`      | : | `{ h:Set((ColumnName, Datatype)) } → { c:ColumnName \| ∃ d, (c,d) ∈ h } → { d:Datatype \| (c,d) ∈ h }`                                                                                                   |  |
| Given a header and a column in this header, *datatype* returns the datatype associated with this column.                                                                                                 | | | | |
| [21]                                                                                                                                                                                                     | `table`         | : | `{ r:Row } → { t:Table \| r ∈ t }`                                                                                                                                                                       |  |
| Given a row, *table* returns the table to which this row belongs.                                                                                                                                        | | | | |
| [22]                                                                                                                                                                                                     | `value`         | : | `{ r:Row } → { a:ColumnName \| a ∈ r } → CellValue`                                                                                                                                                      |  |
| Given a row and a column in this row, *value* returns the cell value (can be NULL) for this column.                                                                                                      | | | | |
| [23]                                                                                                                                                                                                     | `dereference`   | : | `{ r:Row } → { fk:ForeignKey \| fk ∈ foreignKeys(table(r)) }  										→ { targetRow:Row \| let (columnNames, targetTable, ck) = fk in  										                    targetRow ∈ body(targetTable) `   `and ∀ cifk ∈ columnNames, ∀ cjck ∈ ck,  										                        ∀ (ckr, vkr) ∈ r, ∀ (cltarget, vltarget) ∈ targetRow,  										                        i = j → cifk = ckr → cjck = cltarget → vkr = vltarget }` |  |
| Given a row and a foreign key from the table containing this row, *dereference* returns the row which is referenced by this foreign key, i.e. the row for which the values of the foreign key's <unique column list> are *all* equivalent (by the SQL `=` operator) to the values for the foreign key's <column name list> in the referring table. | | | | |

### A.3 RDF Data Model

Per [RDF Concepts and Abstract Syntax](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#section-rdf-graph), an RDF graph is a set of triples of a subject, predicate and object. The subject may be an IRI or a blank node, the predicate must be an IRI and the object may be an IRI, blank node, or an RDF literal.

This section recapitulates for convience the formal definition of RDF.

| [24]                                                                                                                                                                                                     | `Graph`        | ::= | `Set(Triple)`                                            |  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --- | -------------------------------------------------------- | --- |
| [24]                                                                                                                                                                                                     | `Graph`        | ::= | `{ Triple }`                                             |  |
| An *[RDF graph](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-rdf-graph)* is a set of RDF triples.                                                                                           | | | | |
| [25]                                                                                                                                                                                                     | `Triple`       | ::= | `(Subject, Predicate, Object)`                           |  |
| [25]                                                                                                                                                                                                     | `Triple`       | ::= | `( Subject, Predicate, Object )`                         |  |
| An *[RDF triple](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-rdf-triple)* is composed of a subject, predicate and object.                                                                  | | | | |
| [26]                                                                                                                                                                                                     | `Subject`      | ::= | `IRI \| BlankNode`                                       |  |
| [26]                                                                                                                                                                                                     | `Subject`      | ::= | `IRI \| BlankNode`                                       |  |
| A *[subject](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-subject)* is either an IRI or a blank node.                                                                                       | | | | |
| [27]                                                                                                                                                                                                     | `Predicate`    | ::= | `IRI`                                                    |  |
| [27]                                                                                                                                                                                                     | `Predicate`    | ::= | `IRI`                                                    |  |
| A *[predicate](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-predicate)* is always an IRI.                                                                                                   | | | | |
| [28]                                                                                                                                                                                                     | `Object`       | ::= | `IRI \| BlankNode \| Literal`                            |  |
| [28]                                                                                                                                                                                                     | `Object`       | ::= | `IRI \| BlankNode \| Literal`                            |  |
| An *[object](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-object)* is either an IRI, a blank node, or a literal.                                                                            | | | | |
| [29]                                                                                                                                                                                                     | `BlankNode`    | ::= | `RDF blank node`                                         |  |
| [29]                                                                                                                                                                                                     | `BlankNode`    | ::= | `RDF blank node`                                         |  |
| A *[blank node](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-blank-node)* is an arbitrary term used only to establish graph connectivity.                                                   | | | | |
| [30]                                                                                                                                                                                                     | `Literal`      | ::= | `PlainLiteral \| TypedLiteral`                           |  |
| [30]                                                                                                                                                                                                     | `Literal`      | ::= | `PlainLiteral \| TypedLiteral`                           |  |
| A *[literal](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-literal)* is either a plain literal or a typed literal.                                                                           | | | | |
| [31]                                                                                                                                                                                                     | `PlainLiteral` | ::= | `lexicalForm \| (lexicalForm, langageTag)`               |  |
| [31]                                                                                                                                                                                                     | `PlainLiteral` | ::= | `(lexicalForm) \| (lexicalForm, langageTag)`             |  |
| A *[plain literal](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-plain-literal)* has a [lexical form](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-lexical-form) and an optional [language tag](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-language-identifier). | | | | |
| [32]                                                                                                                                                                                                     | `TypedLiteral` | ::= | `(lexicalForm, IRI)`                                     |  |
| [32]                                                                                                                                                                                                     | `TypedLiteral` | ::= | `(lexicalForm, IRI)`                                     |  |
| An *[typed literal](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-typed-literal)* is composed of [lexical form](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-lexical-form) and a [datatype IRI](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-datatype-URI). | | | | |
| [33]                                                                                                                                                                                                     | `IRI`          | ::= | `RDF URI-reference as subsequently restricted by SPARQL` |  |
| [33]                                                                                                                                                                                                     | `IRI`          | ::= | `RDF URI-reference as subsequently restricted by SPARQL` |  |
| An *[IRI](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-URI-reference)* is an [RDF URI reference](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-URI-reference) as subsequently [restricted by SPARQL](https://www.w3.org/TR/rdf-sparql-query/#docTerminology). | | | | |
| [34]                                                                                                                                                                                                     | `lexicalForm`  | ::= | `a Unicode String`                                       |  |
| [34]                                                                                                                                                                                                     | `lexicalForm`  | ::= | `a Unicode String`                                       |  |
| SQL string representing a value.                                                                                                                                                                         | | | | |

### A.4 Denotational semantics

In this model, Databases are inhabitants of RDB (§A.2) and they are denoted by mathematical objects living in the RDF domain (§A.3). This *denotational semantics* is what we call the *Direct Mapping*.

The url-encoding function renders strings in a form suitable to insert into IRIs.
Data values are expressed in the XML Schema canonical form before url-encoding.

| [35]                                                                                                                                                                                                     | `ue`          | : | `String → String`                                                                      |  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --- | -------------------------------------------------------------------------------------- | --- |
| [35]                                                                                                                                                                                                     | `UE(s)`       | = | s percent-encoded.    |  |
| Replace the string with the [IRI-safe](https://www.w3.org/TR/2012/REC-r2rml-20120927/#dfn-iri-safe) form per section 7.3 of [R2RML](https://www.w3.org/TR/rdb-direct-mapping/#R2RML).                  | | | | |
|                                                                                                                                                                                                          | `⟦ ,  ⟧canon` | : | `(Row, Column) → String`                                                               |  |
| [36]                                                                                                                                                                                                     | `⟦r, c⟧canon` | = | `let v = value(r, c) in `   `let d = header(table(r)) in  canonical RDF literal(v, d)` |  |
| [36]                                                                                                                                                                                                     | `canon(A)`    | = | `canonical RDF literal(A)`                                                             |  |
| lexical form of the [canonical RDF literal](https://www.w3.org/TR/2012/REC-r2rml-20120927/#dfn-canonical-rdf-lexical-form) representation of the column value as defined in [R2RML section 10.2 Natural Mapping of SQL Values](https://www.w3.org/TR/2012/REC-r2rml-20120927/#natural-mapping) [R2RML](https://www.w3.org/TR/rdb-direct-mapping/#R2RML) | | | | |

Most of the functions defining the Direct Mapping are higher-order functions parameterized by a function φ(r) row node(r) which maps any row to a unique IRI or Blank Node.

| [37]                                                                                                                                                                                                     | `φ`                             | : | `∀ db:Database, ∀ r:Row, r ∈ db `   `if primaryKey(table(r)) ≠ ∅ then  ue(tablename(table(r))) + '/' + ue(c0) + '=' + ue(canon(r, c0)) + ';'  									    + ⋯ + ';' + ue(cn-1) + '=' + ue(canon(r, cn-1)) `   `else  									    a BlankNode unique to r` |  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| [37]                                                                                                                                                                                                     | `row_node`                      | = | `if (pk(R) ≠ ∅) then  IRI(UE(R.name) + "/" + (join(';', UE(A.name) + '=' + UE(canon(A))) ∣ A ∈ As )) `   `else  									    a BlankNode unique to r`                                                    |  |
| If the table has a primary key, the row node is a relative IRI obtained by concatenating: the percent-encoded form of the table name, the SOLIDUS character '/', for each column in the primary key, in order: the percent-encoded form of the column name, a EQUALS SIGN character '=', the percent-encoded lexical form of the [canonical RDF literal](https://www.w3.org/TR/2012/REC-r2rml-20120927/#dfn-canonical-rdf-lexical-form) representation of the column value as defined in [R2RML section 10.2 Natural Mapping of SQL Values](https://www.w3.org/TR/2012/REC-r2rml-20120927/#natural-mapping), if it is not the last column in the primary key, a SEMICOLON character ';'  If the table has no primary key, the row node is a fresh blank node that is unique to this row. | | | | |
|                                                                                                                                                                                                          | `⟦ ⟧tableIRI`                   | : | `TableName → IRI`                                                                                                                                                                                        |  |
| [38]                                                                                                                                                                                                     | `⟦t⟧tableIRI`                   | = | ue(tablename(t))                                                               |  |
| [38]                                                                                                                                                                                                     | `table_IRI(R)`                  | = | `IRI(R.name)`                                                                                                                                                                                            |  |
| the relative IRI consisting of the percent-encoded form of the table name.                                                                                                                               | | | | |
|                                                                                                                                                                                                          | `⟦ ,  ⟧litcol`                  | : | `(Row, Column) → IRI`                                                                                                                                                                                    |  |
| [39]                                                                                                                                                                                                     | `⟦r, c⟧litcol`                  | = | `ue(tablename(table(r))) + '#' + ue(c))`                                                                                                                                                                 |  |
| [39]                                                                                                                                                                                                     | `literal_property_IRI(R, A)`    | = | `IRI(UE(R.name) + "#" + UE(A.name))`                                                                                                                                                                     |  |
| the concatenation of: the percent-encoded form of the table name, the hash character '#', the percent-encoded form of the column name.                                                                   | | | | |
|                                                                                                                                                                                                          | `⟦ ,   ⟧refcol`                 | : | `(Row, ForeignKey) → IRI`                                                                                                                                                                                |  |
| [40]                                                                                                                                                                                                     | `⟦r, fk⟧refcol`                 | = | `let(from*, reftable, to*) = fk in  ue(tablename(table(r))) + '/ref-'  									+ ue(from0) + ';' + ⋯ + ';' + ue(fromn-1)`                                                                               |  |
| [40]                                                                                                                                                                                                     | `reference_property_IRI(R, As)` | = | `IRI(UE(R.name) + "#ref-" + join(';', UE(A.name)) ∣ A ∈ As )`                                                                                                                                            |  |
| the concatenation of: the percent-encoded form of the table name, the string '#ref-', for each column in the foreign key, in order: the percent-encoded form of the column name, if it is not the last column in the foreign key, a SEMICOLON character ';' | | | | |

The Direct Mapping is defined by [induction](https://en.wikipedia.org/wiki/Mathematical_induction) on the structure of RDB. Thus it is defined for any relational database. The entry point for the Direct Mapping is the function `⟦ ⟧φdatabase` direct graph(r).

|                                                                                                                                                                                                          | `⟦  ⟧φdatabase`           | : | `Database → Graph`                                                                                                                                                                                       |  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| [41]                                                                                                                                                                                                     | `⟦db⟧φdatabase`           | = | `{ triple \| triple ∈ ⟦t⟧φtable \| t ∈ db }`                                                                                                                                                             |  |
| [41]                                                                                                                                                                                                     | `direct_graph()`          | = | `{ table_graph(R) ∣ R ∈ DB }`                                                                                                                                                                            |  |
| the union of the table graphs for each table in a database schema.                                                                         | | | | |
|                                                                                                                                                                                                          | `⟦ ⟧φtable`               | : | `Table → Set(Triple)`                                                                                                                                                                                    |  |
| [42]                                                                                                                                                                                                     | `⟦t⟧φtable`               | = | `{ triple \| triple ∈ ⟦r⟧φrow \| r ∈ body(t) }`                                                                                                                                                          |  |
| [42]                                                                                                                                                                                                     | `table_graph(R)`          | = | `{ row_graph(T, R) ∣ T ∈ R.Body }`                                                                                                                                                                       |  |
| the union of the row graphs for each row in a table.                                                                                         | | | | |
|                                                                                                                                                                                                          | `noNULLs`                 | : | `Row → ForeignKey → Boolean`                                                                                                                                                                             |  |
| [43]                                                                                                                                                                                                     | `noNULLs(r, fk)`          | = | `let (columnNames, _, _) = fk in  									∀ c ∈ columnNames, value(r, c) ≠ NULL`                                                                                                                        |  |
| [43]                                                                                                                                                                                                     | `noNULLs(T, As)`          | = | `∄(T(A) = Null ∣ A ∈ As)`                                                                                                                                                                                |  |
|                                                                                                                                                                                                          | `⟦ ⟧φrow`                 | : | `Row → Set(Triple)`                                                                                                                                                                                      |  |
| [44]                                                                                                                                                                                                     | `⟦r⟧φrow`                 | = | `let s = φ(r) in  									  { ⟦r⟧φtype }  									⋃ { ⟦r, c⟧φlex \| value(r, c) ≠ NULL \| c ∈ lexicals(r) }  									⋃ { ⟦r, fk⟧φref \| noNULLs(r, fk) \| fk ∈ foreignKeys(table(r)) }`               |  |
| [44]                                                                                                                                                                                                     | `row_graph(T, R)`         | = | `  { type_triple(R) }  									∪ { literal_triple(R, A) ∣ A ≠ Null ∧ [A] ∉ R.ForeignKeys(T) }  									∪ { reference_triple(As, T) ∣ noNULLs(T, As) ∧ As ≠ R.PrimaryKey ∣ As ∈ R.ForeignKeys(T)`       |  |
| an RDF graph consisting of the following triples: the row type triple. a reference triple for each <column name list> in a table's foreign keys where none of the column values is NULL. a literal triple for each column in a table where the column value is non-NULL. | | | | |
|                                                                                                                                                                                                          | `⟦ ⟧type`                 | : | `(Row) → Triple`                                                                                                                                                                                         |  |
| [45]                                                                                                                                                                                                     | `⟦r⟧type`                 | = | `let s = φ(r) in `   `let t = table(r) in `   `let o = ⟦t⟧tableIRI in  									{ (s, rdf:type, o) }`                                                                                                    |  |
| [45]                                                                                                                                                                                                     | `type_triple(R)`          | = | `triple(row node(R), rdf:type, table-IRI(R))`                                                                                                                                                            |  |
| an RDF triple with: subject: the row node for the row. predicate: the RDF IRI `rdf:type`. object: the table IRI for the table name. | | | | |
|                                                                                                                                                                                                          | `⟦ ,  ⟧lex`               | : | `(Row, Column) → Triple`                                                                                                                                                                                 |  |
| [46]                                                                                                                                                                                                     | `⟦r, c⟧lex`               | = | `let s = φ(r) in `   `let p = ⟦table(r), c⟧litcol in `   `let v = value(r, c) in `   `let d = header(table(r)) in `   `if v is NULL then ∅ `   `else let o = natural RDF literal(v, d) in  									     { (s, p, o) }` |  |
| [46]                                                                                                                                                                                                     | `literal_triple(R, A)`    | = | `triple(row node(R), literal_property_IRI(R, [A]), natural RDF literal(A))`                                                                                                                              |  |
| an RDF triple with: subject: the row node for the row. predicate: the literal property IRI for the column. object: the [R2RML natural RDF literal](https://www.w3.org/TR/2012/REC-r2rml-20120927/#dfn-natural-rdf-literal) representation of the column value as defined in [R2RML section 10.2 Natural Mapping of SQL Values](https://www.w3.org/TR/2012/REC-r2rml-20120927/#natural-mapping). | | | | |
|                                                                                                                                                                                                          | `⟦ ,   ⟧ref`              | : | `(Row, ForeignKey) → Triple`                                                                                                                                                                             |  |
| [47]                                                                                                                                                                                                     | `⟦r, fk⟧ref`              | = | `let s = φ(r) in `   `let targetSpec = dereference(r, fk) in `   `let p = ⟦table(r), fk⟧refcol in `   `let o = φ(row(targetSpec)) in  									(s, p, o)`                                                |  |
| [47]                                                                                                                                                                                                     | `reference_triple(R, As)` | = | `triple(row node(R), reference_property_IRI(R, As), row_node(row referenced by (R, As)))`                                                                                                                |  |
| an RDF triple with: subject: the row node for the row. predicate: the reference property IRI for the columns. object: the row node for the referenced row. | | | | |

## B Direct Mapping as Rules (Informative)

In this section, we formally present the Direct Mapping as rules in Datalog syntax, inspired by the previous approaches in [SQL2SW](https://www.w3.org/TR/rdb-direct-mapping/#SQL2SW) [DMSurvey](https://www.w3.org/TR/rdb-direct-mapping/#DMSurvey). The left hand side of each rule is the RDF Triple output. The right hand side of each rule consists of a sequence of predicates from the relational database and built-in predicates. The built-in predicates are divided into four groups. The first group contains some built-in predicates for dealing with repeated rows in a table without a primary key.

- card(r, l, k): Given a table name r without a primary key and the list l of values [v1, ..., vn] for a row of table r, it returns in k the multiplicity of l in r (that is, k is the number of times row l appears in r)
- n ≤ m: This is the usual order on positive integer values (given positive integers n and m, it holds if n is smaller than or equal to m)

The second group contains a predicate to deal with null values.

- nonNull(v): Given a value v, it holds if v is not null

The third group of built-in predicates is used to generate IRIs for identifying tables and the columns in a table, and to generate IRIs or blank nodes for identifying each row in a table.

- generateTableIRI(r, i): Given a table name r, it generates the table IRI i of r
- generateLiteralPropertyIRI(r, a, i): Given a table name r and an attribute name a, it generates the literal property IRI i for a
- generateReferencePropertyIRI(r, l, i): Given a table name r and a non-empty list of columns l, it generates the reference property IRI i for l
- generateRowIRI(r, l1, l2, i): Given a table name r, a non-empty list l1 of columns and a non-empty list l2 of values (for the columns in l1), it generates the row node (or Row IRI) i for the given row
- generateRowBlankNode(r, l, n, i): Given a table name r without a primary key, a list l of values for a row of table r and a positive integer n, it generates the row node i for the n-th occurrence of row l in r (which is a [Blank Node](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/#dfn-blank-node) in this case). It is assumed that n is smaller than or equal to the multiplicity of l in r (that is, if card(r, l, k) holds, then 1 ≤ n ≤ k)

Finally, the fourth group of built-in predicates is used to generate typed literals.

- generateTypedLiteral(u, a, r, v): Given a value u, an attribute name a and a table name r, it generates an [R2RML natural RDF literal](https://www.w3.org/TR/2012/REC-r2rml-20120927/#dfn-natural-rdf-literal) v representation of the column value u, given the type of a in r and as defined in [R2RML section 10.2 Natural Mapping of SQL Values](https://www.w3.org/TR/2012/REC-r2rml-20120927/#natural-mapping).

Throughout the section, boxes containing Direct Mapping rules and examples will appear.
These boxes are color-coded. Yellow boxes contain Direct Mapping rules:

```
This box contains a Direct Mapping rule

```

Green boxes contain examples of applying the previous Direct Mapping rule:

```
This box contains examples of applying a Direct Mapping rule

```

Consider again the example from Section §2.1 Direct Mapping Example. It should be noticed that in the rules presented in this section, a formula of the form Addresses(X, Y, Z) indicates that the variables X, Y and Z are used to store the values of a row in the three columns of the table Addresses (according to the order specified in the schema of the table, that is, X, Y and Z store the values of ID, city and state, respectively). In particular, uppercase letters like X, Y, Z, S, P and O are used to denote variables. Moreover, double quotes are used in the rules to refer to the string with the name of a table or a column. For example, a formula of the form generateRowIRI("Addresses", ["ID"], [X], S) is used to generate the row node (or Row IRI) for the row of table "Addresses" whose value in the primary key "ID" is the value stored in the variable X. The value of this Row IRI is stored in the variable S.

### B.1 Generating Row Type Triples

#### B.1.1 Table has a primary key

Assume that r is a table with columns a1, ..., am and such that [ap1, ..., apn] is the primary key of r, where 1 ≤ n ≤ m and 1 ≤ p1 < ... < pn ≤ m. Then the following is the direct mapping rule to generate row type triples from r:

```
Triple(S, "rdf:type", O) ← r(X1, ..., Xm), generateRowIRI("r", ["ap1", ..., "apn"], [Xp1, ..., Xpn], S), generateTableIRI("r", O)

```

For example, table *Addresses* in the §2.1 Direct Mapping Example has columns *ID*, *city* and *state*, and it has column *ID* as its primary key. Then the following is the direct mapping rule to generate row type triples from *Addresses*:

```
Triple(S, "rdf:type", O) ← Addresses(X1, X2, X3), generateRowIRI("Addresses", ["ID"], [X1], S), generateTableIRI("Addresses", O)

```

As a second example, consider table *Department* from the example in Section §2.2 Foreign keys referencing candidate keys, which has columns *ID*, *name*, *city* and *manager*, and assume that (*name*, *city*) is the multi-column primary key of this table (instead of *ID*). Then the following is the direct mapping rule to generate row type triples from *Department*:

```
Triple(S, "rdf:type", O) ← Department(X1, X2, X3, X4), generateRowIRI("Department", ["name","city"], [X2, X3], S),
                            generateTableIRI("Department", O)

```

#### B.1.2 Table does not have a primary key

Assume that r is a table with columns a1, ..., am and such that r does not have a primary key. Then the following is the direct mapping rule to generate row type triples from r:

```
Triple(S, "rdf:type", O) ← r(X1, ..., Xm), card("r", [X1, ..., Xm], U), V ≤ U, generateRowBlankNode("r", [X1, ..., Xm], V, S),
                            generateTableIRI("r", O)

```

For example, table *Tweets* from Section §2.4 Empty (non-existent) primary keys has columns *tweeter*, *when* and *text*, and it does not have a primary key. Then the following is the direct mapping rule to generate row type triples from *Tweets*:

```
Triple(S, "rdf:type", O) ← Tweets(X1, X2, X3), card("Tweets", [X1, X2, X3], U), V ≤ U, generateRowBlankNode("Tweets", [X1, X2, X3], V, S),
                            generateTableIRI("Tweets", O)

```

### B.2 Generating Literal Triples

#### B.2.1 Table has a primary key

Assume that r is a table with columns a1, ..., am and such that [ap1, ..., apn] is the primary key of r, where 1 ≤ n ≤ m and 1 ≤ p1 < ... < pn ≤ m. Then for every aj (1 ≤ j ≤ m), the direct mapping includes the following rule for r and aj to generate literal triples:

```
Triple(S, P, V) ← r(X1, ..., Xm), nonNull(Xj), generateRowIRI("r", ["ap1", ..., "apn"], [Xp1, ..., Xpn], S),
                   generateLiteralPropertyIRI("r", "aj", P), generateTypedLiteral(Xj, "aj", "r", V)

```

For example, table *Addresses* in the §2.1 Direct Mapping Example has columns *ID*, *city* and *state*, and it has column *ID* as its primary key. Then the following are the direct mapping rules to generate literal triples from *Addresses*:

```
Triple(S, P, V) ← Addresses(X1, X2, X3), nonNull(X1), generateRowIRI("Addresses", ["ID"], [X1], S),
                   generateLiteralPropertyIRI("Addresses", "ID", P), generateTypedLiteral(X1, "ID", "Addresses", V)
Triple(S, P, V) ← Addresses(X1, X2, X3), nonNull(X2), generateRowIRI("Addresses", ["ID"], [X1], S),
                   generateLiteralPropertyIRI("Addresses", "city", P), generateTypedLiteral(X2, "city", "Addresses", V)
Triple(S, P, V) ← Addresses(X1, X2, X3), nonNull(X3), generateRowIRI("Addresses", ["ID"], [X1], S),
                   generateLiteralPropertyIRI("Addresses", "state", P), generateTypedLiteral(X3, "state", "Addresses", V)
```

As a second example, consider again table *Department* from the example in Section §2.2 Foreign keys referencing candidate keys, which has columns *ID*, *name*, *city* and *manager*, and assume that (*name*, *city*) is the multi-column primary key of this table (instead of *ID*). Then the following are the direct mapping rules to generate literal triples from *Department*:

```
Triple(S, P, V) ← Department(X1, X2, X3, X4), nonNull(X1), generateRowIRI("Department", ["name", "city"], [X2, X3], S),
                   generateLiteralPropertyIRI("Department", "ID", P), generateTypedLiteral(X1, "ID", "Department", V)
Triple(S, P, V) ← Department(X1, X2, X3, X4), nonNull(X2), generateRowIRI("Department", ["name", "city"], [X2, X3], S),
                   generateLiteralPropertyIRI("Department", "name", P), generateTypedLiteral(X2, "name", "Department", V)
Triple(S, P, V) ← Department(X1, X2, X3, X4), nonNull(X3), generateRowIRI("Department", ["name", "city"], [X2, X3], S),
                   generateLiteralPropertyIRI("Department", "city", P), generateTypedLiteral(X3, "city", "Department", V)
Triple(S, P, V) ← Department(X1, X2, X3, X4), nonNull(X4), generateRowIRI("Department", ["name", "city"], [X2, X3], S),
                   generateLiteralPropertyIRI("Department", "manager", P), generateTypedLiteral(X4, "manager", "Department", V)

```

#### B.2.2 Table does not have a primary key

Assume that r is a table with columns a1, ..., am and such that r does not have a primary key. Then for every aj (1 ≤ j ≤ m), the direct mapping includes the following rule for r and aj to generate literal triples:

```
Triple(S, P, V) ← r(X1, ..., Xm), nonNull(Xj), card("r", [X1, ..., Xm], U), V ≤ U, generateRowBlankNode("r", [X1, ..., Xm], V, S),
                   generateLiteralPropertyIRI("r", "aj", P), generateTypedLiteral(Xj, "aj", "r", V)

```

For example, table *Tweets* from Section §2.4 Empty (non-existent) primary keys has columns *tweeter*, *when* and *text*, and it does not have a primary key. Then the following are the direct mapping rules to generate literal triples from *Tweets*:

```
Triple(S, P, V) ← Tweets(X1, X2, X3), nonNull(X1), card("Tweets", [X1, X2, X3], U), V ≤ U, generateRowBlankNode("Tweets", [X1, X2, X3], V, S),
                   generateLiteralPropertyIRI("Tweets", "tweeter", P), generateTypedLiteral(X1, "tweeter", "Tweets", V)
Triple(S, P, V) ← Tweets(X1, X2, X3), nonNull(X2), card("Tweets", [X1, X2, X3], U), V ≤ U, generateRowBlankNode("Tweets", [X1, X2, X3], V, S),
                   generateLiteralPropertyIRI("Tweets", "when", P), generateTypedLiteral(X2, "when", "Tweets", V)
Triple(S, P, V) ← Tweets(X1, X2, X3), nonNull(X3), card("Tweets", [X1, X2, X3], U), V ≤ U, generateRowBlankNode("Tweets", [X1, X2, X3], V, S),
                   generateLiteralPropertyIRI("Tweets", "text", P), generateTypedLiteral(X3, "text", "Tweets", V)

```

### B.3 Generating Reference Triples

For each foreign key from a table r1 to a table r2, one of the following four cases is applied.

#### B.3.1 Table r1 has a primary key and table r2 has a primary key

Assume that:

- r1 is a table with columns a1, ..., ai and such that [ap1, ..., apj] is the primary key of r1, where 1 ≤ j ≤ i and 1 ≤ p1 < ... < pj ≤ i

- r2 is a table with columns c1, ..., ck and such that [cq1, ..., cqm] is the primary key of r2, where 1 ≤ m ≤ k and 1 ≤ q1 < ... < qm ≤ k

- the foreign key indicates that the columns as1, ..., asn of r1 reference the columns ct1, ..., ctn of r2, where (1) 1 ≤ s1, ..., sn ≤ i, (2) 1 ≤ t1, ..., tn ≤ k, and (3) n ≥ 1

Then the direct mapping includes the following rule for r1 and r2 to generate Reference Triples:

```
Triple(S, P, O) ← r1(X1, ..., Xi), generateRowIRI("r1", ["ap1", ..., "apj"], [Xp1, ..., Xpj], S),
                   r2(Y1, ..., Yk), generateRowIRI("r2", ["cq1", ..., "cqm"], [Yq1, ..., Yqm], O),
                   nonNull(Xs1), ..., nonNull(Xsn), Xs1 = Yt1, ...,  Xsn = Ytn,  generateReferencePropertyIRI("r1", ["as1", ..., "asn"], P)

```

For example, table *Addresses* in the §2.1 Direct Mapping Example has columns *ID*, *city* and *state*, where column *ID* is the primary key. Table *People* in this example has columns *ID*, *fname* and *addr*, where column *ID* is the primary key, and it has a foreign key in the column *addr* that references the column *ID* in the table *Addresses*. In this case, the following is the direct mapping rule to generate Reference Triples:

```
Triple(S, P, O) ← People(X1, X2, X3), generateRowIRI("People", ["ID"], [X1], S),
                   Addresses(Y1, Y2, Y3), generateRowIRI("Addresses", ["ID"], [Y1], O),
                   nonNull(X3), X3 = Y1,  generateReferencePropertyIRI("People", ["addr"], P)

```

#### B.3.2 Table r1 has a primary key and table r2 does not have a primary key

Assume that:

- r1 is a table with columns a1, ..., ai and such that [ap1, ..., apj] is the primary key of r1, where 1 ≤ j ≤ i and and 1 ≤ p1 < ... < pj ≤ i

- r2 is a table with columns c1, ..., ck, and it does not have a primary key

- the foreign key indicates that the columns as1, ..., asn of r1 reference the columns ct1, ..., ctn of r2, where (1) 1 ≤ s1, ..., sn ≤ i, (2) 1 ≤ t1, ..., tn ≤ k, and (3) n ≥ 1

Then the direct mapping includes the following rule for r1 and r2 to generate Reference Triples:

```
Triple(S, P, O) ← r1(X1, ..., Xi), generateRowIRI("r1", ["ap1", ..., "apj"], [Xp1, ..., Xpj], S),
                   r2(Y1, ..., Yk), card("r2", [Y1, ..., Yk], U), V ≤ U, generateRowBlankNode("r2", [Y1, ..., Yk], V, O),
                nonNull(Xs1), ..., nonNull(Xsn), Xs1 = Yt1, ...,  Xsn = Ytn,  generateReferencePropertyIRI("r1", ["as1", ..., "asn"], P)

```

For example, assume that table *Addresses* in the §2.1 Direct Mapping Example has columns *ID*, *city* and *state*, and that column *ID* is a candidate key (instead of a primary key), so that table *Addresses* does not have a primary key. Moreover, assume that table *People* in this example has columns *ID*, *fname* and *addr*, it has column *ID* as its primary key, and it has a foreign key in the column *addr* to the candidate key *ID* in the table *Addresses*. In this case, the following is the direct mapping rule to generate Reference Triples:

```
Triple(S, P, O) ← People(X1, X2, X3), generateRowIRI("People", ["ID"], [X1], S),
                   Addresses(Y1, Y2, Y3), card("Addresses", [Y1, Y2, Y3], U), V ≤ U, generateRowBlankNode("Addresses", [Y1, Y2, Y3], V, O),
                   nonNull(X3), X3 = Y1,  generateReferencePropertyIRI("People", ["addr"], P)

```

#### B.3.3 Table r1 does not have primary key and table r2 has a primary key

Assume that:

- r1 is a table with columns a1, ..., ai, and it does not have a primary key

- r2 is a table with columns c1, ..., ck and such that [cq1, ..., cqm] is the primary key of r2, where 1 ≤ m ≤ k and 1 ≤ q1 < ... < qm ≤ k

- the foreign key indicates that the columns as1, ..., asn of r1 reference the columns ct1, ..., ctn of r2, where (1) 1 ≤ s1, ..., sn ≤ i, (2) 1 ≤ t1, ..., tn ≤ k, and (3) n ≥ 1

Then the direct mapping includes the following rule for r1 and r2 to generate Reference Triples:

```
Triple(S, P, O) ← r1(X1, ..., Xi), card("r1", [X1, ..., Xi], U), V ≤ U, generateRowBlankNode("r1", [X1, ..., Xi], V, S),
                   r2(Y1, ..., Yk), generateRowIRI("r2", ["cq1", ..., "cqm"], [Yq1, ..., Yqm], O),
                   nonNull(Xs1), ..., nonNull(Xsn), Xs1 = Yt1, ...,  Xsn = Ytn,  generateReferencePropertyIRI("r1", ["as1", ..., "asn"], P)

```

For example, table *People* in the §2.1 Direct Mapping Example has columns *ID*, *fname* and *addr*, and it has column *ID* as its primary key, while table *Tweets* from Section §2.4 Empty (non-existent) primary keys has columns *tweeter*, *when* and *text*, it does not have a primary key, and it has a foreign key in column *tweeter* that references column *ID* in table *People*. In this case, the following is the direct mapping rule to generate Reference Triples:

```
Triple(S, P, O) ← Tweets(X1, X2, X3), card("Tweets", [X1, X2, X3], U), V ≤ U, generateRowBlankNode("Tweets", [X1, X2, X3], V, S),
                   People(Y1, Y2, Y3), generateRowIRI("People", ["ID"], [Y1], O),
                   nonNull(X1), X1 = Y1, generateReferencePropertyIRI("Tweets", ["tweeter"], P)

```

#### B.3.4 Table r1 does not have primary key and table r2 does not have a primary key

Assume that:

- r1 is a table with columns a1, ..., ai, and it does not have a primary key

- r2 is a table with columns c1, ..., ck, and it does not have a primary key

- the foreign key indicates that the columns as1, ..., asn of r1 reference the columns ct1, ..., ctn of r2, where (1) 1 ≤ s1, ..., sn ≤ i, (2) 1 ≤ t1, ..., tn ≤ k, and (3) n ≥ 1

Then the direct mapping includes the following rule for r1 and r2 to generate Reference Triples:

```
Triple(S, P, O) ← r1(X1, ..., Xi), card("r1", [X1, ..., Xi], U1), V1 ≤ U1, generateRowBlankNode("r1", [X1, ..., Xi], V1, S),
                   r2(Y1, ..., Yk), card("r2", [Y1, ..., Yk], U2), V2 ≤ U2, generateRowBlankNode("r2", [Y1, ..., Yk], V2, O),
                   nonNull(Xs1), ..., nonNull(Xsn), Xs1 = Yt1, ...,  Xsn = Ytn,  generateReferencePropertyIRI("r1", ["as1", ..., "asn"], P)

```

For example, assume that table *People* in the §2.1 Direct Mapping Example has columns *ID*, *fname* and *addr*, and that column *ID* is a candidate key (instead of a primary key), so that *People* does not have a primary key. Moreover, assume that table *Tweets* from Section §2.4 Empty (non-existent) primary keys has columns *tweeter*, *when* and *text*, it does not have a primary key, and it has a foreign in column *tweeter* that references candidate key *ID* in table *People*. In this case, the following is the direct mapping rule to generate Reference Triples:

```
Triple(S, P, O) ← Tweets(X1, X2, X3), card("Tweets", [X1, X2, X3], U1), V1 ≤ U1, generateRowBlankNode("Tweets", [X1, X2, X3], V1, S),
                   People(Y1, Y2, Y3), card("People", [Y1, Y2, Y3], U2), V2 ≤ U2, generateRowBlankNode("People", [Y1, Y2, Y3], V2, O),
                   nonNull(X1), X1 = Y1, generateReferencePropertyIRI("Tweets", ["tweeter"], P)

```
