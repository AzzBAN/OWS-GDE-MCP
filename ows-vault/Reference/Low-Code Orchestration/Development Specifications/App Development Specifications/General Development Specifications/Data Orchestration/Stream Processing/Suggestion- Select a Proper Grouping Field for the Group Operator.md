---
title: "Suggestion: Select a Proper Grouping Field for the Group Operator"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001917659301.html"
depth: 6
---
# Suggestion: Select a Proper Grouping Field for the Group Operator

**Specification name**: General\_DataFactory\_Stream\_Select\_Available\_Group\_Fields

**Description**: When using the Group operator, select a proper grouping field to ensure that data is evenly distributed and relatively centralized.

**Check guide**: Analyze the input and output data of the Group operator and check whether the grouping field used by the operator is proper.

**Impact**: If the grouping field of the Group operator is improper, data skew occurs and a large amount of local memory is consumed. As a result, computing tasks or the Flink cluster may become abnormal.

**Parent topic:** [[Stream Processing|Stream Processing]]