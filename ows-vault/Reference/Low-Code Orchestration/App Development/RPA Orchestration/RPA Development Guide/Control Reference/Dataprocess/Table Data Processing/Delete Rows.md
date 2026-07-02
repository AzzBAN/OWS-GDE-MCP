---
title: "Delete Rows"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560724.html"
depth: 7
---
# Delete Rows

**pandas.deleteRow**

**Description:**

Delete specified rows of DataFrame table

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560724__table50219mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560724__row50225mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521560724__row50235mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Variable of DataFrame table type. The format is: @{variable name}</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560724__table50245mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560724__row50254mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560724__row50273mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">condition</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Filter criteria for action. Giving single number filter single row; giving numbers separated by a comma filter multiple rows; giving single conditions like 'df["name"]=="Johnny"' or multiple conditions like '(df["name"]=="Johnny") &amp; (df["nationality"]=="China")' to filter eligible rows</td></tr><tr id="EN-US_TOPIC_0000002521560724__row50287mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Create a DataFrame named 'df\_demo':

![[en-us_image_0000002521400974.png]]

Delete the rows whose age is less than 30 and grade is greater than 3 from 'df\_demo'.

(Note: 'df' is a fixed name, indicating the DataFrame to be operated.)

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560724__table50309mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560724__row50314mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560724__row50321mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">(df['age']&lt;30) &amp; (df['grade']&gt;3)</td></tr></tbody></table>

'df\_demo' now is:

![[en-us_image_0000002552560957.png]]

**Parent topic:** [[Table Data Processing|Table Data Processing]]