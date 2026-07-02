---
title: "Catch"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560690.html"
depth: 7
---
# Catch

**Catch**

**Description:**

Catch logic:

1\. Exception obtaining control, which is valid only when try is used together.

2\. The value of exception is the exception type name. If the value is Exception, all exceptions can be captured.

3.You can use the variables exceptionName and exceptionMessage to reference the exception name and information.

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560690__table51343mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560690__row51349mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521560690__row51359mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">exception</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">The name of the exception that needs to be matched (root exception: Exception)</td></tr></tbody></table>

**Samples**

Catch all types of exceptions

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560690__table51370mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560690__row51375mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560690__row51382mcpsimp"><td class="cellrowborder" valign="top" width="50%">exception</td><td class="cellrowborder" valign="top" width="50%">Exception</td></tr></tbody></table>

**Parent topic:** [[Exception|Exception]]