---
title: "Raw Keyboard"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480505.html"
depth: 8
---
# Raw Keyboard

**rawKeyboard**

**Description:**

Press and release the key; this input is a key; it cannot be a string of characters; for example: {Enter} is a function key and not a character string. for the writing of each function key, please refer to the help document 1.1.4.4 function key

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480505__table16372mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480505__row16381mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552480505__row16400mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">key-type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">press|release</td><td class="cellrowborder" valign="top" width="16.666666666666664%">the type of keyboard input action</td></tr><tr id="EN-US_TOPIC_0000002552480505__row16414mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">key</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Key is the input value; Enter the key on the keyboard. For example:press {Enter}</td></tr><tr id="EN-US_TOPIC_0000002552480505__row16428mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552480505__row16442mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Press the Enter keyboard

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480505__table16461mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480505__row16466mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480505__row16473mcpsimp"><td class="cellrowborder" valign="top" width="50%">key-type</td><td class="cellrowborder" valign="top" width="50%">press</td></tr><tr id="EN-US_TOPIC_0000002552480505__row16479mcpsimp"><td class="cellrowborder" valign="top" width="50%">key</td><td class="cellrowborder" valign="top" width="50%">{Enter}</td></tr></tbody></table>

Realse the Enter keyboard

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480505__table16486mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480505__row16491mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480505__row16498mcpsimp"><td class="cellrowborder" valign="top" width="50%">key-type</td><td class="cellrowborder" valign="top" width="50%">release</td></tr><tr id="EN-US_TOPIC_0000002552480505__row16504mcpsimp"><td class="cellrowborder" valign="top" width="50%">key</td><td class="cellrowborder" valign="top" width="50%">{Enter}</td></tr></tbody></table>

**Parent topic:** [[Keyboard|Keyboard]]