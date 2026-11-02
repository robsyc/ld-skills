---
title: "RDFa Core 1.1 - Third Edition"
source: https://www.w3.org/TR/rdfa-core/
family: web
status: W3C Recommendation
spec_date: 2015-03-17
fetched: 2026-11-02
---

# RDFa Core 1.1 - Third Edition

> Embedding RDF in XML/HTML attributes.

## Contents

- Abstract
  - 1 How to Read this Document
- 1 Motivation
- 2 Syntax Overview
  - 2.1 The RDFa Attributes
  - 2.2 Examples
- 3 RDF Terminology
  - 3.1 Statements
  - 3.2 Triples
  - 3.3 IRI References
  - 3.4 Plain Literals
  - 3.5 Typed Literals
  - 3.6 Turtle
  - 3.7 Graphs
  - 3.8 Compact URI Expressions
  - 3.9 Markup Fragments and RDFa
  - 3.10 A Description of RDFa in RDF Terms
- 4 Conformance
  - 4.1 RDFa Processor Conformance
  - 4.2 RDFa Host Language Conformance
  - 4.3 XML+RDFa Document Conformance
- 5 Attributes and Syntax
  - 5.1 Roles of attributes
  - 5.2 White space within attribute values
- 6 CURIE Syntax Definition
  - 6.1 Why CURIEs and not QNames?
- 7 Processing Model
  - 7.1 Overview
  - 7.2 Evaluation Context
  - 7.3 Chaining
  - 7.4 CURIE and IRI Processing
    - 7.4.1 Scoping of Prefix Mappings
    - 7.4.2 General Use of CURIEs in Attributes
    - 7.4.3 General Use of Terms in Attributes
    - 7.4.4 Use of CURIEs in Specific Attributes
    - 7.4.5 Referencing Blank Nodes
  - 7.5 Sequence
  - 7.6 Processor Status
    - 7.6.1 Accessing the Processor Graph
    - 7.6.2 Processor Graph Terms
  - 7.7 Vocabulary Expansion
- 8 RDFa Processing in detail
  - 8.1 Changing the Evaluation Context
    - 8.1.1 Setting the current subject
  - 8.2 Completing incomplete triples
  - 8.3 Object resolution
    - 8.3.1 Object resolution for the @property attribute
    - 8.3.2 IRI object resolution
  - 8.4 List Generation
- 9 RDFa Initial Contexts
- 10 RDFa Vocabulary Expansion
  - 10.1 Details of the RDFa Vocabulary Expansion
    - 10.1.1 RDFa Vocabulary Entailment
  - 10.2 Vocabulary Expansion Control of RDFa Processors
    - 10.2.1 Notes to RDFa Vocabulary Implementations and Publishing
- A CURIE Datatypes
  - A.1 XML Schema Definition
  - A.2 XML DTD Definition
- B The RDFa Vocabulary
  - B.1 Term and Prefix Assignments
  - B.2 Processor Graph Reporting
  - B.3 Term for vocabulary expansion
- C Changes
  - C.1 Major differences since the Last Published Recommentation
  - C.2 Major differences with RDFa Syntax 1.0
- E References
  - E.1 Normative references
  - E.2 Informative references

---

## Abstract

The current Web is primarily made up of an enormous number of documents
that have been created using HTML. These documents contain significant
amounts of structured data, which is largely unavailable to tools and
applications. When publishers can express this data more completely, and
when tools can read it, a new world of user functionality becomes
available, letting users transfer structured data between applications
and web sites, and allowing browsing applications to improve the user
experience: an event on a web page can be directly imported into a
user's desktop calendar; a license on a document can be detected so that
users can be informed of their rights automatically; a photo's creator,
camera setting information, resolution, location and topic can be
published as easily as the original photo itself, enabling structured
search and sharing.

RDFa Core is a specification for attributes to express structured data
in any markup language. The embedded data already available in the
markup language (e.g., HTML) can often be reused by the RDFa markup, so
that publishers don't need to repeat significant data in the document
content. The underlying abstract representation is RDF [RDF11-PRIMER],
which lets publishers build their own vocabulary, extend others, and
evolve their vocabulary with maximal interoperability over time. The
expressed structure is closely tied to the data, so that rendered data
can be copied and pasted along with its relevant structure.

The rules for interpreting the data are generic, so that there is no
need for different rules for different formats; this allows authors and
publishers of data to define their own formats without having to update
software, register formats via a central authority, or worry that two
formats may interfere with each other.

RDFa shares some of the same goals with microformats [MICROFORMATS].
Whereas microformats specify both a syntax for embedding structured data
into HTML documents and a vocabulary of specific terms for each
microformat, RDFa specifies only a syntax and relies on independent
specification of terms (often called vocabularies or taxonomies) by
others. RDFa allows terms from multiple independently-developed
vocabularies to be freely intermixed and is designed such that the
language can be parsed without knowledge of the specific vocabulary
being used.

This document is a detailed syntax specification for RDFa, aimed at:

- those looking to create an RDFa Processor, and who therefore need a
  detailed description of the parsing rules;
- those looking to integrate RDFa into a new markup language;
- those looking to recommend the use of RDFa within their
  organization, and who would like to create some guidelines for their
  users;
- anyone familiar with RDF, and who wants to understand more about
  what is happening 'under the hood', when an RDFa Processor runs.

For those looking for an introduction to the use of RDFa and some
real-world examples, please consult the [RDFA-PRIMER].

### How to Read this Document

First, if you are not familiar with either RDFa *or* RDF, and
simply want to add RDFa to your documents, then you may find the RDFa
Primer [RDFA-PRIMER] to be a better introduction.

If you are already familiar with RDFa, and you want to examine the
processing rules — perhaps to create an RDFa Processor — then you'll
find the §7 Processing Model section of most
interest. It contains an overview of each of the processing steps,
followed by more detailed sections, one for each rule.

If you are not familiar with RDFa, but you *are* familiar
with RDF, then you might find reading the §2 Syntax Overview useful, before looking at the §7 Processing Model since it gives a range of examples of markup that use
RDFa. Seeing some examples first should make reading the processing
rules easier.

If you are not familiar with RDF, then you might want to take a look
at the section on §3 RDF Terminology before trying to do too much with RDFa. Although RDFa is designed to
be easy to author — and authors don't need to understand RDF to use it
— anyone writing applications that *consume* RDFa will need to
understand RDF. There is a lot of material about RDF on the web, and a
growing range of tools that support RDFa. This document only contains
enough background on RDF to make the goals of RDFa more clear.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> RDFa is a way of expressing *RDF*-style
> relationships using simple attributes in existing markup languages
> such as HTML. RDF is fully internationalized, and permits the use of
> Internationalized Resource Identifiers, or IRIs. You will see the term
> 'IRI' used throughout this specification. Even if you are not familiar
> with the term IRI, you probably have seen the term 'URI' or 'URL'.
> IRIs are an extension of URIs that permits the use of characters
> outside those of plain ASCII. RDF allows the use of these characters,
> and so does RDFa. This specification has been careful to use the
> correct term, IRI, to make it clear that this is the case.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Even though this specification exclusively
> references IRIs, it is possible that a Host Language will
> restrict the syntax for its attributes to a subset of IRIs
> (e.g., @href in HTML5). Regardless of
> validation constraints in Host Languages, an RDFa Processor
> is capable of processing IRIs.

## 1. Motivation

*This section is non-normative.*

RDF/XML [RDF-SYNTAX-GRAMMAR] provides sufficient flexibility to represent all
of the abstract concepts in RDF. However, it presents a
number of challenges; first it is difficult or impossible to validate
documents that contain RDF/XML using XML Schemas or DTDs, which
therefore makes it difficult to import RDF/XML into other markup
languages. Whilst newer schema languages such as RELAX NG
[RELAXNG-SCHEMA] do provide a way to validate documents that contain
arbitrary RDF/XML, it will be a while before they gain wide support.

Second, even if one could add RDF/XML directly into an XML dialect like
XHTML, there would be significant data duplication between the rendered
data and the RDF/XML structured data. It would be far better to add RDF
to a document without repeating the document's existing data. For
example, an XHTML document that explicitly renders its author's name in
the text — perhaps as a byline on a news site — should not need to repeat
this name for the RDF expression of the same concept: it should be
possible to supplement the existing markup in such a way that it can
also be interpreted as RDF.

Another reason for aligning the rendered data with the structured data
is that it is highly beneficial to express the web data's structure 'in
context'; as users often want to transfer structured data from one
application to another, sometimes to or from a non-web-based
application, the user experience can be enhanced. For example,
information about specific rendered data could be presented to the user
via 'right-clicks' on an item of interest. Moreover, organizations that generate
a lot of content (e.g., news outlets) find it easier to embed the
semantic data inline than to maintain it separately.

In the past, many attributes were 'hard-wired' directly into the markup
language to represent specific concepts. For example, in XHTML 1.1
[XHTML11] and HTML [HTML401] there is @cite;
the attribute allows an author to add information to a document which is
used to indicate the origin of a quote.

However, these 'hard-wired' attributes make it difficult to define a
generic process for extracting metadata from any document since an RDFa
Processor would need to know about each of the special attributes. One
motivation for RDFa has been to devise a means by which documents can be
augmented with metadata in a general, rather than hard-wired, manner.
This has been achieved by creating a fixed set of attributes and parsing
rules, but allowing those attributes to contain properties from any of a
number of the growing range of available RDF vocabularies. In most cases
the *values* of those properties are the information that is
already in an author's document.

RDFa alleviates the pressure on markup language designers to anticipate
all the structural requirements users of their language might have, by
outlining a new syntax for RDF that relies only on attributes. By
adhering to the concepts and rules in this specification, language
designers can import RDFa into their environment with a minimum of
hassle and be confident that semantic data will be extractable from
their documents by conforming processors.

## 2. Syntax Overview

*This section is non-normative.*

The following examples are intended to help readers who are not
familiar with RDFa to quickly get a sense of how it works. For a more
thorough introduction, please read the RDFa Primer [RDFA-PRIMER].

In RDF, it is common for people to shorten vocabulary terms via
abbreviated IRIs that use a 'prefix' and a 'reference'. This mechanism
is explained in detail in the section titled Compact URI Expressions.
The examples throughout this document assume that the following
vocabulary prefixes have been defined:

| bibo:    | http://purl.org/ontology/bibo/              |
| -------- | ------------------------------------------- |
| cc:      | http://creativecommons.org/ns#              |
| dbp:     | http://dbpedia.org/property/                |
| dbp-owl: | http://dbpedia.org/ontology/                |
| dbr:     | http://dbpedia.org/resource/                |
| dc:      | http://purl.org/dc/terms/                   |
| ex:      | http://example.org/                         |
| foaf:    | http://xmlns.com/foaf/0.1/                  |
| owl:     | http://www.w3.org/2002/07/owl#              |
| rdf:     | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfa:    | http://www.w3.org/ns/rdfa#                  |
| rdfs:    | http://www.w3.org/2000/01/rdf-schema#       |
| xhv:     | http://www.w3.org/1999/xhtml/vocab#         |
| xsd:     | http://www.w3.org/2001/XMLSchema#           |

> **Note:**
>
> > **Note:**
> >
> > Note
>
> In some of the examples below we have used IRIs with
> fragment identifiers that are local to the document containing the RDFa
> fragment identifiers shown (e.g., '`about="#me"`'). This
> idiom, which is also used in RDF/XML [RDF-SYNTAX-GRAMMAR] and other
> RDF serializations, gives a simple way to 'mint' new IRIs for entities
> described by RDFa and therefore contributes considerably to the
> expressive power of RDFa. The precise meaning of IRIs which include
> fragment identifiers when they appear in RDF graphs is given in
> Section 7 of [RDF-SYNTAX-GRAMMAR]. To ensure that such fragment
> identifiers can be interpreted correctly, media type registrations
> for markup languages that incorporate RDFa should directly or
> indirectly reference this specification.

### 2.1 The RDFa Attributes

RDFa makes use of a number of commonly found attributes, as well as
providing a few new ones. Attributes that already exist in widely
deployed languages (e.g., HTML) have the same meaning they always did,
although their syntax has been slightly modified in some cases. For
example, in (X)HTML there is no clear way to add new @rel values; RDFa sets out to explicitly solve this problem, and does so by
allowing IRIs as values. It also introduces the concepts of terms and 'compact URI expressions'
— referred to
as CURIEs in this document — which allow a full IRI value to be
expressed succinctly. For a complete list of RDFa attribute names and
syntax, see §5 Attributes and Syntax.

### 2.2 Examples

In (X)HTML, authors can include metadata and relationships concerning
the current document by using the `meta` and `link` elements (in these examples, XHTML+RDFa [XHTML-RDFA] is used).
For example, the author of the page along with the pages
preceding and following the current page can be expressed using the
link and meta elements:
> **Example:**
>
> > **Example:**
> >
> > Example 1
>
> ```
> <html xmlns="http://www.w3.org/1999/xhtml">
>   <head>
>     <title>Page 7</title>
>     <meta name="author" content="Mark Birbeck" />
>     <link rel="prev" href="page6.html" />
>     <link rel="next" href="page8.html" />
>   </head>
>   <body>...</body>
> </html>
> ```

RDFa makes use of this concept, enhancing it with the ability to make
use of other vocabularies by using full IRIs:
> **Example:**
>
> > **Example:**
> >
> > Example 2
>
> ```
> <html xmlns="http://www.w3.org/1999/xhtml">
>   <head>
>     <title>My home-page</title>
>     <meta property="http://purl.org/dc/terms/creator" content="Mark Birbeck" />
>     <link rel="http://xmlns.com/foaf/0.1/topic" href="http://www.example.com/#us" />
>   </head>
>   <body>...</body>
> </html>
> ```

Because using full IRIs like those above can be cumbersome, RDFa also
permits the use of compact URI expressions so an author can use a shorthand to reference terms in multiple
vocabularies:
> **Example:**
>
> > **Example:**
> >
> > Example 3
>
> ```
> <html
>   xmlns="http://www.w3.org/1999/xhtml"
>   prefix="foaf: http://xmlns.com/foaf/0.1/
>           dc: http://purl.org/dc/terms/"
>   >
>   <head>
>     <title>My home-page</title>
>     <meta property="dc:creator" content="Mark Birbeck" />
>     <link rel="foaf:topic" href="http://www.example.com/#us" />
>   </head>
>   <body>...</body>
> </html>
> ```

RDFa supports the use of @rel and @rev on
any element. This is even more useful with the addition of support for
different vocabularies:
> **Example:**
>
> > **Example:**
> >
> > Example 4
>
> ```
> This document is licensed under the
> <a prefix="cc: http://creativecommons.org/ns#"
>    rel="cc:license"
>    href="http://creativecommons.org/licenses/by-nc-nd/3.0/"
>    >Creative Commons By-NC-ND License</a>.
> ```

Not only can IRIs in the document be re-used to provide metadata, but
so can inline text when used with @property:
> **Example:**
>
> > **Example:**
> >
> > Example 5
>
> ```
> <html
>   xmlns="http://www.w3.org/1999/xhtml"
>   prefix="dc: http://purl.org/dc/terms/"
>   >
>   <head><title>My Home Page</title></head>
>   <body>
>     <h1 property="dc:title">My home-page</h1>
>     <p>Last modified: 16 September 2015</p>
>   </body>
> </html>
> ```

If some displayed text is different from the actual 'value' it
represents, a more precise value can be added using @content. A value can also optionally
be typed using @datatype:
> **Example:**
>
> > **Example:**
> >
> > Example 6
>
> ```
> <html
>   xmlns="http://www.w3.org/1999/xhtml"
>   prefix="xsd: http://www.w3.org/2001/XMLSchema#
>           dc: http://purl.org/dc/terms/"
>   >
>   <head><title>My Home Page</title></head>
>   <body>
>     <h1 property="dc:title">My home-page</h1>
>     <p>Last modified: <span property="dc:modified"
>             content="2015-09-16T16:00:00-05:00"
>             datatype="xsd:dateTime">16 September 2015</span>.</p>
>   </body>
> </html>
> ```

RDFa allows the document to contain metadata information about other
documents and resources:
> **Example:**
>
> > **Example:**
> >
> > Example 7
>
> ```
> <html
>   xmlns="http://www.w3.org/1999/xhtml"
>   prefix="bibo: http://purl.org/ontology/bibo/
>           dc: http://purl.org/dc/terms/"
>   >
>   <head>
>     <title>Books by Marco Pierre White</title>
>   </head>
>   <body>
>     I think White's book
>     '<span about="urn:ISBN:0091808189"
>            property="dc:title">Canteen Cuisine</span>'
>     is well worth getting since although it's quite advanced stuff, he
>     makes it pretty easy to follow. You might also like
>     <span
>      about="urn:ISBN:1596913614"
>      property="dc:description"
>      >White's autobiography</span>.
>   </body>
> </html>
> ```

In many cases a block of markup will contain a number of properties
that relate to the same item. It's possible with RDFa to indicate the
type of that item using @typeof:
> **Example:**
>
> > **Example:**
> >
> > Example 8
>
> ```
> <html
>   xmlns="http://www.w3.org/1999/xhtml"
>   prefix="bibo: http://purl.org/ontology/bibo/
>           dc: http://purl.org/dc/terms/"
>   >
>   <head>
>     <title>Books by Marco Pierre White</title>
>   </head>
>   <body>
>     I think White's book
>     '<span about="urn:ISBN:0091808189" typeof="bibo:Book"
>            property="dc:title">Canteen Cuisine</span>'
>     is well worth getting since although it's quite advanced stuff, he
>     makes it pretty easy to follow. You might also like
>     <span
>      about="urn:ISBN:1596913614"
>      typeof="bibo:Book"
>      property="dc:description"
>      >White's autobiography</span>.
>   </body>
> </html>
> ```

When dealing with small amounts of markup, it is sometimes easier to
use full IRIs, rather than CURIEs. The previous example can also be
written as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 9
>
> ```
> <html xmlns="http://www.w3.org/1999/xhtml">
>   <head>
>     <title>Books by Marco Pierre White</title>
>   </head>
>   <body>
>     I think White's book
>     '<span
>      about="urn:ISBN:0091808189"
>      typeof="http://purl.org/ontology/bibo/Book"
>      property="http://purl.org/dc/terms/title"
>      >Canteen Cuisine</span>'
>     is well worth getting since although it's quite advanced stuff, he
>     makes it pretty easy to follow. You might also like
>     <span
>      about="urn:ISBN:1596913614"
>      typeof="http://purl.org/ontology/bibo/Book"
>      property="http://purl.org/dc/terms/description"
>      >White's autobiography</span>.
>   </body>
> </html>
> ```

A simple way of defining a portion of a document using terms from a
specific vocabulary is to use @vocab to define a default
vocabulary IRI. For example, to use FOAF terms:
> **Example:**
>
> > **Example:**
> >
> > Example 10
>
> ```
> <div vocab="http://xmlns.com/foaf/0.1/" about="#me">
>    My name is <span property="name">John Doe</span> and my blog is called
>    <a rel="homepage" href="http://example.org/blog/">Understanding Semantics</a>.
> </div>
> ```

The example above will produce the following triples, expressed here
in §3.6 Turtle syntax:
> **Example:**
>
> > **Example:**
> >
> > Example 11
>
> ```
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> <#me> foaf:name "John Doe" ;
>       foaf:homepage <http://example.org/blog/> .
> ```

In simple cases the @property property can also be used
in place of @rel. Indeed, in case when the element does
not contain @rel, @datatype, or @content,
but there is, for example, a @href, the effect of @property is analogous to the role of @rel. For example, the
previous example could have been written:
> **Example:**
>
> > **Example:**
> >
> > Example 12
>
> ```
> <div vocab="http://xmlns.com/foaf/0.1/" about="#me">
>    My name is <span property="name">John Doe</span> and my blog is called
>    <a property="homepage" href="http://example.org/blog/">Understanding Semantics</a>.
> </div>
> ```

## 3. RDF Terminology

*This section is non-normative.*

The previous section gave examples of typical markup in order to
illustrate the structure of RDFa markup. RDFa is short for "RDF in
Attributes". In order to author RDFa you do not need to understand RDF,
although it would certainly help. However, if you are building a system
that consumes the RDF output of a language that supports RDFa you will
almost certainly need to understand RDF. This section introduces the
basic concepts and terminology of RDF. For a more thorough explanation
of RDF, please refer to the RDF Concepts document [RDF-SYNTAX-GRAMMAR] and
the RDF Syntax Document [RDF-SYNTAX-GRAMMAR].

### 3.1 Statements

The structured data that RDFa provides access to is a collection of *statements*. A statement is a basic unit of information that
has been constructed in a specific format to make it easier to
process. In turn, by breaking large sets of information down into a
collection of statements, even very complex metadata can be processed
using simple rules.

To illustrate, suppose we have the following set of facts:
> **Example:**
>
> > **Example:**
> >
> > Example 13
>
> ```
> Albert was born on March 14, 1879, in the German Empire. There is a picture of him at
> the web address, http://en.wikipedia.org/wiki/Image:Albert_Einstein_Head.jpg.
> ```

This would be quite difficult for a machine to interpret, and it is
certainly not in a format that could be passed from one data
application to another. However, if we convert the information to a
set of statements it begins to be more manageable. The same
information could therefore be represented by the following shorter
'statements':
> **Example:**
>
> > **Example:**
> >
> > Example 14
>
> ```
> Albert was born on March 14, 1879.
> Albert was born in the German Empire.
> Albert has a picture at
>   http://en.wikipedia.org/wiki/Image:Albert_Einstein_Head.jpg.
> ```

### 3.2 Triples

To make this information machine-processable, RDF defines a
structure for these statements. A statement is formally called a **triple**,
meaning that it is made up of three components. The first is the *subject* of the triple, and is what we are making our statement *about*.
In all of these examples the subject is 'Albert'.

The second part of a triple is the *property* of the subject that we
want to define. In the examples here, the properties would be 'was
born on', 'was born in', and 'has a picture at'. These properties are
typically called *predicates* in RDF.

The final part of a triple is called the *object*. In the
examples here the three objects have the values 'March 14, 1879', 'the
German Empire', and
'http://en.wikipedia.org/wiki/Image:Albert_Einstein_Head.jpg'.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> RDFa supports internationalized
> characters in the subject,
> 'predicate', and the object.

### 3.3 IRI References

Breaking complex information into manageable units helps us be
specific about our data, but there is still some ambiguity. For
example, which 'Albert' are we talking about? If another system has
more facts about 'Albert', how could we know whether they are about
the same person, and so add them to the list of things we know about
that person? If we wanted to find people born in the German Empire,
how could we know that the predicate 'was born in' has the same
purpose as the predicate 'birthplace' that might exist in some other
system? RDF solves this problem by replacing our vague terms with *IRI references*.

IRIs are most commonly used to identify web pages, but RDF makes use
of them as a way to provide unique identifiers for concepts. For
example, we could identify the subject of all of our statements (the
first part of each triple) by using the DBPedia [<http://dbpedia.org>]
IRI for Albert Einstein, instead of the ambiguous string 'Albert':
> **Example:**
>
> > **Example:**
> >
> > Example 15
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein>
>    has the name
>    Albert Einstein.
> <http://dbpedia.org/resource/Albert_Einstein>
>    was born on
>    March 14, 1879.
> <http://dbpedia.org/resource/Albert_Einstein>
>    was born in
>    the German Empire.
> <http://dbpedia.org/resource/Albert_Einstein>
>    has a picture at
>    http://en.wikipedia.org/wiki/Image:Albert_Einstein_Head.jpg.
> ```

IRI references are also used to uniquely identify the objects in
metadata statements (the third part of each triple). The picture of
Einstein is already an IRI, but we could also use an IRI to uniquely
identify the country 'German Empire'. At the same time we'll indicate
that the name and date of birth really are literals (and not IRIs), by
putting quotes around them:
> **Example:**
>
> > **Example:**
> >
> > Example 16
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein>
>    has the name
>    "Albert Einstein".
> <http://dbpedia.org/resource/Albert_Einstein>
>    was born on
>    "March 14, 1879".
> <http://dbpedia.org/resource/Albert_Einstein>
>    was born in
>    <http://dbpedia.org/resource/German_Empire>.
> <http://dbpedia.org/resource/Albert_Einstein>
>    has a picture at
>    <http://en.wikipedia.org/wiki/Image:Albert_Einstein_Head.jpg>.
> ```

IRI references are also used to ensure that predicates are
unambiguous; now we can be sure that 'birthplace', 'place of birth',
'Lieu de naissance' and so on, all mean the same thing:
> **Example:**
>
> > **Example:**
> >
> > Example 17
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein>
>   <http://xmlns.com/foaf/0.1/name>
>   "Albert Einstein".
> <http://dbpedia.org/resource/Albert_Einstein>
>   <http://dbpedia.org/property/dateOfBirth>
>   "March 14, 1879".
> <http://dbpedia.org/resource/Albert_Einstein>
>   <http://dbpedia.org/property/birthPlace>
>   <http://dbpedia.org/resource/German_Empire>.
> <http://dbpedia.org/resource/Albert_Einstein>
>   <http://xmlns.com/foaf/0.1/depiction>
>   <http://en.wikipedia.org/wiki/Image:Albert_Einstein_Head.jpg>.
> ```

### 3.4 Plain Literals

Although IRI resources are always used for subjects and predicates,
the object part of a triple can be either an IRI or a **literal**.
In the example triples, Einstein's name is represented by a **plain*

*literal**, specifically a basic string with no
type or language information:
> **Example:**
>
> > **Example:**
> >
> > Example 18
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein>
>   <http://xmlns.com/foaf/0.1/name> "Albert Einstein".
> ```

A plain literal can also be given a language tag, to capture plain
text in a natural language. For example, Einstein's birthplace has
different names in English and German:
> **Example:**
>
> > **Example:**
> >
> > Example 19
>
> ```
> <http://dbpedia.org/resource/German_Empire>
>   rdfs:label "German Empire"@en;
>   rdfs:label "Deutsches Kaiserreich"@de .
> ```

### 3.5 Typed Literals

Some literals, such as dates and numbers, have very specific
meanings, so RDF provides a mechanism for indicating the type of a
literal. A **typed literal** is indicated by attaching an IRI to the end of a plain literal,
and this IRI indicates the literal's datatype. This IRI is usually
based on datatypes defined in the XML Schema Datatypes specification
[XMLSCHEMA11-2]. The following syntax would be used to unambiguously
express Einstein's date of birth as a literal of type `http://www.w3.org/2001/XMLSchema#date`:
> **Example:**
>
> > **Example:**
> >
> > Example 20
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein>
>   <http://dbpedia.org/property/dateOfBirth>
>      "1879-03-14"^^<http://www.w3.org/2001/XMLSchema#date>.
> ```

### 3.6 Turtle

RDF itself does not have one set way to express triples, since the
key ideas of RDF are the triple and the use of IRIs, and *not* any particular syntax. However, there are a number of mechanisms for
expressing triples, such as RDF/XML [RDF-SYNTAX-GRAMMAR], Turtle
[TURTLE], and of course RDFa. Many discussions of RDF make use of
the *Turtle* syntax to explain their ideas, since it is quite
compact. The examples we have just seen are already using this syntax,
and we'll continue to use it throughout this document when we need to
talk about the RDF that could be generated from some RDFa. Turtle
allows long IRIs to be abbreviated by using an IRI mapping, which can
be used to express a compact IRI expression as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 21
>
> ```
> @prefix dbp: <http://dbpedia.org/property/> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> <http://dbpedia.org/resource/Albert_Einstein>
>   foaf:name "Albert Einstein" .
> <http://dbpedia.org/resource/Albert_Einstein>
>   dbp:birthPlace <http://dbpedia.org/resource/German_Empire> .
> ```

Here 'dbp:' has been mapped to the IRI for DBPedia and 'foaf:' has
been mapped to the IRI for the 'Friend of a Friend' vocabulary.

Any IRI in Turtle could be abbreviated in this way. This means that
we could also have used the same technique to abbreviate the
identifier for Einstein, as well as the datatype indicator:
> **Example:**
>
> > **Example:**
> >
> > Example 22
>
> ```
> @prefix dbp: <http://dbpedia.org/property/> .
> @prefix dbr: <http://dbpedia.org/resource/> .
> @prefix foaf: <http://xmlns.com/foaf/0.1/> .
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
>
> dbr:Albert_Einstein
>   foaf:name "Albert Einstein";
>   dbp:birthPlace dbr:German_Empire;
>   dbp:dateOfBirth "1879-03-14"^^xsd:date;
>   foaf:depiction <http://en.wikipedia.org/wiki/Image:Albert_Einstein_Head.jpg> .
>
> dbr:German_Empire
>   rdfs:label "German Empire"@en;
>   rdfs:label "Deutsches Kaiserreich"@de .
> ```

When writing examples, you will often see the following IRI in the
Turtle representation:
> **Example:**
>
> > **Example:**
> >
> > Example 23
>
> ```
> <>
> ```

This indicates the 'current document', i.e., the document being
processed. In the end there will always be a full IRI based on the
document's location, but this abbreviation serves to make examples
more compact. Note in particular that the whole technique of
abbreviation is merely a way to make examples more compact, and the
actual triples generated would always use the full IRIs.

### 3.7 Graphs

A collection of triples is called a *graph*. All of the
triples that are defined by this specification are contained in the output graph by an RDFa Processor. For more information on graphs
and other RDF concepts, see [RDF-SYNTAX-GRAMMAR].

### 3.8 Compact URI Expressions

In order to allow for the compact expression of RDF statements, RDFa
allows the contraction of most IRI references into a
form called a 'compact URI expression', or CURIE. A
detailed discussion of this mechanism is in the section §7.4 CURIE and IRI Processing.

Note that CURIEs are only used in the markup and Turtle examples, and
will never appear in the generated triples, which are
defined by RDF to use IRI references.

### 3.9 Markup Fragments and RDFa

A growing use of embedded metadata is to take fragments of markup and
move them from one document to another. This may happen through the
use of tools, such as drag-and-drop in a browser, or through snippets
of code provided to authors for inclusion in their documents. A good
example of the latter is the licensing fragment provided by Creative Commons.

However, those involved in creating fragments (either by building
tools, or authoring snippets), should be aware that this specification
does not say how fragments are processed. Specifically, the processing
of a fragment 'outside' of a complete document is undefined because
RDFa processing is largely about context. Future versions of this or
related specifications may do more to define this behavior.

Developers of tools that process fragments, or authors of fragments
for manual inclusion, should also bear in mind what will happen to
their fragment once it is included in a complete document. They should
carefully consider the amount of 'context' information that will be
needed in order to ensure a correct interpretation of their fragment.

### 3.10 A Description of RDFa in RDF Terms

The following is a brief description of RDFa in terms of the RDF
terminology introduced here. It may be useful to readers with an RDF
background:

An *RDF graph* comprises *node*s linked by relationships. The aim of RDFa is to allow a single RDF graph to be carried in various types of document markup. The basic unit
of an RDF graph is a triple, in which a
subject node is linked to an object node via a predicate. The *subject* node is always either a IRI reference or a *blank
node (or bnode)*, the *predicate* is *always* a IRI reference, and the object of a statement can be a IRI reference, a literal, or a bnode.

In RDFa, a subject IRI reference is generally indicated
using @about and predicates are represented using one of @property, @rel, or @rev.
Objects which are IRI references are represented using @resource, @src, or @href, whilst objects that are literals
are represented either with @content or the content of
the element in question (with an optional datatype expressed using @datatype,
and an optional language expressed using a Host Language-defined
mechanism such as @xml:lang).

## 4. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples,
and notes in this specification are non-normative. Everything else in this specification is
normative.

The key words *MAY*, *MUST*, *MUST NOT*, *RECOMMENDED*, *SHOULD*, and *SHOULD NOT* are
to be interpreted as described in [RFC2119].

### 4.1 RDFa Processor Conformance

This specification uses the term *output
graph* to mean all of the triples asserted by a document
according to the §7 Processing Model section. A conforming RDFa Processor *MUST* make available to a consuming application a single RDF graph containing all possible triples generated by using the rules in the §7 Processing Model section.
The
term *processor graph* is used to denote the collection of
all informational, warning, and error triples that *MAY* be generated by
the RDFa Processor to report its status (§7.6).
The output graph and the processor graph are separate graphs and *MUST NOT* be stored in the same graph by the
RDFa Processor. However, processors may permit the two graphs to be
retrieved together; see Section 7.6.1 (§7.6.1) for details.

A conforming RDFa Processor *MAY* make available additional triples
that have been generated using rules not described here, but these
triples *MUST NOT* be made available in the output graph.
(Whether these additional triples are made available in one or more
additional RDF graphs is implementation-specific, and
therefore not defined here.)

A conforming RDFa Processor *MUST* preserve white space in both plain literals and XML literals.
However, it may be the case that the architecture in which a processor
operates has made changes to the white space in a document before that
document ever reaches the RDFa Processor (e.g., [XMLSCHEMA11-1]
processors are permitted to 'normalize' white space in attribute
values - see section 3.1.4). To ensure maximum consistency between
processing environments, authors *SHOULD* remove any unnecessary white
space in their plain and XML Literal content.

A conforming RDFa Processor *MUST* examine the media type of a document
it is processing to determine the document's Host Language. If the
RDFa Processor is unable to determine the media type, or does not
support the media type, the RDFa Processor *MUST* process the document
as if it were media type `application/xml`. See §4.3 XML+RDFa Document Conformance. A Host Language *MAY* specify additional
announcement mechanisms.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> A conforming RDFa Processor *MAY* use additional
> mechanisms (e.g., the DOCTYPE, a file extension, the root element, an overriding
> user-defined parameter) to
> attempt to determine the Host Language if the media type is
> unavailable. These mechanisms are unspecified.

### 4.2 RDFa Host Language Conformance

Host Languages that incorporate RDFa must adhere to the following:

- All of the facilities required in this specification *MUST* be
  included in the Host Language.

- The required attributes defined in this specification *MUST* be included in
  the content model of the Host Language.
  > **Note:**
  >
  > > **Note:**
  > >
  > > Note
  >
  > For the avoidance of doubt, there is no requirement that attributes
  > such as @href and @src are used in a
  > conforming Host Language. Nor is there any requirement that all
  > required attributes are incorporated into the content model of
  > all elements. The working group recommends that Host Language designers
  > ensure that the required attributes are incorporated into the content
  > model of elements that are commonly used throughout the
  > content model of the Host Language.

- If the Host Language uses XML Namespaces [XML-NAMES], the
  attributes in this specification *SHOULD* be defined in 'no
  namespace' (e.g., when the attributes are used on elements in the
  Host Language's namespace, they can be used with no qualifying
  prefix: `<myml:myElement property="license">`).

    When a Host Language does not use the attributes in 'no namespace',
they *MUST* be referenced via the XHTML Namespace (`http://www.w3.org/1999/xhtml`).

- If the Host Language has its own definition for any attribute
  defined in this specification, that definition *MUST* be such that the
  processing required by this specification remains possible when the
  attribute is used in a way consistent with the requirements herein.

- The Host Language *MAY* specify an initial context (e.g., IRI mappings and/or a definition of terms or a default
  vocabulary IRI). Such an initial context *SHOULD* be
  defined using the conventions defined in §9 RDFa Initial Contexts.

### 4.3 XML+RDFa Document Conformance

This specification does not define a stand-alone document type. The
attributes herein are intended to be integrated into other host
languages (e.g., HTML+RDFa or XHTML+RDFa). However, this specification **does** define processing rules for generic XML
documents - that is, those documents delivered as media types `text/xml` or `application/xml`. Such documents must meet all of the
following criteria:

1. The document *MUST* be well-formed as defined in [XML10-4e].
2. The document *SHOULD* use the attributes defined in this
   specification in 'no namespace' (e.g., when the attributes are used on
   elements they are used with no qualifying
   prefix: `<myml:myElement property="license">`).
   > **Note:**
   >
   > > **Note:**
   > >
   > > Note
   >
   > It is possible that an XML grammar will have native attributes that
   > conflict with attributes in this specification. This could result in an RDFa
   > processor generating unexpected triples.

When an RDFa Processor processes an XML+RDFa document, it does so via
the following initial context:

1. There are default terms (e.g., `describedby`, `license`, and `role`), defined
   in [`http://www.w3.org/2011/rdfa-context/rdfa-1.1`](https://www.w3.org/2011/rdfa-context/rdfa-1.1).
2. There are default prefix mappings (e.g., `dc`),
   defined in [`http://www.w3.org/2011/rdfa-context/rdfa-1.1`](https://www.w3.org/2011/rdfa-context/rdfa-1.1).
3. There is no default vocabulary IRI.
4. The base can be set using the @xml:base attribute as defined in [XML10-4e].
5. The current language can be set using @xml:lang attribute.

## 5. Attributes and Syntax

This specification defines a number of attributes and the way in which
the values of those attributes are to be interpreted when generating RDF
triples. This section defines the attributes and the syntax of their
values.

*about*

a SafeCURIEorCURIEorIRI, used for stating what the
data is about (a 'subject' in RDF terminology);

*content*

a `CDATA` string, for supplying machine-readable content
for a literal (a 'literal object', in RDF terminology);

*datatype*

a TERMorCURIEorAbsIRI representing a datatype, to
express the datatype of a literal;

*href* **(optional)**

a traditionally navigable IRI for expressing the
partner resource of a relationship (a 'resource object', in RDF
terminology);

*inlist*

An attribute used to indicate that the object
associated with a `rel` or `property` attribute on the same element is to be added to the list for that
predicate. The value of this attribute *MUST* be ignored.
Presence of this attribute causes a list to be created if it does not already exist.

*prefix*

a white space separated list of prefix-name IRI pairs of the form

```
NCName ':' ' '+ xsd:anyURI
```

*property*

a white space separated list of TERMorCURIEorAbsIRIs,
used for expressing relationships between a subject and either a resource
object if given or some literal
text (also a 'predicate');

*rel*

a white space separated list of TERMorCURIEorAbsIRIs,
used for expressing relationships between two resources ('predicates'
in RDF terminology);

*resource*

a SafeCURIEorCURIEorIRI for expressing the partner
resource of a relationship that is not intended to be navigable (e.g.,
a 'clickable' link) (also an 'object');

*rev*

a white space separated list of TERMorCURIEorAbsIRIs,
used for expressing reverse relationships between two resources (also
'predicates');

*src* **(optional)**

an IRI for expressing the partner resource of a
relationship when the resource is embedded (also a 'resource object');

*typeof*

a white space separated list of TERMorCURIEorAbsIRIs that indicate the RDF type(s) to associate with a subject;

*vocab*

an IRI that defines the mapping to use when a TERM is referenced in an attribute value. See §7.4.3 General Use of Terms in Attributes and the section on Vocabulary Expansion (§10).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> In all cases it is possible for these attributes to be used with
> no value (e.g., @datatype="") or with a value that evaluates to
> no value after evaluation using the rules for §7.4 CURIE and IRI Processing (e.g., @datatype="[noprefix:foobar]").

### 5.1 Roles of attributes

The RDFa attributes play different roles in a semantically rich document.
Briefly, those roles are:

- Syntax attributes: @prefix, @vocab.
- Subject attributes: @about.
- Predicate attributes: @property, @rel, @rev.
- Resource attributes: @resource, @href, @src.
- Literal attributes: @datatype, @content, @xml:lang or @lang.
- Macro attributes: @typeof, @inlist.

### 5.2 White space within attribute values

Many attributes accept a white space separated list of tokens. This
specification defines white space as:

```
whitespace      ::=  (#x20 | #x9 | #xD | #xA)+
```

When

attributes accept a white space separated list of tokens, an RDFa
Processor *MUST* ignore any leading or trailing white space.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This definition is consistent with the definition found
> in [XML10].

## 6. CURIE Syntax Definition
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The working group is currently examining the productions
> for CURIE below in light of recent comments received from the RDF
> Working Group and members of the RDFa Working
> Group. It is possible that there will be minor changes to the production
> rules below in the near future, and that these changes will be
> backward *incompatible*. However, any such incompatibility will be
> limited to edge cases.

The key component of RDF is the IRI, but these are usually long and
unwieldy. RDFa therefore supports a mechanism by which IRIs can be
abbreviated, called 'compact URI expressions' or simply, *CURIEs*.

When expanded, the resulting IRI *MUST* be a syntactically valid IRI
[RFC3987]. For a more detailed explanation see §7.4 CURIE and IRI Processing. The *lexical space* of a CURIE is as
defined in curie below. The *value space* is the set of IRIs.

A CURIE is comprised of two components, a **prefix** and a **reference**. The prefix is separated from the
reference by a colon (`:`). In general use it is possible to
omit the prefix, and so create a CURIE that makes use of the 'default
prefix' mapping; in RDFa the 'default prefix' mapping is `http://www.w3.org/1999/xhtml/vocab#`.
It's also possible to omit both the prefix *and* the colon, and
so create a CURIE that contains just a reference which makes use of the
'no prefix' mapping. This specification does not define a 'no prefix'
mapping. RDFa Host Languages *MUST NOT* define a 'no prefix' mapping.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The RDFa 'default prefix' should not be confused with the
> 'default namespace' as defined in [XML-NAMES]. An RDFa Processor *MUST NOT* treat an XML-NAMES 'default namespace' declaration as if it were
> setting the 'default prefix'.

The general syntax of a CURIE can be summarized as follows:

```
prefix      ::=   NCName

reference   ::=   ( ipath-absolute / ipath-rootless / ipath-empty )
                     [ "?" iquery ] [ "#" ifragment ] (as defined in [!RFC3987])

curie       ::=   [ [ prefix ] ':' ] reference

safe_curie  ::=   '[' [ [ prefix ] ':' ] reference ']'
```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The production `safe_curie` is not required,
> even in situations where an attribute value is permitted to be a CURIE
> or an IRI: An IRI that uses a scheme that is not an in-scope mapping *cannot* be confused with a CURIE. The concept of a safe_curie is retained for
> backward compatibility.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> It is possible to define a CURIE prefix mapping in such a way that
> it would overshadow a defined IRI scheme. For example, a document could map the prefix
> 'mailto' to 'http://www.example.com/addresses/'. Then a @resource that
> contained 'mailto:user@example.com' might create a triple with the object
> 'http://www.example.com/addresses/user@example.com'. Moreover, it is possible
> though unlikely, that schemes will be introduced in the future that will conflict
> with prefix mappings defined in a document (e.g., the newly proposed 'widget'
> scheme [WIDGETS-URI]). In neither case would this RDFa overshadowing of the
> underlying scheme alter the way other consumers of the IRI treat that IRI. It
> could, however, mean that the document author's intended use of the CURIE is
> mis-interpreted by another consumer as an IRI. The working group considers this
> risk to be minimal.

In normal evaluation of CURIEs the following context information would
need to be provided:

- a set of mappings from prefixes to IRIs;
- a mapping to use with the default prefix (for example, `:p`);
- a mapping to use when there is no prefix (for example, `p`);
- a mapping to use with the '_' prefix, which is used to generate
  unique identifiers (for example, `_:p`).

In RDFa these values are defined as follows:

- the **set of mappings from prefixes to IRIs** is
  provided by the current in-scope prefix declarations of the current element during parsing;
- the **mapping to use with the default prefix** is the
  current default prefix mapping;
- the **mapping to use when there is no prefix** is not
  defined;
- the **mapping to use with the '_' prefix**, is not
  explicitly stated, but since it is used to generate bnodes,

    its implementation needs to be compatible with the RDF definition and
rules in §7.4.5 Referencing Blank Nodes. A
  document *SHOULD NOT* define a mapping for the '_' prefix. A Conforming
  RDFa Processor *MUST* ignore any definition of a mapping for the '_'
  prefix.

A CURIE is a representation of a full IRI. The rules for determining
that IRI are:

- If a CURIE consists of an empty `prefix` and a `reference`,
  the IRI is obtained by taking the current default prefix mapping and
  concatenating it with the `reference`. If there is no
  current default prefix mapping, then this is not a valid CURIE and *MUST* be ignored.
- Otherwise, if a CURIE consists of a non-empty `prefix` and a `reference`, and if there is an in-scope mapping for `prefix` (when compared case-insensitively), then the IRI is created by using
  that mapping, and concatenating it with the `reference`.
- Finally, if there is no in-scope mapping for `prefix`,
  then the value is not a CURIE.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> See §7.4.3 General Use of Terms in Attributes for the way items with no colon can be interpreted in some datatypes by
> RDFa Processors.

### 6.1 Why CURIEs and not QNames?

*This section is non-normative.*

In many cases, language designers have attempted to use QNames for an
extension mechanism [XMLSCHEMA11-2]. QNames do permit independent
management of the name collection, and *can* map the names to
a resource. Unfortunately, QNames are unsuitable in most cases because
1) the use of QName as identifiers in attribute values and element
content is problematic as discussed in [QNAMES] and 2) the syntax of
QNames is overly restrictive and does not allow all possible IRIs to
be expressed.

A specific example of the problem this causes comes from attempting
to define the name collection for books. In a QName, the part after
the colon must be a valid element name, making an example such as the
following *invalid*: `isbn:0321154991`

This is not a valid QName simply because "0321154991" is not a valid
element name. Yet, in the example given, we don't really want to
define a valid element name anyway. The whole reason for using a QName
was to reference an item in a private scope - that of ISBNs. Moreover,
in this example, we want the names within that scope to map to an IRI
that will reveal the meaning of that ISBN. As you can see, the
definition of QNames and this (relatively common) use case are in
conflict with one another.

This specification addresses the problem by defining CURIEs.
Syntactically, CURIEs are a superset of QNames.

Note that this specification is targeted at language designers, not
document authors. Any language designer considering the use of QNames
as a way to represent IRIs or unique tokens should consider instead
using CURIEs:

- CURIEs are designed from the ground up to be used in attribute
  values. QNames are designed for unambiguously naming elements and
  attributes.
- CURIEs expand to IRIs, and any IRI can be represented by such an
  expansion. QNames are treated as value pairs, but even if those
  pairs are combined into a string, only a subset of IRIs can be
  represented.
- CURIEs can be used in non-XML grammars, and can even be used in
  XML languages that do not support XML Namespaces. QNames are limited
  to XML Namespace-aware XML Applications.

## 7. Processing Model

This section looks at a generic set of processing rules for creating a
set of triples that represent the structured data present in an RDFa
document. Processing need not follow the DOM traversal technique
outlined here, although the effect of following some other manner of
processing must be the same as if the processing outlined here were
followed. The processing model is explained using the idea of DOM
traversal which makes it easier to describe (particularly in relation to
the evaluation context).

Note that in this section, explanations about the
processing model or guidance to implementors are enclosed in sections
like this.

### 7.1 Overview

Evaluating a document for RDFa triples is carried out by starting at
the document object, and then visiting each of its child elements in
turn, in document order, applying processing rules. Processing is
recursive in that for each child element the processor also visits
each of *its* child elements, and applies the same processing
rules.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> In some environments there will be little difference
> between starting at the root element of the document, and starting at
> the document object itself. It is defined this way because in some
> environments important information is present at the document object
> level which is not present on the root element.

As processing continues, rules are applied which may generate
triples, and may also change the evaluation context information that will then be used when processing descendant
elements.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This specification does not say anything about what
> should happen to the triples generated, or whether more triples might
> be generated during processing than are outlined here. However, to be
> conforming, an RDFa Processor *MUST* act as if at a minimum the rules in
> this section are applied, and a single RDF graph produced. As described in the §4.1 RDFa Processor Conformance section, any additional triples generated *MUST NOT* appear in the output graph. They *MAY* be included in
> the processor graph.

### 7.2 Evaluation Context

During processing, each rule is applied using information provided
by an evaluation context. An *initial context* is created when processing begins. That context has the following
members:

- The *base*. This will usually be the IRI of the
  document being processed, but it could be some other IRI, set by
  some other mechanism, such as the (X)HTML `base` element. The important thing is that it establishes an IRI against
  which relative paths can be resolved.
- The *parent subject*. The initial
  value will be the same as the initial value of base,
  but it will usually change during the course of processing.
- The *parent object*. In some
  situations the object of a statement becomes the subject of any
  nested statements, and this member is used to convey this value.
  Note that this value may be a bnode, since in some
  situations a number of nested statements are grouped together on one bnode. This means that the bnode must be
  set in the containing statement and passed down.
- A list of current, in-scope *IRI

    mappings*.
- A list of *incomplete triple*s. A triple can be
  incomplete when no object resource is provided alongside a predicate
  that requires a resource (i.e., @rel or @rev).

    The triples can be completed when a resource becomes available,
which will be when the next subject is specified (part of the
process called chaining).
- A *list mapping* that associates IRIs with lists.
- The *language*. Note that there is no default
  language.
- The *term mappings*, a list of terms and their
  associated IRIs. This specification does not define an initial list.
  Host Languages *MAY* define an initial list.
- The *default vocabulary*, a value to use as the prefix
  IRI when a term unknown to the RDFa
  Processor is used. This specification does not
  define an initial setting for the default vocabulary. Host Languages *MAY* define an initial setting.

During the course of processing, new evaluation contexts
are created which are passed to each child element. The initial rules
described below will determine the values of the items in the context.
Then the core rules will cause new triples to be created by
combining information provided by an element with information from the evaluation context.

During the course of processing a number of locally scoped values are
needed, as follows:

- An initially empty list of IRI mappings, called the *local list of IRI mappings*.
- An initially empty *list of incomplete triples*,
  called the *local list of incomplete triples*.
- An initially empty language value.
- A *skip element* flag, which indicates whether the current element can safely be ignored since it has no relevant RDFa
  attributes. Note that descendant elements will still be processed.
- A *new subject* value, which once calculated will set
  the parent subject in an evaluation context, as well as being used to complete any incomplete triples, as described in the next section.
- A value for the *current
  property value*, the literal to use when creating triples
  that have a literal object, or IRI-s in the absence of @rel or @rev.
- A value for the *current
  object resource*, the resource to use when creating triples
  that have a resource object.
- A value for the *typed resource*,
  the source for creating `rdf:type` relationships to
  types specified in @typeof.
- The *local term mappings*, a list of terms and their
  associated IRIs.
- The *local list mapping*, mapping IRIs to lists
- A *local default vocabulary*, an IRI to use as a
  prefix mapping when a term is used.

### 7.3 Chaining

Statement *chaining* is an RDFa feature that allows the
author to link RDF statements together while avoiding unnecessary
repetitive markup. For example, if an author were to add statements as
children of an object that was a resource, these statements should be
interpreted as being about that resource:
> **Example:**
>
> > **Example:**
> >
> > Example 24
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div rel="dbp:birthPlace" resource="http://dbpedia.org/resource/German_Empire">
>     <span property="dbp:conventionalLongName">the German Empire</span>
>   </div>
> </div>
> ```

In this example we can see that an object resource
('German_Empire'), has become the subject for nested statements. This
markup also illustrates the basic chaining pattern of 'A has a B has a
C' (i.e., Einstein has a birth place of the German Empire, which has a
long name of 'the German Empire').

It's also possible for the subject of nested statements to provide
the object for *containing* statements — essentially the
reverse of the example we have just seen. To illustrate, we'll take an
example of the type of chaining just described, and show how it could
be marked up more efficiently. To start, we mark up the fact that
Albert Einstein had, at some point in his life, a residence both in
the German Empire and in Switzerland:
> **Example:**
>
> > **Example:**
> >
> > Example 25
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <div rel="dbp-owl:residence" resource="http://dbpedia.org/resource/German_Empire"></div>
>   <div rel="dbp-owl:residence" resource="http://dbpedia.org/resource/Switzerland"></div>
> </div>
> ```

Now, we show the same information, but this time we create an incomplete triple from the residence part, and then use any number of
further subjects to 'complete' that triple, as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 26
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein" rel="dbp-owl:residence">
>   <span about="http://dbpedia.org/resource/German_Empire"></span>
>   <span about="http://dbpedia.org/resource/Switzerland"></span>
> </div>
> ```

In this example, the incomplete triple actually gets
completed twice, once for the German Empire and once for Switzerland,
giving exactly the same information as we had in the earlier example:
> **Example:**
>
> > **Example:**
> >
> > Example 27
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein>
>   dbp-owl:residence <http://dbpedia.org/resource/German_Empire> .
> <http://dbpedia.org/resource/Albert_Einstein>
>   dbp-owl:residence <http://dbpedia.org/resource/Switzerland> .
> ```

Chaining can sometimes involve elements containing relatively
minimal markup, for example showing only one resource, or only one
predicate. Here the `img` element is used to carry a
picture of Einstein:
> **Example:**
>
> > **Example:**
> >
> > Example 28
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <div rel="foaf:depiction">
>     <img src="http://en.wikipedia.org/wiki/Image:Albert_Einstein_Head.jpg" />
>   </div>
> </div>
> ```

When such minimal markup is used, any of the resource-related
attributes could act as a subject or an object in the chaining:
> **Example:**
>
> > **Example:**
> >
> > Example 29
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <div rel="dbp-owl:residence">
>     <span about="http://dbpedia.org/resource/German_Empire"></span>
>     <span about="http://dbpedia.org/resource/Switzerland"></span>
>   </div>
> </div>
> ```

Note that, as noted above, in many situations the @property and @rel are interchangeable. This is *not* true
for chaining. Taking the first example, if that example was used as
follows:
> **Example:**
>
> > **Example:**
> >
> > Example 30
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div property="dbp:birthPlace" resource="http://dbpedia.org/resource/German_Empire">
>     <span property="dbp:conventionalLongName">the German Empire</span>
>   </div>
> </div>
> ```

The subject for 'the German Empire' would remain Albert Einstein (and
that would, of course, be an error). This is the main difference
between @property and @rel: the latter
induces chaining, whereas the former, usually, does not.

### 7.4 CURIE and IRI Processing

Since RDFa is ultimately a means for transporting RDF, a key concept
is the *resource* and its manifestation as an IRI. RDF deals
with complete IRIs (not relative paths); when converting RDFa to
triples, any relative IRIs *MUST* be resolved relative to the base IRI,
using the algorithm defined in section 6.5 of RFC 3987 [RFC3987], *Reference*

*Resolution*. The values of RDFa attributes (§5) that refer to IRIs use three different datatypes: IRI, SafeCURIEorCURIEorIRI, or TERMorCURIEorAbsIRI.
All these attributes are mapped, after processing, to IRIs. The
handling of these attributes is as follows:

IRI

The content is an IRI, and is used as such.

SafeCURIEorCURIEorIRI

- When the value is surrounded by square brackets, then the
  content within the brackets is evaluated as a CURIE according to
  the §6 CURIE Syntax Definition. If it is
  not a valid CURIE, the value *MUST* be ignored.
- Otherwise, the value is evaluated as a CURIE. If it is a valid
  CURIE, the resulting IRI is used; otherwise, the value is
  processed as an IRI.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> A consequence of this is that when the value of an attribute of this
> datatype is the empty string (e.g., @about=""), that value resolves to an
> IRI. An IRI of "" is a relative IRI that is interpreted as being the same as the base.
> In other words, a value of "" will usually resolve to the IRI of the current document.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> A related consequence of this is that when the value of an attribute of this datatype is an empty SafeCURIE (e.g., @about="[]"), that value does not result in an IRI and therefore the value is ignored.

TERMorCURIEorAbsIRI

- If the value is a term then it is evaluated as a term according to §7.4.3 General Use of Terms in Attributes. Note that this step may mean
  that the value is to be ignored.
- If the value is a valid CURIE, then the resulting IRI is used.
- If the value is an absolute IRI, that value is used.
- Otherwise, the value is ignored.

Note

that it is possible for all values in an attribute to be ignored. When
that happens, the attribute *MUST* be treated as if it were empty.

For example, the full IRI for Albert Einstein on DBPedia is:
> **Example:**
>
> > **Example:**
> >
> > Example 31
>
> ```
> http://dbpedia.org/resource/Albert_Einstein
> ```

This can be shortened by authors to make the information easier to
manage, using a CURIE. The first step is for the author to create a
prefix mapping that links a prefix to some leading segment of the IRI.
In RDFa these mappings are expressed using @prefix:
> **Example:**
>
> > **Example:**
> >
> > Example 32
>
> ```
> <div prefix="db: http://dbpedia.org/">
>   ...
> </div>
> ```

Once the prefix has been established, an author can then use it to
shorten an IRI as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 33
>
> ```
> <div prefix="db: http://dbpedia.org/">
>   <div about="db:resource/Albert_Einstein">
>     ...
>   </div>
> </div>
> ```

The author is free to split the IRI at any point.
However, since a common use of CURIEs is to
make available libraries of terms and values, the prefix will usually
be mapped to some common segment that provides the most re-use, often
provided by those who manage the library of terms. For example, since
DBPedia contains an enormous list of resources, it is more efficient
to create a prefix mapping that uses the base location of the
resources:
> **Example:**
>
> > **Example:**
> >
> > Example 34
>
> ```
> <div prefix="dbr: http://dbpedia.org/resource/">
>   <div about="dbr:Albert_Einstein">
>     ...
>   </div>
>   <div about="dbr:Baruch_Spinoza">
>     ...
>   </div>
> </div>
> ```

Note that it is generally considered a bad
idea to use relative paths in prefix declarations. Since it is
possible that an author may ignore this guidance, it is further
possible that the IRI obtained from a CURIE is relative. However,
since all IRIs must be resolved relative to base before
being used to create triples, the use of relative paths should not
have any effect on processing.

#### 7.4.1 Scoping of Prefix Mappings

CURIE prefix mappings are defined on the current element and its
descendants. The inner-most mapping for a given prefix takes
precedence. For example, the IRIs expressed by the following two
CURIEs are different, despite the common prefix, because the prefix
mappings are locally scoped:
> **Example:**
>
> > **Example:**
> >
> > Example 35
>
> ```
> <div prefix="dbr: http://dbpedia.org/resource/">
>   <div about="dbr:Albert_Einstein">
>     ...
>   </div>
> </div>
> <div prefix="dbr: http://someotherdb.org/resource/">
>   <div about="dbr:Albert_Einstein">
>     ...
>   </div>
> </div>
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> In general it is a bad practice to redefine prefix
> mappings within a document. In particular, while it is permitted, mapping a
> prefix to different values at different places within a document could lead to
> confusion. The working group recommends that document authors use the same
> prefix to map to the same vocabulary throughout a document. Many vocabularies
> have recommended prefix names. The working group recommends that these names
> are used whenever possible.

#### 7.4.2 General Use of CURIEs in Attributes

There are a number of ways that attributes make use of CURIEs, and
they need to be dealt with differently. These are:

1. An attribute may allow one or more values that are a mixture of
   TERMs, CURIEs, and absolute IRIs.
2. An attribute may allow one or more values that are a mixture of
   CURIEs and IRIs. In this case any value that is not a CURIE, as
   outlined in section §6 CURIE Syntax Definition,
   will be processed as an IRI.
3. If the value *is* surrounded by square brackets, then
   the content within the brackets is always evaluated according to
   the rules in §6 CURIE Syntax Definition -
   and if that content is not a CURIE, then the content *MUST* be
   ignored.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> An empty attribute value (e.g., `typeof=''`)
> is *still* a CURIE, and is processed as such. The rules
> for this processing are defined in §7.5 Sequence.
> Specifically, however, an empty attribute value is *never* treated as a relative IRI by this specification.

An example of an attribute that can contain a CURIEorIRI is @about.
To express an IRI directly, an author might do this:
> **Example:**
>
> > **Example:**
> >
> > Example 36
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   ...
> </div>
> ```

whilst to express the IRI above as a CURIE an author would do this:
> **Example:**
>
> > **Example:**
> >
> > Example 37
>
> ```
> <div about="dbr:Albert_Einstein">
>   ...
> </div>
> ```

The author could also use a safe CURIE, as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 38
>
> ```
> <div about="[dbr:Albert_Einstein]">
>   ...
> </div>
> ```

Since non-CURIE values *MUST* be ignored, the following value in @about would *not* set a new subject, since @about does not permit the use of TERMs, and the CURIE
has no prefix separator.
> **Example:**
>
> > **Example:**
> >
> > Example 39
>
> ```
> <div about="[Albert_Einstein]">
>   ...
> </div>
> ```

However, this markup *would* set a subject, since it is not
a CURIE, but a valid relative IRI:
> **Example:**
>
> > **Example:**
> >
> > Example 40
>
> ```
> <div about="Albert_Einstein">
>   ...
> </div>
> ```

Note that several RDFa attributes are able to also take TERMS as their value.
This is discussed in the next section.

#### 7.4.3 General Use of Terms in Attributes

Some RDFa attributes have a datatype that permits a *term* to be referenced.
RDFa defines the syntax of a term as:

```
term     ::=  NCNameStartChar termChar*
termChar ::=  ( NameChar - ':' ) | '/'

```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> For the avoidance of doubt, this production
> means a 'term' in RDFa is an XML [NCName](https://www.w3.org/TR/2006/REC-xml-names-20060816/#NT-NCName) that also permits
> slash as a non-leading character.

When an RDFa attribute permits the use of a term, and the value
being evaluated matches the production for term above, it is
transformed to an IRI using the following logic:

- If there is a local default vocabulary the IRI is
  obtained by concatenating that value and the `term`.
- Otherwise, check if the `term` matches an item in the list of local term mappings. First compare against the list *case-sensitively*,
  and if there is no match then compare *case-insensitively*.
  If there is a match, use the associated IRI.
- Otherwise, the `term` has no associated IRI and *MUST* be ignored.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> A local default vocabulary can be defined by the
> Host Language as part of the initial context, and can be overridden on
> the current element and its children using @vocab.

#### 7.4.4 Use of CURIEs in Specific Attributes

The general rules discussed in the previous sections apply to the
RDFa attributes in the following ways:

- @about and @resource support the
  datatype SafeCURIEorCURIEorIRI \- allowing a
  SafeCURIE, a CURIE, or an IRI.
- @href and @src are as defined in the
  Host Language (e.g., XHTML), and support only an IRI.
- @vocab supports an IRI.
- @datatype supports the datatype TERMorCURIEorAbsIRI - allowing a single Term, CURIE, or Absolute IRI.
- @property, @typeof, @rel,
  and @rev support the datatype TERMorCURIEorAbsIRIs \- allowing one or more Terms, CURIEs, or Absolute IRIs.

Any value that matches a defined term *MUST* be expanded into a
reference to the corresponding IRI. For example in
the following examples:
> **Example:**
>
> > **Example:**
> >
> > Example 41
>
> ```
> <link rel="license" href="http://example.org/license.html" />
> <link rel="xhv:license" href="http://example.org/license.html" />
> ```

would each generate the following triple:
> **Example:**
>
> > **Example:**
> >
> > Example 42
>
> ```
> <> <http://www.w3.org/1999/xhtml/vocab#license> <http://example.org/license.html> .
> ```

#### 7.4.5 Referencing Blank Nodes

In RDFa, it is possible to establish relationships using various
types of resource references, including bnodes. If a
subject or object is defined using a CURIE, and that CURIE
explicitly names a bnode, then a Conforming Processor *MUST* create the bnode when it is encountered during
parsing. The RDFa Processor *MUST* also ensure that no bnode created automatically (e.g., as a result of chaining) has a
name that collides with a bnode that is defined by
explicit reference in a CURIE.

Consider the following example:
> **Example:**
>
> > **Example:**
> >
> > Example 43
>
> ```
> <link about="_:john" rel="foaf:mbox"
>   href="mailto:john@example.org" />
> <link about="_:sue" rel="foaf:mbox"
>   href="mailto:sue@example.org" />
> <link about="_:john" rel="foaf:knows"
>   resource="_:sue" />
> ```

In the above fragment, two bnodes are
explicitly created as the subject of triples. Those bnodes are then referenced to demonstrate the relationship between the
parties. After processing, the following triples will be generated:
> **Example:**
>
> > **Example:**
> >
> > Example 44
>
> ```
> _:john foaf:mbox <mailto:john@example.org> .
> _:sue foaf:mbox <mailto:sue@example.org> .
> _:john foaf:knows _:sue .
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> RDFa Processors use, internally, implementation-dependent
> identifiers for bnodes. When triples are *retrieved*, new
> bnode indentifiers are used, which usually bear no relation to the
> original identifiers. However, implementations do ensure that these
> generated bnode identifiers are consistent: each bnode will have its
> own identifier, all references to a particular bnode will use the
> same identifier, and different bnodes will have different
> identifiers.

As a special case, `_:` is also a valid reference for *one* specific bnode.

### 7.5 Sequence

Processing would normally begin after the document to be parsed has
been completely loaded. However, there is no requirement for this to
be the case, and it is certainly possible to use a stream-based
approach, such as SAX [SAX] to extract the RDFa information.
However, if some approach other than the DOM traversal technique
defined here is used, it is important to ensure that Host
Language-specific processing rules are applied (e.g., XHTML+RDFa
[XHTML-RDFA] indicates the `base` element can be used,
and `base` will affect the interpretation of IRIs in `meta` or `link` elements even if those elements are before the `base` element in the stream).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> In this section the term 'resource' is used to mean 'IRI or bnode'. It is possible that this term will be replaced with
> some other, more formal term after consulting with other groups. Changing this
> term will in no way change this processing sequence.

At the beginning of processing, an initial *evaluation

context* is created, as follows:

- the base is set to the IRI of the document (or
  another value specified in a language specific manner such as the
  HTML `base` element);
- the parent subject is set to the base value;
- the parent object is set to null;
- the list of incomplete triples is empty;
- the list mapping is empty;
- the language is set to null.
- the list of IRI mappings is empty (or a list defined
  in the initial context (§9) of the Host
  Language).
- the term mappings is set to null (or a list defined in the initial context (§9) of the Host
  Language).
- the default vocabulary is set to null (or an IRI defined in
  the initial context (§9) of the Host
  Language).

Processing begins by applying the processing rules below to the
document object, in the context of this initial evaluation context. All elements in the tree are also processed
according to the rules described below, depth-first, although the evaluation context used for each set of rules will be based on previous
rules that may have been applied.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This specification defines processing rules for optional
> attributes that may not be present in all Host Languages (e.g., @href).
> If these attributes are not supported in the Host Language, then the
> corresponding processing rules are not relevant for that language.

The processing rules are:

1. First, the local values are initialized,
   as follows:

   - the skip element flag is set to 'false';
   - new subject is set to null;
   - current object resource is set to null;
   - typed resource is set to null;
   - the local list of IRI mappings is set to the
     list of IRI mappings from the evaluation context;
   - the local list of incomplete triples is set to
     null;
   - the list mapping is set to (a reference of) the
     list mapping from the evaluation context;
   - the current language value is set to the language value from the evaluation context.
   - the local term mappings is set to the term mappings from the evaluation context.
   - the local default vocabulary is set to the default vocabulary from the evaluation context.

   Note that some of the local variables are
   temporary containers for values that will be passed to descendant
   elements via an evaluation context. In some cases
   the containers will have the same name, so to make it clear which
   is being acted upon in the following steps, the local version of
   an item will generally be referred to as such.

   Note that the local term mappings is always reset to a global
   value, provided by the initial context.
   Future versions of this specification may introduce
   a mechanism whereby the local term mappings can be set dynamically, in which case the local term mappings would inherit from the parent's values.

2. Next the *current element* is examined for any change to the default vocabulary via @vocab. If @vocab is present and contains
   a value, the local default vocabulary is updated
   according to the section on §7.4 CURIE and IRI Processing.
   If the value is empty, then the local default vocabulary *MUST* be reset to the Host Language
   defined default (if any).

   The value of @vocab is used
   to generate a triple as follows:

   subject

   base

   predicate

   `http://www.w3.org/ns/rdfa#usesVocabulary`

   object

   value from @vocab

   A Host Language is not required to define
   a default vocabulary. In such a case, setting @vocab to the empty value has the effect of setting the local default vocabulary to null.

3. Next, the current element is
   examined for *IRI mapping*s and these are added to the local list of IRI mappings. Note that an IRI mapping will simply overwrite any current mapping in the list that has the
   same name;

   Mappings are defined via @prefix. Values

    in this attribute are evaluated from beginning to end (e.g.,
left to right in typical documents). For

    backward compatibility, RDFa Processors *SHOULD* also permit the
   definition of mappings via @xmlns. In
   this case, the value to be mapped is set by the XML namespace
   prefix, and the value to map is the value of the attribute — an
   IRI. (Note that prefix mapping via @xmlns is deprecated, and may be removed in a future version of this
   specification.) When xmlns is
   supported, such mappings *MUST* be processed before processing any
   mappings from @prefix on the same element. Regardless of how the mapping is declared, the value to be
   mapped *MUST* be converted to lower case, and the IRI is
   not processed in any way; in particular if it is a relative path
   it *MUST NOT* be resolved against the current base.
   Authors *SHOULD NOT* use relative paths as the IRI.

4. The current element is also parsed for any language
   information, and if present, current language is set
   accordingly;

   Host Languages that incorporate RDFa *MAY* provide a mechanism for specifying the natural language of an
   element and its contents (e.g., XML provides the general-purpose
   XML attribute @xml:lang).

5. If the current element contains
   no @rel or @rev attribute, then the next
   step is to establish a value for new subject. This
   step has two possible alternatives.

   1. If the current element contains the @property attribute, but does *not* contain either the @content or @datatype attributes, then

      new subject is set to
      the resource obtained from the first match from the following rule:

      - by using the resource from @about, if present,
        obtained according to the section on §7.4 CURIE and IRI Processing;
      - *otherwise*, if the element is the root element of the document, then
        act as if there is an empty @about present,
        and process it according to the rule for @about,
        above;
      - *otherwise*, if parent object is
        present, new subject is set to the value of parent object.

      If @typeof is present then typed resource is set to the resource obtained from the first match from the following rules:

      - by using the resource from @about, if present,
        obtained according to the section on §7.4 CURIE and IRI Processing;
      - *otherwise*, if the element is the root element of the document, then
        act as if there is an empty @about present and process it according to the previous
        rule;
      - *otherwise*,
        * by using the resource from @resource, if present,
          obtained according to the section on §7.4 CURIE and IRI Processing;
        * *otherwise*, by using the IRI from @href,
          if present, obtained according to the section on §7.4 CURIE and IRI Processing;
        * *otherwise*, by using the IRI from @src,
          if present, obtained according to the section on §7.4 CURIE and IRI Processing;
        * *otherwise*, the value of typed resource is
          set to a newly created bnode.
        * The value of the current object resource is then set to the value of typed resource.

   2. *otherwise*:

      - If the element contains an @about, @href, @src, or @resource attribute, new subject is set to the resource obtained as follows:

        * by using the resource from @about, if present,
          obtained according to the section on §7.4 CURIE and IRI Processing;
        * *otherwise*, by using the resource from @resource, if present,
          obtained according to the section on §7.4 CURIE and IRI Processing;
        * *otherwise*, by using the IRI from @href,
          if present, obtained according to the section on §7.4 CURIE and IRI Processing;
        * *otherwise*, by using the IRI from @src,
          if present, obtained according to the section on §7.4 CURIE and IRI Processing.

      - *otherwise*, if no resource is provided by a resource attribute, then the
        first match from the following rules will apply:

        * if the element is the root element of the document, then
          act as if there is an empty @about present,
          and process it according to the rule for @about,
          above;
        * *otherwise*, if @typeof is present, then new subject is set to be a newly created bnode;
        * *otherwise*, if parent object is
          present, new subject is set to the value of parent object. Additionally, if @property is *not* present then the skip element flag is set to 'true'.

      - Finally, if @typeof is present, set the typed resource to the value of new subject.

6. If the current element *does* contain a @rel or @rev attribute, then the next step is to establish *both* a value
   for new subject and a value for current object resource:

   new subject is set to the
   resource obtained from the first match from the following rules:

   - by using the resource from @about, if present,
     obtained according to the section on §7.4 CURIE and IRI Processing;

   if the @typeof attribute is present, set typed resource to new subject.

   If no resource is provided then the first match from the following
   rules will apply:

   - if the element is the root element of the document then act
     as if there is an empty @about present, and
     process it according to the rule for @about,
     above;
   - *otherwise*, if parent object is
     present, new subject is set to that.

   Then the current object resource is set to the
   resource obtained from the first match from the following rules:

   - by using the resource from @resource, if present,
     obtained according to the section on §7.4 CURIE and IRI Processing;
   - *otherwise*, by using the IRI from @href,
     if present, obtained according to the section on §7.4 CURIE and IRI Processing;
   - *otherwise*, by using the IRI from @src,
     if present, obtained according to the section on §7.4 CURIE and IRI Processing;
   - *otherwise*, if @typeof is present and @about is not, use a newly created bnode.

   If @typeof is present and @about is
   not, set typed resource to current object resource.

   Note that final value of the current object resource will either be null (from initialization) or a full IRI or bnode.

7. If in any of the previous steps a typed resource was
   set to a non-null value, it is now used to provide a subject for
   type values;

   One or more 'types' for the typed resource can be set by using @typeof. If
   present, the attribute may contain one or more IRIs, obtained
   according to the section on §7.4 CURIE and IRI Processing, each of which is used to generate a
   triple as follows:

   subject

   typed resource

   predicate

   http://www.w3.org/1999/02/22-rdf-syntax-ns#type

   object

   current full IRI of 'type' from typed resource

8. If in any of the previous steps a new subject was set to a non-null value *different* from the parent object;

   The list mapping taken from
   the evaluation context is set to a new, empty
   mapping.

9. If in any of the previous steps a current object resource was set to a non-null value, it is now used
   to generate triples and add entries to the local list mapping:

   If the element contains *both* the @inlist and the @rel attributes the @rel may contain one or more resources, obtained according to the section on §7.4 CURIE and IRI Processing each of
   which is used to add an entry to the list mapping as
   follows:

   - if the local list mapping does not contain a
     list associated with the IRI, instantiate a new list and add
     to local list mappings
   - add the current object resource to the list
     associated with the resource in the local list mapping

   Predicates for the current object resource can be set by using one or both of the @rel and the @rev attributes but, in case of the @rel attribute, only if the @inlist is *not* present:

   - If present, @rel may contain one or more resources,
     obtained according to the section on §7.4 CURIE and IRI Processing each of which is used to generate a
     triple as follows:

     subject

     new subject

     predicate

     full IRI

     object

     current object resource

   - If present, @rev may contain one or more resources,
     obtained according to the section on §7.4 CURIE and IRI Processing each of which is used to generate a
     triple as follows:

     subject

     current object resource

     predicate

     full IRI

     object

     new subject

10. If however current object resource was set to null, but there are predicates present,
    then they must be stored as incomplete triples,
    pending the discovery of a subject that can be used as the object.
    Also, current object resource should be set to a newly
    created bnode (so that the incomplete triples have a
    subject to connect to if they are ultimately turned into triples);

    Predicates for incomplete triples
    can be set by using one or both of the @rel and @rev attributes:

    - If present, @rel must contain one or more
      resources, obtained according to the section on §7.4 CURIE and IRI Processing each of which is added to the local list of incomplete triples as follows:
      * If the element contains the @inlist attribute, then
        + if the local list mapping does not
          contain a list associated with the IRI, instantiate a
          new list and add to local list mappings.
        + Add:

          list

          list from local list mapping for
          this IRI

          direction

          none

      * Otherwise add:
        + predicate

          full IRI

          direction

          forward

    - If present, @rev must contain one or more
      resources, obtained according to the section on §7.4 CURIE and IRI Processing, each of which is added to the local list of incomplete triples as follows:

      predicate

      full IRI

      direction

      reverse

11. The next step of the iteration is
    to establish any current property value;

    Predicates for the current property value can be set by using @property. If
    present, one or more resources are obtained according to the section on §7.4 CURIE and IRI Processing, and
    then the actual literal value is obtained as follows:

    - as a typed literal if @datatype is present, does not have an empty value according to the
      section on §7.4 CURIE and IRI Processing, and is not set to `XMLLiteral` in the vocabulary `http://www.w3.org/1999/02/22-rdf-syntax-ns#`.

      The actual literal is either the value of @content (if present) *or* a string created by concatenating
      the value of all descendant text nodes, of the current element in turn. The final string includes the
      datatype IRI, as described in [RDF-SYNTAX-GRAMMAR], which will
      have been obtained according to the section on §7.4 CURIE and IRI Processing.

    - *otherwise*, as a plain literal if @datatype is present but has an empty value according to the section on §7.4 CURIE and IRI Processing.

      The actual literal is either the value of @content (if present) *or* a string created by concatenating
      the value of all descendant text nodes, of the current element in turn.

    - *otherwise*, as an XML literal if @datatype is present and is
      set to `XMLLiteral` in the vocabulary `http://www.w3.org/1999/02/22-rdf-syntax-ns#`.

      The value of the XML literal is a string created by serializing to text, all nodes that
      are descendants of the current element, i.e.,
      not including the element itself, and giving it a datatype
      of `XMLLiteral` in the vocabulary `http://www.w3.org/1999/02/22-rdf-syntax-ns#`.
      The format of the resulting serialized content is as defined
      in Exclusive XML Canonicalization Version 1.0 [XML-EXC-C14N].
      > **Note:**
      >
      > > **Note:**
      > >
      > > Note
      >
      > In order to maintain maximum portability of this literal,
      > any children of the current node that are elements *MUST* have
      > the current XML namespace declarations (if any) declared on
      > the serialized element. Since the child element node could
      > also declare new XML namespaces, the RDFa Processor *MUST* be
      > careful to merge these together when generating the
      > serialized element definition. For avoidance of doubt, any
      > re-declarations on the child node *MUST* take precedence over
      > declarations that were active on the current node.

    - *otherwise*, as a plain literal using
      the value of @content if @content is
      present.

    - *otherwise*, if the @rel, @rev,
      and @content attributes are *not* present,
      as a resource
      obtained from one of the following:

      * by using the resource from @resource, if present,
        obtained according to the section on §7.4 CURIE and IRI Processing;
      * *otherwise*, by using the IRI from @href,
        if present, obtained according to the section on §7.4 CURIE and IRI Processing;
      * *otherwise*, by using the IRI from @src,
        if present, obtained according to the section on §7.4 CURIE and IRI Processing.

    - *otherwise*, if @typeof is present and @about is not, the value of typed resource.

    - *otherwise* as a plain literal.

    Additionally, if there is a value for *current
    language* then the value of the plain literal should include this language information, as described in
    [RDF-SYNTAX-GRAMMAR]. The actual literal is either the value of @content (if present) *or* a string
    created by concatenating the text content of each of the
    descendant elements of the current element in
    document order.

    The current property value is then used with each
    predicate as follows:

    - If the element also includes the @inlist attribute, the current property value is added
      to the local list mapping as follows:
      * if the local list mapping does not contain
        a list associated with the predicate IRI, instantiate a
        new list and add to local list mappings
      * add the current property value to the list
        associated with the predicate IRI in the local list mapping
    - Otherwise the current property value is used
      to generate a triple as follows:

      subject

      new subject

      predicate

      full IRI

      object

      current property value

12. If the skip element flag
    is 'false', *and* new subject was set to a
    non-null value, then any incomplete triples *within*

    *the current context* should be completed:

    The list of incomplete triples from the current evaluation context (*not* the local list of incomplete triples) will contain
    zero or more predicate IRIs. This list is iterated over and each
    of the predicates is used with parent subject and new subject to generate a triple or add a new element to the local list mapping. Note that at each level there are *two* lists of incomplete triples; one for
    the current processing level (which is passed to each child
    element in the previous step), and one that was received as part
    of the evaluation context. It is the latter that is
    used in processing during this step.

    Note that each incomplete triple has a *direction* value that is used to determine what
    will become the subject, and what will become the object, of each
    generated triple:

    - If direction is 'none', the new subject is added to the list from the iterated incomplete triple.

    - If direction is 'forward' then the following
      triple is generated:

      subject

      parent subject

      predicate

      the predicate from the iterated incomplete triple

      object

      new subject

    - If direction is 'reverse'
      then this is the triple generated:

      subject

      new subject

      predicate

      the predicate from the iterated incomplete triple

      object

      parent subject

13. Next, all elements that are children of the current element are processed using the rules described here, using
    a new evaluation context, initialized as follows:

    - If the skip element flag is 'true' then the new evaluation context is a copy of the current context
      that was passed in to this level of processing, with the language and list of IRI mappings values replaced with the
      local values;
    - Otherwise, the values are:
      * the base is set to the base value of the current evaluation context;
      * the parent subject is set to the value of new subject, if non-null, *or* the value of the parent subject of the current evaluation context;
      * the parent object is set to value of current object resource, if non-null, *or* the
        value of new subject, if non-null, *or* the value of the parent subject of the current evaluation context;
      * the list of IRI mappings is set to the local list of IRI mappings;
      * the list of incomplete triples is set to the local list of incomplete triples;
      * the list mapping is set to the local list mapping;
      * language is set to the value of current language.
      * the default vocabulary is set to the value
        of the local default vocabulary.

14. Finally, if there is one or more mapping in
    the local list mapping, list triples are generated as
    follows:

    For each IRI in the local list mapping,
    if the equivalent list does not exist in the evaluation context, indicating that the list was
    originally instantiated on the current element, use the list as
    follows:

    - If there are zero items in the list associated with the IRI,
      generate the following triple:

      subject

      current subject

      predicate

      full IRI of the local list mapping associated with this list

      object

      `http://www.w3.org/1999/02/22-rdf-syntax-ns#nil`

    - Otherwise,
      * Create a new ‘bnode’ array containing newly created bnodes,

            one for each item in the list

      * For each bnode-(IRI or literal) pair from the list
        the following triple is generated:

        subject

        bnode

        predicate

        `http://www.w3.org/1999/02/22-rdf-syntax-ns#first`

        object

        full IRI or literal

      * For each item in the ‘bnode’ array the following triple
        is generated:

        subject

        bnode

        predicate

        `http://www.w3.org/1999/02/22-rdf-syntax-ns#rest`

        object

        next item in the ‘bnode’ array or, if that does not
        exist, `http://www.w3.org/1999/02/22-rdf-syntax-ns#nil`

      * A single additional triple is generated:

        subject

        current subject

        predicate

        full IRI of the local list mapping associated with this list

        object

        first item of the ‘bnode’ array

### 7.6 Processor Status

The processing rules covered in the previous section are designed to
extract as many triples as possible from a document. The RDFa
Processor is designed to continue processing, even in the event of
errors. For example, failing to resolve a prefix mapping or term would result in the RDFa Processor skipping the generation of a triple
and continuing with document processing. There are cases where knowing
each RDFa Processor warning or error would be beneficial to authors.
The processor graph is designed as the mechanism
to capture all informational, warning, and error messages as triples
from the RDFa Processor. These status triples may be retrieved and
used to aid RDFa authoring or automated error detection.

If an RDFa Processor supports the generation of a processor graph,
then it *MUST* generate a set of triples when the following processing
issues occur:

- An `rdfa:Error` *MUST* be generated when the document fails to be
  fully processed as a result of non-conformant Host Language markup.
- A `rdfa:Warning` *MUST* be generated when a CURIE prefix fails to be
  resolved.
- A `rdfa:Warning` *MUST* be generated when a Term fails to be resolved.

Other implementation-specific `rdfa:Info`, `rdfa:Warning`,
or `rdfa:Error` triples *MAY* be generated by the RDFa Processor.

#### 7.6.1 Accessing the Processor Graph

Accessing the processor graph may be accomplished in
a variety of ways and is dependent on the type of RDFa Processor and
access method that the developer is utilizing.

SAX-based processors or processors that utilize function or method
callbacks to report the generation of triples are classified as *event-based

RDFa Processor*s. For Event-based RDFa Processors, the
software *MUST* allow the developer to register a function or callback
that is called when a triple is generated for the processor graph. The callback *MAY* be the same as the one that is used
for the output graph as long as it can be determined
if a generated triple belongs in the processor graph or the output graph.

A *whole-graph RDFa Processor* is defined as any RDFa
Processor that processes the entire document and only
provides the
developer access to the triples after processing has completed. RDFa
Processors that typically fall into this category express their
output via a single call using RDF/XML, N3, TURTLE, or N-Triples
notation. For whole-graph RDFa Processors, the software *MUST* allow
the developer to specify if they would like to retrieve the output graph, the processor graph, or both graphs as
a single, combined graph from the RDFa Processor. If the graph preference is not specified, the output graph *MUST* be returned.

A *web service RDFa Processor* is defined as any RDFa
Processor that is capable of processing a document by performing an
HTTP GET, POST or similar action on an RDFa Processor IRI. For this
class of RDFa Processor, the software *MUST* allow the caller to
specify if they would like to retrieve the output graph,
the processor graph, or both graphs as a single,
combined graph from the web service. The `rdfagraph` query parameter *MUST* be used to specify the value. The allowable
values are `output`, `processor` or both
values, in any order, separated by a comma character. If the graph preference is not specified, the output graph *MUST* be returned.

#### 7.6.2 Processor Graph Terms

To ensure interoperability, a core hierarchy of classes is defined
for the content of the processor graph. Separate errors or warnings
are resources (typically blank nodes) of a specific type, with
additional properties giving more details on the error condition or
the warning. This specification defines only the top level classes
and the ones referring to the error and warning conditions defined explicitly (§7.6) by this document. Other, implementation-specific subclasses may be
defined by the RDFa Processor.

The top level classes are `rdfa:Error`, `rdfa:Warning`,
and `rdfa:Info`, defined as part of the RDFa Vocabulary (§B.2). Furthermore, a single property is defined on those
classes, namely `rdfa:context`, that provides an extra
context for the error, e.g., http response, an XPath information, or
simply the IRI to the RDFa resource. Usage of this property is
optional, and more than one triple can be used with this predicate
on the same subject. Finally, error and warning instances *SHOULD* use
the `dc:description` and `dc:date` properties. `dc:description` should provide a short,
human readable but implementation dependent description of the
error. `dc:date` should give the time when the error was
found and it is advised to be as precise as possible to allow the
detection of, for example, possible network errors.

The example below shows the triples that should be minimally
present in the processor graph as a result of an error (the content
of the literal for the `dc:description` predicate is
implementation dependent):
> **Example:**
>
> > **Example:**
> >
> > Example 45
>
> ```
> @prefix rdfa:    <http://www.w3.org/ns/rdfa#> .
> @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
> @prefix dc:      <http://purl.org/dc/terms/> .
> [] a rdfa:DocumentError ;
>    dc:description "The document could not be parsed due to parsing errors." ;
>    dc:date "2010-06-30T13:40:23"^^xsd:dateTime .
> ```

A slightly more elaborate example makes use of the `rdfa:context` property to provide further information, using external vocabularies
to represent HTTP headers or XPointer information (note that a
processor may not have these information in all cases, i.e., these `rdfa:context` information are not required):
> **Example:**
>
> > **Example:**
> >
> > Example 46
>
> ```
> @prefix rdfa:    <http://www.w3.org/ns/rdfa#> .
> @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
> @prefix dc:      <http://purl.org/dc/terms/> .
> @prefix ptr:     <http://www.w3.org/2009/pointers#> .
> @prefix ht:      <http://www.w3.org/2006/http#> .
>
> [] a rdfa:DocumentError ;
>    dc:description "The document could not be parsed due to parsing errors." ;
>    dc:date "2010-06-30T13:40:23"^^xsd:dateTime ;
>    rdfa:context <http://www.example.org/doc> ;
>    rdfa:context [
>       a ptr:Pointer ;
>       # Detailed xpointer/xpath information provided here to locate the error.
>    ] ;
>    rdfa:context [
>       a ht:Response ;
>       ht:responseCode <http://www.w3.org/2006/http#404>
>       # The HTTP response headers on the request for the source file.
>    ].
> ```

### 7.7 Vocabulary Expansion

Processors *MAY* perform vocabulary expansion by
utilizing limited RDFS and OWL entailment rules,
as described in §10 RDFa Vocabulary Expansion.

## 8. RDFa Processing in detail

*This section is non-normative.*

This section provides an in-depth examination of the processing steps
described in the previous section. It also includes examples which may
help clarify some of the steps involved.

The key to processing is that a triple is generated whenever a
predicate/object combination is detected. The actual triple generated
will include a subject that may have been set previously, so this is
tracked in the current evaluation context and is called
the parent subject. Since the subject will default to the
current document if it hasn't been set explicitly, then a
predicate/object combination is always enough to generate one or more
triples.

The attributes for setting a predicate are @rel, @rev and @property, whilst the attributes for setting an object
are @resource, @href, @content,
and @src. @typeof is unique in that it sets *both* a predicate and an object at the same time (and also a subject when it
appears in the absence of other attributes that would set a subject).
Inline content might also set an object, if @content is not
present, but @property is present.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> There are many examples in this section. The examples are
> all written using XHTML+RDFa. However, the explanations are relevant
> regardless of the Host Language.

### 8.1 Changing the Evaluation Context

#### 8.1.1 Setting the current subject

When triples are created they will always be in relation to a
subject resource which is provided either by new subject (if there are rules on the current element that have set a subject)
or parent subject, as passed in via the evaluation context. This section looks at the specific ways in which
these values are set. Note that it doesn't matter how the subject is
set, so in this section we use the idea of the *current
subject* which may be *either* new subject or parent subject.

##### 8.1.1.1 The current document

When parsing begins, the current subject will be
the IRI of the document being parsed, or a value as set by a Host
Language-provided mechanism (e.g., the `base` element
in (X)HTML). This means that by default any metadata found in the
document will concern the document itself:
> **Example:**
>
> > **Example:**
> >
> > Example 47
>
> ```
> <html xmlns="http://www.w3.org/1999/xhtml">
>   <head>
>     <title>Jo's Friends and Family Blog</title>
>     <link rel="foaf:primaryTopic" href="#bbq" />
>     <meta property="dc:creator" content="Jo" />
>   </head>
>   <body>
>     ...
>   </body>
> </html>
> ```

This would generate the following triples:
> **Example:**
>
> > **Example:**
> >
> > Example 48
>
> ```
> <> foaf:primaryTopic <#bbq> .
> <> dc:creator "Jo" .
> ```

It is possible for the data to appear elsewhere in the document:
> **Example:**
>
> > **Example:**
> >
> > Example 49
>
> ```
> <html xmlns="http://www.w3.org/1999/xhtml">
>   <head>
>     <title>Jo's Blog</title>
>   </head>
>   <body>
>     <h1><span property="dc:creator">Jo</span>'s blog</h1>
>     <p>
>       Welcome to my blog.
>     </p>
>   </body>
> </html>
> ```

which would still generate the triple:
> **Example:**
>
> > **Example:**
> >
> > Example 50
>
> ```
> <> dc:creator "Jo" .
> ```

In (X)HTML the value of `base` may change the initial
value of current subject:
> **Example:**
>
> > **Example:**
> >
> > Example 51
>
> ```
> <html xmlns="http://www.w3.org/1999/xhtml">
>   <head>
>     <base href="http://www.example.org/jo/blog" />
>     <title>Jo's Friends and Family Blog</title>
>     <link rel="foaf:primaryTopic" href="#bbq" />
>     <meta property="dc:creator" content="Jo" />
>   </head>
>   <body>
>     ...
>   </body>
> </html>
> ```

An RDFa Processor should now generate the following triples,
regardless of the IRI from which the document is served:
> **Example:**
>
> > **Example:**
> >
> > Example 52
>
> ```
> <http://www.example.org/jo/blog> foaf:primaryTopic <http://www.example.org//jo/blog#bbq> .
> <http://www.example.org/jo/blog> dc:creator "Jo" .
> ```

##### 8.1.1.2 Using @about

As processing progresses, any @about attributes will
change the current subject. The value of @about is an IRI or a CURIE. If it is a relative IRI then it needs to be
resolved against the current base value. To
illustrate how this affects the statements, note in this markup
how the properties inside the (X)HTML `body` element
become part of a new calendar event object, rather than referring
to the document as they do in the head of the document:
> **Example:**
>
> > **Example:**
> >
> > Example 53
>
> ```
> <html xmlns="http://www.w3.org/1999/xhtml"
>       prefix="cal: http://www.w3.org/2002/12/cal/ical#">
>   <head>
>     <title>Jo's Friends and Family Blog</title>
>     <link rel="foaf:primaryTopic" href="#bbq" />
>     <meta property="dc:creator" content="Jo" />
>   </head>
>   <body>
>     <p about="#bbq" typeof="cal:Vevent">
>       I'm holding
>       <span property="cal:summary">
>         one last summer barbecue
>       </span>,
>       on
>       <span property="cal:dtstart" content="2015-09-16T16:00:00-05:00"
>             datatype="xsd:dateTime">
>         September 16th at 4pm
>       </span>.
>     </p>
>   </body>
> </html>
> ```

With this markup an RDFa Processor will generate the following
triples:
> **Example:**
>
> > **Example:**
> >
> > Example 54
>
> ```
> <> foaf:primaryTopic <#bbq> .
> <> dc:creator "Jo" .
> <#bbq> rdf:type cal:Vevent .
> <#bbq> cal:summary "one last summer barbecue" .
> <#bbq> cal:dtstart "2015-09-16T16:00:00-05:00"^^xsd:dateTime .
> ```

Other kinds of resources can be used to set the current subject, not just references to web-pages. Although not
advised, email addresses might be used to represent a person:
> **Example:**
>
> > **Example:**
> >
> > Example 55
>
> ```
> John knows
> <a about="mailto:john@example.org"
>   rel="foaf:knows" href="mailto:sue@example.org">Sue</a>.
>
> Sue knows
> <a about="mailto:sue@example.org"
>   rel="foaf:knows" href="mailto:jim@example.org">Jim</a>.
> ```

This should generate the following triples:
> **Example:**
>
> > **Example:**
> >
> > Example 56
>
> ```
> <mailto:john@example.org> foaf:knows <mailto:sue@example.org> .
> <mailto:sue@example.org> foaf:knows <mailto:jim@example.org> .
> ```

Similarly, authors may make statements about images:
> **Example:**
>
> > **Example:**
> >
> > Example 57
>
> ```
> <div about="photo1.jpg">
>   this photo was taken by
>   <span property="dc:creator">Mark Birbeck</span>
> </div>
> ```

which should generate the following triple:
> **Example:**
>
> > **Example:**
> >
> > Example 58
>
> ```
> <photo1.jpg> dc:creator "Mark Birbeck" .
> ```

##### 8.1.1.3 Typing resources with @typeof

@typeof defines typing triples. @typeof works differently to other ways of setting a predicate since the
predicate is always `rdf:type`, which means that the
processor only requires the value of the type. The
question is: which resource gets these typing information?

If the element has an @about, which creates a new
context for statements, the typing relationships are defined on
that resource. For example, the following:
> **Example:**
>
> > **Example:**
> >
> > Example 59
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein" typeof="foaf:Person">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="foaf:givenName">Albert</span>
> </div>
> ```

also creates the triple:
> **Example:**
>
> > **Example:**
> >
> > Example 60
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein> rdf:type foaf:Person .
> ```

The @about attribute is the main source for typing;
if it is present on an element, it determines the effect of @typeof with the highest priority. If @about is *not* present, but the element is used only to define possible subject
resources via, e.g., @resource (i.e., there is *no* @rel, @rev, or @property present), then that resource is used for the typed resource, just
like @about.

If an @rel is present (and still no @about)
then the explicit object of the triples defined by @rel is typed. For example, in the case of:
> **Example:**
>
> > **Example:**
> >
> > Example 61
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <div rel="dbp:birthPlace"
>       resource="http://dbpedia.org/resource/German_Empire"
>       typeof="http://schema.org/Country">
>   </div>
> </div>
> ```

the generated triples also include:
> **Example:**
>
> > **Example:**
> >
> > Example 62
>
> ```
> <http://dbpedia.org/resource/German_Empire> rdf:type <http://schema.org/Country> .
> ```

Finally, @typeof also has the additional feature of
creating a new context for statements, *in case no other
attributes define any*. This involves generating a new bnode (see below for more about bnodes). For example, an author may wish
to create markup for a person using the FOAF vocabulary, but
without having a clear identifier for the item:
> **Example:**
>
> > **Example:**
> >
> > Example 63
>
> ```
> <div typeof="foaf:Person">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="foaf:givenName">Albert</span>
> </div>
> ```

This markup would cause a bnode to be created
which has a 'type' of `foaf:Person`, as well as name
and given name properties:
> **Example:**
>
> > **Example:**
> >
> > Example 64
>
> ```
> _:a rdf:type foaf:Person .
> _:a foaf:name "Albert Einstein" .
> _:a foaf:givenName "Albert" .
> ```

This usage of “isolated” @typeof may be viewed as a shorthand for:
> **Example:**
>
> > **Example:**
> >
> > Example 65
>
> ```
> <div resource="_:a" typeof="foaf:Person">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="foaf:givenName">Albert</span>
> </div>
> ```

Similarly,
> **Example:**
>
> > **Example:**
> >
> > Example 66
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <div rel="dbp:birthPlace" typeof="http://schema.org/Country">
>     <span property="dbp:conventionalLongName">the German Empire</span>
>   </div>
> </div>
> ```

generates:
> **Example:**
>
> > **Example:**
> >
> > Example 67
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein"> dbp:birthPlace _:b .
> _:b dbp:conventionalLongName "the German Empire" .
> ```

A bnode is simply a unique
identifier that is only available to the processor, not to any
external software. By generating values internally, the processor
is able to keep track of properties for `_:a` as being
distinct from `_:b`. But by not exposing these values
to any external software, it is possible to have complete control
over the identifier, as well as preventing further statements
being made about the item.

###### 8.1.1.3.1 Chaining with @property and @typeof

As emphasized in the section on chaining (§7.3),
one of the main differences between @property and @rel (or @rev) is that the former does not induce
chaining. The *only* exception to this rule is when @typeof is also present on the element. In that case the effect of @property is identical to @rel. For example, the previous
example could have been written as:
> **Example:**
>
> > **Example:**
> >
> > Example 68
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <div property="dbp:birthPlace" typeof="http://schema.org/Country">
>     <span property="dbp:conventionalLongName">the German Empire</span>
>   </div>
> </div>
> ```

generating the same triples as before. Here again, a @typeof without
an @about or a @resource can be regarded as a shorthand
for an additional @resource attribute referring to the identifier of a fresh bnode.

##### 8.1.1.4 Determining the subject with neither @about nor @typeof

As described in the previous two sections, @about will always take precedence and mark a new subject, but if no @about value is available then @typeof will do the same job,
although using an implied identifier, i.e., a bnode.

But if neither @about or @typeof are
present, there are a number of ways that the subject could be
arrived at. One of these is to 'inherit' the subject from the
containing statement, with the value to be inherited set either
explicitly, or implicitly.

###### 8.1.1.4.1 Inheriting subject from @resource

The most usual way that an inherited subject might get set
would be when the parent statement has an object that is a
resource. Returning to the earlier example, in which the long
name for the German_Empire was added, the following markup was
used:
> **Example:**
>
> > **Example:**
> >
> > Example 69
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div rel="dbp:birthPlace" resource="http://dbpedia.org/resource/German_Empire" />
>   <span about="http://dbpedia.org/resource/German_Empire"
>     property="dbp:conventionalLongName">the German Empire</span>
> </div>
> ```

In an earlier illustration the subject and object for the
German Empire were connected by removing the @resource,
relying on the @about to set the object:
> **Example:**
>
> > **Example:**
> >
> > Example 70
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div rel="dbp:birthPlace">
>     <span about="http://dbpedia.org/resource/German_Empire"
>       property="dbp:conventionalLongName">the German Empire</span>
>   </div>
> </div>
> ```

but it is also possible for authors to achieve the same effect
by removing the @about and leaving the @resource:
> **Example:**
>
> > **Example:**
> >
> > Example 71
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div rel="dbp:birthPlace" resource="http://dbpedia.org/resource/German_Empire">
>     <span property="dbp:conventionalLongName">the German Empire</span>
>   </div>
> </div>
> ```

In this situation, all statements that are 'contained' by the
object resource representing the German Empire (the value in @resource)
will have the same subject, making it easy for authors to add
additional statements:
> **Example:**
>
> > **Example:**
> >
> > Example 72
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div rel="dbp:birthPlace" resource="http://dbpedia.org/resource/German_Empire">
>     <span property="dbp:conventionalLongName">the German Empire</span>
>     <span rel="dbp-owl:capital" resource="http://dbpedia.org/resource/Berlin" />
>   </div>
> </div>
> ```

Looking at the triples that an RDFa Processor would generate,
we can see that we actually have two groups of statements; the
first group is set to refer to the @about that
contains them:
> **Example:**
>
> > **Example:**
> >
> > Example 73
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein> foaf:name "Albert Einstein" .
> <http://dbpedia.org/resource/Albert_Einstein> dbp:dateOfBirth "1879-03-14"^^xsd:date .
> <http://dbpedia.org/resource/Albert_Einstein> dbp:birthPlace <http://dbpedia.org/resource/German_Empire> .
> ```

while the second group refers to the @resource that contains them:
> **Example:**
>
> > **Example:**
> >
> > Example 74
>
> ```
> <http://dbpedia.org/resource/German_Empire>
>   dbp:conventionalLongName "the German Empire" .
> <http://dbpedia.org/resource/German_Empire>
>   dbp-owl:capital <http://dbpedia.org/resource/Berlin> .
> ```

Note also that the same principle described here applies to @src and @href.

###### 8.1.1.4.2 Inheriting an anonymous subject

There will be occasions when the author wants to connect the
subject and object as shown above, but is not concerned to name
the resource that is common to the two statements (i.e., the
object of the first statement, which is the subject of the
second). For example, to indicate that Einstein was influenced
by Spinoza the following markup could well be used:
> **Example:**
>
> > **Example:**
> >
> > Example 75
>
> ```
> <div about="http://dbpedia.org/resource/Baruch_Spinoza" rel="dbp-owl:influenced">
>   <div about="http://dbpedia.org/resource/Albert_Einstein">
>     <span property="foaf:name">Albert Einstein</span>
>     <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   </div>
> </div>
> ```

An RDFa Processor will generate the following triples:
> **Example:**
>
> > **Example:**
> >
> > Example 76
>
> ```
> <http://dbpedia.org/resource/Baruch_Spinoza>
>   dbp-owl:influenced <http://dbpedia.org/resource/Albert_Einstein> .
> <http://dbpedia.org/resource/Albert_Einstein> foaf:name "Albert Einstein" .
> <http://dbpedia.org/resource/Albert_Einstein> dbp:dateOfBirth "1879-03-14"^^xsd:date .
> ```

However, an author could just as easily say that Spinoza
influenced *something by the name of Albert Einstein, that
was born on March 14th, 1879*:
> **Example:**
>
> > **Example:**
> >
> > Example 77
>
> ```
> <div about="http://dbpedia.org/resource/Baruch_Spinoza" rel="dbp-owl:influenced">
>   <div>
>     <span property="foaf:name">Albert Einstein</span>
>     <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   </div>
> </div>
> ```

In RDF terms, the item that 'represents' Einstein is *anonymous*,
since it has no IRI to identify it. However, the item is given
an automatically generated bnode, and it is onto
this identifier that all child statements are attached:

An RDFa Processor will generate the following triples:
> **Example:**
>
> > **Example:**
> >
> > Example 78
>
> ```
> <http://dbpedia.org/resource/Baruch_Spinoza> dbp-owl:influenced _:a .
> _:a foaf:name "Albert Einstein" .
> _:a dbp:dateOfBirth "1879-03-14"^^xsd:date .
> ```

Note that the `div` is superfluous, and an RDFa
Processor will create the intermediate object even if the
element is removed:
> **Example:**
>
> > **Example:**
> >
> > Example 79
>
> ```
> <div about="http://dbpedia.org/resource/Baruch_Spinoza" rel="dbp-owl:influenced">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
> </div>
> ```

An alternative pattern is to *keep* the `div` and move the @rel onto it:
> **Example:**
>
> > **Example:**
> >
> > Example 80
>
> ```
> <div about="http://dbpedia.org/resource/Baruch_Spinoza">
>   <div rel="dbp-owl:influenced">
>     <span property="foaf:name">Albert Einstein</span>
>     <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   </div>
> </div>
> ```

From the point of view of the markup, this latter layout is to
be preferred, since it draws attention to the 'hanging rel'. But
from the point of view of an RDFa Processor, all of these
permutations need to be supported.

### 8.2 Completing incomplete triples

When a new subject is calculated, it is also used to complete any
incomplete triples that are pending. This situation arises when the
author wants to 'chain' a number of statements together. For example,
an author could have a statement that Albert Einstein was born in the
German Empire:
> **Example:**
>
> > **Example:**
> >
> > Example 81
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div rel="dbp:birthPlace" resource="http://dbpedia.org/resource/German_Empire" />
> </div>
> ```

and then a further statement that the 'long name' for this country
is *the German Empire*:
> **Example:**
>
> > **Example:**
> >
> > Example 82
>
> ```
> <span about="http://dbpedia.org/resource/German_Empire"
>   property="dbp:conventionalLongName">the German Empire</span>
> ```

RDFa allows authors to insert this statement as a self-contained
unit into other contexts:
> **Example:**
>
> > **Example:**
> >
> > Example 83
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div rel="dbp:birthPlace" resource="http://dbpedia.org/resource/German_Empire" />
>   <span about="http://dbpedia.org/resource/German_Empire"
>     property="dbp:conventionalLongName">the German Empire</span>
> </div>
> ```

But it also allows authors to avoid unnecessary repetition and to
'normalize' out duplicate identifiers, in this case the one for the
German Empire:
> **Example:**
>
> > **Example:**
> >
> > Example 84
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div rel="dbp:birthPlace">
>     <span about="http://dbpedia.org/resource/German_Empire"
>       property="dbp:conventionalLongName">the German Empire</span>
>   </div>
> </div>
> ```

When this happens the @rel for 'birth place' is
regarded as a 'hanging rel' because it has not yet generated any
triples, but these 'incomplete triples' are completed by the @about that appears on the next line. The first step is therefore to store
the two parts of the triple that the RDFa Processor *does* have, but without an object:
> **Example:**
>
> > **Example:**
> >
> > Example 85
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein> dbp:birthPlace ? .
> ```

Then as processing continues, the RDFa Processor encounters the
subject of the statement about the long name for the German Empire,
and this is used in two ways. First it is used to complete the
'incomplete triple':
> **Example:**
>
> > **Example:**
> >
> > Example 86
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein>
>       dbp:birthPlace <http://dbpedia.org/resource/German_Empire> .
> ```

and second it is used to generate its own triple:
> **Example:**
>
> > **Example:**
> >
> > Example 87
>
> ```
> <http://dbpedia.org/resource/German_Empire>
>       dbp:conventionalLongName "the German Empire" .
> ```

Note that each occurrence of @about will complete any
incomplete triples. For example, to mark up the fact that Albert
Einstein had a residence both in the German Empire and Switzerland, an
author need only specify one @rel value that is then used
with multiple @about values:
> **Example:**
>
> > **Example:**
> >
> > Example 88
>
> ```
> <div about="http://dbpedia.org/resource/Albert_Einstein" rel="dbp-owl:residence">
>   <span about="http://dbpedia.org/resource/German_Empire" />
>   <span about="http://dbpedia.org/resource/Switzerland" />
> </div>
> ```

In this example there is one incomplete triple:
> **Example:**
>
> > **Example:**
> >
> > Example 89
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein> dbp-owl:residence ? .
> ```

When the processor meets each of the @about values,
this triple is completed, giving:
> **Example:**
>
> > **Example:**
> >
> > Example 90
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein>
>   dbp-owl:residence <http://dbpedia.org/resource/German_Empire> .
> <http://dbpedia.org/resource/Albert_Einstein>
>   dbp-owl:residence <http://dbpedia.org/resource/Switzerland> .
> ```

These examples show how @about completes triples, but
there are other situations that can have the same effect. For example,
when @typeof creates a new bnode (as
described above), that will be used to complete any 'incomplete
triples'. To indicate that Spinoza influenced both
Einstein and Schopenhauer, the following markup could be used:
> **Example:**
>
> > **Example:**
> >
> > Example 91
>
> ```
> <div about="http://dbpedia.org/resource/Baruch_Spinoza">
>   <div rel="dbp-owl:influenced">
>     <div typeof="foaf:Person">
>       <span property="foaf:name">Albert Einstein</span>
>       <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>     </div>
>     <div typeof="foaf:Person">
>       <span property="foaf:name">Arthur Schopenhauer</span>
>       <span property="dbp:dateOfBirth" datatype="xsd:date">1788-02-22</span>
>     </div>
>   </div>
> </div>
> ```

First the following incomplete triple is stored:
> **Example:**
>
> > **Example:**
> >
> > Example 92
>
> ```
> <http://dbpedia.org/resource/Baruch_Spinoza> dbp-owl:influenced ? .
> ```

Then when the RDFa Processor processes the two occurrences of @typeof,
each generates a bnode, which is used to both complete
the 'incomplete triple', and to set the subject for further
statements:
> **Example:**
>
> > **Example:**
> >
> > Example 93
>
> ```
> <http://dbpedia.org/resource/Baruch_Spinoza"> dbp-owl:influenced _:a .
> _:a rdf:type foaf:Person .
> _:a foaf:name "Albert Einstein" .
> _:a dbp:dateOfBirth "1879-03-14"^^xsd:date .
> <http://dbpedia.org/resource/Baruch_Spinoza"> dbp-owl:influenced _:b .
> _:b rdf:type foaf:Person .
> _:b foaf:name "Arthur Schopenhauer" .
> _:b dbp:dateOfBirth "1788-02-22"^^xsd:date .
> ```

Triples are also 'completed' if any one of @property, @rel or @rev are present. However, unlike the situation when @about or @typeof are present, all predicates are attached to
one bnode:
> **Example:**
>
> > **Example:**
> >
> > Example 94
>
> ```
> <div about="http://dbpedia.org/resource/Baruch_Spinoza" rel="dbp-owl:influenced">
>   <span property="foaf:name">Albert Einstein</span>
>   <span property="dbp:dateOfBirth" datatype="xsd:date">1879-03-14</span>
>   <div rel="dbp-owl:residence">
>     <span about="http://dbpedia.org/resource/German_Empire" />
>     <span about="http://dbpedia.org/resource/Switzerland" />
>   </div>
> </div>
> ```

This example has two 'hanging rels', and so two situations when
'incomplete triples' will be created. Processing would proceed as
follows; first an incomplete triple is stored:
> **Example:**
>
> > **Example:**
> >
> > Example 95
>
> ```
> <http://dbpedia.org/resource/Baruch_Spinoza> dbp-owl:influenced ? .
> ```

Next, the RDFa Processor processes the predicate values for `foaf:name`, `dbp:dateOfBirth` and `dbp-owl:residence`, but
note that only the first needs to 'complete' the 'hanging rel'. So
processing `foaf:name` generates two triples:
> **Example:**
>
> > **Example:**
> >
> > Example 96
>
> ```
> <http://dbpedia.org/resource/Baruch_Spinoza> dbp-owl:influenced _:a .
> _:a foaf:name "Albert Einstein" .
> ```

but processing `dbp:dateOfBirth` generates only one:
> **Example:**
>
> > **Example:**
> >
> > Example 97
>
> ```
> _:a dbp:dateOfBirth "1879-03-14"^^xsd:date .
> ```

Processing `dbp-owl:residence` also uses the same bnode,
but note that it also generates its own 'incomplete triple':
> **Example:**
>
> > **Example:**
> >
> > Example 98
>
> ```
> _:a dbp-owl:residence ? .
> ```

As before, the two occurrences of @about complete the
'incomplete triple', once each:
> **Example:**
>
> > **Example:**
> >
> > Example 99
>
> ```
> _:a dbp-owl:residence <http://dbpedia.org/resource/German_Empire> .
> _:a dbp-owl:residence <http://dbpedia.org/resource/Switzerland> .
> ```

The entire set of triples that an RDFa Processor should
generate is as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 100
>
> ```
> <http://dbpedia.org/resource/Baruch_Spinoza> dbp-owl:influenced _:a .
> _:a foaf:name "Albert Einstein" .
> _:a dbp:dateOfBirth "1879-03-14"^^xsd:date .
> _:a dbp-owl:residence <http://dbpedia.org/resource/German_Empire> .
> _:a dbp-owl:residence <http://dbpedia.org/resource/Switzerland> .
> ```

### 8.3 Object resolution

Although objects have been discussed in the previous sections, as
part of the explanation of subject resolution, chaining, evaluation
contexts, and so on, this section will look at objects in more detail.

There are two types of object, IRI resources and literals.

A literal object can be set by @content or the inline
text of element if @property to express a predicate. *Note that the use of @content prohibits the inclusion of
rich markup in your literal. If the inline content of an element
accurately represents the object, then documents should rely upon
that rather than duplicating that data using the @content.*

An *IRI resource* object can be set using one of @rel or @rev to express a predicate, and then *either* using one of @href, @resource or @src to provide an object resource explicitly, *or* using the
chaining techniques described above to obtain an object from a nested
subject, or from a bnode. *Alternatively*, the @property can also be used to define an IRI resource; this requires the presence of a @resource, @href, or @src *and* the
absence of @rel, @rev, @datatype,
or @content.

#### 8.3.1 Object resolution for the @property attribute

An *object literal* will be generated when @property is present and no resource attribute is present. @property provides the predicate, and the
following sections describe how the actual literal to be generated
is determined.

##### 8.3.1.1 Plain Literals

@content can be used to indicate a plain literal, as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 101
>
> ```
> <meta about="http://internet-apps.blogspot.com/"
>       property="dc:creator" content="Mark Birbeck" />
> ```

The plain literal can also be specified by using
the content of the element:
> **Example:**
>
> > **Example:**
> >
> > Example 102
>
> ```
> <span about="http://internet-apps.blogspot.com/"
>       property="dc:creator">Mark Birbeck</span>
> ```

Both of these examples give the following triple:
> **Example:**
>
> > **Example:**
> >
> > Example 103
>
> ```
> <http://internet-apps.blogspot.com/> dc:creator "Mark Birbeck" .
> ```

The value of @content is given precedence over any
element content, so the following would give exactly the same
triple as shown above:
> **Example:**
>
> > **Example:**
> >
> > Example 104
>
> ```
> <span about="http://internet-apps.blogspot.com/"
>       property="dc:creator" content="Mark Birbeck">John Doe</span>
> ```

###### 8.3.1.1.1 Language Tags

RDF allows plain literals to have a language tag,
as illustrated by the following example from [RDF11-TESTCASES]:
> **Example:**
>
> > **Example:**
> >
> > Example 105
>
> ```
> <http://example.org/node>
>   <http://example.org/property> "chat"@fr .
> ```

In RDFa the Host Language may provide a mechanism for setting
the language tag. In XHTML+RDFa [XHTML-RDFA], for example,
the XML language attribute @xml:lang or the attribute @lang is used to add
this information, whether the plain literal is designated by @content,
or by the inline text of the element:
> **Example:**
>
> > **Example:**
> >
> > Example 106
>
> ```
> <meta about="http://example.org/node"
>   property="ex:property" xml:lang="fr" content="chat" />
> ```

Note that the language value can be inherited as defined in
[XML10-4e], so the following syntax will give the same triple
as above:
> **Example:**
>
> > **Example:**
> >
> > Example 107
>
> ```
> <html xmlns="http://www.w3.org/1999/xhtml"
>       prefix="ex: http://www.example.com/ns/" xml:lang="fr">
>   <head>
>     <title xml:lang="en">Example</title>
>     <meta about="http://example.org/node"
>       property="ex:property" content="chat" />
>   </head>
>   ...
> </html>
> ```

##### 8.3.1.2 Typed Literals

Literals can be given a data type using @datatype.

This can be represented in RDFa as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 108
>
> ```
> <span property="cal:dtstart" content="2015-09-16T16:00:00-05:00"
>       datatype="xsd:dateTime">
>   September 16th at 4pm
> </span>.
> ```

The triple that this markup generates includes the datatype after
the literal:
> **Example:**
>
> > **Example:**
> >
> > Example 109
>
> ```
> <> cal:dtstart "2015-09-16T16:00:00-05:00"^^xsd:dateTime .
> ```

##### 8.3.1.3 *XML Literals*

XML documents cannot contain XML markup in their attributes,
which means it is not possible to represent XML within @content (the following would cause an XML parser to generate an error):
> **Example:**
>
> > **Example:**
> >
> > Example 110
>
> ```
> <head>
>   <meta property="dc:title"
>     content="E = mc<sup>2</sup>: The Most Urgent Problem of Our Time" />
> </head>
> ```

RDFa therefore supports the use of arbitrary markup to express XML
literals by using @datatype:
> **Example:**
>
> > **Example:**
> >
> > Example 111
>
> ```
> <h2 property="dc:title" datatype="rdf:XMLLiteral">
>   E = mc<sup>2</sup>: The Most Urgent Problem of Our Time
> </h2>
> ```

This would generate the following triple, with the XML preserved
in the literal:
> **Example:**
>
> > **Example:**
> >
> > Example 112
>
> ```
> <> dc:title "E = mc<sup>2</sup>: The Most Urgent Problem of Our Time"^^rdf:XMLLiteral .
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> This requires that an IRI mapping for the prefix `rdf` has been defined.

In the examples given here the `sup` element is
actually part of the meaning of the literal, but there will be
situations where the extra markup means nothing, and can therefore
be ignored. In this situation omitting the @datatype attribute or specifying an empty @datatype value can
be used to create a plain literal:
> **Example:**
>
> > **Example:**
> >
> > Example 113
>
> ```
> <p>You searched for <strong>Einstein</strong>:</p>
> <p about="http://dbpedia.org/resource/Albert_Einstein">
>   <span property="foaf:name" datatype="">Albert <strong>Einstein</strong></span>
>   (b. March 14, 1879, d. April 18, 1955) was a German-born theoretical physicist.
> </p>
> ```

Rendering of this page has highlighted the term the
user searched for. Setting @datatype to nothing
ensures that the data is interpreted as a plain literal, giving
the following triple:
> **Example:**
>
> > **Example:**
> >
> > Example 114
>
> ```
> <http://dbpedia.org/resource/Albert_Einstein> foaf:name "Albert Einstein" .
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The value of this XML Literal is the exclusive canonicalization
> [XML-EXC-C14N] of the RDFa element's value.

#### 8.3.2 IRI object resolution

Most of the rules governing the processing of objects that are
resources are to be found in the processing descriptions given
above, since they are important for establishing the subject. This
section aims to highlight general concepts, and anything that might
have been missed.

One or more *IRI object*s are needed when @rel or @rev is present. Each
attribute will cause triples to be generated when used with @href, @resource or @src, or with the subject
value of any nested statement if none of these attributes are
present.

If @rel or @rev is not present, and neither is @datatype or @content, a @property attribute
will cause triples to be generated when used with @href, @resource or @src.
(See also the section on @property and @typeof (§8.1.1.3.1) for an additional special case involving @property.)

@rel and @rev are essentially the
inverse of each other; whilst @rel establishes a
relationship between the current subject as subject,
and the current object resource as the object, @rev does the exact opposite, and uses the current object resource as the subject, and the current subject as the object.

##### 8.3.2.1 Using @resource to set the object

RDFa provides the @resource attribute as a way to
set the object of statements. This is particularly useful when
referring to resources that are not themselves navigable links:
> **Example:**
>
> > **Example:**
> >
> > Example 115
>
> ```
> <html xmlns="http://www.w3.org/1999/xhtml">
>   <head>
>     <title>On Crime and Punishment</title>
>     <base href="http://www.example.com/candp.xhtml" />
>   </head>
>   <body>
>     <blockquote about="#q1" rel="dc:source" resource="urn:ISBN:0140449132" >
>       <p id="q1">
>         Rodion Romanovitch! My dear friend! If you go on in this way
>         you will go mad, I am positive! Drink, pray, if only a few drops!
>       </p>
>     </blockquote>
>   </body>
> </html>
> ```

The `blockquote` element generates the following
triple:
> **Example:**
>
> > **Example:**
> >
> > Example 116
>
> ```
> <http://www.example.com/candp.xhtml#q1>
>   <http://purl.org/dc/terms/source> <urn:ISBN:0140449132> .
> ```

Note that, in the example above, @property could
have been used instead of @rel, yielding the same
triple.

##### 8.3.2.2 Using @href or @src to set the object

If no @resource is present, then @href or @src are next in priority order for setting the
object.

When a predicate has been expressed using @rel, the @href or @src on the RDFa statement's
element is used to identify the object with a IRI reference.
Their types are an IRI:
> **Example:**
>
> > **Example:**
> >
> > Example 117
>
> ```
> <link about="mailto:john@example.org"
>       rel="foaf:knows" href="mailto:sue@example.org" />
> ```

It's also possible to use both @rel and @rev at the same time on an element. This is particularly useful when
two things stand in two different relationships with each other,
for example when a picture is taken *by* Mark, but that
picture also *depicts* him:
> **Example:**
>
> > **Example:**
> >
> > Example 118
>
> ```
> <img about="http://www.blogger.com/profile/1109404"
>     src="photo1.jpg" rev="dc:creator" rel="foaf:img"/>
> ```

which then yields two triples:
> **Example:**
>
> > **Example:**
> >
> > Example 119
>
> ```
> <photo1.jpg>
>   dc:creator <http://www.blogger.com/profile/1109404> .
> <http://www.blogger.com/profile/1109404>
>   foaf:img <photo1.jpg> .
> ```

##### 8.3.2.3 Incomplete triples

When a triple predicate has been expressed using @rel or @rev, but no @href, @src,
or @resource exists on the same element, there is a
'hanging rel'. This causes the current subject and all possible
predicates (with an indicator of whether they are 'forwards, i.e., @rel values, or not, i.e., @rev values),
to be stored as 'incomplete triples' pending discovery of a
subject that could be used to 'complete' those triples.

This process is described in more detail in Completing 'Incomplete Triples' (§8.2).

### 8.4 List Generation

An RDF graph is a collection of triples. This also means that if the
graph contains two triples sharing the same subject and predicate:
> **Example:**
>
> > **Example:**
> >
> > Example 120
>
> ```
> <http://www.example.com> <http://www.example.com/predicate> "first object", "second object" ;
> ```

There is no way for an application to rely on the relative order of
the two triples when, for example, querying a database containing
these triples. For most of the applications and data sets this is not
a problem, but, in some cases, the order is important. A typical case
is publications: when a book or an article has several co-authors, the
order of the authors may be important.

RDF has a set of predefined predicates that have an agreed-upon
semantic of order. For example, the publication: "Semantic Annotation
and Retrieval, by Ben Adida, Mark Birbeck, and Ivan Herman" could be
described in RDF triples using these terms as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 121
>
> ```
> @prefix bibo:  <http://purl.org/ontology/bibo/> .
> @prefix dc:    <http://purl.org/dc/terms/> .
> @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> [ a bibo:Chapter ;
>   dc:title "Semantic Annotation and Retrieval" ;
>   dc:creator [
>     rdf:first <http://ben.adida.net/#me ;
>     rdf:rest [
>       rdf:first <http://twitter.com/markbirbeck> ;
>       rdf:rest [
>         rdf:first <http://www.ivan-herman.net/foaf#me> ;
>         rdf:rest rdf:nil .
>       ] .
>     ] .
>   ] .
> 	...
> ]
> ```

which conveys the notion of 'order' for the three authors.
Admittedly, this is not very readable. However, Turtle has a
syntactic shorthand for these structures:
> **Example:**
>
> > **Example:**
> >
> > Example 122
>
> ```
> @prefix bibo:  <http://purl.org/ontology/bibo/> .
> @prefix dc:    <http://purl.org/dc/terms/> .
> @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> [ a bibo:Chapter ;
>   dc:title "Semantic Annotation and Retrieval" ;
>   dc:creator
>   ( <http://ben.adida.net/#me>
>     <http://twitter.com/markbirbeck>
>     <http://www.ivan-herman.net/foaf#me>
>   ) .
>   ...
> ]
> ```

It would of course be possible to reproduce the same structure in
RDFa, using the RDF predicates `rdf:first`, `rdf:rest`,
as well as the special resource `rdf:nil`. However, to
make this easier, RDFa provides the @inlist. What this
attribute signals is that the object generated on that element should
be put on a list; the list is used with the common predicate
and subject. Here is how the previous structure could look in
RDFa:
> **Example:**
>
> > **Example:**
> >
> > Example 123
>
> ```
> <p prefix="bibo: http://purl.org/ontology/bibo/ dc: http://purl.org/dc/terms/" typeof="bibo:Chapter">
>   "<span property="dc:title">Semantic Annotation and Retrieval</span>" by
>    <a inlist="" property="dc:creator"
>                 href="http://ben.adida.net/#me">Ben Adida</a>,
>    <a inlist="" property="dc:creator"
>                 href="http://twitter.com/markbirbeck">Mark Birbeck</a>, and
>    <a inlist="" property="dc:creator"
>                 href="http://www.ivan-herman.net/foaf#me">Ivan Herman</a>.
> </p>
> ```

Note that the order in the list is determined by the document order.
(The value of the @inlist is not relevant, only its
presence is.)

Lists may also include IRIs and not only literals. For example, two
of the three co-authors could decide to publicise their FOAF address
in the authors’ list:
> **Example:**
>
> > **Example:**
> >
> > Example 124
>
> ```
> <p prefix="bibo: http://purl.org/ontology/bibo/ dc: http://purl.org/dc/terms/" typeof="bibo:Chapter">
>   "<span property="dc:title">Semantic Annotation and Retrieval</span>", by
>   <span inlist="" property="dc:creator" resource="http://ben.adida.net/#me">Ben Adida</span>,
>   <span inlist="" property="dc:creator">Mark Birbeck</span>, and
>   <span inlist="" property="dc:creator" resource="http://www.ivan-herman.net/foaf#me">Ivan Herman</span>.
> </p>
> ```

yielding:
> **Example:**
>
> > **Example:**
> >
> > Example 125
>
> ```
> @prefix bibo:  <http://purl.org/ontology/bibo/> .
> @prefix dc:    <http://purl.org/dc/terms/> .
> @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> [ a bibo:Chapter ;
>   dc:title "Semantic Annotation and Retrieval" ;
>   dc:creator ( <http://ben.adida.net/#me> "Mark Birbeck" <http://www.ivan-herman.net/foaf#me> ) .
>   ...
> ]
> ```

In the example above, @rel could have been used leading
exactly to the same triples:
> **Example:**
>
> > **Example:**
> >
> > Example 126
>
> ```
> <p prefix="bibo: http://purl.org/ontology/bibo/ dc: http://purl.org/dc/terms/" typeof="bibo:Chapter">
>   "<span property="dc:title">Semantic Annotation and Retrieval</span>", by
>   <span inlist="" rel="dc:creator" resource="http://ben.adida.net/#me">Ben Adida</span>,
>   <span inlist="" property="dc:creator">Mark Birbeck</span>, and
>   <span inlist="" rel="dc:creator" resource="http://www.ivan-herman.net/foaf#me">Ivan Herman</span>.
> </p>
> ```

§8.3.2.3 Incomplete triples can also be
used in conjunction with lists when all list elements are resources
and not literals. For example, the previous example, this time with all
three authors referring to their FOAF profile, could have been written
as:
> **Example:**
>
> > **Example:**
> >
> > Example 127
>
> ```
> <p prefix="bibo: http://purl.org/ontology/bibo/ dc: http://purl.org/dc/terms/" typeof="bibo:Chapter">
>   "<span property="dc:title">Semantic Annotation and Retrieval</span>", by
>    <span rel="dc:creator" inlist="">
>      <a href="http://ben.adida.net/#me">Ben Adida</a>,
>      <a href="http://internet-apps.blogspot.com/2008/03/my-profile.html#me">Mark Birbeck</a>, and
>      <a href="http://www.ivan-herman.net/foaf#me">Ivan Herman</a>.
>    </span>
>   </p>
> ```

Resulting in:
> **Example:**
>
> > **Example:**
> >
> > Example 128
>
> ```
> @prefix bibo:  <http://purl.org/ontology/bibo/> .
> @prefix dc:    <http://purl.org/dc/terms/> .
> @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> [ a bibo:Chapter ;
>   dc:title "Semantic Annotation and Retrieval" ;
>   dc:creator ( <http://ben.adida.net/#me>
>                <http://internet-apps.blogspot.com/2008/03/my-profile.html#me>
>                <http://www.ivan-herman.net/foaf#me> ) .
>   ...
> ]
> ```

Note that it is also possible to express an empty list,
without @inlist, using:
> **Example:**
>
> > **Example:**
> >
> > Example 129
>
> ```
> <span rel="prop" resource="rdf:nil"/>
> ```

## 9. RDFa Initial Contexts

RDFa permits Host Languages to define an initial context.
Such a context is a collection of terms, prefix mappings, and/or a default
vocabulary declaration. An initial context is either intrinsically
known to the parser, or it is loaded as external documents and
processed. These documents *MUST* be defined in an approved RDFa Host
Language (currently XML+RDFa, XHTML+RDFa [XHTML-RDFA], and HTML+RDFa [HTML-RDFA]). They *MAY* also be defined in other formats (e.g., RDF/XML
[RDF-SYNTAX-GRAMMAR], or Turtle [TURTLE]). When an initial
context document is processed, it is evaluated as follows:

1. Parse the content (according to the processing rules for that
   document type) and extract the triples into a collection associated
   with that IRI. Note: These triples *MUST NOT* be co-mingled with the
   triples being extracted from any other IRI.
2. For every subject with a pair of predicates that have the values `rdfa:prefix` and `rdfa:uri`, create a key-value mapping from the `rdfa:prefix` object literal (the key) to the `rdfa:uri` object literal
   (the value). Add this mapping to the list of IRI mappings of the initial evaluation context (§7.5), after
   transforming the 'prefix' component to lower-case.
3. For every subject with a pair of predicates that have the values `rdfa:term` and `rdfa:uri`, create a key-value mapping from the `rdfa:term` object literal (the key) to the `rdfa:uri` object literal
   (the value). Add this mapping to the term mappings of
   the initial evaluation context (§7.5).
4. For an extracted triple that has a predicate of `rdfa:vocabulary`,
   define the default vocabulary of the initial evaluation context (§7.5) to be the object literal of the `rdfa:vocabulary` predicate.

When an RDFa Initial Context is defined using an RDF serialization, it *MUST* use the vocabulary terms above to declare the components of the
context.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Caching of the relevant triples retrieved via this
> mechanism is *RECOMMENDED*. Embedding definitions for well known, stable
> RDFa Initial Contexts in the implementation is *RECOMMENDED*.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> - The object literal for the `rdfa:uri` predicate *MUST* be an absolute IRI.
> - The object literal for the `rdfa:term` predicate *MUST* match the production for term.
> - The
>   object literal for the `rdfa:prefix` predicate must match
>   the production for prefix.
> - The object literal
>   for the `rdfa:vocabulary` predicate *MUST* be an
>   absolute IRI.
> - If one of the objects is not a literal, does not match its associated
>   production, if there is more than one `rdfa:vocabulary` predicate, or if there are additional `rdfa:uri` or `rdfa:term` predicates sharing the same subject, an RDFa Processor *MUST NOT* create
>   the associated mapping.

## 10. RDFa Vocabulary Expansion

Since RDFa is based on RDF, the semantics of RDF vocabularies can be
used to gain more knowledge about data. Vocabularies, properties and
classes are identified by IRIs, which enables them to be discoverable.
RDF data published at the location of these IRIs can be retrieved, and
descriptions of the properties and classes using specified semantics can
be applied.

*RDFa Vocabulary Expansion* is an optional processing step which may be
added once the normal processing steps described in §7 Processing Model are complete. Vocabulary expansion relies on a very small
sub-set of OWL entailment [OWL2-OVERVIEW] to add triples to the output graph based on rules and property/class relationships described
in referenced vocabularies. Vocabulary expansion *MAY* be performed as
part of a larger RDF toolset including, for example, an OWL 2 RL
reasoner. Alternatively, using vocabulary data added to the output graph in processing step 2 of §7.5 Sequence,
expansion *MAY* also be done using a separate and dedicated (e.g., rule
based) reasoner after the output graph has been generated,
or as the last processing step by an RDFa processor.

It can be very useful to make generalized data available for
subsequent usage of RDFa-embedded data by expanding inferred statements
entailed by these semantics. This provides for existing vocabularies
that extend well-known vocabularies to have those properties added to
the output graph automatically. For example, the namespace document of
the Creative Commons vocabulary, i.e., `http://creativecommons.org/ns`,
defines `cc:license` to be a sub-property of `dc:license`.
By using the @vocab attribute, one can describe a licensing
information as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 130
>
> ```
> This document is licensed under the
> <a vocab="http://creativecommons.org/ns#"
>    rel="license"
>    href="http://creativecommons.org/licenses/by-nc-nd/3.0/">
>    Creative Commons By-NC-ND License
> </a>.
> ```

which results in the following output graph:
> **Example:**
>
> > **Example:**
> >
> > Example 131
>
> ```
> @prefix cc:    <http://creativecommons.org/ns#> .
> @prefix rdfa:  <http://www.w3.org/ns/rdfa#> .
> <> cc:license          <http://creativecommons.org/licenses/by-nc-nd/3.0/> ;
>    rdfa:usesVocabulary <http://creativecommons.org/ns#> .
> ```

After vocabulary expansion, the output graph contains:
> **Example:**
>
> > **Example:**
> >
> > Example 132
>
> ```
> @prefix cc:    <http://creativecommons.org/ns#> .
> @prefix rdfa:  <http://www.w3.org/ns/rdfa#> .
> @prefix dc:    <http://purl.org/dc/terms/> .
> <> cc:license          <http://creativecommons.org/licenses/by-nc-nd/3.0/>;
>    dc:license          <http://creativecommons.org/licenses/by-nc-nd/3.0/> ;
>    rdfa:usesVocabulary  <http://creativecommons.org/ns#> .
> ```

Other vocabularies, specifically intended to provide relations to
multiple vocabularies, could also be defined by publishers, allowing use
of terms in a single namespace which result in properties and/or classes
from other primary vocabularies being imported. This benefits publishers
as data is now more widely searchable and encourages the practice of
referencing well-known vocabularies.

### 10.1 Details of the RDFa Vocabulary Expansion

*This section is non-normative.*

Once the output graph is generated following the
processing steps defined in §7.5 Sequence,
processors *MAY* perform the following processing steps on the output
graph. It must do so only if the user of the processor explicitly asks
for it, as prescribed in §10.2 Vocabulary Expansion Control of RDFa Processors.

A *vocabulary graph* is created as follows:
Each object IRI in the output graph that has a subject the current
document (base) IRI and a predicate of `rdfa:usesVocabulary` is dereferenced. If the dereferencing yields the serialization of an RDF
graph, that serialization is parsed and the resulting graph is merged
with the vocabulary graph. (An RDFa processor capable of vocabulary
expansion *MUST* accept an RDF graph serialized in RDFa, and *SHOULD* accept other standard serialization formats of RDF such as RDF/XML
[RDF-SYNTAX-GRAMMAR] and Turtle [TURTLE].)
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Note that if, in the second step, a particular
> vocabulary is serialized in RDFa, that particular graph is not
> expected to undergo any vocabulary expansion on its own.

Vocabulary expansion is then performed as follows:

1. The processor operates on the merge of the default and vocabulary
   graphs using §10.1.1 RDFa Vocabulary Entailment.
2. Add the new triples inferred from the output graph using this entailment to the (expanded) output graph.
   The processor *SHOULD NOT* add the triples appearing in the vocabulary graph only.

The goal of the second step is to avoid adding
the "axioms", e.g., the sub-property definitions to the output graph.
Applications usually do not require any of this additional information.

#### 10.1.1 *RDFa Vocabulary Entailment*

For the purpose of vocabulary processing, RDFa used a very
restricted subset of the OWL vocabulary and is based on the RDF-Based
Semantics of OWL [OWL2-RDF-BASED-SEMANTICS]. The RDFa
Vocabulary Entailment uses the following terms:

- `rdf:type`
- `rdfs:subClassOf`
- `rdfs:subPropertyOf`
- `owl:equivalentClass`
- `owl:equivalentProperty`

> **Note:**
>
> > **Note:**
> >
> > Note
>
> RDFa Vocabulary Entailment considers only the entailment on individuals
> (i.e., not on the relationships that can be deduced on the
> properties or the classes themselves.)
> **Note:**
>
> > **Note:**
> >
> > Note
>
> While the formal definition of the RDFa Entailment
> refers to the general OWL 2 Semantics, practical implementations may
> rely on a subset of the OWL 2 RL Profile’s entailment expressed in
> rules ([section 4.3](https://www.w3.org/TR/2009/REC-owl2-profiles-20091027/#Reasoning_in_OWL_2_RL_and_RDF_Graphs_using_Rules) of [OWL2-PROFILES]). The
> relevant rules are, using the rule identifications in [section 4.3](https://www.w3.org/TR/2009/REC-owl2-profiles-20091027/#Reasoning_in_OWL_2_RL_and_RDF_Graphs_using_Rules) of [OWL2-PROFILES]): `prp-spo1`, `prp-eqp1`, `prp-eqp2`, `cax-sco`, `cax-eqc1`,
> and `cax-eqc2`.

The entailment described in this section is the *minimum* useful level for RDFa. Processors may, of course, choose to follow
more powerful entailment regimes, e.g., include full RDFS [RDF11-MT]
or OWL [OWL2-OVERVIEW] entailments. Using those entailments
applications may perform datatype validation by checking `rdfs:range` of a property, or use the advanced facilities offered by, e.g., OWL’s
property chains to interlink vocabularies further.

### 10.2 Vocabulary Expansion Control of RDFa Processors

Conforming RDFa processors are not required to provide vocabulary
expansion.

If an RDFa processor provides vocabulary expansion, it *MUST NOT* be
performed by default. Instead, the processor *MUST* provide an option, `vocab_expansion`,
which, when used, instructs the RDFa processor to perform a vocabulary
expansion before returning the output graph.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Although vocabulary expansion is described in terms of
> a vocabulary graph and OWL 2 entailment rules, processors
> are free to use any process which obtains equivalent results.

#### 10.2.1 Notes to RDFa Vocabulary Implementations and Publishing

*This section is non-normative.*

For RDFa Processors caching the relevant graphs retrieved via this
mechanism is *RECOMMENDED*. Caching is usually based on HTTP response
headers like expiration time, cache control, etc.

For publishers of vocabularies, the IRI for the vocabularies *SHOULD* be dereferenceable, and should return an RDF graph with the
vocabulary description. This vocabulary description *SHOULD* be
available encoded in RDFa, and *MAY* also be available in other RDF
serialization syntaxes (using content negotiation to choose among
the different formats). If possible, vocabulary descriptions *SHOULD* include subproperty and subclass statements linking the vocabulary
terms to other, well-known vocabularies. Finally, HTTP responses *SHOULD* include fields usable for cache control, e.g., expiration
date.

## A. CURIE Datatypes

In order to facilitate the use of CURIEs in markup languages, this
specification defines some additional datatypes in the XHTML datatype
space (`http://www.w3.org/1999/xhtml/datatypes/`). Markup
languages that want to import these definitions can find them in the
"datatypes" file for their schema grammar:

- [DTD xhtml-datatypes.mod](https://www.w3.org/MarkUp/DTD/xhtml-datatypes-1.mod)
- [XML Schema xhtml-datatypes.xsd](https://www.w3.org/MarkUp/SCHEMA/xhtml-datatypes-1.xsd)

Specifically, the following datatypes are defined:

*CURIE*

A single curie

*CURIEs*

A white space separated list of CURIEs

*CURIEorIRI*

A CURIE or an IRI

*CURIEorIRIs*

A white space separated list of CURIEorIRIs

*SafeCURIE*

A single safe_curie

*SafeCURIEorCURIEorIRI*

A single SafeCURIE or CURIEorIRI

*SafeCURIEorCURIEorIRIs*

A white space separated list of SafeCURIEorCURIEorIRIs.

*TERM*

A single term

*TERMorCURIEorAbsIRI*

A TERM or a CURIEorIRI

*TERMorCURIEorAbsIRIs*

A white space separated list of TERMorCURIEorAbsIRIs

### A.1 XML Schema Definition

*This section is non-normative.*

The following *informative* XML Schema definition for these
datatypes is included as an example:
> **Example:**
>
> > **Example:**
> >
> > Example 133
>
> ```
> <?xml version="1.0" encoding="UTF-8"?>
> <xs:schema
>  xmlns:xs="http://www.w3.org/2001/XMLSchema"
>  xmlns="http://www.w3.org/1999/xhtml/datatypes/"
>  xmlns:xh11d="http://www.w3.org/1999/xhtml/datatypes/"
>  targetNamespace="http://www.w3.org/1999/xhtml/datatypes/"
>  elementFormDefault="qualified"
> >
>     <xs:simpleType name="CURIE">
>         <xs:restriction base="xs:string">
>             <xs:pattern value="(([\i-[:]][\c-[:]]*)?:)?(/[^\s/][^\s]*|[^\s/][^\s]*|[^\s]?)" />
>             <xs:minLength value="1"/>
>         </xs:restriction>
>     </xs:simpleType>
>
>     <xs:simpleType name="CURIEs">
>         <xs:list itemType="xh11d:CURIE"/>
>     </xs:simpleType>
>
>     <xs:simpleType name="SafeCURIE">
>         <xs:restriction base="xs:string">
>             <xs:pattern value="\[(([\i-[:]][\c-[:]]*)?:)?(/[^\s/][^\s]*|[^\s/][^\s]*|[^\s]?)\]" />
>             <xs:minLength value="3"/>
>         </xs:restriction>
>     </xs:simpleType>
>
>     <xs:simpleType name="SafeCURIEs">
>         <xs:list itemType="xh11d:SafeCURIE"/>
>     </xs:simpleType>
>
>     <xs:simpleType name="TERM">
>       <xs:restriction base="xs:Name">
>         <xs:pattern value="[\i-[:]][/\c-[:]]*" />
>       </xs:restriction>
>     </xs:simpleType>
>
>
>     <xs:simpleType name="CURIEorIRI">
>         <xs:union memberTypes="xh11d:CURIE xsd:anyURI" />
>     </xs:simpleType>
>
>     <xs:simpleType name="CURIEorIRIs">
>         <xs:list itemType="xh11d:CURIEorIRI"/>
>     </xs:simpleType>
>
>     <xs:simpleType name="SafeCURIEorCURIEorIRI">
>         <xs:union memberTypes="xh11d:SafeCURIE xh11d:CURIE xsd:anyURI" />
>     </xs:simpleType>
>
>     <xs:simpleType name="SafeCURIEorCURIEorIRIs">
>         <xs:list itemType="xh11d:SafeCURIEorCURIEorIRI"/>
>     </xs:simpleType>
>
>     <xs:simpleType name='AbsIRI'>
>         <xs:restriction base='xs:string'>
>             <xs:pattern value="[\i-[:]][\c-[:]]+:.+" />
>         </xs:restriction>
>     </xs:simpleType>
>
>     <xs:simpleType name="TERMorCURIEorAbsIRI">
>         <xs:union memberTypes="xh11d:TERM xh11d:CURIE xh11d:AbsIRI" />
>     </xs:simpleType>
>
>     <xs:simpleType name="TERMorCURIEorAbsIRIs">
>         <xs:list itemType="xh11d:SafeCURIEorCURIEorAbsIRI"/>
>     </xs:simpleType>
> </xs:schema>
> ```

### A.2 XML DTD Definition

*This section is non-normative.*

The following *informative* XML DTD definition for these
datatypes is included as an example:
> **Example:**
>
> > **Example:**
> >
> > Example 134
>
> ```
> <!ENTITY % CURIE.datatype "CDATA" >
> <!ENTITY % CURIEs.datatype "CDATA" >
> <!ENTITY % CURIEorIRI.datatype "CDATA" >
> <!ENTITY % CURIEorIRIs.datatype "CDATA" >
> <!ENTITY % SafeCURIEorCURIEorIRI.datatype "CDATA" >
> <!ENTITY % SafeCURIEorCURIEorIRIs.datatype "CDATA" >
> <!ENTITY % TERMorCURIEorAbsIRI.datatype "CDATA" >
> <!ENTITY % TERMorCURIEorAbsIRIs.datatype "CDATA" >
> ```

## B. The RDFa Vocabulary

The RDFa Vocabulary has three roles: it contains the predicates to
define the terms and prefixes in initial context documents, it contains the classes and predicates for the messages that
a processor graph may contain and, finally, it contains
the predicate necessary for vocabulary processing. The IRI of the
vocabulary is `http://www.w3.org/ns/rdfa#`; the usual prefix
used in this document is `rdfa`.

This vocabulary specification is available in [XHTML+RDFa 1.1](https://www.w3.org/ns/rdfa.html), [Turtle](https://www.w3.org/ns/rdfa.ttl), and in [RDF/XML](https://www.w3.org/ns/rdfa.rdf) formats.

### B.1 Term and Prefix Assignments

The RDFa Vocabulary includes the following triples (shown here in
Turtle [TURTLE] format):
> **Example:**
>
> > **Example:**
> >
> > Example 135
>
> ```
> @prefix dc:      <http://purl.org/dc/terms/> .
> @prefix owl:     <http://www.w3.org/2002/07/owl#> .
> @prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix rdfa:    <http://www.w3.org/ns/rdfa#> .
> @prefix foaf:    <http://xmlns.com/foaf/0.1/> .
>
> <http://www.w3.org/ns/rdfa#> a owl:Ontology .
>
> rdfa:PrefixOrTermMapping a rdfs:Class, owl:Class ;
>     dc:description "The top level class for prefix or term mappings." .
>
> rdfa:PrefixMapping dc:description "The class for prefix mappings." .
>     rdfs:subClassOf rdfa:PrefixOrTermMapping .
>
> rdfa:TermMapping dc:description "The class for term mappings." .
>     rdfs:subClassOf rdfa:PrefixOrTermMapping .
>
> rdfa:prefix a rdf:Property, owl:DatatypeProperty ;
>      rdfs:domain rdfa:PrefixMapping ;
>      dc:description "Defines a prefix mapping for an IRI; the value is supposed to be a NMTOKEN." .
>
> rdfa:term a rdf:Property, owl:DatatypeProperty ;
>      rdfs:domain rdfa:TermMapping ;
>      dc:description "Defines a term mapping for an IRI; the value is supposed to be a NMTOKEN." .
>
> rdfa:uri a rdf:Property, owl:DatatypeProperty ;
>      rdfs:domain rdfa:PrefixOrTermMapping ;
>      dc:description """Defines the IRI for either a prefix or a term mapping;
>         the value is supposed to be an absolute IRI.""" .
>
> rdfa:vocabulary a rdf:Property, owl:DatatypeProperty ;
>      dc:description """Defines an IRI to be used as a default vocabulary;
>         the value is can be any string; for documentation purposes it is advised to use
>         the string ‘true’ or ‘True’.""" .
> ```

These predicates can be used to define the initial context for a given Host Language.

These predicates are used to 'pair' IRI strings and their usage in
the form of a prefix and/or a term as part of, for example, a blank
node. An example can be as follows:
> **Example:**
>
> > **Example:**
> >
> > Example 136
>
> ```
> [] rdfa:uri     "http://xmlns.com/foaf/0.1/name" ;
>    rdfa:prefix  "foaf" .
> ```

which defines a prefix for the FOAF IRI.

### B.2 Processor Graph Reporting

The Vocabulary includes the following term definitions (shown here in
Turtle [TURTLE] format):
> **Example:**
>
> > **Example:**
> >
> > Example 137
>
> ```
> @prefix dc:      <http://purl.org/dc/terms/> .
> @prefix owl:     <http://www.w3.org/2002/07/owl#> .
> @prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix rdfa:    <http://www.w3.org/ns/rdfa#> .
>
> rdfa:PGClass a rdfs:Class, owl:Class;
>     dc:description "The top level class of the hierarchy." .
>
> rdfa:Error dcterms:description "The class for all error conditions.";
>     rdfs:subClassOf rdfa:PGClass .
>
> rdfa:Warning dcterms:description "The class for all warnings.";
>     rdfs:subClassOf rdfa:PGClass .
>
> rdfa:Info dcterms:description "The class for all informations.";
>     rdfs:subClassOf rdfa:PGClass .
>
> rdfa:DocumentError dc:description "An error condition to be used when the document
>     fails to be fully processed as a result of non-conformant host language markup.";
>     rdfs:subClassOf rdfa:Error .
>
> rdfa:VocabReferenceError dc:description "A warning to be used
>     when the value of a @vocab attribute cannot be dereferenced, hence the vocabulary expansion
>     cannot be completed.";
>     rdfs:subClassOf rdfa:Warning .
>
> rdfa:UnresolvedTerm dc:description "A warning to be used when a Term fails to be resolved.";
>     rdfs:subClassOf rdfa:Warning .
>
> rdfa:UnresolvedCURIE dc:description "A warning to be used when a CURIE prefix
>     fails to be resolved.";
>     rdfs:subClassOf rdfa:Warning .
>
> rdfa:context a owl:ObjectProperty, rdf:Property;
>     dc:description "Provides extra context for the error, e.g., http response,
>     an XPointer/XPath information, or simply the IRI that created the error.";
>     rdfs:domain rdfa:PGClass .
> ```

### B.3 Term for vocabulary expansion

The Vocabulary includes the following term definitions (shown here in
Turtle [TURTLE] format):
> **Example:**
>
> > **Example:**
> >
> > Example 138
>
> ```
> @prefix dc:      <http://purl.org/dc/terms/> .
> @prefix owl:     <http://www.w3.org/2002/07/owl#> .
> @prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
> @prefix rdfa:    <http://www.w3.org/ns/rdfa#> .
>
> rdfa:usesVocabulary a owl:ObjectProperty, rdf:Property;
>     dc:description "Provides a relationship between the host document and a vocabulary
>     defined using the @vocab facility of RDFa1.1." .
> ```

## C. Changes

*This section is non-normative.*

### C.1 Major differences since the Last Published Recommentation

- References to the other RDFa 1.1 documents, as well as to RDF 1.1 documents, have been updated
- A minor clarification has been added to section 4.1. to the processors can return processor and output graphs

### C.2 Major differences with RDFa Syntax 1.0

This specification introduces a number of new features, and extends
the behavior of some features from the previous version. The
following summary may be helpful to RDFa Processor developers, but
is *not* meant to be comprehensive.

- Specific rules about XHTML have been moved into a companion
  specification: [XHTML-RDFA].
- Prefix mappings can now be declared using @prefix in addition to @xmlns. The usage of @xmlns has been deprecated.
- Prefix names are now required to be converted to lower-case when
  the mapping is defined. Prefixes are checked in a case-insensitive
  manner during CURIE expansion.
- You can now use an Absolute IRI everywhere you could previously
  only use a CURIE (e.g., in the value of @datatype).
- There is now a concept of a term. This concept has
  replaced the concept of a 'reserved word'. It is possible now to
  use a 'term' in most places where you could previously only use a
  CURIE.
- You can define a default prefix mapping (via @vocab)
  that will be used on undefined terms.
- When a triple would include an object literal, and there is no
  explicit datatype attribute, the object literal will now be a
  'plain literal'. In version 1.0 it would have been an
  'XMLLiteral'.
- The @inlist attribute can be used to instruct the
  processor to generate RDF lists with the resources rather than
  simple triples.
- The effect of @src is now identical to @href rather than @about like in version 1.0.

While this specification strives to be as backward compatible as
possible with [RDFA-SYNTAX], the changes above mean that there are
some circumstances where it is possible for different RDF triples to
be output for the same document when processed by an RDFa 1.0
processor vs. an RDFa 1.1 processor. In order to minimize these
differences, a document author can do the following:

- Use the XHTML+RDFa 1.0 document type as defined in
  [RDFA-SYNTAX].
- Place a @version attribute with the
  value `XHTML+RDFa 1.0` on the `html` element.
- If there are places in the document where an object literal *MUST* be an XMLLiteral, use `datatype='rdf:XMLLiteral'`.
- If there are places in the document where an object literal *MUST* be a plain literal, use `datatype=''`.
- If there are places in the document where @src is
  used, add an @about (unless already present) with the
  same IRI.

When producing XHTML+RDFa 1.1 documents, it is possible to reduce
the incompatibilities with RDFa 1.0 conforming processors by doing
the following:

- DO NOT use the @vocab feature.
- DO NOT rely upon host language defaults for IRI mappings.
- DO NOT use absolute IRIs in place of CURIEs.
- Use @xmlns AND @prefix when declaring prefix mappings.
- DO NOT use TERMs on @datatype, @property,
  or @typeof.
- When using TERMs in @rel and @rev,
  only use ones defined in [RDFA-SYNTAX].
- Place a version attribute with the
  value `XHTML+RDFa 1.0` on the `html` element.
- If there are places in the document where an object literal *MUST* be an XMLLiteral, use `datatype='rdf:XMLLiteral'`.
- If there are places in the document where an object literal *MUST* be a plain literal, use `datatype=''`.
- If there are places in the document where @src is
  used, add an @about (unless already present) with the
  same IRI.

## E. References

### E.1 Normative references

[HTML-RDFA]

Manu Sporny et al. [HTML+RDFa 1.1 - Second Edition](https://www.w3.org/TR/html-rdfa). 17 March 2015. W3C Recommendation. URL: [http://www.w3.org/TR/html-rdfa/](https://www.w3.org/TR/html-rdfa/)

[OWL2-OVERVIEW]

W3C OWL Working Group. [OWL 2 Web Ontology Language Document Overview (Second Edition)](https://www.w3.org/TR/owl2-overview/). 11 December 2012. W3C Recommendation. URL: [http://www.w3.org/TR/owl2-overview/](https://www.w3.org/TR/owl2-overview/)

[OWL2-PROFILES]

Boris Motik; Bernardo Cuenca Grau; Ian Horrocks; Zhe Wu; Achille Fokoue. [OWL 2 Web Ontology Language Profiles (Second Edition)](https://www.w3.org/TR/owl2-profiles/). 11 December 2012. W3C Recommendation. URL: [http://www.w3.org/TR/owl2-profiles/](https://www.w3.org/TR/owl2-profiles/)

[OWL2-RDF-BASED-SEMANTICS]

Michael Schneider. [OWL 2 Web Ontology Language RDF-Based Semantics (Second Edition)](https://www.w3.org/TR/owl2-rdf-based-semantics/). 11 December 2012. W3C Recommendation. URL: [http://www.w3.org/TR/owl2-rdf-based-semantics/](https://www.w3.org/TR/owl2-rdf-based-semantics/)

[RDF-SYNTAX-GRAMMAR]

Fabien Gandon; Guus Schreiber. [RDF 1.1 XML Syntax](https://www.w3.org/TR/rdf-syntax-grammar/). 25 February 2014. W3C Recommendation. URL: [http://www.w3.org/TR/rdf-syntax-grammar/](https://www.w3.org/TR/rdf-syntax-grammar/)

[RDF11-MT]

Patrick Hayes; Peter Patel-Schneider. [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/). 25 February 2014. W3C Recommendation. URL: [http://www.w3.org/TR/rdf11-mt/](https://www.w3.org/TR/rdf11-mt/)

[RFC2119]

S. Bradner. [Key words for use in RFCs to Indicate Requirement Levels](https://tools.ietf.org/html/rfc2119). March 1997. Best Current Practice. URL: <https://tools.ietf.org/html/rfc2119>

[RFC3987]

M. Duerst; M. Suignard. [Internationalized Resource Identifiers (IRIs)](https://tools.ietf.org/html/rfc3987). January 2005. Proposed Standard. URL: <https://tools.ietf.org/html/rfc3987>

[XHTML-RDFA]

Shane McCarron. [XHTML+RDFa 1.1 - Third Edition](https://www.w3.org/TR/xhtml-rdfa/). 17 March 2015. W3C Recommendation. URL: [http://www.w3.org/TR/xhtml-rdfa/](https://www.w3.org/TR/xhtml-rdfa)

[XML-NAMES]

Tim Bray; Dave Hollander; Andrew Layman; Richard Tobin; Henry Thompson et al. [Namespaces in XML 1.0 (Third Edition)](https://www.w3.org/TR/xml-names). 8 December 2009. W3C Recommendation. URL: [http://www.w3.org/TR/xml-names](https://www.w3.org/TR/xml-names)

[XML10-4e]

C. M. Sperberg-McQueen et al. [Extensible Markup Language (XML) 1.0 (Fourth Edition)](https://www.w3.org/TR/2006/REC-xml-20060816/). 16 August 2006. W3C Recommendation. URL: [http://www.w3.org/TR/2006/REC-xml-20060816/](https://www.w3.org/TR/2006/REC-xml-20060816/)

[XMLSCHEMA11-2]

David Peterson; Sandy Gao; Ashok Malhotra; Michael Sperberg-McQueen; Henry Thompson; Paul V. Biron et al. [W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/). 5 April 2012. W3C Recommendation. URL: [http://www.w3.org/TR/xmlschema11-2/](https://www.w3.org/TR/xmlschema11-2/)

### E.2 Informative references

[HTML401]

Dave Raggett; Arnaud Le Hors; Ian Jacobs. [HTML 4.01 Specification](https://www.w3.org/TR/html401). 24 December 1999. W3C Recommendation. URL: [http://www.w3.org/TR/html401](https://www.w3.org/TR/html401)

[MICROFORMATS]

[Microformats](http://microformats.org). URL: <http://microformats.org>

[QNAMES]

N. Walsh. [Using Qualified Names (QNames) as Identifiers in XML Content](https://www.w3.org/2001/tag/doc/qnameids-2004-03-17). 17 March, 2004. TAG Finding. URL: [http://www.w3.org/2001/tag/doc/qnameids-2004-03-17](https://www.w3.org/2001/tag/doc/qnameids-2004-03-17)

[RDF11-PRIMER]

Guus Schreiber; Yves Raimond. [RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/). 24 June 2014. W3C Note. URL: [http://www.w3.org/TR/rdf11-primer/](https://www.w3.org/TR/rdf11-primer/)

[RDF11-TESTCASES]

Gregg Kellogg; Markus Lanthaler. [RDF 1.1 Test Cases](https://www.w3.org/TR/rdf11-testcases/). 25 February 2014. W3C Note. URL: [http://www.w3.org/TR/rdf11-testcases/](https://www.w3.org/TR/rdf11-testcases/)

[RDFA-PRIMER]

Ben Adida; Ivan Herman; Manu Sporny; Mark Birbeck. [RDFa 1.1 Primer - Third Edition](https://www.w3.org/TR/rdfa-primer/). 17 March 2015. W3C Note. URL: [http://www.w3.org/TR/rdfa-primer/](https://www.w3.org/TR/rdfa-primer)

[RDFA-SYNTAX]

Ben Adida; Mark Birbeck; Shane McCarron; Steven Pemberton et al. [RDFa in XHTML: Syntax and Processing](https://www.w3.org/TR/2008/REC-rdfa-syntax-20081014). 14 October 2008. W3C Recommendation. URL: [http://www.w3.org/TR/2008/REC-rdfa-syntax-20081014](https://www.w3.org/TR/2008/REC-rdfa-syntax-20081014)

[RELAXNG-SCHEMA]

[Information technology -- Document Schema Definition Language (DSDL) -- Part 2: Regular-grammar-based validation -- RELAX NG](http://standards.iso.org/ittf/PubliclyAvailableStandards/c052348_ISO_IEC_19757-2_2008(E).zip). ISO/IEC 19757-2:2008. URL: <http://standards.iso.org/ittf/PubliclyAvailableStandards/c052348_ISO_IEC_19757-2_2008(E).zip>

[SAX]

D. Megginson, et al. [SAX: The Simple API for XML](http://www.megginson.com/downloads/SAX/). May 1998. URL: <http://www.megginson.com/downloads/SAX/>

[TURTLE]

Eric Prud'hommeaux; Gavin Carothers. [RDF 1.1 Turtle](https://www.w3.org/TR/turtle/). 25 February 2014. W3C Recommendation. URL: [http://www.w3.org/TR/turtle/](https://www.w3.org/TR/turtle/)

[WIDGETS-URI]

Marcos Caceres. [Widget URI scheme](https://www.w3.org/TR/widgets-uri/). 13 March 2012. W3C Note. URL: [http://www.w3.org/TR/widgets-uri/](https://www.w3.org/TR/widgets-uri/)

[XHTML11]

Shane McCarron; Masayasu Ishikawa. [XHTML™ 1.1 - Module-based XHTML - Second Edition](https://www.w3.org/TR/xhtml11/). 23 November 2010. W3C Recommendation. URL: [http://www.w3.org/TR/xhtml11/](https://www.w3.org/TR/xhtml11/)

[XML-EXC-C14N]

John Boyer; Donald Eastlake; Joseph Reagle. [Exclusive XML Canonicalization Version 1.0](https://www.w3.org/TR/xml-exc-c14n). 18 July 2002. W3C Recommendation. URL: [http://www.w3.org/TR/xml-exc-c14n](https://www.w3.org/TR/xml-exc-c14n)

[XML10]

Tim Bray; Jean Paoli; Michael Sperberg-McQueen; Eve Maler; François Yergeau et al. [Extensible Markup Language (XML) 1.0 (Fifth Edition)](https://www.w3.org/TR/xml). 26 November 2008. W3C Recommendation. URL: [http://www.w3.org/TR/xml](https://www.w3.org/TR/xml)

[XMLSCHEMA11-1]

Sandy Gao; Michael Sperberg-McQueen; Henry Thompson; Noah Mendelsohn; David Beech; Murray Maloney. [W3C XML Schema Definition Language (XSD) 1.1 Part 1: Structures](https://www.w3.org/TR/xmlschema11-1/). 5 April 2012. W3C Recommendation. URL: [http://www.w3.org/TR/xmlschema11-1/](https://www.w3.org/TR/xmlschema11-1/)
