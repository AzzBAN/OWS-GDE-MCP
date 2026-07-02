---
title: "Suggestion: To Save Costs, Use Lightweight ETL Operators to Process Less than 10 Million Records in Batches"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001237104693.html"
depth: 6
---
# Suggestion: To Save Costs, Use Lightweight ETL Operators to Process Less than 10 Million Records in Batches

**Specification name**: General\_DataFactory\_Data\_Amount\_Less\_10Million\_Recommend\_LightETL

**Description**: The cost of deploying the Hadoop cluster is high. It is recommended that lightweight ETL operators be used to process less than 10 million records in batches.

**Check guide**: Check the amount of data processed by the data flows and the type of the data flows.

**Impact**: In scenarios with small data volume, Spark-based batch processing cannot improve performance, and deploying the Hadoop cluster consumes extra resources.

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]