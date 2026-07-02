---
title: "Rule: The Dependency Operator of Data Job Schedule Must Avoid Cyclic Dependency"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001192464720.html"
depth: 6
---
# Rule: The Dependency Operator of Data Job Schedule Must Avoid Cyclic Dependency

**Specification name**: General\_DataFactory\_Unified\_Schedule\_Dependency\_Avoiding\_Cyclic\_Dependencies

**Description**: The Dependency operator of Data Job Schedule can depend on the flows or operators of the current project or other projects, but cyclic dependency is not allowed. If cyclic dependency is formed, the flow scheduling enters the infinite loop of waiting.

**Check guide**:

1.  In the flow that operator A depends on, check whether there is any operator that depends on the flow that contains operator A. If yes, cyclic dependency is formed.
2.  In the flow that operator A depends on, check whether there is any operator that depends on operator A. If yes, cyclic dependency is formed.
3.  Check whether the operator of the task (on which operator A depends) depends on operator A. If yes, cyclic dependency is formed.
4.  Check whether the operator of the task (on which operator A depends) depends on the flow that contains operator A. If yes, cyclic dependency is formed.

**Impact**: If cyclic dependency occurs for the Dependency operator of Data Job Schedule, the program execution conditions are never met. As a result, tasks cannot be executed.

**Parent topic:** [[Data Job Schedule|Data Job Schedule]]