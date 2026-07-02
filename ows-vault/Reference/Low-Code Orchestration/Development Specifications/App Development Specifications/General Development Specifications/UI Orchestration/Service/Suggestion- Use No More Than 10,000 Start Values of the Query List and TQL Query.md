---
title: "Suggestion: Use No More Than 10,000 Start Values of the Query List and TQL Query"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123600.html"
depth: 6
---
# Suggestion: Use No More Than 10,000 Start Values of the Query List and TQL Query

**Description**: If the value of start in the query list is large, the database or Elasticsearch loads more data to the memory. As a result, the memory usage is high and the system response is affected.

**Check guide**: Check whether the start value of the query list and TQL query is proper. It is recommended that the value be less than or equal to 10,000. The maximum value is 300,000.

**Positive example**: The maximum value of start in the query list and TQL query configuration is less than 10000. You are advised to restrict the time range for the time type.

**Negative example**: The maximum number of query lists and TQL statements is not limited or the configured maximum value start is greater than 10000.

**Tool supported or not**: yes

**Specification name**: General\_Service\_Start\_Value\_Cannot\_Exceed\_10000

**Severity**: suggestion

**Parent topic:** [[Service|Service]]