---
title: "Add Row"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560699.html"
depth: 7
---
# Add Row

**pandas.addRow**

**Description:**

Add a new row to DataFrame table

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560699__table144945mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560699__row144951mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560699__row144961mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Variable of DataFrame table type. The format is: @{variable name}</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560699__table144971mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560699__row144980mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560699__row144999mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">data</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Data for new row, support list data or dict data. The length of list data must be equal to the columns count of DataFrame object.</td></tr><tr id="EN-US_TOPIC_0000002552560699__row145013mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">ifDifferentSchema</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">error</td><td class="cellrowborder" valign="top" width="16.666666666666664%">error|ignore</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Processing policy for column header mismatch (applicable only to the scenario where the new data is a dictionary). Processing policy when the key in the input dictionary and DataFrame column names are inconsistent. The default value is error, indicating that an exception is thrown. If ignore is selected, NaN is used for mismatched key.</td></tr><tr id="EN-US_TOPIC_0000002552560699__row145027mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Create a DataFrame named 'df\_demo':

![[en-us_image_0000002521560978.png]]

Create a list 'myList' with values \["Jay",21,3\] and add it to 'df\_demo'.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560699__table145048mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560699__row145053mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560699__row145060mcpsimp"><td class="cellrowborder" valign="top" width="50%">data</td><td class="cellrowborder" valign="top" width="50%">@{myList}</td></tr></tbody></table>

'df\_demo' now is:

![[en-us_image_0000002521400972.png]]

Create a dictionary 'myDict' with values {"name":"Jay","age":21,"grade":3} and add it to 'df\_demo'.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560699__table145069mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560699__row145074mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560699__row145081mcpsimp"><td class="cellrowborder" valign="top" width="50%">data</td><td class="cellrowborder" valign="top" width="50%">@{myDict}</td></tr></tbody></table>

'df\_demo' now is:

![[en-us_image_0000002552560955.png]]

Enter string data directly and add it to the table as a list of single elements.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560699__table145090mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560699__row145095mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560699__row145102mcpsimp"><td class="cellrowborder" valign="top" width="50%">data</td><td class="cellrowborder" valign="top" width="50%">"Jay"</td></tr></tbody></table>

**Parent topic:** [[Table Data Processing|Table Data Processing]]