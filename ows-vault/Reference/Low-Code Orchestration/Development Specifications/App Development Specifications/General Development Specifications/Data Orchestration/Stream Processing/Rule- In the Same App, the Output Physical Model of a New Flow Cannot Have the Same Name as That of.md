---
title: "Rule: In the Same App, the Output Physical Model of a New Flow Cannot Have the Same Name as That of a Historical Flow"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001871619822.html"
depth: 6
---
# Rule: In the Same App, the Output Physical Model of a New Flow Cannot Have the Same Name as That of a Historical Flow

**Specification name**: General\_DataFactory\_Stream\_App\_Incremental\_Development\_Restriction

**Description**: In the same app, the output physical model of a newly developed flow cannot have the same name as that of a historical flow.

**Check guide**: In the same app, check whether the output physical model of a newly developed flow has the same name as that of a historical flow. If yes, change the name of the output physical model of the new flow.

**Impact**: If this rule is violated, historical flows may be overwritten during app running, resulting in an app upgrade failure or service interruption.

**Parent topic:** [[Stream Processing|Stream Processing]]