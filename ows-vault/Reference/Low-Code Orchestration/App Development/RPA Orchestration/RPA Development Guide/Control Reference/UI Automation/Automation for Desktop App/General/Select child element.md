---
title: "Select child element"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480519.html"
depth: 8
---
# Select child element

**select**

**Description:**

Select child element

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480519__table28924mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480519__row28933mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552480519__row28952mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">target</td><td class="cellrowborder" valign="top" width="16.666666666666664%">json</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Control Information</td></tr><tr id="EN-US_TOPIC_0000002552480519__row28966mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">by</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">text</td><td class="cellrowborder" valign="top" width="16.666666666666664%">index|text</td><td class="cellrowborder" valign="top" width="16.666666666666664%">pattern</td></tr><tr id="EN-US_TOPIC_0000002552480519__row28980mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">value</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The value of the option</td></tr><tr id="EN-US_TOPIC_0000002552480519__row28994mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552480519__row29008mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples1**

Selects the win32 menu whose text value is 'This PC'.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480519__table29027mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480519__row29032mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480519__row29039mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">{"driver_type":"uiautomation","appName":"explorer.exe","title":"wa-uidesktop","offset-x":"161","offset-y":"16","target": [{"ClassName":"CabinetWClass","x":"612","width":"229","y":"358","ControlType":"WindowControl","Name":"wa-uidesktop","height":"25"},{"ClassName":"#32770","ControlType":"WindowControl","Name": "folder option "},{"GlobalIndex":"2","ClassName":"ComboBox","ControlType":"ComboBoxControl","Name": "Open when opening File Explorer"}]}</td></tr><tr id="EN-US_TOPIC_0000002552480519__row29045mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">This PC</td></tr></tbody></table>

**samples2**

Selects the sap menu whose index is 1.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480519__table29054mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480519__row29059mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480519__row29066mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">**JSON** containing sap element information</td></tr><tr id="EN-US_TOPIC_0000002552480519__row29072mcpsimp"><td class="cellrowborder" valign="top" width="50%">by</td><td class="cellrowborder" valign="top" width="50%">index</td></tr><tr id="EN-US_TOPIC_0000002552480519__row29078mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">1</td></tr></tbody></table>

**samples3**

Selects the sap menu whose text value is 'first'.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480519__table29087mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480519__row29092mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480519__row29099mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">**JSON** containing sap element information</td></tr><tr id="EN-US_TOPIC_0000002552480519__row29105mcpsimp"><td class="cellrowborder" valign="top" width="50%">by</td><td class="cellrowborder" valign="top" width="50%">text</td></tr><tr id="EN-US_TOPIC_0000002552480519__row29111mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">first</td></tr></tbody></table>

**Parent topic:** [[General|General]]