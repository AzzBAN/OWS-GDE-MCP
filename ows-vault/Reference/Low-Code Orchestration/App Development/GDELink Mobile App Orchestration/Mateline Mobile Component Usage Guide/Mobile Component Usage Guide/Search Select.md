---
title: "Search Select"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731564186.html"
depth: 5
---
# Search Select

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001731564186__table2894mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:25%"> <col style="width:75%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001731564186__row2899mcpsimp"><td class="cellrowborder" valign="top" width="25%">Property Name</td><td class="cellrowborder" valign="top" width="75%">Description</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2904mcpsimp"><td class="cellrowborder" valign="top" width="25%">Aside Field</td><td class="cellrowborder" valign="top" width="75%">Side title of the search item</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2909mcpsimp"><td class="cellrowborder" valign="top" width="25%">Can Use When Offline</td><td class="cellrowborder" valign="top" width="75%">Whether the component is available in offline mode</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2914mcpsimp"><td class="cellrowborder" valign="top" width="25%">Header Field</td><td class="cellrowborder" valign="top" width="75%">Search item title</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2919mcpsimp"><td class="cellrowborder" valign="top" width="25%">Label</td><td class="cellrowborder" valign="top" width="75%">Component label</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2924mcpsimp"><td class="cellrowborder" valign="top" width="25%">Name</td><td class="cellrowborder" valign="top" width="75%">Component name</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2929mcpsimp"><td class="cellrowborder" valign="top" width="25%">Parent Select Name</td><td class="cellrowborder" valign="top" width="75%">Name of the cascaded parent component</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2934mcpsimp"><td class="cellrowborder" valign="top" width="25%">Place Holder</td><td class="cellrowborder" valign="top" width="75%">Placeholder</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2939mcpsimp"><td class="cellrowborder" valign="top" width="25%">Read Only</td><td class="cellrowborder" valign="top" width="75%">Whether the component is read-only</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2944mcpsimp"><td class="cellrowborder" valign="top" width="25%">Search Field</td><td class="cellrowborder" valign="top" width="75%">Search key. For example, if this parameter is set to text_id and 001 is entered in the search box, data whose text_id is 001 is searched.</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2949mcpsimp"><td class="cellrowborder" valign="top" width="25%">Service Id</td><td class="cellrowborder" valign="top" width="75%">Search service, that is, the service from which data is searched and obtained.</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2954mcpsimp"><td class="cellrowborder" valign="top" width="25%">Service Parameters</td><td class="cellrowborder" valign="top" width="75%">Service parameter</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2959mcpsimp"><td class="cellrowborder" valign="top" width="25%">Summary Field</td><td class="cellrowborder" valign="top" width="75%">Content field</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2964mcpsimp"><td class="cellrowborder" valign="top" width="25%">Text Field</td><td class="cellrowborder" valign="top" width="75%">Field displayed after data is selected</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2969mcpsimp"><td class="cellrowborder" valign="top" width="25%">Value</td><td class="cellrowborder" valign="top" width="75%">Default value</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2974mcpsimp"><td class="cellrowborder" valign="top" width="25%">Value Field</td><td class="cellrowborder" valign="top" width="75%">Value displayed after data is selected</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2979mcpsimp"><td class="cellrowborder" valign="top" width="25%">Visible</td><td class="cellrowborder" valign="top" width="75%">Whether the component is visible</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2984mcpsimp"><td class="cellrowborder" valign="top" width="25%">Width</td><td class="cellrowborder" valign="top" width="75%">Component width</td></tr><tr id="EN-US_TOPIC_0000001731564186__row2989mcpsimp"><td class="cellrowborder" valign="top" width="25%">Required</td><td class="cellrowborder" valign="top" width="75%">Whether the component is mandatory</td></tr></tbody></table>

**APIs**

**setTextAndValue(text,value)**

Input parameters: String

Output parameters: none

Description: Set the displayed value and actual value.

Example:

C("compId").setTextAndValue("Messi","Lionel Messi");

**setValue(value)**

Input parameters: String

Output parameters: none

Description: Set the value.

Example:

C("compId").setValue("Messi");

**getValue()**

Input parameters: none

Output parameters: String

Description: Set the value.

Example:

C("compId").getValue();

**Events**

N/A

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]