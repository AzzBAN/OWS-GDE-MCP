---
title: "Suggestion: Set Orchestration Calling Principles"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001471355960.html"
depth: 6
---
# Suggestion: Set Orchestration Calling Principles

**Description**: All orchestrations comply with the unified MVC calling specifications. It is recommended that operations of the same type be exposed through the API layer after the orchestration is closed.

The following figure shows the orchestration overview of GDE.

![[en-us_image_0000002360258805.png]]

1\. Big data-related processing must be closed in data orchestration and exposed to other orchestrations through unified scheduling or query services.

2\. Small- and medium-scale (less than 10 million) raw data is stored in the OLTP data model. For long-term storage, you are advised to store the data in the OLAP model after data orchestration and batch processing.

3\. REST API integration is preferentially converted into internal or external standard protocols through API orchestration (API Fabric).

4\. It is recommended that interfaces exposed on pages be encapsulated through service orchestration.

5\. It is recommended that independent modules be defined for APIs used externally and the APIs be exposed to external systems in a centralized manner.

6\. Interfaces exposed to third-party heterogeneous systems are uniformly orchestrated using APIs and exposed to external systems through data integration.

7\. It is recommended that data exposure between assets be encapsulated through APIs. It is not recommended that model operations be directly exposed.

**Tool supported or not**: no

**Specification name**: General\_Basic\_Invoking\_Principle

**Severity**: suggestion

**Parent topic:** [[Principles|Principles]]