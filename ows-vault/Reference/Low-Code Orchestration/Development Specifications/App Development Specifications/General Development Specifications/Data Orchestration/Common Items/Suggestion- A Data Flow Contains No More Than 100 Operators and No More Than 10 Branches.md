---
title: "Suggestion: A Data Flow Contains No More Than 100 Operators and No More Than 10 Branches"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001236944715.html"
depth: 6
---
# Suggestion: A Data Flow Contains No More Than 100 Operators and No More Than 10 Branches

**Specification name**: General\_DataFactory\_DataFlow\_Operator\_Amount\_Less\_100

**Description**: In a data flow, it is recommended that the number of operators be no more than 100 and the number of branches be no more than 10. Complex business logic should be split into multiple data flows and connected by control flow.

**Check guide**: Check the number of operators and branches in the data flow.

**Impact**: Implementing excessively complex logic in one data flow may cause issues, such as difficulty in flow understanding, poor readability, high probability of flow errors, time-consuming debugging, poor flow reuse, and slow rendering or even frame freezing of operations (for example, page verification).

**Parent topic:** [[Common Items|Common Items]]