---
title: "RDFa Lite 1.1 - Second Edition"
source: https://www.w3.org/TR/rdfa-lite/
family: web
status: W3C Recommendation
spec_date: 2015-03-17
fetched: 2026-11-02
---

# RDFa Lite 1.1 - Second Edition

> The minimal five-attribute subset of RDFa.

## Contents

- Abstract
- 1 Introduction
- 2 The Attributes
  - 2.1 vocab, typeof, and property
  - 2.2 resource
  - 2.3 prefix
- 3 Conformance
  - 3.1 Document Conformance
- 4 Change History Since the Last Published Recommentation
- A References
  - A.1 Normative references
  - A.2 Informative references

---

## Abstract

RDFa Lite is a minimal subset of RDFa, the Resource Description Framework in
attributes, consisting of a few attributes that may
be used to express machine-readable data in Web documents like HTML, SVG, and
XML. While it is not a complete solution for advanced data markup tasks, it
does work for most day-to-day needs and can be learned by most Web authors
in a day.

## 1. Introduction

*This section is non-normative.*

The full RDFa syntax [rdfa-core] provides a number of basic and advanced
features that enable authors to express fairly complex structured data,
such as relationships among people, places, and events in an HTML or
XML document. Some of these advanced features may make it difficult for
authors, who may not be experts in structured data, to use RDFa.
This lighter version of RDFa is a gentler introduction to the world of
structured data, intended for authors that want to express fairly simple
data in their web pages. The goal is to provide a minimal subset that is
easy to learn and will work for 80% of authors doing simple data markup.

## 2. The Attributes

*This section is non-normative.*

RDFa Lite consists of five simple attributes; `vocab`, `typeof`, `property`, `resource`, and `prefix`. RDFa 1.1 Lite is completely upwards compatible with the
full set of RDFa 1.1 attributes. This means that if an author finds that
RDFa Lite isn't powerful enough, transitioning to the full version of RDFa is
just a matter of adding the more powerful RDFa attributes into the existing
RDFa Lite markup.

### 2.1 vocab, typeof, and property

RDFa, like Microformats [microformats] and Microdata [microdata],
enables us to talk about *things* on the Web such that a machine can understand what we are saying.
Typically when we talk about a thing, we use a particular **vocabulary** to talk about it. So, if you wanted to talk about
People, the vocabulary that you would use would specify terms like *name* and *telephone number*. When we want to mark up things on
the Web, we need to do something very similar, which is specify which
vocabulary that we are going to be using. Here is a simple example that
specifies a vocabulary that we intend to use to markup things in the paragraph:
> **Example:**
>
> > **Example:**
> >
> > Example 1
>
> ```
> <p vocab="http://schema.org/">
>    My name is Manu Sporny and you can give me a ring via 1-800-555-0199.
> </p>
> ```

In this example we have specified that we are going to be using the **vocabulary** that can be found at `http://schema.org/`. This is a vocabulary that has been
released by major search engine companies to talk about common things on the
Web that Search Engines care about – things like People, Places, Reviews,
Recipes, and Events. Once we have specified the vocabulary, we need to specify
the **type of** the thing that we're talking about. In this
particular case we are talking about a Person, which can be marked up like so:
> **Example:**
>
> > **Example:**
> >
> > Example 2
>
> ```
> <p vocab="http://schema.org/" typeof="Person">
>    My name is Manu Sporny and you can give me a ring via 1-800-555-0199.
> </p>
> ```

Now all we need to do is specify which **properties** of that
person we want to point out to the search engine. In the following example, we
mark up the person's name, phone number and web page. Both text and URLs can
be marked up with RDFa Lite. In the following example, pay particular attention
to the types of data that are being pointed out to the search engine,
which are highlighted in blue:
> **Example:**
>
> > **Example:**
> >
> > Example 3
>
> ```
> <p vocab="http://schema.org/" typeof="Person">
>    My name is
>    <span property="name">Manu Sporny</span>
>    and you can give me a ring via
>    <span property="telephone">1-800-555-0199</span>
>    or visit
>    <a property="url" href="http://manu.sporny.org/">my homepage</a>.
> </p>
> ```

Now, when somebody types in “phone number for Manu Sporny” into a
search engine, the search engine can more reliably answer the question
directly, or point the person searching to a more relevant Web page.

### 2.2 resource

If you want Web authors to be able to talk *about* each thing on your
page, you need to create an identifier for each of these things. Just like we
create identifiers for parts of a page using the `id` attribute
in HTML, you can create identifiers for things described on a page using the `resource` attribute:
> **Example:**
>
> > **Example:**
> >
> > Example 4
>
> ```
> <p vocab="http://schema.org/" resource="#manu" typeof="Person">
>    My name is
>    <span property="name">Manu Sporny</span>
>    and you can give me a ring via
>    <span property="telephone">1-800-555-0199</span>.
>    <img property="image" src="http://manu.sporny.org/images/manu.png" />
> </p>
> ```

If we assume that the markup above can be found at `http://example.org/people`, then the identifier for the thing is
the address, plus the value in the `resource` attribute. Therefore,
the identifier for the thing on the page would be: `http://example.org/people#manu`. This identifier is also useful if
you want to talk about that same thing on another Web page. By identifying all
things on the Web using a unique Uniform Resource Locator (URL), we can start
building a Web of things. Companies building software for the Web can use this
Web of things to answer complex questions like: "What is Manu Sporny's phone
number and what does he look like?".

### 2.3 prefix

In some cases, a vocabulary may not have all of the terms an author needs when
describing their *thing*. The last feature in RDFa 1.1 Lite that some
authors might need is the ability to specify more than one vocabulary. For
example, if we are describing a Person and we need to specify that they have a
favorite animal, we could do something like the following:
> **Example:**
>
> > **Example:**
> >
> > Example 5
>
> ```
> <p vocab="http://schema.org/" prefix="ov: http://open.vocab.org/terms/" resource="#manu" typeof="Person">
>    My name is
>    <span property="name">Manu Sporny</span>
>    and you can give me a ring via
>    <span property="telephone">1-800-555-0199</span>.
>    <img property="image" src="http://manu.sporny.org/images/manu.png" />
>    My favorite animal is the <span property="ov:preferredAnimal">Liger</span>.
> </p>
> ```

The example assigns a short-hand prefix to the Open Vocabulary
(`ov`) and uses that prefix to specify the `preferredAnimal` vocabulary term. Since schema.org doesn't have
a clear way of expressing a favorite animal, the author instead depends on
this alternate vocabulary to get the job done.

RDFa 1.1 Lite also pre-defines a number of [useful and popular prefixes](https://www.w3.org/2011/rdfa-context/rdfa-1.1), such as `dc`, `foaf`, and `schema`. This ensures that even if authors forget to declare the
popular prefixes, that their structured data will continue to work. A full list
of pre-declared prefixes can be found in the [initial context document for RDFa 1.1](https://www.w3.org/2011/rdfa-context/rdfa-1.1).

If you would like to learn more about what is possible with RDFa Lite,
including an introduction to the data model, please read the section on
RDFa Lite in the RDFa Primer [rdfa-primer].

## 3. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples,
and notes in this specification are non-normative. Everything else in this specification is
normative.

The key words *MAY*, *MUST*, *MUST NOT*, and *SHOULD* are
to be interpreted as described in [RFC2119].

### 3.1 Document Conformance

In order for a document to be labeled as a conforming **RDFa Lite 1.1
document**:

- It *MUST* only require the facilities described as mandatory
  in its Host Language.
- It *MUST NOT* use any additional RDFa attributes other than `vocab`, `typeof`, `property`, `resource`, and `prefix`; it may also use `href` and `src`, when the Host Language authorizes
  the usage of those attributes.
  However, even if authorized by the Host Language, the usage of `rel` and `rev` *SHOULD* be restricted to non-RDFa usage patterns, as defined by the
  Host Language.
- All RDFa attributes *SHOULD* be used in a way that is conformant with
  [rdfa-core].
- In XML-based languages, a document *MAY* still be labeled as a conforming RDFa
  Lite 1.1 document as long as the usage of the `xmlns` attribute
  is not used to declare CURIE prefixes.

If additional non-RDFa Lite attributes are used from the RDFa Core 1.1
specification, the document *MUST* be referred to as a conforming **RDFa 1.1 document**. All conforming RDFa Lite 1.1 documents *MAY* be referred to as conforming RDFa 1.1 documents.

## 4. Change History Since the Last Published Recommentation

*This section is non-normative.*

2014-12-16: Two grammatical errors have been changed in the Status Section

2014-12-16: References to the other RDFa documents have been updated

2014-12-16: The style of the references have been updated to the latest `respec` style

## A. References

### A.1 Normative references

[RFC2119]

S. Bradner. [Key words for use in RFCs to Indicate Requirement Levels](https://tools.ietf.org/html/rfc2119). March 1997. Best Current Practice. URL: <https://tools.ietf.org/html/rfc2119>

[rdfa-core]

Ben Adida; Mark Birbeck; Shane McCarron; Ivan Herman et al. [RDFa Core 1.1 - Third Edition: Syntax and processing rules for embedding RDF through attributes](https://www.w3.org/TR/rdfa-core). 17 March 2015. W3C Recommendation. URL: [http://www.w3.org/TR/rdfa-core/](https://www.w3.org/TR/rdfa-core/)

### A.2 Informative references

[microdata]

Ian Hickson. [HTML Microdata](https://www.w3.org/TR/microdata/). 29 October 2013. W3C Note. URL: [http://www.w3.org/TR/microdata/](https://www.w3.org/TR/microdata/)

[microformats]

[Microformats](http://microformats.org). URL: <http://microformats.org>

[rdfa-primer]

Ben Adida; Ivan Herman; Manu Sporny; Mark Birbeck. [RDFa 1.1 Primer - Third Edition](https://www.w3.org/TR/rdfa-primer/). 17 March 2015. W3C Note. URL: [http://www.w3.org/TR/rdfa-primer/](https://www.w3.org/TR/rdfa-primer)
