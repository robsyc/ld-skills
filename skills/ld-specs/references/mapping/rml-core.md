---
title: "RML-Core"
source: https://w3id.org/rml/core/spec
family: mapping
spec_date: 2026-03-16
fetched: 2026-11-02
---

# RML-Core

> Core mapping constructs — triples maps, term maps (W3C CG draft).

## Contents

- Abstract
- 1 Conformance
- 2 RML Overview and Example
  - 2.1 Example input data sources
- 3 RML Mapping Documents
  - 3.1 RML Mapping
  - 3.2 Mapping Graphs and the RML Vocabulary
  - 3.3 RDF-based Turtle Syntax; Media Type
- 4 RML Processors, Validators and Generators
  - 4.1 RML Processor
    - 4.1.1 Base IRI
  - 4.2 RML Validator
  - 4.3 Data Errors
- 5 Defining Iterables and Logical Sources
- 6 Mapping to RDF with Triples Maps
  - 6.1 Creating Resources with Subject Maps
  - 6.2 Typing Resources (rml:class)
  - 6.3 Creating Properties and Values with Predicate-Object Maps
- 7 Generating values with expressions
  - 7.1 Expression map (rml:ExpressionMap)
    - 7.1.1 Constant expression (rml:constant)
    - 7.1.2 Reference (rml:reference)
    - 7.1.3 Template (rml:template)
- 8 Term Maps
  - 8.1 Constant RDF Terms (rml:constant)
    - 8.1.1 Shortcuts for constant-valued term maps
  - 8.2 Reference (rml:reference)
  - 8.3 Template (rml:template)
    - 8.3.1 IRI encoding
  - 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
    - 8.4.1 Default Term Types
    - 8.4.2 Explicitly Defined Term Types
  - 8.5 Language tags (rml:languageMap and rml:language)
  - 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- 9 Joins
  - 9.1 Referencing Object Map
  - 9.2 Join Condition
    - 9.2.1 Shortcuts for reference-valued child map and parent map
- 10 Assigning Triples to Named Graphs
  - 10.1 Scope of Blank Nodes
- 11 Datatype conversions
  - 11.1 Natural mapping of source values
  - 11.2 Datatype-override mapping of source values
  - 11.3 Summary of XSD Lexical Forms
- 12 The Output Dataset
  - 12.1 The Generated RDF Triples of a Triples Map
    - 12.1.1 Adding Triples to the Output Dataset
  - 12.2 Generated RDF Term of a Term Map
- 13 Definitions
- 14 Terminology
  - 14.1 RDF Terminology
  - 14.2 RDFS Terminology
  - 14.3 XML Schema Definition Language (XSD) Terminology
  - 14.4 Uniform Resource Identifier Terminology
- A References
  - A.1 Normative references
  - A.2 Informative references

---

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 2.1 Example input data sources (2)
- § 3.2 Mapping Graphs and the RML Vocabulary (2) (3)
- § 4.1.1 Base IRI
- § 4.2 RML Validator
- § 4.3 Data Errors (2)
- § 9.1 Referencing Object Map
- § 9.2 Join Condition
- § 10. Assigning Triples to Named Graphs
- § 12. The Output Dataset (2) (3)

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 2.1 Example input data sources
- § 4.3 Data Errors
- § 8.2 Reference (rml:reference)
- § 8.3.1 IRI encoding (2) (3) (4)
- § 8.5 Language tags (rml:languageMap and rml:language)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)

Permalink

**Referenced in:**

- § 3.2 Mapping Graphs and the RML Vocabulary (2)
- § 3.3 RDF-based Turtle Syntax; Media Type (2)
- § 8.1.1 Shortcuts for constant-valued term maps
- § 9.2.1 Shortcuts for reference-valued child map and parent map

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 3.2 Mapping Graphs and the RML Vocabulary (2) (3) (4)

Permalink

**Referenced in:**

- § 3.2 Mapping Graphs and the RML Vocabulary

Permalink

**Referenced in:**

- § 3.2 Mapping Graphs and the RML Vocabulary (2) (3) (4)
- § 9.2 Join Condition (2) (3)

Permalink

**Referenced in:**

- § 2.1 Example input data sources (2) (3)
- § 3.3 RDF-based Turtle Syntax; Media Type (2)
- § 4.1.1 Base IRI (2) (3)

Permalink

**Referenced in:**

- § 3.2 Mapping Graphs and the RML Vocabulary
- § 3.3 RDF-based Turtle Syntax; Media Type
- § 4.1 RML Processor (2) (3) (4)
- § 4.1.1 Base IRI
- § 4.2 RML Validator
- § 4.3 Data Errors (2) (3) (4)
- § 12. The Output Dataset (2) (3)
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 4.1.1 Base IRI
- § 4.2 RML Validator
- § 9.2 Join Condition (2)

Permalink

**Referenced in:**

- § 4.2 RML Validator
- § 4.3 Data Errors

Permalink

**Referenced in:**

- § 4.2 RML Validator (2)
- § 8.3.1 IRI encoding
- § 8.4.2 Explicitly Defined Term Types
- § 11.2 Datatype-override mapping of source values
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 5. Defining Iterables and Logical Sources (2) (3) (4) (5) (6)

Permalink

**Referenced in:**

- § 5. Defining Iterables and Logical Sources (2)
- § 7. Generating values with expressions
- § 7.1.2 Reference (rml:reference)
- § 9.2 Join Condition
- § 11. Datatype conversions (2)
- § 11.1 Natural mapping of source values
- § 11.3 Summary of XSD Lexical Forms
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 5. Defining Iterables and Logical Sources
- § 9.2 Join Condition

Permalink

**Referenced in:**

- Not referenced in this document.

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 5. Defining Iterables and Logical Sources (2)
- § 6. Mapping to RDF with Triples Maps (2) (3) (4)
- § 6.3 Creating Properties and Values with Predicate-Object Maps
- § 7. Generating values with expressions
- § 7.1 Expression map (rml:ExpressionMap)
- § 7.1.2 Reference (rml:reference)
- § 7.1.3 Template (rml:template)
- § 8. Term Maps
- § 8.1 Constant RDF Terms (rml:constant)
- § 8.2 Reference (rml:reference) (2)
- § 8.3.1 IRI encoding (2) (3)
- § 9.1 Referencing Object Map
- § 9.2 Join Condition (2)
- § 12.1 The Generated RDF Triples of a Triples Map (2)
- § 12.2 Generated RDF Term of a Term Map (2) (3)

Permalink

**Referenced in:**

- § 3.1 RML Mapping
- § 4.2 RML Validator
- § 4.3 Data Errors
- § 5. Defining Iterables and Logical Sources (2) (3) (4) (5)
- § 11. Datatype conversions
- § 11.1 Natural mapping of source values
- § 11.3 Summary of XSD Lexical Forms

Permalink

**Referenced in:**

- § 2. RML Overview and Example (2) (3)
- § 2.1 Example input data sources
- § 3.2 Mapping Graphs and the RML Vocabulary
- § 4.1 RML Processor (2)
- § 6. Mapping to RDF with Triples Maps (2) (3) (4) (5) (6) (7) (8)
- § 6.3 Creating Properties and Values with Predicate-Object Maps
- § 7.1.2 Reference (rml:reference)
- § 9. Joins (2)
- § 9.1 Referencing Object Map (2)
- § 9.2 Join Condition (2) (3) (4) (5) (6) (7) (8) (9) (10)
- § 12.1 The Generated RDF Triples of a Triples Map
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 2. RML Overview and Example (2) (3)
- § 2.1 Example input data sources (2) (3)
- § 3.1 RML Mapping
- § 3.2 Mapping Graphs and the RML Vocabulary (2) (3)
- § 4.1.1 Base IRI
- § 5. Defining Iterables and Logical Sources
- § 6. Mapping to RDF with Triples Maps (2) (3)
- § 6.1 Creating Resources with Subject Maps
- § 6.3 Creating Properties and Values with Predicate-Object Maps
- § 8. Term Maps
- § 9. Joins (2)
- § 9.1 Referencing Object Map (2)
- § 9.2 Join Condition (2) (3) (4) (5) (6) (7) (8)
- § 12. The Output Dataset
- § 12.1 The Generated RDF Triples of a Triples Map (2) (3) (4)

Permalink

**Referenced in:**

- § 2. RML Overview and Example (2)
- § 2.1 Example input data sources
- § 3.2 Mapping Graphs and the RML Vocabulary (2)
- § 6. Mapping to RDF with Triples Maps (2) (3) (4)
- § 6.2 Typing Resources (rml:class) (2)
- § 6.3 Creating Properties and Values with Predicate-Object Maps
- § 8. Term Maps (2)
- § 8.3.1 IRI encoding (2) (3) (4)
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.1 Default Term Types
- § 8.4.2 Explicitly Defined Term Types
- § 9. Joins
- § 10. Assigning Triples to Named Graphs (2) (3)
- § 12.1 The Generated RDF Triples of a Triples Map (2)

Permalink

**Referenced in:**

- § 6.2 Typing Resources (rml:class)
- § 12.1 The Generated RDF Triples of a Triples Map (2)

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 3.2 Mapping Graphs and the RML Vocabulary
- § 6. Mapping to RDF with Triples Maps (2)
- § 6.2 Typing Resources (rml:class)
- § 6.3 Creating Properties and Values with Predicate-Object Maps
- § 8.2 Reference (rml:reference) (2)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 9.1 Referencing Object Map
- § 9.2 Join Condition (2)
- § 10. Assigning Triples to Named Graphs (2)
- § 12.1 The Generated RDF Triples of a Triples Map (2) (3) (4)

Permalink

**Referenced in:**

- § 2. RML Overview and Example (2)
- § 3.2 Mapping Graphs and the RML Vocabulary
- § 6. Mapping to RDF with Triples Maps
- § 6.3 Creating Properties and Values with Predicate-Object Maps (2)
- § 8. Term Maps (2)
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.1 Default Term Types
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 2. RML Overview and Example (2)
- § 3.2 Mapping Graphs and the RML Vocabulary
- § 6. Mapping to RDF with Triples Maps
- § 6.2 Typing Resources (rml:class)
- § 6.3 Creating Properties and Values with Predicate-Object Maps (2) (3)
- § 8. Term Maps (2)
- § 8.2 Reference (rml:reference)
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.1 Default Term Types
- § 8.4.2 Explicitly Defined Term Types
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 5. Defining Iterables and Logical Sources (2)
- § 6. Mapping to RDF with Triples Maps
- § 7.1 Expression map (rml:ExpressionMap)
- § 7.1.2 Reference (rml:reference)

Permalink

**Referenced in:**

- § 7.1 Expression map (rml:ExpressionMap) (2)
- § 7.1.1 Constant expression (rml:constant)
- § 7.1.2 Reference (rml:reference)
- § 7.1.3 Template (rml:template)
- § 8. Term Maps
- § 8.4.2 Explicitly Defined Term Types
- § 8.5 Language tags (rml:languageMap and rml:language)
- § 9.2 Join Condition (2)
- § 12.2 Generated RDF Term of a Term Map (2)

Permalink

**Referenced in:**

- § 4.1.1 Base IRI
- § 7.1.1 Constant expression (rml:constant)
- § 7.1.2 Reference (rml:reference)
- § 11. Datatype conversions (2)
- § 11.1 Natural mapping of source values (2)
- § 11.2 Datatype-override mapping of source values
- § 11.3 Summary of XSD Lexical Forms (2)
- § 12.2 Generated RDF Term of a Term Map (2) (3)

Permalink

**Referenced in:**

- § 7.1.2 Reference (rml:reference)
- § 7.1.3 Template (rml:template) (2)

Permalink

**Referenced in:**

- § 6. Mapping to RDF with Triples Maps
- § 7.1.1 Constant expression (rml:constant)
- § 8.1 Constant RDF Terms (rml:constant)
- § 9.2 Join Condition (2)

Permalink

**Referenced in:**

- § 7.1.1 Constant expression (rml:constant)
- § 8.1 Constant RDF Terms (rml:constant)
- § 8.4.2 Explicitly Defined Term Types

Permalink

**Referenced in:**

- § 8.1 Constant RDF Terms (rml:constant)
- § 8.4.2 Explicitly Defined Term Types
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 7.1.2 Reference (rml:reference)
- § 8.2 Reference (rml:reference) (2)
- § 9.2.1 Shortcuts for reference-valued child map and parent map (2)

Permalink

**Referenced in:**

- § 7.1.1 Constant expression (rml:constant)
- § 7.1.2 Reference (rml:reference) (2) (3)
- § 7.1.3 Template (rml:template) (2) (3) (4) (5) (6) (7) (8)

Permalink

**Referenced in:**

- § 7.1.3 Template (rml:template) (2)
- § 8.2 Reference (rml:reference) (2) (3)
- § 8.3.1 IRI encoding (2)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 7.1.3 Template (rml:template)
- § 8.3 Template (rml:template) (2)

Permalink

**Referenced in:**

- § 7.1.3 Template (rml:template) (2)
- § 8.3.1 IRI encoding (2)

Permalink

**Referenced in:**

- § 7.1.3 Template (rml:template) (2) (3) (4) (5) (6)
- § 8.3.1 IRI encoding

Permalink

**Referenced in:**

- § 7.1.3 Template (rml:template) (2)
- § 8.3.1 IRI encoding (2) (3) (4)

Permalink

**Referenced in:**

- § 8.3 Template (rml:template)
- § 8.3.1 IRI encoding (2) (3)
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 4.3 Data Errors (2) (3)
- § 6.2 Typing Resources (rml:class)
- § 8. Term Maps (2)
- § 8.1 Constant RDF Terms (rml:constant) (2)
- § 8.2 Reference (rml:reference)
- § 12.1.1 Adding Triples to the Output Dataset
- § 12.2 Generated RDF Term of a Term Map (2) (3)

Permalink

**Referenced in:**

- § 3.2 Mapping Graphs and the RML Vocabulary
- § 4.3 Data Errors (2)
- § 6. Mapping to RDF with Triples Maps (2)
- § 6.1 Creating Resources with Subject Maps
- § 6.3 Creating Properties and Values with Predicate-Object Maps (2)
- § 8. Term Maps (2) (3) (4) (5) (6) (7)
- § 8.1.1 Shortcuts for constant-valued term maps
- § 8.3.1 IRI encoding
- § 8.4.1 Default Term Types
- § 8.4.2 Explicitly Defined Term Types (2) (3)
- § 8.5 Language tags (rml:languageMap and rml:language) (2)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype) (2) (3) (4)
- § 10. Assigning Triples to Named Graphs
- § 12. The Output Dataset
- § 12.2 Generated RDF Term of a Term Map (2) (3) (4) (5)

Permalink

**Referenced in:**

- § 8.1 Constant RDF Terms (rml:constant)
- § 8.2 Reference (rml:reference)
- § 8.3.1 IRI encoding
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.2 Explicitly Defined Term Types (2)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 12.1 The Generated RDF Triples of a Triples Map (2) (3) (4) (5) (6) (7) (8) (9) (10)
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 8.1 Constant RDF Terms (rml:constant)
- § 8.1.1 Shortcuts for constant-valued term maps
- § 8.4.2 Explicitly Defined Term Types (2)
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 6. Mapping to RDF with Triples Maps
- § 6.3 Creating Properties and Values with Predicate-Object Maps (2)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 10. Assigning Triples to Named Graphs (2)

Permalink

**Referenced in:**

- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.1 Default Term Types
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 8.3.1 IRI encoding (2) (3)
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.2 Explicitly Defined Term Types
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 11.1 Natural mapping of source values
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 8.3.1 IRI encoding (2)

Permalink

**Referenced in:**

- § 8.3.1 IRI encoding

Permalink

**Referenced in:**

- § 6. Mapping to RDF with Triples Maps
- § 8. Term Maps
- § 8.3.1 IRI encoding (2) (3) (4) (5)
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.1 Default Term Types
- § 8.4.2 Explicitly Defined Term Types (2) (3) (4) (5) (6) (7) (8) (9)
- § 8.5 Language tags (rml:languageMap and rml:language)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 11.1 Natural mapping of source values

Permalink

**Referenced in:**

- § 8.5 Language tags (rml:languageMap and rml:language) (2) (3) (4)

Permalink

**Referenced in:**

- § 8. Term Maps
- § 8.1.1 Shortcuts for constant-valued term maps
- § 8.5 Language tags (rml:languageMap and rml:language) (2) (3)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 12.2 Generated RDF Term of a Term Map (2)

Permalink

**Referenced in:**

- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype) (2) (3) (4) (5) (6)

Permalink

**Referenced in:**

- § 8. Term Maps (2) (3)
- § 8.1.1 Shortcuts for constant-valued term maps
- § 8.5 Language tags (rml:languageMap and rml:language)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype) (2) (3) (4) (5)
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 3.2 Mapping Graphs and the RML Vocabulary
- § 6.3 Creating Properties and Values with Predicate-Object Maps
- § 9. Joins
- § 9.1 Referencing Object Map (2)
- § 9.2 Join Condition (2) (3) (4) (5) (6) (7)
- § 12.1 The Generated RDF Triples of a Triples Map (2) (3) (4)

Permalink

**Referenced in:**

- § 2.1 Example input data sources (2)
- § 9.1 Referencing Object Map (2) (3)
- § 9.2 Join Condition (2)
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 3.2 Mapping Graphs and the RML Vocabulary
- § 9. Joins
- § 9.1 Referencing Object Map (2)
- § 9.2 Join Condition (2) (3) (4) (5)
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 9.2 Join Condition (2)
- § 9.2.1 Shortcuts for reference-valued child map and parent map

Permalink

**Referenced in:**

- § 9.2 Join Condition
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 9.2 Join Condition (2)
- § 9.2.1 Shortcuts for reference-valued child map and parent map

Permalink

**Referenced in:**

- § 9.2 Join Condition
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 9.1 Referencing Object Map
- § 9.2 Join Condition (2) (3) (4)

Permalink

**Referenced in:**

- § 9.2 Join Condition

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 3.2 Mapping Graphs and the RML Vocabulary
- § 8. Term Maps (2)
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.1 Default Term Types
- § 8.4.2 Explicitly Defined Term Types
- § 10. Assigning Triples to Named Graphs (2) (3) (4)
- § 12.1 The Generated RDF Triples of a Triples Map (2) (3) (4)

Permalink

**Referenced in:**

- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 11. Datatype conversions
- § 11.1 Natural mapping of source values (2) (3)
- § 11.3 Summary of XSD Lexical Forms

Permalink

**Referenced in:**

- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 11. Datatype conversions
- § 11.1 Natural mapping of source values (2)
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 7.1.3 Template (rml:template)
- § 11.1 Natural mapping of source values
- § 11.2 Datatype-override mapping of source values
- § 12.2 Generated RDF Term of a Term Map (2) (3)

Permalink

**Referenced in:**

- § 11.1 Natural mapping of source values
- § 11.3 Summary of XSD Lexical Forms

Permalink

**Referenced in:**

- § 11.1 Natural mapping of source values
- § 11.3 Summary of XSD Lexical Forms

Permalink

**Referenced in:**

- § 4.3 Data Errors
- § 11.1 Natural mapping of source values (2)
- § 11.3 Summary of XSD Lexical Forms

Permalink

**Referenced in:**

- § 4.3 Data Errors
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype) (2) (3)
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 4.3 Data Errors
- § 11.2 Datatype-override mapping of source values (2)

Permalink

**Referenced in:**

- § 11.2 Datatype-override mapping of source values

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 4.1 RML Processor (2) (3) (4) (5)
- § 4.3 Data Errors (2)
- § 10. Assigning Triples to Named Graphs (2)
- § 10.1 Scope of Blank Nodes
- § 12. The Output Dataset (2) (3) (4)
- § 12.1 The Generated RDF Triples of a Triples Map (2)
- § 12.1.1 Adding Triples to the Output Dataset (2)

Permalink

**Referenced in:**

- § 12. The Output Dataset
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 12.2 Generated RDF Term of a Term Map (2) (3)

Permalink

**Referenced in:**

- § 7.1.3 Template (rml:template)
- § 8.5 Language tags (rml:languageMap and rml:language)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 13. Definitions (2)

Permalink

**Referenced in:**

- § 12. The Output Dataset (2)

Permalink

**Referenced in:**

- § Abstract
- § 3.2 Mapping Graphs and the RML Vocabulary (2)
- § 10.1 Scope of Blank Nodes

Permalink

**Referenced in:**

- § 2. RML Overview and Example (2) (3) (4) (5)
- § 2.1 Example input data sources (2) (3) (4)
- § 3.2 Mapping Graphs and the RML Vocabulary
- § 4.1.1 Base IRI
- § 5. Defining Iterables and Logical Sources
- § 6. Mapping to RDF with Triples Maps (2) (3)
- § 6.1 Creating Resources with Subject Maps
- § 6.2 Typing Resources (rml:class)
- § 6.3 Creating Properties and Values with Predicate-Object Maps
- § 8. Term Maps (2) (3) (4) (5) (6)
- § 8.2 Reference (rml:reference) (2)
- § 8.5 Language tags (rml:languageMap and rml:language)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype) (2)
- § 10. Assigning Triples to Named Graphs (2) (3)
- § 10.1 Scope of Blank Nodes
- § 12. The Output Dataset
- § 12.1 The Generated RDF Triples of a Triples Map (2)
- § 12.1.1 Adding Triples to the Output Dataset

Permalink

**Referenced in:**

- § 2. RML Overview and Example (2) (3)
- § 3.2 Mapping Graphs and the RML Vocabulary (2) (3) (4) (5) (6) (7)
- § 4.1.1 Base IRI (2) (3) (4) (5) (6) (7) (8) (9)
- § 4.3 Data Errors
- § 6.2 Typing Resources (rml:class) (2) (3) (4)
- § 8. Term Maps (2) (3) (4) (5) (6)
- § 8.3.1 IRI encoding (2) (3) (4) (5) (6) (7) (8) (9)
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType) (2)
- § 8.4.2 Explicitly Defined Term Types (2) (3) (4) (5)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype) (2)
- § 9.2 Join Condition
- § 10. Assigning Triples to Named Graphs (2)
- § 11.1 Natural mapping of source values (2)
- § 12.1.1 Adding Triples to the Output Dataset (2) (3) (4) (5)
- § 12.2 Generated RDF Term of a Term Map (2)

Permalink

**Referenced in:**

- § 4.1 RML Processor
- § 4.1.1 Base IRI (2) (3) (4) (5) (6)
- § 4.2 RML Validator
- § 12.2 Generated RDF Term of a Term Map (2)

Permalink

**Referenced in:**

- § 8. Term Maps (2) (3)
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.2 Explicitly Defined Term Types (2) (3)
- § 9.2 Join Condition
- § 10. Assigning Triples to Named Graphs (2)
- § 10.1 Scope of Blank Nodes
- § 12. The Output Dataset (2)
- § 12.1.1 Adding Triples to the Output Dataset
- § 12.2 Generated RDF Term of a Term Map (2)

Permalink

**Referenced in:**

- § 3.2 Mapping Graphs and the RML Vocabulary
- § 10.1 Scope of Blank Nodes
- § 12. The Output Dataset (2) (3) (4) (5)

Permalink

**Referenced in:**

- § 4.3 Data Errors
- § 8.4.1 Default Term Types
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype) (2) (3) (4)
- § 11.1 Natural mapping of source values (2)
- § 11.2 Datatype-override mapping of source values (2) (3)
- § 11.3 Summary of XSD Lexical Forms (2)

Permalink

**Referenced in:**

- § 8. Term Maps
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype) (2)
- § 11.2 Datatype-override mapping of source values (2) (3) (4)

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 10. Assigning Triples to Named Graphs (2)
- § 12.1.1 Adding Triples to the Output Dataset

Permalink

**Referenced in:**

- § 8.4.1 Default Term Types
- § 8.5 Language tags (rml:languageMap and rml:language) (2) (3) (4)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype)
- § 12.2 Generated RDF Term of a Term Map (2) (3)

Permalink

**Referenced in:**

- § 8.5 Language tags (rml:languageMap and rml:language) (2)

Permalink

**Referenced in:**

- § 8.5 Language tags (rml:languageMap and rml:language) (2)
- § 11.1 Natural mapping of source values (2)
- § 11.2 Datatype-override mapping of source values (2)
- § 11.3 Summary of XSD Lexical Forms (2)

Permalink

**Referenced in:**

- § 11.2 Datatype-override mapping of source values (2)
- § 11.3 Summary of XSD Lexical Forms (2)

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 8. Term Maps (2)
- § 8.3.1 IRI encoding
- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.2 Explicitly Defined Term Types (2)
- § 8.6 Datatypes of Literals (rml:datatypeMap and rml:datatype) (2) (3) (4) (5) (6)
- § 11.1 Natural mapping of source values (2) (3) (4)
- § 11.2 Datatype-override mapping of source values (2) (3)
- § 12.2 Generated RDF Term of a Term Map

Permalink

**Referenced in:**

- § 2. RML Overview and Example
- § 8. Term Maps
- § 10. Assigning Triples to Named Graphs (2) (3) (4) (5)
- § 12. The Output Dataset (2)
- § 12.1.1 Adding Triples to the Output Dataset (2)

Permalink

**Referenced in:**

- § 9.2 Join Condition

Permalink

**Referenced in:**

- § 2.1 Example input data sources (2)
- § 6.2 Typing Resources (rml:class)
- § 6.3 Creating Properties and Values with Predicate-Object Maps
- § 9.1 Referencing Object Map

Permalink

**Referenced in:**

- § 6.2 Typing Resources (rml:class)
- § 6.3 Creating Properties and Values with Predicate-Object Maps
- § 10. Assigning Triples to Named Graphs

Permalink

**Referenced in:**

- § 9.1 Referencing Object Map
- § 9.2 Join Condition (2)

Permalink

**Referenced in:**

- § 6. Mapping to RDF with Triples Maps (2)
- § 6.3 Creating Properties and Values with Predicate-Object Maps (2)
- § 9.2 Join Condition (2)

Permalink

**Referenced in:**

- § 2.1 Example input data sources
- § 6. Mapping to RDF with Triples Maps (2)
- § 6.1 Creating Resources with Subject Maps
- § 9.1 Referencing Object Map
- § 12.1 The Generated RDF Triples of a Triples Map

Permalink

**Referenced in:**

- § 6.2 Typing Resources (rml:class)

Permalink

**Referenced in:**

- § 11.3 Summary of XSD Lexical Forms

Permalink

**Referenced in:**

- § 11.1 Natural mapping of source values (2)
- § 11.3 Summary of XSD Lexical Forms

Permalink

**Referenced in:**

- § 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)
- § 8.4.2 Explicitly Defined Term Types
- § 12.2 Generated RDF Term of a Term Map (2)

Permalink

**Referenced in:**

- § 4.1.1 Base IRI

Permalink

**Referenced in:**

- § 12.2 Generated RDF Term of a Term Map (2)

Permalink

**Referenced in:**

- § 8.3.1 IRI encoding (2)

## Abstract

This document describes RML, a generic mapping language, based on and extending [R2RML](https://www.w3.org/TR/r2rml). The RDF Mapping language (RML) is a mapping language defined to express customized mapping rules from heterogeneous data structures and serializations to the RDF [RDF-CONCEPTS](https://www.w3.org/TR/rdf-concepts/) data model. RML is defined as a superset of the W3C-standardized mapping language [R2RML](https://www.w3.org/TR/r2rml), aiming to extend its applicability and broaden its scope, adding support for data in other structured formats. [R2RML](https://www.w3.org/TR/r2rml) is the W3C standard to express customized mappings from relational databases to RDF. RML follows exactly the same syntax as R2RML; therefore, RML mappings are themselves RDF graphs. The present document describes the RML-Core language and its concepts through definitions and examples.

## 1. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, *OPTIONAL*, *SHOULD*, and *SHOULD NOT* in this document
are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [RFC2119] [RFC8174]
when, and only when, they appear in all
capitals, as shown here.

## 2. RML Overview and Example

*This section is non-normative.*

This section gives a brief overview of the RML mapping language, followed by a simple example of JSON documents with an RML mapping document and its output RDF. Further RML examples can be found in the [RML-core test-cases](http://w3id.org/rml/core/test-cases).

An RML mapping refers to logical sources to retrieve data from the input data source.

Each logical source is mapped to RDF using a triples map.
The triples map is a rule that maps each iteration in the logical source to a number of RDF triples.
The rule has two main parts:

1. A subject map that generates the subject of all RDF triples that will be generated from a logical source iteration.
   The subjects often are IRIs.
2. Multiple predicate-object maps that
   in turn consist of predicate maps and object maps (or referencing object maps).

Triples are produced by combining the subject map with a predicate map and object map, and applying these three to each logical iteration. For example, the complete rule for generating a set of triples might be:

Subjects: A template `http://data.example.com/image/{ID}` is used to generate subject IRIs from the `ID` name.
Predicates: The constant vocabulary IRI `ex:title` is used.
Objects: The value of the `Title` name is used to produce an RDF literal.

By default, all RDF triples are in the default graph of the output dataset.
A triples map can contain graph maps that
place some or all of the triples into named graphs instead.

An overview of the RML vocabulary is shown in Figure 1:

![RML-Core vocabulary](https://kg-construct.github.io/rml-core/spec/docs/resources/diagram.png)

*Figure 1 RML-Core vocabulary*

### 2.1 Example input data sources
> **Example:**
>
> Example 1: Example input data sources
>
> Input source: images.json
>
> ```
> {
>   "Images": [
>     {
>       "Width":  800,
>       "Height": 600,
>       "Title": {
>           "Lang": "en",
>           "Value": "View from 15th Floor"
>       },
>       "Keywords": ["building", "city", "view"],
>       "Thumbnail": {
>           "Url":    "http://www.example.com/image/481989943",
>           "Height": 125,
>           "Width":  100
>       },
>       "Animated" : false,
>       "ID": 116
>     }
>   ]
> }
> ```
>
> Input source: album.json
>
> ```
> {
>   "Album": {
>     "ID": 43,
>     "Title": "City Views",
>     "Description": "A collection of stunning cityscape images.",
>     "CreatedDate": "2023-10-01",
>     "DateFormat": "date",
>     "Author": "Zoë Krüger",
>     "Images": [
>       {
>         "ID": 116,
>         "Reference": "http://www.example.com/image/481989943"
>       },
>       {
>         "ID": 117,
>         "Reference": "http://www.example.com/image/481989944"
>       }
>     ]
>   }
> }
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The mapping constructs for the concrete logical source in the following examples are defined in [RML-IO], but are used here to provide a complete example.
> **Example:**
>
> Example 2: Desired RDF output
>
> The desired RDF triples to be produced from these input data sources are as follows:
>
> ```
> <http://data.example.com/image/116> a ex:Image .
> <http://data.example.com/image/116> ex:height 600 .
>
> <http://data.example.com/album/43> a ex:Album .
> <http://data.example.com/album/43> ex:title "City Views" .
> <http://data.example.com/album/43> ex:hasImage <http://data.example.com/image/116> .
> ```
>
> > **Example:**
> >
> > Example 3: Simple mappings
> >
> > The following partial RML mapping document maps the `images.json` input source to RDF triples.
> >
> > ```
> > @prefix rml: <http://w3id.org/rml/> .
> > @prefix ex: <http://example.com/ns#> .
> >
> > <#ImageLogicalSource>
> >   rml:source [
> >     a rml:RelativePathSource ;
> >     rml:root rml:MappingDirectory ;
> >     rml:path "images.json" ;
> >   ] ;
> >   rml:iterator "$.Images[*]" ;
> >   rml:referenceFormulation rml:JSONPath .
> >
> > <#ImageTriplesMap>
> >   rml:logicalSource <#ImageLogicalSource> ;
> >   rml:subjectMap [
> >     rml:template "http://data.example.com/image/{$.ID}" ;
> >     rml:class ex:Image ;
> >   ] ;
> >   rml:predicateObjectMap [
> >     rml:predicate ex:height ;
> >     rml:objectMap [
> >       rml:reference "$.Height" ;
> >     ] ;
> >   ] .
> > ```
> >
> > The following RDF triples are generated by the RML mapping above.
> >
> > ```
> > <http://data.example.com/image/116> a ex:Image .
> > <http://data.example.com/image/116> ex:height 600 .
> > ```
> >
> > The following partial RML mapping document maps the `album.json` input source to RDF triples.
> >
> > ```
> > <#AlbumTriplesMap>
> >   rml:logicalSource [
> >     rml:source [
> >       a rml:RelativePathSource ;
> >       rml:root rml:MappingDirectory ;
> >       rml:path "album.json" ;
> >     ] ;
> >     rml:iterator "$.Album" ;
> >     rml:referenceFormulation rml:JSONPath ;
> >   ] ;
> >   rml:subjectMap [
> >     rml:template "http://data.example.com/album/{$.ID}" ;
> >     rml:class ex:Album ;
> >   ] ;
> >   rml:predicateObjectMap [
> >     rml:predicate ex:title ;
> >     rml:objectMap [
> >       rml:reference "$.Title" ;
> >     ] ;
> >   ] .
> > ```
> >
> > The following RDF triples are generated by the RML mapping above.
> >
> > ```
> > <http://data.example.com/album/43> a ex:Album .
> > <http://data.example.com/album/43> ex:title "City Views" .
> > ```
>
> > **Example:**
> >
> > Example 4: Joining two input data sources
> >
> > To complete the mapping document, `ex:hasImage` triples need to be generated. Their subjects come from the second triples map (`<#AlbumTriplesMap>`) and their objects come from the first triples map (`<#ImageTriplesMap>`).
> >
> > This can be achieved by adding another `rml:predicateObjectMap` to `<#AlbumTriplesMap>`. This one used the other triples map, `<#ImageTriplesMap>`, as the parent triples map.
> >
> > ```
> > <#AlbumTriplesMap>
> >   rml:predicateObjectMap [
> >     rml:predicate ex:hasImage ;
> >     rml:objectMap [
> >       rml:parentTriplesMap <#ImageTriplesMap> ;
> >       rml:joinCondition [
> >         rml:child "$.Images[*].ID" ;
> >         rml:parent "$.ID" ;
> >       ] ;
> >     ] ;
> >   ] .
> > ```
> >
> > This performs a join between the `ID` field in the `Images` array of the `album.json` input source and the `ID` field in the `images.json` input source. The objects will be generated from the subject map of the parent triples map, yielding the desired triple.
> >
> > ```
> > <http://data.example.com/album/43> ex:hasImage <http://data.example.com/image/116> .
> > ```

## 3. RML Mapping Documents

### 3.1 RML Mapping

An *RML mapping* defines a mapping from a data source to RDF.
It is a structure that consists of one or more triples maps.

The input to an RML mapping is a data source called the *input data source*.

### 3.2 Mapping Graphs and the RML Vocabulary

An RML mapping is represented as an RDF graph.
In other words, RDF is used not just as the target data model of the mapping,
but also as a formalism for representing the RML mapping itself.

An RDF graph that represents an RML mapping is called an *RML mapping graph*.

The *RML vocabulary* is the set of IRIs defined in this specification
that start with the `rml:` as prefix and uses namespace IRI: `http://w3id.org/rml/`

An RML mapping graph:

1. *SHOULD NOT* include any IRIs that start with the `rml:` namespace IRI,
   but are not defined in the RML vocabulary.
2. *SHOULD NOT* include IRIs from the RML vocabulary where such use is not explicitly allowed or required by a clause in this specification.
3. *SHOULD* contain only mapping components that are referenced by some triples map
   (in other words, all mapping components should actually be “used” in the mapping).
4. *MAY* contain arbitrary additional triples whose terms are not from the RML vocabulary.
   In particular, a valid mapping graph *MAY* contain documentation
   in the form of `rdfs:label`, `rdfs:comment` and similar properties.
5. *MAY* assign IRIs or blank node identifiers to any mapping component in order to enable reuse of mapping components within the mapping graph.
   For example, an IRI that represents a subject map may be used as the [subject= map=] of multiple triples maps;
   and may even be used as an object map of another triples map if it has the right properties.

The RML vocabulary also includes the following *RML classes*:

- `rml:TriplesMap` is the class of triples maps.
- `rml:LogicalSource` is the class of logical sources.
- `rml:TermMap` is the class of term maps. It has four subclasses:
  * `rml:SubjectMap` is the class of subject maps.
  * `rml:PredicateMap` is the class of predicate maps.
  * `rml:ObjectMap` is the class of object maps.
  * `rml:GraphMap` is the class of graph maps.
- `rml:PredicateObjectMap` is the class of predicate-object maps.
- `rml:RefObjectMap` is the class of referencing object maps.
- `rml:Join` is the class of join conditions.

The members of these classes are collectively called *mapping components*.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Many of these classes differ only in capitalization from properties in the RML vocabulary.

Explicit typing of the resources in a mapping graph with RML classes is *OPTIONAL* and has no effect on the behaviour of an RML processor.
The mapping component represented by any given resource in a mapping graph
is defined by the presence or absence of certain properties,
as defined throughout this specification.
A resource *SHOULD NOT* be typed as an RML class
if it does not meet the definition of that class.

### 3.3 RDF-based Turtle Syntax; Media Type

An *RML mapping document* is any document written in the Turtle [TURTLE] RDF syntax
that encodes an RML mapping graph.

The media type for RML mapping documents is the same as for Turtle documents in general: `text/turtle`.
The content encoding of Turtle content is always UTF-8
and the charset parameter on the media type *SHOULD* always be used: `text/turtle;charset=utf-8`. The file extension `.ttl` *SHOULD* be used.

A conforming RML processor *SHOULD* accept RML mapping documents in Turtle syntax.
It *MAY* accept RML mapping graphs encoded in other RDF syntaxes.

## 4. RML Processors, Validators and Generators

### 4.1 RML Processor

An *RML processor* is a system that, given an RML mapping and an input data source,
provides access to the output dataset.

The process of generating the output dataset by an RML processor is called the *RML mapping process*.

There are no constraints on the method of access to the output dataset provided by a conforming RML processor.
An RML processor *MAY* materialize the output dataset into a file,
or offer virtual access through an interface,
or offer any other means of providing access to the output dataset.

An RML processor also has access to an execution environment consisting of:

- A logical source
- A base IRI

How the logical source is accessed,
or how users are authenticated against the database,
is outside of the scope of this document.

#### 4.1.1 Base IRI

A base IRI is used in resolving relative IRIs produced by the RML mapping. The base IRI *MUST* be
defined within the mapping document for each Triples Map or as execution environment for the mapping document.
> **Example:**
>
> Example 5: Base IRI example
>
> The following RML Mapping Document maps the album.json input source to RDF Triples with a base IRI.
>
> ```
> # Triples Map that has a declared base IRI
> <#TriplesMap> a rml:TriplesMap;
>     rml:baseIRI <http://example.com/baseIRI/> ;
>     rml:source [
>       a rml:RelativePathSource ;
>       rml:root rml:MappingDirectory ;
>       rml:path "album.json" ;
>     ] ;
>     rml:iterator "$.Album" ;
>     rml:referenceFormulation rml:JSONPath ;
>   ] ;
>   rml:subjectMap [
>     rml:template "{$.ID}" ;
>     rml:class ex:Album ;
>   ] ;
>   rml:predicateObjectMap [
>     rml:predicate ex:title ;
>     rml:objectMap [
>       rml:reference "$.Title" ;
>     ] ;
>   ] .
> ```
>
> The following RDF triples are generated by the RML mapping above.
>
> ```
> <http://example.com/baseIRI/43> a ex:Album .
> <http://example.com/baseIRI/43> ex:title "City Views" .
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The base IRI of the mapping document is used to resolve relative IRIs in the RML document following the specification of the Turtle serialisaiton.

The base IRI *MUST* be a valid IRI. It *SHOULD NOT* contain question mark ("`?`") or hash ("`#`") characters and *SHOULD* end in a slash ("`/`") character.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> To obtain an absolute IRI from a relative IRI,
> the term generation rules of RML use simple string concatenation,
> rather than the more complex algorithm for resolution of relative URIs.
> This ensures that the original expression evaluation result can be reconstructed from the generated absolute IRI.
> Both algorithms are equivalent if all of the following are true:
>
> 1. The base IRI does not contain question marks or hashes,
> 2. the base IRI ends in a slash,
> 3. the relative IRI does not start with a slash, and
> 4. the relative IRI does not contain any “.” or “..” path segments.

If no specific base IRI is provided and the mapping process needs to generate absolute IRIs from relative ones,
the default base IRI to be used by the RML Processor *MUST* be <http://example.org/>.

### 4.2 RML Validator

An *RML data validator* is a system that takes as its input
an RML mapping, a base IRI, and one or more data sources,
and checks for the presence of data errors.
A data validator *MUST* report any data errors that are raised in the mapping process.

An RML processor *MAY* include an RML data validator, but this is not required.

### 4.3 Data Errors

A *data error* is a condition of the data in the input data source that would lead to the generation of an invalid RDF term.
The following conditions give rise to data errors:

1. A term map with term type `rml:IRI` results in the generation of an invalid IRI.
2. A term map whose natural RDF datatype is overridden with a specified datatype produces an ill-typed literal (see datatype-override RDF literal).

When providing access to the output dataset,
an RML processor *MUST* abort any operation
that requires inspecting or returning an RDF term whose generation would give rise to a data error,
and report an error to the agent invoking the operation.
A conforming RML processor *MAY*, however,
allow other operations that do not require inspecting or returning these RDF terms,
and thus *MAY* provide partial access to an output dataset that contains data errors.
Nevertheless, an RML processor *SHOULD* report data errors as early as possible.

The presence of data errors does not make an RML mapping non-conforming.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Data errors cannot generally be detected by analyzing the schema of the input data,
> but only by scanning the data in the data source.
> For large and rapidly changing databases, this can be impractical.
> Therefore, RML processors are allowed to answer queries
> that do not "touch" a data error,
> and the behavior of such operations is well-defined. For the same reason,
> the conformance of RML mappings is defined without regard for the presence of data errors.
>
> RML data validators can be used to explicitly scan a data source for data errors.

## 5. Defining Iterables and Logical Sources

An *iterable* is an abstract construct to describe data access and iteration for a data source.

An iterable (`rml:Iterable`) *MUST* have:

- zero or one `rml:referenceFormulation` property, whose value is a *reference formulation* which defines how to reference parts of the underlying data source, and which expressions can be evaluated on logical iterations. If no `rml:referenceFormulation` is provided, it *MUST* be inferred as defined for the specific type of Iterable.
- zero or one `rml:iterator` property, whose value is a *logical iterator* that defines a sequence of logical iterations on the data source. If no iterator is provided, a *default iterator* *MUST* be associated with the reference formulation.

A *logical iteration* is an item in the sequence produced by the iterable, on which expressions can be evaluated.

A *data source* is an abstract concept that represents a source of data that can be accessed via a iterable. A data source can be a file, a database, a web service, or any other source of data, depending on the type of iterable.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> There can be many different types of reference formulation. The known types, and the details of how a reference formulation is handled and implemented for each data format, are specified in [RML-IO-Registry]. Test cases are provided in as JSON files with JSONPath as reference formulation and `rml:FilePath` as access description, but it is not required to support these within this specification, any access description and reference formulation *MAY* be used in the test cases as long as the test case and expected output remains unchanged.

An *abstract logical source* (`rml:AbstractLogicalSource`) is a sub-class of iterable that can be associated with a triples map such that a data source can be mapped to RDF triples.

## 6. Mapping to RDF with Triples Maps

A *triples map* specifies a set of rules for translating each iteration of a logical source to zero or more RDF triple.

All RDF triples generated from one logical iteration in the logical source share the same subject.

A triples map is represented by a resource that references the following other resources:

- It *MUST* have zero or one logical source (`rml:logicalSource`) property whose value *MUST* be an instance of a sub-class of an abstract logical source (`rml:AbstractLogicalSource`).
- It *MUST* have exactly one subject map (`rml:SubjectMap`) that specifies how to generate a subject for each iteration of the logical source.
  It may be specified in two ways:
  1. using the subject map `rml:subjectMap` property, whose value *MUST* be the subject map, or
  2. using the constant shortcut property (`rml:subject`).
- It *MUST* have zero or more predicate-object map (`rml:predicateObjectMap`) properties, whose values *MUST* be predicate-object maps.
  They specify pairs of predicate maps and object maps that, together with the subjects generated by the subject map, may form one or more RDF triples for each iteration.

> **Note:**
>
> > **Note:**
> >
> > Note
>
> The logical source on a triples map can be omitted if all its term maps produce values irrespective of a logical source. This is the case if all its term maps are constant-valued expression maps, or have `rml:BlankNode` as term type and no declared expression.
> **Example:**
>
> Example 6: Usage of triples map
>
> The following example shows a triples map including its logical source, subject map and two predicate-object maps.
>
> ```
> <#TM>
>   rml:logicalSource [
>     rml:source [
>       a rml:RelativePathSource ;
>       rml:root rml:MappingDirectory ;
>       rml:path "images.json" ;
>     ] ;
>     rml:iterator "$.Images[*]" ;
>     rml:referenceFormulation rml:JSONPath ;
>   ] ;
>   rml:subjectMap [
>     rml:template "http://data.example.com/image/{$.ID}" ;
>   ] ;
>   rml:predicateObjectMap [
>     rml:predicate ex:height ;
>     rml:objectMap [
>       rml:reference "$.Height" ;
>     ] ;
>   ] ;
>   rml:predicateObjectMap [
>     rml:predicate ex:width ;
>     rml:objectMap [
>       rml:reference "$.Width" ;
>     ] ;
>   ] .
> ```

### 6.1 Creating Resources with Subject Maps

A *subject map* is a term map. It specifies a rule for generating the subjects of the RDF triples generated by a triples map.

### 6.2 Typing Resources (rml:class)

A *class IRI* is an IRI that denotes an RDFS class.
A subject map *MAY* have one or more class IRIs. They are represented by the `rml:class` property.
The values of the `rml:class` property *MUST* be IRIs.
For each RDF term generated by the subject map, RDF triples with predicate `rdf:type` and the class IRI as object will be generated.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Mappings where the class IRI is not constant,
> but needs to be computed based on the contents of the logical source,
> can be achieved by defining a predicate-object map with predicate `rdf:type` and a non-constant object map.

### 6.3 Creating Properties and Values with Predicate-Object Maps

A *predicate-object map* is a function that creates one or more predicate-object pairs for each logical iteration of a logical source.
It is used in conjunction with a subject map to generate RDF triples in a triples map.

A predicate-object map is represented by a resource that references the following other resources:

- One or more predicate maps. Each of them may be specified in one of two ways:

  1. using the `rml:predicateMap` property, whose value *MUST* be a predicate map, or
  2. using the constant shortcut property `rml:predicate`.

- One or more object maps or referencing object maps.
  Each of them may be specified in one of two ways:

  1. using the `rml:objectMap` property,
     whose value *MUST* be either an object map, or a referencing object map.
     using the constant shortcut property `rml:object`.

A *predicate map* is a term map.

An *object map* is a term map.

## 7. Generating values with expressions

*Expressions* are mapping constructs that can be evaluated on a logical iteration, according to the specified reference formulation, to generate values during the mapping process.

### 7.1 Expression map (`rml:ExpressionMap`)

An *expression map* (`rml:ExpressionMap`) is an abstract class, that is specialized by other RML classes. An expression map *MUST* have one the following properties:

- 0 or 1 `rml:constant`, or
- 0 or 1 `rml:reference`, or
- 0 or 1 `rml:template`, or
- another property, or properties, defined by a subclass of `rml:ExpressionMap`.

Each of these properties specifies an expression which, upon evaluation, results in a naturally ordered list of values (i.e., preserving the order in which they are produced by the iterations), called the *expression evaluation result*.

The *reference expression set* of an expression map is the set of expressions which are evaluated on a logical iteration.

#### 7.1.1 Constant expression (`rml:constant`)

A *constant-valued expression map* is an expression map that always generates the same expression evaluation result. A constant-valued expression map is represented by a resource that has exactly one `rml:constant` property, the value of which is called a *constant expression*.

The *constant value* is a singleton list containing the constant expression.

The reference expressions of a constant-valued expression map is an empty list.

#### 7.1.2 Reference (`rml:reference`)

A *reference-valued expression map* is an expression map that is represented by a resource that has exactly one `rml:reference` property, the value of which is called a *reference expression*.

The reference expression *MUST* be a valid expression according to the defined reference formulation in the logical source.

The reference expression set of a reference-valued expression map is the singleton set containing the reference expression.

The *reference value* is the expression evaluation result obtained by evaluating the reference expression against a given logical iteration.

#### 7.1.3 Template (`rml:template`)

A *template-valued expression map* is an expression map that is represented by a resource that has exactly one `rml:template` property, the value of which is called a *template expression*. The template expression *MUST* be a valid string template.

A *string template* is a format string that can be used to build strings from multiple components. It can apply reference expressions by enclosing them in curly braces (`{` and `}`). The following syntax rules apply to valid string templates:

- Pairs of unescaped curly braces *MUST* enclose valid reference expressions.
- Curly braces that do not enclose reference expressions *MUST* be escaped by a backslash character (`\`). This also applies to curly braces within reference expressions.
- Backslash characters (`\`) *MUST* be escaped by preceding them with another backslash character, yielding (`\\`). This also applies to backslashes within reference expressions.
- There *SHOULD* be at least one pair of unescaped curly braces.

The reference expression set of a template expression is the set of reference expressions enclosed in unescaped curly braces in the string template.

Sub classes of template-valued expression maps *MAY* define a *reference value transforming function* which will be applied to each reference value when evaluating the template.

The *template value* when evaluating a string template for a given logical iteration is determined as follows:

1. Let `result` be the reference expression set of the string template
2. For each reference expression in `result`:
   1. Let `values` be the reference value of the reference expression that is enclosed in the curly braces
   2. If `values` is an empty list, then return `NULL`
   3. For each `value` in `values`:
      1. Let `value` be the natural RDF lexical form corresponding to `value`
3. Let `result` be the n-ary Cartesian product of `result`
4. For each ordered list `product` in `result`:
   1. Let `template` be the string template
   2. For each pair of unescaped curly braces in `template`:
      1. Let `value` be the value at the index of `product` corresponding with the index of `value` in `template`
      2. If a reference value transforming function is applicable, let `value` be the value after applying the reference value transforming function
      3. Replace the pair of curly braces with `value`
   3. Let `product` be `template`
5. Return `result`

## 8. Term Maps

An *RDF term* is either an IRI, a blank node, or a literal.

A *term map* (`rml:TermMap`) is a rule that defines how to generate an RDF term from a logical iteration.
The result of the execution of that rule is the *generated RDF term*.

A term map is a sub-class of an expression map.

Term maps (`rml:TermMap`)
are used to generate the subjects, predicates and objects of the RDF triples that are generated by a triples map (`rml:TriplesMap`).
Consequently, there are several kinds of term maps (`rml:TermMap`).
Depending on where in the mapping they occur, a term map (`rml:TermMap`) can be:

- a subject map (`rml:SubjectMap`),
  if it is a rule that specifies how the RDF triple's subject is generated;
- a predicate map (`rml:PredicateMap`),
  if it is a rule that specifies how the RDF triple's predicate is generated;
- an object map (`rml:ObjectMap`),
  if it is a rule that specifies how the RDF triple's object is generated; and
- a graph map (`rml:GraphMap`),
  if it is a rule that specifies how the RDF triple's named graph is generated.
- a datatype map (`rml:DatatypeMap`),
  if it is a rule that specifies how the datatype IRI's of an object is generated.

A term map generates different types of RDF terms depending on the position of the term map in the RDF triple:

- a subject map (`rml:SubjectMap`)
  is a rule that *MUST* generate either an IRI, or a blank node;
- a predicate map (`rml:PredicateMap`)
  is a rule that *MUST* generate an IRI;
- an object map (`rml:ObjectMap`)
  is a rule that *MUST* generate an IRI, a blank node or a literal;
- a graph map (`rml:GraphMap`)
  is a rule that *SHOULD* generate an IRI.
- a datatype map (`rml:DatatypeMap`)
  is a rule that *MUST* generate an IRI.

A term map *MUST* have

- 0 or 1 datatype map or 0 or 1 language map;
- 0 or 1 term type.

### 8.1 Constant RDF Terms (`rml:constant`)

A *constant-valued term map* is a term map that ignores the logical iteration and always generates the same RDF term. A constant-valued term map is a constant-valued expression map, and is thus represented by a resource that has exactly one `rml:constant` property. The constant expression *MUST* be a valid RDF term.

The constant value of the `rml:constant` property is the generated RDF Term.

#### 8.1.1 Shortcuts for constant-valued term maps

Constant-valued term maps can be expressed more concisely
using the *constant shortcut properties* `rml:subject`, `rml:predicate`, `rml:object`, and `rml:graph` for the term maps, and `rml:datatype` and `rml:language` for the datatype map and language map respectively.
Occurrences of these properties *MUST* be treated exactly as if
the following triples were present in the mapping graph instead:

| Triple involving constant shortcut property | Replacement triples                        |
| ------------------------------------------- | ------------------------------------------ |
| `?x rml:subject ?y.`                        | `?x rml:subjectMap [ rml:constant ?y ].`   |
| `?x rml:predicate ?y.`                      | `?x rml:predicateMap [ rml:constant ?y ].` |
| `?x rml:object ?y.`                         | `?x rml:objectMap [ rml:constant ?y ].`    |
| `?x rml:graph ?y.`                          | `?x rml:graphMap [ rml:constant ?y ].`     |
| `?x rml:datatype ?y.`                       | `?x rml:datatypeMap [ rml:constant ?y ].`  |
| `?x rml:language ?y.`                       | `?x rml:languageMap [ rml:constant ?y ].`  |

### 8.2 Reference (`rml:reference`)

A *reference-valued term map* is a reference-valued expression map, and is thus represented by a resource that has exactly one `rml:reference` property.

The evaluation of a reference-valued expression map against a given logical iteration produces a reference value. For each value in the list, an RDF term is created. If the reference value is an empty list, then there will be no generated RDF term.
> **Example:**
>
> Example 7: Usage of reference-valued term map
>
> The following example defines a predicate-object map that generates RDF triples with the `ex:keyword` predicate and the `Keywords` value from the `images.json` input data source from Example 1.
>
> ```
> <#ImageTriplesMap>
>   rml:predicateObjectMap [
>     rml:predicate ex:keyword ;
>     rml:objectMap [
>       rml:reference "$.Keywords" ;
>     ] ;
>   ] .
> ```
>
> Using the logical iteration, the reference value of the object map is:
>
> ```
> ["building", "city", "view"]
> ```
>
> The RDF triples generated by the predicate-object map are:
>
> ```
> <http://data.example.com/image/116> ex:keyword "building" .
> <http://data.example.com/image/116> ex:keyword "city" .
> <http://data.example.com/image/116> ex:keyword "view" .
> ```

### 8.3 Template (`rml:template`)

A *template-valued term map* is a template-valued expression map, and is thus represented by a resource
that has exactly one `rml:template` property.

If the template value returned by the template-valued expression map is an empty list, no RDF term will be created.

#### 8.3.1 IRI encoding

If the term type of the template-valued term map is `rml:IRI`, then a reference value transforming function *MUST* be applied during the evaluation of the template expression. The reference value transforming function *MUST* transform a reference value into an IRI-safe version of that value.

The *IRI-safe version* of a string is obtained by applying the following transformation
to any character that is not in the [`iunreserved` production](http://tools.ietf.org/html/rfc3987#section-2.2) in [RFC3987]:

1. Convert the character to a sequence of one or more octets using [UTF-8](http://tools.ietf.org/html/rfc3629) in [RFC3629]
2. Percent-encode each octet

If the term type of the template-valued term map is `rml:URI`, then a reference value transforming function *MUST* be applied during the evaluation of the template expression. The reference value transforming function *MUST* transform a reference value into a URI-safe version of that value.

The *URI-safe version* of a string is obtained by applying the following transformation to any character that is
not in the [`unreserved` production](https://www.rfc-editor.org/rfc/rfc3986#section-2.3) in [RFC3986]:

1. Convert the character to a sequence of one or more octets using [UTF-8](http://tools.ietf.org/html/rfc3629) in [RFC3629]
2. Percent-encode each octet

The following table shows examples of strings and their IRI-safe and URI-safe versions:

| String               | IRI-safe version         | URI-safe version         |
| -------------------- | ------------------------ | ------------------------ |
| 42                   | 42                       | 42                       |
| Hello World!         | Hello%20World%21         | Hello%20World%21         |
| 2011-08-23T22:17:00Z | 2011-08-23T22%3A17%3A00Z | 2011-08-23T22%3A17%3A00Z |
| ~A_17.1-2¢           | ~A_17.1-2¢               | ~A_17.1-2%C2%A2          |
| Zoë Krüger           | Zoë%20Krüger             | Zo%C3%AB%20Kr%C3%BCger   |

> **Note:**
>
> > **Note:**
> >
> > Note
>
> RML always performs percent-encoding when IRIs are generated from string templates.
> If IRIs need to be generated without percent-encoding, then the term map *MUST* use `rml:UnsafeIRI` as term type.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Term maps with term type `rml:IRI` cause data errors if the value is not a valid IRI (see generated RDF term for details).
> Data values from the input data source may require percent-encoding before they can be used in IRIs. Template-valued term maps are a convenient way of percent-encoding data values.
> **Example:**
>
> Example 8: Usage of template-valued term map
>
> The following example defines a subject map that generates IRIs from the `ID` of the `images.json` input data source from Example 1.
>
> ```
> <#ImageTriplesMap>
>   rml:subjectMap [
>     rml:template "http://data.example.com/image/{$.ID}" ;
>   ] .
> ```
>
> Using the logical iteration, the template value of the subject map would be:
>
> ```
> <http://data.example.com/image/116>
> ```
> **Example:**
>
> Example 9: IRI-safe template values
>
> The following example shows how an IRI-safe template value is created.
> Here the `album.json` input data source is used to generate an IRI using the `Author` name.
>
> ```
> <#AuthorTriplesMap>
>   rml:subjectMap [
>     rml:template "http://data.example.com/author/{$.Author}" ;
>   ] .
> ```
>
> Using the logical iteration, the template value of the subject map would be:
>
> ```
> <http://data.example.com/author/Zoë%20Krüger>
> ```
>
> The space character is not in the [`iunreserved` production](http://tools.ietf.org/html/rfc3987#section-2.2), and therefore percent-encoding is applied to the character, yielding "`%20`".
> **Example:**
>
> Example 10: IRI unsafe template values
>
> The following example shows how an IRI unsafe template value is created.
> Here the `album.json` input data source is used to generate an IRI using the `Author` name.
>
> ```
> <#AuthorTriplesMap>
>   rml:subjectMap [
>     rml:template "http://data.example.com/author/{$.Author}" ;
>     rml:termType rml:UnsafeIRI
>   ] .
> ```
>
> Using the logical iteration, the template value of the subject map would be:
>
> ```
> <http://data.example.com/author/Zoë Krüger>
> ```
> **Example:**
>
> Example 11: Backslash escapes in templates
>
> The following example shows the use of backslash escapes in string templates. The template will generate a fancy title such as
>
> ```
> "{{{ \o/ Hello World! \o/ }}}"
> ```
>
> from a string "Hello World!" in the `Title` reference. By default, `rml:template` generates IRIs. Since the intention here is to create a literal instead, the term type has to be set.
>
> ```
> <#TriplesMap>
>   rml:objectMap [
>     rml:template "\\{\\{\\{ \\\\o/ {Title} \\\\o/ \\}\\}\\}" ;
>     rml:termType rml:Literal ;
>   ] .
> ```
>
> Note that because [backslashes need to be escaped by a second backslash in the Turtle syntax](https://www.w3.org/TR/turtle/#string) [TURTLE], a double backslash is needed to escape each curly brace, and to get one literal backslash in the output one needs to write four backslashes in the template.

### 8.4 IRIs, URIs, Literal, Blank Nodes (rml:termType)

The *term type* of a reference-valued term map or template-valued term map determines the kind of generated RDF term (IRIs, URI, blank nodes or literals).

If the term map has an optional `rml:termType` property,
then its term type is the value of that property.
The value *MUST* be an IRI and *MUST* be one of the following options:

- If the term map is a subject map: `rml:IRI`, `rml:URI` or `rml:BlankNode`
- If the term map is a predicate map: `rml:IRI`, `rml:URI`
- If the term map is an object map: `rml:IRI`, `rml:URI`, `rml:BlankNode`, or `rml:Literal`
- If the term map is a graph map: `rml:IRI`, `rml:URI`

#### 8.4.1 Default Term Types

If the term map does not have a `rml:termType` property, then its term type is:

- `rml:IRI`, if it is a subject map, predicate map or graph map
- `rml:Literal`, if it is an object map and at least one of the following conditions is true (`rml:IRI`, otherwise):
  * It is a reference-valued term map.
  * It has a `rml:languageMap` property (and thus a specified language tag).
  * It has a `rml:datatypeMap` property (and thus a specified datatype).

#### 8.4.2 Explicitly Defined Term Types

To change the default term type of a subject map or graph map to a blank node, the term type *MUST* be explicitly defined to be a `rml:BlankNode` or `rml:URI.

To change the default term type of an object map, the term type *MUST* be explicitly defined:

- If the term type is `rml:IRI`, an IRI will be generated`;`
- If the term type is `rml:URI`, a URI will be generated`;`
- If the term type is `rml:BlankNode`, a blank node will be generated.

If the term type is explicitly defined to be a `rml:BlankNode`,
a term map *MAY* not have an expression map.
Then an RML Processor *MUST* generate a random value for the blank node.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Term maps with term type `rml:IRI` cause data errors if the value is not a valid IRI (see generated RDF term for details).
> Data values from the logical source may require percent-encoding before they can be used in IRIs. Template-valued term maps are a convenient way of percent-encoding data values.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Constant-valued term maps are not considered as having a term type, and specifying `rml:termType` on these term maps has no effect.
> The type of the generated RDF term is determined directly by the value of `rml:constant`: If it is an IRI, then an IRI will be generated; if it is a literal, a literal will be generated.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> Constant-valued term maps are only allowed to be IRIs and literals. Blank nodes are explicitly not allowed. The reason for this is that blank node identifiers are always locally scoped to the file or RDF store, and are not persistent or portable identifiers [rdf11-concepts-20140225]. This means that they cannot be used as a constant expression, since the idea of a constant expression is to use that same constant value as the result of a mapping process. By definition, a blank node identifier cannot be ported from a mapping document to a mapping result.

### 8.5 Language tags (`rml:languageMap` and `rml:language`)

A *language-taggable term map* is a term map with a term type of `rml:Literal` that does not have a specified datatype map.

A language-taggable term map *MAY* be associated with a language map.

A *language map* (`rml:LanguageMap`) is an expression map. It specifies a rule for generating one or more language tags for a language-taggable term map. Following [rdf11-concepts-20140225], the generated language tags *MUST* be well-formed according to [BCP47].

Given the list of values resulting from a language-taggable term map `T`, and the list of values resulting from its language map `L`, the resulting terms are generated by the n-ary Cartesian product combination of `T × L`, where the values in `T` are the lexical forms, and the values in `L` are the non-empty language tags.

Each combination of `T × L` causes the generation of a language-tagged string.
> **Example:**
>
> Example 12: Usage of language map
>
> In the following example the lexical form values generated by reference `"Title.value"` are combined with the well-formed language tag values from reference `"Title.lang"` on the `images.json` input data source from Example 1 to generate a output with a language-tagged string.
>
> ```
> <#ImageTriplesMap>
>   rml:predicateObjectMap [
>     rml:predicate ex:title ;
>     rml:objectMap [
>       rml:reference "$.Title.Value" ;
>       rml:languageMap [
>         rml:reference "$.Title.Lang" ;
>       ] ;
>     ] ;
>   ] .
> ```
>
> This creates the following RDF triples.
>
> ```
> <http://data.example.com/image/116> ex:title "View from 15th Floor"@en .
> ```
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The generation of language-taggable term map in cases where the language map and its associated term map require correlated or non-trivial iteration patterns (e.g., alignment of multiple references or nested structures) falls
> outside the scope of this specification.
>
> Such advanced iteration behaviour *SHOULD* be handled using the mechanisms defined in the [RML-LV](https://w3id.org/rml/lv/spec/),
> which extends RML-Core with logical views and fine-grained control over iteration and data correlation.

### 8.6 Datatypes of Literals (`rml:datatypeMap` and `rml:datatype`)

A *datatypeable term map* is a term map with a term type of `rml:Literal` that does not have a specified language map.

Datatypeable term maps *MUST* generate zero or more literals. The datatype of these literals can be automatically determined with a natural mapping (producing a natural RDF literal), or it can be explicitly specified using a datatype map (producing a datatype-override RDF literal).

A *datatype map* (`rml:DatatypeMap`) is a term map. It specifies a rule for generating one or more datatypes for a datatypeable term map. A datatype map *MUST* generate a list of IRI values, in which the IRIs are the datatype IRIs of the datatypeable term map.

Given the list of values resulting from a datatypeable term map `T`, and the list of values resulting from its datatype map `D`, the resulting terms are generated by the n-ary Cartesian product combination of `T × D`, where the values in `T` are the literal values, and the values in `D` are the datatype IRIs.
> **Example:**
>
> Example 13: Usage of datatype map
>
> In the following example the literal values generated by reference `"CreatedDate"` are combined with the datatype values from the template with the `DateFormat` reference to generate a datatype-override RDF literal.
>
> ```
> <#ImageTriplesMap>
>   rml:predicateObjectMap [
>     rml:predicate ex:createdOn ;
>     rml:objectMap [
>       rml:reference "$.CreatedDate" ;
>       rml:datatypeMap [
>         rml:template "http://www.w3.org/2001/XMLSchema#{$.DateFormat}" ;
>       ] ;
>     ] ;
>   ] ;
> ```
>
> This creates the following RDF triples.
>
> ```
> <http://data.example.com/image/116> ex:createdOn "2023-10-01"^^xsd:date .
> ```

A datatypeable term map *MUST* have zero or one datatype maps, which can be specified in two ways:

1. using the `rml:datatypeMap` property, whose value *MUST* be a datatype map, or
2. using the constant shortcut property `rml:datatype`.

A term map that is not a datatypeable term map *MUST NOT* have an `rml:datatypeMap` or `rml:datatype` property.

See generated RDF term for further details on generating literals from term maps.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> One cannot explicitly state that a literal without language tag should be generated.
> To generate one from a non-string reference value,
> a template-valued term map with a template such as `"{MY_REFERENCE}"` and a term type of `rml:Literal` can be used.
> **Example:**
>
> Example 14: Datatype-override
>
> The following example shows a predicate-object map with an object map that explicitly specifies `xsd:positiveInteger` type.
> A datatype-override RDF literal of that datatype will be generated when applied to the `images.json` input data source from Example 1.
>
> ```
> <#ImageTriplesMap>
>   rml:predicateObjectMap [
>     rml:predicate ex:id ;
>     rml:objectMap [
>       rml:reference "$.ID" ;
>       rml:datatype xsd:positiveInteger ;
>     ] ;
>   ] ;
> ```
>
> This creates the following RDF triples.
>
> ```
> <http://data.example.com/image/116> ex:id "116"^^xsd:positiveInteger .
> ```

## 9. Joins

A referencing object map allows using the subject generated by the subject map (`rml:SubjectMap`) of the referenced triples map (`rml:TriplesMap`).
Since the two triples maps may be based on different logical sources (`rml:LogicalSource`), this may require a join between the logical sources. This is not restricted to 1:1 joins.

### 9.1 Referencing Object Map

A *referencing object map* (`rml:ReferencingObjectMap`) is represented by a resource that *MUST* have:

- exactly one parent triples map (`rml:parentTriplesMap`) property,
  whose value *MUST* be a triples map, known as the referencing object map's *parent triples map*.
- one or more join condition (`rml:joinCondition`) properties, whose values *MUST* be join conditions.

The referencing object map causes the generation of new object which is constructed with the subject generated by evaluating the parent triples map.
> **Example:**
>
> Example 15: Usage of referencing object map
>
> This example shows a referencing object map as part of a predicate-object map in a triples map mapping the `ex:hasThumbnail` property of the image.
> Since the source data for the thumbnail is part of the same logical iteration as for the image, the logical source is identical, and thus effectively equal, to the logical source of the parent triples map, and no join condition is needed.
>
> ```
> <#ImageTriplesMap>
>   rml:predicateObjectMap [
>     rml:predicate ex:hasThumbnail ;
>     rml:objectMap [
>       rml:parentTriplesMap <#ThumbnailTriplesMap> ;
>     ] ;
>   ] .
>
> <#ThumbnailTriplesMap>
>   rml:logicalSource <#ImageLogicalSource> ;
>   rml:subjectMap [
>     rml:reference "$.Thumbnail.Url" ;
>     rml:termType rr:IRI ;
>   ] .
> ```
>
> The following RDF triples are generated by the RML mapping above.
>
> ```
> <http://data.example.com/image/116> ex:hasThumbnail <http://data.example.com/image/116/thumbnail> .
> ```

### 9.2 Join Condition

A *join condition* is represented by a resource that has exactly one value for each of the following two properties:

- a child map (`rml:childMap`) property, whose value is a child map, or a constant-valued expression map.
  A *child map* (`rml:ChildMap`) is an expression map which *MUST* be evaluated against the child logical source. The *child logical source* is the logical source of the triples map that contains the referencing object map, i.e. the current triples map..

- a parent map (`rml:parentMap`) property, whose value is a parent map, or a constant-valued expression map.
  A *parent map* (`rml:ParentMap`) is an expression map, which *MUST* be evaluated against the parent logical source. The *parent logical source* is the logical source of the referencing object map's parent triples map, i.e. the referenced triples map.

If the the logical source of the triples map that contains the referencing object map and the logical source of the referencing object map's parent triples map are not effectively equal, then the referencing object map *MUST* have one or more join conditions.

A join condition is satisfied if the result of evaluating the child map against the logical source of the current triples map is equal to the result of evaluating the parent map against the logical source of the referenced triples map.

If a referencing object map has multiple join conditions, then all of them *MUST* be satisfied for the referencing object map to be evaluated.

A mapping component is *effectively equal* to another mapping component if they are identical, or if all their corresponding effective properties have the same values, recursively comparing values that are resources that have properties as well.

An *effective property* of a mapping component is a property that has an effect on the mapping process.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> The effective properties of a mapping component are the properties that are used in the mapping process, and are defined by this specification or other specifications that extend this specification.
> **Example:**
>
> Example 16: Usage of join condition
>
> This example shows a referencing object map as part of a predicate-object map, where the logical sources of the two triples maps are not effectively equal. Therefore, a join condition is needed to join the two logical iterations.
>
> ```
> <#AlbumTriplesMap>
>   rml:predicateObjectMap [
>     rml:predicate ex:hasImage ;
>     rml:objectMap [
>       rml:parentTriplesMap <#ImageTriplesMap> ;
>       rml:joinCondition [
>         rml:childMap [
>           rml:reference "$.Images[*].ID" ;
>         ] ;
>         rml:parentMap [
>           rml:reference "$.ID" ;
>         ] ;
>       ] ;
>     ] ;
>   ] .
> ```
>
> The following RDF triples are generated by the RML mapping above, since the first `ID` field in the `Images` array of the `album.json` input source is joined with the `ID` field in the `images.json` input source.
>
> ```
> <http://data.example.com/album/43> ex:hasImage <http://data.example.com/image/116> .
> ```
> **Example:**
>
> Example 17: Reference object map for non-identical, but effectively equal, logical sources
>
> This example shows a referencing object map as part of a predicate-object map, where the logical sources of the two triples maps are not identical, but are effectively equal. Therefore, no join condition is needed to join the two logical iterations.
>
> ```
> <#ImageTriplesMap>
>   rml:predicateObjectMap [
>     rml:predicate ex:hasThumbnail ;
>     rml:objectMap [
>       rml:parentTriplesMap <#ThumbnailTriplesMap2> ;
>     ] ;
>   ] .
>
> <#ThumbnailTriplesMap2>
>   rml:logicalSource [
>     rdfs:label "Thumbnail source" ;
>     rml:source [
>       a rml:RelativePathSource ;
>       rml:root rml:MappingDirectory ;
>       rml:path "images.json" ;
>     ] ;
>     rml:iterator "$.Images[*]" ;
>     rml:referenceFormulation rml:JSONPath ;
>   ] ;
>   rml:subjectMap [
>     rml:reference "$.Thumbnail.Url" ;
>     rml:termType rr:IRI ;
>   ] .
> ```
>
> The rml:logicalSource of `<#ThumbnailTriplesMap2>` is different from the rml:logicalSource `<#ImageLogicalSource>` of `<#ImageTriplesMap>` as defined in Example 3, but they are effectively equal, since all effective properties are the same. The following properties are effective in this case:
>
> - `rml:source` - defined in [RML-IO]
>   * `rml:root` - defined in [RML-IO]
>   * `rml:path` - defined in [RML-IO]
> - `rml:iterator` - the iterator
> - `rml:referenceFormulation` - the reference formulation
> The `rdfs:label` is not an `effective property` and is not considered in the comparison.
>
> Note also that the logical source node from Example 3 is named with an IRI `<#ImageLogicalSource>`, and the logical source for `<#ThumbnailTriplesMap2>` is named with a blank node. The name of a resource has no effect on the mapping process and is not considered in the comparison.

#### 9.2.1 Shortcuts for reference-valued child map and parent map

If the child map is a reference-valued expression map, then the `rml:child` shortcut could be used.

Similarly, if the parent map is a reference-valued expression map, then the `rml:parent` shortcut could be used.

Occurrences of these properties *MUST* be treated exactly as if the following triples were present in the mapping graph instead:

| Triple involving reference shortcut property | Replacement triples                      |
| -------------------------------------------- | ---------------------------------------- |
| `?x rml:child ?y.`                           | `?x rml:childMap [ rml:reference ?y ].`  |
| `?x rml:parent ?y.`                          | `?x rml:parentMap [ rml:reference ?y ].` |

> **Example:**
>
> Example 18: Usage of shortcut properties for child map and parent map
>
> ```
> <#AlbumTriplesMap>
>   rml:predicateObjectMap [
>     rml:predicate ex:hasImage ;
>     rml:objectMap [
>       rml:parentTriplesMap <#ImageTriplesMap> ;
>       rml:joinCondition [
>         rml:child "$.Images[*].ID" ;
>         rml:parent "$.ID" ;
>       ] ;
>     ] ;
>   ] .
> ```

## 10. Assigning Triples to Named Graphs

Each triple generated from an RML mapping is placed into one or more graphs of the output dataset. Possible target graphs are the unnamed default graph, the IRI-named named graphs, and blank node named named graphs

Any subject map or predicate-object map *MUST* have zero or more associated *graph maps*. They are specified in one of two ways:

1. using the `rml:graphMap` property, whose value *MUST* be a graph map,
2. using the constant shortcut property `rml:graph`.

Graph maps are themselves term maps. When RDF triples are generated, the set of target graphs is determined by taking into account any graph maps associated with the subject map or predicate-object map.

If a graph map generates the special IRI `rml:defaultGraph`, then the target graph is the default graph of the output dataset.
> **Example:**
>
> Example 19: Usage of graph maps
>
> In the following subject map example, all generated RDF triples will be stored in the named graph `ex:AlbumGraph`.
>
> ```
> <#ImageTriplesMap>
>   rml:subjectMap [
>     rml:template "http://data.example.com/image/{$.ID}" ;
>     rml:graphMap [ rml:constant ex:AlbumGraph ] ;
>   ] .
> ```
>
> This is equivalent to the following example, which uses a constant shortcut property:
>
> ```
> <#ImageTriplesMap>
>   rml:subjectMap [
>     rml:template "http://data.example.com/image/{$.ID}" ;
>     rml:graph ex:AlbumGraph ;
>   ] .
> ```
>
> In the following example, RDF triples are placed into a IRI-named named graphs according to `ID` of the images:
>
> ```
> <#ImageTriplesMap>
>   rml:subjectMap [
>     rml:template "http://data.example.com/image/{$.ID}" ;
>     rml:graphMap [
>       rml:template "http://data.example.com/graph/{$.ID}" ;
>     ] ;
>   ] .
> ```
>
> However, in this example, RDF triples of the predicate `ex:title` are placed into blank node named graphs according to `ID` of the images:
>
> ```
> <#ImageTriplesMap>
>   rml:subjectMap [
>     rml:template "http://data.example.com/image/{$.ID}" ;
>   ] ;
>   rml:predicateObjectMap [
>     rml:predicate ex:title ;
>     rml:objectMap [
>       rml:reference "$.Title.Value" ;
>     ] ;
>     rml:graphMap [
>       rml:reference "$.ID" ;
>       rml:termType rml:BlankNode ;
>     ] ;
>   ] .
> ```

### 10.1 Scope of Blank Nodes

Blank nodes in the output dataset are scoped to a single RDF graph. If the same blank node identifier occurs in multiple RDF triples that are in the same graph, then the triples will share the same blank node. If, however, the same blank node identifier occurs in multiple graphs, then a distinct blank node be created for each graph. An RML-generated blank node can never be shared by two triples in two different graphs.

This implies that triples generated from a single logical source row will have different subjects if the subjects are blank nodes and the triples are placed into different graphs.

## 11. Datatype conversions

For each reference formulation there may be a set of defined *natural RDF mappings* that are applied to the expression evaluation results on the data source. These natural mappings are defined in the [RML-IO-Registry] and are used to convert the values of the expression evaluation result to the appropriate natural RDF literal corresponding with the reference formulation.

### 11.1 Natural mapping of source values

The *natural RDF literal* is a literal obtained by applying a natural mapping on a value from a data source, resulting in the most appropriate representation of that value in RDF. The natural RDF literal has a natural RDF lexical form.

The *natural RDF lexical form* is the lexical form of the literal on which implementations *SHOULD* apply the XSD canonical mapping, making it a canonical RDF lexical form. It is used in RML when non-string expression evaluation results are used in a string context, for example when a timestamp is used in an template-valued term map with term type IRI.

The *canonical RDF lexical form* is the lexical form of the literal on which the XSD canonical mapping *MUST* be applied.

*Cast to string* is an implementation-dependent function that maps values from expression evaluation results to equivalent Unicode strings. The specifics of cast to string per reference formulation are defined in the [RML-IO-Registry].

Additionally, the natural mapping determines the natural RDF datatype of the literal.

The *natural RDF datatype* is the datatype corresponding to the natural RDF literal that is the result of the natural mapping. The natural RDF datatype is an IRI that represents the datatype of the value in RDF.

### 11.2 Datatype-override mapping of source values

The *datatype-override RDF literal* corresponding to an expression evaluation result value `v` and a datatype IRI `dt`, is a literal whose lexical form is the natural RDF lexical form corresponding to `v`, and whose datatype IRI is `dt`. If the literal is ill-typed, then a data error is raised.

A literal is *ill-typed* in RML if its datatype IRI denotes a validatable RDF datatype and its lexical form is not in the lexical space of the RDF datatype identified by its datatype IRI.

The set of *validatable RDF datatypes* includes all datatypes in the RDF datatype column of Table 1, as defined in [XMLSCHEMA11-2]. This set *MAY* include implementation-defined additional RDF datatypes.

For example, `"X"^^xsd:boolean` is ill-typed because `xsd:boolean` is a validatable RDF datatype in RML, and `"X"` is not in the lexical space of `xsd:boolean` [XMLSCHEMA11-2].

### 11.3 Summary of XSD Lexical Forms

*This section is non-normative.*

The natural mappings make reference to various XSD datatypes and require that values from expression evaluation results be converted to strings that are appropriate as lexical forms for these datatypes. This subsection gives examples of these lexical forms in order to aid implementers of the mappings. This subsection is non-normative; the normative definitions of the lexical spaces as well as the canonical mappings are found in [XMLSCHEMA11-2].

A general approach that may be used for implementing the natural mappings is as follows:

1. Identify the source datatype of value of the expression evaluation result on the data source.
2. Look up its corresponding natural RDF datatype for the reference formulation in the [RML-IO-Registry].
3. Apply cast to string to the value.
4. Ensure that the resulting string is in the lexical space of the target RDF datatype; that is, it must be in a form such as those listed in either column of Table 1 below. This may require some transformations of the string, in particular for `xsd:hexBinary`, `xsd:dateTime` and `xsd:boolean`.
5. If the goal is to obtain a canonical RDF lexical form, then further string transformations may be required to obtain a form such as those listed in the Canonical lexical forms column of Table 1 below.

*Table 1 Table of canonical and non\-canonical lexical forms for some XSD datatypes*

| RDF datatype    | Non-canonical lexical forms     | Canonical lexical forms | Comments                                                                                                        |
| --------------- | ------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------- |
| `xsd:hexBinary` | `5232524d4c`                    | `5232524D4C`            | Convert from SQL by applying [`xsd:hexBinary` lexical mapping](https://www.w3.org/TR/xmlschema11-2/#hexBinary). |
| `xsd:decimal`   | `.224`                          | `0.224`                 |                                                                                                                 |
|                 | `+001`                          | `1`                     |                                                                                                                 |
|                 | `42.0`                          | `42`                    |                                                                                                                 |
|                 | `-5.9000`                       | `-5.9`                  |                                                                                                                 |
| `xsd:integer`   | `-05`                           | `-5`                    |                                                                                                                 |
|                 | `+333`                          | `333`                   |                                                                                                                 |
|                 | `00`                            | `0`                     |                                                                                                                 |
| `xsd:double`    | `-5.90`                         | `-5.9E0`                | Also supports `INF`, `-INF`, `NaN` and `-0.0E0`, but these do not appear in standard SQL.                       |
|                 | `+0.00014770215000`             | `1.4770215E-4`          |                                                                                                                 |
|                 | `+01E+3`                        | `1.0E3`                 |                                                                                                                 |
|                 | `100.0`                         | `1.0E2`                 |                                                                                                                 |
|                 | `0`                             | `0.0E0`                 |                                                                                                                 |
| `xsd:boolean`   | `1`                             | `true`                  | Must be lowercase.                                                                                              |
|                 | `0`                             | `false`                 |                                                                                                                 |
| `xsd:date`      |                                 | `2011-08-23`            | Dates in SQL don't have timezone offsets. They are optional in XSD.                                             |
| `xsd:time`      | `22:17:34.885+00:00`            | `22:17:34.885Z`         | May or may not have timezone offset.                                                                            |
|                 | `22:17:34.000`                  | `22:17:34`              |                                                                                                                 |
|                 | `22:17:34.1+01:00`              | `22:17:34.1+01:00`      |                                                                                                                 |
| `xsd:dateTime`  | `2011-08-23T22:17:00.000+00:00` | `2011-08-23T22:17:00Z`  | May or may not have timezone offset. Convert from SQL by replacing space with "`T`".                            |

## 12. The Output Dataset

The *output dataset* of an RML mapping is an RDF dataset that contains the generated RDF triples for each of the triples maps of the RML mapping.
The output dataset *MUST NOT* contain any other RDF triples or named graphs besides these.
However, RML processors *MAY* provide access to datasets that contain additional triples or graphs beyond those in the output dataset, such as inferred triples or provenance information.

Conforming RML processors *MAY* rename blank nodes when providing access to the output dataset.
This means that client applications may see actual blank node identifiers that differ from those produced by the RML mapping.
Client applications *SHOULD NOT* rely on the specific text of the blank node identifier for any purpose.
> **Note:**
>
> > **Note:**
> >
> > Note
>
> RDF syntaxes and RDF APIs generally represent blank nodes with blank node identifiers. But the characters allowed in blank node identifiers differ between syntaxes, and not all characters occurring in the values produced by a term map may be allowed, so a bijective mapping function from values to valid blank node identifiers may be required. The details of this mapping function are implementation-dependent, and RML processors may have to use different functions for different output syntaxes or access interfaces. Strings matching the regular expression `[a-zA-Z_][a-zA-Z_0-9-]*` are valid blank node identifiers in all W3C-recommended RDF syntaxes (as of this document's publication).
> **Note:**
>
> > **Note:**
> >
> > Note
>
> RDF datasets may contain empty named graphs. RML cannot generate such output datasets.

### 12.1 The Generated RDF Triples of a Triples Map

This subsection describes the process of *generating RDF triples* from a Triples Map. This process contributes RDF triples to the output dataset. Each generated triple *MUST* be placed into one or more graphs of the output dataset.

The generated RDF triples are determined by the following algorithm. RML Processors *MAY* employ alternative implementations to compute the generated RDF triples, provided that the resulting output dataset is semantically equivalent to the one obtained by this algorithm.

Let:

- **sm** be the subject map of the Triples Map.
- **iterations** be the set of logical iterations obtained by evaluating the logical source of the Triples Map using its declared reference formulation.
- **classes** be the set of class IRIs defined in **sm** (via `rml:class`).
- **sgm** be the set of graph maps attached to **sm**.

For each logical iteration **iteration** in **iterations**, apply the following steps:

1. Let subject be the generated RDF term resulting from applying **sm** to **iteration**.

2. Let **subject_graphs** be the set of generated RDF terms resulting from applying each graph map in **sgm** to **iteration**.

3. For each class IRI in **classes**, add a triple to the output dataset as follows:

    | Component     | Value                                                                    |
    | ------------- | ------------------------------------------------------------------------ |
    | Subject       | **subject**                                                              |
    | Predicate     | `rdf:type`                                                               |
    | Object        | class IRI                                                                |
    | Target graphs | If **sgm** is empty → `rml:defaultGraph`; otherwise → **subject_graphs** |

4. For each predicate-object map of the Triples Map, apply the following steps:

   - Let **predicates** be the set of generated RDF terms resulting from applying each predicate map of the predicate-object map to **iteration**.
   - Let **objects** be the set of generated RDF terms resulting from applying each object map (excluding referencing object maps) to **iteration**.
   - Let **pogm** be the set of graph maps of the predicate-object map.
   - Let **predicate_object_graphs** be the set of generated RDF terms resulting from applying each graph map in **pogm** to **iteration**.

   For each possible combination `<predicate, object>`, where *predicate* ∈ **predicates** and *object* ∈ **objects**, add a triple to the output dataset as follows:

    | Component     | Value                                                                                                                           |
    | ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
    | Subject       | **subject**                                                                                                                     |
    | Predicate     | *predicate*                                                                                                                     |
    | Object        | *object*                                                                                                                        |
    | Target graphs | If both **sgm** and **pogm** are empty → `rml:defaultGraph`; otherwise → union(**subject_graphs**, **predicate_object_graphs**) |

For each referencing object map of a predicate-object map in the Triples Map apply the following steps:

- Let **psm** be the subject map of the parent Triples Map referenced by referencing object map.
- Let **pogm** be the set of graph maps of the predicate-object map.
- Let **joined_iterations** be the result of evaluating the join conditions defined by the referencing object map, combining iterations from both the child logical source and parent logical sources.

For each pair `<child_iteration, parent_iteration>` in **joined_iterations**, apply the following steps:

1. Let **subject** be the generated RDF term resulting from applying **sm** to **child_iteration**.
2. Let **predicates** be the set of generated RDF terms resulting from applying each predicate map of the predicate-object map to **child_iteration**.
3. Let **object** be the generated RDF term resulting from applying **psm** to **parent_iteration**.
4. Let **subject_graphs** be the set of generated RDF terms resulting from applying each graph map in **sgm** to **child_iteration**.
5. Let **predicate_object_graphs** be the set of generated RDF terms resulting from applying each graph map in **pogm** to **child_iteration**.

For each *predicate* in **predicates**, add a triple to the output dataset as follows:

| Component     | Value                                                                                                                           |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Subject       | **subject**                                                                                                                     |
| Predicate     | *predicate*                                                                                                                     |
| Object        | **object**                                                                                                                      |
| Target graphs | If both **sgm** and **pogm** are empty → `rml:defaultGraph`; otherwise → union(**subject_graphs**, **predicate_object_graphs**) |

#### 12.1.1 Adding Triples to the Output Dataset

“Add triples to the output dataset” is a process that takes the following inputs:

| Input             | Description                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Subject**       | an IRI, blank node, or empty |
| **Predicate**     | an IRI, or empty                                                                                  |
| **Object**        | an RDF term or empty                                                                         |
| **Target graphs** | a set of zero or more IRIs                                                                        |

Execute the following steps:

1. If **Subject**, **Predicate**, or **Object** is empty, **abort** these steps.
2. Otherwise, generate an RDF triple `<Subject, Predicate, Object>`.
3. If the set of target graphs includes `rml:defaultGraph`, add the triple to the default graph of the output dataset.
4. For each IRI in the set of target graphs not equal to `rml:defaultGraph`, add the triple to the named graph identified by that IRI in the output dataset.
   - If the named graph does not yet exist, create it.

RDF graphs *MUST NOT* contain duplicate triples. Adding multiple identical triples to the same graph has the same effect as adding it once. Also note the 10.1 Scope of Blank Nodes (§10.1).

### 12.2 Generated RDF Term of a Term Map

A term map defines how an RDF term is generated from the evaluation of a logical iteration over a logical source.
The result of evaluating a term map for a given logical iteration can be one of the following:

- **Empty**, if the expression evaluation result of the term map evaluates to a null, empty or missing value (each data format defines it in [RML-IO-Registry](https://w3id.org/kg-construct/rml-io-registry/));
- **An RDF term**, when evaluation produces a valid RDF term according to the term generation rules;
- **A data error**, when a valid RDF term cannot be produced.

The generated RDF term of a term map for a given logical iteration is determined as follows:

1. If the term map is a constant-valued term map, then the generated RDF term is the term map’s constant value.
2. If the term map is a reference-valued term map, then the generated RDF term is determined by applying the term generation rules to its reference value.
3. If the term map is a template-valued term map, then the generated RDF term is determined by applying the term generation rules to the template value.

The *term generation rules* define how a concrete RDF term is generated from each value from an expression evaluation result:

1. **If the value is null, empty or missing**, then no RDF term is generated.

2. **If the term type is `rml:IRI` or `rml:UnsafeIRI`:**

   1. Let *value* be the natural RDF lexical form corresponding to the evaluated value.
   2. If *value* is a valid [absolute IRI](https://datatracker.ietf.org/doc/html/rfc3987#section-2.2) [RFC3987], then return an IRI generated from *value*.
   3. Otherwise, prepend *value* with the base IRI. If the result is a valid [absolute IRI](https://datatracker.ietf.org/doc/html/rfc3987#section-2.2) [RFC3987], then return that IRI.
   4. Otherwise, raise a **data error**.

3. **If the term type is `rml:URI` or `rml:UnsafeURI`:**

   1. Let *value* be the natural RDF lexical form corresponding to the evaluated value.
   2. If *value* is a valid absolute URI [RFC3986], then return an URI generated from *value*.
   3. Otherwise, prepend *value* with the base IRI. If the result is a valid absolute URI [RFC3986], then return that URI .
   4. Otherwise, raise a **data error**.

4. **If the term type is `rml:BlankNode`:**

   - If the term map has an expression map, return a blank node whose identifier is determined by the expression evaluation result.
   - If the term map has no expression map, generate a fresh blank node with a unique identifier.

5. **If the term type is `rml:Literal`:**

   - If the term map declares a language map, then evaluate the language map to obtain a language tag. If the result is a valid language tag according to [BCP47], return a literal with that language tag and the natural RDF lexical form corresponding to *value*. Otherwise, raise a **data error**.
   - Otherwise, if the term map declares a datatype map, then evaluate it to obtain a datatype-override RDF literal corresponding to *value* and the specified datatype.
   - Otherwise, return the natural RDF literal corresponding to *value*.

## 13. Definitions

*n-ary Cartesian product*

Given set `𝑋₁`, `...`, `𝑋ₙ`, the n-ary Cartesian product over *n* sets `𝑋₁`, `...`, `𝑋ₙ`, denoted `𝑋₁ × ... × 𝑋ₙ`, is defined as the set of all ordered lists of *n* elements `(𝑥₁ , ... , 𝑥ₙ)` such that `𝑥ₙ` belongs to `𝑋ₙ`.
For example, if `A = {1, 2}`, `B = {a, b, c}`, and `C = {Z}`, then the n-ary Cartesian product of A, B and C is `{(1, a, Z), (1, b, Z), (1, c, Z), (2, a, Z), (2, b, Z), (2, c, Z)}`.

## 14. Terminology

*This section is non-normative.*

### 14.1 RDF Terminology

This section lists some terms normatively defined in [RDF11-CONCEPTS] and used in RML:

- *[RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset)*
- *[RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph)*
- *[RDF triple](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-triple)*
- *[IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri)*
- *[base IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-base-iri)*
- *[blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)*
- *[blank node identifier](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node-identifier)*
- *[datatype](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype)*
- *[datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri)*
- *[default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph)*
- *[language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag)*
- *[language-tagged string](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string)*
- *[lexical form](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-form)*
- *[lexical space](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-space)*
- *[literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal)*
- *[named graph](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph)*
- *[node](https://www.w3.org/TR/rdf11-concepts/#dfn-node)*
- *[object](https://www.w3.org/TR/rdf11-concepts/#dfn-object)*
- *[predicate](https://www.w3.org/TR/rdf11-concepts/#dfn-predicate)*
- *[property](https://www.w3.org/TR/rdf11-concepts/#dfn-property)*
- *[resource](https://www.w3.org/TR/rdf11-concepts/#dfn-resource)*
- *[subject](https://www.w3.org/TR/rdf11-concepts/#dfn-subject)*

### 14.2 RDFS Terminology

This section lists some terms normatively defined in [RDF11-SCHEMA] and used in RML:

- *[RDFS class](https://www.w3.org/TR/rdf-schema/#ch_class)*

### 14.3 XML Schema Definition Language (XSD) Terminology

This section lists some terms normatively defined in [XMLSCHEMA11-2] and used in RML:

- *[XSD Datatype](https://www.w3.org/TR/xmlschema11-2/#datatype)*
- *[Canonical mapping](https://www.w3.org/TR/xmlschema11-2/#canonical-lexical-representation)*

### 14.4 Uniform Resource Identifier Terminology

This section lists some terms normatively defined in [RFC3986] and used in RML:

- *[URI](https://www.rfc-editor.org/rfc/rfc3986#section-1.1.3)*
- *[relative URIs](https://www.rfc-editor.org/rfc/rfc3986#section-5.2)*
- *[absolute URI](https://www.rfc-editor.org/rfc/rfc3986#section-4.3)*
- *[Percent-encode](https://www.rfc-editor.org/rfc/rfc3986#section-2.1)*

## A. References

### A.1 Normative references

[BCP47]

[Tags for Identifying Languages](https://www.rfc-editor.org/rfc/rfc5646). A. Phillips, Ed.; M. Davis, Ed. IETF. September 2009. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc5646>

[rdf11-concepts-20140225]

[RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/). Richard Cyganiak; David Wood; Markus Lanthaler. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/>

[RFC2119]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

[RFC3629]

[UTF-8, a transformation format of ISO 10646](https://www.rfc-editor.org/rfc/rfc3629). F. Yergeau. IETF. November 2003. Internet Standard. URL: <https://www.rfc-editor.org/rfc/rfc3629>

[RFC3986]

[Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986). T. Berners-Lee; R. Fielding; L. Masinter. IETF. January 2005. Internet Standard. URL: <https://www.rfc-editor.org/rfc/rfc3986>

[RFC3987]

[Internationalized Resource Identifiers (IRIs)](https://www.rfc-editor.org/rfc/rfc3987). M. Duerst; M. Suignard. IETF. January 2005. Proposed Standard. URL: <https://www.rfc-editor.org/rfc/rfc3987>

[RFC8174]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

[RML-IO-Registry]

[RML-IO Registry](http://w3id.org/rml/rml-io-registry). KGC-CG-W3C. 31 March 2025. Draft Community Group Report. URL: <http://w3id.org/rml/rml-io-registry>

[TURTLE]

[RDF 1.1 Turtle](https://www.w3.org/TR/turtle/). Eric Prud'hommeaux; Gavin Carothers. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/turtle/>

[XMLSCHEMA11-2]

[W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/). David Peterson; Sandy Gao; Ashok Malhotra; Michael Sperberg-McQueen; Henry Thompson; Paul V. Biron et al. W3C. 5 April 2012. W3C Recommendation. URL: <https://www.w3.org/TR/xmlschema11-2/>

### A.2 Informative references

[RDF11-CONCEPTS]

[RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). Richard Cyganiak; David Wood; Markus Lanthaler. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf11-concepts/>

[RDF11-SCHEMA]

[RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/). Dan Brickley; Ramanathan Guha. W3C. 25 February 2014. W3C Recommendation. URL: <https://www.w3.org/TR/rdf-schema/>

[RML-IO]

[RML-IO](https://w3id.org/rml/io/spec). KGC-CG. 12 February 2025. Draft Community Group Report. URL: <https://w3id.org/rml/io/spec>
