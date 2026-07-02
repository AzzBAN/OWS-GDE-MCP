---
title: "Rule: Metadata Information of the Data Stored in Data Cube of GDE Must Be Registered with MetaOne of Data Cube of GDE"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001237104689.html"
depth: 6
---
# Rule: Metadata Information of the Data Stored in Data Cube of GDE Must Be Registered with MetaOne of Data Cube of GDE

**Specification name**: General\_DataFactory\_Data\_Model\_Unified\_Metadata\_Registration\_Principle

**Description**: To meet the GTS data governance requirements, the metadata information of all data stored in Data Cube of GDE must be registered with the MetaOne service of Data Cube of GDE based on the metadata management specifications. The metadata registration methods are as follows:

-   Register metadata with MetaOne through RESTful APIs.

-   Install app packages through AppManager of GDE.
    
    The metadata information that can be registered includes: logical models (including logical entities, logical attributes, and entity relationships), physical models (including physical entities and physical attributes), and multidimensional models (including dimension models, indicator models, measure models, and aggregation models).
    

**Check guide**: View the metadata information through the MetaOne service.

**Negative example**: Metadata is managed offline.

**Positive example**: All products (such as SEQ Analyst, Discovery, and vCEM) in the GTS business experience domain store the business data in the data warehouse provided by Data Cube of GDE. The metadata of the business data is registered with MetaOne of GDE based on the metadata management specifications. The metadata can be registered by installing apps or calling service-oriented APIs.

**Impact**: Data without metadata description or lack of unified metadata management causes issues, such as scattered system assets and data inconsistency between apps.

**Parent topic:** [[Data Models|Data Models]]