---
title: "Tab Panel"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001778643665.html"
depth: 5
---
# Tab Panel

Note: The Tab Panel component provides multiple tabs, but only one tab page can be opened at a time. You can click the relevant tab to switch the tab page.

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001778643665__table6334mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:56.99999999999999%"> <col style="width:43%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001778643665__row6339mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%">Property Name</td><td class="cellrowborder" valign="top" width="43%">Description</td></tr><tr id="EN-US_TOPIC_0000001778643665__row6344mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%">Id</td><td class="cellrowborder" valign="top" width="43%">Component ID</td></tr><tr id="EN-US_TOPIC_0000001778643665__row6349mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%">Tab Bar Background</td><td class="cellrowborder" valign="top" width="43%">Tab bar background style</td></tr><tr id="EN-US_TOPIC_0000001778643665__row6354mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%">Tab Bar Icon Style</td><td class="cellrowborder" valign="top" width="43%">Tab bar icon style</td></tr><tr id="EN-US_TOPIC_0000001778643665__row6359mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%">Tab Content Height</td><td class="cellrowborder" valign="top" width="43%">Tab content height</td></tr><tr id="EN-US_TOPIC_0000001778643665__row6364mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%">Tab Position</td><td class="cellrowborder" valign="top" width="43%">Tab bar position</td></tr></tbody></table>

**APIs**

**getSelectedIndex**

Input parameters: none

Output parameters: Number

Description: Obtain the index of the selected tab.

Example:

C("ComId").getSelectedIndex(); // **ComId** indicates the component ID.

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]