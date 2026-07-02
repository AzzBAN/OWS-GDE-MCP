---
title: "Get mac address"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480583.html"
depth: 7
---
# Get mac address

**sys.getMacAddress**

**Description:**

Get the mac address information of the network card

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480583__table118019mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480583__row118028mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552480583__row118047mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552480583__row118061mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480583__table118077mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480583__row118085mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002552480583__row118101mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">String</td><td class="cellrowborder" valign="top" width="20%">sysgetMacAddress_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">mac address info</td></tr></tbody></table>

**Samples**

Get the MAC address of the current computer

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480583__table118116mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480583__row118121mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480583__row118128mcpsimp"><td class="cellrowborder" valign="top" width="50%">return</td><td class="cellrowborder" valign="top" width="50%">getMacAddress_ret</td></tr></tbody></table>

**Parent topic:** [[OS|OS]]