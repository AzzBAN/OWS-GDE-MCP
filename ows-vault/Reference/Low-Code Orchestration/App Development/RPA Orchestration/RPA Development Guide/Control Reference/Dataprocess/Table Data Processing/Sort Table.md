---
title: "Sort Table"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560693.html"
depth: 7
---
# Sort Table

**pandas.sortValues**

**Description:**

Sorting DataFrame by Column or row.Ensure that the specified rows or columns have the same data type.

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560693__table33477mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560693__row33483mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33493mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Specified DataFrame Table</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560693__table33503mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560693__row33512mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33531mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">axis</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">0</td><td class="cellrowborder" valign="top" width="16.666666666666664%">0|1</td><td class="cellrowborder" valign="top" width="16.666666666666664%">sort axis, The value 0 indicates sort by column and 1 indicates by row.</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33545mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">row</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specify the name of the row to be sorted.For example, 0 indicates sorting by the first row. Multiple rows are in array format, for example, [0,1].Ensure that the data types of the specified rows are the same.</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33559mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">col</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specify the name of the column to be sorted.For example, "name" indicates sorting by column named 'name'. Multiple columns are in array format, for example, ["name","Age"].Ensure that the data types of the specified columns are the same.</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33573mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">ascending</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">true</td><td class="cellrowborder" valign="top" width="16.666666666666664%">true|false</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Indicates whether to sort in ascending order. true: sort in ascending order; false: sort in descending order</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33587mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560693__table33603mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560693__row33611mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33627mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">TableObject</td><td class="cellrowborder" valign="top" width="20%">pandassortValues_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">New DataFrame Table after sorting</td></tr></tbody></table>

**samples**

Create a DataFrame named 'df\_demo':

![[en-us_image_0000002521560974.png]]

Sort the table by the 'age' column.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560693__table33644mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560693__row33649mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33656mcpsimp"><td class="cellrowborder" valign="top" width="50%">axis</td><td class="cellrowborder" valign="top" width="50%">0</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33662mcpsimp"><td class="cellrowborder" valign="top" width="50%">col</td><td class="cellrowborder" valign="top" width="50%">age</td></tr></tbody></table>

The new DataFrame will be:

![[en-us_image_0000002521400968.png]]

Sort tables in descending order based on the 'age' column

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560693__table33671mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560693__row33676mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33683mcpsimp"><td class="cellrowborder" valign="top" width="50%">axis</td><td class="cellrowborder" valign="top" width="50%">0</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33689mcpsimp"><td class="cellrowborder" valign="top" width="50%">col</td><td class="cellrowborder" valign="top" width="50%">age</td></tr><tr id="EN-US_TOPIC_0000002552560693__row33695mcpsimp"><td class="cellrowborder" valign="top" width="50%">ascending</td><td class="cellrowborder" valign="top" width="50%">false</td></tr></tbody></table>

Then the sorting table objects in descending order are:

![[en-us_image_0000002552560951.png]]

**Parent topic:** [[Table Data Processing|Table Data Processing]]