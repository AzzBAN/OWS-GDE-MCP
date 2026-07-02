---
title: "Suggestion: Inject SQL Statements with the Same Logic in the Control Flow to Reduce the Impact of Data Skew When Group Keys of the Group Operator for Batch Processing Are Not Evenly Distributed During the Aggregation and Computing"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001327028861.html"
depth: 6
---
# Suggestion: Inject SQL Statements with the Same Logic in the Control Flow to Reduce the Impact of Data Skew When Group Keys of the Group Operator for Batch Processing Are Not Evenly Distributed During the Aggregation and Computing

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Grouping\_Operators\_Equivalent\_SQL

**Description**: If functions, such as MAX, MIN, and AVG, are used in aggregation and computing, the Group operator cannot be used for discretization. In this case, you can use SQL statements with the same logic as that of the Group operator and use the Hadoop SQL executor.

**Check guide**: Check whether the Group operator uses functions, such as MAX, MIN, and AVG, during aggregation and computing in data skew scenarios.

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]