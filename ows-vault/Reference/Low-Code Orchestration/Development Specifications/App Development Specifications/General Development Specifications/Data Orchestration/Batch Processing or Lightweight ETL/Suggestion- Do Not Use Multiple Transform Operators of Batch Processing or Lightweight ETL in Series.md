---
title: "Suggestion: Do Not Use Multiple Transform Operators of Batch Processing or Lightweight ETL in Series to Process Fields"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001276789004.html"
depth: 6
---
# Suggestion: Do Not Use Multiple Transform Operators of Batch Processing or Lightweight ETL in Series to Process Fields

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Merging\_Continuous\_Conversion\_Operator

**Description**: To improve computing performance, develop the continuous data conversion logic using one Transform operator of batch processing or lightweight ETL to process fields. Avoid connecting multiple Transform operators in series.

**Check guide**: Check whether Transform operators are connected in series during data flow orchestration.

**Impact**: After multiple Transform operators are combined into one, resource consumption can be reduced and computing performance can be improved.

**Positive example**: [Figure 1](#EN-US_TOPIC_0000001276789004__fig54001645115317) shows the two Transform operators that can be combined.

**Figure 1** Flow before optimization  
![[en-us_image_0000001682800781.png]]

**Figure 2** Flow after optimization  
![[en-us_image_0000001682801465.png]]

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]