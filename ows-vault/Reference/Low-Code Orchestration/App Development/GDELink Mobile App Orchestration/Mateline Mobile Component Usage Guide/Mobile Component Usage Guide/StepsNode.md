---
title: "StepsNode"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001734223460.html"
depth: 5
---
# StepsNode

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| label | Node label |
| Location | Location that will be redirected after a node is clicked. |
| url | Same as Location. But its priority is low. |
| parameters | Redirection parameter |
| RecordHistory | Whether to record the history |
| Status | Node status | **APIs**

**changeStatus**

Input parameter: **status**

Output parameters: none

Description: Set the node status.

Example:

C("stepsNode1").changeStatus("succeed");

**FAQs**

N/A

**Precautions**

N/A

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]