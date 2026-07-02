---
title: "Person Select"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731723314.html"
depth: 5
---
# Person Select

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001731723314__table2821mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:28.999999999999996%"> <col style="width:71%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001731723314__row2826mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">Property Name</td><td class="cellrowborder" valign="top" width="71%">Description</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2831mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">label</td><td class="cellrowborder" valign="top" width="71%">Component label</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2836mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">Display Name Type</td><td class="cellrowborder" valign="top" width="71%">Value type, including full user name and user name</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2841mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">Name</td><td class="cellrowborder" valign="top" width="71%">Component name</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2846mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">Read Only</td><td class="cellrowborder" valign="top" width="71%">Whether the component is read-only</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2851mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">Value</td><td class="cellrowborder" valign="top" width="71%">Initial value</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2856mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">Visible</td><td class="cellrowborder" valign="top" width="71%">Visibility condition</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2861mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">ServiceId</td><td class="cellrowborder" valign="top" width="71%">Service for querying a user. The default value is mobilesocial_search_userlist.</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2866mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">Width</td><td class="cellrowborder" valign="top" width="71%">Component width</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2871mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">Can Select Myself</td><td class="cellrowborder" valign="top" width="71%">Whether the login user can be selected</td></tr><tr id="EN-US_TOPIC_0000001731723314__row2876mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%">Required</td><td class="cellrowborder" valign="top" width="71%">Whether the component is mandatory</td></tr></tbody></table>

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