---
title: "Number Input"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731564182.html"
depth: 5
---
# Number Input

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001731564182__table2733mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:38%"> <col style="width:62%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001731564182__row2738mcpsimp"><td class="cellrowborder" valign="top" width="38%">Property Name</td><td class="cellrowborder" valign="top" width="62%">Description</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2743mcpsimp"><td class="cellrowborder" valign="top" width="38%">label</td><td class="cellrowborder" valign="top" width="62%">Component label</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2748mcpsimp"><td class="cellrowborder" valign="top" width="38%">Name</td><td class="cellrowborder" valign="top" width="62%">Component name</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2753mcpsimp"><td class="cellrowborder" valign="top" width="38%">Pattern</td><td class="cellrowborder" valign="top" width="62%">Type. The value can be Float or Integer.</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2758mcpsimp"><td class="cellrowborder" valign="top" width="38%">Read Only</td><td class="cellrowborder" valign="top" width="62%">Whether the component is read-only</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2763mcpsimp"><td class="cellrowborder" valign="top" width="38%">Value</td><td class="cellrowborder" valign="top" width="62%">Initial value</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2768mcpsimp"><td class="cellrowborder" valign="top" width="38%">Visible</td><td class="cellrowborder" valign="top" width="62%">Visibility condition</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2773mcpsimp"><td class="cellrowborder" valign="top" width="38%">Width</td><td class="cellrowborder" valign="top" width="62%">Component width</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2778mcpsimp"><td class="cellrowborder" valign="top" width="38%">Max</td><td class="cellrowborder" valign="top" width="62%">Maximum value</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2783mcpsimp"><td class="cellrowborder" valign="top" width="38%">Min</td><td class="cellrowborder" valign="top" width="62%">Minimum value</td></tr><tr id="EN-US_TOPIC_0000001731564182__row2788mcpsimp"><td class="cellrowborder" valign="top" width="38%">Required</td><td class="cellrowborder" valign="top" width="62%">Whether the component is mandatory</td></tr></tbody></table>

**APIs**

**getValue**

Input parameters: none

Output parameters: String

Description: Obtain the value.

Example:

C("compId").getValue();

**setValue**

Input parameters: String or Number

Output parameters: none

Description: Set the value.

Example:

C("compId").setValue("111");

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]