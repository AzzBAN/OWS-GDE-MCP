---
title: "Rule: Data Cleanup Must Be Considered During Data Orchestration to Avoid Duplicate Data in the Same Batch Due to Repeated Execution"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002032616385.html"
depth: 6
---
# Rule: Data Cleanup Must Be Considered During Data Orchestration to Avoid Duplicate Data in the Same Batch Due to Repeated Execution

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Avoid\_Duplicate\_Batch\_Data

**Description**:

-   For small-period (within 30 minutes) scheduling tasks, set the timeout interval to twice the scheduling period.
-   For large-period (30 minutes or longer) scheduling tasks, add the Hadoop SQL Executor operator before the loading operator to clear data (using **drop segment**/**partition** or **delete** to directly delete data).

**Check guide**: For flows that are repeatedly executed in the same batch (such as those involve timeout retry and manual retry), check whether data is cleared before data is loaded.

**Impact**: The time required for clearing data varies depending on different factors (such as the queue resource size and clearing mode). Select a proper clearing mode.

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]