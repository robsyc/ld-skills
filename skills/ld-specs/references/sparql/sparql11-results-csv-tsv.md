---
title: "SPARQL 1.1 Query Results CSV and TSV Formats"
source: https://www.w3.org/TR/sparql11-results-csv-tsv/
family: sparql
version: "1.1"
status: W3C Recommendation
spec_date: 2013-03-21
fetched: 2026-11-09
---

# SPARQL 1.1 Query Results CSV and TSV Formats

> CSV/TSV results (1.1 Recommendation).

## Contents

- Abstract
- 1 Introduction
  - 1.1 Example
- 2 Transmission issues using CSV and TSV Formats
- 3 CSV - Comma Separated values
  - 3.1 Serializing the Results Table
  - 3.2 Serializing RDF Terms
  - 3.3 Example of CSV-Serialized Results
- 4 TSV - Tab Separated values
  - 4.1 Serializing the Results Table
  - 4.2 Serializing RDF Terms
  - 4.3 Example of TSV-Serialized Results
- A References
  - A.1 Normative References
  - A.2 Non-normative References
- Change Log
  - Changes since Proposed Recommendation
  - Changes since Last Call
- B References
  - B.1 Normative references
  - B.2 Informative references

---

## Abstract

The formats CSV [RFC4180] (comma separated values)
and TSV [IANA-TSV] (tab separated values)
provide simple, easy to process formats for the transmission of tabular data.
They are supported as input datat formats to many tools, particularly spreadsheets.
This document describes their use for expressing SPARQL query results from `SELECT` queries.

## 1. Introduction

This document describes CSV and TSV formats for expressing
the results of a SPARQL `SELECT` query.
They provide lowest common denominator
formats between systems using different
implementation technologies.

Other formats for expression SPARQL results are the
SPARQL XML Results Format [RDF-SPARQL-XMLRES]
and SPARQL JSON Results Format [SPARQL11-JSON-RES].
Each format is useful in different application scenarios.

The SPARQL Results CSV Results Format is a lossy encoding
of a table of results. It does not encode all the details of
each RDF term in the results but instead just gives a string
without indicating the type of the term (IRI, Literal, Literal
with datatype, Literal with language, or blank node). This makes
it simple to consume data, such as text and numbers, in
applications without needing to understand the details
of RDF. In some applications, guesses as to which
elements are hyperlinks are made pragmatically, for example,
guessing that strings starting "http://" are links.

The SPARQL Results TSV Results Format does encode the details
of RDF terms in the results table by using the syntax that SPARQL [SPARQL11-QUERY]
and Turtle [TURTLE] use. An application receiving a TSV-encoded
results set can
split each line into elements of the result row, and extract
all the details it wishes to process of the RDF terms by
simple string processing, without a complete XML or JSON parser
required by the more complex SPARQL result formats.

When this document uses the words *must*, *must not*, *should*, *should
not*, *may* and *recommended*, they must be interpreted as described in
RFC 2119 [RFC2119].

### 1.1 Example

The following artificial example is used to illustrate the
features of serializing results in each format.

| x                  | literal               | *Comment (not part of the table)*                           |
| ------------------ | --------------------- | ----------------------------------------------------------- |
| <http://example/x> | String                | An IRI and a string consisting of characters S-t-r-i-n-g    |
| <http://example/x> | String-with-dquote"   | String with a double quote in it.                           |
| _:b0               | Blank node            | Blank node                                                  |
|                    | Missing 'x'           | No RDF term for the **x** column                            |
|                    |                       | This row has no terms in it.                                |
| <http://example/x> |                       | No term in the **literal** column.                          |
| _:b1               | "String-with-lang"@en | An RDF literal with a language tag                          |
| _:b1               | 123                   | An RDF literal, datatype xsd:integer, and lexical form 123. |

## 2. Transmission issues using CSV and TSV Formats

The SPARQL results formats described here
confirm to the formal specifications of the
relevant formats, Comma Separated values (CSV) [RFC4180] and
Tab Separated Value (TSV) [IANA-TSV].

Systems providing these formats should note that the content types for CSV is `text/csv` and for TSV `text/tab-separated-values`.
Being `text/*`, the default character set is US-ASCII.
The `charset` parameter *should* be used in conjunction
with SPARQL Results; UTF-8 is recommended: `text/csv; charset=utf-8` and `text/tab-separated-values; charset=utf-8`.

The end-of-line in CSV is `CRLF` i.e.
Unicode codepoints 13 (0x0D) and 10 (0x0A).

The end-of-line in TSV is `EOL` i.e.
Unicode codepoint 10 (0x0A).

Applications reading these formats are advised to cope with
both CRLF and LF as end of line markers
and not rely on conformance to the formal specifications.

## 3. CSV - Comma Separated values

In the SPARQL Results CSV Format,
the results table is serialized as one line listing the variables
in the results, using the CSV header line,
followed by one line for each query solution
(a line may end up split by newlines in the data).
Values in the results are strings, for URIs, literals and blank nodes,
together with numbers when the literals are of numeric XSD
datatype.

### 3.1 Serializing the Results Table

The first line of a SPARQL CSV Results Format response
is the header line giving the names of the variables
used in the result set. The header line consists of the
variable names, without leading `?`, separated by commas.

While the `text/csv` format does not require a header row,
the SPARQL CSV Results Format *must* use a header row.
If the content type parameter `header` is used,
it *must* be `header=present`.

The remaining rows are the values of the results,
with each binding determined by the position in the row,
corresponding to the entry in the header line.

If a variable is not bound, an empty field is used (e.g. `,,`).
Each row *must* have the same number of fields,
with each field corresponding to a binding to the variable
in the header line in the same field position.

### 3.2 Serializing RDF Terms

The entry in each field is the string corresponding to the RDF term value.
(c.f. SPARQL STR()) without syntax to denote what kind of
term it is. The encoding quoting rules of CSV format must be
used.

Blank nodes use the `_:label` form from Turtle and SPARQL.
Use of the same label indicates the same blank node within the
results but has no significance outside
the results.

Fields containing any of `"` (QUOTATION MARK, code point 34, 0x22 in Unicode[UNICODE]), `,` (COMMA, code point 44, 0x2C), `LF` (code point 10, 0x0A) or `CR` (code point 13, 0x0D)
must be quoted using the quoting mechanism
of RFC4180 [RFC4180]. Fields are limited by a pair of
quotation marks `"` (code point 0x22).
Within quote strings,
all characters except `"`,
including new line characters have their exact meaning -
newlines do not end a CSV record. `"` is written using a pair of quotation marks `""`.

The standard CSV format does not distinguish between missing
values and empty strings.
The SPARQL 1.1 CSV Results Format uses the same representation
for unbound variables as for variables bound to an empty string
literal. The other SPARQL Result formats (based on JSON, TSV or XML)
can be used if this distinction is required.

### 3.3 Example of CSV-Serialized Results

```
x,literal
http://example/x,String
http://example/x,"String-with-dquote"""
_:b0,Blank node
,Missing 'x'
,
http://example/x,
_:b1,String-with-lang
_:b1,123
```

## 4. TSV - Tab Separated values

In the SPARQL Results TSV Format,
the results table is serialized as one line listing the variables
in the results, followed by one line for each query solution.
All RDF terms used in the format are encoded in the format
specified by Turtle [TURTLE] except that the
triple quoted forms for the lexical part of literals *must not* be used. These forms would allow raw newlines and
tabs that form part of the TSV format. A TSV format SPARQL result
set must use the single quoted literal forms, together with
any necessary escapes such as `\t`, `\n` and `\r`.

### 4.1 Serializing the Results Table

The results table is serialized as one line listing the variables
in the results, followed by one line for each query solution.
This first line is required by the TSV format [IANA-TSV],
unlike CSV, where it is optional.

Variables are serialized in SPARQL syntax, using question mark `?` character followed by the variable name.

Each row of the result set is serialized by sequence of
RDF terms in SPARQL syntax, separated by a tab
(Horizontal Tab, Unicode codepoint 9) character.

If a variable is not bound in a row, an empty field is used.
Each row *must* have the same number of fields, corresponding to the variables
listed in the first row.

### 4.2 Serializing RDF Terms

The SPARQL Results TSV Results Format serializes
RDF terms in the results table by using the syntax that SPARQL [SPARQL11-QUERY]
and Turtle [TURTLE] use.

IRIs enclosed in `<...>`,
literals are enclosed with double quotes `"`...`"` or single quotes `'` ...`'` with optional `@lang` or `^^` for datatype.
The quotes around the lexical
form is required.
Tab, newline and carriage return characters (Unicode codepoints
0x09, 0x0A (line feed) and 0x0D (Carriage Return))
are encoded in strings as `\t`, `\n` and `\r` respectively.
The long string forms using triple quotes `"""` and `'''` *must not* be used.

The abbreviated forms for numbers (XSD integers, decimals and doubles) *should* be used.

Blank nodes use the `_:label` form from Turtle and SPARQL.
Use of the same label indicates the same blank node within the
results but has no significance outside
the results.

### 4.3 Example of TSV-Serialized Results

Writing `<TAB>` for a raw tab character (Unicode
code point 9):

```
?x<TAB>?literal
<http://example/x><TAB>"String"
<http://example/x><TAB>"String-with-dquote\""

_:blank0<TAB>"Blank node"
<TAB>"Missing 'x'"
<TAB>
<http://example/x><TAB>
_:blank1<TAB>"String-with-lang"@en
_:blank1<TAB>123
```

## A. References

This section includes references not yet included in the standard biblio DB

### A.1 Normative References

SPARQL11-JSON-RES

[SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/2013/REC-sparql11-results-json-20130321), A. Seaborne, Editor, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-results-json-20130321. [Latest version](https://www.w3.org/TR/sparql11-results-json/ "Latest version of SPARQL 1.1 Query Results JSON Format") available at http://www.w3.org/TR/sparql11-results-json.

SPARQL11-QUERY

[SPARQL 1.1 Query Language](https://www.w3.org/TR/2013/REC-sparql11-query-20130321), S. Harris, A. Seaborne, Editors, W3C Recommendation, 21 March 2013, http://www.w3.org/TR/2013/REC-sparql11-query-20130321. [Latest version](https://www.w3.org/TR/sparql11-query/ "Latest version of SPARQL 1.1 Query Language") available at http://www.w3.org/TR/sparql11-query.

### A.2 Non-normative References

## Change Log

### Changes since Proposed Recommendation

- None

### Changes since Last Call

- None.

## B. References

### B.1 Normative references

[IANA-TSV]

Paul Lindner. [Definition of tab-separated-values (tsv)](http://www.iana.org/assignments/media-types/text/tab-separated-values) June 1993. IANA Media Type Registration. URL: <http://www.iana.org/assignments/media-types/text/tab-separated-values>

[RFC2119]

S. Bradner. [Key words for use in RFCs to Indicate Requirement Levels.](http://www.ietf.org/rfc/rfc2119.txt) March 1997. Internet RFC 2119. URL: <http://www.ietf.org/rfc/rfc2119.txt>

[RFC4180]

Y. Shafranovich. [Common Format and MIME Type for Comma-Separated Values (CSV) Files](http://www.ietf.org/rfc/rfc4180.txt) October 2005. Internet RFC 3987. URL: <http://www.ietf.org/rfc/rfc4180.txt>

[TURTLE]

David Beckett, Tim Berners-Lee. [Turtle: Terse RDF Triple Language.](https://www.w3.org/TeamSubmission/turtle/) January 2008. W3C Team Submission. URL: [http://www.w3.org/TeamSubmission/turtle/](https://www.w3.org/TeamSubmission/turtle/)

### B.2 Informative references

[RDF-SPARQL-XMLRES]

Jeen Broekstra; Dave Beckett. [SPARQL Query Results XML Format.](https://www.w3.org/TR/2008/REC-rdf-sparql-XMLres-20080115) 15 January 2008. W3C Recommendation. URL: [http://www.w3.org/TR/2008/REC-rdf-sparql-XMLres-20080115](https://www.w3.org/TR/2008/REC-rdf-sparql-XMLres-20080115)

[UNICODE]

The Unicode Consortium. [The Unicode Standard.](http://www.unicode.org/unicode/standard/versions/enumeratedversions.html) 2003. Defined by: The Unicode Standard, Version 4.0 (Boston, MA, Addison-Wesley, ISBN 0-321-18578-1), as updated from time to time by the publication of new versions URL: <http://www.unicode.org/unicode/standard/versions/enumeratedversions.html>
