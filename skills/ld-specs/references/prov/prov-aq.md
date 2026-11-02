---
title: "PROV-AQ: Provenance Access and Query"
source: https://www.w3.org/TR/prov-aq/
family: prov
spec_date: 2013-04-30
fetched: 2026-11-02
---

# PROV-AQ: Provenance Access and Query

> Locating and querying provenance on the web.

## Contents

- Abstract
- 1 Introduction
  - 1.1 Concepts
  - 1.2 Provenance and resources
  - 1.3 Interpreting provenance records
  - 1.4 URI types and dereferencing
- 2 Accessing provenance records
- 3 Locating provenance records
  - 3.1 Resource accessed by HTTP
    - 3.1.1 Specifying Provenance Query Services
    - 3.1.2 Content negotiation, redirection and Link: headers
  - 3.2 Resource represented as HTML
    - 3.2.1 Specifying Provenance Query Services
  - 3.3 Resource represented as RDF
- 4 Provenance query services
  - 4.1 Provenance query service description
    - 4.1.1 Direct HTTP query service description
    - 4.1.2 SPARQL query service description
    - 4.1.3 Service description example
  - 4.2 Direct HTTP query service invocation
  - 4.3 Provenance query service discovery
- 5 Provenance pingback
- 6 Security considerations
- B Terms added to prov: namespace
- C References
  - C.1 Informative references

---

## Abstract

This document specifies how to use standard Web protocols,
including HTTP, to obtain information about the provenance of
resources on the Web. We describe both simple access mechanisms for
locating provenance records associated with web pages or resources, and
provenance query services for more complex deployments. This is
part of the larger W3C PROV provenance family of documents.

The [PROV Document Overview](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/) describes the overall state of PROV, and should be read before other PROV documents.

## 1. Introduction

The Provenance Data Model [PROV-DM], Provenance Ontology [PROV-O] and related specifications define how to represent provenance on the World Wide Web (see the [PROV-OVERVIEW]).

This note describes how standard web protocols may be used to locate, retrieve and query provenance records:

- Simple mechanisms for retrieving and discovering provenance records are described in section 2. Accessing provenance records (§2) and section 3. Locating provenance records (§3) .
- Provenance query mechanisms that may be used for more demanding deployments are described in section 4. Provenance query services (§4).
- A simple "ping-back" mechanism allowing for discovery of additional provenance that would otherwise be unknown to the publisher of the resource (e.g. provenance about future entities that are based upon or influenced by a resource) is described in section 5. Provenance pingback (§5).

Most mechanisms described in this note are independent of the provenance format used, and may be used to access provenance in any available format. For interoperable provenance publication, use of PROV represented in any of its specified formats is recommended. Where alternative formats are available, selection may be made by HTTP content negotiation [HTTP11].

For ease of reference, the main body of this document contains some links to external web pages. Such links are distinguished from internal references thus: [W3C Provenance Working Group](https://www.w3.org/2011/prov/wiki/Main_Page).

This document is a W3C Note, not a formal W3C Specification. However, to clarify the description of intended behaviours, it does use the key words *MUST*, *MUST NOT*, *REQUIRED*, *SHOULD*, *SHOULD NOT*, *RECOMMENDED*, *MAY* and *OPTIONAL* as described in [RFC2119].

### 1.1 Concepts

This document uses the term URI for web resource identifiers, as this is the term used in many of the currently ratified specifications that this document builds upon. In many situations, a URI may also be an IRI [RFC3987], which is a generalisation of a URI allowing a wider range of Unicode characters. Every absolute URI is an IRI, but not every IRI is an URI. When IRIs are used in situations that require a URI, they must first be converted according to the mapping defined in section 3.1 of [RFC3987]. A notable example is retrieval over the HTTP protocol. The mapping involves UTF-8 encoding of non-ASCII characters, %-encoding of octets not allowed in URIs, and Punycode-encoding of domain names.

In defining the specification below, we make use of the following concepts.

*Resource*

a resource in the general sense of "whatever might be identified by a URI", as described by the Architecture of the World Wide Web [WEBARCH], [section 2.2](https://www.w3.org/TR/webarch/#id-resources). A resource may be associated with multiple instances or views (constrained resources) with differing provenance.

*Constrained resource*

a specialization (e.g. an aspect, version or instance) of a resource, about which one may wish to present provenance records. For example, a weather report for a given date may be an aspect of a resource that is maintained as the current weather report. A constrained resource is itself a resource, and may have its own URI different from that of the original. See also section 1.2 Provenance and resources (§1.2), [PROV-DM] [section 5.5.1](https://www.w3.org/TR/prov-dm/#term-specialization), and [WEBARCH] [section 2.3.2](https://www.w3.org/TR/webarch/#representation-reuse).

*Target-URI*

a URI denoting a resource (including any constrained resource), and which identifies that resource for the purpose of expressing provenance. Such a resource is typically an [entity](https://www.w3.org/TR/prov-dm/#section-entity-activity) in the sense of [PROV-DM], but may be something else described by provenance records, such as an [activity](https://www.w3.org/TR/prov-dm/#section-entity-activity).

*Provenance record*

refers to provenance represented in some fashion.

*Provenance-URI*

a URI denoting some provenance record.

*Provenance query service*

a service that accesses provenance given a query containing a target-URI or other information that identifies the desired provenance.

*Service-URI*

the URI of a provenance query service.

*Pingback-URI*

the URI of a provenance pingback service that can receive references to additional provenance related to an entity.

*Accessing* provenance records

given the identity of a resource, the process of discovering and retrieving some provenance record(s) about that resource. This may involve locating a provenance record, then performing an HTTP GET to retrieve it, or locating and using a query service for provenance about an identified resource, or some other mechanism not covered in this document.

*Locating* provenance records

given the identity of a resource, discovery of a provenance-URI or a service-URI that may be used to obtain a provenance record about that resource.

provenance *provider*

is an agent that makes available provenance records.

provenance *consumer*

is an agent that receives and interprets provenance records.

### 1.2 Provenance and resources

Fundamentally, a provenance record is *about* resources.
In general, resources may vary over time and context. E.g., a resource describing the weather in London changes from day-to-day, or a listing of restaurants near you will vary depending on your location.

Provenance records a history of the entities, activities, and people involved in producing an artifact, and may be collected from several sources at different times [PROV-DM]. In order to create a meaningful history, the individual provenance records used must retain their intended meaning when interpreted in a context other than that in which they were collected.
Yet, we may still want to make provenance assertions about dynamic or context-dependent resources (e.g. a weather forecast for London on a particular day may have been derived from a particular set of Meteorological Office data).

Provenance records for dynamic and context-dependent resources are possible through a notion of constrained resources. A constrained resource is simply a resource (in the sense defined by [WEBARCH], [section 2.2](https://www.w3.org/TR/webarch/#id-resources)) that is a specialization or instance of some other resource. For example, a W3C specification typically undergoes several public revisions before it is finalized. A URI that refers to the "current" revision might be thought of as denoting the specification throughout its lifetime. Each individual revision would also have its own target-URI denoting the specification at that particular stage in its development. Using these, we can make provenance assertions that a particular revision was published on a particular date, and was last modified by a particular editor. Target-URIs may use any URI scheme, and are not required to be dereferencable.

Requests for provenance about a resource may return provenance records that use one or more target-URIs to refer to versions of that resource, such as when there are assertions referring to the same underlying resource in different contexts. For example, a provenance record for a W3C document might include information about all revisions of the document using statements that use the different target-URIs of the various revisions.

These ideas are represented in the provenance data model [PROV-DM] by the concepts [entity](https://www.w3.org/TR/prov-dm/#term-entity) and [specialization](https://www.w3.org/TR/prov-dm/#term-specialization). In particular, an entity may be a specialization of some resource whose "fixed aspects" provide sufficient constraint for expressed provenance about the resource to be invariant with respect to that entity. This entity is itself just another resource (e.g. the weather forecast for a give date as opposed to the current weather forecast), with its own URI for referring to it within a provenance record.

### 1.3 Interpreting provenance records

The mechanisms described in this document are intended to allow a provider to supply information that allows a consumer to access provenance records, which themselves explicitly identify the [entities](https://www.w3.org/TR/prov-dm/#term-entity) they describe.
A provenance record may contain information about several entities, referring to them using their various target-URIs.
Thus, a consumer should be selective in its use of the information provided when interpreting a provenance record.

A provenance record consumer will need to isolate information about the specific entity or entities of interest. These may be constrained resources identified by separate target-URIs that differ from the resource URI, in which case the consumer needs to discover those target-URIs. The mechanisms defined later allow a provider to expose such URIs.

While a provider should avoid giving spurious information, there are no fixed semantics, particularly when multiple resources are indicated, and a client should not assume that a specific given provenance-URI will yield information about a specific target-URI. In the general case, a client presented with multiple provenance-URIs and multiple target-URIs should look at all of the provenance-URIs for information about any or all of the target-URIs.

A provenance record is not of itself guaranteed to be authoritative or correct. Trust in provenance records must be determined separately from trust in the original resource. Just as in the web at large, it is a user's responsibility to determine an appropriate level of trust in any other resource; e.g. based on the domain that serves it, or an associated digital signature. (See also section 6. Security considerations (§6).)

### 1.4 URI types and dereferencing

A number of resource types are described above in section 1.1 Concepts (§1.1). The table below summarizes what these various URIs are intended to denote, and the kind of information that should be returned if they are dereferenced:

|                                                                     | Denotes                                                                                                                                                                                                  | Dereferences to                                                                                                                                                                                          |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Target-URI         | Any resource that is described by some provenance - typically an [entity](https://www.w3.org/TR/prov-dm/#section-entity-activity) (in the sense of [PROV-DM]), but may be of another type (such as [PROV-DM] activity). | Not specified (the URI is not even required to be dereferencable).                                                                                                                                       |
| Provenance-URI | A provenance record, or provenance description, in the sense described by [PROV-DM] ([PROV Overview](https://www.w3.org/TR/prov-dm/#section-prov-overview)). | A provenance record in any defined format, selectable via content negotiation.                                                                                                                           |
| Service-URI       | A provenance query service. The service-URI is the initial URI used when accessing a provenance query service; following REST API style [REST-APIs], URIs for accessing provenance are determined via the service description. | A provenance query service description per section 4.1 Provenance query service description (§4.1). Alternative formats may be offered via HTTP content negotiation. |
| Pingback-URI     | A provenance pingback service. This is a service to which provenance pingback information can be submitted using an HTTP POST operation per section 5. Provenance pingback (§5). No other operations are specified. | None specified (the owner of a provenance pingback URI may choose to return useful information, but is not required to do so.)                                                                           |

## 2. Accessing provenance records

This specification describes two ways to access provenance records:

1. Direct access: given a provenance-URI, simply dereference it, and
2. Indirectly via a query service: given the URIs of some resource (or maybe other information) and a provenance query service, use the service to access provenance of the resource.

Web applications may access a provenance record in the same way as any resource on the Web, by dereferencing its URI (commonly using an HTTP GET operation). Thus, any provenance record may be associated with a provenance-URI, and may be accessed by dereferencing that URI using web mechanisms.
How much or how little provenance is returned in a provenance record is a matter for the provider, taking account that a provenance trace may extend as linked data across multiple provenance records.

When there is no easy way to associate a provenance-URI with a resource (e.g. for resources not directly web-accessible, or whose publication mechanism is controlled by someone else), a provenance description may be obtained using a provenance query service at an indicated service-uri.
A REST protocol for provenance queries is defined in Section section 4. Provenance query services (§4); also described there is a mechanism for locating a SPARQL query service [SPARQL-SD].

When publishing provenance, corresponding provenance-URIs or service-URIs should be discoverable using one or more of the mechanisms described in section 3. Locating provenance records (§3).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Provenance may be presented as a [bundle](https://www.w3.org/TR/prov-dm/#component4), which is "a named set of provenance descriptions, and is itself an entity, so allowing provenance of provenance to be expressed" [PROV-DM]. A provenance description at a dereferencable provenance-URI may be treated as a bundle, and this is a good way to make provenance easily accessible. But there are other possible implementations of a bundle, such as a named graph in an RDF dataset [RDF-CONCEPTS11], for which the bundle URI may not be directly dereferencable.
>
> When a bundle is published as part of an RDF Dataset, to access it would require accessing the RDF Dataset and then extracting the identified graph component; this in turn would require knowing a URI or some other way to retrieve the RDF dataset. This specification does not describe a specific mechanism for extracting components from a document containing multiple graphs.
>
> The W3C Linked Data Platform group ([www.w3.org/2012/ldp/](https://www.w3.org/2012/ldp/)) is chartered to produce a W3C Recommendation for HTTP-based (RESTful) application integration patterns using read/write Linked Data; we anticipate that they may address access to RDF Datasets in due course.

## 3. Locating provenance records

A provenance record can be accessed using direct web retrieval, given its provenance-URI. If this is known in advance, there is nothing more to specify. If a provenance-URI is not known then a mechanism to discover one must be based on information that is available to the would-be accessor. Likewise, provenance may be exposed by a query service, in which case, the corresponding service-URI must be discovered.

Three mechanisms are defined for a provenance consumer to find information about a provenance-URI or service-URI, along with a target-URI:

1. The consumer knows the resource URI *and* the resource is accessible using HTTP
2. The consumer has a copy of a resource represented as HTML or XHTML
3. The consumer has a copy of a resource represented as RDF (including the range of possible RDF syntaxes, such as HTML with embedded RDFa)

These particular cases are selected as corresponding to current primary web protocol and data formats. Similar approaches may be defined for other protocols or resource formats.

Provenance records may be offered by several providers other than that of the original resource publisher, each with different concerns, and presenting provenance at different locations. It is possible that these different providers may present contradictory provenance.

### 3.1 Resource accessed by HTTP

For a resource accessible using HTTP, a provenance record may be indicated using an HTTP `Link` header field, as defined by [Web Linking (RFC 5988)](http://tools.ietf.org/html/rfc5988#section-5) [LINK-REL]. The `Link` header field is included in the HTTP response to a GET or HEAD operation (other HTTP operations are not excluded, but are not considered here).

A `has_provenance` link relation type for referencing a provenance record may be used thus:

```
Link: <provenance-URI>;
  rel="http://www.w3.org/ns/prov#has_provenance";
  anchor="target-URI"
```

When used in conjunction with an HTTP success response code (`2xx`), this HTTP header field indicates that `provenance-URI` is the URI of a provenance record about the originally requested resource, and that the requested resource is identified within the provenance record as `target-URI`. (See also section 1.3 Interpreting provenance records (§1.3).)

If no `anchor` parameter is provided then the `target-URI` is assumed to be the URI of the requested resource used in the corresponding HTTP request.

This note does not define the meaning of these links returned with other HTTP response codes: future revisions may define interpretations for these.

An HTTP response *MAY* include multiple `has_provenance` link header fields, indicating a number of different provenance resources (and anchors) that are known to the responding server, each referencing a provenance record about the accessed resource.

The presence of a `has_provenance` link in an HTTP response does not preclude the possibility that other providers also may offer provenance records about the same resource. In such cases, discovery of the additional provenance records must use other means (e.g. see section 4. Provenance query services (§4)).

An example HTTP response including provenance headers might look like this (where `C:` and `S:` prefixes indicate client and server emitted data respectively):
> **Example:**
>
> > **Example:**
> >
> > Example 1
>
> ```
> C: GET http://example.com/resource123/ HTTP/1.1
> C: Accept: text/html
>
> S: HTTP/1.1 200 OK
> S: Content-type: text/html
> S: Link: <http://example.com/resource123/provenance/>;
>          rel="http://www.w3.org/ns/prov#has_provenance";
>          anchor="http://example.com/resource123/"
> S:
> S: <html ...>
> S:  :
> S: </html>
> ```

#### 3.1.1 Specifying Provenance Query Services

The resource provider may indicate that provenance records about the resource are provided by a provenance query service. This is done through the use of a `has_query_service` link relation type following the same pattern as above:

```
Link: <service-URI>;
  rel="http://www.w3.org/ns/prov#has_query_service";
  anchor="target-URI"
```

The `has_query_service` link identifies the service-URI. Dereferencing this URI yields a service description that provides further information to enable a client to submit a query to retrieve a provenance record for a resource; see section 4. Provenance query services (§4) for more details.
> **Example:**
>
> > **Example:**
> >
> > Example 2
>
> ```
> C: GET http://example.com/resource123/ HTTP/1.1
> C: Accept: text/html
>
> S: HTTP/1.1 200 OK
> S: Content-type: text/html
> S: Link: <http://example.com/resource123/provenance-query/>;
>          rel="http://www.w3.org/ns/prov#has_query_service";
>          anchor="http://example.com/resource123/"
> S:
> S: <html ...>
> S:  :
> S: </html>
> ```

There *MAY* be multiple `has_query_service` link header fields, and these *MAY* appear in an HTTP response together with `has_provenance` link header fields.

#### 3.1.2 Content negotiation, redirection and Link: headers

When performing content negotiation for a resource, it is common for HTTP 302 or 303 redirect response codes to be used to direct a client to an appropriately-formatted resource. When accessing a resource for which provenance is available, link headers *SHOULD* be included with the response to the final redirected request, and not on the intermediate 303 responses. (When accessing a resource from a browser using Javascript, the intermediate 303 responses are usually handled transparently by the browser and are not visible to the HTTP client code.)

Following content negotiation, any provenance link returned refers to the resource whose URI is used in the corresponding HTTP request, or the given anchor parameter if that is different.

An example transaction using content negotiation and redirection might look like this (where `C:` and `S:` prefixes indicate client and server emitted data respectively):
> **Example:**
>
> > **Example:**
> >
> > Example 3
>
> ```
> C: GET http://example.com/resource123/ HTTP/1.1
> C: Accept: text/html
>
> S: HTTP/1.1 302 Found
> S: Location: /resource123/content.html
> S: Vary: Accept
> S:
> S: HTML content for http://example.com/resource123/
> S: is available at http://example.com/resource123/content.html
>
> C: GET http://example.com/resource123/content.html HTTP/1.1
> C: Accept: text/html
>
> S: HTTP/1.1 200 OK
> S: Content-type: text/html
> S: Link: <http://example.com/resource123/provenance/>;
>          rel="http://www.w3.org/ns/prov#has_provenance";
>          anchor="http://example.com/resource123/20130226/content.html"
> S:
> S: <html>
> S:  <!-- HTML content here... -->
> S: </html>
> ```

This example indicates a provenance record at `http://example.com/resource123/provenance/`, which uses `http://example.com/resource123/20130226/content.html` as the target-URI for the requested resource. If the `anchor=` parameter were to be omitted from the `Link` header field, the indicated target-URI would be `http://example.com/resource123/content.html`.

### 3.2 Resource represented as HTML

For a document presented as HTML or XHTML, without regard for how it has been obtained, a provenance record may be associated with a resource by adding a `<link>` element to the HTML `<head>` section.
Two link relation types for referencing provenance may be used:

```
  <html>
     <head>
        <link rel="http://www.w3.org/ns/prov#has_provenance" href="provenance-URI">
        <link rel="http://www.w3.org/ns/prov#has_anchor" href="target-URI">
        <title>Welcome to example.com</title>
     </head>
     <body>
       <!-- HTML content here... -->
     </body>
  </html>
```

The `provenance-URI` given by the first link element (`#has_provenance` ) identifies the provenance-URI for the document.

The `target-URI` given by the second link element (`#has_anchor`) specifies an identifier for the document that may be used within the provenance record when referring to the document.

If no `target-URI` is provided (via a `#has_anchor` link element) then is it is assumed to be the URI of the document. It is *RECOMMENDED* that this convention be used only when the document has a URI that is reasonably expected to be known or easily discoverable by a consumer of the document (e.g. when delivered from a web server, or as part of a MIME structure containing content identifiers [RFC2392]).

An HTML document header *MAY* present multiple `provenance-URI`s over several `#has_provenance` link elements, indicating a number of different provenance records that are known to the publisher of the document, each of which may provide provenance about the document (see section 1.3 Interpreting provenance records (§1.3)).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The mechanisms used with HTTP and HTML/RDF are slightly inconsistent in their approach to specifying `target-URI` values. In HTTP `Link` header fields, an optional `anchor=` parameter may be supplied for each such header. In HTML and RDF, separate `#has_anchor` relations are defined. It was felt that avoiding reinvention of existing mechanisms was more important than being completely consistent. If anchors are processed as described in section 1.3 Interpreting provenance records (§1.3) (3rd paragraph), observable behaviour across all approaches should be consistent.

#### 3.2.1 Specifying Provenance Query Services

The document creator may specify that the provenance about the document is provided by a provenance query service. This is done through the use of a third link relation type following the same pattern as above:

```
  <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
        <link rel="http://www.w3.org/ns/prov#has_query_service" href="service-URI">
        <link rel="http://www.w3.org/ns/prov#has_anchor" href="target-URI">
        <title>Welcome to example.com</title>
     </head>
     <body>
       <!-- HTML content here... -->
     </body>
  </html>
```

The `has_query_service` link element identifies the service-URI. Dereferencing this URI yields a service description that provides further information to enable a client to query for provenance about a resource; see section 4. Provenance query services (§4) for more details.

There *MAY* be multiple `#has_query_service` link elements, and these *MAY* appear in the same document as `#has_provenance` link elements (though we do not anticipate that `#has_provenance` and `#has_query_service` link relations will commonly be used together).

### 3.3 Resource represented as RDF

If a resource is represented as RDF (in any of its recognized syntaxes, including RDFa), it may contain references to its own provenance using additional RDF statements.
For this purpose, the link relations introduced above (section 3. Locating provenance records (§3)) may be used as RDF properties: `prov:has_provenance`, `prov:has_anchor`, and `prov:has_query_service`, where the `prov:` prefix here indicates the PROV namespace URI `http://www.w3.org/ns/prov#`.

The RDF property `prov:has_provenance` is a relation between two resources, where the object of the property is a provenance-URI that denotes a provenance record about the subject resource. Multiple `prov:has_provenance` assertions may be made about a subject resource.

Property `prov:has_anchor` specifies a target-URI used in the indicated provenance to refer to the containing RDF document.

Property `prov:has_query_service` specifies a service-URI for provenance queries.
> **Example:**
>
> > **Example:**
> >
> > Example 4
>
> ```
> @prefix prov: <http://www.w3.org/ns/prov#>.
>
> <> dcterms:title        "Welcome to example.com" ;
>    prov:has_anchor       <http://example.com/data/resource.rdf> ;
>    prov:has_provenance   <http://example.com/provenance/resource.rdf> ;
>    prov:has_query_service <http://example.com/provenance-query-service/> .
>
>    # (More RDF data ...)
> ```

(The above example uses Turtle RDF syntax [TURTLE].)
> **Note:**
>
> > **Note:**
> >
> > Note
>
> These terms (`prov:has_provenance`, `prov:has_anchor`, and `prov:has_query_service`) may be also used in RDF statements with other subjects to indicate provenance of other resources, but discussion of such use is beyond the scope of this document.
>
> See also the note about target-URIs at the end of section 3.2 Resource represented as HTML (§3.2).

## 4. Provenance query services

This section describes a simple HTTP query protocol for accessing provenance records, and also a mechanism for locating a SPARQL service endpoint [SPARQL-SD]. The HTTP query protocol specifies HTTP operations [HTTP11] for retrieving provenance records from a provenance query service, following the approach of the SPARQL Graph Store HTTP Protocol [SPARQL-HTTP].

The introduction of query services is motivated by the following possible considerations:

- third-party providers of provenance descriptions may be unable to use the mechanisms of Section 3 because the corresponding target-URI is outside their control;
- services unknown to the original publisher may have provenance records about the same resource;
- there is no known dereferencable provenance-URI or a particular entity;
- query services may provide additional filters over what provenance is returned; and
- query services may support more expressive selections, such as "which
  entities were derived from entities attributed to agent X".

The patterns for using provenance query services are designed around REST principles [REST], which aim to minimize coupling between client and server implementation details.

The query mechanisms provided by a provenance query service are described by a service description, which is obtained by dereferencing a service-URI. A service description may contain information about additional mechanisms that are not described here. In keeping with REST practice for web applications, alternative service descriptions using different formats may be offered and accessed using HTTP content negotiation. We describe below a service description format that uses RDF to describe two query mechanisms.

The general procedure for using a provenance query service is:

1. retrieve the service description;
2. within the service description, locate information about a recognized query mechanism (ignoring unrecognized descriptions if the description covers multiple service options);
3. if a recognized query mechanism is found, extract information needed to use that mechanism (e.g. a URI template or a SPARQL service endpoint URI); and
4. use the information obtained to query for required provenance, using the selected query mechanism.

The remainder of this section covers the following topics:

- section 4.1 Provenance query service description (§4.1) - describes an RDF-based service description format and vocabularies to convey information about direct HTTP query and/or SPARQL service options.
  * section 4.1.1 Direct HTTP query service description (§4.1.1) - RDF structure for describing a direct HTTP query service.
  * section 4.1.2 SPARQL query service description (§4.1.2) - RDF structure for describing a SPARQL query service.
- section 4.2 Direct HTTP query service invocation (§4.2) - describes how to perform a direct HTTP query for provenance, using information obtained from the service description.
- section 4.3 Provenance query service discovery (§4.3) - briefly discusses some possible approaches to discovery of provenance query services.

### 4.1 Provenance query service description

Dereferencing a service-URI yields a service description. The service description may be in any format selectable through content negotiation, and it may contain descriptions of one or more available query mechanisms. The format described here uses RDF, serialized as Turtle [TURTLE], but any selectable RDF serialization could be used. In this RDF service description, each query mechanism is associated with an RDF type, as explained below.

The overall structure of a service description is as follows:

```
<service-URI> a prov:ServiceDescription ;
    prov:describesService <direct-query-description>, <sparql-query-description> .

<direct-query-description> a prov:DirectQueryService ;
  prov:provenanceUriTemplate "direct-query-template"
  .

<sparql-query-description> a sd:Service ;
  sd:endpoint <sparql-query> ;
  # other details...
  .
```

We see here that the `service-URI` identifies a resource of type `prov:ServiceDescription`, which collects descriptions of one or more provenance query mechanisms. Each associated mechanism is indicated by a `prov:describesService` statement.

#### 4.1.1 Direct HTTP query service description

A direct HTTP query service is described by an RDF resource of type `prov:DirectQueryService`.
It allows for accessing provenance about a specified target-URI. The query URI to use is described by a URI Template [URI-template] (level 2 or above) in which the variable `uri` stands for the target-URI. The URI template is specified as:

```
<direct-query-description> a prov:DirectQueryService ;
  prov:provenanceUriTemplate "uri-template" .
```

where `direct-query-description` is any distinct RDF subject node (i.e. a blank node or a URI), and `uri-template` is a URI template [RFC3986].

The URI template indicated by `prov:provenanceUriTemplate` may expand to an absolute or relative URI reference. A URI for the desired provenance record is obtained by expanding the URI template with the variable `uri` set to the target-URI for which provenance is requested. In this example, if the target-URI contains '#' or '&' these must be %-escaped as `%23` or `%26` respectively before template expansion [RFC3986]. If the result is a relative reference, it is interpreted per [RFC3986] (section 5.2) using the URI of the service description as its base URI (which is generally the same as the query service-URI, unless HTTP redirection has been invoked).
> **Example:**
>
> > **Example:**
> >
> > Example 5
>
> ```
> <http://example.com/prov/service> a prov:ServiceDescription;
>     prov:describesService _:direct .
>
> _:direct a prov:DirectQueryService ;
>   prov:provenanceUriTemplate
>     "http://www.example.com/provenance/service?target={uri}" .
> ```

A provenance query service *MAY* recognize additional parameters encoded as part of a URI for the provenance record. If it does, it *SHOULD* include these in the provenance URI template in the service description, so that clients may discover how a URI is formed using this additional information.
For example, a query service might offer to include just the immediate provenance of a target, or to also supply provenance of other resources from which the target is derived. Suppose a service accepts an additional parameter `steps` that defines the number of previous steps to include in a provenance trace, it might publish its service description thus:
> **Example:**
>
> > **Example:**
> >
> > Example 6
>
> ```
> <http://example.com/prov/service> a prov:ServiceDescription;
>     prov:describesService _:direct .
>
> _:direct a prov:DirectQueryService ;
>   prov:provenanceUriTemplate
>     "http://www.example.com/provenance/service?target={uri}{&steps}" .
> ```

(Note that in this case, a "level 3" URI template feature is used [URI-template].)

Section section 4.2 Direct HTTP query service invocation (§4.2) discusses how a client interacts with a direct HTTP query service.

#### 4.1.2 SPARQL query service description

A SPARQL query service is described by an RDF resource of type `sd:Service` [SPARQL-SD].

It allows for accessing provenance information using a SPARQL query, which may be constructed to retrieve provenance for a particular resource, or for multiple resources. The query may be formulated using the PROV-O vocabulary terms [PROV-O], and others supported by the SPARQL endpoint as appropriate.

The SPARQL query service description is constructed as defined by SPARQL 1.1 Service Description [SPARQL-SD]; e.g.
> **Example:**
>
> > **Example:**
> >
> > Example 7
>
> ```
> <http://example.com/prov/service> a prov:ServiceDescription;
>     prov:describesService _:sparql .
>
> _:sparql a sd:Service ;
>     sd:endpoint <http://www.example.com/provenance/sparql> ;
>     sd:supportedLanguage sd:SPARQL11Query .
> ```

where `http://www.example.com/provenance/sparql` is the URI of a provenance query SPARQL endpoint.

The SPARQL service description may be detailed or sparse, provided that it includes at least a `sd:endpoint` statement with the SPARQL service endpoint URI.

The endpoint may be given as an absolute or relative URI reference. If a relative reference is given, it is interpreted in the normal way for the RDF format used, which will commonly be relative to the URI of the service document itself.

#### 4.1.3 Service description example

The following service description example uses Turtle [TURTLE] syntax to describe both direct HTTP and SPARQL query services:
> **Example:**
>
> > **Example:**
> >
> > Example 8
>
> ```
> @prefix prov:    <http://www.w3c.org/ns/prov#> .
> @prefix dcterms: <http://purl.org/dc/terms/> .
> @prefix foaf:    <http://xmlns.com/foaf/0.1/> .
> @prefix sd:      <http://www.w3.org/ns/sparql-service-description#> .
>
> <> a prov:ServiceDescription ;
>     prov:describesService <#direct>, <#sparql> ;
>     dcterms:publisher <#us>
>     .
>
> <#us> a foaf:Organization ;
>     foaf:name "and not a service!"
>     .
>
> <#direct> a prov:DirectQueryService ;
>     prov:provenanceUriTemplate "/direct?target={+uri}"
>     .
>
> <#sparql> a sd:Service ;
>     sd:endpoint </sparql/> ;
>     sd:supportedLanguage sd:SPARQL11Query ;
>     sd:resultFormat <http://www.w3.org/ns/formats/RDF_XML> ,
>                     <http://www.w3.org/ns/formats/Turtle> ,
>                     <http://www.w3.org/ns/formats/SPARQL_Results_XML> ,
>                     <http://www.w3.org/ns/formats/SPARQL_Results_JSON> ,
>                     <http://www.w3.org/ns/formats/SPARQL_Results_CSV> ,
>                     <http://www.w3.org/ns/formats/SPARQL_Results_TSV>
>     .
> ```

### 4.2 Direct HTTP query service invocation

This section describes the interaction between a client and a direct HTTP query service whose service description is as presented in section 4.1.1 Direct HTTP query service description (§4.1.1), once the service description has been analyzed and its URI template has been extracted.

The target-URI for which provenance is required is used in the expansion of the supplied URI template [RFC3986] to formulate an HTTP GET request.

Thus, in the first service description example in section 4.1.1 Direct HTTP query service description (§4.1.1), the URI template is `http://www.example.com/provenance/service?target={uri}`. If the supplied target-URI is `http://www.example.com/entity123`, this would be used as the value for variable `uri` when expanding the template. The resulting HTTP request used to retrieve a provenance record would be:
> **Example:**
>
> > **Example:**
> >
> > Example 9
>
> ```
> GET /provenance/service?target=http%3A%2F%2Fwww.example.com%2Fentity123 HTTP/1.1
> Host: example.com
> ```

Any server that implements this protocol and receives a request URI in a form corresponding to its published URI template *SHOULD* return a provenance record for the embedded target-URI. The target-URI is obtained by percent-decoding [RFC3986] the part of the request URI corresponding to occurrences of the variable `uri` in the URI template. E.g., in the above example, the decoded target-URI is `http://www.example.com/entity123`. The target-URI *MUST* be an absolute URI, and the server *SHOULD* respond with `400 Bad Request` if it is not.

A server *SHOULD NOT* offer a template containing `{+uri}` or other non-simple variable expansion options [URI-template] unless all valid target-URIs for which it can provide provenance do not contain problematic characters like `'#'` or `'&'`.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The defined URI template expansion process [URI-template] generally takes care of %-escaping characters that are not permitted in URIs. However, when expanding a template with `{+uri}` (or other non-simple variable expansion options), some permitted characters such as `'#'` and `'&'` are not escaped. If the supplied target-URI contains these characters, then they may disrupt interpretation of the resulting query URI. A generally more reliable approach is to use `{uri}` in the URI template string, which will cause all URI-reserved characters to be %-escaped as part of the URI-template expansion, as in the example above.

If the provenance described by the request is unknown to the server, a suitable error response code *SHOULD* be returned. In the absence of any security of privacy concerns about the resource, that might be `404 Not Found`. But if the existence or non-existence of a resource is considered private or sensitive, an authorization failure or other response may be returned.

The direct HTTP query service may return provenance in any available format.
For interoperable provenance publication, use of PROV represented in any of its specified formats is recommended. Where alternative formats are available, selection may be made by content negotiation, using `Accept:` header fields in the HTTP request.
Services *MUST* identify the `Content-Type` of the provenance returned.

Additional URI query parameters may be used as indicated by the service description in section 4.1.1 Direct HTTP query service description (§4.1.1). The second service description example specifies a URI template with an additional variable which may be used to control the scope of provenance information returned: `http://www.example.com/provenance/service?target={+uri}{&steps}`. Following [RFC3986], if no value for variable `steps` is provided when expanding the template, this extra element is effectively ignored. But if a `steps` value of (say) `2` is provided, then the resulting HTTP query would be:
> **Example:**
>
> > **Example:**
> >
> > Example 10
>
> ```
> GET http://example.com/provenance/service?target=http://www.example.com/entity&steps=2 HTTP/1.1
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The use of any specific URI template variable other than `uri` for the target-URI is a matter for agreement between the client and query service, and is not specified in this note. It is mentioned here simply to show that the possibility exists to formulate more detailed queries.

### 4.3 Provenance query service discovery

Previously, section 3. Locating provenance records (§3) has described use of HTTP `Link:` header fields, HTML `<link>` elements and RDF statements to indicate provenance query services. Beyond that, this specification does not define any specific mechanism for discovering query services. Applications may use any appropriate mechanism, including but not limited to: prior configuration, search engines, service registries, etc.

To facilitate service discovery, we recommend that RDF publication of dataset and service descriptions use the property `prov:has_query_service` and the provenance service type `prov:ServiceDescription` as appropriate (see the appendix section B. (§B) ).

For example, a VoID description [VoID] of a dataset might indicate a provenance query service providing information about that dataset:

```
  <http://example.org/dataset/> a void:Dataset ;
    prov:has_query_service <http://example.org/provenance/> .
```

The RDF service description example in section 4.1.3 Service description example (§4.1.3) shows use of the `prov:ServiceDescription` type.

## 5. Provenance pingback

This section describes a mechanism that may be used to discover related provenance information that the publisher of a resource does not otherwise know about; e.g. provenance describing how it is used after it has been created.

The mechanisms discussed in previous sections are primarily concerned with the publisher enabling access to known provenance about an entity, answering with questions such as:

- what was this resource based upon?
- how was it constructed?
- who made it?
- when was it made?

These questions can be opened up to consider provenance information created by unrelated third parties, like:

- what new resources are based on this resource?
- what has this resource been used for?
- who has used it?
- what other resources are derived from the same sources as this resource?

The ability to answer such broader questions requires some cooperation among the parties who use a resource; for example, a consumer could report use directly to the publisher, or a search engine could discover and report downstream resource usage. To facilitate such cooperation, a resource publisher may receive provenance "ping-backs". (The mechanism described here is
inspired by [blog pingbacks](http://www.hixie.ch/specs/pingback/pingback), but avoids the need for XML-RPC and is specific for provenance records.)

A resource may have an associated provenance ping-back URI, which may be presented with references to provenance about the resource. The ping-back URI is associated with a resource using mechanisms similar to those used for presenting a provenance-URI, but using a `prov:pingback` link relation instead of `prov:has_provenance`. A consumer of the resource, or some other system, may perform an HTTP POST operation to the pingback URI, with a request body containing a list of provenance-URIs for provenance records describing uses of the resource.

For example, consider a resource that is published by `acme.example.com`, and is subsequently used by `coyote.example.org` in the construction of some new entity; we might see an exchange along the following lines. We start with `coyote.example.org` retrieving a copy of `acme.example.org`'s resource:
> **Example:**
>
> > **Example:**
> >
> > Example 11
>
> ```
> C: GET http://acme.example.org/super-widget123 HTTP/1.1
>
> S: 200 OK
> S: Link: <http://acme.example.org/super-widget123/provenance>;
>          rel="http://www.w3.org/ns/prov#has_provenance"
> S: Link: <http://acme.example.org/super-widget123/pingback>;
>          rel="http://www.w3.org/ns/prov#pingback"
>  :
> (super-widget123 resource data)
> ```

The first of the links in the response is a `has_provenance` link with a provenance-URI that has been described previously (section 3.1 Resource accessed by HTTP (§3.1)). The second is a distinct resource that exists to receive provenance pingbacks. Later, when a new resource has been created or some related action performed based upon the `acme.example.org/super-widget123`, a client may post a pingback request to the supplied `pingback` URI:
> **Example:**
>
> > **Example:**
> >
> > Example 12
>
> ```
> C: POST http://acme.example.org/super-widget123/pingback HTTP/1.1
> C: Content-Type: text/uri-list
> C:
> C: http://coyote.example.org/contraption/provenance
> C: http://coyote.example.org/another/provenance
>
> S: 204 No Content
> ```

The pingback request supplies a list of provenance-URIs from which additional provenance may be retrieved. The pingback service may do as it chooses with these URIs; e.g., it may choose to save them for later use, to retrieve the associated provenance and save that, to publish the URIs along with other provenance information about the original entity to which they relate, or even to ignore them.

There is no required information in the server response to a pingback POST request.
In the examples here, the pingback service responds positively with `204 No Content` and an empty response body. Other HTTP status values like `200 OK`, `201 Created`, `202 Accepted`, and `303 See Other` might also be appropriate positive responses depending on the domain and application.

The only defined operation on a pingback-URI is POST, which supplies links to provenance information or services as described above. A pingback-URI *MAY* respond to other requests, but no requirements are imposed on how it responds. In particular, it is not specified here how a pingback resource should respond to an HTTP GET request.

The pingback client *MAY* include extra `has_provenance` links to indicate provenance records related to a different resources, specified with correspondingly different anchor URIs. These *MAY* indicate further provenance about existing resources, or about new resources (such as new entities derived or specialized from that for which the pingback URI was provided). For example:
> **Example:**
>
> > **Example:**
> >
> > Example 13
>
> ```
> C: POST http://acme.example.org/super-widget123/pingback HTTP/1.1
> C: Link: <http://coyote.example.org/extra/provenance>;
>          rel="http://www.w3.org/ns/prov#has_provenance";
>          anchor="http://acme.example.org/extra-widget"
> C: Content-Type: text/uri-list
> C:
> C: http://coyote.example.org/contraption/provenance
> C: http://coyote.example.org/another/provenance
> C: http://coyote.example.org/extra/provenance
>
> S: 204 No Content
> ```

The client *MAY* also supply `has_query_service` links indicating provenance query services that can describe the target-URI. The anchor *MUST* be included, and *SHOULD* be either the target-URI of the resource for which the pingback URI was provided (from the examples above, that would be `http://acme.example.org/super-widget123`), or some related resource with relevant provenance. For example:
> **Example:**
>
> > **Example:**
> >
> > Example 14
>
> ```
> C: POST http://acme.example.org/super-widget123/pingback HTTP/1.1
> C: Link: <http://coyote.example.org/sparql>;
>          rel="http://www.w3.org/ns/prov#has_query_service";
>          anchor="http://acme.example.org/super-widget123"
> C: Content-Type: text/uri-list
> C: Content-Length: 0
> C:
>
> S: 204 No Content
> ```

Here, the pingback client has supplied a query service URI, but did not submit any provenance-URIs and the URI list is therefore empty. The `Link` header field indicates that the resource `http://acme.example.org/super-widget123/provenance` contains provenance information relating to `http://acme.example.org/super-widget123` (that being the URI of the resource for which the pingback URI was provided).

## 6. Security considerations

Provenance is central to establishing trust in data. If provenance is corrupted, it may lead agents (human or software) to draw inappropriate and possibly harmful conclusions. Therefore, care is needed to ensure that the integrity of provenance is maintained. Just as provenance can help determine a level of trust in some information, a provenance record related to the provenance itself ("provenance of provenance") can help determine trust in the provenance.

The [HTTP security considerations](https://www.w3.org/Protocols/rfc2616/rfc2616-sec15.html) [HTTP11] generally apply for all of the resources and services located through the mechanism in this document.

Secure HTTP (https) *SHOULD* be used across unsecured networks when accessing provenance that may be used as a basis for trust decisions, or to obtain a provenance URI for same.

When retrieving a provenance URI from a document, steps *SHOULD* be taken to ensure the document itself is an accurate copy of the original whose author is being trusted (e.g. signature checking, or use of a trusted secure web service). (See also section 1.3 Interpreting provenance records (§1.3).)

Provenance may present a route for leakage of privacy-related information, combining as it does a diversity of information types with possible personally-identifying information; e.g. editing timestamps may provide clues to the working patterns of document editors, or derivation traces might indicate access to sensitive materials. In particular, note that the fact that a resource is openly accessible does not mean that its provenance should also be. When publishing provenance, its sensitivity *SHOULD* be considered and appropriate access controls applied where necessary. When a provenance-aware publishing service accepts some resource for publication, the contributors *SHOULD* have some opportunity to review and correct or conceal any provenance that they don't wish to be exposed. Provenance management systems *SHOULD* embody mechanisms for enforcement and auditing of privacy policies as they apply to provenance. Implementations *MAY* choose to use standard HTTP authorization mechanisms to restrict access to resources, returning `401 Unauthorized`, `403 Forbidden` or `404 Not Found` as appropriate.

Provenance may be used by audits to establish accountability for information use [INFO-ACC] and to verify use of proper processes in information processing activities. Thus, provenance management systems can provide mechanisms to support auditing and enforcement of information handling policies. In such cases, provenance itself may be a valuable target for attack by malicious agents, and care must be taken to ensure it is stored securely and in a fashion that resists attempts to tamper with it.

The pingback service described in section 5. Provenance pingback (§5) might be abused for "link spamming" (similar to the way that weblog ping-backs have been used to direct viewers to spam sites). As with many such services, an application needs to find a balance between maintaining ease of submission for useful information and blocking unwanted information. We have no easy solutions for this problem, and the caveats noted above about establishing integrity of provenance records apply similarly to information provided by ping-back calls.

When clients and servers are retrieving submitted URIs such as provenance descriptions and following or registering links; reasonable care should be taken to prevent malicious use such as distributed denial of service attacks (DDoS), cross-site request forgery (CSRF), spamming and hosting of inappropriate materials. Reasonable preventions might include same-origin policy, HTTP authorization, SSL, rate-limiting, spam filters, moderation queues, user acknowledgements and validation. It is out of scope for this document to specify how such mechanisms work and should be applied.

Provenance pingback uses an HTTP POST operation, which may be used for non-"safe" interactions in the sense of [WEBARCH] ([section 3.4](https://www.w3.org/TR/2004/REC-webarch-20041215/#safe-interaction)). Care needs to be taken that user agents are not tricked into POSTing to incorrect URIs in such a way that may incur unintended effects or obligations. For example, a malicious site may present a pingback URI that executes an instruction on a different web site. Risks of such abuse may be mitigated by: performing pingbacks only to URIs from trusted sources; performing pingbacks only to the same origin as the provider of the pingback URI (like in-browser javascript same-origin restrictions), not sending credentials with pingback requests that were not obtained specifically for that purpose, and any other measures that may be appropriate.

Accessing provenance services might reveal to the service and third-parties information which is considered private, including which resources a client has taken interest in. For instance, a browser extension which collects all provenance data for a resource which is being saved to the local disk, could be revealing user interest in a sensitive resource to a third-party site listed by `prov:has_provenance` or `prov:has_query_service` relation. A detailed query submitted to a third-party provenance query service might be revealing personal information such as social security numbers. Accordingly, user agents in particular *SHOULD NOT* follow provenance and provenance service links without first obtaining the user's explicit permission to do so.

## B. Terms added to prov: namespace

This specification defines the following additional names in the provenance namespace
with URI [http://www.w3.org/ns/prov#](https://www.w3.org/ns/prov#).

| Name                    | Description                                                                                                                                                                                              | Definition ref                                                                                                                                                                                           |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ServiceDescription`    | Type for a generic provenance query service. Mainly for use in RDF provenance query service descriptions, to facilitate discovery in linked data environments.                                           | section 4.3 Provenance query service discovery (§4.3)                                                                                      |
| `DirectQueryService`    | Type for a direct HTTP query service description. Mainly for use in RDF provenance query service descriptions, to distinguish direct HTTP query service descriptions from other query service descriptions. | section 4.1.1 Direct HTTP query service description (§4.1.1)                                                                              |
| `has_anchor`            | Indicates a target-URI for an resource, used by an associated provenance record.                                                                        | section 3.2 Resource represented as HTML (§3.2), section 3.3 Resource represented as RDF (§3.3) |
| `has_provenance`        | Indicates a provenance-URI for a resource; the resource identified by this property presents a provenance record about its subject or anchor resource. | section 3.1 Resource accessed by HTTP (§3.1), section 3.2 Resource represented as HTML (§3.2) |
| `has_query_service`     | Indicates a provenance query service that can access provenance related to its subject or anchor resource.                                | section 3.1.1 Specifying Provenance Query Services (§3.1.1)                                                                                |
| `describesService`      | relates a generic provenance query service resource (type `prov:ServiceDescription`) to a specific query service description (e.g. a `prov:DirectQueryService` or a `sd:Service`).                       | section 4.1 Provenance query service description (§4.1)                                                                                  |
| `provenanceUriTemplate` | Indicates a URI template string for constructing provenance-URIs                                                                                                                                         | section 4.1.1 Direct HTTP query service description (§4.1.1)                                                                              |
| `pingback`              | Relates a resource to a provenance pingback service that may receive additional provenance links about the resource.                                                                                     | section 5. Provenance pingback (§5)                                                                                                                     |

The ontology describing these terms is available [here](https://www.w3.org/ns/prov-aq).

## C. References

### C.1 Informative references

[HTTP11]

R. Fielding et al. [Hypertext Transfer Protocol - HTTP/1.1](http://www.ietf.org/rfc/rfc2616.txt). June 1999. RFC 2616. URL: <http://www.ietf.org/rfc/rfc2616.txt>

[INFO-ACC]

Weitzner, Abelson, Berners-Lee, Feigenbaum, Hendler, and Sussman. [Information Accountability](http://dig.csail.mit.edu/2008/06/info-accountability-cacm-weitzner.pdf). Communications of the ACM, Jun. 2008, 82-87, <http://doi.acm.org/10.1145/1349026.1349043>, <http://dig.csail.mit.edu/2008/06/info-accountability-cacm-weitzner.pdf> (alt)

[LINK-REL]

M. Nottingham, [Web Linking](http://www.ietf.org/rfc/rfc5988.txt), October 2010, Internet RFC 5988. URL: <http://www.ietf.org/rfc/rfc5988.txt>

[PROV-CONSTRAINTS]

James Cheney; Paolo Missier; Luc Moreau; eds. [Constraints of the PROV Data Model](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/). 30 April 2013, W3C Recommendation. URL: [http://www.w3.org/TR/2013/REC-prov-constraints-20130430/](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/)

[PROV-DC]

Daniel Garijo; Kai Eckert; eds. [Dublin Core to PROV Mapping](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-dc-20130430/](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/)

[PROV-DICTIONARY]

Tom De Nies; Sam Coppens; eds. [PROV Dictionary: Modeling Provenance for Dictionary Data Structures](https://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/). 30 April 2013, W3C Note. URL: [http://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/](https://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/)

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

[RDF-CONCEPTS11]

Richard Cyganiak, David Wood, eds. [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). Working Draft. URL: [http://www.w3.org/TR/rdf11-concepts/](https://www.w3.org/TR/rdf11-concepts/)

[REST]

R. Fielding. [Representational State Transfer (REST)](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm). 2000, Ph.D. dissertation. URL: <http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm>

[REST-APIs]

R. Fielding. [REST APIs must be hypertext driven](http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven). October 2008 (blog post), URL: <http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven>

[RFC2119]

S. Bradner. [Key words for use in RFCs to Indicate Requirement Levels.](http://www.ietf.org/rfc/rfc2119.txt) March 1997. Internet RFC 2119. URL: <http://www.ietf.org/rfc/rfc2119.txt>

[RFC2392]

E. Levinson. [Content-ID and Message-ID Uniform Resource Locators.](http://www.ietf.org/rfc/rfc2392.txt) August 1998. Internet RFC 2392. URL: <http://www.ietf.org/rfc/rfc2392.txt>

[RFC3986]

T. Berners-Lee; R. Fielding; L. Masinter. [Uniform Resource Identifier (URI): Generic Syntax (RFC 3986)](http://www.ietf.org/rfc/rfc3986.txt). January 2005. RFC. URL: <http://www.ietf.org/rfc/rfc3986.txt>

[RFC3987]

M. Dürst; M. Suignard. [Internationalized Resource Identifiers (IRIs) (RFC 3987)](http://www.ietf.org/rfc/rfc3987.txt). January 2005. RFC. URL: <http://www.ietf.org/rfc/rfc3987.txt>

[SPARQL-HTTP]

Chimezie Ogbuji. [SPARQL 1.1 Graph Store HTTP Protocol](https://www.w3.org/TR/sparql11-http-rdf-update/). 21 March 2013, W3C Recommendation. URL: [http://www.w3.org/TR/sparql11-http-rdf-update/](https://www.w3.org/TR/sparql11-http-rdf-update/)

[SPARQL-SD]

G. T. Williams. [SPARQL 1.1 Service Description](https://www.w3.org/TR/sparql11-service-description/). 21 March 2013, W3C Recommendation. URL: [http://www.w3.org/TR/sparql11-service-description/](https://www.w3.org/TR/sparql11-service-description/)

[TURTLE]

Eric Prud'hommeaux, Gavin Carothers. [Turtle: Terse RDF Triple Language](https://www.w3.org/TR/turtle/). 19 February 2013. W3C Candidate Recommendation. URL: [http://www.w3.org/TR/turtle/](https://www.w3.org/TR/turtle/)

[URI-template]

J. Gregorio; R. Fielding; M. Hadley; M. Nottingham; D. Orchard. [URI Template](http://tools.ietf.org/html/rfc6570). March 2012, Internet RFC 6570. URL: [http://tools.ietf.org/html/rfc6570](http://tools.ietf.org/html/rfc6570/)

[VoID]

Keith Alexander, Richard Cyganiak, Michael Hausenblas, Jun Zhao. [Describing Linked Datasets with the VoID Vocabulary](https://www.w3.org/TR/void/), W3C Interest Group Note 03 March 2011, [http://www.w3.org/TR/void/](https://www.w3.org/TR/void/)

[WEBARCH]

Norman Walsh; Ian Jacobs. [Architecture of the World Wide Web, Volume One](https://www.w3.org/TR/2004/REC-webarch-20041215/). 15 December 2004. W3C Recommendation. URL: [http://www.w3.org/TR/2004/REC-webarch-20041215/](https://www.w3.org/TR/2004/REC-webarch-20041215/)
