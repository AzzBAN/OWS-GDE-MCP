---
title: "Raw Mouse"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480893.html"
depth: 7
---
# Raw Mouse

**citrix.rawMouse**

**Description:**

Simulate a mouse click.When the type is LButtonDown (RButtonDown), LButtonUp (RButtonUp) is required for subsequent use

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480893__table46184mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480893__row46193mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46212mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">LButtonDown|LButtonUp|MouseWheel|RButtonDown|RButtonUp</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The type of mouse click action</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46226mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">pos</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">target coordinate</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46240mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">wheel</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The sliding distance of the scroll bar. Negative number means roll back, positive number means roll forward.When type is MouseWheel, use this parameter</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46254mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46268mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Left mouse button pressed

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480893__table46287mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480893__row46292mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46299mcpsimp"><td class="cellrowborder" valign="top" width="50%">type</td><td class="cellrowborder" valign="top" width="50%">LButtonDown</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46305mcpsimp"><td class="cellrowborder" valign="top" width="50%">pos</td><td class="cellrowborder" valign="top" width="50%">360,90</td></tr></tbody></table>

Left mouse button realese

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480893__table46312mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480893__row46317mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46324mcpsimp"><td class="cellrowborder" valign="top" width="50%">type</td><td class="cellrowborder" valign="top" width="50%">LButtonUp</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46330mcpsimp"><td class="cellrowborder" valign="top" width="50%">pos</td><td class="cellrowborder" valign="top" width="50%">360,90</td></tr></tbody></table>

right mouse button pressed

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480893__table46337mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480893__row46342mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46349mcpsimp"><td class="cellrowborder" valign="top" width="50%">type</td><td class="cellrowborder" valign="top" width="50%">RButtonDown</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46355mcpsimp"><td class="cellrowborder" valign="top" width="50%">pos</td><td class="cellrowborder" valign="top" width="50%">360,90</td></tr></tbody></table>

right mouse button realese

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480893__table46362mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480893__row46367mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46374mcpsimp"><td class="cellrowborder" valign="top" width="50%">type</td><td class="cellrowborder" valign="top" width="50%">RButtonUp</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46380mcpsimp"><td class="cellrowborder" valign="top" width="50%">pos</td><td class="cellrowborder" valign="top" width="50%">360,90</td></tr></tbody></table>

Mouse scroll block scroll event. The value of wheel is positive and the scroll direction is up; the value of wheel is negative and the scroll direction is down

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480893__table46387mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480893__row46392mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46399mcpsimp"><td class="cellrowborder" valign="top" width="50%">type</td><td class="cellrowborder" valign="top" width="50%">MouseWheel</td></tr><tr id="EN-US_TOPIC_0000002552480893__row46405mcpsimp"><td class="cellrowborder" valign="top" width="50%">wheel</td><td class="cellrowborder" valign="top" width="50%">-100</td></tr></tbody></table>

**Parent topic:** [[Image processing|Image processing]]