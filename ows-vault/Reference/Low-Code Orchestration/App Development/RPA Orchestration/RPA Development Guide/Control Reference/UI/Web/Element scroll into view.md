---
title: "Element scroll into view"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560809.html"
depth: 7
---
# Element scroll into view

**scrollIntoView**

**Description:**

element scroll into view:

1.May cause page disorder

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560809__table93940mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560809__row93946mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560809__row93956mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Designated browser,If null, specify the browser with the open command(Tips:If you want to manipulate the browser opened by the new_browser command, you must specify the browser here.)</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560809__table93966mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560809__row93975mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560809__row93994mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">target</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Method of positioning elements,et:id/name/class/link/xpath/css=%s and anchor=%s, %s, %s,Position the element position with the values written in the previous seven ways, where anchor is to find the element that starts with anchor and finds the element closest to the anchor point. The value method is: anchor = anchor point, position, tagName, anchor parameter. 1: Anchor point (the variable returned by getElement, Use the returned variable directly without using @{}); Parameter 2: The position of the element to be found (left, right, top, bottom, auto, if it is auto, the nearest one is searched for up, down, left and right); Parameter 3: wait Find element's tagName (*, A, INPUT, etc.)</td></tr><tr id="EN-US_TOPIC_0000002552560809__row94008mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552560809__row94022mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

The following configuration will scroll the element into view in the page according to xpath="xpath=//\*\[@id="content"\]/div\[3\]/app-process-defects-grid/div/div\[2\]"

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560809__table94041mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560809__row94046mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560809__row94053mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">xpath=//*[@id="content"]/div[3]/app-process-defects-grid/div/div[2]</td></tr></tbody></table>

**Parent topic:** [[Web|Web]]