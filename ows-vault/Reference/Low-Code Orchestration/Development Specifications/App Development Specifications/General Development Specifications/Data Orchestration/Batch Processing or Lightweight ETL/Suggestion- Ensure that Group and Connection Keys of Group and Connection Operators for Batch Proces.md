---
title: "Suggestion: Ensure that Group and Connection Keys of Group and Connection Operators for Batch Processing Are Evenly Distributed When Configuring Upstream Data Processing Logic of Businesses, Preventing Task Running Failures Caused by Data Skew"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001276948956.html"
depth: 6
---
# Suggestion: Ensure that Group and Connection Keys of Group and Connection Operators for Batch Processing Are Evenly Distributed When Configuring Upstream Data Processing Logic of Businesses, Preventing Task Running Failures Caused by Data Skew

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Services\_Ensure\_Data\_Not\_Skewed

**Description**: When configuring business orchestration logic, you need to ensure that group and connection keys of Group and Connection operators are evenly distributed. For example, a large number of empty values or same constants are not allowed.

**Check guide**: Deduce data transfer logic in business design to ensure that group and connection keys of Group and Connection operators are evenly distributed.

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]