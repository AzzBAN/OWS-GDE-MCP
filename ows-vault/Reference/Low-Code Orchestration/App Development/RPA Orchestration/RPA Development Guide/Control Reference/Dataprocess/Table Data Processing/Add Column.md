---
title: "Add Column"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480683.html"
depth: 7
---
# Add Column

**pandas.addColumn**

**Description:**

Add a new column to DataFrame table

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480683__table129448mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480683__row129454mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552480683__row129464mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Variable of DataFrame table type. The format is: @{variable name}</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480683__table129474mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480683__row129483mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552480683__row129502mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">column-name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Name of the new column. A number is randomly allocated default</td></tr><tr id="EN-US_TOPIC_0000002552480683__row129516mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">data</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Data for new column, support number, string or list data. The length of list data must be equal to the rows count of DataFrame object.</td></tr><tr id="EN-US_TOPIC_0000002552480683__row129530mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Create a DataFrame named 'df\_demo':

![[en-us_image_0000002552480939.png]]

Add a column 'addr' to 'df\_demo' with values \["beijing","tianjin","nanjing"\].

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480683__table129551mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480683__row129556mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480683__row129563mcpsimp"><td class="cellrowborder" valign="top" width="50%">column-name</td><td class="cellrowborder" valign="top" width="50%">addr</td></tr><tr id="EN-US_TOPIC_0000002552480683__row129569mcpsimp"><td class="cellrowborder" valign="top" width="50%">data</td><td class="cellrowborder" valign="top" width="50%">["beijing","tianjin","nanjing"]</td></tr></tbody></table>

'df\_demo' now is:

![[en-us_image_0000002521560980.png]]

**Parent topic:** [[Table Data Processing|Table Data Processing]]