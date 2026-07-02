---
title: "Obtaining Base Name"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560607.html"
depth: 7
---
# Obtaining Base Name

**getBaseName**

**Description:**

Obtains the name of a file or folder in a specified path

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560607__table52496mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560607__row52505mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52524mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Target Path</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52538mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">contain-suffix</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True|False</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Contain by default.Select whether to include the extension when obtaining the file name.This parameter does not take effect when the path is a folder</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52552mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52566mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560607__table52582mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560607__row52590mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52606mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">String</td><td class="cellrowborder" valign="top" width="20%">base_name</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Name of the obtained file or folder</td></tr></tbody></table>

**Samples**

Obtain the file name of the D:/temp/temp.txt file, including the extension

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560607__table52621mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560607__row52626mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52633mcpsimp"><td class="cellrowborder" valign="top" width="50%">path</td><td class="cellrowborder" valign="top" width="50%">D:/temp/temp.txt</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52639mcpsimp"><td class="cellrowborder" valign="top" width="50%">contain-suffix</td><td class="cellrowborder" valign="top" width="50%">True</td></tr></tbody></table>

Obtain the file name of the D:/temp/temp.txt file, excluding the extension

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560607__table52646mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560607__row52651mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52658mcpsimp"><td class="cellrowborder" valign="top" width="50%">path</td><td class="cellrowborder" valign="top" width="50%">D:/temp/temp.txt</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52664mcpsimp"><td class="cellrowborder" valign="top" width="50%">contain-suffix</td><td class="cellrowborder" valign="top" width="50%">False</td></tr></tbody></table>

Obtain the file name in the D:/temp/temp directory

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560607__table52671mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560607__row52676mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560607__row52683mcpsimp"><td class="cellrowborder" valign="top" width="50%">path</td><td class="cellrowborder" valign="top" width="50%">D:/temp/temp</td></tr></tbody></table>

The usage example is as follows:

![[en-us_image_0000002521400942.png]]

**Parent topic:** [[File|File]]