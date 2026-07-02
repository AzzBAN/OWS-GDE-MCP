---
title: "Raw Keyboard"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560934.html"
depth: 7
---
# Raw Keyboard

**citrix.rawKeyboard**

**Description:**

Press and release keys; this input is a key; cannot be a string; eg: Enter is a function key not a string

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560934__table21921mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560934__row21930mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560934__row21949mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">KeyDown|KeyUp</td><td class="cellrowborder" valign="top" width="16.666666666666664%">the type of keyboard input action</td></tr><tr id="EN-US_TOPIC_0000002521560934__row21963mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">key</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Key is the input value; Enter the key on the keyboard. For example:press Enter</td></tr><tr id="EN-US_TOPIC_0000002521560934__row21977mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560934__row21991mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Press the keyboard

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560934__table22010mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560934__row22015mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560934__row22022mcpsimp"><td class="cellrowborder" valign="top" width="50%">type</td><td class="cellrowborder" valign="top" width="50%">KeyDown</td></tr><tr id="EN-US_TOPIC_0000002521560934__row22028mcpsimp"><td class="cellrowborder" valign="top" width="50%">key</td><td class="cellrowborder" valign="top" width="50%">Enter</td></tr></tbody></table>

realse the keyboard

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560934__table22035mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560934__row22040mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560934__row22047mcpsimp"><td class="cellrowborder" valign="top" width="50%">type</td><td class="cellrowborder" valign="top" width="50%">KeyUp</td></tr><tr id="EN-US_TOPIC_0000002521560934__row22053mcpsimp"><td class="cellrowborder" valign="top" width="50%">key</td><td class="cellrowborder" valign="top" width="50%">Enter</td></tr></tbody></table>

**Parent topic:** [[Image processing|Image processing]]