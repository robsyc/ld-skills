---
title: "SPARQL 1.2 Query Results XML Format"
source: https://www.w3.org/TR/sparql12-results-xml/
family: sparql
version: "1.2"
status: W3C Working Draft
spec_date: 2024-12-27
fetched: 2026-11-02
---

# SPARQL 1.2 Query Results XML Format

> XML serialization of SPARQL results.

## Contents

- Abstract
- 1 Introduction
- 2 Definition
  - 2.1 Document Element
  - 2.2 Header
  - 2.3 Results
    - 2.3.1 Variable Binding Results
    - 2.3.2 Boolean Results
- 3 Examples
  - 3.1 Variable Binding Results Examples
  - 3.2 Variable Binding Results Examples with Triple Terms
  - 3.3 Boolean Results Examples
- 4 XML Schemas
- A Changes between SPARQL Query Results XML Format (Second Edition) and SPARQL 1.2 Query Results XML Format
- B Internet Media Type, File Extension and Macintosh File Type
- Internet Media Type Registration Form
- C Privacy Considerations
- D Security Considerations
- E Internationalization Considerations
- F Index
  - F.1 Terms defined by this specification
  - F.2 Terms defined by reference
- G References
  - G.1 Informative references

---

## Abstract

## 1. Introduction

The [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/) defines several *Query
Result Forms* ([SPARQL Query section 10](https://www.w3.org/TR/sparql12-query/#QueryForms)). This document defines a SPARQL Results Document that encodes the variable binding query results from `SELECT` queries ([SPARQL Query section 10.2](https://www.w3.org/TR/sparql12-query/#select)) and boolean query results from `ASK` queries ([SPARQL Query section 10.5](https://www.w3.org/TR/sparql12-query/#ask)) in [XML](https://www.w3.org/TR/xml/#).

There are two other results formats which follow a similar design but do not use XML: [SPARQL 1.2 Query Results JSON Format](https://www.w3.org/TR/sparql12-results-json/) and [SPARQL 1.2 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql12-results-csv-tsv/).

## 2. Definition

**Definition:** SPARQL Results Document

A SPARQL Results Document is an XML document that is valid with respect to either the RELAX NG XML Schema or the W3C XML Schema in Section 4. (§4)

### 2.1 Document Element

The SPARQL Results Document begins with `sparql` document element in the `http://www.w3.org/2005/sparql-results#` namespace, written as follows:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#"
  xmlns:its="http://www.w3.org/2005/11/its"
  its:version="2.0">
 ...
</sparql>
```

Inside the `sparql` element are two sub-elements, `head` and a results element (either `results` or `boolean`) which must appear in that order.

If no literals with base direction appear in the results, the `sparql` document element may be simplified as follows.

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">
 ...
</sparql>
```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Different values of `its:version` are allowed.

### 2.2 Header

The `head` element is the first child element of the `sparql` element.

For a variable binding query result, `head` must contain a sequence of elements describing the set of [Query Variable](https://www.w3.org/TR/sparql12-query/#defn_QueryVariable) names in the [Solution Sequence](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionSequence) (here called query results).

The order of the variable names in the sequence is the order of the variable names given to the argument of the `SELECT` statement in the SPARQL query. If `SELECT *` is
used, the order of the names is undefined.

Inside the `head` element, the ordered sequence of variable names chosen are used to create empty child elements `variable` with the variable name as the value of an
attribute `name` giving a document like this:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#"
  xmlns:its="http://www.w3.org/2005/11/its"
  its:version="2.0">

  <head>
    <variable name="x"/>
    <variable name="hpage"/>
    <variable name="name"/>
    <variable name="mbox"/>
    <variable name="blurb"/>
  </head>
...
</sparql>
```

For a boolean query result, no elements are required inside `head` and `variable` must not be present.

For any query result, `head` may also contain `link` child elements with an `href` attribute containing a relative URI that provides a link to some additional
metadata about the query results. The relative URI is resolved against the in-scope base URI which is usually the query results format document URI. `link` elements must appear after any `variable` elements that are present.

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#"
  xmlns:its="http://www.w3.org/2005/11/its"
  its:version="2.0">

  <head>
    ...
    <link href="metadata.rdf"/>
  </head>
...
</sparql>
```

### 2.3 Results

The second child-element of `sparql` must appear after `head` and is either `results` or `boolean`. It is written even if the query results are
empty.

#### 2.3.1 Variable Binding Results

The `results` element contains the complete sequence of query results.

For each [Query Solution](https://www.w3.org/TR/sparql12-query/#defn_sparqlSolutionMapping) in the query results, a `result` child-element of `results` is added giving a document like:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#"
  xmlns:its="http://www.w3.org/2005/11/its"
  its:version="2.0">
  ...  head ...

  <results>
    <result>...
    </result>
    <result>...
    </result>
    ...
  </results>

</sparql>
```

Each `result` element corresponds to one *Query Solution* in a result and contains child elements (in no particular order) for each *Query Variable* that appears in the
solution. It is used to record how the query variables bind to [RDF Terms](https://www.w3.org/TR/rdf12-concepts/#dfn-rdf-term).

Each binding inside a solution is written as an element `binding` as a child of `result` with the query variable name as the value of the `name` attribute. So
for a result binding two variables *x* and *hpage* it would look like:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#"
  xmlns:its="http://www.w3.org/2005/11/its"
  its:version="2.0">
  <head>
    <variable name="x"/>
    <variable name="hpage"/>
  </head>

  <results>
    <result>
      <binding name="x"> ... </binding>
      <binding name="hpage"> ... </binding>
    </result>

    <result>
      <binding name="x"> ... </binding>
      <binding name="hpage"> ... </binding>
    </result>
    ...
  </results>

</sparql>
```

The value of a query variable binding, which is an *RDF Term*, is included as the content of the `binding` as follows:

RDF URI Reference *U*

`<binding><uri>`*U*`</uri></binding>`

RDF Literal *S*

`<binding><literal>`*S*`</literal></binding>`

RDF Literal *S* with language *L* without base direction

`<binding><literal xml:lang="`*L*`">`*S*`</literal></binding>`

RDF Literal *S* with language *L* with base direction *L*

`<binding><literal xml:lang="`*L*`" its:dir="`*B*`">`*S*`</literal></binding>`

RDF Typed Literal *S* with datatype URI *D*

`<binding><literal datatype="`*D*`">`*S*`</literal></binding>`

Blank Node label *I*

`<binding><bnode>`*I*`</bnode></binding>`

Triple Term, with subject *S*, predicate *P*, object *O*

`<binding>`
`   <triple>`
`     <subject>`*S*`</subject>`
`     <predicate>`*P*`</predicate>`
`     <object>`*O*`</object>`
`   </triple>`
` </binding>`

If, for a particular solution, a variable is *unbound*, no `binding` element for that variable is included in the `result` element.

*S*, *P*, and *O* in Triple Terms are encoded recursively, using the same format, without the enclosing `<binding>` tag

**Note:** The blank node label *I* is scoped to the result set XML document and need not have any association to the blank node label for that RDF Term in the query
graph.

An example of a query solution encoded in this format is as follows:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#"
  xmlns:its="http://www.w3.org/2005/11/its"
  its:version="2.0">

  <head>
    <variable name="x"/>
    <variable name="hpage"/>
    <variable name="name"/>
    <variable name="age"/>
    <variable name="mbox"/>
    <variable name="friend"/>
  </head>

  <results>

    <result>
      <binding name="x">
        <bnode>r2</bnode>
      </binding>
      <binding name="hpage">
        <uri>http://work.example.org/bob/</uri>
      </binding>
      <binding name="name">
        <literal xml:lang="en">Bob</literal>
      </binding>
      <binding name="age">
        <literal datatype="http://www.w3.org/2001/XMLSchema#integer">30</literal>
      </binding>
      <binding name="mbox">
        <uri>mailto:bob@work.example.org</uri>
      </binding>

    ...
  </results>

</sparql>
```

An example of a query solution that includes triple terms is as follows:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#"
  xmlns:its="http://www.w3.org/2005/11/its"
  its:version="2.0">

  <head>
    <variable name="x"/>
    <variable name="name"/>
    <variable name="triple"/>
  </head>

  <results>

    <result>
      <binding name="x">
        <bnode>r2</bnode>
      </binding>
      <binding name="name">
        <literal xml:lang="en">Bob</literal>
      </binding>
      <binding name="triple">
        <triple>
            <subject>
                <uri>http://example.org/alice</uri>
            </subject>
            <predicate>
                <uri>http://example.org/name</uri>
            </predicate>
            <object>
                <literal datatype="http://www.w3.org/2001/XMLSchema#string">Alice</literal>
            </object>
        </triple>
      </binding>
    </result>

    ...
  </results>

</sparql>
```

As an alternative to including the `xml:its` declaration in every result
set, the namespace can be declared on specific elements as needed:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">
  <head>
    <variable name="animal"/>
  </head>
  <results>
    <result>
      <binding name="animal">
        <literal xmlns:its="http://www.w3.org/2005/11/its" its:version="2.0"
                 xml:lang="ar" its:dir="rtl">قطة</literal>
      </binding>
    </result>
    <result>
      <binding name="animal">
        <literal xml:lang="en">cat</literal>
      </binding>
    </result>
    <result>
      <binding name="animal">
        <literal xmlns:its="http://www.w3.org/2005/11/its" its:version="2.0"
                 xml:lang="fr" its:dir="ltr">chat</literal>
      </binding>
    </result>
  </results>
</sparql>
```

#### 2.3.2 Boolean Results

A boolean result is written as the element content of a `boolean` child-element of the `sparql` element directly after a `head`, containing either `true` or `false` as follows:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">
  ...  head ...

  <boolean>true</boolean>

</sparql>
```

## 3. Examples

### 3.1 Variable Binding Results Examples

An example `SELECT` SPARQL Query in [example.rq](https://www.w3.org/TR/sparql12-results-xml/example.rq) operating on query graph Turtle/N3 data in [data.ttl](https://www.w3.org/TR/sparql12-results-xml/data.ttl) providing ordered variable binding query results written in XML in [output.srx](https://www.w3.org/TR/sparql12-results-xml/output.srx).

This XML can be transformed into XHTML using the sample XML Query script [result-to-html.xq](https://www.w3.org/TR/sparql12-results-xml/result-to-html.xq) giving [output-xquery.html](https://www.w3.org/TR/sparql12-results-xml/output-xquery.html) or with XSLT sheet [result-to-html.xsl](https://www.w3.org/TR/sparql12-results-xml/result-to-html.xsl) giving [output-xslt.html](https://www.w3.org/TR/sparql12-results-xml/output-xslt.html)

### 3.2 Variable Binding Results Examples with Triple Terms

An example `SELECT` SPARQL Query in [example-triple-terms.rq](https://www.w3.org/TR/sparql12-results-xml/example-triple-terms.rq) operating on query graph Turtle/N3 data in [data.ttl](https://www.w3.org/TR/sparql12-results-xml/data.ttl) providing ordered variable binding query results written in XML in [output-triple-terms.srx](https://www.w3.org/TR/sparql12-results-xml/output-triple-terms.srx). These results contain triple terms.

### 3.3 Boolean Results Examples

An example `ASK` SPARQL Query in [example2.rq](https://www.w3.org/TR/sparql12-results-xml/example2.rq) operating on query graph Turtle/N3 data in [data.ttl](https://www.w3.org/TR/sparql12-results-xml/data.ttl) provides a boolean query result written in XML in [output2.srx](https://www.w3.org/TR/sparql12-results-xml/output2.srx).

This XML can be transformed into XHTML using the sample XML Query script [result-to-html.xq](https://www.w3.org/TR/sparql12-results-xml/result-to-html.xq) giving [output-xquery2.html](https://www.w3.org/TR/sparql12-results-xml/output-xquery2.html) or with XSLT sheet [result-to-html.xsl](https://www.w3.org/TR/sparql12-results-xml/result-to-html.xsl) giving [output-xslt2.html](https://www.w3.org/TR/sparql12-results-xml/output-xslt2.html)

## 4. XML Schemas

There are normative XML schemas provided in the following formats:

1. RELAX NG [RELAXNG] Compact [RELAXNG-COMPACT] in [result.rnc](https://www.w3.org/TR/sparql12-results-xml/result.rnc)
2. RELAX NG XML in [result.rng](https://www.w3.org/TR/sparql12-results-xml/result.rng)
3. W3C XML Schema [XMLSCHEMA-1] in [result.xsd](https://www.w3.org/TR/sparql12-results-xml/result.xsd)
   Note: this schema is machine-generated from the RELAX NG XML schema.

If W3C XML Schema is used, an `xsi:schemaLocation` attribute can be used pointing to the schema as follows:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.w3.org/2005/sparql-results# http://www.w3.org/2007/SPARQL/result.xsd">

  ...

</sparql>
```

## A. Changes between SPARQL Query Results XML Format (Second Edition) and SPARQL 1.2 Query Results XML Format

*This section is non-normative.*

- The document title changed from "SPARQL Query Results XML Format (Second Edition)" to "SPARQL 1.2 Query Results XML Format"
- Add RNC, RNG, and XSD files
- Allow triple terms to be expressed in 2.3.1 Variable Binding Results (§2.3.1)
- Use Media Type language instead of MIME Type in B. Internet Media Type, File Extension and Macintosh File Type (§B)
- Support directional language-tagged strings in 2.3.1 Variable Binding Results (§2.3.1)

## B. Internet Media Type, File Extension and Macintosh File Type

The Internet Media Type (formerly known as MIME Type) for the SPARQL Query Results XML Format is "application/sparql-results+xml".

It is recommended that result files have the extension ".srx" (all lowercase) on all platforms.

It is recommended that result files stored on Macintosh HFS file systems be given a file type of "TEXT".

## Internet Media Type Registration Form

Type name:

application

Subtype name:

sparql-results+xml

Required parameters:

None

Optional parameters:

"charset": This parameter has identical semantics to the charset parameter of the "application/xml" media type as specified in [RFC3023], section 3.2.

Encoding considerations:

Identical to those of "application/xml" as specified in [RFC3023], section 3.2.

Security considerations:

SPARQL query results uses URIs. See Section 7 of [RFC3986].

SPARQL query results uses IRIs. See Section 8 of [RFC3987].

As this media type uses the "+xml" convention, it shares the same security considerations as described in [RFC3023], section 10.

Interoperability considerations:

There are no known interoperability issues.

Published specification:

This specification.

Applications which use this media type:

No known applications currently use this media type.

Additional information:

Magic number(s):

As specified for "application/xml" in [RFC3023], section 3.2.

File extension(s):

".srx"

Fragment identifiers:

Identical to that of "application/xml" as described in [RFC3023], section 5.

Base URI:

As specified in [RFC3023], section 6.

Macintosh file type code(s):

"TEXT"

Person & email address to contact for further information:

Dave Beckett, Eric Prud'hommeaux <public-rdf-dawg-comments@w3.org>

Intended usage:

COMMON

Restrictions on usage:

None

Author/Change controller:

The SPARQL specification is a work product of the World Wide Web Consortium's RDF Data Access Working Group. The W3C has change control over these specifications.

## C. Privacy Considerations

TODO

## D. Security Considerations

TODO

## E. Internationalization Considerations

TODO

## F. Index

### F.1 Terms defined by this specification

### F.2 Terms defined by reference

- [RDF12-CONCEPTS] defines the following:
  * RDF Terms
- [SPARQL12-QUERY] defines the following:
  * Query Solution
  * Query Variable
  * Solution Sequence
  * SPARQL Query section 10
  * SPARQL Query section 10.2
  * SPARQL Query section 10.5
- [XML] defines the following:
  * XML

## G. References

### G.1 Informative references

[RDF12-CONCEPTS]

[RDF 1.2 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf12-concepts/). Olaf Hartig; Pierre-Antoine Champin; Gregg Kellogg; Andy Seaborne. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/rdf12-concepts/>

[RELAXNG]

[RELAX NG Specification](http://www.oasis-open.org/committees/relax-ng/spec-20011203.html). James Clark; Murata Makoto. OASIS. 3 December 2001. URL: <http://www.oasis-open.org/committees/relax-ng/spec-20011203.html>

[RELAXNG-COMPACT]

[RELAX NG Compact Syntax](http://www.oasis-open.org/committees/relax-ng/compact-20021121.html). James Clark. OASIS. 21 November 2002. URL: <http://www.oasis-open.org/committees/relax-ng/compact-20021121.html>

[RFC3023]

[XML Media Types](https://www.rfc-editor.org/rfc/rfc3023). M. Murata; S. St. Laurent; D. Kohn. IETF. January 2001. Proposed Standard. URL: <https://www.rfc-editor.org/rfc/rfc3023>

[RFC3986]

[Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986). T. Berners-Lee; R. Fielding; L. Masinter. IETF. January 2005. Internet Standard. URL: <https://www.rfc-editor.org/rfc/rfc3986>

[RFC3987]

[Internationalized Resource Identifiers (IRIs)](https://www.rfc-editor.org/rfc/rfc3987). M. Duerst; M. Suignard. IETF. January 2005. Proposed Standard. URL: <https://www.rfc-editor.org/rfc/rfc3987>

[SPARQL12-CONCEPTS]

[SPARQL 1.2 Concepts](https://w3c.github.io/sparql-concepts/spec/). The W3C RDF-star Working Group. W3C. W3C Working Draft. URL: <https://w3c.github.io/sparql-concepts/spec/>

[SPARQL12-ENTAILMENT]

[SPARQL 1.2 Entailment Regimes](https://www.w3.org/TR/sparql12-entailment/). Peter Patel-Schneider. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-entailment/>

[SPARQL12-FEDERATED-QUERY]

[SPARQL 1.2 Federated Query](https://www.w3.org/TR/sparql12-federated-query/). Ruben Taelman; Gregory Williams. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-federated-query/>

[SPARQL12-GRAPH-STORE-PROTOCOL]

[SPARQL 1.2 Graph Store Protocol](https://www.w3.org/TR/sparql12-graph-store-protocol/). Andy Seaborne; Thomas Pellissier Tanon. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-graph-store-protocol/>

[SPARQL12-NEW]

[What’s New in SPARQL 1.2](https://w3c.github.io/sparql-new/spec/). The W3C RDF-star Working Group. W3C. W3C Working Draft. URL: <https://w3c.github.io/sparql-new/spec/>

[SPARQL12-PROTOCOL]

[SPARQL 1.2 Protocol](https://www.w3.org/TR/sparql12-protocol/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-protocol/>

[SPARQL12-QUERY]

[SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/). Olaf Hartig; Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-query/>

[SPARQL12-RESULTS-CSV-TSV]

[SPARQL 1.2 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql12-results-csv-tsv/). Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-csv-tsv/>

[SPARQL12-RESULTS-JSON]

[SPARQL 1.2 Query Results JSON Format](https://www.w3.org/TR/sparql12-results-json/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-results-json/>

[SPARQL12-SERVICE-DESCRIPTION]

[SPARQL 1.2 Service Description](https://www.w3.org/TR/sparql12-service-description/). Ruben Taelman; Gregory Williams. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-service-description/>

[SPARQL12-UPDATE]

[SPARQL 1.2 Update](https://www.w3.org/TR/sparql12-update/). Ruben Taelman; Andy Seaborne; Thomas Pellissier Tanon. W3C. 19 December 2024. W3C Working Draft. URL: <https://www.w3.org/TR/sparql12-update/>

[XML]

[Extensible Markup Language (XML) 1.0 (Fifth Edition)](https://www.w3.org/TR/xml/). Tim Bray; Jean Paoli; Michael Sperberg-McQueen; Eve Maler; François Yergeau et al. W3C. 26 November 2008. W3C Recommendation. URL: <https://www.w3.org/TR/xml/>

[XMLSCHEMA-1]

[XML Schema Part 1: Structures Second Edition](https://www.w3.org/TR/xmlschema-1/). Henry Thompson; David Beech; Murray Maloney; Noah Mendelsohn et al. W3C. 28 October 2004. W3C Recommendation. URL: <https://www.w3.org/TR/xmlschema-1/>

Permalink

**Referenced in:**

- § 2.3.1 Variable Binding Results

Permalink

**Referenced in:**

- § 2.3.1 Variable Binding Results

Permalink

**Referenced in:**

- § 2.2 Header

Permalink

**Referenced in:**

- § 2.2 Header

Permalink

**Referenced in:**

- § 1. Introduction

Permalink

**Referenced in:**

- § 1. Introduction

Permalink

**Referenced in:**

- § 1. Introduction

Permalink

**Referenced in:**

- § 1. Introduction
