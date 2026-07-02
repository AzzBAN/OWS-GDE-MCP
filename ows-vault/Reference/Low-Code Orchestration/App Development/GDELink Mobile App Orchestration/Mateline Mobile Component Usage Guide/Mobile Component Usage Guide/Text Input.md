---
title: "Text Input"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001778643641.html"
depth: 5
---
# Text Input

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001778643641__table5423mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:26%"> <col style="width:74%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001778643641__row5428mcpsimp"><td class="cellrowborder" valign="top" width="26%">Property Name</td><td class="cellrowborder" valign="top" width="74%">Description</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5433mcpsimp"><td class="cellrowborder" valign="top" width="26%">Allow Copy</td><td class="cellrowborder" valign="top" width="74%">Whether to allow replication</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5438mcpsimp"><td class="cellrowborder" valign="top" width="26%">Open History</td><td class="cellrowborder" valign="top" width="74%">Whether to open the historical record. If the value is true, the historical record entered last time is displayed when the text box is clicked.</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5443mcpsimp"><td class="cellrowborder" valign="top" width="26%">Name</td><td class="cellrowborder" valign="top" width="74%">Component name</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5448mcpsimp"><td class="cellrowborder" valign="top" width="26%">Label</td><td class="cellrowborder" valign="top" width="74%">Component label</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5453mcpsimp"><td class="cellrowborder" valign="top" width="26%">Place Holder</td><td class="cellrowborder" valign="top" width="74%">Placeholder</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5458mcpsimp"><td class="cellrowborder" valign="top" width="26%">Read Only</td><td class="cellrowborder" valign="top" width="74%">Whether the component is read-only</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5463mcpsimp"><td class="cellrowborder" valign="top" width="26%">Tooltip</td><td class="cellrowborder" valign="top" width="74%">Prompt information</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5468mcpsimp"><td class="cellrowborder" valign="top" width="26%">Value</td><td class="cellrowborder" valign="top" width="74%">Initial value of the component</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5473mcpsimp"><td class="cellrowborder" valign="top" width="26%">Visible</td><td class="cellrowborder" valign="top" width="74%">Visibility condition</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5478mcpsimp"><td class="cellrowborder" valign="top" width="26%">Width</td><td class="cellrowborder" valign="top" width="74%">Component width</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5483mcpsimp"><td class="cellrowborder" valign="top" width="26%">Avoid Special Chars</td><td class="cellrowborder" valign="top" width="74%">Whether special characters are forbidden</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5488mcpsimp"><td class="cellrowborder" valign="top" width="26%">Max Length</td><td class="cellrowborder" valign="top" width="74%">Maximum length</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5493mcpsimp"><td class="cellrowborder" valign="top" width="26%">Min Length</td><td class="cellrowborder" valign="top" width="74%">Minimum length</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5498mcpsimp"><td class="cellrowborder" valign="top" width="26%">Required</td><td class="cellrowborder" valign="top" width="74%">Whether the component is mandatory</td></tr><tr id="EN-US_TOPIC_0000001778643641__row5503mcpsimp"><td class="cellrowborder" valign="top" width="26%">Special Chars</td><td class="cellrowborder" valign="top" width="74%">Special characters that are not allowed. This property is used together with Avoid Special Chars.</td></tr></tbody></table>

**APIs**

**setValue(value)**

Input parameters: String

Output parameters: none

Description: Set the value.

Example:

C("compId").setValue("aaa");

**getValue()**

Input parameters: none

Output parameters: String

Description: Set the value.

Example:

C("compId").getValue();

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]