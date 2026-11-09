---
title: "RML-IO"
source: https://w3id.org/rml/io/spec/
family: mapping
spec_date: 2026-03-16
fetched: 2026-11-09
---

# RML-IO

> Logical sources and targets for any input/output format (W3C CG draft).

## Contents

- Abstract
- 1 Conformance
- 2 Overview
- 3 Logical Source vocabulary
  - 3.1 Defining Logical Sources
    - 3.1.1 Reference formulations
  - 3.2 Source
    - 3.2.1 NULL values
    - 3.2.2 Compression formats
    - 3.2.3 Encoding formats
  - 3.3 Examples
- 4 Logical Target vocabulary
  - 4.1 Defining Logical Targets
  - 4.2 Target
    - 4.2.1 Serialization formats
    - 4.2.2 Mode
    - 4.2.3 Compression formats
    - 4.2.4 Encoding formats
    - 4.2.5 Relative paths
  - 4.3 Examples
- 5 Logical Source in RML
- 6 Logical Target in RML
- 7 Single targets
  - 7.1 Subject Map
  - 7.2 Predicate Map
  - 7.3 Object Map
  - 7.4 Graph Map
  - 7.5 Language Map
  - 7.6 Datatype Map
  - 7.7 Function Map
- 8 Combining multiple Targets
  - 8.1 Multiple Targets in the same Term Map
  - 8.2 Subject Map and Predicate Map
  - 8.3 Subject Map and Object Map
  - 8.4 Predicate Map and Object Map
  - 8.5 Subject Map, Predicate Map and Object Map
  - 8.6 Subject Map and Graph Map
  - 8.7 Predicate Map and Graph Map
  - 8.8 Object Map and Graph Map
  - 8.9 Language Map and Graph Map
  - 8.10 Language Map and Object Map
  - 8.11 Multiple Predicate Maps
  - 8.12 Multiple Object Maps
  - 8.13 Multiple Graph Maps
- 9 Overriding Targets
  - 9.1 Separate Triples Map
  - 9.2 Conditions
- A References
  - A.1 Normative references

---

## Abstract

This document describes *Logical Source* and *Logical Target* to access data sources and targets.

A *Logical Source* is a formal model and common representation
for describing access to data sources.
A *Logical Target* is
a formal model and a common representation
for specifying how a Knowledge Graph should be exported to a given target.

Logical Source and Logical Target reuses existing data access descriptions
and is therefore not limited to a specific set of targets or data sources.
The current document describes the Logical Source and Logical Target concepts
through definitions and examples.

The version of this document is *DRAFT*.

## 1. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY* and *MUST* in this document
are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all
capitals, as shown here.

## 2. Overview

*This section is non-normative.*

This document specifies *Logical Source* and *Logical Target*,
Logical Source is a description
for specifying how a data source should be accessed.
A Logical Source description is not limited to a specific Source
which allows to access any type of Source and provides a reference formulation
to refer to data inside the Source.

Logical Target is
a description for defining how a generated
RDF [RDF-Concepts]
knowledge graph must be exported.
A Logical Target description is not tailored towards a specific Target
which allows to export the generated RDF triples to any type of Target
and provides fine-grained control over where each RDF triple is exported to.

Logical Source and Logical Target leverage
the access descriptions of data access
such as DCAT [DCAT], SD [SD], etc.

In this document, examples assume
the following namespace prefix bindings unless otherwise stated:

| Prefix    | Namespace                                             |
| --------- | ----------------------------------------------------- |
| `rml`     | <http://w3id.org/rml/>                                |
| `formats` | <http://www.w3.org/ns/formats/>                       |
| `sd`      | <http://www.w3.org/ns/sparql-service-description#>    |
| `dcat`    | <http://www.w3.org/ns/dcat#>                          |
| `td`      | <https://www.w3.org/2019/wot/td#>                     |
| `hctl`    | <https://www.w3.org/2019/wot/hypermedia#>             |
| `htv`     | <http://www.w3.org/2011/http#>                        |
| `d2rq`    | <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> |
| `wotsec`  | <https://www.w3.org/2019/wot/security#>               |
| `idsa`    | <https://w3id.org/idsa/core/>                         |

The examples are contained in pink colored boxes:

```
# This box contains the example's Logical Source description.
```

```
# This box contains the example's Logical Target description.
```

## 3. Logical Source vocabulary

The Logical Source vocabulary namespace is <http://w3id.org/rml/> and its prefix is `rml`.

The Logical Source vocabulary consists of 2 classes:

1. `rml:LogicalSource` describes how data of a source can be referenced.
2. `rml:Source` describes how a source can be accessed, it referenced from a `rml:LogicalSource`.

### 3.1 Defining Logical Sources

A *Logical Source* is an [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) which specifies the access to a [data source](https://w3id.org/rml/core/spec#dfn-data-source) to be used as
input for a [Triples Map](https://w3id.org/rml/core/spec#dfn-triples-map).

An Logical Source (`rml:LogicalSource`) *MUST* adhere to the properties defined for the [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract=logical-source).

Furthermore, an Logical Source *MUST* have:

- exactly one **source** (`rml:source`) property which specifies how a [data source](https://w3id.org/rml/core/spec#dfn-data-source) is using a Source (`rml:Source`).

The [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) *MUST* be specified in
the case that the [data source](https://w3id.org/rml/core/spec#dfn-data-source) is a relational database,
CSV, TSV, XML, or JSON data sources.

By default `rml:SQL2008Query` for databases, `rml:CSV` for CSV and TSV data sources.
XPath for XML and JSONPath for JSON and JSONL data sources.

By default, the [iterator](https://w3id.org/rml/core/spec#dfn-iterator) is considered a row,
if not specified:

- In the case of CSV or TSV data sources, the value of `rml:iterator` is considered a "row" and must not be specified.
- In the case of XML and JSON data sources, it is a valid reference
  to an element or an object respectively considering the [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) specified.
- In the case of relational databases, the value of `rml:iterator` is either
  a SQL query (`rml:referenceFormulation rml:SQL2008Query`) or the SQL table
  name (`rml:referenceFormulation rml:SQL2008Table`). For SQL table names,
  they can be converted to a SQL query using the following SQL query template: `SELECT * FROM {table}` where `{table}` is the table name.

The Logical Source definition requires only the source (`rml:source`)
to be specified, all other properties are optional.
If a property is specified, it *MUST* only occur once.

| Property     | Domain              | Range |
| ------------ | ------------------- | ----- |
| `rml:source` | `rml:LogicalSource` | `IRI` |

![Logical Source structure](https://kg-construct.github.io/rml-io/spec/docs/resources/images/source-structure.png)

*Figure 1 The structure of Logical Source*

#### 3.1.1 Reference formulations

Each Logical Source has a [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) to define how
to express a reference to elements of the data of the input [data source](https://w3id.org/rml/core/spec#dfn-data-source).
Several [reference formulation](https://w3id.org/rml/core/spec#dfn-reference-formulation) (`rml:ReferenceFormulation`) are defined in this specification:

- `rml:CSV`: CSV or TSV data sources
- `rml:JSONPath`: JSON documents
- `rml:XPath`: XML documents with optionally
  the definition of XML namespaces used in references.
  By default, no namespaces are defined.
- `rml:SQL2008Query`: SQL query for a relational database.
- `rml:SQL2008Table`: Shortcut to select all columns from a SQL table.

`rml:XPath` may specify zero or more `rml:namespace` properties with a `rml:Namespace`.
A `rml:Namespace` contains the following required properties:

- `rml:namespacePrefix`: A Literal with the prefix used for the XML namespace.
- `rml:namespaceURL`: A Literal with the URL identifying the XML namespace.

These reference formulations are defined in the [RML-IO-Registry].

```
<#XMLNamespace> a rml:LogicalSource;
     rml:source [ a rml:Source, rml:FilePath;
         rml:path "/path/to/file/data.xml";
     ];
     rml:referenceFormulation [ a rml:XPathReferenceFormulation;
       rml:namespace [ a rml:Namespace;
         rml:namespacePrefix "ex";
         rml:namespaceURL "http://example.org";
       ];
     ];
     rml:iterator "/xpath/ex:namespace/expression";
.
```

Since `rml:source` is open to any IRI, you can implement your own source access
description for [data source](https://w3id.org/rml/core/spec#dfn-data-source) that are not
covered by existing vocabularies such as paginated Web APIs which implement pagination
in a Web API specific way.

### 3.2 Source

A *Source* (`rml:Source`) defines how a [data source](https://w3id.org/rml/core/spec#dfn-data-source) should be accessed.
It complements other source descriptions
such as SD Service, CSVW Table, DCAT Distribution, etc.
to support encoding, null values, compression, and other access properties.
The properties of a Source take precedence over the properties of other source
descriptions, for example: `rml:encoding` takes precedence over `csvw:encoding` if both are specified.

A Source *MUST* have the following properties:

- zero or one **`rml:encoding`** property, which specifies the encoding
  of the data inside the source. Defaults to `rml:UTF-8` if not specified.
- zero or more **`rml:null`** describes which data values inside the source
  should be considered as NULL.
  The value for this predicate defaults to the default NULL token
  of the underlying data model (e.g., NULL in relational databases
  and null in JSON) and are always processed as such.
  Some data models have no such default NULL token, such as CSV.
  When that is the case, then nothing is considered NULL unless specified by `rml:null`.
  Example: CSV does not have a default NULL character,
  so no value is considered NULL.
  However, JSON has a NULL character specified: `null`,
  this one is used together with the ones specified through `rml:null`.
  For a relational database, `rml:null "foo"` results into the following values
  considered as NULL: `{NULL, "foo"}` where `NULL` comes from the relational
  database model as NULL value.
- zero or one **`rml:compression`** specifies if the source is compressed
  and the used compression algorithm. Defaults to no compression.

```
<#JSON> a rml:LogicalSource;
     rml:source [ a rml:Source, rml:FilePath;
       rml:path "/path/to/data.json.gz";
       rml:null ""; # empty string as NULL besides default null character
       rml:compression rml:gzip; # GZip compression
       rml:encoding rml:UTF-16; # UTF-16 encoding
     ];
     rml:referenceFormulation rml:JSONPath;
     rml:iterator "$.jsonpath.expression";
.
```

| Property          | Domain       | Range             |
| ----------------- | ------------ | ----------------- |
| `rml:encoding`    | `rml:Source` | `rml:Encoding`    |
| `rml:null`        | `rml:Source` | `Literal`         |
| `rml:compression` | `rml:Source` | `rml:Compression` |

#### 3.2.1 NULL values

Each Source *MAY* describe the values that should be considered as NULL
with `rml:null`, similar to `NULL` in relational databases.
By default, standardized NULL values are always considered,
but additional ones can be specified. Multiple NULL values are allowed.
For example, in relational databases `NULL` is always considered as a NULL
value while also an empty column can be considered as a NULL value by
specifying it through `rml:null` in a Source.

#### 3.2.2 Compression formats

Each Source *MAY* specify the compression with `rml:compression` to apply when exporting RDF triples to a Source for saving storage space.
Several compression formats are defined:

- `rml:none`: No compression is applied
- `rml:gzip`: GZip compression
- `rml:zip`: Zip archive with Zip compression
- `rml:tarxz`: Tar archive with Xz compression
- `rml:targz`: Tar archive with GZip compression

If unspecified, the default value is no compression.
This namespace is NOT limited to the listed compression formats
and *MAY* be extended in the future.

#### 3.2.3 Encoding formats

Each Source *MAY* describe the encoding format to use when exporting
RDF triples to a Source. Several encoding formats are defined:

- `rml:UTF-8`: UTF-8 encoding
- `rml:UTF-16`: UTF-16 encoding

If unspecified, the default value is `rml:UTF-8`.
This namespace is NOT limited to the listed compression formats
and may be extended in the future.

### 3.3 Examples

The following example shows a Source of a CSV file.
RML-IO-Registry provides also support for CSVW which allows more fine-grained control
over CSV files such as delimeters, encoding, etc. but it is not required for
Processors to implement CSVW, only CSV is the minimum to be compliant with
the RML IO module.

```
<#CSV> a rml:LogicalSource;
     rml:source [ a rml:Source, rml:FilePath;
        rml:path "/path/to/data.csv";
        rml:null "NULL";
        rml:null "";
     ];
     rml:referenceFormulation rml:CSV;
.
```

Note that there is no `rml:iterator` present because its default is row.
This particular CSV file has two different ways to specify a NULL value: `NULL` or an empty value. Implementations need to check if a value is equal to one of
the values defined by `rml:null` to check for NULL values in the data.

The following example shows a Source specified for a MySQL database querying
the `student` table. The database username and password are provided as well.

```
<#RDB> a rml:LogicalSource;
    rml:source [ a rml:Source, d2rq:Database;
        d2rq:jdbcDSN "jdbc:mysrml://localhost/example";
        d2rq:jdbcDriver "com.mysql.jdbc.Driver";
        d2rq:username "user";
        d2rq:password "password";
    ];
    rml:iterator "SELECT * FROM student;";
    rml:referenceFormulation rml:SQL2008Query;
.
```

A shortcut is available to select all columns from a table,
such as in the example above, by using the `rml:SQL2008Table` as `rml:referenceFormulation`.

Relative paths to files are covered by a source access description included
in this specification which subclasses `rml:Source` as `rml:FilePath`.
This access description allows accessing files relative from:

- `rml:CurrentWorkingDirectory`: relative to the current working directory of the RML processor.
- `rml:MappingDirectory`: relative to the location of the RML mapping.
- A string Literal: a string describing an absolute path against which relative paths are resolved, similar to the Base URI in [RFC3986](https://www.rfc-editor.org/rfc/rfc3986).

If `rml:root` is not specified, it defaults to `rml:CurrentWorkingDirectory`.

| Property   | Domain         | Range                                                              |
| ---------- | -------------- | ------------------------------------------------------------------ |
| `rml:root` | `rml:FilePath` | `rml:CurrentWorkingDirectory`, `rml:MappingDirectory` or `Literal` |
| `rml:path` | `rml:FilePath` | `Literal`                                                          |

Example of accessing a CSV file relative to the current working directory.
The file's absolute path is `$CURRENT_WORKING_DIR/file.csv` where `$CURRENT_WORKING_DIR` is
the location of the RML mapping.

```
<#RelativePathCWD> a rml:LogicalSource;
  rml:source [ a rml:FilePath, rml:Source;
    rml:root rml:CurrentWorkingDirectory;
    rml:path "./file.csv";
  ];
.
```

Example of accessing a JSON file relative to the path of the mapping.
The file's absolute path is `$MAPPING_DIR/file.json` where `$MAPPING_DIR` is
the location of the RML mapping.

```
<#RelativePathMapping> a rml:LogicalSource;
  rml:source [ a rml:FilePath, rml:Source;
    rml:root rml:MappingDirectory;
    rml:path "./file.json";
  ];
  rml:referenceFormulation rml:JSONPath;
  rml:iterator "$";
.
```

Example of accessing an XML file relative to an absolute root path
specified by a string Literal. The file's absolute path is `/root/file.xml`.

```
<#RelativePathLiteral> a rml:LogicalSource;
  rml:source [ a rml:FilePath, rml:Source;
    rml:root "/root";
    rml:path "file.xml";
  ];
  rml:referenceFormulation rml:JSONPath;
  rml:iterator "$";
.
```

## 4. Logical Target vocabulary

The LogicalTarget vocabulary namespace is <http://w3id.org/rml/> and it's prefix is `rml`.

The LogicalTarget vocabulary consists of `rml:LogicalTarget` and `rml:Target` classes to describe how a knowledge graph must be exported after generation.

### 4.1 Defining Logical Targets

A Logical Target is any target to where RDF triples are exported to.

| Property     | Domain              | Range    |
| ------------ | ------------------- | -------- |
| `rml:target` | `rml:LogicalTarget` | `Target` |

- The target access description (`rml:target`) *MUST* specify how to access
  the target through an `rml:Target`.
  The Target definition requires only the target (`rml:target`) to be specified,
  all other properties are optional.

### 4.2 Target

A Target describes how a target must be accessed when exporting RDF triples.
An external vocabulary such as DCAT, SD, etc. is allowed here.
If a target cannot be accessed with existing vocabulary, a custom vocabulary
can be used, for example: handling an authentication flow may be specific
for that specific target. A custom ontology can be used here to describe
this authentication flow such as [W3C Web of Things Security](https://www.w3.org/2019/wot/security).

A Target (`rml:Target`) *MAY* contain the following properties:

- The **serialization format** (`rml:serialization`) *MAY* specify
  the serialization format for exporting a knowledge graph.
  The serialization format is described using the W3C [formats](http://www.w3.org/ns/formats/) namespace.
  By default, the serialization format is N-Quads [N-Quads].
- The **compression algorithm** (`rml:compression`) *MAY* describe
  the compression algorithm to apply when exporting a knowledge graph.
  By default, no compression is applied.
- The **encoding** (`rml:encoding`) *MAY* specify which encoding must be used
  when exporting a knowledge graph.
  By default, UTF-8 is used.

| Property            | Domain              | Range             |
| ------------------- | ------------------- | ----------------- |
| `rml:serialization` | `rml:LogicalTarget` | `formats:Format`  |
| `rml:mode`          | `rml:Target`        | `rml:Mode`        |
| `rml:compression`   | `rml:Target`        | `rml:Compression` |
| `rml:encoding`      | `rml:Target`        | `rml:Encoding`    |

![Logical Target structure](https://kg-construct.github.io/rml-io/spec/docs/resources/images/target-structure.png)

*Figure 2 The structure of Logical Target*

Logical Targets are the same if they are effectively equal as described in [RML-Core](https://kg-construct.github.io/rml-core/spec/docs/#dfn-effectively-equal).

#### 4.2.1 Serialization formats

Each Target *MAY* describe the serialization format
with `rml:serialization` to use when exporting RDF triples to a Target.
The possible formats are defined in the W3C [formats](http://www.w3.org/ns/formats/) namespace
such as N-Quads, N-Triples, JSON-LD, Turtle, etc.
If unspecified, the default format is N-Quads [N-Quads].

#### 4.2.2 Mode

Each Target *MAY* describe the operation mode when accessing a Target
with `rml:mode` to specify if the Target must be appended, overwritten, etc.
If not specified, defaults to `rml:Write`.
This property accepts the range of `rml:Mode`:

- `rml:Read`: read-only mode (`r`). Start beginning of file. Not useful for targets. File must exist.
- `rml:ReadWrite`: read-write mode (`r+`). Start beginning of file, no truncation. Only write part is useful for targets. File must exist.
- `rml:Write`: write mode (`w`). Truncate/create file and start at the beginning to add new data.
- `rml:WriteRead`: write-read mode (`w`). Truncate/create file and start at the beginning to add new data. Only write part is useful for targets
- `rml:Append`: append-only mode. Existing file is kept and new data is appended at the end. File is created if not exist.
- `rml:AppendRead`: append-read mode. Existing file is kept and new data is appended at the end. File is created if not exist.

#### 4.2.3 Compression formats

Each Target *MAY* specify the compression with `rml:compression` to apply when exporting RDF triples to a Target for saving storage space.
Several compression formats are specified by the `comp` namespace:

- `rml:none`: No compression is applied
- `rml:gzip`: GZip compression
- `rml:zip`: Zip archive with Zip compression
- `rml:tarxz`: Tar archive with Xz compression
- `rml:targz`: Tar archive with GZip compression

If unspecified, the default value is no compression.
This namespace is NOT limited to the listed compression formats
and *MAY* be extended in the future.

#### 4.2.4 Encoding formats

Each Target *MAY* describe the encoding format to use when exporting
RDF triples to a Target. Several encoding formats are defined:

- `rml:UTF-8`: UTF-8 encoding
- `rml:UTF-16`: UTF-16 encoding

If unspecified, the default value is UTF-8.
This namespace is NOT limited to the listed compression formats
and *MAY* be extended in the future.

#### 4.2.5 Relative paths

Relative paths to files are covered by a target access description included
in this specification which subclasses `rml:Target` as `rml:FilePath` re-used from the Logical Source.

### 4.3 Examples

The following example show a Target of an RDF dump in Turtle [Turtle]
format with GZip compression and UTF-8 encoding:

```
<#FileDump> a rml:LogicalTarget;
    rml:target [ a rml:Target, rml:FilePath;
        rml:path "/data/dump.ttl";
        rml:compression rml:gzip;
        rml:encoding rml:UTF-8;
    ];
    rml:serialization formats:Turtle;
.
```

## 5. Logical Source in RML

[RML-Core] introduces an [abstract logical source](https://w3id.org/rml/core/spec#dfn-abstract-logical-source) as an abstract construct to describe how a [data source](https://w3id.org/rml/core/spec#dfn-data-source) can be accessed to be used in a [Triples Map](https://w3id.org/rml/core/spec#dfn-triples-map).

In this specification we introduce the Logical Source to describe how an input [data source](https://w3id.org/rml/core/spec#dfn-data-source) can be accessed.

In the example below, a CSV file is transformed into a knowledge graph.
The CSV file is accessed using the [CSVW] vocabulary,
transformed into a knowledge graph using [RML] mappings,

```
id;name;nickname
0;Nathan Ford;Mastermind
1;Sophie Devereaux;Grifter
2;Eliot Spender;Hitter
3;Parker;Thief
4;Alec Hardison;Hacker
```

```
<#CSVSourceAccess> a rml:Source, rml:FilePath;
  rml:root rml:CurrentWorkingDirectory;
  rml:path "./Leverage.csv";
.
```

```
@base <http://example.com/ns#> .

<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#CSVSourceAccess>;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.com/{id}";
    rml:class foaf:Person;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname";
    ];
  ];
.
```

```
<http://example.org/0> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Nathan Ford" _b0 .
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Mastermind" _b0 .
<http://example.org/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Sophie Devereaux" _b0 .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Grifter" _b0 .
<http://example.org/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Eliot Spencer" _b0 .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Hitter" _b0 .
<http://example.org/3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Parker" _b0 .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Thief" _b0 .
<http://example.org/4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Alec Hardison" _b0 .
<http://example.org/4> <http://xmlns.com/foaf/0.1/nickname> "Hacker" _b0 .
```

## 6. Logical Target in RML

RML is aligned with the Logical Target vocabulary
by extending `rml:TermMap` with the `rml:logicalTarget` property
to describe on Term Map [RML] level where each triple must be directed to.
A Term Map is a function that generates an RDF term
from a logical reference [RML].
The result of that function is known as the term map's generated
RDF term [RDF-Concepts]
such as subjects, predicates, objects, named graphs and language tags.

Each RML processor has a default target where generated triples are exported.
Logical Targets provide a mechanism to override this default target for some
of the triples to be exported.

Logical Targets are defined in Term Maps. A Term Map *MAY* contain
one or more `rml:logicalTarget` properties to export all triples containing
the generated term to different targets. Specifically, when generating a
triple `t`, if any of the term maps involved in the generation of `t` contains a Logical Target `LT`, then triple `t` exported to target `LT`.
If none of those Term Maps contains a Logical Target,
then the triple `t` is sent to the default target of the RML processor.

Multiple Logical Targets *MAY* be combined by specifying multiple Logical Targets
in the same Term Map or multiple Term Maps of the same RDF triple
(Section 8. Combining multiple Targets (§8)).
Logical Targets *MAY* be overriden by using a separate Triples Map
or conditions [FnO] (Section 9. Overriding Targets (§9)).

If the mapping document contains no Targets,
the processor falls back to the default target,
as it is specified through the processor's
specific configuration file or command line parameters.
If a mapping document contains at least one Target,
the processor will export the triples to these Targets,
triples which do not have one or more Target(s) assigned,
are exported to the default target of the processor.

| Property            | Domain        | Range               |
| ------------------- | ------------- | ------------------- |
| `rml:logicalTarget` | `rml:TermMap` | `rml:LogicalTarget` |

In the example below, a CSV file is transformed into a knowledge graph.
The CSV file is accessed using the [CSVW] vocabulary,
transformed into a knowledge graph using [RML] mappings,
and exported to two Logical Targets, which are accessed through the [DCAT]
vocabulary.
The knowledge graph is exported as N-Quads to the first Target,
and as Turtle to the second Target.
The Turtle file of the second Target is also compressed using the Zip
compression algorithm.

```
id;name;nickname
0;Nathan Ford;Mastermind
1;Sophie Devereaux;Grifter
2;Eliot Spender;Hitter
3;Parker;Thief
4;Alec Hardison;Hacker
```

```
<#CSVSourceAccess> a rml:Source, rml:FilePath;
  rml:root rml:CurrentWorkingDirectory;
  rml:path "./Leverage.csv";
.
```

```
@base <http://example.com/ns#> .

<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#CSVSourceAccess>;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.com/{id}";
    rml:logicalTarget <#TargetDump1>;
    rml:class foaf:Person;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
      rml:logicalTarget <#TargetDump2>;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.

<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump2>;
  rml:serialization formats:Turtle;
.
```

```
<#Dump1> a rml:FilePath;
  rml:path "/data/dump1.nt";
.

<#Dump2> a rml:FilePath;
  rml:path "/data/dump2.ttl.zip";
  rml:compression rml:zip;
.
```

```
# file:///data/dump1.nq
<http://example.org/0> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Nathan Ford" _b0 .
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Mastermind" _b0 .
<http://example.org/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Sophie Devereaux" _b0 .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Grifter" _b0 .
<http://example.org/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Eliot Spencer" _b0 .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Hitter" _b0 .
<http://example.org/3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Parker" _b0 .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Thief" _b0 .
<http://example.org/4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> _b0 .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Alec Hardison" _b0 .
<http://example.org/4> <http://xmlns.com/foaf/0.1/nickname> "Hacker" _b0 .

# file:///data/dump2.ttl.zip
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

<http://example.org/0>
  foaf:name "Nathan Ford";
.
<http://example.org/1>
  foaf:name "Sophie Devereaux";
.
<http://example.org/2>
  foaf:name "Eliot Spencer";
.
<http://example.org/3>
  foaf:name "Parker";
.
<http://example.org/4>
  foaf:name "Alec Hardison";
.
```

## 7. Single targets

In the following examples, the RDF triples are exported to a single Target.
In some examples, not all RDF triples have a dedicated Target assigned,
therefore, they will be exported to the default Target of the processor.

### 7.1 Subject Map

All triples containing the generated subject are exported
to the specified targets in the Subject Map [RML].

The following example exports all triples containing
the generated subject `http://example.org/{id}` to an RDF dump with N-Quads as serialization format and GZip compression:

```
[
  {
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  {
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  {
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  {
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  {
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Friends.json";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.[*]";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{id}";
    rml:logicalTarget <#TargetDump1>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.name";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:age;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.age";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Quads;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nq.gz";
  rml:compression rml:gzip;
.
```

```
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Monica Geller" .
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Rachel Green" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Joey Tribbiani" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Chandler Bing" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Ross Geller" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37" .
```

### 7.2 Predicate Map

All triples containing the generated predicate are exported
to the specified targets in the Predicate Map [RML].

The following example exports all triples containing
the generated predicate `foaf:name` to an RDF dump
with Turtle as serialization format and Zip compression:

```
[
  {
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  {
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  {
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  {
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  {
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Friends.json";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.[*]";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
      rml:logicalTarget <#TargetDump1>;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.name";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:age;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.age";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:Turtle;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.ttl.gz";
  rml:compression rml:gzip;
.
```

```
# file:///data/dump1.ttl.zip
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@base <http://example.com/ns#> .

<http://example.org/0>
  foaf:name "Monica Geller";
.
<http://example.org/1>
  foaf:name "Rachel Green";
.
<http://example.org/2>
  foaf:name "Joey Tribbiani";
.
<http://example.org/3>
  foaf:name "Chandler Bing";
.
<http://example.org/4>
  foaf:name "Ross Geller";
.

# default target of the processor
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37" .
```

### 7.3 Object Map

All triples containing the generated object are exported
to the specified targets in the Object Map [RML].

The following example exports all triples containing
the generated object from the reference `name` to an RDF dump
with N-Triples as serialization format:

```
[
  {
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  {
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  {
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  {
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  {
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Friends.json";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.[*]";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.name";
      rml:logicalTarget <#TargetDump1>;
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:age;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.age";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Monica Geller" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Rachel Green" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Joey Tribbiani" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Chandler Bing" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Ross Geller" .

# default target of the processor
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37" .
```

### 7.4 Graph Map

All triples within a named graph are exported to the specified targets
in the Graph Map [RML].
The named graph influences to where the named graph's triples
may be exported to as the Target's serialization format must
support named graphs such as N-Quads, JSON-LD or TriG.
When a Target contains a serialization format
which does not support named graphs and a Graph Map is used,
the mapping is considered invalid.
If a named graph is spread over multiple targets,
all targets must be combined to access the complete named graph.
In case RDF triples are not within a specific named graph,
they are added to the default graph as specified
by the [R2RML] specification.

The following example exports all triples in the named graph `ex:Friends` to an RDF dump with N-Quads as serialization format:

```
[
  {
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  {
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  {
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  {
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  {
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Friends.json";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.[*]";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{id}";
    rml:graphMap [
      rml:logicalTarget <#TargetDump1>;
      rml:constant ex:Friends;
    ];
   ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.name";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:age;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.age";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nq";
.
```

```
# file:///data/dump1.nq
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33" <http://example.org/Friends> .
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Monica Geller" <http://example.org/Friends> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34" <http://example.org/Friends> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Rachel Green" <http://example.org/Friends> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35" <http://example.org/Friends> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Joey Tribbiani" <http://example.org/Friends> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36" <http://example.org/Friends> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Chandler Bing" <http://example.org/Friends> .
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37" <http://example.org/Friends> .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Ross Geller" <http://example.org/Friends> .
```

### 7.5 Language Map

All triples with a language tag are exported to the specified targets
in the Language Map [RML].

The following examples export all triples with a language tag
to a RDF dump with N-Triples as serialization format:

```
[
  {
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  {
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  {
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  {
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  {
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Friends.json";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.[*]";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{id}";
   ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.name";
      rml:languageMap [
        rml:logicalTarget <#TargetDump1>;
        rml:constant "en";
      ];
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:age;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.age";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Monica Geller"@en .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Rachel Green"@en .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Joey Tribbiani"@en .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Chandler Bing"@en .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Ross Geller"@en .

# default target of the processor
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37" .
```

### 7.6 Datatype Map

All triples with a datatype are exported to the specified targets
in the Datatype Map [RML].

The following examples export all triples with a datatype xsd:integer
to a RDF dump with N-Triples as serialization format:

```
[
  {
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  {
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  {
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  {
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  {
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Friends.json";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.[*]";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{id}";
   ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.name";
      rml:languageMap [
        rml:constant "en";
      ];
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:age;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.age";
      rml:datatypeMap [ a rml:DatatypeMap;
        rml:constant xsd:integer;
        rml:logicalTarget <#TargetDump1>;
      ]
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33"^^xsd:integer .
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34"^^xsd:integer .
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35"^^xsd:integer .
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36"^^xsd:integer .
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37"^^xsd:integer .

# default target of the processor
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Monica Geller"@en .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Rachel Green"@en .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Joey Tribbiani"@en .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Chandler Bing"@en .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Ross Geller"@en .
```

### 7.7 Function Map

```
[
  {
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  {
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  {
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  {
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  {
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Friends.json";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.[*]";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:functionExecution <#Execution>;
      rml:return grel:stringOut;
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:age;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.age";
    ];
  ];
.

<#Execution> a rml:FunctionExecution;
  rml:logicalTarget <#TargetDump1>;
  rml:function grel:toUppercase;
  rml:input [ a rml:Input;
    rml:parameter grel:valueParam;
      rml:inputValueMap [
        rml:reference "$.name"
      ]
  ]
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Quads;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nq.gz";
  rml:compression rml:gzip;
.
```

```
# dump1.nq.gz
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "MONICA GELLER" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "RACHEL GREEN" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "JOEY TRIBBIANI" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "CHANDLER BING" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "ROSS GELLER" .

# default target of the processor
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37" .
```

## 8. Combining multiple Targets

Multiple Targets *MAY* be specified for the same triple
in the same or multiple Term Maps.
If multiple Targets are defined in the same Term Map,
all triples containing the generated Term are exported
to all the specified Targets.
In case multiple Term Maps of the same RDF triple contain more than one Target,
the generated triples are exported to all the specified Targets.
If multiple Term Maps of an RDF triple refer multiple times to the same Target,
the RDF triple is written only once to the target to avoid duplicates.

### 8.1 Multiple Targets in the same Term Map

All triples are exported to all Targets, if the Term Map contains multiple
Targets. In the example a Subject Map has three specified Targets,
all triples with the subject `http://example.org/{@id}` are exported
to the three specified Targets:

- Target 1: `/data/dump.nt.zip`, N-Triples serialization, Zip compression
- Target 2: `/data/dump.jsonld.tar.xz`, JSON-LD serialization, TarXz compression
- Target 3: `/data/dump.rdf.tar.gzip`, RDF/XML serialization, TarGZip compression

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
    rml:logicalTarget <#TargetDump1>;
    rml:logicalTarget <#TargetDump2>;
    rml:logicalTarget <#TargetDump3>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump2>;
  rml:serialization formats:JSON-LD;
.
<#TargetDump3> a rml:LogicalTarget;
  rml:target <#Dump3>;
  rml:serialization formats:RDF_XML;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt.zip";
  rml:compression rml:zip;
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.jsonld.tar.xz";
  rml:compression rml:tarxz;
.
<#Dump3> a rml:Target, rml:FilePath;
  rml:path "/data/dump3.rdf.tar.gz";
  rml:compression rml:targz;
.
```

```
# file:///data/dump1.nt.zip
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" .

# file:///data/dump2.jsonld.tar.xz
[
  {
    "@id": "http://example.org/0",
    "http://xmlns.com/foaf/0.1/name": [
      {
        "@value": "Kara Danvers"
      }
    ]
  },
  {
    "@id": "http://example.org/1",
    "http://xmlns.com/foaf/0.1/name": [
      {
        "@value": "Alex Danvers"
      }
    ]
  },
  {
    "@id": "http://example.org/2",
    "http://xmlns.com/foaf/0.1/name": [
      {
        "@value": "J'onn J'onzz"
      }
    ]
  },
  {
    "@id": "http://example.org/3",
    "http://xmlns.com/foaf/0.1/name": [
      {
        "@value": "Nia Nal"
      }
    ]
  }
]

# file:///data/dump3.rdf.tar.gz
<?xml version="1.0" encoding="utf-8" ?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:foaf="http://xmlns.com/foaf/0.1/">
  <rdf:Description rdf:about="http://example.org/0">
    <foaf:name>Kara Danvers</foaf:name>
  </rdf:Description>
  <rdf:Description rdf:about="http://example.org/1">
    <foaf:name>Alex Danvers</foaf:name>
  </rdf:Description>
  <rdf:Description rdf:about="http://example.org/2">
    <foaf:name>J'onn J'onzz</foaf:name>
  </rdf:Description>
  <rdf:Description rdf:about="http://example.org/3">
    <foaf:name>Nia Nal</foaf:name>
  </rdf:Description>
</rdf:RDF>
```

### 8.2 Subject Map and Predicate Map

All triples containing the subject `http://example.org/{id}` are exported to `TargetDump1` and all triples containing the predicate `foaf:name` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
    rml:logicalTarget <#TargetDump1>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
      rml:logicalTarget <#TargetDump2>;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" .
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" .

# file:///data/dump2.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" .
```

### 8.3 Subject Map and Object Map

All triples containing the subject `http://example.org/{id}` are exported to `TargetDump1` and all triples containing the object reference `name/text()` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
    rml:logicalTarget <#TargetDump1>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
      rml:logicalTarget <#TargetDump2>;
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" .
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" .

# file:///data/dump2.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" .
```

### 8.4 Predicate Map and Object Map

All triples containing the predicate `foaf:name` are exported to `TargetDump1` and all triples containing the object reference `nickname/text()` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
      rml:logicalTarget <#TargetDump1>;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
      rml:logicalTarget <#TargetDump2>;
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" .

# file:///data/dump2.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" .
```

### 8.5 Subject Map, Predicate Map and Object Map

All triples containing the subject `http://example.org/{@id}` are exported to `TargetDump1` and all triples containing the object reference `nickname/text()` or
predicate `foaf:nickname` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
    rml:logicalTarget <#TargetDump1>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
      rml:logicalTarget <#TargetDump2>;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
      rml:logicalTarget <#TargetDump2>;
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" .
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" .

# file:///data/dump2.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" .
```

### 8.6 Subject Map and Graph Map

All triples containing the subject `http://example.org/{@id}` are exported to `TargetDump1` and all triples within the named graph `ex:Characters` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
    rml:logicalTarget <#TargetDump1>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:graphMap [ a rml:GraphMap;
      rml:logicalTarget <#TargetDump2>;
      rml:constant ex:Characters;
    ];
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nq
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" <http://example.org/Characters> .
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" _b0 .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" <http://example.org/Characters> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" _b0 .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" <http://example.org/Characters> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" _b0 .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" <http://example.org/Characters> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" _b0 .

# file:///data/dump2.nq
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" <http://example.org/Characters> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" <http://example.org/Characters> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" <http://example.org/Characters> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" <http://example.org/Characters> .
```

### 8.7 Predicate Map and Graph Map

All triples containing the predicate `foaf:nickname` are exported to `TargetDump1` and all triples within the named graph `ex:Characters` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:graphMap [ a rml:GraphMap;
      rml:logicalTarget <#TargetDump2>;
      rml:constant ex:Characters;
    ];
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
      rml:logicalTarget <#TargetDump1>;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nq
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" _b0 .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" _b0 .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" _b0 .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" _b0 .

# file:///data/dump2.nq
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" <http://example.org/Characters> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" <http://example.org/Characters> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" <http://example.org/Characters> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" <http://example.org/Characters> .
```

### 8.8 Object Map and Graph Map

All triples containing the object reference `nickname/text()` are exported to `TargetDump1` and all triples within the named graph `ex:Characters` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:graphMap [ a rml:GraphMap;
      rml:logicalTarget <#TargetDump2>;
      rml:constant ex:Characters;
    ];
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
      rml:logicalTarget <#TargetDump1>;
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nq
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" _b0 .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" _b0 .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" _b0 .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" _b0 .

# file:///data/dump2.nq
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" <http://example.org/Characters> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" <http://example.org/Characters> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" <http://example.org/Characters> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" <http://example.org/Characters> .
```

### 8.9 Language Map and Graph Map

All triples containing the language tag `en` are exported to `TargetDump1` and all triples within the named graph `ex:Characters` are exported to `TargetDump2`.
The other triples are exported to the default target of the processor
as there is no dedicated Target assigned to triples containing `foaf:nickname` as predicate.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:graphMap [ a rml:GraphMap;
      rml:logicalTarget <#TargetDump2>;
      rml:constant ex:Characters;
    ];
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
      rml:languageMap [
        rml:logicalTarget <#TargetDump1>;
        rml:constant "en";
      ];
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
      rml:logicalTarget <#TargetDump2>;
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers"@en <http://example.org/Characters> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers"@en <http://example.org/Characters> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz"@en <http://example.org/Characters> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal"@en <http://example.org/Characters> .

# file:///data/dump2.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers"@en <http://example.org/Characters> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers"@en <http://example.org/Characters> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz"@en <http://example.org/Characters> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal"@en <http://example.org/Characters> .

# default target of processor
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" _b0 .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" _b0 .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" _b0 .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" _b0 .
```

### 8.10 Language Map and Object Map

All triples containing the language tag `en` are exported to `TargetDump1` and all triples containing the object reference `nickname/text()` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
      rml:languageMap [
        rml:logicalTarget <#TargetDump1>;
        rml:constant "en";
      ];
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
      rml:logicalTarget <#TargetDump2>;
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers"@en .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers"@en .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz"@en .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal"@en .

# file:///data/dump2.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" .
```

### 8.11 Multiple Predicate Maps

All triples containing the predicate `foaf:name` are exported to `TargetDump1` and all triples containing the predicate `foaf:nickname` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
      rml:logicalTarget <#TargetDump1>;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
      rml:logicalTarget <#TargetDump2>;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" .

# file:///data/dump2.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" .
```

### 8.12 Multiple Object Maps

All triples containing the object reference `name/text()` are exported to `TargetDump1` and all triples containing the object reference `nickname/text()` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
      rml:logicalTarget <#TargetDump1>;
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
      rml:logicalTarget <#TargetDump2>;
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" .

# file:///data/dump2.nt
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" .
```

### 8.13 Multiple Graph Maps

All triples within the named graph `ex:Characters` are exported to `TargetDump1` and all triples within the named graph `ex:NickNames` are exported to `TargetDump2`.

```
<Supergirl>
  <Character id="0">
    <name>Kara Danvers</name>
    <nickname>Supergirl</nickname>
  </Character>
  <Character id="1">
    <name>Alex Danvers</name>
    <nickname>Sentinel</nickname>
  </Character>
  <Character id="2">
    <name>J'onn J'onzz</name>
    <nickname>Martian Manhunter</nickname>
  </Character>
  <Character id="3">
    <name>Nia Nal</name>
    <nickname>Dreamer</nickname>
  </Character>
</Supergirl>
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "Supergirl.xml";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Supergirl/Character/";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:graphMap [ a rml:GraphMap;
      rml:logicalTarget <#TargetDump1>;
      rml:constant ex:Characters;
    ];
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:graphMap [ a rml:GraphMap;
      rml:logicalTarget <#TargetDump2>;
      rml:constant ex:NickNames;
    ];
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname/text()";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nq
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Kara Danvers" <http://example.org/Characters> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Alex Danvers" <http://example.org/Characters> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "J'onn J'onzz" <http://example.org/Characters> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Nia Nal" <http://example.org/Characters> .

# file:///data/dump2.nq
<http://example.org/0> <http://xmlns.com/foaf/0.1/nickname> "Supergirl" <http://example.org/Nicknames> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/nickname> "Sentinel" <http://example.org/Nicknames> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/nickname> "Martian Manhunter" <http://example.org/Nicknames> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/nickname> "Dreamer" <http://example.org/Nicknames> .
```

## 9. Overriding Targets

In some cases exporting all triples to a target is not desired,
therefore Targets can be overridden when needed
by either using a separate Triples Map which isolates certain triples or
by using FnO functions [FnO] as conditions.

### 9.1 Separate Triples Map

Triples can be exported to a specific Target while not to other Targets
by isolating these triples in a separate Triples Map.

In this example, the same subject and object are used in both Triples Maps,
but with a diffent predicate. The triples with the first predicate `foaf:name` are exported to the first Target and the triples with the second predicate `schema:name` to the second Target.

```
# DBPedia Friends actors as CSV
actor,name,nickname
http://dbpedia.org/resource/Kevin_Sussman,Kevin Sussman
http://dbpedia.org/resource/Jim_Parsons,Jim Parsons
http://dbpedia.org/resource/Kaley_Cuoco,Kaley Cuoco
http://dbpedia.org/resource/Sara_Gilbert,Sara Gilbert
http://dbpedia.org/resource/Kunal_Nayyar,Kunal Nayyar
http://dbpedia.org/resource/Laura_Spencer_(actress),Laura Spencer
http://dbpedia.org/resource/Simon_Helberg,Simon Helberg
http://dbpedia.org/resource/Johnny_Galecki,Johnny Galecki
http://dbpedia.org/resource/Mayim_Bialik,Mayim Bialik
http://dbpedia.org/resource/Melissa_Rauch,Melissa Rauch
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "FriendsDBPedia.csv";
.
```

```
<#TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:CSV;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:reference "actor";
    rml:termType rml:IRI;
    rml:logicalTarget <TargetDump1>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name";
    ];
  ];

<#TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#SourceAccess>;
    rml:referenceFormulation rml:CSV;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:reference "actor";
    rml:termType rml:IRI;
    rml:logicalTarget <TargetDump2>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant schema:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name";
    ];
  ];
.
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump2>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://dbpedia.org/resource/Kevin_Sussman> <http://xmlns.com/foaf/0.1/name> "Kevin Sussman" .
<http://dbpedia.org/resource/Jim_Parsons> <http://xmlns.com/foaf/0.1/name> "Jim Parsons" .
<http://dbpedia.org/resource/Kaley_Cuoco> <http://xmlns.com/foaf/0.1/name> "Kaley Cuoco" .
<http://dbpedia.org/resource/Sara_Gilbert> <http://xmlns.com/foaf/0.1/name> "Sara Gilbert" .
<http://dbpedia.org/resource/Kunal_Nayyar> <http://xmlns.com/foaf/0.1/name> "Kunal Nayyar" .
<http://dbpedia.org/resource/Laura_Spencer> <http://xmlns.com/foaf/0.1/name> "Laura Spencer" .
<http://dbpedia.org/resource/Simon_Helberg> <http://xmlns.com/foaf/0.1/name> "Simon Helberg" .
<http://dbpedia.org/resource/Johnny_Galecki> <http://xmlns.com/foaf/0.1/name> "Johnny Galecki" .
<http://dbpedia.org/resource/Mayim_Bialik> <http://xmlns.com/foaf/0.1/name> "Mayim Bialik" .
<http://dbpedia.org/resource/Melissa_Rauch> <http://xmlns.com/foaf/0.1/name> "Melissa Rauch" .

# file:///data/dump2.nt
<http://dbpedia.org/resource/Kevin_Sussman> <http://schema.org/name> "Kevin Sussman" .
<http://dbpedia.org/resource/Jim_Parsons> <http://schema.org/name> "Jim Parsons" .
<http://dbpedia.org/resource/Kaley_Cuoco> <http://schema.org/name> "Kaley Cuoco" .
<http://dbpedia.org/resource/Sara_Gilbert> <http://schema.org/name> "Sara Gilbert" .
<http://dbpedia.org/resource/Kunal_Nayyar> <http://schema.org/name> "Kunal Nayyar" .
<http://dbpedia.org/resource/Laura_Spencer> <http://schema.org/name> "Laura Spencer" .
<http://dbpedia.org/resource/Simon_Helberg> <http://schema.org/name> "Simon Helberg" .
<http://dbpedia.org/resource/Johnny_Galecki> <http://schema.org/name> "Johnny Galecki" .
<http://dbpedia.org/resource/Mayim_Bialik> <http://schema.org/name> "Mayim Bialik" .
<http://dbpedia.org/resource/Melissa_Rauch> <http://schema.org/name> "Melissa Rauch" .
```

### 9.2 Conditions

FnO functions *MAY* be leveraged to export triples
only under certain conditions.
Conditions are already integrated in RML+FnO processors,
thus conditions apply on Targets as well.
Triples are generated and exported based on the FnO condition's evaluation.
Only if the condition is true, the triples are generated and exported.

In the example, the triples with `Jim Parsons` as object are exported
to the first Target, triples with `Kaley Cuoco` as object are exported
to the second Target.

```
# DBPedia Friends actors as CSV
actor,name,nickname
http://dbpedia.org/resource/Kevin_Sussman,Kevin Sussman
http://dbpedia.org/resource/Jim_Parsons,Jim Parsons
http://dbpedia.org/resource/Kaley_Cuoco,Kaley Cuoco
http://dbpedia.org/resource/Sara_Gilbert,Sara Gilbert
http://dbpedia.org/resource/Kunal_Nayyar,Kunal Nayyar
http://dbpedia.org/resource/Laura_Spencer_(actress),Laura Spencer
http://dbpedia.org/resource/Simon_Helberg,Simon Helberg
http://dbpedia.org/resource/Johnny_Galecki,Johnny Galecki
http://dbpedia.org/resource/Mayim_Bialik,Mayim Bialik
http://dbpedia.org/resource/Melissa_Rauch,Melissa Rauch
```

```
<#SourceAccess> a rml:Source, rml:FilePath;
  rml:path "FriendsDBPedia.csv";
.
```

```
<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <SourceAccess>;
    rml:referenceFormulation rml:CSV;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:reference "actor";
    rml:termType rml:IRI;
    rml:logicalTarget <TargetDump1>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name";
    ];
  ];
  rml:predicateObjectMap [
    rml:predicateMap [ rml:constant foaf:name ];
    rml:objectMap [
      fnml:functionValue [
        rml:predicateObjectMap [
          rml:predicate fno:executes ;
          rml:objectMap [ rml:constant idlab-fn:decide ]
        ];
        rml:predicateObjectMap [
          rml:predicate idlab-fn:expectedStr ;
          rml:objectMap [ rml:constant "Jim Parsons"]
        ];
        rml:predicateObjectMap [
          rml:predicate idlab-fn:str ;
          rml:objectMap [
            rml:reference "name";
            rml:logicalTarget <#TargetDump1>;
          ];
        ];
      ];
    ];
  ];
  rml:predicateObjectMap [
    rml:predicateMap [ rml:constant foaf:name ];
    rml:objectMap [
      fnml:functionValue [
        rml:predicateObjectMap [
          rml:predicate fno:executes ;
          rml:objectMap [ rml:constant idlab-fn:decide ]
        ];
        rml:predicateObjectMap [
          rml:predicate idlab-fn:expectedStr ;
          rml:objectMap [ rml:constant "Kaley Cuoco"]
        ];
        rml:predicateObjectMap [
          rml:predicate idlab-fn:str ;
          rml:objectMap [
            rml:reference "name";
            rml:logicalTarget <#TargetDump2>;
          ];
        ];
      ];
    ];
  ];
```

```
<#TargetDump1> a rml:LogicalTarget;
  rml:target <#Dump1>;
  rml:serialization formats:N-Triples;
.
<#TargetDump2> a rml:LogicalTarget;
  rml:target <#Dump2>;
  rml:serialization formats:N-Triples;
.
```

```
<#Dump1> a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
<#Dump2> a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
```

```
# file:///data/dump1.nt
<http://dbpedia.org/resource/Jim_Parsons> <http://xmlns.com/foaf/0.1/name> "Jim Parsons" .

# file:///data/dump2.nt
<http://dbpedia.org/resource/Kaley_Cuoco> <http://xmlns.com/foaf/0.1/name> "Kaley Cuoco" .
```

## A. References

### A.1 Normative references

[CSVW]

[CSV on the Web: A Primer](https://www.w3.org/TR/tabular-data-primer/). Jeni Tennison. W3C. 25 February 2016. W3C Working Group Note. URL: <https://www.w3.org/TR/tabular-data-primer/>

[DCAT]

[Data Catalog Vocabulary (DCAT) - Version 2](https://www.w3.org/TR/vocab-dcat/). W3C. 22 February 2020. W3C Recommendation. URL: <https://www.w3.org/TR/vocab-dcat/>

[FnO]

[Function Ontology (FnO)](https://w3id.org/function/spec). Ben De Meester; Anastasia Dimou; Florian Kleedorfer. IDLab - Ghent University - imec. 10 November 2021. Unofficial Draft. URL: <https://w3id.org/function/spec>

[N-Quads]

[RDF 1.1 N-Quads](https://www.w3.org/TR/n-quads/). W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/n-quads/>

[R2RML]

[R2RML: RDB to RDF Mapping Language](https://www.w3.org/TR/r2rml/). Souripriya Das; Seema Sundara; Richard Cyganiak. W3C. 27 September 2012. W3C Recommendation. URL: <https://www.w3.org/TR/r2rml/>

[RDF-Concepts]

[Resource Description Framework (RDF): Concepts and Abstract Syntax](https://www.w3.org/TR/rdf-concepts/). Graham Klyne; Jeremy Carroll. W3C. 10 February 2004. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-concepts/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

[RML]

[RDF Mapping Language (RML)](https://rml.io/specs/rml). Anastasia Dimou; Miel Vander Sande; Ben De Meester; Pieter Heyvaert; Thomas Delva. IDLab - Ghent University - imec. 16 November 2022. W3C Unofficial Draft. URL: <https://rml.io/specs/rml>

[RML-Core]

[RML-Core](https://w3id.org/rml/core/spec). KGC-CG-W3C. Draft Community Group Report. URL: <https://w3id.org/rml/core/spec>

[RML-IO-Registry]

[RML-IO-Registry](https://kg-construct.github.io/rml-io-registry/). KGC-CG-W3C. Draft Community Group Report. URL: <https://kg-construct.github.io/rml-io-registry/>

[SD]

[SPARQL 1.1 Service Description](https://www.w3.org/TR/sparql11-service-description/). W3C. 21 March 2013. W3C Recommendation. URL: <https://www.w3.org/TR/sparql11-service-description/>

[Turtle]

[RDF 1.1 Turtle](https://www.w3.org/TR/turtle/). W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/turtle/>

Permalink

**Referenced in:**

- § 3.1 Defining Logical Sources (2) (3)
- § 3.1.1 Reference formulations
- § 5. Logical Source in RML

Permalink

**Referenced in:**

- § 3.1 Defining Logical Sources
- § 3.2 Source (2)
- § 3.2.1 NULL values
- § 3.2.2 Compression formats (2)
- § 3.2.3 Encoding formats
- § 3.3 Examples
