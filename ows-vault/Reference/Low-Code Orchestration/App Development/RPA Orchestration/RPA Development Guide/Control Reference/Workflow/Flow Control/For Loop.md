---
title: "For Loop"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560661.html"
depth: 7
---
# For Loop

**For**

**Description:**

For Loop Statement:

1.This control has two attributes: list and item.

2.list indicates the set data to be traversed. The value can be a character string or a list. The number of iterations indicates the number of cycles.

3.item indicates the value obtained in each iteration.

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560661__table44554mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560661__row44560mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560661__row44570mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">fail_on_error</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Whether to exit the robot when the action fails</td></tr><tr id="EN-US_TOPIC_0000002552560661__row44578mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">python</td><td class="cellrowborder" valign="top" width="33.33333333333333%">For loop array.It supports python expressions, such as range (5), it means that the for loop loops 5 times.For loops can use the built-in variable @ {forloop}, which represents the number of iterations,starting from 0.</td></tr><tr id="EN-US_TOPIC_0000002552560661__row44586mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">item</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Single for loop instance, Use numbers, letters, and underscores</td></tr><tr id="EN-US_TOPIC_0000002552560661__row44594mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">index_name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Index variable name.Leave blank and use the default variable name forloop</td></tr></tbody></table>

**Samples**

Loops through the list

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560661__table44605mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560661__row44610mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560661__row44617mcpsimp"><td class="cellrowborder" valign="top" width="50%">list</td><td class="cellrowborder" valign="top" width="50%">[0,1,2,3,4,5]</td></tr></tbody></table>

Cycle 10 times

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560661__table44624mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560661__row44629mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560661__row44636mcpsimp"><td class="cellrowborder" valign="top" width="50%">list</td><td class="cellrowborder" valign="top" width="50%">range(10)</td></tr></tbody></table>

Cyclicly traverses the dictionary keys (name, score, and age)

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560661__table44643mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560661__row44648mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560661__row44655mcpsimp"><td class="cellrowborder" valign="top" width="50%">list</td><td class="cellrowborder" valign="top" width="50%">{"name": "Tom", "score": 98, "age": 18}.keys()</td></tr></tbody></table>

Cyclicly traverses the dictionary values (Tom, 98, and 18 respectively)

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560661__table44662mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560661__row44667mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560661__row44674mcpsimp"><td class="cellrowborder" valign="top" width="50%">list</td><td class="cellrowborder" valign="top" width="50%">{"name": "Tom", "score": 98, "age": 18}.values()</td></tr></tbody></table>

**Parent topic:** [[Flow Control|Flow Control]]