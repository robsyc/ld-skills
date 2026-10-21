---
title: "vCard Ontology - for describing People and Organizations"
source: https://www.w3.org/TR/vcard-rdf/
family: vocabularies
spec_date: 2014-05-22
fetched: 2026-10-21
---

# vCard Ontology - for describing People and Organizations

> People and organizations in RDF (vcard:Individual, vcard:hasEmail...).

## Contents

- Abstract
- 1 Overview
- 2 Mapping
  - 2.1 Property Parameters
  - 2.2 General Properties
  - 2.3 Identification Properties
  - 2.4 Delivery Addressing Properties
  - 2.5 Communications Properties
  - 2.6 Geographical Properties
  - 2.7 Organizational Properties
  - 2.8 Explanatory Properties
  - 2.9 Security Properties
  - 2.10 Calendar Properties
  - 2.11 Type Code Sets
  - 2.12 Equivalent Terms
- 3 Examples
- 4 Ontology
- 4.1 Classes
  - 4.1.1 Acquaintancec back to ToC or Class ToC
  - 4.1.2 Addressc back to ToC or Class ToC
  - 4.1.3 Agentc back to ToC or Class ToC
  - 4.1.4 BBSc back to ToC or Class ToC
  - 4.1.5 Carc back to ToC or Class ToC
  - 4.1.6 Cellc back to ToC or Class ToC
  - 4.1.7 Childc back to ToC or Class ToC
  - 4.1.8 Colleaguec back to ToC or Class ToC
  - 4.1.9 Contactc back to ToC or Class ToC
  - 4.1.10 Coresidentc back to ToC or Class ToC
  - 4.1.11 Coworkerc back to ToC or Class ToC
  - 4.1.12 Crushc back to ToC or Class ToC
  - 4.1.13 Datec back to ToC or Class ToC
  - 4.1.14 Domc back to ToC or Class ToC
  - 4.1.15 Emailc back to ToC or Class ToC
  - 4.1.16 Emergencyc back to ToC or Class ToC
  - 4.1.17 Faxc back to ToC or Class ToC
  - 4.1.18 Femalec back to ToC or Class ToC
  - 4.1.19 Friendc back to ToC or Class ToC
  - 4.1.20 Genderc back to ToC or Class ToC
  - 4.1.21 Groupc back to ToC or Class ToC
  - 4.1.22 Homec back to ToC or Class ToC
  - 4.1.23 Individualc back to ToC or Class ToC
  - 4.1.24 Internetc back to ToC or Class ToC
  - 4.1.25 Intlc back to ToC or Class ToC
  - 4.1.26 ISDNc back to ToC or Class ToC
  - 4.1.27 Kinc back to ToC or Class ToC
  - 4.1.28 Kindc back to ToC or Class ToC
  - 4.1.29 Labelc back to ToC or Class ToC
  - 4.1.30 Locationc back to ToC or Class ToC
  - 4.1.31 Malec back to ToC or Class ToC
  - 4.1.32 Mec back to ToC or Class ToC
  - 4.1.33 Metc back to ToC or Class ToC
  - 4.1.34 Modemc back to ToC or Class ToC
  - 4.1.35 Msgc back to ToC or Class ToC
  - 4.1.36 Musec back to ToC or Class ToC
  - 4.1.37 Namec back to ToC or Class ToC
  - 4.1.38 Neighborc back to ToC or Class ToC
  - 4.1.39 Nonec back to ToC or Class ToC
  - 4.1.40 Organizationc back to ToC or Class ToC
  - 4.1.41 Otherc back to ToC or Class ToC
  - 4.1.42 Pagerc back to ToC or Class ToC
  - 4.1.43 Parcelc back to ToC or Class ToC
  - 4.1.44 Parentc back to ToC or Class ToC
  - 4.1.45 PCSc back to ToC or Class ToC
  - 4.1.46 Phonec back to ToC or Class ToC
  - 4.1.47 Postalc back to ToC or Class ToC
  - 4.1.48 Prefc back to ToC or Class ToC
  - 4.1.49 Relation Typec back to ToC or Class ToC
  - 4.1.50 Siblingc back to ToC or Class ToC
  - 4.1.51 Spousec back to ToC or Class ToC
  - 4.1.52 Sweetheartc back to ToC or Class ToC
  - 4.1.53 Telc back to ToC or Class ToC
  - 4.1.54 Textc back to ToC or Class ToC
  - 4.1.55 Text phonec back to ToC or Class ToC
  - 4.1.56 Typec back to ToC or Class ToC
  - 4.1.57 Unknownc back to ToC or Class ToC
  - 4.1.58 VCardc back to ToC or Class ToC
  - 4.1.59 Videoc back to ToC or Class ToC
  - 4.1.60 Voicec back to ToC or Class ToC
  - 4.1.61 Workc back to ToC or Class ToC
  - 4.1.62 X400c back to ToC or Class ToC
- 4.2 Object Properties
  - 4.2.1 addressop back to ToC or Object Property ToC
  - 4.2.2 agentop back to ToC or Object Property ToC
  - 4.2.3 emailop back to ToC or Object Property ToC
  - 4.2.4 geoop back to ToC or Object Property ToC
  - 4.2.5 has additional nameop back to ToC or Object Property ToC
  - 4.2.6 has addressop back to ToC or Object Property ToC
  - 4.2.7 has calendar busyop back to ToC or Object Property ToC
  - 4.2.8 has calendar linkop back to ToC or Object Property ToC
  - 4.2.9 has calendar requestop back to ToC or Object Property ToC
  - 4.2.10 has categoryop back to ToC or Object Property ToC
  - 4.2.11 has country nameop back to ToC or Object Property ToC
  - 4.2.12 has emailop back to ToC or Object Property ToC
  - 4.2.13 has family nameop back to ToC or Object Property ToC
  - 4.2.14 has formatted nameop back to ToC or Object Property ToC
  - 4.2.15 has genderop back to ToC or Object Property ToC
  - 4.2.16 has geoop back to ToC or Object Property ToC
  - 4.2.17 has given nameop back to ToC or Object Property ToC
  - 4.2.18 has honorific prefixop back to ToC or Object Property ToC
  - 4.2.19 has honorific suffixop back to ToC or Object Property ToC
  - 4.2.20 has keyop back to ToC or Object Property ToC
  - 4.2.21 has languageop back to ToC or Object Property ToC
  - 4.2.22 has localityop back to ToC or Object Property ToC
  - 4.2.23 has logoop back to ToC or Object Property ToC
  - 4.2.24 has memberop back to ToC or Object Property ToC
  - 4.2.25 has messagingop back to ToC or Object Property ToC
  - 4.2.26 has nameop back to ToC or Object Property ToC
  - 4.2.27 has nicknameop back to ToC or Object Property ToC
  - 4.2.28 has noteop back to ToC or Object Property ToC
  - 4.2.29 has organization nameop back to ToC or Object Property ToC
  - 4.2.30 has organization unit nameop back to ToC or Object Property ToC
  - 4.2.31 has photoop back to ToC or Object Property ToC
  - 4.2.32 has postal codeop back to ToC or Object Property ToC
  - 4.2.33 has regionop back to ToC or Object Property ToC
  - 4.2.34 has relatedop back to ToC or Object Property ToC
  - 4.2.35 has roleop back to ToC or Object Property ToC
  - 4.2.36 has soundop back to ToC or Object Property ToC
  - 4.2.37 has sourceop back to ToC or Object Property ToC
  - 4.2.38 has street addressop back to ToC or Object Property ToC
  - 4.2.39 has telephoneop back to ToC or Object Property ToC
  - 4.2.40 has titleop back to ToC or Object Property ToC
  - 4.2.41 has uidop back to ToC or Object Property ToC
  - 4.2.42 has urlop back to ToC or Object Property ToC
  - 4.2.43 has valueop back to ToC or Object Property ToC
  - 4.2.44 keyop back to ToC or Object Property ToC
  - 4.2.45 logoop back to ToC or Object Property ToC
  - 4.2.46 nameop back to ToC or Object Property ToC
  - 4.2.47 organizationop back to ToC or Object Property ToC
  - 4.2.48 photoop back to ToC or Object Property ToC
  - 4.2.49 soundop back to ToC or Object Property ToC
  - 4.2.50 telephoneop back to ToC or Object Property ToC
  - 4.2.51 urlop back to ToC or Object Property ToC
- 4.3 Data Properties
  - 4.3.1 additional namedp back to ToC or Data Property ToC
  - 4.3.2 anniversarydp back to ToC or Data Property ToC
  - 4.3.3 birth datedp back to ToC or Data Property ToC
  - 4.3.4 categorydp back to ToC or Data Property ToC
  - 4.3.5 classdp back to ToC or Data Property ToC
  - 4.3.6 country namedp back to ToC or Data Property ToC
  - 4.3.7 extended addressdp back to ToC or Data Property ToC
  - 4.3.8 family namedp back to ToC or Data Property ToC
  - 4.3.9 formatted namedp back to ToC or Data Property ToC
  - 4.3.10 given namedp back to ToC or Data Property ToC
  - 4.3.11 honorific prefixdp back to ToC or Data Property ToC
  - 4.3.12 honorific suffixdp back to ToC or Data Property ToC
  - 4.3.13 labeldp back to ToC or Data Property ToC
  - 4.3.14 languagedp back to ToC or Data Property ToC
  - 4.3.15 latitudedp back to ToC or Data Property ToC
  - 4.3.16 localitydp back to ToC or Data Property ToC
  - 4.3.17 longitudedp back to ToC or Data Property ToC
  - 4.3.18 mailerdp back to ToC or Data Property ToC
  - 4.3.19 nicknamedp back to ToC or Data Property ToC
  - 4.3.20 notedp back to ToC or Data Property ToC
  - 4.3.21 organization namedp back to ToC or Data Property ToC
  - 4.3.22 organizational unit namedp back to ToC or Data Property ToC
  - 4.3.23 post office boxdp back to ToC or Data Property ToC
  - 4.3.24 postal codedp back to ToC or Data Property ToC
  - 4.3.25 product iddp back to ToC or Data Property ToC
  - 4.3.26 regiondp back to ToC or Data Property ToC
  - 4.3.27 revisiondp back to ToC or Data Property ToC
  - 4.3.28 roledp back to ToC or Data Property ToC
  - 4.3.29 sort asdp back to ToC or Data Property ToC
  - 4.3.30 street addressdp back to ToC or Data Property ToC
  - 4.3.31 time zonedp back to ToC or Data Property ToC
  - 4.3.32 titledp back to ToC or Data Property ToC
  - 4.3.33 valuedp back to ToC or Data Property ToC
- 4.4 Namespace Declarations back to ToC
- A Change History
- B Acknowledgements
- C References

---

## Abstract

The
document describes a mapping of the vCard specification (RFC6350) to
RDF/OWL. The goal is to promote the use of vCard for the description of
people and organisations utilising semantic web techniques and allowing
compatibility with traditional vCard implementations.

*This section describes the status of this document at the time of its publication. Other
documents may supersede this document. A list of current W3C publications and the latest revision
of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at http://www.w3.org/TR/.*

This document was published by the [Semantic Web Interest Group](https://www.w3.org/2001/sw/interest/) as an Interest Group Note.

If you wish to make comments regarding this document, please send them to <semantic-web@w3.org> (subscribe, [archives](http://lists.w3.org/Archives/Public/semantic-web/)).

This document updates the W3C Member Submission on vCard RDF [VCARD-MEMBER](https://www.w3.org/TR/vcard-rdf/#VCARD-MEMBER) to align with the new semantics of IETF RFC6350 [RFC6350](https://www.w3.org/TR/vcard-rdf/#RFC6350) as developed by the IETF vCard Working Group. Note that RFC6350 obsoletes the
previous RFC2426 [RF2426](https://www.w3.org/TR/vcard-rdf/#RFC2426) that the W3 Member Submission was based on.

Publication as an Interest Group Note does not imply endorsement by the W3C Membership. This is a draft document and may be updated, replaced or obsoleted by other documents at any time. It is inappropriate to cite this document as other than work in progress.

The disclosure obligations of the Participants of this group are described in the [charter](https://www.w3.org/2006/07/swig-charter#Ipr).

## 1. Overview

vCard is a specification developed by the IETF for the description
of people and organisations. Recently, vCard has been significantly
updated to Version 4 as documented in [RFC6350](https://www.w3.org/TR/vcard-rdf/#RFC6350). Typically, vCard objects are encoded in
its own defined text-based syntax or XML renderings.

The objective of this document is to provide an equivalent
representation of vCard utilizing the Semantic Web representations of
RDF/OWL. The goal is to allow compatible representations between
RFC6350 and this vCard Ontololgy.

Previous vCard ontologies, such as the W3C Member Submission on Representing vCard Objects in RDF [VCARD-MEMBER](https://www.w3.org/TR/vcard-rdf/#VCARD-MEMBER) covered vCard version 3.0 as defined in RFC2426 [RFC2426](https://www.w3.org/TR/vcard-rdf/#RFC2426).
RFC2426 has been obsoleted by RFC6350 and it is recommeded that this
vCard Ontology be used for any vCard semantic representations.
RFC6350 has introduced many additional changes such as new structures
and properties (for example, Kind, Gender, Language, Anniversary,
Calendaring attributes), additional parameters, and removed features
(for example, some Address types, inline vCards, Label). See Appendix A
of [RFC6350](https://www.w3.org/TR/vcard-rdf/#RFC6350) for complete details.
> **Issue:**
>
> > **Issue:**
> >
> > Namespace URI
>
> The current vCard Ontology (See Section 4) has continued to use the `http://www.w3.org/2006/vcard/ns#` namespace URI that was used by the previous W3C Member Submission
> on Representing vCard Objects in RDF [VCARD-MEMBER](https://www.w3.org/TR/vcard-rdf/#VCARD-MEMBER).
> This will support backwards compatibility. Please note some of the
> equivalent/deprecated terms from the previous ontology in Section 2.12.
>
> In addition, this namespace URI will also serve the JSON-LD context.

The vCard specifications have a long history and were first proposed in
1995 and then standardized by the IETF in 1998. Since then, new
vocabularies, such as the [FOAF Vocabulary Specification](http://xmlns.com/foaf/spec/) (2005), and
the [The Organisation Ontology](https://www.w3.org/TR/vocab-org/) (2013) have appeared. The vCard Ontology has also focused on
describing people and organisations, including location information and
groups of such entities. The FOAF ontology focuses more on the
relationships between people, agents, things and social web entities,
and the ORG ontology focuses on organizational structures, roles, and
activities. There are some overlaps between the three ontologies, but
they can provide useful vocabularies individually, and also can
provided enhanced information when used collaboratively.

## 2. Mapping

In order to create the OWL ontology mapping from RFC6350, some
changes and enhancements are required to reflect and support RDF/OWL
features, linked data principles, and support ontology reuse. No
semantics are changed in the mapping from RFC6350 to the vCard
Ontology. All the data types defined in RFC6350 are fully supported as
XML Schema dataypes.

The model informing the mapping from RFC6350 to OWL has been to
create OWL object properties for all things that would typically be
resources (e.g. identified with a URI) and OWL data properties for all
things
that would typically be literals (e.g. strings and dates). The model
includes naming all the object properties with a "hasX" name pattern,
and the data properties with just the "x" name pattern. However, in
some circumstances (see examples in Property Relation Mechanisms) the
data property may use its equivalent object property to support
vCard's property parameters.

> **Note:**
>
> > **Note:**
> >
> > Property Relation Mechanisms
>
>
> All versions of vCard supported additional property parameters that
> could be used with any of the descriptive properties. For example the sort-string and geography
> property parameters could be associated with any of the vCard
> properties to provide further meta-information. To support vCard's
> property parameters, a new object property (hasValue) and data property
> (value) have been defined that relates both the property and parameter
> to the vCard kind.
>
> Consider the following simple example that only includes direct property relationships:
>
> > **Example:**
> >
> > > **Example:**
> > >
> > > Direct Example
> >
> > ```
> >      <vcard:Individual rdf:about="http://example.com/me/corky">
> >        <vcard:fn>Corky Crystal</vcard:fn>
> >        <vcard:nickname>Corks</vcard:nickname>
> >        <vcard:hasEmail rdf:resource="mailto:corky@example.com"/>
> >      </vcard:Individual>
> >
> > ```
>
> If we wanted to add a *sort-as* property parameter to the
> nickname (data) property and a type property parameter (to indicate a
> home email address) to the hasEmail (object) property, then we need to
> use the hasNickname object property with the value data property and the hasValue object property with
> the hasEmail object property to capture these n-ary relationships, as
> shown below:
>
> > **Example:**
> >
> > > **Example:**
> > >
> > > N-Ary Example
> >
> > ```
> >     <vcard:Individual rdf:about="http://example.com/me/corky">
> >       <vcard:fn>Corky Crystal</vcard:fn>
> >         <vcard:hasNickname rdf:parseType="Resource">
> >           <vcard:value>Corks</vcard:value>
> >           <vcard:sort-string>cork</vcard:sort-string>
> >         </vcard:hasNickname>
> >       <vcard:hasEmail rdf:parseType="Resource">
> >         <vcard:hasValue rdf:resource="mailto:corky@example.com"/>
> >         <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Home"/>
> >       </vcard:hasEmail>
> >     </vcard:Individual>
> >
> > ```
>
> In general, the direct mechanism provides simpler vCard resources, but
> the n-ary mechanism can be used for more detailed vCard resources
> requiring property parameters.
>
> > **Issue:**
> >
> > > **Issue:**
> > >
> > > Use of rdf:value
> >
> > In previous vCard/RDF specifications, the use of rdf:value was recommended to support vCard property
> > parameters. **The use of rdf:value is now deprecated in favour of the above mechanism.** Additionally, this
> > enables the current vCard Ontology to support OWL-DL.

The following sections outlines the mapping from RFC6350 to the
vCard Ontology showing both the n-ary Relation and Direct properties.

### 2.1 Property Parameters

These properties can apply to most vCard properties.

| RFC Property | Note                                                                                            | Ontology Property |
| ------------ | ----------------------------------------------------------------------------------------------- | ----------------- |
| LANGUAGE     | The human language used in the related property (from RFC5646)                                  | language          |
| VALUE        | Not required as this is implicit in the ontology datatypes                                      |                   |
| PREF         | Recommended to use `rdf:Seq` to support ordered preferences                                     |                   |
| ALTID        | Recommended to use `rdf:Alt` to support alternative values                                      |                   |
| PID          | Recommended to use `rdf:ID` to support identified properties                                    |                   |
| TYPE         | Recommended to use `rdf:type` to indicate type. See Section 2.11 for list of vCard Type values. |                   |
| MEDIATYPE    | Not required                                                                                    |                   |
| CALSCALE     | Assume the default Gregorian system for datetimes                                               |                   |
| SORT-AS      | The string used for sorting the property                                                        | sort-string       |
| GEO          | The geographic location related to the property value (expressed as a geo URI)                  | hasGeo            |
| TZ           | The timezone related to the property value                                                      | tz                |

### 2.2 General Properties

| RFC Property | Note                                                                                | Ontology Class | Ontology Property |
| ------------ | ----------------------------------------------------------------------------------- | -------------- | ----------------- |
| BEGIN        | Not required                                                                        |                |                   |
| END          | Not required                                                                        |                |                   |
| SOURCE       | The orginal source of the vCard information                                         |                | hasSource         |
| KIND         | vCard defines "Kinds" to represent the types of objects to be represented by vCard: | Kind           |                   |
|              | Individual - To represent people                                                    | Individual     |                   |
|              | Organization - To represent organisations                                           | Organization   |                   |
|              | Group - To represent groups of vCard objects                                        | Group          |                   |
|              | Location - To represent location objects                                            | Location       |                   |
| XML          | Not required                                                                        |                |                   |

### 2.3 Identification Properties

| RFC Property | Note                                                                                   | Ontology Property                                                                                      | N-Ary Property                                                                     |
| ------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| FN           | The full name of the object (as a single string). This is the only mandatory property. | fn                                                                                                     | hasFN                                                                              |
| N            | The name of the object represented in structured parts                                 | hasName (range of class Name) given-name family-name additional-name honorific-prefix honorific-suffix | hasGivenName hasFamilyName hasAdditionalName hasHonorificPrefix hasHonorifixSuffix |
| NICKNAME     | A nickname for the object                                                              | nickname                                                                                               | hasNickname                                                                        |
| PHOTO        |                                                                                        | hasPhoto                                                                                               |                                                                                    |
| BDAY         | Birth date of the object. Should only apply to Individual.                             | bday                                                                                                   |                                                                                    |
| ANNIVERSARY  | Should only apply to Individual                                                        | anniversary                                                                                            |                                                                                    |
| GENDER       | Should only apply to Individual. See Gender Codes in Section 2.11.                     | hasGender                                                                                              |                                                                                    |

### 2.4 Delivery Addressing Properties

| RFC Property | Note                                                      | Ontology Property                                                                           | N-Ary Property                                                      |
| ------------ | --------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| ADR          | The address of the object represented in structured parts | hasAddress (range of class Address) street-address locality region country-name postal-code | hasStreetAddress hasLocality hasRegion hasCountryName hasPostalCode |

### 2.5 Communications Properties

| RFC Property | Note                                                                                                                                                 | Ontology Property | N-Ary Property |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | -------------- |
| TEL          | The telephone number as a tel URI. Recommended to use `rdf:type` to indicate the Telephone Type. See Section 2.11 for list of Telephone Type values. | hasTelephone      |                |
| EMAIL        | The email address as a mailto URI                                                                                                                    | hasEmail          |                |
| IMPP         | The IMPP instant messaging contact information                                                                                                       | hasInstantMessage |                |
| LANG         | The language of the object                                                                                                                           | language          | hasLanguage    |

### 2.6 Geographical Properties

| RFC Property | Note                                                 | Ontology Property |
| ------------ | ---------------------------------------------------- | ----------------- |
| TZ           | The timezone of the object                           | tz                |
| GEO          | The geographical coordinates of the object (geo URI) | hasGeo            |

### 2.7 Organizational Properties

| RFC Property | Note                                                                                                                                   | Ontology Property   | N-Ary Property        |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------- |
| TITLE        | The title of the object                                                                                                                | title               | hasTitle              |
| ROLE         | The role of the object                                                                                                                 | role                | hasRole               |
| LOGO         | The logo of the object (data URI)                                                                                                      | hasLogo             |                       |
| ORG          | The organisation related to the object                                                                                                 | organization-name   | hasOrganizationName   |
| ORGUNIT      | The organisational unit related to the object                                                                                          | organizational-unit | hasOrganizationalUnit |
| MEMBER       | Can only be used for Group Kind objects. Must point to other Individual or Organization objects.                                       | hasMember           |                       |
| RELATED      | Link to related objects. Recommended to use `rdf:type` to indicate the Related Type. See Section 2.11 for list of Related Type values. | hasRelated          |                       |

### 2.8 Explanatory Properties

| RFC Property | Note                                                        | Ontology Property | N-Ary Property |
| ------------ | ----------------------------------------------------------- | ----------------- | -------------- |
| CATEGORIES   | The categories of the object                                | category          | hasCategory    |
| NOTE         | Notes about the object                                      | note              | hasNote        |
| PRODID       | The identifier of the product that created the vCard object | prodid            |                |
| REV          | The revision datetime of the vCard object                   | rev               |                |
| SOUND        | Audio related to the object (data URI)                      | hasSound          |                |
| UID          | A unique identifier for the object                          | hasUID            |                |
| CLIENTPIDMAP | Not required                                                |                   |                |
| URL          | Any URL related to the object                               | hasURL            |                |
| VERSION      | Not required (namespace will capture this)                  |                   |                |

### 2.9 Security Properties

| RFC Property | Note                           | Ontology Property |
| ------------ | ------------------------------ | ----------------- |
| KEY          | The security key of the object | hasKey            |

### 2.10 Calendar Properties

| RFC Property | Note                             | Ontology Property  |
| ------------ | -------------------------------- | ------------------ |
| FBURL        | Calendar Busy Time of the object | hasCalendarBusy    |
| CALADURI     | Calendar Request of the object   | hasCalendarRequest |
| CALURI       | Calendar Link of the object      | hasCalendarLink    |

### 2.11 Type Code Sets

| RFC Property   | OWL Class                                                                                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| vCard Type     | Home Work                                                                                                                                            |
| Gender         | Female Male None Other Unknown                                                                                                                       |
| Telephone Type | Cell (mobile) Fax Pager Text (sms) TextPhone Video Voice                                                                                             |
| Related Type   | Acquaintance Agent Child Colleague Contact Coresident Coworker Crush Date Emergency Friend Kin Me Met Muse Neighbor Parent Sibling Spouse Sweetheart |

### 2.12 Equivalent Terms

The following concepts from the previous vCard Ontology have the following mappings in the current vCard Ontology

| Previous Ontology                | Equivalent (Current Ontology)          |
| -------------------------------- | -------------------------------------- |
| VCard (Class)                    | Kind                                   |
| BBS (Class)                      | NOTE: This concept has been deprecated |
| Car (Class)                      | NOTE: This concept has been deprecated |
| Dom (Class)                      | NOTE: This concept has been deprecated |
| Email (Class)                    | NOTE: This concept has been deprecated |
| ISDN (Class)                     | NOTE: This concept has been deprecated |
| Internet (Class)                 | NOTE: This concept has been deprecated |
| Intl (Class)                     | NOTE: This concept has been deprecated |
| Label (Class)                    | NOTE: This concept has been deprecated |
| Modem (Class)                    | NOTE: This concept has been deprecated |
| Msg (Class)                      | NOTE: This concept has been deprecated |
| PCS (Class)                      | NOTE: This concept has been deprecated |
| Parcel (Class)                   | NOTE: This concept has been deprecated |
| Postal (Class)                   | NOTE: This concept has been deprecated |
| Pref (Class)                     | NOTE: This concept has been deprecated |
| Tel (Class)                      | NOTE: This concept has been deprecated |
| X400 (Class)                     | NOTE: This concept has been deprecated |
| adr (object property)            | hasAddress                             |
| email (object property)          | hasEmail                               |
| geo (object property)            | hasGeo                                 |
| key (object property)            | hasKey                                 |
| logo (object property)           | hasLogo                                |
| n (object property)              | hasName                                |
| org (object property)            | organization-name                      |
| photo (object property)          | hasPhoto                               |
| sound (object property)          | hasSound                               |
| tel (object property)            | hasTelephone                           |
| url (object property)            | hasURL                                 |
| agent (object property)          | NOTE: This concept has been deprecated |
| class (data property)            | NOTE: This concept has been deprecated |
| extended-address (data property) | NOTE: This concept has been deprecated |
| label (data property)            | NOTE: This concept has been deprecated |
| latitude (data property)         | NOTE: This concept has been deprecated |
| longitude (data property)        | NOTE: This concept has been deprecated |
| mailer (data property)           | NOTE: This concept has been deprecated |
| post-office-box (data property)  | NOTE: This concept has been deprecated |

## 3. Examples
> **Example:**
>
> > **Example:**
> >
> > RDF/XML Example
>
> ```
>     <rdf:RDF  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
>               xmlns:vcard="http://www.w3.org/2006/vcard/ns#">
>       <vcard:Individual rdf:about="http://example.com/me/corky">
>         <vcard:fn>Corky Crystal</vcard:fn>
>         <vcard:nickname>Corks</vcard:nickname>
>         <vcard:hasTelephone rdf:parseType="Resource">
>           <vcard:hasValue rdf:resource="tel:+61755555555"/>
>           <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Home"/>
>           <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Voice"/>
>         </vcard:hasTelephone>
>         <vcard:hasEmail rdf:resource="mailto:corky@example.com"/>
>         <vcard:hasAddress rdf:parseType="Resource">
>           <vcard:street-address>111 Lake Drive</vcard:street-address>
>           <vcard:locality>WonderCity</vcard:locality>
>           <vcard:postal-code>5555</vcard:postal-code>
>           <vcard:country-name>Australia</vcard:country-name>
>           <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Home"/>
>         </vcard:hasAddress>
>       </vcard:Individual>
>     </rdf:RDF>
>
> ```
> **Example:**
>
> > **Example:**
> >
> > RDFa Example
>
> ```
>     <div vocab="http://www.w3.org/2006/vcard/ns#"
>          resource="http://example.com/me/corky" typeof="Individual">
>      <span property="fn">Corky Crystal</span>
>      <span property="nickname">Corks</span>
>      <span property="hasTelephone" typeof="Home Voice">
>        <span property="hasValue" href="tel:+61755555555"/>
>      </span>
>      <link property="hasEmail" href="mailto:corky@example.com"/>
>      <span property="hasAddress" typeof="Home">
>        <span property="street-address">111 Lake Drive</span>
>        <span property="locality">WonderCity</span>
>        <span property="postal-code">5555</span>
>        <span property="country-name">Australia</span>
>      </span>
>     </div>
>
> ```
> **Example:**
>
> > **Example:**
> >
> > Turtle Example
>
> ```
>     @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
>     @prefix rdfa: <http://www.w3.org/ns/rdfa#> .
>     <http://example.com/me/corky> a vcard:Individual;
>       vcard:hasEmail <mailto:corky@example.com>;
>       vcard:fn "Corky Crystal";
>       vcard:hasAddress [ a vcard:Home;
>         vcard:country-name "Australia";
>         vcard:locality "WonderCity";
>         vcard:postal-code "5555";
>         vcard:street-address "111 Lake Drive" ];
>       vcard:hasTelephone [ a vcard:Home,
>         vcard:Voice;
>         vcard:hasValue <tel:+61755555555> ];
>        vcard:nickname "Corks" .
>
> ```
> **Example:**
>
> > **Example:**
> >
> > JSON-LD Example
>
> ```
> {
>   "@context": "http://www.w3.org/2006/vcard/ns",
>   "@id": "http://example.com/me/corky",
>   "@type": "Individual",
>   "fn": "Corky Crystal",
>   "nickname": "Corks",
>   "hasEmail": "mailto:corky@example.com",
>   "hasAddress": {
>     "@type": "Home",
>     "country-name": "Australia",
>     "locality": "WonderCity",
>     "postal-code": "5555",
>     "street-address": "111 Lake Drive"
>   },
>   "hasTelephone": {
>     "@type": [ "Home", "Voice" ],
>     "hasValue": "tel:+61755555555"
>   }
> }
>
> ```

## 4. Ontology

1. §4.1 Classes
2. §4.2 Object Properties
3. §4.3 Data Properties
4. Namespace Declarations (§4.4)

## Classes

- Acquaintance (§4.1.1)
- Address (§4.1.2)
- Agent (§4.1.3)
- BBS (§4.1.4)
- Car (§4.1.5)
- Cell (§4.1.6)
- Child (§4.1.7)
- Colleague (§4.1.8)
- Contact (§4.1.9)
- Coresident (§4.1.10)
- Coworker (§4.1.11)
- Crush (§4.1.12)
- Date (§4.1.13)
- Dom (§4.1.14)
- Email (§4.1.15)
- Emergency (§4.1.16)
- Fax (§4.1.17)
- Female (§4.1.18)
- Friend (§4.1.19)
- Gender (§4.1.20)
- Group (§4.1.21)
- Home (§4.1.22)
- Individual (§4.1.23)
- Internet (§4.1.24)
- Intl (§4.1.25)
- ISDN (§4.1.26)
- Kin (§4.1.27)
- Kind (§4.1.28)
- Label (§4.1.29)
- Location (§4.1.30)
- Male (§4.1.31)
- Me (§4.1.32)
- Met (§4.1.33)
- Modem (§4.1.34)
- Msg (§4.1.35)
- Muse (§4.1.36)
- Name (§4.1.37)
- Neighbor (§4.1.38)
- None (§4.1.39)
- Organization (§4.1.40)
- Other (§4.1.41)
- Pager (§4.1.42)
- Parcel (§4.1.43)
- Parent (§4.1.44)
- PCS (§4.1.45)
- Phone (§4.1.46)
- Postal (§4.1.47)
- Pref (§4.1.48)
- Relation Type (§4.1.49)
- Sibling (§4.1.50)
- Spouse (§4.1.51)
- Sweetheart (§4.1.52)
- Tel (§4.1.53)
- Text (§4.1.54)
- Text phone (§4.1.55)
- Type (§4.1.56)
- Unknown (§4.1.57)
- VCard (§4.1.58)
- Video (§4.1.59)
- Voice (§4.1.60)
- Work (§4.1.61)
- X400 (§4.1.62)

### Acquaintancec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Acquaintance

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Addressc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Address

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the components of the delivery address for the object

is equivalent to

((country name (§4.3.6)dp some xsd:string) and (country name (§4.3.6)dp max 1)) or ((locality (§4.3.16)dp some xsd:string) and (locality (§4.3.16)dp max 1)) or ((postal code (§4.3.24)dp some xsd:string) and (postal code (§4.3.24)dp max 1)) or ((region (§4.3.26)dp some xsd:string) and (region (§4.3.26)dp max 1)) or ((street address (§4.3.30)dp some xsd:string) and (street address (§4.3.30)dp max 1))

is in range of

has address (§4.2.6)op

### Agentc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Agent

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### BBSc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#BBS

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Phone (§4.1.46)c

### Carc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Car

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Phone (§4.1.46)c

### Cellc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Cell

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Also called mobile telephone

has super-classes

Phone (§4.1.46)c

### Childc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Child

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Colleaguec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Colleague

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Contactc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Contact

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Coresidentc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Coresident

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Coworkerc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Coworker

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Crushc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Crush

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Datec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Date

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Domc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Dom

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Type (§4.1.56)c

### Emailc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Email

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the electronic mail address for communication with the object the vCard represents. Use the hasEmail object property.

is in range of

has email (§4.2.12)op

### Emergencyc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Emergency

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Faxc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Fax

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Phone (§4.1.46)c

### Femalec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Female

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Gender (§4.1.20)c

### Friendc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Friend

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Genderc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Gender

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used for gender codes. The URI of the gender code must be used as the value for Gender.

has sub-classes

Female (§4.1.18)c, Male (§4.1.31)c, None (§4.1.39)c, Other (§4.1.41)c, Unknown (§4.1.57)c

### Groupc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Group

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Object representing a group of persons or entities. A group object will usually contain hasMember properties to specify the members of the group.

is equivalent to

(has member (§4.2.24)op some Kind (§4.1.28)c) and (has member (§4.2.24)op min 1 Kind (§4.1.28)c)

has super-classes

Kind (§4.1.28)c

is in domain of

has member (§4.2.24)op

is disjoint with

Individual (§4.1.23)c, Location (§4.1.30)c, Organization (§4.1.40)c

### Homec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Home

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This implies that the property is related to an individual's personal life

has super-classes

Type (§4.1.56)c

### Individualc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Individual

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

An object representing a single person or entity

has super-classes

Kind (§4.1.28)c

is disjoint with

Group (§4.1.21)c, Location (§4.1.30)c, Organization (§4.1.40)c

### Internetc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Internet

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Type (§4.1.56)c

### Intlc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Intl

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Type (§4.1.56)c

### ISDNc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#ISDN

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Type (§4.1.56)c

### Kinc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Kin

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Kindc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Kind

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The parent class for all objects

is equivalent to

VCard (§4.1.58)c

formatted name (§4.3.9)dp min 1

has sub-classes

Group (§4.1.21)c, Individual (§4.1.23)c, Location (§4.1.30)c, Organization (§4.1.40)c

is in range of

has member (§4.2.24)op

### Labelc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Label

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Type (§4.1.56)c

### Locationc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Location

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

An object representing a named geographical place

has super-classes

Kind (§4.1.28)c

is disjoint with

Group (§4.1.21)c, Individual (§4.1.23)c, Organization (§4.1.40)c

### Malec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Male

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Gender (§4.1.20)c

### Mec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Me

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Metc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Met

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Modemc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Modem

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Phone (§4.1.46)c

### Msgc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Msg

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Phone (§4.1.46)c

### Musec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Muse

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Namec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Name

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the components of the name of the object

is equivalent to

((additional name (§4.3.1)dp some xsd:string) and (additional name (§4.3.1)dp min 0)) or ((family name (§4.3.8)dp some xsd:string) and (family name (§4.3.8)dp max 1)) or ((given name (§4.3.10)dp some xsd:string) and (given name (§4.3.10)dp max 1)) or ((honorific prefix (§4.3.11)dp some xsd:string) and (honorific prefix (§4.3.11)dp min 0)) or ((honorific suffix (§4.3.12)dp some xsd:string) and (honorific suffix (§4.3.12)dp min 0))

is in range of

has name (§4.2.26)op

### Neighborc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Neighbor

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Nonec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#None

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Gender (§4.1.20)c

### Organizationc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Organization

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

An object representing an organization. An organization is a single entity, and might represent a business or government, a department or division within a business or government, a club, an association, or the like.

has super-classes

Kind (§4.1.28)c

is disjoint with

Group (§4.1.21)c, Individual (§4.1.23)c, Location (§4.1.30)c

### Otherc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Other

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Gender (§4.1.20)c

### Pagerc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Pager

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Phone (§4.1.46)c

### Parcelc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Parcel

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Type (§4.1.56)c

### Parentc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Parent

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### PCSc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#PCS

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Phone (§4.1.46)c

### Phonec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#TelephoneType

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used for telephone type codes. The URI of the telephone type code must be used as the value for the Telephone Type.

has sub-classes

BBS (§4.1.4)c, Car (§4.1.5)c, Cell (§4.1.6)c, Fax (§4.1.17)c, Modem (§4.1.34)c, Msg (§4.1.35)c, PCS (§4.1.45)c, Pager (§4.1.42)c, Text (§4.1.54)c, Text phone (§4.1.55)c, Video (§4.1.59)c, Voice (§4.1.60)c

### Postalc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Postal

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Type (§4.1.56)c

### Prefc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Pref

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Type (§4.1.56)c

### Relation Typec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#RelatedType

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used for relation type codes. The URI of the relation type code must be used as the value for the Relation Type.

has sub-classes

Acquaintance (§4.1.1)c, Agent (§4.1.3)c, Child (§4.1.7)c, Colleague (§4.1.8)c, Contact (§4.1.9)c, Coresident (§4.1.10)c, Coworker (§4.1.11)c, Crush (§4.1.12)c, Date (§4.1.13)c, Emergency (§4.1.16)c, Friend (§4.1.19)c, Kin (§4.1.27)c, Me (§4.1.32)c, Met (§4.1.33)c, Muse (§4.1.36)c, Neighbor (§4.1.38)c, Parent (§4.1.44)c, Sibling (§4.1.50)c, Spouse (§4.1.51)c, Sweetheart (§4.1.52)c

### Siblingc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Sibling

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Spousec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Spouse

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Sweetheartc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Sweetheart

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Relation Type (§4.1.49)c

### Telc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Tel

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated. Use the hasTelephone object property.

### Textc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Text

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Also called sms telephone

has super-classes

Phone (§4.1.46)c

### Text phonec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#TextPhone

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Phone (§4.1.46)c

### Typec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Type

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used for type codes. The URI of the type code must be used as the value for Type.

has sub-classes

Dom (§4.1.14)c, Home (§4.1.22)c, ISDN (§4.1.26)c, Internet (§4.1.24)c, Intl (§4.1.25)c, Label (§4.1.29)c, Parcel (§4.1.43)c, Postal (§4.1.47)c, Pref (§4.1.48)c, Work (§4.1.61)c, X400 (§4.1.62)c

### Unknownc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Unknown

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Gender (§4.1.20)c

### VCardc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#VCard

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The vCard class is equivalent to the new Kind class, which is the parent for the four explicit types of vCards (Individual, Organization, Location, Group)

### Videoc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Video

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Phone (§4.1.46)c

### Voicec back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Voice

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

has super-classes

Phone (§4.1.46)c

### Workc back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#Work

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This implies that the property is related to an individual's work place

has super-classes

Type (§4.1.56)c

### X400c back to ToC or Class ToC (§4.1)

**IRI:** http://www.w3.org/2006/vcard/ns#X400

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This class is deprecated

has super-classes

Type (§4.1.56)c

## Object Properties

- address (§4.2.1)
- agent (§4.2.2)
- email (§4.2.3)
- geo (§4.2.4)
- has additional name (§4.2.5)
- has address (§4.2.6)
- has calendar busy (§4.2.7)
- has calendar link (§4.2.8)
- has calendar request (§4.2.9)
- has category (§4.2.10)
- has country name (§4.2.11)
- has email (§4.2.12)
- has family name (§4.2.13)
- has formatted name (§4.2.14)
- has gender (§4.2.15)
- has geo (§4.2.16)
- has given name (§4.2.17)
- has honorific prefix (§4.2.18)
- has honorific suffix (§4.2.19)
- has key (§4.2.20)
- has language (§4.2.21)
- has locality (§4.2.22)
- has logo (§4.2.23)
- has member (§4.2.24)
- has messaging (§4.2.25)
- has name (§4.2.26)
- has nickname (§4.2.27)
- has note (§4.2.28)
- has organization name (§4.2.29)
- has organization unit name (§4.2.30)
- has photo (§4.2.31)
- has postal code (§4.2.32)
- has region (§4.2.33)
- has related (§4.2.34)
- has role (§4.2.35)
- has sound (§4.2.36)
- has source (§4.2.37)
- has street address (§4.2.38)
- has telephone (§4.2.39)
- has title (§4.2.40)
- has uid (§4.2.41)
- has url (§4.2.42)
- has value (§4.2.43)
- key (§4.2.44)
- logo (§4.2.45)
- name (§4.2.46)
- organization (§4.2.47)
- photo (§4.2.48)
- sound (§4.2.49)
- telephone (§4.2.50)
- url (§4.2.51)

### addressop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#adr

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has address (§4.2.6)op

### agentop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#agent

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been deprecated

### emailop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#email

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has email (§4.2.12)op

### geoop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#geo

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has geo (§4.2.16)op

### has additional nameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasAdditionalName

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the additional name data property

### has addressop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasAddress

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the components of the delivery address for the object

has equivalent properties

address (§4.2.1)op

has range

Address (§4.1.2)c

### has calendar busyop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasCalendarBusy

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the busy time associated with the object. (Was called FBURL in RFC6350)

### has calendar linkop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasCalendarLink

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the calendar associated with the object. (Was called CALURI in RFC6350)

### has calendar requestop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasCalendarRequest

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the calendar user address to which a scheduling request be sent for the object. (Was called CALADRURI in RFC6350)

### has categoryop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasCategory

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the category data property

### has country nameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasCountryName

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the country name data property

### has emailop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasEmail

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the electronic mail address for communication with the object

has equivalent properties

email (§4.2.3)op

has range

Email (§4.1.15)c

### has family nameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasFamilyName

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the family name data property

### has formatted nameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasFN

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the formatted name data property

### has genderop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasGender

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the sex or gender identity of the object. URIs are recommended to enable interoperable sex and gender codes to be used.

### has geoop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasGeo

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify information related to the global positioning of the object. May also be used as a property parameter.

has equivalent properties

geo (§4.2.4)op

### has given nameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasGivenName

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the given name data property

### has honorific prefixop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasHonorificPrefix

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the honorific prefix data property

### has honorific suffixop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasHonorificSuffix

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the honorific suffix data property

### has keyop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasKey

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify a public key or authentication certificate associated with the object

has equivalent properties

key (§4.2.44)op

### has languageop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasLanguage

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the language data property

### has localityop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasLocality

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the locality data property

### has logoop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasLogo

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify a graphic image of a logo associated with the object

has equivalent properties

logo (§4.2.45)op

### has memberop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasMember

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To include a member in the group this object represents. (This property can only be used by Group individuals)

has domain

Group (§4.1.21)c

has range

Kind (§4.1.28)c

### has messagingop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasInstantMessage

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the instant messaging and presence protocol communications with the object. (Was called IMPP in RFC6350)

### has nameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasName

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the components of the name of the object

has equivalent properties

name (§4.2.46)op

has range

Name (§4.1.37)c

### has nicknameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasNickname

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the nickname data property

### has noteop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasNote

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the note data property

### has organization nameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasOrganizationName

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the organization name data property

### has organization unit nameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasOrganizationUnit

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the organization unit name data property

### has photoop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasPhoto

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify an image or photograph information that annotates some aspect of the object

has equivalent properties

photo (§4.2.48)op

### has postal codeop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasPostalCode

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the postal code data property

### has regionop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasRegion

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the region data property

### has relatedop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasRelated

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify a relationship between another entity and the entity represented by this object

### has roleop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasRole

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the role data property

### has soundop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasSound

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify a digital sound content information that annotates some aspect of the object

has equivalent properties

sound (§4.2.49)op

### has sourceop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasSource

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To identify the source of directory information of the object

### has street addressop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasStreetAddress

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the street address data property

### has telephoneop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasTelephone

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the telephone number for telephony communication with the object

has equivalent properties

telephone (§4.2.50)op

### has titleop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasTitle

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to support property parameters for the title data property

### has uidop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasUID

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify a value that represents a globally unique identifier corresponding to the object

### has urlop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasURL

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify a uniform resource locator associated with the object

has equivalent properties

url (§4.2.51)op

### has valueop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#hasValue

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to indicate the resource value of an object property that requires property parameters

### keyop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#key

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has key (§4.2.20)op

### logoop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#logo

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has logo (§4.2.23)op

### nameop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#n

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has name (§4.2.26)op

### organizationop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#org

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped. Use the organization-name data property.

### photoop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#photo

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has photo (§4.2.31)op

### soundop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#sound

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has sound (§4.2.36)op

### telephoneop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#tel

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has telephone (§4.2.39)op

### urlop back to ToC or Object Property ToC (§4.2)

**IRI:** http://www.w3.org/2006/vcard/ns#url

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This object property has been mapped

has equivalent properties

has url (§4.2.42)op

## Data Properties

- additional name (§4.3.1)
- anniversary (§4.3.2)
- birth date (§4.3.3)
- category (§4.3.4)
- class (§4.3.5)
- country name (§4.3.6)
- extended address (§4.3.7)
- family name (§4.3.8)
- formatted name (§4.3.9)
- given name (§4.3.10)
- honorific prefix (§4.3.11)
- honorific suffix (§4.3.12)
- label (§4.3.13)
- language (§4.3.14)
- latitude (§4.3.15)
- locality (§4.3.16)
- longitude (§4.3.17)
- mailer (§4.3.18)
- nickname (§4.3.19)
- note (§4.3.20)
- organization name (§4.3.21)
- organizational unit name (§4.3.22)
- post office box (§4.3.23)
- postal code (§4.3.24)
- product id (§4.3.25)
- region (§4.3.26)
- revision (§4.3.27)
- role (§4.3.28)
- sort as (§4.3.29)
- street address (§4.3.30)
- time zone (§4.3.31)
- title (§4.3.32)
- value (§4.3.33)

### additional namedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#additional-name

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The additional name associated with the object

has range

xsd:string

### anniversarydp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#anniversary

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The date of marriage, or equivalent, of the object

has range

xsd:dateTime or xsd:gYear

### birth datedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#bday

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the birth date of the object

has range

xsd:dateTime or xsd:dateTimeStamp or xsd:gYear

### categorydp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#category

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The category information about the object, also known as tags

has range

xsd:string

### classdp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#class

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This data property has been deprecated

### country namedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#country-name

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The country name associated with the address of the object

has range

xsd:string

### extended addressdp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#extended-address

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This data property has been deprecated

### family namedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#family-name

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The family name associated with the object

has range

xsd:string

### formatted namedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#fn

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The formatted text corresponding to the name of the object

has range

xsd:string

### given namedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#given-name

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The given name associated with the object

has range

xsd:string

### honorific prefixdp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#honorific-prefix

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The honorific prefix of the name associated with the object

has range

xsd:string

### honorific suffixdp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#honorific-suffix

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The honorific suffix of the name associated with the object

has range

xsd:string

### labeldp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#label

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This data property has been deprecated

### languagedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#language

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the language that may be used for contacting the object. May also be used as a property parameter.

### latitudedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#latitude

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This data property has been deprecated. See hasGeo

### localitydp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#locality

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The locality (e.g. city or town) associated with the address of the object

has range

xsd:string

### longitudedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#longitude

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This data property has been deprecated. See hasGeo

### mailerdp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#mailer

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This data property has been deprecated

### nicknamedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#nickname

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The nick name associated with the object

has range

xsd:string

### notedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#note

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

A note associated with the object

has range

xsd:string

### organization namedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#organization-name

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the organizational name associated with the object

has sub-properties

organizational unit name (§4.3.22)dp

has range

xsd:string

### organizational unit namedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#organization-unit

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the organizational unit name associated with the object

has super-properties

organization name (§4.3.21)dp

has range

xsd:string

### post office boxdp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#post-office-box

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

This data property has been deprecated

### postal codedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#postal-code

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The postal code associated with the address of the object

has range

xsd:string

### product iddp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#prodid

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the identifier for the product that created the object

has range

xsd:string

### regiondp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#region

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The region (e.g. state or province) associated with the address of the object

has range

xsd:string

### revisiondp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#rev

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify revision information about the object

has range

xsd:dateTime

### roledp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#role

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the function or part played in a particular situation by the object

has range

xsd:string

### sort asdp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#sort-string

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the string to be used for national-language-specific sorting. Used as a property parameter only.

has range

xsd:string

### street addressdp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#street-address

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

The street address associated with the address of the object

has range

xsd:string

### time zonedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#tz

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To indicate time zone information that is specific to the object. May also be used as a property parameter.

has range

xsd:string

### titledp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#title

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

To specify the position or job of the object

has range

xsd:string

### valuedp back to ToC or Data Property ToC (§4.3)

**IRI:** http://www.w3.org/2006/vcard/ns#value

is defined by

[http://www.w3.org/2006/vcard/ns](https://www.w3.org/2006/vcard/ns)

Used to indicate the literal value of a data property that requires property parameters

## Namespace Declarations back to ToC

*default namespace*

http://www.w3.org/2006/vcard/ns#

owl

http://www.w3.org/2002/07/owl#

rdf

http://www.w3.org/1999/02/22-rdf-syntax-ns#

rdfs

http://www.w3.org/2000/01/rdf-schema#

vcard

http://www.w3.org/2006/vcard/

xsd

http://www.w3.org/2001/XMLSchema#

## A. Change History

Changes since Previous Version ([Working Draft 24 Sept 2013](https://www.w3.org/TR/2013/WD-vcard-rdf-20130924/))

- Updated the examples of RDFa, Turtle and JSON-LD in section 3 (vcard:hasValue has a literal value which should be a URI as an ObjectProperty)
- Updated JSON text and link to JSON-LD schema at Namespace URI
- Added lang (en) to all labels and comments also add a rdfs:definedBy pointing the ontology itself to every concept
- Removed the deprecated statements, added comment that they have consistently named equivalents, along with equivalentProperty/equivalentClass axioms (only deprecate concpets no longer in RFC6350)
- Added gYear to range for birthdate and anniversary.

## B. Acknowledgements

Thanks to member of the W3C Semantic Web Interest Group and the IETF vCard
Working Group for valuable feedback and suggestions; Dan Brickley, Ivan Herman, Michael Angstadt, Adrian Pohl, Dave Reynolds, Brian McBride, Martin Hepp, and Shahim Essaid.

Special thanks to Masahide Kanzaki for feedback on the OWL Ontology and Markus Lanthaler for providing the JSON-LD schema.

The ontology HTML section was obtained by processing the OWL ontology source
code through [LODE](http://lode.sourceforge.net), *Live OWL Documentation
Environment*, developed by [Silvio Peroni](http://palindrom.es/phd/whoami/).

## C. References

[RFC6350]

vCard Format Specification. IETF RFC 6350, August 2011 <http://tools.ietf.org/html/rfc6350>

[RFC2426]

vCard MIME Directory Profile. IETF RFC 2426, September 1998 <http://tools.ietf.org/html/rfc2426>

[VCARD-MEMBER]

Representing vCard Objects in RDF. W3C Member Submission, 20 January 2010 [http://www.w3.org/Submission/2010/SUBM-vcard-rdf-20100120/](https://www.w3.org/Submission/2010/SUBM-vcard-rdf-20100120/)
