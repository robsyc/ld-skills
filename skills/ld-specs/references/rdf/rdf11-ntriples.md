---
title: "RDF 1.1 N-Triples"
source: https://www.w3.org/TR/n-triples/
family: rdf
version: "1.1"
status: W3C Recommendation
spec_date: 2014-02-25
fetched: 2026-10-21
---

# RDF 1.1 N-Triples

> Line-based syntax for graphs (1.1 Recommendation).

## Contents

- Abstract
- 1 Introduction
- 2 N-Triples Language
  - 2.1 Simple Triples
  - 2.2 IRIs
  - 2.3 RDF Literals
  - 2.4 RDF Blank Nodes
- 3 Changes from RDF Test Cases format
- 4 A Canonical form of N-Triples
- 5 Conformance
- 6 Media Type and Content Encoding
  - 6.1 Other Media Types
- 7 Grammar
- 8 Parsing
  - 8.1 RDF Term Constructors
  - 8.2 RDF Triple Construction
- A Change log
  - A.1 Changes between Proposed Recommendation and Recommendation
  - A.2 Changes between Candidate Recommendation and Proposed Recommendation
  - A.3 Changes between Last Call Working Draft and Candidate recommendation
  - A.4 Changes between Last Call Working Draft and publication as Note
- B N-Triples Internet Media Type, File Extension and Macintosh File Type
- C References
  - C.1 Normative references
  - C.2 Informative references

---

## Abstract

N-Triples is a line-based, plain text format for encoding an RDF graph.

## 1. Introduction

This document defines N-Triples, a concrete syntax for
RDF [RDF11-CONCEPTS].
N-Triples is an easy to parse line-based subset of
Turtle [TURTLE].

The syntax is a revised version of N-Triples as originally defined in the RDF Test Cases [RDF-TESTCASES] document. Its original intent was for writing test cases, but it has proven to be popular as an exchange format for RDF data.

An N-Triples document contains no parsing directives.

N-Triples triples are a sequence of RDF terms representing the subject, predicate and object of an RDF Triple. These may be separated by white space (spaces `U+0020` or tabs `U+0009`). This sequence is terminated by a '`.`' and a new line (optional at the end of a document).
> **Example:**
>
> > **Example:**
> >
> > Example 1

N-Triples triples are also Turtle §2.1 Simple Triples, but Turtle includes other representations of RDF terms and [abbreviations of RDF Triples](https://www.w3.org/TR/turtle/#predicate-lists). When parsed by a Turtle parser, data in the N-Triples format will produce exactly the same triples as a parser for the N-triples language.

The RDF graph represented by an N-Triples document contains
exactly each triple matching the N-Triples `triple` production.

## 2. N-Triples Language

### 2.1 Simple Triples

The simplest triple statement is a sequence of (subject, predicate, object) terms, separated by whitespace and terminated by '`.`' after each triple.
> **Example:**
>
> > **Example:**
> >
> > Example 2

### 2.2 IRIs

[IRIs](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) may be written only as absolute IRIs.
IRIs are enclosed in '`<`' and '`>`' and may contain numeric escape sequences (described below). For example `<http://example.org/#green-goblin>`.

### 2.3 RDF Literals

[Literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) are used to identify values such as strings, numbers,
dates.

Literals (Grammar production Literal) have a lexical form followed by a language tag, a datatype IRI, or neither.
The representation of the lexical form consists of an
initial delimiter `"` (U+0022), a sequence of permitted
characters or numeric escape sequence or string escape sequence, and a final delimiter. Literals may not contain the characters `"`, `LF`, `CR` except in their escaped forms. In addition '`\`' (U+005C) may not appear in any quoted literal except as part of an escape sequence.
The corresponding [RDF lexical form](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-form) is the characters between the delimiters, after processing any escape sequences.
If present, the [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string) is preceded by a '`@`' (U+0040).
If there is no language tag, there may be a [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri), preceded by '`^^`' (U+005E U+005E). If there is no datatype IRI and no language tag it is a [simple literal](https://www.w3.org/TR/rdf11-concepts/#dfn-simple-literal) and the datatype is `http://www.w3.org/2001/XMLSchema#string`.
> **Example:**
>
> > **Example:**
> >
> > Example 3

### 2.4 RDF Blank Nodes

[RDF blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) in N-Triples are expressed as `_:` followed by a blank node label which is a series of name characters.
The characters in the label are built upon PN_CHARS_BASE, liberalized as follows:

- The characters `_` and `[0-9]` may appear anywhere in a blank node label.
- The character `.` may appear anywhere except the first or last character.
- The characters `-`, `U+00B7`, `U+0300` to `U+036F` and `U+203F` to `U+2040` are permitted anywhere except the first character.

A fresh RDF blank node is allocated for each unique blank node label in a document.
Repeated use of the same blank node label identifies the same RDF blank node.
> **Example:**
>
> > **Example:**
> >
> > Example 4

## 3. Changes from RDF Test Cases format

*This section is non-normative.*

- Encoding is UTF-8 rather than US-ASCII
- Uses IRIs rather than RDF URI References
- Defines a unique media type `application/n-triples`
- Subset of Turtle rather than Notation 3
- Comments may occur after a triple production
- Allows `\b` and `\f` for backspace and form feed
- More than one way to represent a single character
- Blank node labels may start with a digit

## 4. A Canonical form of N-Triples

This section defined a canonical form of N-Triples which has
less variability in layout. The grammar for the language is the
same. Implementers are encouraged to produce this form.

Canonical N-Triples has the following additional constraints on layout:

- The whitespace following `subject`, `predicate`,
  and `object` *MUST* be a single space,
  (`U+0020`). All other locations that allow
  whitespace *MUST* be empty.
- There *MUST* be no comments.
- `HEX` *MUST* use only uppercase letters (`[A-F]`).
- Characters *MUST NOT* be represented by `UCHAR`.
- Within STRING_LITERAL_QUOTE,
  only the characters `U+0022`, `U+005C`, `U+000A`, `U+000D` are encoded using `ECHAR`. `ECHAR` *MUST NOT* be used for characters that are
  allowed directly in STRING_LITERAL_QUOTE.

## 5. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples,
and notes in this specification are non-normative. Everything else in this specification is
normative.

The key words *MUST*, *MUST NOT*, *REQUIRED*, *SHOULD*, *SHOULD NOT*, *RECOMMENDED*, *MAY*,
and *OPTIONAL* in this specification are to be interpreted as described in [RFC2119].

This specification defines conformance criteria for:

- N-Triples documents
- Canonical N-Triples documents
- N-Triples parsers

A conforming *N-Triples document* is a Unicode string that conforms to the grammar and additional constraints defined in section 7. Grammar (§7), starting with the `ntriplesDoc` production. An N-Triples document serializes an RDF graph.

A conforming *Canonical N-Triples document* is an **N-Triples document** that follows the additional constraints (§4) of Canonical N-Triples.

A conforming *N-Triples parser* is a system capable of reading N-Triples documents on behalf of an application. It makes the serialized RDF graph, as defined in section 8. Parsing (§8), available to the application, usually through some form of API.

The IRI that identifies the N-Triples language is: `http://www.w3.org/ns/formats/N-Triples`

## 6. Media Type and Content Encoding

The media type of N-Triples is `application/n-triples`.
The content encoding of N-Triples is always UTF-8.
See N-Triples Media Type (§B) for the media type
registration form.

### 6.1 Other Media Types

N-Triples has been historically provided with other media types. N-Triples may also be provided as `text/plain`. When used in this way N-Triples *MUST* use the escaped form of any character outside US-ASCII. As N-Triples is a subset of Turtle an N-Triples document *MAY* also be provided as `text/turtle`. In both of these cases the document is not an N-Triples document as an N-Triples document is only provided as `application/n-triples`.

## 7. Grammar

An N-Triples document is a Unicode [UNICODE] character string encoded in UTF-8.
Unicode code points only in the range U+0 to U+10FFFF inclusive are allowed.

White space (tab `U+0009` or space `U+0020`) is used to separate two terminals which would otherwise be (mis-)recognized as one terminal. White space is significant in the production STRING_LITERAL_QUOTE.

Comments in N-Triples take the form of '`#`',
outside an `IRIREF` or `STRING_LITERAL_QUOTE`, and continue
up-to, and excluding, the end of line (`EOL`),
or end of file if there is no end of line after the comment
marker. Comments are treated as white space.

The EBNF used
here is defined in XML 1.0
[EBNF-NOTATION].

Escape sequence rules are the same as Turtle
[TURTLE]. However, as only the `STRING_LITERAL_QUOTE` production is allowed new lines in literals *MUST* be escaped.

| [1]                       | `ntriplesDoc`          | ::= | triple? (EOL triple)`*` EOL? |
| ------------------------- | ---------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [2]                       | `triple`               | ::= | subject predicate object '`.`' |
| [3]                       | `subject`              | ::= | IRIREF `\| ` BLANK_NODE_LABEL                                      |
| [4]                       | `predicate`            | ::= | IRIREF                                                                                                                                     |
| [5]                       | `object`               | ::= | IRIREF `\|  \| ` BLANK_NODE_LABEL literal |
| [6]                       | `literal`              | ::= | STRING_LITERAL_QUOTE ('`^^ \| `' IRIREF LANGTAG)? |
| Productions for terminals | | | |
| [144s]                    | `LANGTAG`              | ::= | '`@`' [`a-zA-Z`]`+` ('`-`' [`a-zA-Z0-9`]`+`)`*`                                                                                                                                                          |
| [7]                       | `EOL`                  | ::= | [`#xD#xA`]`+`                                                                                                                                                                                            |
| [8]                       | `IRIREF`               | ::= | '`<`' ([``^#x00-#x20<>"{}\|^`\``] `\| ` UCHAR)`*` '`>`'                                                                                     |
| [9]                       | `STRING_LITERAL_QUOTE` | ::= | '`"`' ([`^#x22#x5C#xA#xD`] `\|  \| ` ECHAR UCHAR)`*` '`"`'                     |
| [141s]                    | `BLANK_NODE_LABEL`     | ::= | '`_: \| `' (PN_CHARS_U [`0-9 \| `]) ((PN_CHARS '`.`')`*` PN_CHARS)? |
| [10]                      | `UCHAR`                | ::= | '`\u \| `' HEX HEX HEX HEX '`\U`' HEX HEX HEX HEX HEX HEX HEX HEX |
| [153s]                    | `ECHAR`                | ::= | '`\`' [`tbnrf"'\`]                                                                                                                                                                                       |
| [157s]                    | `PN_CHARS_BASE`        | ::= | [`A-Z`] `\| ` [`a-z`] `\| ` [`#x00C0-#x00D6`] `\| ` [`#x00D8-#x00F6`] `\| ` [`#x00F8-#x02FF`] `\| ` [`#x0370-#x037D`] `\| ` [`#x037F-#x1FFF`] `\| ` [`#x200C-#x200D`] `\| ` [`#x2070-#x218F`] `\| ` [`#x2C00-#x2FEF`] `\| ` [`#x3001-#xD7FF`] `\| ` [`#xF900-#xFDCF`] `\| ` [`#xFDF0-#xFFFD`] `\| ` [`#x10000-#xEFFFF`] |
| [158s]                    | `PN_CHARS_U`           | ::= | PN_CHARS_BASE `\| ` '`_`' `\| ` '`:`'                                                                                               |
| [160s]                    | `PN_CHARS`             | ::= | PN_CHARS_U `\| ` '`-`' `\| ` [`0-9`] `\|  #x00B7` [`#x0300-#x036F`] `\| ` [`#x203F-#x2040`]                                            |
| [162s]                    | `HEX`                  | ::= | [`0-9`] `\| ` [`A-F`] `\| ` [`a-f`]                                                                                                                                                                      |

## 8. Parsing

Parsing N-Triples requires a state of one item:

- Map[string -> [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)] `bnodeLabels` — A mapping from string to blank node.

### 8.1 RDF Term Constructors

This table maps productions and lexical tokens to `RDF terms` or components of `RDF terms` listed in section 8. Parsing (§8):

| production                                                                                       | type                                                                   | procedure                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IRIREF                             | [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri)                   | The characters between "<" and ">" are taken, with escape sequences unescaped, to form the unicode string of the IRI.                                                                                    |
| STRING_LITERAL_QUOTE | [lexical form](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-form) | The characters between the outermost '"'s are taken, with escape sequences unescaped, to form the unicode string of a lexical form.                                                                      |
| LANGTAG                           | [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) | The characters following the `@` form the unicode string of the language tag.                                                                                                                            |
| literal                           | [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal)           | The literal has a lexical form of the first rule argument, `   STRING_LITERAL_QUOTE`, and either a language tag of `LANGTAG` or a datatype IRI of `iri`, depending on which rule matched the input. If the `LANGTAG` rule matched, the datatype is `rdf:langString` and the language tag is `LANGTAG`. If neither a language tag nor a datatype IRI is provided, the literal has a datatype of `xsd:string`. |
| BLANK_NODE_LABEL         | [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)     | The string after '`_:`', is a key in bnodeLabels. If there is no corresponding blank node in the map, one is allocated.                                  |

### 8.2 RDF Triple Construction

An N-Triples document defines an RDF graphs composed of a set of RDF triples. The `triple` production produces a triple defined by the terms constructed for `subject`, `predicate` and `object`.

## A. Change log

### A.1 Changes between Proposed Recommendation and Recommendation

- [Bug in grammar rule [6]](http://lists.w3.org/Archives/Public/public-rdf-comments/2014Feb/0009.html) concerning language-typed literals fixed.

### A.2 Changes between Candidate Recommendation and Proposed Recommendation

- A normative reference to RDF Concepts was added.
- The text for "Canonical N-Triples" has been made into a separate section.

### A.3 Changes between Last Call Working Draft and Candidate recommendation

No substantive changes.

### A.4 Changes between Last Call Working Draft and publication as Note

- Section defines canonical N-Triples document.
- White space rules defined outside of grammar, as in Turtle.
- Comment processing defined.
- Parsing is defined.
- Removed "Summary of differences in N-Triples and Turtle".
- Recommendation track, not a working group Note.

## B. N-Triples Internet Media Type, File Extension and Macintosh File Type

Contact:

Eric Prud'hommeaux

See also:

[How to Register a Media Type for a W3C Specification](https://www.w3.org/2002/06/registering-mediatype)

[Internet Media Type registration, consistency of use](https://www.w3.org/2001/tag/2002/0129-mime)
TAG Finding 3 June 2002 (Revised 4 September 2002)

The Internet Media Type / MIME Type for N-Triples is "application/n-triples".

It is recommended that N-Triples files have the extension ".nt" (all lowercase) on all platforms.

It is recommended that N-Triples files stored on Macintosh HFS file systems be given a file type of "TEXT".

This information that follows will be submitted to the IESG for review, approval, and registration with IANA.

Type name:

application

Subtype name:

n-triples

Required parameters:

None

Optional parameters:

None

Encoding considerations:

The syntax of N-Triples is expressed over code points in Unicode [UNICODE]. The encoding is always UTF-8 [UTF-8].

Unicode code points may also be expressed using an \uXXXX (U+0 to U+FFFF) or \UXXXXXXXX syntax (for U+10000 onwards) where X is a hexadecimal digit [0-9A-F]

Security considerations:

N-Triples is a general-purpose assertion language; applications may evaluate given data to infer more assertions or to dereference IRIs, invoking the security considerations of the scheme for that IRI. Note in particular, the privacy issues in [RFC3023] section 10 for HTTP IRIs. Data obtained from an inaccurate or malicious data source may lead to inaccurate or misleading conclusions, as well as the dereferencing of unintended IRIs. Care must be taken to align the trust in consulted resources with the sensitivity of the intended use of the data; inferences of potential medical treatments would likely require different trust than inferences for trip planning.

N-Triples is used to express arbitrary application data; security considerations will vary by domain of use. Security tools and protocols applicable to text (e.g. PGP encryption, MD5 sum validation, password-protected compression) may also be used on N-Triples documents. Security/privacy protocols must be imposed which reflect the sensitivity of the embedded information.

N-Triples can express data which is presented to the user, for example, RDF Schema labels. Application rendering strings retrieved from untrusted N-Triples documents must ensure that malignant strings may not be used to mislead the reader. The security considerations in the media type registration for XML ([RFC3023] section 10) provide additional guidance around the expression of arbitrary data and markup.

N-Triples uses IRIs as term identifiers. Applications interpreting data expressed in N-Triples should address the security issues of *Internationalized Resource Identifiers (IRIs)* [RFC3987] Section 8, as well as *Uniform Resource Identifier (URI): Generic Syntax* [RFC3986] Section 7.

Multiple IRIs may have the same appearance. Characters in different scripts may
look similar (a Cyrillic "о" may appear similar to a Latin "o"). A character followed
by combining characters may have the same visual representation as another character
(LATIN SMALL LETTER E followed by COMBINING ACUTE ACCENT has the same visual representation
as LATIN SMALL LETTER E WITH ACUTE).
Any person or application that is writing or interpreting data in Turtle must take care to use the IRI that matches the intended semantics, and avoid IRIs that make look similar.
Further information about matching of similar characters can be found
in *Unicode Security Considerations* [UNICODE-SECURITY] and *Internationalized Resource Identifiers (IRIs)* [RFC3987] Section 8.

Interoperability considerations:

There are no known interoperability issues.

Published specification:

This specification.

Applications which use this media type:

No widely deployed applications are known to use this media type. It may be used by some web services and clients consuming their data.

Additional information:

Magic number(s):

None.

File extension(s):

".nt"

Macintosh file type code(s):

"TEXT"

Person & email address to contact for further information:

Eric Prud'hommeaux <eric@w3.org>

Intended usage:

COMMON

Restrictions on usage:

None

Author/Change controller:

The N-Triples specification is the product of the RDF WG. The W3C reserves change control over this specifications.

## C. References

### C.1 Normative references

[EBNF-NOTATION]

Tim Bray; Jean Paoli; C. M. Sperberg-McQueen; Eve Maler; François Yergeau. [EBNF Notation](https://www.w3.org/TR/REC-xml/#sec-notation) 26 November 2008. W3C Recommendation. URL: [http://www.w3.org/TR/REC-xml/#sec-notation](https://www.w3.org/TR/REC-xml/#sec-notation)

[RDF-TESTCASES]

jan grant; Dave Beckett. [RDF Test Cases](https://www.w3.org/TR/rdf-testcases). 10 February 2004. W3C Recommendation. URL: [http://www.w3.org/TR/rdf-testcases](https://www.w3.org/TR/rdf-testcases)

[RDF11-CONCEPTS]

Richard Cyganiak, David Wood, Markus Lanthaler. [RDF 1.1 Concepts and Abstract Syntax.](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) W3C Recommendation, 25 February 2014. URL: [http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/). The latest edition is available at [http://www.w3.org/TR/rdf11-concepts/](https://www.w3.org/TR/rdf11-concepts/)

[RFC2119]

S. Bradner. [Key words for use in RFCs to Indicate Requirement Levels.](http://www.ietf.org/rfc/rfc2119.txt) March 1997. Internet RFC 2119. URL: <http://www.ietf.org/rfc/rfc2119.txt>

[RFC3023]

M. Murata; S. St.Laurent; D. Kohn. [XML Media Types (RFC 3023)](http://www.ietf.org/rfc/rfc3023.txt). January 2001. RFC. URL: <http://www.ietf.org/rfc/rfc3023.txt>

[RFC3986]

T. Berners-Lee; R. Fielding; L. Masinter. [Uniform Resource Identifier (URI): Generic Syntax (RFC 3986)](http://www.ietf.org/rfc/rfc3986.txt). January 2005. RFC. URL: <http://www.ietf.org/rfc/rfc3986.txt>

[RFC3987]

M. Dürst; M. Suignard. [Internationalized Resource Identifiers (IRIs)](http://www.ietf.org/rfc/rfc3987.txt). January 2005. RFC. URL: <http://www.ietf.org/rfc/rfc3987.txt>

[TURTLE]

Eric Prud'hommeaux, Gavin Carothers. [RDF 1.1 Turtle: Terse RDF Triple Language.](https://www.w3.org/TR/2014/REC-turtle-20140225/) W3C Recommendation, 25 February 2014. URL: [http://www.w3.org/TR/2014/REC-turtle-20140225/](https://www.w3.org/TR/2014/REC-turtle-20140225/). The latest edition is available at [http://www.w3.org/TR/turtle/](https://www.w3.org/TR/turtle/)

[UNICODE]

[The Unicode Standard](http://www.unicode.org/versions/latest/). URL: <http://www.unicode.org/versions/latest/>

[UTF-8]

F. Yergeau. [UTF-8, a transformation format of ISO 10646](http://www.ietf.org/rfc/rfc3629.txt). IETF RFC 3629. November 2003. URL: <http://www.ietf.org/rfc/rfc3629.txt>

### C.2 Informative references

[UNICODE-SECURITY]

Mark Davis; Michel Suignard. [Unicode Security Considerations](http://www.unicode.org/reports/tr36/). URL: <http://www.unicode.org/reports/tr36/>
