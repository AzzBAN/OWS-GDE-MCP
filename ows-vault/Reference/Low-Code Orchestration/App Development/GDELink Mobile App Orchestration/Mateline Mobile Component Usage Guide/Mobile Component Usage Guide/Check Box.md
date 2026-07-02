---
title: "Check Box"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731723306.html"
depth: 5
---
# Check Box

This is a check box component. The **Option** subitem needs to be configured.

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001731723306__table2670mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:53%"> <col style="width:47%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001731723306__row2675mcpsimp"><td class="cellrowborder" valign="top" width="53%">Property Name</td><td class="cellrowborder" valign="top" width="47%">Description</td></tr><tr id="EN-US_TOPIC_0000001731723306__row2680mcpsimp"><td class="cellrowborder" valign="top" width="53%">Label</td><td class="cellrowborder" valign="top" width="47%">Component label</td></tr><tr id="EN-US_TOPIC_0000001731723306__row2685mcpsimp"><td class="cellrowborder" valign="top" width="53%">Name</td><td class="cellrowborder" valign="top" width="47%">Component name</td></tr><tr id="EN-US_TOPIC_0000001731723306__row2690mcpsimp"><td class="cellrowborder" valign="top" width="53%">Read Only</td><td class="cellrowborder" valign="top" width="47%">Whether the component is read-only</td></tr><tr id="EN-US_TOPIC_0000001731723306__row2695mcpsimp"><td class="cellrowborder" valign="top" width="53%">Value</td><td class="cellrowborder" valign="top" width="47%">Initial value</td></tr><tr id="EN-US_TOPIC_0000001731723306__row2700mcpsimp"><td class="cellrowborder" valign="top" width="53%">Visible</td><td class="cellrowborder" valign="top" width="47%">Visibility condition</td></tr><tr id="EN-US_TOPIC_0000001731723306__row2705mcpsimp"><td class="cellrowborder" valign="top" width="53%">Width</td><td class="cellrowborder" valign="top" width="47%">Component width</td></tr><tr id="EN-US_TOPIC_0000001731723306__row2710mcpsimp"><td class="cellrowborder" valign="top" width="53%">Required</td><td class="cellrowborder" valign="top" width="47%">Whether the component is mandatory</td></tr></tbody></table>

**APIs**

**getValue**

Input parameters: none

Output parameters: String

Description: Obtain the value.

Example:

C("compId").getValue(); // **compId** indicates the component ID.

**setValue**

Input parameters: String

Output parameters: none

Description: Set the value.

Example:

C("check1").setValue("option1,''"); // Each option needs to be reset and the deselected options need to be set to null.

**setReadonly**

Input parameters: Boolean

Output parameters: none

Description: Set the component status to read-only.

Example:

C("check1").setReadonly(true);

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]