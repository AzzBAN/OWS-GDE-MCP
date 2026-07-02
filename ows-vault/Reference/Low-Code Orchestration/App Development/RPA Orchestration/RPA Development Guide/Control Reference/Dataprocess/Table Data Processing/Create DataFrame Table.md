---
title: "Create DataFrame Table"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400710.html"
depth: 7
---
# Create DataFrame Table

**pandas.putDataTable**

**Description:**

Create a DataFrame by referencing variables. The supported reference variable types include lists and dictionaries. For details, see the example description

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400710__table61889mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400710__row61895mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521400710__row61905mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Variable name of specified data</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400710__table61915mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400710__row61924mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400710__row61943mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">column_headers</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specifies the column name which is of the array type for the data. If the input data does not contain a name, like [["johnny",20],["mick",30]], you can give a column name like ["Name","Age"]. otherwise, it will be named with numbers.</td></tr><tr id="EN-US_TOPIC_0000002521400710__row61957mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">row_headers</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specifies the row index which is of the array type for the data. The default row index is a numeric sequence. You can also specify another type like ["Row1","Row2"].</td></tr><tr id="EN-US_TOPIC_0000002521400710__row61971mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400710__table61987mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400710__row61995mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521400710__row62011mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">TableObject</td><td class="cellrowborder" valign="top" width="20%">pandasputDataTable_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">A new dataFrame</td></tr></tbody></table>

**samples**

Create a empty DataFrame

(Do not write any \[Input\])

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400710__table62027mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400710__row62032mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr></tbody></table>

**samples**

Create a 'myList' with values: \[\["Joe",30,2\],\["Ken",21,3\],\["Su",22,4\]\]

Converts the list myList to a DataFrame (with no parameters).:

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400710__table62043mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400710__row62048mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr></tbody></table>

The new DataFrame will be:

![[en-us_image_0000002552480931.png]]

Converts the list 'myList' to a DataFrame, specifying the column name.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400710__table62058mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400710__row62063mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400710__row62070mcpsimp"><td class="cellrowborder" valign="top" width="50%">column_headers</td><td class="cellrowborder" valign="top" width="50%">["name","age","grade"]</td></tr></tbody></table>

The new DataFrame will be:

![[en-us_image_0000002521560972.png]]

Converts the list 'myList' to a DataFrame, specifying both the column name and the row name.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400710__table62079mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400710__row62084mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400710__row62091mcpsimp"><td class="cellrowborder" valign="top" width="50%">column_headers</td><td class="cellrowborder" valign="top" width="50%">["name","age","grade"]</td></tr><tr id="EN-US_TOPIC_0000002521400710__row62097mcpsimp"><td class="cellrowborder" valign="top" width="50%">row_headers</td><td class="cellrowborder" valign="top" width="50%">["R1","R2","R3"]</td></tr></tbody></table>

The new DataFrame will be:

![[en-us_image_0000002521400966.png]]

Create a list named 'myList2' with values: \[{"name":"Joe","age":30,"grade":2},{"name":"Ken","age":21,"grade":3},{"name":"Su","age":22,"grade":4}\].Convert 'myList2' to a DataFrame

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400710__table62106mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400710__row62111mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr></tbody></table>

The new DataFrame will be:

![[en-us_image_0000002552560949.png]]

Create a dict named 'myDict' with values: {"name":\["Joe","Ken","Su"\],"age":\[30,21,22\],"grade":\[2,3,4\]}. Convert 'myDict' to a DataFrame

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400710__table62121mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400710__row62126mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr></tbody></table>

The new DataFrame will be:

![[en-us_image_0000002552480933.png]]

**Parent topic:** [[Table Data Processing|Table Data Processing]]