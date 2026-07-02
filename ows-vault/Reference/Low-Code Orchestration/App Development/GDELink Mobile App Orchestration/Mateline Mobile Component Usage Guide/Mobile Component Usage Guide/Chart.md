---
title: "Chart"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001782618373.html"
depth: 5
---
# Chart

Before a chart is displayed, you need to configure a dashboard chart. For details about how to configure the dashboard, see the secondary development guide.

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001782618373__table3622mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:43%"> <col style="width:56.99999999999999%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001782618373__row3627mcpsimp"><td class="cellrowborder" valign="top" width="43%">Property Name</td><td class="cellrowborder" valign="top" width="56.99999999999999%">Description</td></tr><tr id="EN-US_TOPIC_0000001782618373__row3632mcpsimp"><td class="cellrowborder" valign="top" width="43%">Height</td><td class="cellrowborder" valign="top" width="56.99999999999999%">Component height</td></tr><tr id="EN-US_TOPIC_0000001782618373__row3637mcpsimp"><td class="cellrowborder" valign="top" width="43%">Width</td><td class="cellrowborder" valign="top" width="56.99999999999999%">Component width</td></tr><tr id="EN-US_TOPIC_0000001782618373__row3642mcpsimp"><td class="cellrowborder" valign="top" width="43%">Widget Name</td><td class="cellrowborder" valign="top" width="56.99999999999999%">Name of the chart to be displayed</td></tr></tbody></table>

**APIs**

**refresh()**

Input parameters: none

Output parameters: none

Description: Refresh the list.

Example:

C("ComId").refresh(); // **ComId** indicates the component ID.

**getWidget()**

Input parameters: none

Output parameters: widget

Description: Obtain the chart object.

Example:

C("ComId").getWidget(); // **ComId** indicates the component ID.

**destroy()**

Input parameters: none

Output parameters: none

Description: Destroy a component.

Example:

C("ComId").destroy(); // **ComId** indicates the component ID.

**Events**

**chart\_before\_init**

Description: This event is triggered before initialization.

Example:

Spl.EventBus.registerById(id, "chart\_before\_init", function(params){});

**chart\_after\_init**

Description: This event is triggered after initialization.

Example:

Spl.EventBus.registerById(id, "chart\_after\_init", function(params){});

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]