---
title: "Introduction to Model Flow Elements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_dataflow_002.html"
depth: 4
---
# Introduction to Model Flow Elements

The model flow function enables users to orchestrate multiple model operations into a process and schedule the process based on time cycle.

  
| Node Type | Node Name | Node Description |
| :-- | :-- | :-- |
| Data Input | Model Input | Model data source node, which is used to configure models and TQL search criteria. |
| TQL Input | TQL data source node, which is used to configure model TQL query statements. |
| Data Operation | TQL Filter | Data filtering based on TQL statements. |
| Run Script | 
-   Value assignment and data calculation based on scripts.
-   The script processing mode can be batch processing (default) or single processing.
-   The input and output are data lists.

 |
| Data output node | Model Output | You can select a model as the output node, and create, update, supplement, or delete data. The primary key mapping must be specified for data update and deletion operations. |
| API Output | Services, built-in model services, SOAP, REST, outbound APIs, and common APIs can be called. | **Parent topic:** [[Configuring a Model Flow|Configuring a Model Flow]]