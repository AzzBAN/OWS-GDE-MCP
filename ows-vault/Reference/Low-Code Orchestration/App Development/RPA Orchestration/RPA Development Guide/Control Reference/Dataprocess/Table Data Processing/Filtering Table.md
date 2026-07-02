---
title: "Filtering Table"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560726.html"
depth: 7
---
# Filtering Table

**pandas.query**

**Description:**

Extract specific data as a new DataFrame table

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560726__table7694mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560726__row7700mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521560726__row7710mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Variable of DataFrame table type. The format is: @{variable name}</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560726__table7720mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560726__row7729mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560726__row7748mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">expr</td><td class="cellrowborder" valign="top" width="16.666666666666664%">python</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Filter expression, which is a standard Python syntax expression. For example, age&gt;18 indicates that data whose age is greater than 18 in the DataFrame table is extracted to form a new DataFrame. Precautions: 1. If the column name contains special characters such as spaces, use `` to wrap the column name, for example, `live days`&gt;2.</td></tr><tr id="EN-US_TOPIC_0000002521560726__row7764mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">column_headers</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Obtains data of specified columns. The value is of the array type. For example, ["age","city"] indicates that only columns 'age' and 'city' in the DataFrame table are obtained. By default, all columns are obtained.</td></tr><tr id="EN-US_TOPIC_0000002521560726__row7778mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560726__table7794mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560726__row7802mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521560726__row7818mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">TableObject</td><td class="cellrowborder" valign="top" width="20%">query_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">A new DataFrame table</td></tr></tbody></table>

**samples**

Create a DataFrame named 'df\_demo':

![[en-us_image_0000002521560984.png]]

Obtain the data from 'df\_demo' whose addr is 'beijing'.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560726__table7835mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560726__row7840mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560726__row7847mcpsimp"><td class="cellrowborder" valign="top" width="50%">expr</td><td class="cellrowborder" valign="top" width="50%">addr=='beijing'</td></tr></tbody></table>

The new DataFrame is:

![[en-us_image_0000002521400978.png]]

Obtain data from 'df\_demo' whose 'age' is greater than 21 and 'grade' is greater than 3.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560726__table7856mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560726__row7861mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560726__row7868mcpsimp"><td class="cellrowborder" valign="top" width="50%">expr</td><td class="cellrowborder" valign="top" width="50%">age&gt;21 and grade&gt;3</td></tr></tbody></table>

The new DataFrame is:

![[en-us_image_0000002552560961.png]]

Obtain the data from 'df\_demo' whose sum of 'age' and 'grade' is greater than 30.

(Common operations such as +, -, \*, and / can be performed on columns.)

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560726__table7878mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560726__row7883mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560726__row7890mcpsimp"><td class="cellrowborder" valign="top" width="50%">expr</td><td class="cellrowborder" valign="top" width="50%">age+grade &gt;30</td></tr></tbody></table>

The new DataFrame is:

![[en-us_image_0000002552480945.png]]

**Parent topic:** [[Table Data Processing|Table Data Processing]]