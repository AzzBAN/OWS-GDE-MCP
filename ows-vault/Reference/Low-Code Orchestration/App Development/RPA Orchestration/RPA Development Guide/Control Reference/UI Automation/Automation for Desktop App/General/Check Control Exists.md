---
title: "Check Control Exists"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560556.html"
depth: 8
---
# Check Control Exists

**hasElement**

**Description:**

Determines whether the element exists. When the element does not exist, it will be retried within the timeout period until the element exists (the check result is True) or the execution times out (the check result is False).

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560556__table42611mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560556__row42620mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560556__row42639mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">target</td><td class="cellrowborder" valign="top" width="16.666666666666664%">json</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Control Information</td></tr><tr id="EN-US_TOPIC_0000002521560556__row42653mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560556__row42667mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560556__table42683mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560556__row42691mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521560556__row42707mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">Boolean</td><td class="cellrowborder" valign="top" width="20%">has_element_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Check Result</td></tr></tbody></table>

**samples**

Determines whether the control (ListItemControl) whose ClassName is "TileListViewItem" exist

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560556__table42722mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560556__row42727mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560556__row42734mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">{"driver_type":"uiautomation","appName":"ShellExperienceHost.exe","by":"Path","offset-x":"53","offset-y":"63","target":[{"ClassName":"Windows.UI.Core.CoreWindow","x":"324","width":"100","y":"449","ControlType":"WindowControl","Name":"start up","height":"100"},{"ControlType":"WindowControl"},{"ClassName":"TileListView","ControlType":"ListControl"},{"ClassName":"TileListViewItem","ControlType":"GroupControl"},{"GlobalIndex":"1","ClassName":"TileListViewItem","ControlType":"ListItemControl"}]}</td></tr></tbody></table>

**Parent topic:** [[General|General]]