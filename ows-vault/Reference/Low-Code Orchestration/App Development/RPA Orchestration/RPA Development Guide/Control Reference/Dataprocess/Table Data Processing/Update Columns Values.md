---
title: "Update Columns Values"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560701.html"
depth: 7
---
# Update Columns Values

**pandas.updateColumn**

**Description:**

Update data of columns in specified rows of DataFrame table

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560701__table85457mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560701__row85463mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560701__row85473mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Variable of DataFrame table type. The format is: @{variable name}</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560701__table85483mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560701__row85492mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560701__row85511mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">column-value</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Data to be update, which is in dict form, and the key-value format is 'column name - update value'</td></tr><tr id="EN-US_TOPIC_0000002552560701__row85525mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">condition</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Filter criteria for action. Giving single number filter single row; giving numbers separated by a comma filter multiple rows; giving single conditions like 'df["name"]=="Johnny"' or multiple conditions like '(df["name"]=="Johnny") &amp; (df["nationality"]=="China")' to filter eligible rows</td></tr><tr id="EN-US_TOPIC_0000002552560701__row85539mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Create a DataFrame named 'df\_demo':

![[en-us_image_0000002552560959.png]]

Change the value of 'grade' to 3 and the value of 'age' to 40 in 'df\_demo' whose name is 'Joe'

(Note: 'df' is a fixed name, indicating the DataFrame to be operated.)

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560701__table85561mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560701__row85566mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560701__row85573mcpsimp"><td class="cellrowborder" valign="top" width="50%">column-value</td><td class="cellrowborder" valign="top" width="50%">{"grade":3, "age":40}</td></tr><tr id="EN-US_TOPIC_0000002552560701__row85579mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">df["name"]=="Joe"</td></tr></tbody></table>

'df\_demo' now is:

![[en-us_image_0000002552480943.png]]

**Parent topic:** [[Table Data Processing|Table Data Processing]]