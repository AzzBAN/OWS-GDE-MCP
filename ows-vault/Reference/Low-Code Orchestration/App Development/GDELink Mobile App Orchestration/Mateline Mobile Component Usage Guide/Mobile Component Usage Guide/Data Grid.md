---
title: "Data Grid"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001778643645.html"
depth: 5
---
# Data Grid

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001778643645__table3173mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:28.000000000000004%"> <col style="width:72%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001778643645__row3178mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%">Property Name</td><td class="cellrowborder" valign="top" width="72%">Description</td></tr><tr id="EN-US_TOPIC_0000001778643645__row3183mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%">Can Use When Offline</td><td class="cellrowborder" valign="top" width="72%">Whether to use cached data. The value is of the Boolean type.</td></tr><tr id="EN-US_TOPIC_0000001778643645__row3188mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%">Service Id</td><td class="cellrowborder" valign="top" width="72%">Service name, which is used to obtain table data.</td></tr><tr id="EN-US_TOPIC_0000001778643645__row3193mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%">Parameters</td><td class="cellrowborder" valign="top" width="72%">Service parameter</td></tr><tr id="EN-US_TOPIC_0000001778643645__row3198mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%">Align</td><td class="cellrowborder" valign="top" width="72%">Data alignment mode in a table</td></tr><tr id="EN-US_TOPIC_0000001778643645__row3203mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%">Direction</td><td class="cellrowborder" valign="top" width="72%">Table display direction. vertical: The header is in the upper part. horizontal: The header is on the left.</td></tr></tbody></table>

**APIs**

**hide()**

Input parameters: none

Output parameters: none

Description: Hide a table.

Example:

C("compId").hide();

**show()**

Input parameters: none

Output parameters: none

Description: Show the table.

Example:

C("compId").show();

**reload(serviceId, customParam, customCallback)**

Input parameters: **serviceId**: service name. **customParam**: parameters. **customCallback**: callback after the loading is complete.

Output parameters: none

Description: Reload the table data.

Example:

C("compId").reload("ms\_contacts\_info\_getList",{"start":5},func);

**doRefresh()**

Input parameters: none

Output parameters: none

Description: Refresh the table.

Example:

C("compId").doRefresh();

**Events**

**dataLoaded**

Description: An event is called after data is loaded.

Example:

C("compId").on("dataLoaded",function(json){

console.log(json.results);

});

**click**

Example:

C("compId").on("click",function(row,config){

console.log(config.header);

});

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]