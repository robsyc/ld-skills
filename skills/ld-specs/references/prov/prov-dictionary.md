---
title: "PROV-Dictionary: Modeling Provenance for Dictionary Data Structures"
source: https://www.w3.org/TR/prov-dictionary/
family: prov
spec_date: 2013-04-30
fetched: 2026-11-02
---

# PROV-Dictionary: Modeling Provenance for Dictionary Data Structures

> Modeling dictionaries/participating collections in PROV.

## Contents

- Abstract
- 1 Introduction
- 2 PROV Namespace
- 3 Conceptual Definition of Dictionary
  - 3.1 Dictionary Membership
  - 3.2 Dictionary Insertion
  - 3.3 Dictionary Removal
- 4 PROV-N Notation of Dictionary Concepts
  - 4.1 Dictionary and EmptyDictionary Expression
  - 4.2 Dictionary Membership
  - 4.3 Insertion
  - 4.4 Removal
  - 4.5 Other expressions
- 5 PROV-O Representation of Dictionary
  - 5.1 Overview
  - 5.2 Dictionary Classes
  - 5.2.1 Class: prov:Dictionary
  - 5.2.2 Class: prov:EmptyDictionary
  - 5.2.3 Class: prov:KeyEntityPair
  - 5.2.4 Class: prov:Insertion
  - 5.2.5 Class: prov:Removal
  - 5.3 Dictionary Properties
  - 5.3.1 Property: prov:derivedByInsertionFromop
  - 5.3.2 Property: prov:derivedByRemovalFromop
  - 5.3.3 Property: prov:dictionaryop
  - 5.3.4 Property: prov:insertedKeyEntityPairop
  - 5.3.5 Property: prov:hadDictionaryMemberop
  - 5.3.6 Property: prov:pairKeydp
  - 5.3.7 Property: prov:pairEntityop
  - 5.3.8 Property: prov:qualifiedInsertionop
  - 5.3.9 Property: prov:qualifiedRemovalop
  - 5.3.10 Property: prov:removedKeydp
- 6 PROV-XML Representation of Dictionary
  - 6.1 Dictionary
  - 6.2 Key-Entity Pair
  - 6.3 Dictionary Membership
  - 6.4 Insertion
  - 6.5 Removal
- 7 Constraints Associated with Dictionary
  - 7.1 Notation and Conventions
  - 7.2 Inferences
  - 7.3 Constraints
  - 7.4 Typing
- A Example
  - A.1 Data
  - A.2 Provenance
    - A.2.1 PROV-N
    - A.2.2 PROV-O
    - A.2.3 PROV-XML
- B Change Log
  - B.1 Change Log Since First Public Working Draft
- D References
  - D.1 Informative references

---

## Abstract

Provenance is information about entities, activities, and people
involved in producing a piece of data or thing, which can be used to
form assessments about its quality, reliability or trustworthiness. This document describes extensions to PROV to facilitate the modeling of provenance for dictionary data structures. [PROV-DM] specifies a [Collection](https://www.w3.org/TR/2013/REC-prov-dm-20130430/Overview.html#component6) as an entity that provides a structure to some constituents, which are themselves entities. However, some applications may need a mechanism to specify more structure to a Collection, in order to accurately describe its provenance.
Therefore, in this document, we introduce Dictionary, a specific type of Collection with a logical structure consisting of key-entity pairs.

The [PROV Document Overview](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/) describes the overall state of PROV, and should be read before other PROV documents.

## 1. Introduction

[Provenance](< http://www.w3.org/TR/2013/REC-prov-dm-20130430/>) is a record that describes the people, institutions, entities, and
activities involved in producing, influencing, or delivering a piece
of data or a thing. The specifications [PROV-O], [PROV-DM],
[PROV-N], and [PROV-XML] have respectively defined the PROV
ontology, the PROV conceptual model, the PROV notation, and the PROV
XML schema, allowing provenance descriptions to be expressed,
represented in various representations, and interchanged between systems across the Web.

[PROV-DM] specifies Collection as an entity that provides a structure to some constituents, which are themselves entities. However, some applications may need a mechanism to specify more structure to a Collection, in order to accurately describe its provenance.

Therefore, this document introduces a new concept, Dictionary, that has a logical structure consisting of key-entity pairs.

## 2. PROV Namespace

The PROV namespace URI is http://www.w3.org/ns/prov# and prefix prov.

All the concepts, reserved names, classes, properties, attributes introduced in this specification belong to the PROV namespace.

## 3. Conceptual Definition of Dictionary

In this section a specific type of [collection](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#component6), as specified in [PROV-DM], is introduced. This new type of collection, Dictionary, is specified as follows.

Conceptually, a dictionary has a logical structure consisting of key-entity pairs. This structure is often referred to as a *map*, and is a generic indexing mechanism that can abstract commonly used data structures, including associative lists, relational tables, ordered lists, and more.
This document provides a mechanism to assert the provenance for these types of data structures, in the most general way, as a collection of key-entity pairs, modified through insertions and deletions. Any more specialized structures can be modeled to some extent in terms of these key-entity pairs.
Here, we will discuss the provenance of dictionaries structured in terms of key-entity pairs. However, how this key-entity pair structure is translated to more specialized data structures, is beyond the scope of this document.

In this document, a dictionary is viewed as a snapshot of a data structure with key-entity pairs, following a sequence of state-changing insertion and removal operations. These operations result in new snapshots, each snapshot forming a distinct and identifiable dictionary entity. Thus, when the structure of a dictionary changes (through insertions or removals), a new dictionary entity is defined, whereas the older dictionary entity remains the same. The concepts defined in this document can be used to specify the differences between these dictionary entities.

Following the [definition of prov:Collection](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-collection), PROV-Dictionary defines the following types related to dictionaries:

- prov:Dictionary is a subtype of prov:Collection. It denotes an entity of type dictionary, i.e. an entity that can participate in relations that involve dictionaries and their member entities;
- prov:EmptyDictionary is a subtype of both prov:EmptyCollection and prov:Dictionary. It denotes an empty dictionary.

Note that the complete content of a dictionary is unknown unless it can be traced back to an empty dictionary through a series of insertions and removals. If an asserter wants to explicitly state that a dictionary is empty, it is recommended that the prov:type prov:EmptyDictionary is used.

> **Example:**
>
> > **Example:**
> >
> > Example 1 ◊
>
> ```
> entity(d0, [prov:type='prov:EmptyDictionary' ])  // d0 is an empty dictionary
> entity(d1, [prov:type='prov:Dictionary'  ])      // d1 is a dictionary, with (so far) unknown content
> ```

### 3.1 Dictionary Membership

Similar to the [collection membership](< http://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-membership>) relation, the **dictionary membership** allows stating the members of a Dictionary. However, it provides additional structure.
Note that §3.1 Dictionary Membership implies [collection membership](< http://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-membership>), but not vice versa. This implication is formalized in Inference D1.

A *dictionary membership* ◊ relation, written prov:hadDictionaryMember(d, e_1, key_1), has:

- dictionary: an identifier (d) for the dictionary whose members are asserted;
- entity: an entity e_1 that is associated with the key and is a member of the dictionary;
- key: a key key_1 that is associated with the specified entity. key_1 is a [value](< http://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-value>) ;

Keys cannot be repeated in the same dictionary. However, a dictionary can contain the same entity more than once, as long as it is associated with different keys.

Note that the [collection membership](< http://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-membership>) relation, written hadMember(c, e), can be used when c has prov:type = 'prov:Collection' or prov:type = 'prov:Dictionary'. However, the §3.1 Dictionary Membership, written hadDictionaryMember(d, e, "k"), can only be used when d has prov:type = 'prov:Dictionary'.
> **Example:**
>
> > **Example:**
> >
> > Example 2 ◊
>
> ```
> entity(d, [prov:type='prov:Dictionary' ])    // d is a dictionary, with (so far) unknown content
>
> entity(e1)
> entity(e2)
>
> prov:hadDictionaryMember(d, e1, "k1")
> prov:hadDictionaryMember(d, e2, "k2")
> ```
>
> From these descriptions, we conclude:
>
> - d had the following key-entity pairs as members: ("k1", e1), ("k2", e2), and may have contained others.
> Thus, the membership of d is only partially known, unless it was derived through insertions and removals from an empty dictionary (See Completeness constraints).

### 3.2 Dictionary Insertion

An *Insertion* ◊ relation, written prov:derivedByInsertionFrom(id; d2, d1, {(key_1, e_1), ..., (key_n, e_n)}, attrs), has:

- id: an *OPTIONAL* identifier identifying the relation;
- after: an identifier (d2) for the dictionary *after* insertion;
- before: an identifier (d1) for the dictionary *before* insertion;
- key-entity-set: all inserted key-entity pairs (key_1, e_1), ..., (key_n, e_n). Here, each key_i is a [value](< http://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-value>), and e_i is an identifier for the entity that has been inserted with the key;
  each key_i is expected to be unique for the key-entity-set, as formalized in Inference D3;
- attributes: an *OPTIONAL* set (attrs) of attribute-value pairs representing additional information about this relation.

An Insertion relation prov:derivedByInsertionFrom(id; d2, d1, {(key_1, e_1), ..., (key_n, e_n)}) states that d2 is the dictionary
following the insertion of key-entity pairs (key_1, e_1), ..., (key_n, e_n) into dictionary d1. In other words, the set of key-entity pairs {(key_1, e_1), ...,(key_n, e_n)} is to be seen as the difference between d1 and d2.
Note that this key-entity-set is considered to be complete. This means that we assume that no unknown keys were inserted in or removed from a dictionary derived by an insertion relation. This is formalized in Inference D4.
> **Example:**
>
> > **Example:**
> >
> > Example 3 ◊
>
> ```
> entity(d0, [prov:type='prov:EmptyDictionary' ])    // d0 is an empty dictionary
> entity(e1)
> entity(e2)
> entity(e3)
> entity(d1, [prov:type='prov:Dictionary' ])
> entity(d2, [prov:type='prov:Dictionary' ])
>
> prov:derivedByInsertionFrom(d1, d0, {("k1", e1), ("k2", e2)})
> prov:derivedByInsertionFrom(d2, d1, {("k3", e3)}, [ dcterms:description ="A second insertion" ])    //an insertion with optional attribute dcterms:description
> ```
>
> From this set of descriptions, we conclude:
>
> - d0 was the dictionary { }
> - d1 was the dictionary { ("k1", e1), ("k2", e2) }
> - d2 was the dictionary { ("k1", e1), ("k2", e2), ("k3", e3) }

Futhermore, insertion provides an "update semantics" for the keys that are already present in a dictionary,
since a new pair replaces an existing pair with the same key in the new dictionary. This is illustrated by the following example.
> **Example:**
>
> > **Example:**
> >
> > Example 4 ◊
>
> ```
> entity(d0, [prov:type='prov:EmptyDictionary' ])    // d0 is an empty dictionary
> entity(e1)
> entity(e2)
> entity(e3)
> entity(d1, [prov:type='prov:Dictionary' ])
> entity(d2, [prov:type='prov:Dictionary' ])
>
> prov:derivedByInsertionFrom(d1, d0, {("k1", e1), ("k2", e2)})
> prov:derivedByInsertionFrom(d2, d1, {("k1", e3)})
> ```
>
> This is a case of *update* of e1 to e3 for the same key, "k1".
> From this set of descriptions, we conclude:
>
>
> - d0 was the dictionary { }
> - d1 was the dictionary { ("k1", e1), ("k2", e2) }
> - d2 was the dictionary { ("k1", e3), ("k2", e2) }

### 3.3 Dictionary Removal

A *Removal* ◊ relation, written prov:derivedByRemovalFrom(id; d2, d1, {key_1, ... key_n}, attrs), has:

- id: an *OPTIONAL* identifier identifying the relation;
- after: an identifier (d2) for the dictionary *after* the deletion;
- before: an identifier (d1) for the dictionary *before* the deletion;
- key-set: the set of deleted keys key_1, ..., key_n. Here, each key_i is a [value](< http://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-value>);
- attributes: an *OPTIONAL* set (attrs) of attribute-value pairs representing additional information about this relation.

A Removal relation prov:derivedByRemovalFrom(id; d2,d1, {key_1, ..., key_n}) states that d2 is the dictionary following the removal of the set of pairs corresponding to keys key_1...key_n from d1.
In other words, the key-set {key_1,...,key_n} is to be seen as the difference in keys and corresponding entities between d1 and d2. Note that this key-set is considered to be complete. This means that we assume that no unknown keys were inserted in or removed from a dictionary derived by a removal relation. This is formalized in Inference D5.
> **Example:**
>
> > **Example:**
> >
> > Example 5 ◊
>
> ```
> entity(d0, [prov:type="prov:EmptyDictionary"])    // d0 is an empty dictionary
> entity(e1)
> entity(e2)
> entity(e3)
> entity(d1, [prov:type="prov:Dictionary"])
> entity(d2, [prov:type="prov:Dictionary"])
> entity(d3, [prov:type="prov:Dictionary"])
> entity(d4, [prov:type="prov:Dictionary"])
>
> prov:derivedByInsertionFrom(d1, d0, {("k1", e1), ("k2",e2)})
> prov:derivedByInsertionFrom(d2, d1, {("k3", e3)})
> prov:derivedByRemovalFrom(d3, d2, {"k1", "k3"})
> prov:derivedByRemovalFrom(d4, d3, {"k1"})
> ```
>
> From this set of descriptions, we conclude:
>
> - d0 was the dictionary { }
> - d1 was the dictionary { ("k1", e1), ("k2", e2) }
> - d2 was the dictionary { ("k1", e1), ("k2", e2), ("k3", e3) }
> - d3 was the dictionary { ("k2", e2) }
> - d4 was the dictionary { ("k2", e2) }
>
> Note that there is no constraint stating that removed keys had to be present in the original dictionary. For example, "k1" was not present in d3, and thus its removal to obtain d4 did not change the contents of the dictionary.

## 4. PROV-N Notation of Dictionary Concepts

The notation used for dictionaries in this document extends the standard PROV-N according to the principles described in [the PROV-N extensibility chapter](https://www.w3.org/TR/2013/REC-prov-n-20130430/#extensibility).
The [[Grammar for PROV-Dictionary](https://www.w3.org/TR/prov-dictionary/prov-dictionary-grammar.txt)] is available for download.

### 4.1 Dictionary and EmptyDictionary Expression

PROV-Dictionary provides no dedicated syntax for Dictionary and EmptyDictionary. Dictionaries are declared in [the same way](https://www.w3.org/TR/2013/REC-prov-n-20130430/#expression-collection) as Collections. A Dictionary or an EmptyDictionary *MUST* be expressed as an `entityExpression` with attribute `prov:type='prov:Dictionary'`, or `prov:type='prov:EmptyDictionary'`, respectively.

> **Example:**
>
> > **Example:**
> >
> > Example 6 ◊
>
> The following two expressions are about a dictionary and an empty dictionary, respectively.
>
> ```
>   entity(ex:d1,   [ prov:type='prov:Dictionary' ])
>   entity(ex:d2,   [ prov:type='prov:EmptyDictionary' ])
> ```

### 4.2 Dictionary Membership

| [1] | `dictionaryMembershipExpression` | ::= | `"prov:hadDictionaryMember" "(" dIdentifier    ","    eIdentifier    ","   key    ")"   ` |
| --- | -------------------------------- | --- | ----------------------------------------------------------------------------------------- |

The following table summarizes how each constituent of a PROV-Dictionary Membership maps to a non-terminal.

| **Dictionary Membership**                                                       | **Non-Terminal** |
| ------------------------------------------------------------------------------- | ---------------- |
|                                                                                 |                  |
| dictionary (§3.1) | `dIdentifier`    |
| entity (§3.1)     | `eIdentifier`    |
| key (§3.1)        | `key`            |
> **Example:**
>
> > **Example:**
> >
> > Example 7 ◊
>
> In this example, d is a dictionary known to have e0 as member, and may have other members.
>
> ```
> entity(e0)
>
> entity(d, [prov:type='prov:Dictionary'  ])
> prov:hadDictionaryMember(d, e0, "k0")
> ```

### 4.3 Insertion

| [2] | `derivationByInsertionFromExpression` | ::= | `"prov:derivedByInsertionFrom" "("    (optionalIdentifier    ";")?    dIdentifier    ","    dIdentifier    "," "{"   keyEntityPairs    "}"    optionalAttributeValuePairs    ")"   ` |
| --- | ------------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

The following table summarizes how each constituent of a PROV-Dictionary Insertion maps to a non-terminal.

| **Insertion**                                                                        | **Non-Terminal**              |
| ------------------------------------------------------------------------------------ | ----------------------------- |
|                                                                                      |                               |
| id (§3.2)               | `optionalIdentifier`          |
| after (§3.2)            | `dIdentifier`                 |
| before (§3.2)           | `dIdentifier`                 |
| key-entity-pairs (§3.2) | `keyEntityPairs`              |
| attributes (§3.2)       | `optionalAttributeValuePairs` |
> **Example:**
>
> > **Example:**
> >
> > Example 8 ◊
>
> ```
>  prov:derivedByInsertionFrom(id; d1, d, {("k1", e1), ("k2", e2)}, [])
>
> ```
>
> Here id is the optional insertion identifier, d1 is the identifier for the dictionary after the insertion, d is the identifier for the dictionary before the insertion, {("k1", e1), ("k2", e2)} is the set of key-entity pairs that have been inserted in d,
> and [] is the optional (empty) set of attributes.
>
> The remaining examples show cases where some of the optionals are omitted.
>
> ```
>  prov:derivedByInsertionFrom(d1, d, {("k1", e1), ("k2", e2)})
>  prov:derivedByInsertionFrom(d1, d, {("k1", e1)})
>  prov:derivedByInsertionFrom(d1, d, {("k1", e1), ("k2", e2)}, [])
> ```

### 4.4 Removal

| [3] | `derivationByRemovalFromExpression` | ::= | `"prov:derivedByRemovalFrom" "("    (optionalIdentifier    ";")?    dIdentifier    ","    dIdentifier    "," "{"   keySet    "}"    optionalAttributeValuePairs    ")"   ` |
| --- | ----------------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The following table summarizes how each constituent of a PROV-Dictionary Removal maps to a non-terminal.

| **Removal**                                                                  | **Non-Terminal**              |
| ---------------------------------------------------------------------------- | ----------------------------- |
|                                                                              |                               |
| id (§3.3)         | `optionalIdentifier`          |
| after (§3.3)      | `dIdentifier`                 |
| before (§3.3)     | `dIdentifier`                 |
| key-set (§3.3)    | `keySet`                      |
| attributes (§3.3) | `optionalAttributeValuePairs` |
> **Example:**
>
> > **Example:**
> >
> > Example 9 ◊
>
> ```
>  prov:derivedByRemovalFrom(id; d3, d, {"k1", "k2"}, [])
>
> ```
>
> Here id is the optional removal identifier, d3 is the identifier for the collection after the removal, d is the identifier for the collection before the removal, {"k1", "k2"} is the set of keys that have been removed from d,
> and [] is the optional (empty) set of attributes.
>
> The remaining examples show cases where some of the optionals are omitted.
>
> ```
>    prov:derivedByRemovalFrom(d2, d, {"k1", "k2"})
>    prov:derivedByRemovalFrom(d2, d, {"k1"})
>    prov:derivedByRemovalFrom(d2, d, {"k1", "k2"}, [])
> ```

### 4.5 Other expressions

For the notation of dictionaries, we used some new non-terminals. We provide their production rules here.

| [4] | `dIdentifier`    | ::= | `identifier `                           |
| --- | ---------------- | --- | --------------------------------------- |
| [5] | `key`            | ::= | `literal `                              |
| [6] | `keyEntityPairs` | ::= | `keyEntityPair    ("," keyEntityPair)*` |
| [7] | `keyEntityPair`  | ::= | `"(" key     "," eIdentifier ")"`       |
| [8] | `keySet`         | ::= | `key    ("," key)*`                     |

## 5. PROV-O Representation of Dictionary

In this section, the ontological definition of `prov:Dictionary` is given, in order to extend [PROV-O] with dictionaries. For more information on the terminology, syntax and conventions used in this section, we refer to [PROV-O].

The classes and properties defined in this document are included in the default namespace of PROV.
Users of the ontology have the option of importing `<http://www.w3.org/ns/prov#>`, which includes all extensions, including PROV-Dictionary. Additionally, the [[OWL file for PROV-Dictionary](https://www.w3.org/ns/prov-dictionary)] is available for download.

A `prov:Dictionary` is a `prov:Entity` that acts as a container to some members,
which are themselves entities.
Specifically, a dictionary is composed of set of key-entity pairs, where a
literal key is used to identify a constituent entity within the dictionary.

> **Example:**
>
> > **Example:**
> >
> > > **Example:**
> > >
> > > Example 1
> >
> > ```
> > @prefix prov: <http://www.w3.org/ns/prov#> .
> > @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> > @prefix :     <http://example.org/> .
> >
> > :e1 a prov:Entity .
> > :e2 a prov:Entity .
> >
> > :d1 a prov:Dictionary;
> >     prov:hadDictionaryMember [
> >        a prov:KeyEntityPair;
> >        prov:pairKey   "k1"^^xsd:string;
> >        prov:pairEntity :e1
> >      ], [
> >        a prov:KeyEntityPair;
> >        prov:pairKey   "k2"^^xsd:string;
> >        prov:pairEntity :e2
> >      ];
> > .
> > ```

It is worth noting that `:d1` *MAY* also
have other members. If one wants to explicitly state that a dictionary has no members, that dictionary can be described as an instance of the
subclass `prov:EmptyDictionary` (§5.2.2).

To describe the provenance of a dictionary, PROV-Dictionary provides two
kinds of influence: `prov:qualifiedInsertion` is used to
describe that a dictionary was obtained from an existing dictionary by inserting (§3.2) a set of key-entity pairs. `prov:qualifiedRemoval` is used to specify
that a given dictionary was obtained from an existing dictionary by removing (§3.3) a set of key-entity pairs. The example below specifies that
the dictionary `:d1` was obtained from the empty dictionary `:d` by *inserting* the key-entity pairs `("k1", :e1)` and `("k2", :e2)`.
> **Example:**
>
> > **Example:**
> >
> > > **Example:**
> > >
> > > Example 2
> >
> > ```
> > @prefix prov: <http://www.w3.org/ns/prov#> .
> > @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> > @prefix :     <http://example.org/> .
> >
> > :e1 a prov:Entity .
> > :e2 a prov:Entity .
> >
> > :d  a prov:EmptyDictionary .
> >
> > :d1 a prov:Dictionary;
> >    prov:derivedByInsertionFrom :d;
> >    prov:qualifiedInsertion [
> >       a prov:Insertion;
> >       prov:dictionary :d;
> >       prov:insertedKeyEntityPair [
> >          a prov:KeyEntityPair;
> >          prov:pairKey   "k1"^^xsd:string;
> >          prov:pairEntity :e1;
> >       ], [
> >          a prov:KeyEntityPair;
> >          prov:pairKey   "k2"^^xsd:string;
> >          prov:pairEntity :e2;
> >       ];
> >    ];
> > .
> > ```

Similarly, the example below specifies that the dictionary `:d3` was obtained by *removing* the key-entity pairs associated with
the keys `"k1"` and `"k2"` from the dictionary `:d2`. Thus, `:d3` does not contain the
members `("k1", :e1)` and `("k2", 	:e2)` from `:d2`.
> **Example:**
>
> > **Example:**
> >
> > > **Example:**
> > >
> > > Example 3
> >
> > ```
> > @prefix prov: <http://www.w3.org/ns/prov#> .
> > @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> > @prefix :     <http://example.org/> .
> >
> > :d2 a prov:Dictionary .
> >
> > :d3 a prov:Dictionary;
> >    prov:derivedByRemovalFrom :d2;
> >    prov:qualifiedRemoval [
> >       a prov:Removal;
> >       prov:dictionary :d2;
> >       prov:removedKey    "k1"^^xsd:string,
> >                       "k3"^^xsd:string;
> >    ];
> > .
> > ```

### 5.1 Overview

These terms are used to describe the provenance of dictionaries.

- prov:Dictionary (§5.2.1)
- prov:EmptyDictionary (§5.2.2)
- prov:Insertion (§5.2.4)
- prov:KeyEntityPair (§5.2.3)
- prov:Removal (§5.2.5)
- prov:derivedByInsertionFrom (§5.3.1)
- prov:derivedByRemovalFrom (§5.3.2)
- prov:dictionary (§5.3.3)
- prov:insertedKeyEntityPair (§5.3.4)
- prov:hadDictionaryMember (§5.3.5)
- prov:pairKey (§5.3.6)
- prov:pairEntity (§5.3.7)
- prov:qualifiedInsertion (§5.3.8)
- prov:qualifiedRemoval (§5.3.9)
- prov:removedKey (§5.3.10)

### 5.2 Dictionary Classes

### Class: prov:Dictionary (§5.2.1)

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#Dictionary

A dictionary is an entity that provides a structure to some constituents, which are themselves entities. These constituents are said to be members of the dictionary.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix my:     <http://example.org/ontology#> .
> @prefix dcterms: <http://purl.org/dc/terms/> .
> @prefix :     <http://example.org/> .
>
> :seating_chart_2012
>    a prov:Dictionary, prov:Collection, prov:Entity, my:SeatingChart;
>    prov:derivedByInsertionFrom :seating_chart_2011;
>    dcterms:date "2012";
>    my:hasTotalStudents 45;
> .
> ```

This concept allows for the provenance of the dictionary, but also of its constituents to be expressed. Such a notion of dictionary corresponds to a wide variety of concrete data structures, such as a maps or associative arrays.

A given dictionary forms a given structure for its members. A different structure (obtained either by insertion or removal of members) constitutes a different dictionary.

is subclass of

[prov:Collection](https://www.w3.org/TR/2013/REC-prov-o-20130430/#Collection "http://www.w3.org/ns/prov#Collection")

described with properties

prov:hadDictionaryMember (§5.3.5)op prov:derivedByInsertionFrom (§5.3.1)op prov:qualifiedRemoval (§5.3.9)op prov:qualifiedInsertion (§5.3.8)op prov:derivedByRemovalFrom (§5.3.2)op

in range of

prov:derivedByInsertionFrom (§5.3.1)op prov:derivedByRemovalFrom (§5.3.2)op prov:dictionary (§5.3.3)op

has subclass

prov:EmptyDictionary (§5.2.2)

### Class: prov:EmptyDictionary (§5.2.2)

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#EmptyDictionary

An empty dictionary is a dictionary that has no members.
> **Example:**
>
> **Example**
>
> ```
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix :     <http://example.org/> .
>
> :e1 a prov:Entity .
> :e2 a prov:Entity .
>
> :d  a prov:EmptyDictionary
> .
> ```

is subclass of

prov:Dictionary (§5.2.1) [prov:EmptyCollection](https://www.w3.org/TR/2013/REC-prov-o-20130430/#EmptyCollection "http://www.w3.org/ns/prov#EmptyCollection")

### Class: prov:KeyEntityPair (§5.2.3)

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#KeyEntityPair

A key-entity pair. Part of a prov:Dictionary through prov:hadDictionaryMember. The key is any RDF Literal, the value is a prov:Entity.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
>
> :our-baseball-team-field-positions
>    a prov:Dictionary,
>          :FieldPositions;
>     prov:hadDictionaryMember [
>        a prov:KeyEntityPair;
>        prov:pairKey "first-baseman"^^xsd:string;
>        prov:pairEntity :george;
>     ];
>     prov:hadDictionaryMember [
>        a prov:KeyEntityPair;
>        prov:pairKey "pitcher"^^xsd:string;
>        prov:pairEntity :carl;
>     ];
> .
>
> :george a prov:Entity .
> :carl   a prov:Entity .
> ```

described with properties

prov:pairKey (§5.3.6)dp prov:pairEntity (§5.3.7)op

in range of

prov:hadDictionaryMember (§5.3.5)op prov:insertedKeyEntityPair (§5.3.4)op

### Class: prov:Insertion (§5.2.4)

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#Insertion

Insertion is a derivation that describes the transformation of a dictionary into another, by insertion of one or more key-entity pairs.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :our-NEW-baseball-team-field-positions
>    a prov:Dictionary,
>          :FieldPositions;
>    prov:derivedByInsertionFrom :our-old-baseball-team-field-positions;
>    prov:qualifiedInsertion [
>       a prov:Insertion;
>       prov:dictionary :our-old-baseball-team-field-positions;
>       prov:insertedKeyEntityPair [
>          a prov:KeyEntityPair;
>          prov:pairKey   "first-baseman"^^xsd:string;
>          prov:pairEntity <http://dbpedia.org/resource/Jim_Thorpe>;
>       ];
>    ];
> .
>
> <http://dbpedia.org/resource/Jim_Thorpe> a prov:Entity .
>
> :our-old-baseball-team-field-positions a prov:Dictionary .
> ```

is subclass of

[prov:Derivation](https://www.w3.org/TR/2013/REC-prov-o-20130430/#Derivation "http://www.w3.org/ns/prov#Derivation")

described with properties

prov:dictionary (§5.3.3) prov:insertedKeyEntityPair (§5.3.4)

in range of

prov:qualifiedInsertion (§5.3.8)op

qualifies

prov:derivedByInsertionFrom (§5.3.1)

### Class: prov:Removal (§5.2.5)

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#Removal

Removal is a derivation that describes the transformation of a dictionary into another, by removing one or more keys.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :d1 a prov:Dictionary .
>
> :d2
>    a prov:Dictionary,
>      prov:Entity;
>    prov:derivedByRemovalFrom :d1;
>    prov:qualifiedRemoval [
>       a prov:Removal, prov:DictionaryInvolvement;
>       prov:dictionary :d1;
>       prov:removedKey "k1"^^xsd:string,
>                       "k2"^^xsd:string;
>    ];
> .
> ```

is subclass of

[prov:Derivation](https://www.w3.org/TR/2013/REC-prov-o-20130430/#Derivation "http://www.w3.org/ns/prov#Derivation")

described with properties

prov:dictionary (§5.3.3) prov:removedKey (§5.3.10)dp

in range of

prov:qualifiedRemoval (§5.3.9)op

qualifies

prov:derivedByRemovalFrom (§5.3.2)

### 5.3 Dictionary Properties

### Property: prov:derivedByInsertionFrom (§5.3.1)op

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#derivedByInsertionFrom

The dictionary was derived from the other by insertion. Can be qualified with prov:qualifiedInsertion, which shows details of the insertion, in particular the inserted key-entity pairs.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
>
> :e1 a prov:Entity .
> :e2 a prov:Entity .
>
> :d  a prov:EmptyDictionary .
>
> :d1 a prov:Dictionary;
>    prov:derivedByInsertionFrom :d;
>    prov:qualifiedInsertion [
>       a prov:Insertion;
>       prov:dictionary :d;
>       prov:insertedKeyEntityPair [
>          a prov:KeyEntityPair;
>          prov:pairKey   "k1"^^xsd:string;
>          prov:pairEntity :e1;
>       ], [
>          a prov:KeyEntityPair;
>          prov:pairKey   "k2"^^xsd:string;
>          prov:pairEntity :e2;
>       ];
>    ];
> .
> ```

has super-properties

- [prov:wasDerivedFrom](https://www.w3.org/TR/2013/REC-prov-o-20130430/#wasDerivedFrom "http://www.w3.org/ns/prov#wasDerivedFrom")

has domain

- prov:Dictionary (§5.2.1)

has range

- prov:Dictionary (§5.2.1)

can be qualified with

- prov:qualifiedInsertion (§5.3.8)
- prov:Insertion (§5.2.4)

### Property: prov:derivedByRemovalFrom (§5.3.2)op

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#derivedByRemovalFrom

The dictionary was derived from the other by removal. Can be qualified with prov:qualifiedRemoval, which shows details of the removal, in particular the removed keys.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :d1 a prov:Dictionary .
>
> :d2
>    a prov:Dictionary, prov:Entity;
>    prov:derivedByRemovalFrom :d1;
>    prov:qualifiedRemoval [
>       a prov:Removal;
>       prov:dictionary :d1;
>       prov:removedKey "k1"^^xsd:string,
>                       "k2"^^xsd:string;
>    ];
> .
> ```

has super-properties

- [prov:wasDerivedFrom](https://www.w3.org/TR/2013/REC-prov-o-20130430/#wasDerivedFrom "http://www.w3.org/ns/prov#wasDerivedFrom")

has domain

- prov:Dictionary (§5.2.1)

has range

- prov:Dictionary (§5.2.1)

can be qualified with

- prov:qualifiedRemoval (§5.3.9)
- prov:Removal (§5.2.5)

### Property: prov:dictionary (§5.3.3)op

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#dictionary

The property used by a prov:Insertion and prov:Removal to cite the prov:Dictionary that was prov:derivedByInsertionFrom or prov:derivedByRemovalFrom another dictionary.
> **Example:**
>
> **Example**
>
> ```
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix :     <http://example.org/> .
>
> :e1 a prov:Entity .
>
> :d  a prov:EmptyDictionary .
>
> :d1 a prov:Dictionary;
>    prov:derivedByInsertionFrom :d;
>    prov:qualifiedInsertion [
>       a prov:Insertion;
>       prov:dictionary :d;
>       prov:insertedKeyEntityPair [
>          a prov:KeyEntityPair;
>          prov:pairKey   "k1"^^xsd:string;
>          prov:pairEntity :e1;
>       ];
>    ];
> .
> ```

has super-properties

- [prov:entity](https://www.w3.org/TR/2013/REC-prov-o-20130430/#p_entity "http://www.w3.org/ns/prov#entity")

has domain

- prov:Insertion (§5.2.4) or prov:Removal (§5.2.5)

has range

- prov:Dictionary (§5.2.1)

### Property: prov:insertedKeyEntityPair (§5.3.4)op

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#insertedKeyEntityPair

An object property to refer to the prov:KeyEntityPair inserted into a prov:Dictionary.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :our-NEW-baseball-team-field-positions
>    a prov:Dictionary,
>          :FieldPositions;
>    prov:derivedByInsertionFrom :our-old-baseball-team-field-positions;
>    prov:qualifiedInsertion [
>       a prov:Insertion;
>       prov:dictionary :our-old-baseball-team-field-positions;
>       prov:insertedKeyEntityPair [
>          a prov:KeyEntityPair;
>          prov:pairKey   "first-baseman"^^xsd:string;
>          prov:pairEntity <http://dbpedia.org/resource/Jim_Thorpe>;
>       ];
>    ];
> .
>
> <http://dbpedia.org/resource/Jim_Thorpe> a prov:Entity .
>
> :our-old-baseball-team-field-positions a prov:Dictionary .
> ```

has domain

- prov:Insertion (§5.2.4)

has range

- prov:KeyEntityPair (§5.2.3)

### Property: prov:hadDictionaryMember (§5.3.5)op

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#hadDictionaryMember

Describes the key-entity pair that was member of a prov:Dictionary. A dictionary can have multiple members.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :our-old-baseball-team-field-positions
>    a prov:Dictionary,
>          :FieldPositions;
>       prov:hadDictionaryMember [
>          a prov:KeyEntityPair;
>          prov:pairKey "first-baseman"^^xsd:string;
>          prov:pairEntity :george;
>       ], [
>          a prov:KeyEntityPair;
>          prov:pairKey "pitcher"^^xsd:string;
>          prov:pairEntity :carl;
>       ];
> .
>
> :george a prov:Entity .
> :carl   a prov:Entity .
> ```

has domain

- prov:Dictionary (§5.2.1)

has range

- prov:KeyEntityPair (§5.2.3)

### Property: prov:pairKey (§5.3.6)dp

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#pairKey

The key of a prov:KeyEntityPair, which is an element of a prov:Dictionary.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :our-old-baseball-team-field-positions
>    a prov:Dictionary,
>          :FieldPositions;
>       prov:hadDictionaryMember [
>          a prov:KeyEntityPair;
>          prov:pairKey "first-baseman"^^xsd:string;
>          prov:pairEntity :george;
>       ], [
>          a prov:KeyEntityPair;
>          prov:pairKey "pitcher"^^xsd:string;
>          prov:pairEntity :carl;
>       ];
> .
>
> :george a prov:Entity .
> :carl   a prov:Entity .
> ```

**has characteristics** [Functional](https://www.w3.org/TR/owl2-syntax/#Functional_Object_Properties)

has domain

- prov:KeyEntityPair (§5.2.3)

has range

- [rdfs:Literal](https://www.w3.org/TR/2004/REC-rdf-schema-20040210/#ch_literal "http://www.w3.org/TR/2004/REC-rdf-schema-20040210/#ch_literal")

### Property: prov:pairEntity (§5.3.7)op

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#pairEntity

The entity of a prov:KeyEntityPair, which is an element of a prov:Dictionary.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :our-old-baseball-team-field-positions
>    a prov:Dictionary,
>          :FieldPositions;
>       prov:hadDictionaryMember [
>          a prov:KeyEntityPair;
>          prov:pairKey "first-baseman"^^xsd:string;
>          prov:pairEntity :george;
>       ], [
>          a prov:KeyEntityPair;
>          prov:pairKey "pitcher"^^xsd:string;
>          prov:pairEntity :carl;
>       ];
> .
>
> :george a prov:Entity .
> :carl   a prov:Entity .
> ```

**has characteristics** [Functional](https://www.w3.org/TR/owl2-syntax/#Functional_Object_Properties)

has domain

- prov:KeyEntityPair (§5.2.3)

has range

- [prov:Entity](https://www.w3.org/TR/2013/REC-prov-o-20130430/#Entity "http://www.w3.org/ns/prov#Entity")

### Property: prov:qualifiedInsertion (§5.3.8)op

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#qualifiedInsertion

prov:qualifiedInsertion shows the details of an insertion, in particular the inserted key-entity pairs.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :our-NEW-baseball-team-field-positions
>    a prov:Dictionary,
>          :FieldPositions;
>    prov:derivedByInsertionFrom :our-old-baseball-team-field-positions;
>    prov:qualifiedInsertion [
>       a prov:Insertion;
>       prov:dictionary :our-old-baseball-team-field-positions;
>       prov:insertedKeyEntityPair [
>          a prov:KeyEntityPair;
>          prov:pairKey   "first-baseman"^^xsd:string;
>          prov:pairEntity <http://dbpedia.org/resource/Jim_Thorpe>;
>       ];
>    ];
> .
>
> <http://dbpedia.org/resource/Jim_Thorpe> a prov:Entity .
>
> :our-old-baseball-team-field-positions
>    a prov:Dictionary,
>          :FieldPositions  .
> ```

has super-properties

- [prov:qualifiedDerivation](https://www.w3.org/TR/2013/REC-prov-o-20130430/#qualifiedDerivation "http://www.w3.org/ns/prov#qualifiedDerivation")

has domain

- prov:Dictionary (§5.2.1)

has range

- prov:Insertion (§5.2.4)

qualifies

prov:derivedByInsertionFrom (§5.3.1)

### Property: prov:qualifiedRemoval (§5.3.9)op

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#qualifiedRemoval

prov:qualifiedRemoval shows the details of a removal, in particular the removed keys.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :d1 a prov:Dictionary .
>
> :d2
>    a prov:Dictionary, prov:Entity;
>    prov:derivedByRemovalFrom :d1;
>    prov:qualifiedRemoval [
>       a prov:Removal;
>       prov:dictionary :d1;
>       prov:removedKey "k1"^^xsd:string,
>                       "k2"^^xsd:string;
>    ];
> .
> ```

The dictionary was derived from the other by removal. prov:qualifiedRemoval shows details of the removal, in particular the removed keys.

has super-properties

- [prov:qualifiedDerivation](https://www.w3.org/TR/2013/REC-prov-o-20130430/#qualifiedDerivation "http://www.w3.org/ns/prov#qualifiedDerivation")

has domain

- prov:Dictionary (§5.2.1)

has range

- prov:Removal (§5.2.5)

qualifies

prov:derivedByRemovalFrom (§5.3.2)

### Property: prov:removedKey (§5.3.10)dp

back to §5.1 Overview

**IRI:** http://www.w3.org/ns/prov#removedKey

The key removed in a Removal.
> **Example:**
>
> **Example**
>
> ```
> @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
> @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
> @prefix owl:  <http://www.w3.org/2002/07/owl#> .
> @prefix prov: <http://www.w3.org/ns/prov#> .
> @prefix :     <http://example.com/> .
>
> :d2
>    a prov:Dictionary,
>      prov:Entity;
>    prov:derivedByRemovalFrom :d1;
>    prov:qualifiedRemoval [
>       a prov:Removal,
>         prov:DictionaryInvolvement;
>       prov:dictionary :d1;
>       prov:removedKey "k1"^^xsd:string,
>                        1337,
>                        3.14;
>    ];
> .
> ```

has domain

- prov:Removal (§5.2.5)

has range

- [rdfs:Literal](https://www.w3.org/TR/2004/REC-rdf-schema-20040210/#ch_literal "http://www.w3.org/TR/2004/REC-rdf-schema-20040210/#ch_literal")

## 6. PROV-XML Representation of Dictionary

This section details how to describe dictionaries with
the [PROV-XML] serialization. The [[XML schema for PROV-Dictionary](https://www.w3.org/ns/prov-dictionary.xsd)] is available for download, and includes [prov-core.xsd](https://www.w3.org/ns/prov-core.xsd), the core schema of PROV. Alternatively, the default schema, [prov.xsd](https://www.w3.org/ns/prov.xsd) can be used, which imports [prov-core.xsd](https://www.w3.org/ns/prov-core.xsd) and all extension schemas developed by the Working Group.

### 6.1 Dictionary

To specialize an Entity as a prov:Dictionary or prov:EmptyDictionary, the element `<prov:dictionary>` or `<prov:emptyDictionary>` is used, respectively.

```
<xs:complexType xmlns:xs="http://www.w3.org/2001/XMLSchema" name="Dictionary"  >
  <xs:complexContent>
  <xs:extension base="prov:Collection"></xs:extension>
  </xs:complexContent>
</xs:complexType>
```

Usage in XML:

```
<xs:element name="dictionary" type="prov:Dictionary" substitutionGroup="prov:internalElement" />
```

An EmptyDictionary is asserted with the `prov:type` "prov:EmptyDictionary" and denotes a Dictionary with no members.

```
<xs:complexType xmlns:xs="http://www.w3.org/2001/XMLSchema" name="EmptyDictionary"  >
  <xs:complexContent>
  <xs:extension base="prov:Dictionary"></xs:extension>
  </xs:complexContent>
</xs:complexType>
```

Usage in XML:

```
<xs:element name="emptyDictionary" type="prov:EmptyDictionary" substitutionGroup="prov:internalElement" />
```
> **Example:**
>
> > **Example:**
> >
> > Example 4
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <!-- d0 is an empty dictionary -->
>   <prov:emptyDictionary prov:id="d0" />
>
>   <!-- d1 is a dictionary, with (so far) unknown content -->
>   <prov:dictionary prov:id="d1" />
>
> </prov:document>
> ```

### 6.2 Key-Entity Pair

Key-entity pairs are used to identify the members of a dictionary.

```
<xs:complexType xmlns:xs="http://www.w3.org/2001/XMLSchema" name="KeyEntityPair"  >
  <xs:sequence>
    <xs:element name="key" type="xs:anySimpleType" />
    <xs:element name="entity" type="prov:IDRef" />
  </xs:sequence>
</xs:complexType>
```

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="keyEntityPair" type="prov:KeyEntityPair" substitutionGroup="prov:internalElement"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 5
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#"
>     xmlns:ex="http://example.com/ns/ex#">
>
>   <prov:entity prov:id="e0"/>
>   <prov:entity prov:id="e1"/>
>
>   <prov:keyEntityPair>
>     <prov:key>k0</prov:key>
>     <prov:entity prov:ref="e0"/>
>   </prov:keyEntityPair>
>
>   <prov:keyEntityPair>
>     <prov:key>k1</prov:key>
>     <prov:entity prov:ref="e1"/>
>   </prov:keyEntityPair>
> </prov:document>
> ```

### 6.3 Dictionary Membership

The members of a dictionary are specified by listing key-entity pairs inside a `prov:DictionaryMembership` element

```
<xs:complexType xmlns:xs="http://www.w3.org/2001/XMLSchema" name="DictionaryMembership">
  <xs:sequence>
    <xs:element name="dictionary" type="prov:IDRef"/>
    <xs:element name="keyEntityPair type="prov:KeyEntityPair" minOccurs="1" maxOccurs="unbounded"/>
  </xs:sequence>
</xs:complexType>
```

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="hadDictionaryMember" type="prov:DictionaryMembership" substitutionGroup="prov:internalElement"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 6
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#">
>
>   <prov:entity prov:id="e0"/>
>   <prov:entity prov:id="e1"/>
>   <prov:entity prov:id="e2"/>
>
>   <prov:dictionary prov:id="d" />
>
>   <prov:hadDictionaryMember>
>     <prov:dictionary prov:ref="d"/>
>     <prov:keyEntityPair>
>       <prov:key>k0</prov:key>
>       <prov:entity prov:ref="e0"/>
>     </prov:keyEntityPair>
>     <prov:keyEntityPair>
>       <prov:key>k1</prov:key>
>       <prov:entity prov:ref="e1"/>
>     </prov:keyEntityPair>
>     <prov:keyEntityPair>
>       <prov:key>k2</prov:key>
>       <prov:entity prov:ref="e2"/>
>     </prov:keyEntityPair>
>   </prov:hadDictionaryMember>
>
> </prov:document>
> ```

### 6.4 Insertion

To specify that one dictionary was derived by insertion of key-entity pairs into another one, a `prov:Insertion` element is used.

```
<xs:complexType xmlns:xs="http://www.w3.org/2001/XMLSchema" name="Insertion">
  <xs:sequence>
    <xs:element name="newDictionary" type="prov:IDRef"/>
    <xs:element name="oldDictionary" type="prov:IDRef"/>
    <xs:element name="keyEntityPair type="prov:KeyEntityPair" minOccurs="1" maxOccurs="unbounded"/>
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="derivedByInsertionFrom" type="prov:Insertion" substitutionGroup="prov:internalElement"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 7
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#">
>
>   <prov:entity prov:id="e0"/>
>   <prov:entity prov:id="e1"/>
>   <prov:entity prov:id="e2"/>
>
>   <prov:dictionary prov:id="d1" />
>
>   <prov:dictionary prov:id="d2" />
>
>   <prov:hadDictionaryMember>
>     <prov:dictionary prov:ref="d1"/>
>     <prov:keyEntityPair>
>       <prov:key>k0</prov:key>
>       <prov:entity prov:ref="e0"/>
>     </prov:keyEntityPair>
>   </prov:hadDictionaryMember>
>
>   <prov:derivedByInsertionFrom>
>     <prov:newDictionary prov:ref="d2"/>
>     <prov:oldDictionary prov:ref="d1"/>
>     <prov:keyEntityPair>
>       <prov:key>k1</prov:key>
>       <prov:entity prov:ref="e1"/>
>     </prov:keyEntityPair>
>     <prov:keyEntityPair>
>       <prov:key>k2</prov:key>
>       <prov:entity prov:ref="e2"/>
>     </prov:keyEntityPair>
>   </prov:derivedByInsertionFrom>
>
> </prov:document>
> ```

### 6.5 Removal

To specify that one dictionary was derived by removal of key-entity pairs from another one, a `prov:Removal` element is used.

```
<xs:complexType xmlns:xs="http://www.w3.org/2001/XMLSchema" name="Removal">
  <xs:sequence>
    <xs:element name="newDictionary" type="prov:IDRef"/>
    <xs:element name="oldDictionary" type="prov:IDRef"/>
    <xs:element name="key" type="xs:anySimpleType" minOccurs="1" maxOccurs="unbounded" />
    <xs:element ref="prov:label" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element ref="prov:type" minOccurs="0" maxOccurs="unbounded"/>
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute ref="prov:id"/>
</xs:complexType>
```

```
<xs:element xmlns:xs="http://www.w3.org/2001/XMLSchema" name="derivedByRemovalFrom" type="prov:Removal" substitutionGroup="prov:internalElement"/>
```
> **Example:**
>
> > **Example:**
> >
> > Example 8
>
> ```
> <prov:document
>     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>     xmlns:prov="http://www.w3.org/ns/prov#">
>
>   <prov:entity prov:id="e0"/>
>   <prov:entity prov:id="e1"/>
>   <prov:entity prov:id="e2"/>
>
>   <prov:dictionary prov:id="d1" />
>
>   <prov:dictionary prov:id="d2" />
>
>   <prov:hadDictionaryMember>
>     <prov:dictionary prov:ref="d1"/>
>     <prov:keyEntityPair>
>       <prov:key>k0</prov:key>
>       <prov:entity prov:ref="e0"/>
>     </prov:keyEntityPair>
>     <prov:keyEntityPair>
>       <prov:key>k1</prov:key>
>       <prov:entity prov:ref="e1"/>
>     </prov:keyEntityPair>
>     <prov:keyEntityPair>
>       <prov:key>k2</prov:key>
>       <prov:entity prov:ref="e2"/>
>     </prov:keyEntityPair>
>   </prov:hadDictionaryMember>
>
>   <prov:derivedByRemovalFrom>
>     <prov:newDictionary prov:ref="d2"/>
>     <prov:oldDictionary prov:ref="d1"/>
>     <prov:key>k1</prov:key>
>     <prov:key>k2</prov:key>
>   </prov:derivedByRemovalFrom>
>
> </prov:document>
> ```

## 7. Constraints Associated with Dictionary

In this section, we specify some inferences and constraints associated with dictionaries. These inferences and constraints *MAY* be applied to obtain valid provenance when using dictionaries. For more information about valid provenance and its purpose, we refer to the [disclaimer](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/#purpose) in [PROV-CONSTRAINTS].
Whereas collections were deliberately left unconstrained in [PROV-DM] and [PROV-CONSTRAINTS] to remain as general as possible, dictionaries are intended to provide more structure, and thus, are constrained more strictly.
For more information on how to read this section, we refer to [PROV-CONSTRAINTS].

### 7.1 Notation and Conventions

In the constraints below, statements are made concerning the equality of sets of key-entity pairs and sets of keys. For the sake of clarity, we will explain the used notations here.

1. To state that a set of keys K1 and another set of keys K2 hold exactly the same keys, we use the notation K1 = K2.
2. To state that a set of key-entity pairs KV1 and another set of key-entity pairs KV2 hold exactly the same keys, with each key in KV1 mapped to exactly the same entity as the same key in KV2, we use the notation KV1 = KV2.

For example. the sets of keys {"k1", "k2"} and {"k1", "k3", "k4"} are not considered equal, since one of the sets holds keys the other does not. Analogously, the set of key-entity pairs {("k1", e1),("k2", e2)} and the set {("k1", e2),("k2", e3)} are not considered equal, since the keys in the latter set map to different values than the same keys in the former set. The sets {("k1",e1),("k2",e2)} and {("k2",e2),("k1",e1)} are equal, because they hold the same keys, mapped to the same values, regardless of ordering.

### 7.2 Inferences

§3.1 Dictionary Membership implies [collection membership](< http://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-membership>).

Inference D1 (dictionary-membership-collection-membership)

IF prov:hadDictionaryMember(d, e1, k1) THEN hadMember(d, e1)

[Collection membership](< http://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-membership>) for collections that are dictionaries implies §3.1 Dictionary Membership.

Inference D2 (collection-membership-dictionary-membership)

IF hadMember(d, e) and 'prov:Dictionary' ∈ typeOf(d) THEN there exists a
key k such that prov:hadDictionaryMember(d, e, k)

Each key maps to a single entity.

Inference D3 (key-single-entity)

IF prov:hadDictionaryMember(d1, e1, k1) and prov:hadDictionaryMember(d1, e2, k1) THEN e1 = e2

No key-entity pairs were added to or removed from a dictionary derived by insertion, except those added or updated by the insertion.

Inference D4 (membership-insertion-membership)

Here, KV1 is a set of key-entity pairs and K1 is the key-set of KV1.

1. IF prov:hadDictionaryMember(d1, e, k) and prov:derivedByInsertionFrom(d2, d1, KV1) and k ∉ K1 THEN prov:hadDictionaryMember(d2, e, k)
2. IF prov:hadDictionaryMember(d2, e, k) and prov:derivedByInsertionFrom(d2, d1, KV1) and k ∉ K1 THEN prov:hadDictionaryMember(d1, e, k)

No key-entity pairs were added to or removed from a dictionary derived by removal, except those specified by the removal.

Inference D5 (membership-removal-membership)

Here, K1 is a set of keys.

1. IF prov:hadDictionaryMember(d1, e, k) and prov:derivedByRemovalFrom(d2, d1, K1) and k ∉ K1 THEN prov:hadDictionaryMember(d2, e, k)
2. IF prov:hadDictionaryMember(d2, e, k) and prov:derivedByRemovalFrom(d2, d1, K1) THEN prov:hadDictionaryMember(d1, e, k)

Note that inferences D4 and D5, together with constraints D9, D10 , D11 and D12, and the fact that an EmptyDictionary does not contain any key-entity pairs (as formalized in [PROV-Constraints](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/#membership-empty-collection)),
guarantee **completeness** of a dictionary, if it can be traced back to an EmptyDictionary through insertions and removals.
Here, completeness means that all key-entity pairs of the dictionary are known through a hadDictionaryMember statement.

A dictionary that was derived by an insertion of key-entity pairs, holds all these specified key-entity pairs. This inference also means that Insertion provides an "update semantics" for the keys that are already present in a dictionary.

Inference D6 (insertion-membership)

Here, KV1 is a set of key-entity pairs.

IF prov:derivedByInsertionFrom(d2, d1, KV1) THEN prov:hadDictionaryMember(d2, e, k) for each (k, e) ∈ KV1

Insertion and removal are special cases of derivation.

Inference D7 (insertion-derivation)

Here, KV1 is a set of key-entity pairs.

IF prov:derivedByInsertionFrom(d2, d1, KV1) THEN prov:wasDerivedFrom(d2, d1)

Inference D8 (removal-derivation)

Here, K1 is a set of keys.

IF prov:derivedByRemovalFrom(d2, d1, K1) THEN prov:wasDerivedFrom(d2, d1)

### 7.3 Constraints

A dictionary that was derived by removal from another dictionary, cannot contain the key-entity pairs that were removed from the latter.

Constraint D9 (impossible-removal-membership)

Here, K1 is a set of key-entity pairs.

IF prov:derivedByRemovalFrom(d2, d1, K1) and prov:hadDictionaryMember(d2, e, k) and k ∈ K1 THEN INVALID

A dictionary must not be derived through multiple insertion or removal relations.

Constraint D10 (impossible-removal-insertion)

Here, K0 is a set of keys and KV1 is a set of key-entity pairs.

IF prov:derivedByRemovalFrom(d2, d0, K0) and prov:derivedByInsertionFrom(d2, d1, KV1)THEN INVALID

Constraint D11 (unique-insertion)

Here, KV0 and KV1 are sets of key-entity pairs.

IF prov:derivedByInsertionFrom(d2, d0, KV0) and prov:derivedByInsertionFrom(d2, d1, KV1)THEN d0 = d1 and KV1 = KV2

Constraint D12 (unique-removal)

Here, K0 and K1 are sets of keys.

IF prov:derivedByRemovalFrom(d2, d0, K0) and prov:derivedByRemovalFrom(d2, d1, K1)THEN d0 = d1 and K1 = K2

### 7.4 Typing

Constraint D13 (typing)

1. IF entity(d, [prov:type='prov:Dictionary']) THEN 'prov:Dictionary' ∈ typeOf(d) and 'prov:Collection' ∈ typeOf(d) and 'entity' ∈ typeOf(d)

2. IF entity(d, [prov:type='prov:EmptyDictionary']) THEN 'prov:EmptyDictionary' ∈ typeOf(d) and 'prov:Dictionary' ∈ typeOf(d) and 'prov:Collection' ∈ typeOf(d) and 'prov:EmptyCollection' ∈ typeOf(d) and 'entity' ∈ typeOf(d)

3. IF prov:hadDictionaryMember(d, e, "k") THEN 'prov:Dictionary' ∈ typeOf(d) and 'prov:Collection' ∈ typeOf(d) and 'entity' ∈ typeOf(d) and 'entity' ∈ typeOf(e)

4. Here, KV is a set of key-entity pairs

   IF prov:derivedByInsertionFrom(d2, d1, KV) THEN 'prov:Dictionary' ∈ typeOf(d1) and 'prov:Dictionary' ∈ typeOf(d2) and 'prov:Collection' ∈ typeOf(d1) and 'entity' ∈ typeOf(d1) and 'prov:Collection' ∈ typeOf(d2) and 'entity' ∈ typeOf(d2) and 'entity' ∈ typeOf(e1)

5. Here, K is a set of keys

   IF prov:derivedByRemovalFrom(d2, d1, K) THEN 'prov:Dictionary' ∈ typeOf(d1) and 'prov:Dictionary' ∈ typeOf(d2) and 'prov:Collection' ∈ typeOf(d1) and 'entity' ∈ typeOf(d1) and 'prov:Collection' ∈ typeOf(d2) and 'entity' ∈ typeOf(d2)

## A. Example

To further clarify the use of PROV-Dictionary, we present its use in a practical scenario: tracking the provenance of a baseball team and its field positions.
In this scenario, we consider the players of the team in two consecutive seasons, and the field positions of the two opening day lineups. As example data, we use the information that is publicly available on the Wikipedia page of the Boston Red Sox [2011 season](https://en.wikipedia.org/wiki/2011_Boston_Red_Sox_season) and [2012 season](https://en.wikipedia.org/wiki/2012_Boston_Red_Sox_season).

### A.1 Data

Player roster in 2011:

| Uniform Number | Player                                                                                                | Uniform Number | Player                                                                                              | Uniform Number | Player                                                                                              | Uniform Number | Player                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------- |
|                |                                                                                                       |                |                                                                                                     |                |                                                                                                     |                |                                                                                                    |
| 91             | [Alfredo Aceves](http://dbpedia.org/resource/Alfredo_Aceves "Alfredo Aceves")                         | 32             | [Matt Albers](http://dbpedia.org/resource/Matt_Albers "Matt Albers")                                | 48             | [Scott Atchison](http://dbpedia.org/resource/Scott_Atchison "Scott Atchison")                       | 51             | [Daniel Bard](http://dbpedia.org/resource/Daniel_Bard "Daniel Bard")                               |
| 19             | [Josh Beckett](http://dbpedia.org/resource/Josh_Beckett "Josh Beckett")                               | 23             | [Érik Bédard](http://dbpedia.org/resource/%C3%89rik_B%C3%A9dard "Érik Bédard")                      | 64             | [Michael Bowden](http://dbpedia.org/resource/Michael_Bowden_(baseball) "Michael Bowden (baseball)") | 11             | [Clay Buchholz](http://dbpedia.org/resource/Clay_Buchholz "Clay Buchholz")                         |
| 61             | [Félix Doubront](http://dbpedia.org/resource/F%C3%A9lix_Doubront "Félix Doubront")                    | 53             | [Rich Hill](http://dbpedia.org/resource/Rich_Hill_(baseball) "Rich Hill (pitcher)")                 | 68             | [Tommy Hottovy](http://dbpedia.org/resource/Tommy_Hottovy "Tommy Hottovy")                          | 52             | [Bobby Jenks](http://dbpedia.org/resource/Bobby_Jenks "Bobby Jenks")                               |
| 41             | [John Lackey](http://dbpedia.org/resource/John_Lackey "John Lackey")                                  | 31             | [Jon Lester](http://dbpedia.org/resource/Jon_Lester "Jon Lester")                                   | 18             | [Daisuke Matsuzaka](http://dbpedia.org/resource/Daisuke_Matsuzaka "Daisuke Matsuzaka")              | 30             | [Andrew Miller](http://dbpedia.org/resource/Andrew_Miller_(baseball) "Andrew Miller (baseball)")   |
| 56             | [Trever Miller](http://dbpedia.org/resource/Trever_Miller "Trever Miller")                            | 46             | [Franklin Morales](http://dbpedia.org/resource/Franklin_Morales "Franklin Morales")                 | 37             | [Hideki Okajima](http://dbpedia.org/resource/Hideki_Okajima "Hideki Okajima")                       | 58             | [Jonathan Papelbon](http://dbpedia.org/resource/Jonathan_Papelbon "Jonathan Papelbon")             |
| 59             | [Dennys Reyes](http://dbpedia.org/resource/Dennys_Reyes "Dennys Reyes")                               | 63             | [Junichi Tazawa](http://dbpedia.org/resource/Junichi_Tazawa "Junichi Tazawa")                       | 49             | [Tim Wakefield](http://dbpedia.org/resource/Tim_Wakefield "Tim Wakefield")                          | 70             | [Kyle Weiland](http://dbpedia.org/resource/Kyle_Weiland "Kyle Weiland")                            |
| 35             | [Dan Wheeler](http://dbpedia.org/resource/Dan_Wheeler "Dan Wheeler")                                  | 43             | [Randy Williams](http://dbpedia.org/resource/Randy_Williams_(baseball) "Randy Williams (baseball)") | 60             | [Ryan Lavarnway](http://dbpedia.org/resource/Ryan_Lavarnway "Ryan Lavarnway")                       | 39             | [Jarrod Saltalamacchia](http://dbpedia.org/resource/Jarrod_Saltalamacchia "Jarrod Saltalamacchia") |
| 33             | [Jason Varitek](http://dbpedia.org/resource/Jason_Varitek "Jason Varitek")                            | 62             | [Lars Anderson](http://dbpedia.org/resource/Lars_Anderson_(baseball) "Lars Anderson (baseball)")    | 3              | [Mike Avilés](http://dbpedia.org/resource/Mike_Avil%C3%A9s "Mike Avilés")                           | 28             | [Adrian Gonzalez](http://dbpedia.org/resource/Adrian_Gonzalez "Adrian Gonzalez")                   |
| 76             | [José Iglesias](http://dbpedia.org/resource/Jos%C3%A9_Iglesias_(baseball) "José Iglesias (baseball)") | 12             | [Jed Lowrie](http://dbpedia.org/resource/Jed_Lowrie "Jed Lowrie")                                   | 60             | [Yamaico Navarro](http://dbpedia.org/resource/Yamaico_Navarro "Yamaico Navarro")                    | 34             | [David Ortiz](http://dbpedia.org/resource/David_Ortiz "David Ortiz")                               |
| 15             | [Dustin Pedroia](http://dbpedia.org/resource/Dustin_Pedroia "Dustin Pedroia")                         | 10             | [Marco Scutaro](http://dbpedia.org/resource/Marco_Scutaro "Marco Scutaro")                          | 71             | [Nate Spears](http://dbpedia.org/resource/Nate_Spears "Nate Spears")                                | 44             | [Drew Sutton](http://dbpedia.org/resource/Drew_Sutton "Drew Sutton")                               |
| 20             | [Kevin Youkilis](http://dbpedia.org/resource/Kevin_Youkilis "Kevin Youkilis")                         | 23             | [Mike Cameron](http://dbpedia.org/resource/Mike_Cameron "Mike Cameron")                             | 13             | [Carl Crawford](http://dbpedia.org/resource/Carl_Crawford "Carl Crawford")                          | 7              | [J. D. Drew](http://dbpedia.org/resource/J._D._Drew "J. D. Drew")                                  |
| 2              | [Jacoby Ellsbury](http://dbpedia.org/resource/Jacoby_Ellsbury "Jacoby Ellsbury")                      | 55             | [Joey Gathright](http://dbpedia.org/resource/Joey_Gathright "Joey Gathright")                       | 36             | [Conor Jackson](http://dbpedia.org/resource/Conor_Jackson "Conor Jackson")                          | 54             | [Darnell McDonald](http://dbpedia.org/resource/Darnell_McDonald "Darnell McDonald")                |
| 16             | [Josh Reddick](http://dbpedia.org/resource/Josh_Reddick "Josh Reddick")                               |                |                                                                                                     |                |                                                                                                     |                |                                                                                                    |

Player roster in 2012:

| Uniform Number | Player                                                                                           | Uniform Number | Player                                                                                           | Uniform Number | Player                                                                                           | Uniform Number | Player                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------------ | -------------- | ----------------------------------------------------------------------------------------------------- |
|                |                                                                                                  |                |                                                                                                  |                |                                                                                                  |                |                                                                                                       |
| 91             | [Alfredo Aceves](http://dbpedia.org/resource/Alfredo_Aceves "Alfredo Aceves")                    | 32             | [Matt Albers](http://dbpedia.org/resource/Matt_Albers "Matt Albers")                             | 48             | [Scott Atchison](http://dbpedia.org/resource/Scott_Atchison "Scott Atchison")                    | 40             | [Andrew Bailey](http://dbpedia.org/resource/Andrew_Bailey_(baseball) "Andrew Bailey (baseball)")      |
| 51             | [Daniel Bard](http://dbpedia.org/resource/Daniel_Bard "Daniel Bard")                             | 54             | [Pedro Beato](http://dbpedia.org/resource/Pedro_Beato "Pedro Beato")                             | 19             | [Josh Beckett](http://dbpedia.org/resource/Josh_Beckett "Josh Beckett")                          | 64             | [Michael Bowden](http://dbpedia.org/resource/Michael_Bowden_(baseball) "Michael Bowden (baseball)")   |
| 32             | [Craig Breslow](http://dbpedia.org/resource/Craig_Breslow "Craig Breslow")                       | 11             | [Clay Buchholz](http://dbpedia.org/resource/Clay_Buchholz "Clay Buchholz")                       | 52             | [Chris Carpenter](http://dbpedia.org/resource/Chris_Carpenter "Chris Carpenter")                 | 35             | [Aaron Cook](http://dbpedia.org/resource/Aaron_Cook_(baseball) "Aaron Cook (baseball)")               |
| 61             | [Félix Doubront](http://dbpedia.org/resource/F%C3%A9lix_Doubront "Félix Doubront")               | 47             | [Justin Germano](http://dbpedia.org/resource/Justin_Germano "Justin Germano")                    | 53             | [Rich Hill](http://dbpedia.org/resource/Rich_Hill_(baseball) "Rich Hill (pitcher)")              | 31             | [Jon Lester](http://dbpedia.org/resource/Jon_Lester "Jon Lester")                                     |
| 18             | [Daisuke Matsuzaka](http://dbpedia.org/resource/Daisuke_Matsuzaka "Daisuke Matsuzaka")           | 37             | [Mark Melancon](http://dbpedia.org/resource/Mark_Melancon "Mark Melancon")                       | 30             | [Andrew Miller](http://dbpedia.org/resource/Andrew_Miller_(baseball) "Andrew Miller (baseball)") | 46             | [Franklin Morales](http://dbpedia.org/resource/Franklin_Morales "Franklin Morales")                   |
| 59             | [Clayton Mortensen](http://dbpedia.org/resource/Clayton_Mortensen "Clayton Mortensen")           | 44             | [Vicente Padilla](http://dbpedia.org/resource/Vicente_Padilla "Vicente Padilla")                 | 47             | [Zach Stewart](http://dbpedia.org/resource/Zach_Stewart "Zach Stewart")                          | 63             | [Junichi Tazawa](http://dbpedia.org/resource/Junichi_Tazawa "Junichi Tazawa")                         |
| 78             | [Justin Thomas](http://dbpedia.org/resource/Justin_Thomas "Justin Thomas")                       | 60             | [Ryan Lavarnway](http://dbpedia.org/resource/Ryan_Lavarnway "Ryan Lavarnway")                    | 62             | [Guillermo Quiróz](http://dbpedia.org/resource/Guillermo_Quir%C3%B3z "Guillermo Quiróz")         | 39             | [Jarrod Saltalamacchia](http://dbpedia.org/resource/Jarrod_Saltalamacchia "Jarrod Saltalamacchia")    |
| 10             | [Kelly Shoppach](http://dbpedia.org/resource/Kelly_Shoppach "Kelly Shoppach")                    | 62             | [Lars Anderson](http://dbpedia.org/resource/Lars_Anderson_(baseball) "Lars Anderson (baseball)") | 3              | [Mike Avilés](http://dbpedia.org/resource/Mike_Avil%C3%A9s "Mike Avilés")                        | 77             | [Pedro Ciriaco](http://dbpedia.org/resource/Pedro_Ciriaco "Pedro Ciriaco")                            |
| 56             | [Iván DeJesús, Jr.](http://dbpedia.org/resource/Iv%C3%A1n_DeJes%C3%BAs,_Jr. "Iván DeJesús, Jr.") | 50             | [Mauro Gomez](http://dbpedia.org/resource/Mauro_Gomez "Mauro Gomez")                             | 28             | [Adrian Gonzalez](http://dbpedia.org/resource/Adrian_Gonzalez "Adrian Gonzalez")                 | 58             | [José Iglesias](http://dbpedia.org/resource/Jos%C3%A9_Iglesias_(baseball) "José Iglesias (baseball)") |
| 23             | [Brent Lillibridge](http://dbpedia.org/resource/Brent_Lillibridge "Brent Lillibridge")           | 22             | [James Loney](http://dbpedia.org/resource/James_Loney_(baseball) "James Loney (baseball)")       | 64             | [Will Middlebrooks](http://dbpedia.org/resource/Will_Middlebrooks "Will Middlebrooks")           | 34             | [David Ortiz](http://dbpedia.org/resource/David_Ortiz "David Ortiz")                                  |
| 15             | [Dustin Pedroia](http://dbpedia.org/resource/Dustin_Pedroia "Dustin Pedroia")                    | 5              | [Nick Punto](http://dbpedia.org/resource/Nick_Punto "Nick Punto")                                | 71             | [Nate Spears](http://dbpedia.org/resource/Nate_Spears "Nate Spears")                             | 23             | [Danny Valencia](http://dbpedia.org/resource/Danny_Valencia "Danny Valencia")                         |
| 20             | [Kevin Youkilis](http://dbpedia.org/resource/Kevin_Youkilis "Kevin Youkilis")                    | 23             | [Marlon Byrd](http://dbpedia.org/resource/Marlon_Byrd "Marlon Byrd")                             | 13             | [Carl Crawford](http://dbpedia.org/resource/Carl_Crawford "Carl Crawford")                       | 2              | [Jacoby Ellsbury](http://dbpedia.org/resource/Jacoby_Ellsbury "Jacoby Ellsbury")                      |
| 70             | [Ryan Kalish](http://dbpedia.org/resource/Ryan_Kalish "Ryan Kalish")                             | 85             | [Che-Hsuan Lin](http://dbpedia.org/resource/Che-Hsuan_Lin "Che-Hsuan Lin")                       | 54             | [Darnell McDonald](http://dbpedia.org/resource/Darnell_McDonald "Darnell McDonald")              | 66             | [Daniel Nava](http://dbpedia.org/resource/Daniel_Nava "Daniel Nava")                                  |
| 26             | [Scott Podsednik](http://dbpedia.org/resource/Scott_Podsednik "Scott Podsednik")                 | 16             | [Jason Repko](http://dbpedia.org/resource/Jason_Repko "Jason Repko")                             | 7              | [Cody Ross](http://dbpedia.org/resource/Cody_Ross "Cody Ross")                                   | 12             | [Ryan Sweeney](http://dbpedia.org/resource/Ryan_Sweeney "Ryan Sweeney")                               |

Field positions of opening game in 2011:

| Position | Player                                                                                             |
| -------- | -------------------------------------------------------------------------------------------------- |
|          |                                                                                                    |
| CF       | [Jacoby Ellsbury](http://dbpedia.org/resource/Jacoby_Ellsbury "Jacoby Ellsbury")                   |
| 2B       | [Dustin Pedroia](http://dbpedia.org/resource/Dustin_Pedroia "Dustin Pedroia")                      |
| 1B       | [Adrian Gonzalez](http://dbpedia.org/resource/Adrian_Gonzalez "Adrian Gonzalez")                   |
| DH       | [David Ortiz](http://dbpedia.org/resource/David_Ortiz "David Ortiz")                               |
| 3B       | [Kevin Youkilis](http://dbpedia.org/resource/Kevin_Youkilis "Kevin Youkilis")                      |
| RF       | [Mike Cameron](http://dbpedia.org/resource/Mike_Cameron "Mike Cameron")                            |
| LF       | [Carl Crawford](http://dbpedia.org/resource/Carl_Crawford "Carl Crawford")                         |
| C        | [Jarrod Saltalamacchia](http://dbpedia.org/resource/Jarrod_Saltalamacchia "Jarrod Saltalamacchia") |
| SS       | [Marco Scutaro](http://dbpedia.org/resource/Marco_Scutaro "Marco Scutaro")                         |
| SP       | [Jon Lester](http://dbpedia.org/resource/Jon_Lester "Jon Lester")                                  |

Field positions of opening game in 2012:

| Position | Player                                                                                             |
| -------- | -------------------------------------------------------------------------------------------------- |
|          |                                                                                                    |
| CF       | [Jacoby Ellsbury](http://dbpedia.org/resource/Jacoby_Ellsbury "Jacoby Ellsbury")                   |
| 2B       | [Dustin Pedroia](http://dbpedia.org/resource/Dustin_Pedroia "Dustin Pedroia")                      |
| 1B       | [Adrian Gonzalez](http://dbpedia.org/resource/Adrian_Gonzalez "Adrian Gonzalez")                   |
| DH       | [David Ortiz](http://dbpedia.org/resource/David_Ortiz "David Ortiz")                               |
| 3B       | [Kevin Youkilis](http://dbpedia.org/resource/Kevin_Youkilis "Kevin Youkilis")                      |
| RF       | [Ryan Sweeney](http://dbpedia.org/resource/Ryan_Sweeney "Ryan Sweeney")                            |
| LF       | [Cody Ross](http://dbpedia.org/resource/Cody_Ross "Cody Ross")                                     |
| C        | [Jarrod Saltalamacchia](http://dbpedia.org/resource/Jarrod_Saltalamacchia "Jarrod Saltalamacchia") |
| SS       | [Mike Avilés](http://dbpedia.org/resource/Mike_Avil%C3%A9s "Mike Avilés")                          |
| SP       | [Jon Lester](http://dbpedia.org/resource/Jon_Lester "Jon Lester")                                  |

### A.2 Provenance

In this section, the provenance of the data is asserted in each of the three serializations described in this document.

#### A.2.1 PROV-N

The following is an excerpt of the complete provenance, not listing all the player entities to avoid overloading this document. The complete provenance is available for download as a [separate file](https://www.w3.org/TR/prov-dictionary/example/example.provn).

```
document
  prefix ex <http://example.org>
  prefix dbpedia <http://dbpedia.org/resource/>
  ////////////////
  //All Players//
  ////////////////
  ... //see external file for complete provenance
  ///////////////
  //2011 Roster//
  ///////////////
  entity(ex:roster_2011, [prov:type="prov:Dictionary])
  ... //see external file for complete provenance
  ///////////////////////////
  //2011 Opening Day lineup//
  ///////////////////////////
  entity(ex:opening_day_lineup_2011, [prov:type="prov:Dictionary])
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:Jacoby_Ellsbury, "CF")
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:Dustin_Pedroia, "2B")
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:Adrian_Gonzalez, "1B")
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:David_Ortiz, "DH")
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:Kevin_Youkilis, "3B")
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:Mike_Cameron, "RF")
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:Carl_Crawford, "LF")
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:Jarrod_Saltalamacchia, "C")
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:Marco_Scutaro, "SS")
  prov:hadDictionaryMember(ex:opening_day_lineup_2011, dbpedia:Jon_Lester, "SP")
  //////////////////////////////////////////////////////////////////////////////////////////////////
  //2011 roster without players that left the team after the 2011 season or changed uniform number//
  //////////////////////////////////////////////////////////////////////////////////////////////////
  entity(ex:roster_2011_after_removals, prov:type="prov:Dictionary")
  prov:wasDerivedByRemovalFrom(ex:roster_2011_after_removals, ex:roster_2011,
    {"10", "12", "16", "23", "23", "33", "35", "36", "37", "41", "43", "44", "49", "52", "55", "56",
    "58", "59", "60", "68", "7", "70", "76"})
  ///////////////
  //2012 Roster//
  ///////////////
  entity(ex:roster_2012, [prov:type="prov:Dictionary])
  prov:wasDerivedByInsertionFrom(ex:roster_2012, ex:roster_2011_after_removals, {
    ("10", dbpedia:Kelly_Shoppach),
    ("12", dbpedia:Ryan_Sweeney),
    ("16", dbpedia:Jason_Repko),
    ("22", dbpedia:James_Loney_(baseball)),
    ("23", dbpedia:Brent_Lillibridge),
    ("23", dbpedia:Danny_Valencia),
    ("23", dbpedia:Marlon_Byrd),
    ("26", dbpedia:Scott_Podsednik),
    ("32", dbpedia:Craig_Breslow),
    ("35", dbpedia:Aaron_Cook_(baseball)),
    ("37", dbpedia:Mark_Melancon),
    ("40", dbpedia:Andrew_Bailey_(baseball)),
    ("44", dbpedia:Vicente_Padilla),
    ("47", dbpedia:Justin_Germano),
    ("47", dbpedia:Zach_Stewart),
    ("5", dbpedia:Nick_Punto),
    ("50", dbpedia:Mauro_Gomez),
    ("52", dbpedia:Chris_Carpenter),
    ("54", dbpedia:Pedro_Beato),
    ("56", dbpedia:Ivan_DeJesus,_Jr.),
    ("58", dbpedia:Jose_Iglesias_(baseball)),
    ("59", dbpedia:Clayton_Mortensen),
    ("62", dbpedia:Guillermo_Quiroz),
    ("64", dbpedia:Will_Middlebrooks),
    ("66", dbpedia:Daniel_Nava),
    ("7", dbpedia:Cody_Ross),
    ("70", dbpedia:Ryan_Kalish),
    ("77", dbpedia:Pedro_Ciriaco),
    ("78", dbpedia:Justin_Thomas),
    ("85", dbpedia:Che-Hsuan_Lin)
  })
  ///////////////////////////////////////////////////////
  //2012 Opening Day lineup (update of 2011 dictionary)//
  ///////////////////////////////////////////////////////
  entity(ex:opening_day_lineup_2012, [prov:type="prov:Dictionary])
  prov:wasDerivedByInsertionFrom(ex:opening_day_lineup_2012, ex:opening_day_lineup_2011, {
    ("RF", dbpedia:Ryan_Sweeney"),
    ("LF", dbpedia:Cody_Ross"),
    ("SS", dbpedia:Mike_Aviles"),
  })

endDocument

```

#### A.2.2 PROV-O

The following is an excerpt of the complete provenance, not listing all the player entities to avoid overloading this document. The complete provenance is available for download as a [separate file](https://www.w3.org/TR/prov-dictionary/example/example.ttl).

```
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dbpedia: <http://dbpedia.org/resource/> .
@prefix ex: <http://example.com/> .

#All Player Entities, see complete provenance file.
...

#2011 Roster
ex:roster_2011
  a prov:Entity, prov:Dictionary;
  ... #For all dictionary members, see complete provenance file.
  .

#2011 Opening Day lineup
ex:opening_day_lineup_2011
  a prov:Entity, prov:Dictionary;
  prov:hadDictionaryMember [
    a prov:KeyEntityPair;
    prov:pairKey "CF"^^xsd:string;
    prov:pairEntity dbpedia:Jacoby_Ellsbury;
  ],  [
    a prov:KeyEntityPair;
    prov:pairKey "2B"^^xsd:string;
    prov:pairEntity dbpedia:Dustin_Pedroia;
  ],  [
    a prov:KeyEntityPair;
    prov:pairKey "1B"^^xsd:string;
    prov:pairEntity dbpedia:Adrian_Gonzalez;
  ],  [
    a prov:KeyEntityPair;
    prov:pairKey "DH"^^xsd:string;
    prov:pairEntity dbpedia:David_Ortiz;
  ],  [
    a prov:KeyEntityPair;
    prov:pairKey "3B"^^xsd:string;
    prov:pairEntity dbpedia:Kevin_Youkilis;
  ],  [
    a prov:KeyEntityPair;
    prov:pairKey "RF"^^xsd:string;
    prov:pairEntity dbpedia:Mike_Cameron;
  ],  [
    a prov:KeyEntityPair;
    prov:pairKey "LF"^^xsd:string;
    prov:pairEntity dbpedia:Carl_Crawford;
  ],  [
    a prov:KeyEntityPair;
    prov:pairKey "C"^^xsd:string;
    prov:pairEntity dbpedia:Jarrod_Saltalamacchia;
  ],  [
    a prov:KeyEntityPair;
    prov:pairKey "SS"^^xsd:string;
    prov:pairEntity dbpedia:Marco_Scutaro;
  ],  [
    a prov:KeyEntityPair;
    prov:pairKey "SP"^^xsd:string;
    prov:pairEntity dbpedia:Jon_Lester;
  ] .

#2011 roster without players that left the team after the 2011 season or changed uniform number
ex:roster_2011_after_removals
  a prov:Entity, prov:Dictionary;
  prov:derivedByRemovalFrom ex:roster_2011;
  prov:qualifiedRemoval [
    a prov:Removal;
    prov:dictionary ex:roster_2011;
    prov:removedKey "10"^^xsd:string, "12"^^xsd:string, "16"^^xsd:string, "23"^^xsd:string,
                    "23"^^xsd:string, "33"^^xsd:string, "35"^^xsd:string, "36"^^xsd:string,
                    "37"^^xsd:string, "41"^^xsd:string, "43"^^xsd:string, "44"^^xsd:string,
                    "49"^^xsd:string, "52"^^xsd:string, "55"^^xsd:string, "56"^^xsd:string,
                    "58"^^xsd:string, "59"^^xsd:string, "60"^^xsd:string, "68"^^xsd:string,
                    "7"^^xsd:string, "70"^^xsd:string, "76"^^xsd:string;
    ] .

#2012 Roster
ex:roster_2012
  a prov:Entity, prov:Dictionary;
  prov:derivedByInsertionFrom ex:roster_2011_after_removals;
  prov:qualifiedInsertion [
    a prov:Insertion;
    prov:insertedKeyEntityPair [
      prov:pairKey "10"^^xsd:string;
      prov:pairEntity dbpedia:Kelly_Shoppach;
    ], [
      prov:pairKey "12"^^xsd:string;
      prov:pairEntity dbpedia:Ryan_Sweeney;
    ], [
      prov:pairKey "16"^^xsd:string;
      prov:pairEntity dbpedia:Jason_Repko;
    ], [
      prov:pairKey "22"^^xsd:string;
      prov:pairEntity <http://dbpedia.org/resource/James_Loney_(baseball)>;
    ], [
      prov:pairKey "23"^^xsd:string;
      prov:pairEntity dbpedia:Brent_Lillibridge;
    ], [
      prov:pairKey "23"^^xsd:string;
      prov:pairEntity dbpedia:Danny_Valencia;
    ], [
      prov:pairKey "23"^^xsd:string;
      prov:pairEntity dbpedia:Marlon_Byrd;
    ], [
      prov:pairKey "26"^^xsd:string;
      prov:pairEntity dbpedia:Scott_Podsednik;
    ], [
      prov:pairKey "32"^^xsd:string;
      prov:pairEntity dbpedia:Craig_Breslow;
    ], [
      prov:pairKey "35"^^xsd:string;
      prov:pairEntity <http://dbpedia.org/resource/Aaron_Cook_(baseball)>;
    ], [
      prov:pairKey "37"^^xsd:string;
      prov:pairEntity dbpedia:Mark_Melancon;
    ], [
      prov:pairKey "40"^^xsd:string;
      prov:pairEntity <http://dbpedia.org/resource/Andrew_Bailey_(baseball)>;
    ], [
      prov:pairKey "44"^^xsd:string;
      prov:pairEntity dbpedia:Vicente_Padilla;
    ], [
      prov:pairKey "47"^^xsd:string;
      prov:pairEntity dbpedia:Justin_Germano;
    ], [
      prov:pairKey "47"^^xsd:string;
      prov:pairEntity dbpedia:Zach_Stewart;
    ], [
      prov:pairKey "5"^^xsd:string;
      prov:pairEntity dbpedia:Nick_Punto;
    ], [
      prov:pairKey "50"^^xsd:string;
      prov:pairEntity dbpedia:Mauro_Gomez;
    ], [
      prov:pairKey "52"^^xsd:string;
      prov:pairEntity dbpedia:Chris_Carpenter;
    ], [
      prov:pairKey "54"^^xsd:string;
      prov:pairEntity dbpedia:Pedro_Beato;
    ], [
      prov:pairKey "56"^^xsd:string;
      prov:pairEntity <http://dbpedia.org/resource/Ivan_DeJesus,_Jr.>;
    ], [
      prov:pairKey "58"^^xsd:string;
      prov:pairEntity <http://dbpedia.org/resource/Jose_Iglesias_(baseball)>;
    ], [
      prov:pairKey "59"^^xsd:string;
      prov:pairEntity dbpedia:Clayton_Mortensen;
    ], [
      prov:pairKey "62"^^xsd:string;
      prov:pairEntity dbpedia:Guillermo_Quiroz;
    ], [
      prov:pairKey "64"^^xsd:string;
      prov:pairEntity dbpedia:Will_Middlebrooks;
    ], [
      prov:pairKey "66"^^xsd:string;
      prov:pairEntity dbpedia:Daniel_Nava;
    ], [
      prov:pairKey "7"^^xsd:string;
      prov:pairEntity dbpedia:Cody_Ross;
    ], [
      prov:pairKey "70"^^xsd:string;
      prov:pairEntity dbpedia:Ryan_Kalish;
    ], [
      prov:pairKey "77"^^xsd:string;
      prov:pairEntity dbpedia:Pedro_Ciriaco;
    ], [
      prov:pairKey "78"^^xsd:string;
      prov:pairEntity dbpedia:Justin_Thomas;
    ], [
      prov:pairKey "85"^^xsd:string;
      prov:pairEntity dbpedia:Che-Hsuan_Lin;
    ];
  ] .

#2012 Opening Day lineup (update of 2011 dictionary)
ex:opening_day_lineup_2012
  a prov:Entity, prov:Dictionary;
  prov:wasDerivedByInsertionFrom ex:opening_day_lineup_2011;
  prov:qualifiedInsertion [
    a prov:Insertion;
    prov:insertedKeyEntityPair [
      a prov:KeyEntityPair;
      prov:pairKey "RF"^^xsd:string;
      prov:pairEntity dbpedia:Ryan_Sweeney;
    ],[
      a prov:KeyEntityPair;
      prov:pairKey "LF"^^xsd:string;
      prov:pairEntity dbpedia:Cody_Ross;
    ],[
      a prov:KeyEntityPair;
      prov:pairKey "SS"^^xsd:string;
      prov:pairEntity dbpedia:Mike_Aviles;
    ];
  ] .

```

#### A.2.3 PROV-XML

The following is an excerpt of the complete provenance, not listing all the player entities to avoid overloading this document. The complete provenance is available for download as a [separate file](https://www.w3.org/TR/prov-dictionary/example/example.provx).

```
<?xml version="1.0" encoding="UTF-8"?>
<prov:document
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:prov="http://www.w3.org/ns/prov#"
    xmlns:dbpedia="http://dbpedia.org/resource/"
    xmlns:ex="http://example.com/"
    xsi:schemaLocation="http://www.w3.org/ns/prov#
http://www.w3.org/ns/prov.xsd ">
  <!-- All Player Entities -->
  ... <!-- See complete provenance file -->

  <!-- 2011 Roster -->
  <prov:dictionary prov:id="ex:roster_2011" />
  <prov:hadDictionaryMember>
    <prov:dictionary prov:ref="ex:roster_2011"/>
    ... <!-- See complete provenance file -->
  </prov:hadDictionaryMember>

  <!-- 2011 Opening Day lineup -->
  <prov:dictionary prov:id="ex:opening_day_lineup_2011" />
  <prov:hadDictionaryMember>
    <prov:dictionary prov:ref="ex:opening_day_lineup_2011"/>
    <prov:keyEntityPair>
      <prov:key>CF</prov:key>
      <prov:entity prov:ref="dbpedia:Jacoby_Ellsbury"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>2B</prov:key>
      <prov:entity prov:ref="dbpedia:Dustin_Pedroia"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>1B</prov:key>
      <prov:entity prov:ref="dbpedia:Adrian_Gonzalez"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>DH</prov:key>
      <prov:entity prov:ref="dbpedia:David_Ortiz"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>3B</prov:key>
      <prov:entity prov:ref="dbpedia:Kevin_Youkilis"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>RF</prov:key>
      <prov:entity prov:ref="dbpedia:Mike_Cameron"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>LF</prov:key>
      <prov:entity prov:ref="dbpedia:Carl_Crawford"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>C</prov:key>
      <prov:entity prov:ref="dbpedia:Jarrod_Saltalamacchia"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>SS</prov:key>
      <prov:entity prov:ref="dbpedia:Marco_Scutaro"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>SP</prov:key>
      <prov:entity prov:ref="dbpedia:Jon_Lester"/>
    </prov:keyEntityPair>
  </prov:hadDictionaryMember>

  <!-- 2011 roster without players that left the team after the 2011 season or changed uniform number -->
  <prov:dictionary prov:id="ex:roster_2011_after_removals" />
  <prov:derivedByRemovalFrom>
    <prov:newDictionary prov:ref="ex:roster_2011_after_removals"/>
    <prov:oldDictionary prov:ref="ex:roster_2011"/>
    <prov:key>10</prov:key>
    <prov:key>12</prov:key>
    <prov:key>16</prov:key>
    <prov:key>23</prov:key>
    <prov:key>23</prov:key>
    <prov:key>33</prov:key>
    <prov:key>35</prov:key>
    <prov:key>36</prov:key>
    <prov:key>37</prov:key>
    <prov:key>41</prov:key>
    <prov:key>43</prov:key>
    <prov:key>44</prov:key>
    <prov:key>49</prov:key>
    <prov:key>52</prov:key>
    <prov:key>55</prov:key>
    <prov:key>56</prov:key>
    <prov:key>58</prov:key>
    <prov:key>59</prov:key>
    <prov:key>60</prov:key>
    <prov:key>68</prov:key>
    <prov:key>7</prov:key>
    <prov:key>70</prov:key>
    <prov:key>76</prov:key>
  </prov:derivedByRemovalFrom>

  <!-- 2012 Roster -->
  <prov:dictionary prov:id="ex:roster_2012" />
  <prov:derivedByInsertionFrom>
    <prov:newDictionary prov:ref="ex:roster_2012"/>
    <prov:oldDictionary prov:ref="ex:roster_2011_after_removals"/>
    <prov:keyEntityPair>
      <prov:key>10</prov:key>
      <prov:entity prov:ref="dbpedia:Kelly_Shoppach"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>12</prov:key>
      <prov:entity prov:ref="dbpedia:Ryan_Sweeney"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>16</prov:key>
      <prov:entity prov:ref="dbpedia:Jason_Repko"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>22</prov:key>
      <prov:entity xmlns:dbpedia="http://dbpedia.org/resource/James_Loney_(baseball)#" prov:ref="dbpedia:James_Loney_baseball"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>23</prov:key>
      <prov:entity prov:ref="dbpedia:Brent_Lillibridge"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>23</prov:key>
      <prov:entity prov:ref="dbpedia:Danny_Valencia"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>23</prov:key>
      <prov:entity prov:ref="dbpedia:Marlon_Byrd"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>26</prov:key>
      <prov:entity prov:ref="dbpedia:Scott_Podsednik"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>32</prov:key>
      <prov:entity prov:ref="dbpedia:Craig_Breslow"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>35</prov:key>
      <prov:entity xmlns:dbpedia="http://dbpedia.org/resource/Aaron_Cook_(baseball)#" prov:ref="dbpedia:Aaron_Cook_baseball"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>37</prov:key>
      <prov:entity prov:ref="dbpedia:Mark_Melancon"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>40</prov:key>
      <prov:entity xmlns:dbpedia="http://dbpedia.org/resource/Andrew_Bailey_(baseball)#" prov:ref="dbpedia:Andrew_Bailey_baseball"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>44</prov:key>
      <prov:entity prov:ref="dbpedia:Vicente_Padilla"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>47</prov:key>
      <prov:entity prov:ref="dbpedia:Justin_Germano"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>47</prov:key>
      <prov:entity prov:ref="dbpedia:Zach_Stewart"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>5</prov:key>
      <prov:entity prov:ref="dbpedia:Nick_Punto"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>50</prov:key>
      <prov:entity prov:ref="dbpedia:Mauro_Gomez"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>52</prov:key>
      <prov:entity prov:ref="dbpedia:Chris_Carpenter"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>54</prov:key>
      <prov:entity prov:ref="dbpedia:Pedro_Beato"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>56</prov:key>
      <prov:entity prov:ref="dbpedia:Ivan_DeJesus_Jr."/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>58</prov:key>
      <prov:entity xmlns:dbpedia="http://dbpedia.org/resource/Jose_Iglesias_(baseball)#" prov:ref="dbpedia:Jose_Iglesias_baseball"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>59</prov:key>
      <prov:entity prov:ref="dbpedia:Clayton_Mortensen"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>62</prov:key>
      <prov:entity prov:ref="dbpedia:Guillermo_Quiroz"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>64</prov:key>
      <prov:entity prov:ref="dbpedia:Will_Middlebrooks"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>66</prov:key>
      <prov:entity prov:ref="dbpedia:Daniel_Nava"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>7</prov:key>
      <prov:entity prov:ref="dbpedia:Cody_Ross"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>70</prov:key>
      <prov:entity prov:ref="dbpedia:Ryan_Kalish"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>77</prov:key>
      <prov:entity prov:ref="dbpedia:Pedro_Ciriaco"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>78</prov:key>
      <prov:entity prov:ref="dbpedia:Justin_Thomas"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>85</prov:key>
      <prov:entity prov:ref="dbpedia:Che-Hsuan_Lin"/>
    </prov:keyEntityPair>
  </prov:derivedByInsertionFrom>

  <!-- 2012 Opening Day lineup (update of 2011 dictionary) -->
  <prov:dictionary prov:id="ex:opening_day_lineup_2012" />
  <prov:derivedByInsertionFrom>
    <prov:newDictionary prov:ref="ex:opening_day_lineup_2012"/>
    <prov:oldDictionary prov:ref="ex:opening_day_lineup_2011"/>
    <prov:keyEntityPair>
      <prov:key>RF</prov:key>
      <prov:entity prov:ref="dbpedia:Ryan_Sweeney"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>LF</prov:key>
      <prov:entity prov:ref="dbpedia:Cody_Ross"/>
    </prov:keyEntityPair>
    <prov:keyEntityPair>
      <prov:key>SS</prov:key>
      <prov:entity prov:ref="dbpedia:Mike_Aviles"/>
    </prov:keyEntityPair>
  </prov:derivedByInsertionFrom>
</prov:document>

```

Note that certain disambiguated dbpedia URIs contain parentheses, and thus cannot be turned into valid XML namespace-qualified names ([QName](https://www.w3.org/TR/2009/REC-xml-names-20091208/#NT-QName)).
For URIs like these, we add a valid [NCName](https://www.w3.org/TR/2009/REC-xml-names-20091208/#NT-NCName) (derived by removing the invalid characters) as a fragment, and split the URI after the # symbol.
The first part of the URI is then used to override the `dbpedia:` prefix in the element that uses the URI as an identifier, and the valid [NCName](https://www.w3.org/TR/2009/REC-xml-names-20091208/#NT-NCName) is used as the [LocalPart](https://www.w3.org/TR/2009/REC-xml-names-20091208/#NT-LocalPart) of the [QName](https://www.w3.org/TR/2009/REC-xml-names-20091208/#NT-QName).

For example:
`<prov:entity xmlns:dbpedia="http://dbpedia.org/resource/Jose_Iglesias_(baseball)#" prov:ref="dbpedia:Jose_Iglesias_baseball"/>`

While it can be argued whether or not this practice is entirely desirable, it does follow the guidance given in the [RDF/XML Syntax Specification](https://www.w3.org/TR/2004/REC-rdf-syntax-grammar-20040210/#section-Serialising).

## B. Change Log

### B.1 Change Log Since First Public Working Draft

- Added the full title of the document.
- Added namespace and convention sections.
- Made prov: prefix explicit.
- Changed all mentions of "key-value pair" to the more accurate "key-entity pair".
- Clarified that insertions and removals are to be seen as differences rather than as operations in the context of provenance.
- Updated PROV-N grammar (renaming of concepts and restyling).
- Made prov:qualifiedInsertion (§5.3.8) and prov:qualifiedRemoval (§5.3.9) sub-properties of [qualifiedDerivation](https://www.w3.org/TR/2013/REC-prov-o-20130430/#qualifiedDerivation).
- Updated XML schema definition.
- Added an notations and conventions paragraph to the constraints.
- Updated constraints after discussion within the Working Group.
- Added example to the appendix.
- Various corrections.

## D. References

### D.1 Informative references

[PROV-AQ]

Graham Klyne; Paul Groth; eds. [Provenance Access and Query](https://www.w3.org/TR/2013/NOTE-prov-aq-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-aq-20130430/](https://www.w3.org/TR/2013/NOTE-prov-aq-20130430/)

[PROV-CONSTRAINTS]

James Cheney; Paolo Missier; Luc Moreau; eds. [Constraints of the PROV Data Model](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-constraints-20130430/](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/)

[PROV-DC]

Daniel Garijo; Kai Eckert; eds. [Dublin Core to PROV Mapping](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-dc-20130430/](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/)

[PROV-DM]

Luc Moreau; Paolo Missier; eds. [PROV-DM: The PROV Data Model](https://www.w3.org/TR/2013/REC-prov-dm-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-dm-20130430/](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)

[PROV-LINKS]

Luc Moreau; Timothy Lebo; eds. [Linking Across Provenance Bundles](https://www.w3.org/TR/2013/NOTE-prov-links-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-links-20130430/](https://www.w3.org/TR/2013/NOTE-prov-links-20130430/)

[PROV-N]

Luc Moreau; Paolo Missier; eds. [PROV-N: The Provenance Notation](https://www.w3.org/TR/2013/REC-prov-n-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-n-20130430/](https://www.w3.org/TR/2013/REC-prov-n-20130430/)

[PROV-O]

Timothy Lebo; Satya Sahoo; Deborah McGuinness; eds. [PROV-O: The PROV Ontology](https://www.w3.org/TR/2013/REC-prov-o-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-o-20130430/](https://www.w3.org/TR/2013/REC-prov-o-20130430/)

[PROV-OVERVIEW]

Paul Groth; Luc Moreau; eds. [PROV-OVERVIEW: An Overview of the PROV Family of Documents](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-overview-20130430/](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/)

[PROV-PRIMER]

Yolanda Gil; Simon Miles; eds. [PROV Model Primer](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-primer-20130430/](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/)

[PROV-SEM]

James Cheney; ed. [Semantics of the PROV Data Model](https://www.w3.org/TR/2013/NOTE-prov-sem-20130430). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-sem-20130430](https://www.w3.org/TR/2013/NOTE-prov-sem-20130430).

[PROV-XML]

Hook Hua; Curt Tilmes; Stephan Zednik; eds. [PROV-XML: The PROV XML Schema](https://www.w3.org/TR/2013/NOTE-prov-xml-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-xml-20130430/](https://www.w3.org/TR/2013/NOTE-prov-xml-20130430/)
