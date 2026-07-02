---
title: "Rule: The Dependency Operator in a Batch Processing or Lightweight ETL Control Flow Must Avoid Cyclic Dependency"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001236784719.html"
depth: 6
---
# Rule: The Dependency Operator in a Batch Processing or Lightweight ETL Control Flow Must Avoid Cyclic Dependency

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Dependency\_Avoiding\_Cyclic\_Dependencies

**Description**: The Dependency operator in a batch processing or lightweight ETL control flow can depend on the flows or operators of the current project or other projects. Cyclic dependency is not allowed in the configured dependency. Otherwise, the flow scheduling will enter the infinite loop of dependency waiting.

**Check guide**:

1.  In the flow that operator A depends on, check whether there is any operator that depends on the flow that contains operator A. If yes, cyclic dependency is formed.
2.  In the flow that operator A depends on, check whether there is any operator that depends on operator A. If yes, cyclic dependency is formed.
3.  Check whether the operator of the task (on which operator A depends) depends on operator A. If yes, cyclic dependency is formed.
4.  Check whether the operator of the task (on which operator A depends) depends on the flow that contains operator A. If yes, cyclic dependency is formed.

**Impact**: If the cyclic dependency is formed for the Dependency operator in a batch processing or lightweight ETL control flow, the program execution conditions cannot be met. As a result, the task cannot be executed.

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]