---
title: "For In Count"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480645.html"
depth: 7
---
# For In Count

**ForInCount**

**Description:**

ForInCount Loop Statement:

It's used for a loop. The value of the start number is incremented each time until the value of the start number reaches the value of the end number.

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480645__table103329mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480645__row103335mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552480645__row103345mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">fail_on_error</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Whether to exit the robot when the action fails</td></tr><tr id="EN-US_TOPIC_0000002552480645__row103353mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">start</td><td class="cellrowborder" valign="top" width="33.33333333333333%">number</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Loop start count</td></tr><tr id="EN-US_TOPIC_0000002552480645__row103361mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">end</td><td class="cellrowborder" valign="top" width="33.33333333333333%">number</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Loop end count</td></tr><tr id="EN-US_TOPIC_0000002552480645__row103369mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">step</td><td class="cellrowborder" valign="top" width="33.33333333333333%">number</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Increment count</td></tr><tr id="EN-US_TOPIC_0000002552480645__row103377mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">current_count_name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Current count variable name.Leave blank and use the default variable name current_count</td></tr></tbody></table>

**Samples**

Cycle 10 times

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480645__table103388mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480645__row103393mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480645__row103400mcpsimp"><td class="cellrowborder" valign="top" width="50%">end</td><td class="cellrowborder" valign="top" width="50%">10</td></tr></tbody></table>

Cycle 3 times

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480645__table103407mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480645__row103412mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480645__row103419mcpsimp"><td class="cellrowborder" valign="top" width="50%">start</td><td class="cellrowborder" valign="top" width="50%">4</td></tr><tr id="EN-US_TOPIC_0000002552480645__row103425mcpsimp"><td class="cellrowborder" valign="top" width="50%">step</td><td class="cellrowborder" valign="top" width="50%">-1</td></tr><tr id="EN-US_TOPIC_0000002552480645__row103431mcpsimp"><td class="cellrowborder" valign="top" width="50%">end</td><td class="cellrowborder" valign="top" width="50%">1</td></tr></tbody></table>

**Parent topic:** [[Flow Control|Flow Control]]