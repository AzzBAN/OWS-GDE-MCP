---
title: "Suggestion: Edit SQL Statements Based on Service Data Query Requirements and Take Restriction Measures If Necessary to Avoid Resource Performance Loss Caused by Extensive Query"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001613883730.html"
depth: 6
---
# Suggestion: Edit SQL Statements Based on Service Data Query Requirements and Take Restriction Measures If Necessary to Avoid Resource Performance Loss Caused by Extensive Query

**Specification name**: General\_DataFactory\_Data\_Explorer\_SQL\_Statement\_Editing\_Principle

**Description**: You are advised to edit SQL statements based on data query requirements and take necessary measures to reduce performance loss and improve query efficiency.

**Check guide**:

-   Use the limit condition to limit the amount of data to be queried when compiling SQL statements based on data query requirements to reduce database performance loss.
-   When a large amount of data is queried from the Spark SQL data source table, do not use aggregation functions such as order by and group by, because using these functions may cause quick consumption of database resources and performance loss.

**Positive example**: To check whether data that meets the conditions exists, use **select\* from** _xxx_ **where** _xxx_ **limit 1;**.

**Parent topic:** [[Data Exploration|Data Exploration]]