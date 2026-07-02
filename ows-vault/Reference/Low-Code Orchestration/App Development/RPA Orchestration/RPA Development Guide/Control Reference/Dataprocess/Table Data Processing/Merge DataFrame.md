---
title: "Merge DataFrame"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400722.html"
depth: 7
---
# Merge DataFrame

**pandas.merge**

**Description:**

Merge DataFrames according to one or more fields, similar to the join operation of database table.List of user-defined parameters:

1\. left\_on: The field used for connection in the left data table, multiple fields use the form of an array.

2\. right\_on: The field used for connection in the right data table, multiple fields use the form of an array.

3\. left\_index: Whether to use the index of the left data table as the connection field, the default is False.

4\. right\_index: Whether to use the index of the right data table as the connection field, the default is False.

5\. copy: Whether to copy the data table, the default is True.

6\. indicator: Whether to add a column of data in the result data table, indicating the source of each row of data. The default is False.

7\. Set the type of validation merge:

one\_to\_one: Check whether the merged field is unique in the two data tables.

one\_to\_many: Check whether the merged field is unique in the left data table.

many\_to\_one: Check whether the merged field is unique in the right data table.

many\_to\_many: The merge field does not need to be unique in both data tables.

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400722__table90364mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400722__row90370mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90380mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">left</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">DataFrame on the left</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90388mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">right</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">DataFrame on the Right</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400722__table90398mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400722__row90407mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90426mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">how</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">inner</td><td class="cellrowborder" valign="top" width="16.666666666666664%">left|right|outer|inner|cross</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Type of merge to be performed</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90440mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">on</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Fields used to join two DataFrames.Use array form for multiple fields</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90454mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">sort</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True|False</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Sorting according to the lexicographical order of the joined fields</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90468mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">suffixes</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">('_x', '_y')</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Set the suffixes of the overlapping fields on the left and right except the join fields, in array form, the default is: ('_x', '_y')</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90482mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">user-defined</td><td class="cellrowborder" valign="top" width="16.666666666666664%">flexibleTable</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">User-defined parameters are used to configure additional parameters of the interface pandas.merge. For details, see the official Pandas documentation https://pandas.pydata.org/docs/reference/api/pandas.merge.html</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90496mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400722__table90512mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400722__row90520mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90536mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">TableObject</td><td class="cellrowborder" valign="top" width="20%">merged_df</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">The new DataFrame generated by merging</td></tr></tbody></table>

**samples**

Join the two input data tables on the field name

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400722__table90551mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400722__row90556mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90563mcpsimp"><td class="cellrowborder" valign="top" width="50%">how</td><td class="cellrowborder" valign="top" width="50%">inner</td></tr><tr id="EN-US_TOPIC_0000002521400722__row90569mcpsimp"><td class="cellrowborder" valign="top" width="50%">on</td><td class="cellrowborder" valign="top" width="50%">name</td></tr></tbody></table>

**Parent topic:** [[Table Data Processing|Table Data Processing]]