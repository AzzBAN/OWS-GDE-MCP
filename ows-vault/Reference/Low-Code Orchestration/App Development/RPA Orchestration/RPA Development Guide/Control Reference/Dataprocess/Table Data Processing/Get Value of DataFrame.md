---
title: "Get Value of DataFrame"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560716.html"
depth: 7
---
# Get Value of DataFrame

**pandas.getDataByIndex**

**Description:**

Get the value of the specified row and column in the DateFrame

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560716__table46552mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560716__row46558mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521560716__row46568mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Specified DataFrame</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560716__table46578mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560716__row46587mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560716__row46606mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">col</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Column name</td></tr><tr id="EN-US_TOPIC_0000002521560716__row46620mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">row</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Row number, starting from 0, that is, 0 means the first line. Not filling means to get the value of a column.</td></tr><tr id="EN-US_TOPIC_0000002521560716__row46634mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560716__table46650mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560716__row46658mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521560716__row46674mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">Object</td><td class="cellrowborder" valign="top" width="20%">pandasgetDataByIndex_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">The value of the specified row and column in the DateFrame</td></tr><tr id="EN-US_TOPIC_0000002521560716__row46686mcpsimp"><td class="cellrowborder" valign="top" width="20%">return_type</td><td class="cellrowborder" valign="top" width="20%">list</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">list</td><td class="cellrowborder" valign="top" width="20%">Type of return value</td></tr></tbody></table>

**samples**

Create a DataFrame named 'df\_demo':

![[en-us_image_0000002521400964.png]]

Obtain the data of the cell in row 1 and column'age' in 'df\_demo'. 21 is returned.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560716__table46703mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560716__row46708mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560716__row46715mcpsimp"><td class="cellrowborder" valign="top" width="50%">col</td><td class="cellrowborder" valign="top" width="50%">age</td></tr><tr id="EN-US_TOPIC_0000002521560716__row46721mcpsimp"><td class="cellrowborder" valign="top" width="50%">row</td><td class="cellrowborder" valign="top" width="50%">1</td></tr></tbody></table>

Obtain the entire column of 'age' column in 'df\_demo'

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560716__table46728mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560716__row46733mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560716__row46740mcpsimp"><td class="cellrowborder" valign="top" width="50%">col</td><td class="cellrowborder" valign="top" width="50%">age</td></tr></tbody></table>

The output is(if named 'col\_data'):

![[en-us_image_0000002552560947.png]]

1.The output is a Series object,you can get each row by index, like @{col\_data}\[0\] get the first item.

2.Use 'series2list' to translate to list.

**Parent topic:** [[Table Data Processing|Table Data Processing]]