---
title: "SPARQL Query Results XML Format (Second Edition)"
source: https://www.w3.org/TR/sparql11-results-xml/
family: sparql
version: "1.1"
status: W3C Recommendation
spec_date: 2013-03-21
fetched: 2026-10-26
---

# SPARQL Query Results XML Format (Second Edition)

> XML results (1.1 Recommendation, 2nd edition).

## Contents

- Abstract
    - 1 May Be Superseded
    - 2 Set of Documents
    - No Substantive Changes
    - Please Send Comments
    - Endorsed By W3C
    - 3 Patents
- 1 Introduction
- 2 Definition
  - 2.1 Document Element
  - 2.2 Header
  - 2.3 Results
  - 2.3.1 Variable Binding Results
  - 2.3.2 Boolean Results
- 3 Examples
- 3.1 Variable Binding Results Examples
- 3.2 Boolean Results Examples
- 4 XML Schemas
- 5 Internet Media Type, File Extension and Macintosh File Type
  - Internet Media Type Registration Form
  - References
- 6 References
- Change Log
  - Changes since Proposed Edited Recommendation
  - Changes since 2008 Recommendation

---

---

## Abstract

RDF is a flexible, extensible way to represent information
about World Wide Web resources. It is used to represent, among
other things, personal information, social networks, metadata
about digital artifacts like music and images, as well as
provide a means of integration over disparate sources of
information. A standardized query language for RDF data with
multiple implementations offers developers and end users a way
to write and to consume the results of queries across this wide
range of information.

This document describes an XML format for the variable binding
and boolean results formats provided by the SPARQL query language for RDF, developed by the [W3C RDF Data Access Working Group](https://www.w3.org/2001/sw/DataAccess/) (DAWG), part of the [Semantic Web Activity](https://www.w3.org/2001/sw/) as described in the [activity statement](https://www.w3.org/2001/sw/Activity) .

#### May Be Superseded

*This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at http://www.w3.org/TR/.*

#### Set of Documents

This document is one of eleven SPARQL 1.1 Recommendations produced by the [SPARQL Working Group](https://www.w3.org/2001/sw/DataAccess/):

1. [SPARQL 1.1 Overview](https://www.w3.org/TR/2013/REC-sparql11-overview-20130321)
2. [SPARQL 1.1 Query Language](https://www.w3.org/TR/2013/REC-sparql11-query-20130321)
3. [SPARQL 1.1 Update](https://www.w3.org/TR/2013/REC-sparql11-update-20130321)
4. [SPARQL1.1 Service Description](https://www.w3.org/TR/2013/REC-sparql11-service-description-20130321)
5. [SPARQL 1.1 Federated Query](https://www.w3.org/TR/2013/REC-sparql11-federated-query-20130321)
6. [SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/2013/REC-sparql11-results-json-20130321)
7. [SPARQL 1.1 Query Results CSV and TSV Formats](https://www.w3.org/TR/2013/REC-sparql11-results-csv-tsv-20130321)
8. [SPARQL Query Results XML Format (Second Edition)](https://www.w3.org/TR/2013/REC-rdf-sparql-XMLres-20130321)
9. [SPARQL 1.1 Entailment Regimes](https://www.w3.org/TR/2013/REC-sparql11-entailment-20130321)
10. [SPARQL 1.1 Protocol](https://www.w3.org/TR/2013/REC-sparql11-protocol-20130321)
11. [SPARQL 1.1 Graph Store HTTP Protocol](https://www.w3.org/TR/2013/REC-sparql11-http-rdf-update-20130321)

#### No Substantive Changes

There have been no substantive changes to this document since the [previous version](https://www.w3.org/TR/2012/PER-rdf-sparql-XMLres-20121108/). Minor editorial changes, if any, are detailed in the change log and visible in the [color-coded diff](https://www.w3.org/TR/sparql11-results-xml/diff).

#### Please Send Comments

Please send any comments to <public-rdf-dawg-comments@w3.org> ([public archive](http://lists.w3.org/Archives/Public/public-rdf-dawg-comments/)). Although work on this document by the [SPARQL Working Group](https://www.w3.org/2009/sparql/) is complete, comments may be addressed in the [errata](https://www.w3.org/2013/sparql-errata) or in future revisions. Open discussion is welcome at <public-sparql-dev@w3.org> ([public archive](http://lists.w3.org/Archives/Public/public-sparql-dev/)).

#### Endorsed By W3C

*This document has been reviewed by W3C Members, by software developers, and by other W3C groups and interested parties, and is endorsed by the Director as a W3C Recommendation. It is a stable document and may be used as reference material or cited from another document. W3C's role in making the Recommendation is to draw attention to the specification and to promote its widespread deployment. This enhances the functionality and interoperability of the Web.*

#### Patents

*This document was produced by a group operating under the [5 February 2004 W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy-20040205/). W3C maintains a [public list of any patent disclosures](https://www.w3.org/2004/01/pp-impl/35463/status) made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains [Essential Claim(s)](https://www.w3.org/Consortium/Patent-Policy-20040205/#def-essential) must disclose the information in accordance with [section 6 of the W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy-20040205/#sec-Disclosure).*

---

## 1. Introduction

The [SPARQL Query Language for RDF](https://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/) [SPARQL-QUERY](https://www.w3.org/TR/sparql11-results-xml/#ref-sparql-query) defines several *Query Result Forms* ([SPARQL Query section 10](https://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/#QueryForms)).
This document defines a SPARQL Results Document that encodes
the variable binding query results from `SELECT` queries
([SPARQL Query section 10.2](https://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/#select))
and boolean query results from `ASK` queries
([SPARQL Query section 10.5](https://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/#ask))
in [XML](https://www.w3.org/TR/2004/REC-xml-20040204/) [XML](https://www.w3.org/TR/sparql11-results-xml/#ref-xml).

There are two other results formats which follow a similar design but do not use XML: [SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/sparql11-results-json/) [SRJ] and [SPARQL 1.1 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql11-results-csv-tsv/) [SRC].

## 2. Definition

**Definition:** SPARQL Results Document

A SPARQL Results Document is an
XML document that is valid with respect to either the
RELAX NG XML Schema or the W3C XML Schema in Section 4. (§4)

### 2.1. Document Element

The SPARQL Results Document begins with `sparql` document element in the `http://www.w3.org/2005/sparql-results#` namespace,
written as follows:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">
 ...
</sparql>
```

Inside the `sparql` element are two sub-elements, `head` and
a results element (either `results` or `boolean`)
which must appear in that order.

### 2.2. Header

The `head` element is the first child element of
the `sparql` element.

For a variable binding query result, `head` must contain a
sequence of elements describing the set of [Query Variable](https://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/#defn_QueryVariable) names in the [Solution Sequence](https://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/#defn_sparqlSolutionSequence) (here called query results).

The order of the variable names in the sequence is the order of
the variable names given to the argument of the `SELECT` statement in the SPARQL query. If `SELECT *` is used, the
order of the names is undefined.

Inside the `head` element, the ordered sequence of
variable names chosen are used to create empty child elements `variable` with the variable name as the value of an
attribute `name` giving a document like this:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">

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

For any query result, `head` may also contain `link` child elements with an `href` attribute
containing a relative URI that provides a link to some additional
metadata about the query results. The relative URI is resolved
against the in-scope base URI which is usually the query results
format document URI. `link` elements must appear after
any `variable` elements that are present.

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">

  <head>
    ...
    <link href="metadata.rdf"/>
  </head>
...
</sparql>
```

### 2.3. Results

The second child-element of `sparql` must appear after `head` and is either `results` or `boolean`.
It is written even if the query results are empty.

### 2.3.1. Variable Binding Results

The `results` element contains the complete sequence of
query results.

For each [Query Solution](https://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/#defn_sparqlSolutionMapping) in the query results, a `result` child-element of `results` is added giving
a document like:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">
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

Each `result` element corresponds to one *Query
Solution* in a result and contains child elements (in no particular order) for each *Query
Variable* that appears in the solution. It
is used to record how the query variables bind to [RDF Term](https://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/#defn_RDFTerm)s.

Each binding inside a solution is written as an element `binding` as a child of `result` with the query
variable name as the value of the `name` attribute. So for a
result binding two variables *x* and *hpage* it would
look like:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">
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

The value of a query variable binding, which is an *RDF Term*, is
included as the content of the `binding` as follows:

RDF URI Reference *U*

`<binding><uri>`*U*`</uri></binding>`

RDF Literal *S*

`<binding><literal>`*S*`</literal></binding>`

RDF Literal *S* with language *L*

`<binding><literal xml:lang="`*L*`">`*S*`</literal></binding>`

RDF Typed Literal *S* with datatype URI *D*

`<binding><literal datatype="`*D*`">`*S*`</literal></binding>`

Blank Node label *I*

`<binding><bnode>`*I*`</bnode></binding>`

If, for a particular solution, a variable is *unbound*, no `binding` element for that variable is included in the `result` element.

**Note:** The blank node label *I* is scoped
to the result set XML document and need not have any association to
the blank node label for that RDF Term in the query graph.

An example of a query solution encoded in this format is as follows:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">

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
    </result>

    ...
  </results>

</sparql>
```

### 2.3.2. Boolean Results

A boolean result is written as the element content of a `boolean` child-element of the `sparql` element directly after a `head`,
containing either `true` or `false` as follows:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">
  ...  head ...

  <boolean>true</boolean>

</sparql>
```

## 3. Examples

## 3.1. Variable Binding Results Examples

An example `SELECT` SPARQL Query in [example.rq](https://www.w3.org/2009/sparql/xml-results/example.rq) operating
on query graph Turtle/N3 data in [data.n3](https://www.w3.org/2009/sparql/xml-results/data.n3) providing ordered variable binding query results written in XML
in [output.srx](https://www.w3.org/2009/sparql/xml-results/output.srx).

This XML can be transformed into XHTML using the
sample XML Query script [result-to-html.xq](https://www.w3.org/2009/sparql/xml-results/result-to-html.xq) giving [output-xquery.html](https://www.w3.org/2009/sparql/xml-results/output-xquery.html) or with
XSLT sheet [result-to-html.xsl](https://www.w3.org/2009/sparql/xml-results/result-to-html.xsl) giving [output-xslt.html](https://www.w3.org/2009/sparql/xml-results/output-xslt.html)

## 3.2. Boolean Results Examples

An example `ASK` SPARQL Query in [example2.rq](https://www.w3.org/2009/sparql/xml-results/example2.rq) operating
on query graph Turtle/N3 data in [data.n3](https://www.w3.org/2009/sparql/xml-results/data.n3) provides a boolean query result written in XML
in [output2.srx](https://www.w3.org/2009/sparql/xml-results/output2.srx).

This XML can be transformed into XHTML using the
sample XML Query script [result-to-html.xq](https://www.w3.org/2009/sparql/xml-results/result-to-html.xq) giving [output-xquery2.html](https://www.w3.org/2009/sparql/xml-results/output-xquery2.html) or with
XSLT sheet [result-to-html.xsl](https://www.w3.org/2009/sparql/xml-results/result-to-html.xsl) giving [output-xslt2.html](https://www.w3.org/2009/sparql/xml-results/output-xslt2.html)

## 4. XML Schemas

There are normative XML schemas provided in the following formats:

1. RELAX NG[RELAXNG](https://www.w3.org/TR/sparql11-results-xml/#ref-relaxng) Compact[RELAXNG-COMPACT](https://www.w3.org/TR/sparql11-results-xml/#ref-relaxng-nx) in [result.rnc](https://www.w3.org/2007/SPARQL/result.rnc)
2. RELAX NG XML in [result.rng](https://www.w3.org/2007/SPARQL/result.rng)
3. W3C XML Schema[XMLSCHEMA-1](https://www.w3.org/TR/sparql11-results-xml/#ref-xmlschema-1) in [result.xsd](https://www.w3.org/2007/SPARQL/result.xsd)
   Note: this schema is machine-generated from the RELAX NG XML schema.

If W3C XML Schema is used, an `xsi:schemaLocation` attribute can be used pointing to the schema as follows:

```
<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.w3.org/2007/SPARQL/result.xsd">

  ...

</sparql>
```

## 5. Internet Media Type, File Extension and Macintosh File Type

The Internet Media Type / MIME Type for the SPARQL Query Results XML
Format is "application/sparql-results+xml".

It is recommended that result files have the extension ".srx" (all
lowercase) on all platforms.

It is recommended that result files stored on Macintosh HFS file
systems be given a file type of "TEXT".

### Internet Media Type Registration Form

Type name:

application

Subtype name:

sparql-results+xml

Required parameters:

None

Optional parameters:

"charset": This parameter has identical semantics to the charset
parameter of the "application/xml" media type as
specified in [RFC3023](https://www.w3.org/TR/sparql11-results-xml/#mime-rfc-3023), section 3.2.

Encoding considerations:

Identical to those of "application/xml" as specified in [RFC3023](https://www.w3.org/TR/sparql11-results-xml/#mime-rfc-3023),
section 3.2.

Security considerations:

SPARQL query results uses URIs. See Section 7 of [RFC3986](https://www.w3.org/TR/sparql11-results-xml/#mime-rfc-3986).

SPARQL query results uses IRIs. See Section 8 of [RFC3987](https://www.w3.org/TR/sparql11-results-xml/#mime-rfc-3987).

As this media type uses the "+xml" convention, it shares the same
security considerations as described in [RFC3023](https://www.w3.org/TR/sparql11-results-xml/#mime-rfc-3023), section 10.

Interoperability considerations:

There are no known interoperability issues.

Published specification:

This specification.

Applications which use this media type:

No known applications currently use this media type.

Additional information:

Magic number(s):

As specified for "application/xml" in [RFC3023](https://www.w3.org/TR/sparql11-results-xml/#mime-rfc-3023), section 3.2.

File extension(s):

".srx"

Fragment identifiers:

Identical to that of "application/xml" as described in RFC 3023 [RFC3023](https://www.w3.org/TR/sparql11-results-xml/#mime-rfc-3023), section 5.

Base URI:

As specified in [RFC3023](https://www.w3.org/TR/sparql11-results-xml/#mime-rfc-3023), section 6.

Macintosh file type code(s):

"TEXT"

Person & email address to contact for further information:

Dave Beckett, Eric Prud'hommeaux <public-rdf-dawg-comments@w3.org>

Intended usage:

COMMON

Restrictions on usage:

None

Author/Change controller:

The SPARQL specification is a work product of the World Wide Web
Consortium's RDF Data Access Working Group. The W3C has change
control over these specifications.

### References

[RFC3023] Murata, M., St. Laurent, S., and D. Kohn, "XML Media Types",
RFC 3023, January 2001.

[RFC3986] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform
Resource Identifier (URI): Generic Syntax", STD 66, RFC
3986, January 2005.

[RFC3987] Duerst, M. and M. Suignard, "Internationalized Resource
Identifiers (IRIs)", RFC 3987, January 2005.

## 6. References

[XML]

[Extensible Markup Language (XML) 1.0, Third Edition](https://www.w3.org/TR/2004/REC-xml-20040204/), T. Bray, J. Paoli, C.M. Sperberg-McQueen, E. Maler, F. Yergeau, Editors, W3C Recommendation, 4 February 2004. This document is http://www.w3.org/TR/2004/REC-xml-20040204 . The [latest version](https://www.w3.org/TR/REC-xml/ "Latest version of XML") is available at http://www.w3.org/TR/REC-xml .

[SPARQL-QUERY]

[SPARQL 1.1 Query Language](https://www.w3.org/TR/2013/REC-sparql11-query-20130321), S. Harris, A. Seaborne, Editors, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-query-20130321. [Latest version](https://www.w3.org/TR/sparql11-query/ "Latest version of SPARQL 1.1 Query Language") available at http://www.w3.org/TR/sparql11-query.

[RELAXNG]

[RELAX NG Specification](http://www.oasis-open.org/committees/relax-ng/spec-20011203.html), James Clark and MURATA Makoto, Editors, OASIS Committee Specification, 3 December 2001. This document is http://www.oasis-open.org/committees/relax-ng/spec-20011203.html . The [latest version](http://www.oasis-open.org/committees/relax-ng/spec.html "Latest version of RELAX NG Specification") is available at http://www.oasis-open.org/committees/relax-ng/spec.html .

[RELAXNG-COMPACT]

[RELAX NG Compact Syntax](http://www.oasis-open.org/committees/relax-ng/compact-20021121.html), James Clark, Editor. OASIS Committee Specification, 21 November 2002. This document is http://www.oasis-open.org/committees/relax-ng/compact-20021121.html .

[XMLSCHEMA-1]

[XML Schema Part 1: Structures Second Edition](https://www.w3.org/TR/2004/REC-xmlschema-1-20041028/), D. Beech, N. Mendelsohn, M. Maloney, H. S. Thompson, Editors, W3C Recommendation, 28 October 2004. This document is http://www.w3.org/TR/2004/REC-xmlschema-1-20041028/ . The [latest version](https://www.w3.org/TR/xmlschema-1/ "Latest version of XML Schema Part 1: Structures Second Edition") is available at http://www.w3.org/TR/xmlschema-1/ .

[SRJ]

[SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/2013/REC-sparql11-results-json-20130321), A. Seaborne, Editor, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-results-json-20130321. [Latest version](https://www.w3.org/TR/sparql11-results-json/ "Latest version of SPARQL 1.1 Query Results JSON Format") available at http://www.w3.org/TR/sparql11-results-json.

[SRC]

[SPARQL 1.1 Query Results CSV and TSV Formats](https://www.w3.org/TR/2013/REC-sparql11-results-csv-tsv-20130321), A. Seaborne, Editor, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-results-csv-tsv-20130321. [Latest version](https://www.w3.org/TR/sparql11-results-csv-tsv/ "Latest version of SPARQL 1.1 Query Results CSV and TSV Formats") available at http://www.w3.org/TR/sparql11-results-csv-tsv.

## Change Log

### Changes since Proposed Edited Recommendation

- Removed statement that IANA had not processed registration

### Changes since 2008 Recommendation

- Mention the JSON and CSV/TSV results formats
- Make in the examples point to maintainable versions
