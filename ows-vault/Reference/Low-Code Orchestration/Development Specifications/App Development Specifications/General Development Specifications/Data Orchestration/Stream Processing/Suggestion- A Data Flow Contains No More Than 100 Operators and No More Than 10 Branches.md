---
title: "Suggestion: A Data Flow Contains No More Than 100 Operators and No More Than 10 Branches"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001237224693.html"
depth: 6
---
# Suggestion: A Data Flow Contains No More Than 100 Operators and No More Than 10 Branches

**Specification name**: General\_DataFactory\_Stream\_Canvas\_Scale

**Description**: In a stream processing data flow, it is recommended that the number of operators be no more than 100 and the number of branches be no more than 10. Complex logic should be implemented in several data flows which are connected by the control flow of Data Job Schedule.

**Check guide**: Check the number of operators and branches in the data flow.

**Impact**: Implementing excessively complex logic in one data flow may cause issues, such as difficulty in flow understanding, poor readability, high probability of flow errors, time-consuming debugging, poor flow reuse, and slow rendering or even frame freezing of operations (for example, page verification).

**Parent topic:** [[Stream Processing|Stream Processing]]