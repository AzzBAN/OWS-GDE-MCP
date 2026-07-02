---
title: "Remove Duplicate Rows"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480679.html"
depth: 7
---
# Remove Duplicate Rows

**pandas.dropDuplicates**

**Description:**

Remove duplicate rows in DataFrame Table

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480679__table34572mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480679__row34578mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552480679__row34588mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Variable of DataFrame table type. The format is: @{variable name}</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480679__table34598mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480679__row34607mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552480679__row34626mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">subset</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specifies the columns used to determine duplicate data. By default, duplicate data is identified only when all columns in two rows are the same. For example, ["name","age"] indicates that duplicate data is identified only when names and ages are the same.</td></tr><tr id="EN-US_TOPIC_0000002552480679__row34640mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">keep</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">first</td><td class="cellrowborder" valign="top" width="16.666666666666664%">first|last|false</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Retention policy of duplicate data. 'first' indicates that the first record is retained, 'last' indicates that the last record is retained, and 'false' indicates that all duplicated rows will be removed.</td></tr><tr id="EN-US_TOPIC_0000002552480679__row34654mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Create a DataFrame named 'df\_demo':

![[en-us_image_0000002521400970.png]]

Completely remove rows with the same'age' and'grade'

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480679__table34675mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480679__row34680mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480679__row34687mcpsimp"><td class="cellrowborder" valign="top" width="50%">keep</td><td class="cellrowborder" valign="top" width="50%">false</td></tr><tr id="EN-US_TOPIC_0000002552480679__row34693mcpsimp"><td class="cellrowborder" valign="top" width="50%">subset</td><td class="cellrowborder" valign="top" width="50%">["age","grade"]</td></tr></tbody></table>

'df\_demo' now is:

![[en-us_image_0000002552560953.png]]

Check the rows in which the'age' and'grade' are the same. If the rows are the same, only the first row is retained.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480679__table34702mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480679__row34707mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480679__row34714mcpsimp"><td class="cellrowborder" valign="top" width="50%">keep</td><td class="cellrowborder" valign="top" width="50%">first</td></tr><tr id="EN-US_TOPIC_0000002552480679__row34720mcpsimp"><td class="cellrowborder" valign="top" width="50%">subset</td><td class="cellrowborder" valign="top" width="50%">["age","grade"]</td></tr></tbody></table>

'df\_demo' now is:

![[en-us_image_0000002552480937.png]]

**Parent topic:** [[Table Data Processing|Table Data Processing]]