---
title: "YARRRML"
source: https://w3id.org/yarrrml/spec/
family: mapping
fetched: 2026-10-26
---

# YARRRML

> Human-friendly YAML mapping language compiled to RML.

## Contents

- 1 Terminology
- 2 Profiles
- 3 Base IRI
- 4 Prefixes and namespaces
- 5 Authors
- 6 Template
- 7 Data sources
- 8 Keys
- 9 Type
- 10 Access
- 11 Query formulation
- 12 Query
- 13 Reference formulation
- 14 Iterator
- 15 Delimiter
- 16 Encoding
- 17 Credentials
- 18 Content type
- 19 Operation type
- 20 Security
- 21 Query formulation vs reference formulation
- 22 Examples
- 23 Targets
- 24 Keys
- 25 Type
- 26 Access
- 27 Serialization
- 28 Compression
- 29 Examples
- 30 Mappings
- 31 Data sources
- 32 Targets
- 33 Subjects
- 34 Predicates and objects
- 35 Datatypes
- 36 Languages
- 37 Referring to other mappings
- 38 Graphs
  - 38.1 All triples
  - 38.2 All triples with a specific predicate and object
- 39 Functions
- 40 Conditions
- 41 External references
- 42 Shortcuts
- 43 Keys
- 44 Predicates
- 45 Reference implementation

---

YARRRML (pronounced /jɑɹməl/) is a human readable text-based representation for declarative generation rules.
It is a subset of [YAML],
a widely used data serialization language designed to be human-friendly.

## Terminology

*subject*

the subject of an RDF triple

*predicate*

the predicate of an RDF triple

*object*

the object of an RDF triple

*class*

the type of an entity

*datatype*

the type of a literal value

*reference*

the reference to a data fraction in a data source

*function*

a programmatic function that takes 0 or more input parameters and returns a single result

## Profiles

This specification includes the following main profiles for tools that process YARRRML documents:

- R2RML: applies the semantics specified by [R2RML];
- RML: applies the semantics specified by [RML]; and
- RMLT: applies the semantics specified by [RMLT].
- RMLAHT: applies the semantics specified by [RMLATH].
- RMLTDT: applies the semantics specified by [RMLTDT].

These profiles can be extended with additional profiles, which cannot be used on their own:

- FORMATS: applies the semantics specified by the [W3C Formats namespace](http://w3.org/ns/formats).
- COMP: applies the semantics specified by the [Compression namespace](http://semweb.mmlab.be/ns/rml-compression#).
- VOID: applies the semantics specified by [VoID];
- FnO: applies the semantics specified by [FnO];
- DCAT: applies the semantics specified by [DCAT];
- D2RQ: applies the semantics specified by [D2RQ];
- SD: applies the semantics specified by SD ([sparql11-service-description]); and
- CSVW: applies the semantics specified by CSVW ([csv2rdf]).
- WOT: applies the semantics specified by WoT Thing Description and WoT Security ([wot-thing-description], [wot-security])

## Base IRI

A base IRI can be defined.
This IRI will be used for the creation of the IRIs of the term maps and sources of the [R2]RML rules.

A base IRI can be added by adding key `base` with as value the IRI itself to the root of the document.
In the following example the base IRI is set to `http://mybaseiri.com#`.

```
        base: http://mybaseiri.com#

```

## Prefixes and namespaces

A set of prefixes and namespaces are predefined by default in every YARRRML document.
There are the same as the predefined prefixes for [RDFa](https://www.w3.org/2011/rdfa-context/rdfa-1.1).

Custom prefixes can be added by adding the collection `prefixes` to the root of the document.
Each combination of a prefix and namespace is added to this collection as a key-value pair.

In the following example two prefixes are defined: `ex` and `test`.

```
        prefixes:
          ex: http://www.example.com
          test: http://www.test.com

```

## Authors

The authors of the YARRRML rules can be added via the key `authors`.
The value is an array with an object for each author.
Each author can have the following keys:

*name*

the name of the author

*email*

the email of the author

*website*

the website of the author

In the following example two authors are defined.

- YARRRML
- RML

```
              authors:
                - name: John Doe
                  email: john@doe.com
                - name: Jane Doe
                  website: https://janedoe.com

```

```
              :Rules a void:Dataset;
                void:exampleResource <#TM>; # linking all Triples Maps
                dcterms:contributor [
                  a foaf:Person;
                  rdfs:label "John Doe";
                  foaf:mbox <mailto:john@doe.com>
                ], [
                  a foaf:Person;
                  rdfs:label "Jane Doe";
                  foaf:homepage <https://janedoe.com>
                ].

```

A string template exists that provides a shortcut version: `name <email> (website)`.
In the following example the same two authors are defined.

- YARRRML
- RML

```
              authors:
                - John Doe <john@doe.com>
                - Jane Doe (https://janedoe.com)

```

```
              :Rules a void:Dataset;
                void:exampleResource <#TM>; # linking all Triples Maps
                dcterms:contributor [
                  a foaf:Person;
                  rdfs:label "John Doe";
                  foaf:mbox <mailto:john@doe.com>
                ], [
                  a foaf:Person;
                  rdfs:label "Jane Doe";
                  foaf:homepage <https://janedoe.com>>
                ].

```

In the case that authors have a WebID, it can be used instead of providing the name, email and so on.
In the following example the same two authors are added via their WebIDs.

- YARRRML
- RML

```
              authors:
                - http://johndoe.com/#me
                - http://janedoe.com/#me

```

```
                :Rules a void:Dataset;
                  void:exampleResource <#TM>; # linking all Triples Maps
                  dcterms:contributor <http://johndoe.com/#me>,
                    <http://janedoe.com/#me>.

```

In all the above cases when there is only author, an array is not needed.
In the following example one author is defined.

- YARRRML
- RML

```
              authors: John Doe <john@doe.com>

```

```
              :Rules a void:Dataset;
                void:exampleResource <#TM>; # linking all Triples Maps
                dcterms:contributor [
                  a foaf:Person;
                  rdfs:label "John Doe";
                  foaf:mbox <mailto:john@doe.com>
                ].

```

## Template

A template contains 0 or more constant strings and 0 or more references to data in a data.
References are prefixed with `$(` and suffixed with `)`.
For example, `foo` is a template with one constant string. `$(id)` is a template with one reference to `id`. `foo-$(id)` is a template with one constant string `foo-` and one reference to `id`.

## Data sources

The data sources are defined in the `sources` collection in the root of the document.
Each source is added to this collection via a key-value pair.
The key has to be unique for every source.
The value is a collection with the keys described below.

## Keys

*type*

Type of the data source.
Required profiles: RML.
Datatype: string.

*access*

Local or remote location of the data source.
Required profiles: RML.
Datatype: string.

*credentials*

Credentials required to access the data source.
Required profiles: RML.
Datatype: collection.

*queryFormulation*

Query formulation used to query the data source.
Required profiles: RML or R2RML.
Datatype: string.

*query*

Query to execute on the data source to retrieve the desired data.
Required profiles: RML or R2RML.
Datatype: string.

*encoding*

Encoding used by the data.
Required profiles: RML and CSVW.
Datatype: string.

*delimiter*

Delimiter to separate fields in a record.
Required profiles: RML and CSVW.
Datatype: string.

*contentType*

Content type to expect expressed as MIME types.
Required profiles: RML and WOT.
Datatype: string.

*operationType*

Indicates the operation type of the Web of Things description.
Required profiles: RML and WOT.
Datatype: string.

*referenceFormulation*

Reference formulation used to access the data retrieved from the data source.
Required profiles: RML.
Datatype: string.

*iterator*

Path to the records over which to iterate.
Required profiles: RML.
Datatype: string.

## Type

This key's value describes what type of data source is used,
so that the correct way of connecting to the data source can be determined.
By default a local file is assumed when the `access` value is a path such as `file.json`.
The value of type is then implicitly `localfile`.
By default a remote file is assumed and retrieved via an HTTP GET when a URL is given such as `http://example.org/file.json`.
The value of type is then implicitly `remotefile`.
The following values are supported:

| Data source type                                                                   | Value          | Required profiles |
| ---------------------------------------------------------------------------------- | -------------- | ----------------- |
| [Oracle Database](https://www.oracle.com/database/technologies/)                   | oracle         | RML and D2RQ      |
| [MySQL](https://www.mysql.com/)                                                    | mysql          | RML and D2RQ      |
| [HSQLDB](http://hsqldb.org/)                                                       | hsql           | RML and D2RQ      |
| [PostgreSQL](https://www.postgresql.org/)                                          | postgresql     | RML and D2RQ      |
| [IBM DB2](https://www.ibm.com/products/db2-database)                               | db2            | RML and D2RQ      |
| [IBM Informix](https://www.ibm.com/products/informix)                              | informix       | RML and D2RQ      |
| [Ingres](https://www.actian.com/data-management/actian-x-hybrid-rdbms/)            | ingres         | RML and D2RQ      |
| [SAP Adaptive Server Enterprise](https://www.sap.com/products/sybase-ase.html)     | sapase         | RML and D2RQ      |
| [SAP SQL Anywhere](https://www.sap.com/products/sql-anywhere.html)                 | sapsqlanywhere | RML and D2RQ      |
| [Firebird](https://firebirdsql.org/)                                               | firebird       | RML and D2RQ      |
| [Microsoft SQL Server](https://www.microsoft.com/en-gb/sql-server/sql-server-2019) | mssqlserver    | RML and D2RQ      |
| [Virtuoso](https://virtuoso.openlinksw.com/)                                       | virtuoso       | RML and D2RQ      |
| [Web of Things](https://www.w3.org/WoT/)                                           | wot            | RML and WOT       |
| SPARQL endpoint                                                                    | sparql         | RML and SD        |
| Local file                                                                         | localfile      | RML               |
| Remote file                                                                        | remotefile     | RML               |

> **Note:**
>
> R2RML rules do not include this information:
> it is supplied directly to the used R2RML processor.
> Also, it does not support SPARQL endpoints, local files, and remote files.

## Access

This key's value describes where the data source can be accessed.
Examples are `file.json` and `http://example.org/my/db`.

## Query formulation

Query formulations define what type of query is used query to a data source.
This key's supported values are the same as the values for the type,
together with the additional values below.
Therefore, if only a type is provided the query formulation is implicitly the same.
But if you want for example to use a MySQL query with an Oracle Database,
then you need to specify both the type and the query formulation.

In the case of SPARQL endpoints, defined by the value `sparql` for type,
the query formulation is by default `sparql11`: the data sources are queried
via a [SPARQL 1.1 query](https://www.w3.org/TR/sparql11-query/).

| Query formulation                                                                       | Value    | Required profiles      |
| --------------------------------------------------------------------------------------- | -------- | ---------------------- |
| [SPARQL 1.1 query](https://www.w3.org/TR/sparql11-query/) (default for SPARQL endpoint) | sparql11 | RML and SD             |
| [SQL:2008](https://en.wikipedia.org/wiki/SQL:2008)                                      | sql2008  | RML and D2RQ, or R2RML |
| [SQL:2011](https://en.wikipedia.org/wiki/SQL:2011)                                      | sql2011  | RML and D2RQ, or R2RML |
| [SQL:2016](https://en.wikipedia.org/wiki/SQL:2016)                                      | sql2016  | RML and D2RQ, or R2RML |

## Query

This key's value is a query that conforms the selected query formulation.
For example, if the query formulation is `mysql`, then
the value of `query` needs to be a valid MySQL query.

## Reference formulation

Reference formulations define how to access the data retrieved from the data source.
For example, this retrieved data can be query results coming from a database or
a JSON file on the local file system.
The value of this key is a string.
This key's supported values are.

| Reference formulation                               | Value    | Required profiles |
| --------------------------------------------------- | -------- | ----------------- |
| CSV (tables with columns and rows)                  | csv      | RML               |
| [JSONPath](https://goessner.net/articles/JsonPath/) | jsonpath | RML               |
| [XPath](https://www.w3.org/TR/xpath/)               | xpath    | RML               |
| [XQuery](https://www.w3.org/TR/xquery/)             | xquery   | RML               |

## Iterator

This key's value defines what records are processed.
It has to conform to the selected reference formulation.

Consider the following JSON example with an array of two people.
One person is one record.

```
{
  "people": [
    {...},
    {...}
  ]
}

```

To iterate over all the people,
the iterator is `$.people[*]` when using `jsonpath` as a reference formulation.
If no iterator is provided,
it is unclear what the records are.

## Delimiter

This key's value defines the delimiter when working with CSV files.
The default is `,`.

## Encoding

This key's value defines the encoding of the retrieved data.
The default is `utf-8`.

## Credentials

Credentials are provided when accessing a data source requires authentication.
This key's value is a collection with the keys described below.

*username*

User name required to access the data source.
Required profiles: RML and D2RQ.

*password*

Password required to access the data source.
Required profiles: RML and D2RQ.

## Content type

This key's value defines the content type of the retrieved data with a MIME type.

## Operation type

This key's value defines the operation type for the Web of Things description.

| Operation                            | Value   | Operation type     |
| ------------------------------------ | ------- | ------------------ |
| Retrieve data from Web API or stream | `read`  | `td:readproperty`  |
| Push data to Web API or stream       | `write` | `td:writeproperty` |

## Security

Web of Things Security description to describe how authentication
should be performed againast a Web API or stream when accessing its data.

| Security                 | Value    | Web of Things Security scheme |
| ------------------------ | -------- | ----------------------------- |
| Security through API key | `apikey` | `wotsec:APISecurityScheme`    |

*type*

Security scheme to apply.
Required profiles: RML and WOT.

*in*

Where to store the security information when performing authentication against a Web API or stream.
Required profiles: RML and WOT.

*name*

Name of the property holding the private security information such as API key.
Required profiles: RML and WOT.

*value*

Value of the property holding the private security information such as API key.
Required profiles: RML and WOT.

## Query formulation vs reference formulation

![Sequence diagram showing difference between query and reference formulation](https://rml.io/yarrrml/spec/resources/images/query-vs-reference-formulations.jpeg)

In the figure above, you find a sequence diagram showing at what point the query and query formulation are used and
a what point the iterator and reference formulation are used.
The component "Processor" represents the software application that executes the converted YARRRML rules,
e.g., RML rules.
For clarity, this conversion is not included in the figure.
The processor gets the `type` and `access` from the YARRRML rules.
It uses this information to create a connection with the data source.
Next, the processor gets the `query formulation` and `query`.
It uses this information to query the desired data from the data source,
making use of the earlier created connection.
Once the data is retrieved the connection is closed.
The processor gets the `reference formulation` and `iterator`.
It uses this information to iterate over the retrieved data.

![Sequence diagram showing difference between query and reference formulation for a SPARQL endpoint](https://rml.io/yarrrml/spec/resources/images/query-vs-reference-formulations-example.jpeg)

In the figure above, you find a sequence diagram showing an example of
the use of query, query formulation, iterator, and reference formulation.
The data source is a SPARQL endpoint, available at `http://example.org/sparql`,
which is queried using a SPARQL 1.1 query.
The query formulation is `sparql11` and
the query is `SELECT * WHERE{?s ?p ?o}` The result is an XML document which is iterated upon using the iterator `/sparql/results/result` that conforms to the XPath specification.

## Examples

In the following example a single data source is defined `person-source`.

- YARRRML
- RML

```
            sources:
              person-source:
                access: data/person.json
                referenceFormulation: jsonpath
                iterator: $

```

```
              <#LogicalSource> a rml:LogicalSource;
                rml:source "data/person.json";
                rml:referenceFormulation ql:JSONPath;
                rml:iterator "$".

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
                sources:
                  person-source: [data/person.json~jsonpath, $]

```

```
                <#LogicalSource> a rml:LogicalSource;
                  rml:source "data/person.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$".

```

The collection is replaced with an array where
the first element contains the value for `access` appended with the `~` and the value for `referenceFormulation`, and
the second element contains the iterator.

The following mapping access a SQL database and select the required data via a query.

- YARRRML
- RML

```
                mapping:
                  person:
                    sources:
                      access: http://localhost/example
                      type: mysql
                      credentials:
                        username: root
                        password: root
                      queryFormulation: sql2008
                      query: |
                        SELECT DEPTNO, DNAME, LOC,
                        (SELECT COUNT(*) FROM EMP WHERE EMP.DEPTNO=DEPT.DEPTNO) AS STAFF
                        FROM DEPT;
                      referenceFormulation: csv

```

```
                <#TriplesMap> a rr:TriplesMap;

                  rml:logicalSource [
                    a rml:LogicalSource;
                    rml:source <#DataSource>;
                    rr:sqlVersion rr:SQL2008;
                    rml:query "SELECT DEPTNO, DNAME, LOC,
                          (SELECT COUNT(*) FROM EMP WHERE EMP.DEPTNO=DEPT.DEPTNO) AS STAFF
                          FROM DEPT;";
                    rml:referenceFormulation ql:CSV
                  ].

                <#DataSource> a d2rq:Database;
                  d2rq:jdbcDSN "jdbc:mysql://localhost/example";
                  d2rq:jdbcDriver "com.mysql.jdbc.Driver";
                  d2rq:username "root";
                  d2rq:password "root" .

```

## Targets

## Keys

*type*

Type of the target.
Required profiles: RMLT.
Datatype: string.

*access*

Local or remote location of the target.
Required profiles: RMLT.
Datatype: string.

*serialization*

Serialization format to use when exporting to the target.
Required profiles: RMLT and FORMATS.
Datatype: string.

*compression*

Compression algorithm to use when exporting to the target.
Required profiles: RMLT and COMP.
Datatype: string.

## Type

This key's value describes what type of target is used, so that the correct way
of accessing to the target can be determined. By default a local file is assumed
when the `access` value is a path such as file.nq. The value of type is
then implicitly `localfile`. The following values are supported:

| Target type     | Value       | Required profiles       |
| --------------- | ----------- | ----------------------- |
| SPARQL endpoint | `sparql`    | RML, RMLT and SD        |
| Local file      | `localfile` | RML, RMLT and VOID/DCAT |

## Access

This key's value describes where the target can be accessed. Example: `file.nq`.

## Serialization

This key's value is the serialization format that should be used to serialize
the RDF when exporting to the target. By default, the serialization format is N-Quads
[DataIO]. The supported serialization formats are listed by the [W3C Formats namespace](http://w3.org/ns/formats).

| Serialization format   | Value         |
| ---------------------- | ------------- |
| JSON-LD                | jsonld        |
| N3                     | n3            |
| N-Triples              | ntriples      |
| N-Quads                | nquads        |
| LD Patch               | ldpatch       |
| microdata              | microdata     |
| OWL XML Serialization  | owlxml        |
| OWL Functional Syntax  | owlfunctional |
| OWL Manchester Syntax  | owlmanchester |
| POWDER                 | powder        |
| POWDER-S               | powder-s      |
| PROV-N                 | prov-n        |
| PROV-XML               | prov-xml      |
| RDFa                   | rdfa          |
| RDF/JSON               | rdfjson       |
| RDF/XML                | rdfxml        |
| RIF XML Syntax         | rifxml        |
| SPARQL Results in XML  | sparqlxml     |
| SPARQL Results in JSON | sparqljson    |
| SPARQL Results in CSV  | sparqlcsv     |
| SPARQL Results in TSV  | sparqltsv     |
| Turtle                 | turtle        |
| TriG                   | trig          |

## Compression

Compression defines which compression algorithm should be applied when exporting
to a target. By default, no compression algorithm is applied [DataIO]. The supported
compression algorithms are listed by the [Compression namespace](http://semweb.mmlab.be/ns/rml-compression#).

| Compression algorithm | Value   |
| --------------------- | ------- |
| GZip                  | gzip    |
| Zip                   | zip     |
| TarGZip               | targzip |
| TarXz                 | tarxz   |

## Examples

In the following example a single target is defined `person-target`.

- YARRRML
- RML

```
                targets:
                  person-target:
                    access: data/dump.ttl.gz
                    type: void
                    serialization: turtle
                    compression: gzip

```

```
                <#LogicalTarget> a rmlt:LogicalTarget;
                  rmlt:target [ a void:Dataset;
                    void:dataDump <file://data/dump.ttl.gz>
                  ];
                  rmlt:serialization formats:Turtle;
                  rmlt:compression comp:gzip.

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
                targets:
                  person-target: [data/dump.ttl.gz~void, turtle, gzip]

```

```
                <#LogicalTarget> a rmlt:LogicalTarget;
                  rmlt:target [ a void:Dataset;
                    void:dataDump <file://data/dump.ttl.gz>
                  ];
                  rmlt:serialization formats:Turtle;
                  rmlt:compression comp:gzip.

```

The collection is replaced with an array where the first element contains the value
for access appended with the `~` and the value for `type`, the
second element contains serialization format, and the third element contains the
compression algorithm. The serialization format and compression algorithm are not required.
By default N-Quads is used a serialization format and no compression is applied.

The following mapping access a SPARQL endpoint as target using SPARQL UPDATE queries:

- YARRRML
- RML

```
                mapping:
                  person:
                    subjects:
                      - value: http://example.org/{id}
                        targets:
                          access: http://localhost/sparql
                          type: sparql

```

```
                <#TriplesMap> a rr:TriplesMap;
                 rr:subjectMap [ a rr:SubjectMap;
                   rr:template "http://example.org/{id}";
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target <#Target>
                   ];
                 ].

                <#Target> a sd:Service;
                  sd:endpoint <http://localhost/sparql>
                  sd:supportedLanguage sd:SPARQL11Update.

```

## Mappings

The `mappings` collection contains all the mappings of the document.
Each mapping is added to this collection via key-value pair.
The key is unique for each mapping.
The value is collection containing rules to generate the subjects, predicates, and objects.

In the following example two mappings are defined: `person` and `project`.

- YARRRML
- RML

```
              mappings:
                person: ...
                project: ...

```

```
              <#TriplesMap> a rr:TriplesMap. #person
              <#TriplesMap2> a rr:TriplesMap. #project

```

## Data sources

Besides defining data sources at the root of the document,
data sources can also be defined inside a mapping via the collection `sources`.
However, no unique key is specified for a source, and, thus, it cannot be referred to from other mappings.
The key-value to add to a source are the same when defining sources at the root of the document.

In the following example the mapping `person` has one source.

- YARRRML
- RML

```
            mapping:
              person:
                sources:
                  access: data/person.json
                  referenceFormulation: jsonpath
                  iterator: $

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$".
                ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
            mapping:
              person:
                sources:
                  - [data/person.json~jsonpath, $]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$".
                ].

```

In case a mapping needs to be applied to multiple data sources, multiple sources can be added to the `scources` collection.
In the following example the `person` mapping has two data sources.

- YARRRML
- RML

```
              mapping:
                person:
                  sources:
                    - access: data/person.json
                      referenceFormulation: jsonpath
                      iterator: $
                    - access: data/person2.json
                      referenceFormulation: jsonpath
                      iterator: "$.persons[*]"

```

```
              <#TriplesMap> a rr:TriplesMap; #person, first source

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$".
                ].

              <#TriplesMap2> a rr:TriplesMap; #person, second source

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person2.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$.persons[*]".
                ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
              mapping:
                person:
                  sources:
                    - [data/person.json~jsonpath, $]
                    - [data/person2.json~jsonpath, "$.persons[*]"]

```

```
              <#TriplesMap> a rr:TriplesMap; #person, first source

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$".
                ].

              <#TriplesMap2> a rr:TriplesMap; #person, second source

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person2.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$.persons[*]".
                ].

```

If you describe a data source outside of the mappings, you can include via their unique key.

- YARRRML
- RML

```
              sources:
                person-source:
                  access: data/person.json
                  referenceFormulation: jsonpath
                  iterator: $

              mapping:
                person:
                  sources: person-source

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$".
                ].

```

Multiple sources can be used by using an array of source keys as value for the key `sources`.

- YARRRML
- RML

```
              sources:
                person-source:
                  access: data/person.json
                  referenceFormulation: jsonpath
                  iterator: $
                person-source2:
                  access: data/person2.json
                  referenceFormulation: jsonpath
                  iterator: "$.person[*]"

              mapping:
                person:
                  sources:
                    - person-source
                    - person-source2

```

```
              <#TriplesMap> a rr:TriplesMap; #person, first source

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$".
                ].

              <#TriplesMap2> a rr:TriplesMap; #person, second source

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person2.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$.persons[*]".
                ].

```

A combination of both sources defined outside and inside a mapping is possible.

- YARRRML
- RML

```
              sources:
                person-source:
                  access: data/person.json
                  referenceFormulation: jsonpath
                  iterator: $

              mapping:
                person:
                  sources:
                   - person-source
                   - access: data/person2.json
                     referenceFormulation: jsonpath
                     iterator: "$.persons[*]"

```

```
              <#TriplesMap> a rr:TriplesMap; #person, first source

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$".
                ].

              <#TriplesMap2> a rr:TriplesMap; #person, second source

                rml:logicalSource [
                  a rml:LogicalSource;
                  rml:source "data/person2.json";
                  rml:referenceFormulation ql:JSONPath;
                  rml:iterator "$.persons[*]".
                ].

```

## Targets

Besides defining targets at the root of the document, targets can also be defined inside a
mapping via the collection `targets`. However, no unique key is specified for a target,
and, thus, it cannot be referred to from other mappings. The key-value to add to a target are the
same when defining targets at the root of the document. In the following example the mapping `person` has one target.

- YARRRML
- RML

```
                mapping:
                  person:
                    subjects:
                      - value: "http://example.org/$(id)"
                        targets:
                          access: data/dump.ttl.gz
                          type: void
                          serialization: turtle
                          compression: gzip

```

```
                <#TriplesMap> a rr:TriplesMap;
                 rr:subjectMap [ a rr:SubjectMap;
                   rr:template "http://example.org/{id}";
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump
                     ];
                     rmlt:serialization formats:Turtle;
                     rmlt:compression comp:gzip.
                   ];
                 ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
                mapping:
                  person:
                    subjects:
                      - value: "http://example.org/$(id)"
                        targets:
                          - ["data/dump.ttl.gz~void", "turtle", "gzip"]

```

```
                <#TriplesMap> a rr:TriplesMap;
                 rr:subjectMap [ a rr:SubjectMap;
                   rr:template "http://example.org/{id}";
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump
                     ];
                     rmlt:serialization formats:Turtle;
                     rmlt:compression comp:gzip.
                   ];
                 ].

```

In case the output of a mapping needs to be exported to multiple targets, multiple targets
can be added to the targets collection. In the following example the `person` mapping
has two data sources.

- YARRRML
- RML

```
                mapping:
                  person:
                    subjects:
                      - value: "http://example.org/$(id)"
                        targets:
                          - access: data/dump1.nq
                            type: void
                          - access: data/dump2.nq
                            type: void

```

```
                <#TriplesMap> a rr:TriplesMap;
                 rr:subjectMap [ a rr:SubjectMap;
                   rr:template "http://example.org/{id}";
                   # Target 1
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump <file://data/dump1.nq>;
                     ];
                   ];
                   # Target 2
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump <file://data/dump2.nq>;
                     ];
                   ].
                 ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
                mapping:
                  person:
                    subjects:
                      - value: "http://example.org/$(id)"
                        targets:
                          - ["data/dump1.nq~void"]
                          - ["data/dump2.nq~void"]

```

```
                <#TriplesMap> a rr:TriplesMap;
                 rr:subjectMap [ a rr:SubjectMap;
                   rr:template "http://example.org/{id}";
                   # Target 1
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump <file://data/dump1.nq>;
                     ];
                   ];
                   # Target 2
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump <file://data/dump2.nq>;
                     ];
                   ].
                 ].

```

If you describe a target outside of the mappings, you can include via their unique key.

- YARRRML
- RML

```
                targets:
                  person-target:
                    access: data/dump.jsonld.gz
                    type: dcat
                    serialization: jsonld
                    compression: gzip

                mapping:
                  person:
                    subjects:
                      - value: "http://example.org/$(id)"
                        targets: person-target

```

```
                <#TriplesMap> a rr:TriplesMap;
                 rr:subjectMap [ a rr:SubjectMap;
                   rr:template "http://example.org/{id}";
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump <file://data/dump1.jsonld.gz>;
                     ];
                     rmlt:serialization formats:JSON-LD;
                     rmlt:compression comp:gzip;
                   ].
                 ].

```

Multiple targets can be used by using an array of target keys as value for the key `targets`.

- YARRRML
- RML

```
                targets:
                  person-target1:
                    access: data/dump.jsonld.gz
                    type: dcat
                    serialization: jsonld
                    compression: gzip
                  person-target2:
                    access: data/dump2.rdf
                    type: void
                    serialization: rdfxml

                mapping:
                  person:
                    subjects:
                      - value: "http://example.org/$(id)"
                        targets:
                          - person-target1
                          - person-target2

```

```
                <#TriplesMap> a rr:TriplesMap;
                 rr:subjectMap [ a rr:SubjectMap;
                   rr:template "http://example.org/{id}";
                   # Target 1
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump <file://data/dump1.jsonld.gz>;
                     ];
                     rmlt:serialization formats:JSON-LD;
                     rmlt:compression comp:gzip;
                   ];
                   # Target 2
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump <file://data/dump2.rdf>;
                     ];
                     rmlt:serialization formats:RDF_XML;
                   ];
                 ].

```

A combination of both targets defined outside and inside a mapping is possible.

- YARRRML
- RML

```
                targets:
                  person-target:
                    access: data/dump1.nq

                mapping:
                  person:
                    subjects:
                      - value: "http://example.org/$(id)"
                        targets:
                          - person-target
                          - access: data/dump2.nq

```

```
                <#TriplesMap> a rr:TriplesMap;
                 rr:subjectMap [ a rr:SubjectMap;
                   rr:template "http://example.org/{id}";
                   # Target 1
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump <file://data/dump1.nq>;
                     ];
                   ];
                   # Target 2
                   rml:logicalTarget [
                     a rmlt:LogicalTarget;
                     rmlt:target [ a void:Dataset;
                       void:dataDump <file://data/dump2.nq>;
                     ];
                   ].
                 ].

```

## Subjects

For every triple is required to define whether a IRI or blank node needs to used.
This information is added to a mapping via the collection `subjects`.
In the case of an IRI, this collection contains 0 or more templates that specify the IRI.
In the case of a blank node, this collection is set to `null` or is not specified at all.

In the following example the mapping `person` generate IRI for the subjects based on the template `http://wwww.example.com/person/$(id)`.

- YARRRML
- RML

```
              mappings:
                person:
                  subjects: http://wwww.example.com/person/$(id)

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:subjectMap [
                  a rr:SubjectMap;
                  rr:template "http://wwww.example.com/person/{id}"
                ].

```

It is also possible to specify multiple subjects.
In this case an array of templates is used.
In the following example the mapping `person` generate subjects based on the templates `http://wwww.example.com/person/$(id)` and `http://www.test.com/$(firstname)`.

- YARRRML
- RML

```
              mappings:
                person:
                  subjects: [http://wwww.example.com/person/$(id), http://www.test.com/$(firstname)]

```

```
              <#TriplesMap> a rr:TriplesMap; #person, first subject

                rr:subjectMap [
                  a rr:SubjectMap;
                  rr:template "http://wwww.example.com/person/{id}"
                ].

              <#TriplesMap2> a rr:TriplesMap; #person, second subject

                rr:subjectMap [
                  a rr:SubjectMap;
                  rr:template "http://www.test.com/{firstname}"
                ].

```

It is possible to apply functions on subjects.

## Predicates and objects

In the following example the mapping `person` generates combinations of predicates and objects,
where the predicate is `foaf:firstName` and the object is the `firstname` of each person.

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - predicates: foaf:firstName
                      objects: $(firstname)

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:firstName;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname"
                  ]
                ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - [foaf:firstName, $(firstname)]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:firstName;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname"
                  ]
                ].

```

It is possible to specify multiple predicates and objects.
In this case an array of templates is used.

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - predicates: [foaf:name, rdfs:label]
                      objects: [$(firstname), $(lastname)]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:name;
                  rr:predicate rdfs:label;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname"
                  ];
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "lastname"
                  ]
                ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - [[foaf:name, rdfs:label], [$(firstname), $(lastname)]]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:name;
                  rr:predicate rdfs:label;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname"
                  ];
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "lastname"
                  ]
                ].

```

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - predicates: foaf:knows
                      objects:
                        value: $(colleague)
                        type: iri

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:knows;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "colleague";
                    rr:TermType rr:IRI
                  ]
                ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - [[foaf:knows, rdfs:label], $(colleague)~iri]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:knows;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "colleague";
                    rr:TermType rr:IRI
                  ]
                ].

```

The inverse predicate can also be added.
This is only valid when the object is an IRI or a blank node.

```
          mappings:
            work:
              predicateobjects:
                - predicates: ex:createdBy
                  inversepredicates: ex:created
                  objects: $(foafprofile)
                  type: iri

```

## Datatypes

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - predicates: foaf:firstName
                      objects:
                        value: $(firstname)
                        datatype: xsd:string

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:firstName;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname";
                    rr:datatype xsd:string
                  ]
                ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - [foaf:firstName, $(firstname), xsd:string]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:firstName;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname";
                    rr:datatype xsd:string
                  ]
                ].

```

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - predicates: foaf:name
                      objects:
                        - value: $(firstname)
                          datatype: ex:string
                        - value: $(lastname)
                          datatype: ex:anotherString
                    - predicates: rdfs:label
                      objects:
                        - value: $(firstname)
                          datatype: ex:string
                        - value: $(lastname)
                          datatype: ex:anotherString

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:name;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname";
                    rr:datatype ex:string
                  ];
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "lastname";
                    rr:datatype ex:anotherString
                  ]
                ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - predicates: [foaf:name, rdfs:label]
                      objects: [[$(firstname), ex:string], [$(lastname), ex:anotherString]]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:name;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname";
                    rr:datatype ex:string
                  ];
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "lastname";
                    rr:datatype ex:anotherString
                  ]
                ].

```

## Languages

- YARRRML
- RML

```
                mappings:
                  person:
                    predicateobjects:
                      - predicates: foaf:firstName
                        objects:
                          value: $(firstname)
                          language: en

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:firstName;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname";
                    rr:language "en"
                  ]
                ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - [foaf:firstName, $(firstname), en~lang]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:firstName;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname";
                    rr:language "en"
                  ]
                ].

```

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - predicates: foaf:name
                      objects:
                        - value: $(firstname)
                          language: en
                        - value: $(lastname)
                          language: nl

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:name;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname";
                    rr:language "en"
                  ];
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "lastname";
                    rr:language "nl"
                  ]
                ].

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
              mappings:
                person:
                  predicateobjects:
                    - predicates: [foaf:name, rdfs:label]
                      objects: [[$(firstname), en~lang], [$(lastname), nl~lang]]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:name;
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "firstname";
                    rr:language "en"
                  ];
                  rr:objectMap [
                    a rr:ObjectMap;
                    rml:reference "lastname";
                    rr:language "nl"
                  ]
                ].

```

## Referring to other mappings

In certain use cases triples need to be generated between the records of two mappings.
For example, in the following example we have two mappings: persons and projects.
In the existing data there is for every person a field `projectID` referring to the project
on which the person is working.
Therefore, we want to generate triples between every person and his/her project.
The `objects` collection has an object with the key `mapping`.
The value of this key refers to the mapping that provides the IRIs that will serve as object for the predicate-object combination.
Furthermore, a condition is added, so that only persons and projects are linked when they are actually related, based on the `projectID` of the person and the `ID` of the project.
Note that a condition is not required.
But when a condition is used an extra value can be given to a parameter of a function.
This is either `s` or `o`. `s` means that the value of the parameter is coming from the subject of the relationship, while `o` means that the value is coming from the object of the relationship.
The default value is `s`.
In this example it would result in relationships between every person and their projects.

- YARRRML
- RML

```
              mappings:
                person:
                  subjects: http://example.com/person/$(ID)
                  predicateobjects:
                    - predicates: foaf:worksFor
                      objects:
                      - mapping: project
                        condition:
                          function: equal
                          parameters:
                            - [str1, $(projectID), s]
                            - [str2, $(ID), o]
                project:
                  subjects: http://example.com/project/$(ID)

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:subjectMap [
                  a rr:SubjectMap;
                  rr:template "http://example.com/person/{ID}"
                ]

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:worksFor;
                  rr:objectMap [
                    a rr:RefObjectMap;
                    rr:parentTriplesMap <#TriplesMap2>;
                    rr:joinCondition [
                      rr:child "projectID";
                      rr:parent "ID"
                    ]
                  ]
                ].

              <#TriplesMap2> a rr:TriplesMap; #person

                rr:subjectMap [
                  a rr:SubjectMap;
                  rr:template "http://example.com/project/{ID}"
                ]

```

## Graphs

### All triples

- YARRRML
- RML

```
                mappings:
                  person:
                    graphs: ex:myGraph

```

```
                <#TriplesMap> a rr:TriplesMap; #person

                  rr:subjectMap [
                    a rr:SubjectMap;
                    rr:graphMap [
                      a rr:GraphMap;
                      rr:template "http://example.org/myGraph"
                    ]
                  ].

```

### All triples with a specific predicate and object

- YARRRML
- RML

```
                mappings:
                  person:
                    predicateobjects:
                     - predicates: foaf:firstName
                       objects: $(firstname)
                       graphs: ex:myGraph

```

```
                <#TriplesMap> a rr:TriplesMap; #person

                  rr:predicateObjectMap [
                    a rr:PredicateObjectMap;
                    rr:predicate foaf:firstName;
                    rr:objectMap [
                      a rr:ObjectMap;
                      rr:template "{firstname}"
                    ];
                    rr:graphMap [
                      a rr:GraphMap;
                      rr:template "http://example.org/myGraph"
                    ]
                  ].

```

## Functions

Functions can be added to subjects, predicates, and objects.

- YARRRML
- RML

```
            mappings:
              person:
                predicateobjects:
                 - predicates: foaf:firstName
                   objects:
                    - function: ex:toLowerCase
                      parameters:
                       - parameter: ex:input
                         value: $(firstname)

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:firstName;
                  rr:objectMap <#FunctionMap>
                ].

                <#FunctionMap>
                  fnml:functionValue [
                    rml:logicalSource <#LogicalSource> ;
                    rr:predicateObjectMap [
                      rr:predicate fno:executes ;
                      rr:objectMap [ rr:constant ex:toLowerCase ]
                    ] ;

                    rr:predicateObjectMap [
                      rr:predicate ex:input ;
                      rr:objectMap [ rml:reference "firstname" ]
                    ]
                  ] .

```

A shortcut version of this example looks as follows.

- YARRRML
- RML

```
            mappings:
              person:
                predicateobjects:
                 - predicates: foaf:firstName
                   objects:
                    - function: ex:toLowerCase
                      parameters:
                       - [ex:input, $(firstname)]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:worksFor;
                  rr:objectMap <#FunctionMap>
                ].

                <#FunctionMap>
                  fnml:functionValue [
                    rml:logicalSource <#LogicalSource> ;
                    rr:predicateObjectMap [
                      rr:predicate fno:executes ;
                      rr:objectMap [ rr:constant ex:toLowerCase ]
                    ] ;

                    rr:predicateObjectMap [
                      rr:predicate ex:input ;
                      rr:objectMap [ rml:reference "firstname" ]
                    ]
                  ] .

```

Datatypes can also be assigned to the results of functions.

- YARRRML
- RML

```
            mappings:
              person:
                predicateobjects:
                 - predicates: ex:age
                   objects:
                    - function: ex:double
                      parameters:
                       - [ex:input, $(age)]
                      datatype: xsd:integer

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:worksFor;
                  rr:objectMap <#FunctionMap>
                ].

                <#FunctionMap>
                  rr:datatype xsd:integer;
                  fnml:functionValue [
                    rml:logicalSource <#LogicalSource> ;
                    rr:predicateObjectMap [
                      rr:predicate fno:executes ;
                      rr:objectMap [ rr:constant ex:toLowerCase ]
                    ] ;

                    rr:predicateObjectMap [
                      rr:predicate ex:input ;
                      rr:objectMap [ rml:reference "firstname" ]
                    ]
                  ] .

```

It possible to combine multiple functions, i.e., the value of a parameter of a function is the result of another function.

- YARRRML
- RML

```
            mappings:
              person:
                predicateobjects:
                 - predicates: schema:name
                   objects:
                    - function: ex:escape
                      parameters:
                       - parameter: ex:valueParameter
                         value:
                           function: ex:toUpperCase
                           parameters:
                             - [ex:valueParameter, $(name)]
                       - [ex:modeParameter, html]

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate schema:name;
                  rr:objectMap <#FunctionMap>
                ].

                <#FunctionMap>
                  fnml:functionValue [
                    rml:logicalSource <#LogicalSource> ;
                    rr:predicateObjectMap [
                      rr:predicate fno:executes ;
                      rr:objectMap [ rr:constant ex:escape ]
                    ] ;

                    rr:predicateObjectMap [
                      rr:predicate ex:valueParameter ;
                      rr:objectMap <#FunctionMap2>
                    ];

                    rr:predicateObjectMap [
                      rr:predicate ex:modeParameter ;
                      rr:objectMap [ rr:constant "html" ]
                    ]
                  ] .

                <#FunctionMap2>
                  fnml:functionValue [
                    rml:logicalSource <#LogicalSource> ;
                    rr:predicateObjectMap [
                      rr:predicate fno:executes ;
                      rr:objectMap [ rr:constant ex:toUpperCase ]
                    ] ;

                    rr:predicateObjectMap [
                      rr:predicate ex:valueParameter ;
                      rr:objectMap [ rml:reference "name" ]
                    ]
                  ] .

```

Additionally, it is possible to combine the function and its parameters in one line.
The function is followed by brackets (`(...)`),
every parameter-value pair is separated by a comma (`,`), and
parameters are separated from their value by an equal sign (`=`).

- YARRRML
- RML

```
            mappings:
              person:
                predicateobjects:
                 - predicates: foaf:firstName
                   objects:
                    - function: ex:toLowerCase(ex:input = $(firstname))

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:worksFor;
                  rr:objectMap <#FunctionMap>
                ].

                <#FunctionMap>
                  fnml:functionValue [
                    rml:logicalSource <#LogicalSource> ;
                    rr:predicateObjectMap [
                      rr:predicate fno:executes ;
                      rr:objectMap [ rr:constant ex:toLowerCase ]
                    ] ;

                    rr:predicateObjectMap [
                      rr:predicate ex:input ;
                      rr:objectMap [ rml:reference "firstname" ]
                    ]
                  ] .

```

Note that it is possible to exclude the prefix of the parameters
if it is the same as the prefix of the function:

- YARRRML
- RML

```
            mappings:
              person:
                predicateobjects:
                 - predicates: foaf:firstName
                   objects:
                    - function: ex:toLowerCase(input = $(firstname))

```

```
              <#TriplesMap> a rr:TriplesMap; #person

                rr:predicateObjectMap [
                  a rr:PredicateObjectMap;
                  rr:predicate foaf:worksFor;
                  rr:objectMap <#FunctionMap>
                ].

                <#FunctionMap>
                  fnml:functionValue [
                    rml:logicalSource <#LogicalSource> ;
                    rr:predicateObjectMap [
                      rr:predicate fno:executes ;
                      rr:objectMap [ rr:constant ex:toLowerCase ]
                    ] ;

                    rr:predicateObjectMap [
                      rr:predicate ex:input ;
                      rr:objectMap [ rml:reference "firstname" ]
                    ]
                  ] .

```

## Conditions

A subject or predicate-object combination is in certain cases only generated when a condition is fulfilled.
In the following example, the predicate-object is only generated when the `firstname` is valid.

```
          mappings:
            person:
              predicateobjects:
               - predicates: foaf:firstName
                 objects: $(firstname)
                 condition:
                  function: ex:isValid
                  parameters:
                   - [ex:input, $(firstname)]

```

In the following example, the mapping is only executed for every record that has set its `ID`.

```
          mappings:
            person:
              subjects: http://example.com/{ID}
              condition:
                  function: ex:isSet
                  parameters:
                   - [ex:input, $(ID)]
              predicateobjects:
               - predicates: foaf:firstName
                 objects: $(firstname)

```

## External references

It is possible to define references that do not refer to data in a data source.
These references are called "external references".
They are provided via the `external` key that has
as value a list of references with their values.
In the following example two external references are defined: `name` and `city` with as values `John` and `Ghent`.

```
          external:
            name: John
            city: Ghent

          mappings:
            person:
              subjects: http://example.org/$(id)
              po:
                - [ex:name, $(_name)]
                - [ex:firstName, $(_name)]
                - [ex:city, $(_city)]

```

Replacing the external references with their actual values results in the following.

```
          mappings:
            person:
              s: http://example.org/$(id)
              po:
                - [ex:name, John]
                - [ex:firstName, John]
                - [ex:city, Ghent]

```

If the value for an external reference is not provided, then the reference is not replaced.
In the following example no value is provided for `name`.

```
          external:
            city: Ghent

          mappings:
            person:
              subjects: http://example.org/$(id)
              po:
                - [ex:name, $(_name)]
                - [ex:firstName, $(_name)]
                - [ex:city, $(_city)]

```

Replacing the remaining external reference with its actual value results in the following.

```
          mappings:
            person:
              subjects: http://example.org/$(id)
              po:
                - [ex:name, $(_name)]
                - [ex:firstName, $(_name)]
                - [ex:city, Ghent]

```

`$(_name)` is not replaced.

If you want use a reference as both a regular and an external reference,
you add a `\` before the regular reference.
In the following example `$(_name)` is an external reference and `$(\_name)` is a regular reference.

```
          external:
            name: John

          mappings:
            person:
              subjects: http://example.org/$(id)
              po:
                - [ex:name, $(_name)]
                - [ex:firstName, $(\_name)]

```

Replacing the external reference with its actual value results in the following.

```
          mappings:
            person:
              subjects: http://example.org/$(id)
              po:
                - [ex:name, John]
                - [ex:firstName, $(_name)]

```

## Shortcuts

## Keys

- mappings: mapping, m
- subjects: subject, s
- predicates: predicate, p
- inversepredicates: inversepredicate, i
- objects: object, o
- predicateobjects: po
- function: fn, f
- parameters: pms
- parameter: pm
- value: v
- authors: author, a

## Predicates

- http://www.w3.org/1999/02/22-rdf-syntax-ns#type: a

## Reference implementation

The [YARRRML Parser](https://github.com/rmlio/yarrrml-parser) is a reference implementation that generates [R2]RML rules based on YARRRML.
The parser's code also includes tests to validate a parser's conformance to the YARRRML specification.
