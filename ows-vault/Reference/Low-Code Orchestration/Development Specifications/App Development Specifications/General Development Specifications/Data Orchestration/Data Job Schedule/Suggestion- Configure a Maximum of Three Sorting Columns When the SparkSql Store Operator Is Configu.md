---
title: "Suggestion: Configure a Maximum of Three Sorting Columns When the SparkSql Store Operator Is Configured for Aggregation and Computing"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001614224472.html"
depth: 6
---
# Suggestion: Configure a Maximum of Three Sorting Columns When the SparkSql Store Operator Is Configured for Aggregation and Computing

**Specification name**: General\_DataFactory\_Aggregation\_Calculation\_SparkSql\_Sort\_Column

**Description**: When creating a BFS-Spark or IMC aggregation and computing task, you can migrate the computing result to a specific storage medium, for example, SparkSQL. In this case, physical models need to be created for the BFS-Spark task, and storage operators need to be used for the IMC computing task. When the storage medium is SparkSQL and **Format** is **CarbonData**, you can set **Sorting Column** to improve query performance, which, in turn, slightly affects loading performance. Therefore, you are advised to use high-frequency query columns as sorting columns and ensure that the number of sorting columns does not exceed three.

**Check guide**: Check whether the configured sorting columns are high-frequency query columns and whether the number of sorting columns exceeds three.

**Positive example**: No more than three sorting columns are configured when the SparkSql Store operator is used.

![[en-us_image_0000001645223838.png]]

**Parent topic:** [[Data Job Schedule|Data Job Schedule]]