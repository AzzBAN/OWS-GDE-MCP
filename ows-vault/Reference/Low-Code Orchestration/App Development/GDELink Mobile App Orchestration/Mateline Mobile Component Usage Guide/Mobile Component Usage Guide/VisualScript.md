---
title: "VisualScript"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001778803405.html"
depth: 5
---
# VisualScript

The ECharts is displayed. Visual Script is the encapsulation of Baidu ECharts. Its WYSIWYG configuration is better than the dashboard. For details about how to configure the VisualScript charts, see Baidu ECharts APIs.

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001778803405__table4528mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:32%"> <col style="width:68%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001778803405__row4533mcpsimp"><td class="cellrowborder" valign="top" width="32%">Property Name</td><td class="cellrowborder" valign="top" width="68%">Description</td></tr><tr id="EN-US_TOPIC_0000001778803405__row4538mcpsimp"><td class="cellrowborder" valign="top" width="32%">Height</td><td class="cellrowborder" valign="top" width="68%">Component height</td></tr><tr id="EN-US_TOPIC_0000001778803405__row4543mcpsimp"><td class="cellrowborder" valign="top" width="32%">Width</td><td class="cellrowborder" valign="top" width="68%">Component width</td></tr><tr id="EN-US_TOPIC_0000001778803405__row4548mcpsimp"><td class="cellrowborder" valign="top" width="32%">Script</td><td class="cellrowborder" valign="top" width="68%">Name of the VisualScript chart to be displayed</td></tr><tr id="EN-US_TOPIC_0000001778803405__row4553mcpsimp"><td class="cellrowborder" valign="top" width="32%">Parameters</td><td class="cellrowborder" valign="top" width="68%">Input parameters required for configuring the data source service of the VisualScript chart</td></tr></tbody></table>

**APIs**

**autoRefresh(sec)**

Input parameters: Number

Output parameters: none

Description: Perform automatic refresh.

Example:

C("ComId").autoRefresh(1000); // **ComId** indicates the component ID. The component is refreshed every one second.

**refresh()**

Input parameters: none

Output parameters: none

Description: Refresh the chart.

Example:

C("ComId").refresh(); // **ComId** indicates the component ID.

**clearTimer()**

Input parameters: none

Output parameters: none

Description: Clear the automatic refresh.

Example:

C("ComId").clearTimer(); // **ComId** indicates the component ID.

**reload(parameters,\_options)**

Input parameters:

Service input parameter in parameters:json format.

\_options:{script:_xx_, width:_xx_, height:_xx_}: VisualScript script configuration

Output parameters: none

Description: Reload data.

Example:

C("ComId").reload({start:0,limit:10},{script:testWidget,width:200,height:200}); // **ComId** indicates the component ID.

**destroy()**

Input parameters: none

Output parameters: none

Description: Destroy a component.

Example:

C("ComId").destroy(); // **ComId** indicates the component ID.

**Events**

**dataLoaded**

Description: The event is triggered after data loading is complete.

Example:

C("id").on("dataLoaded",function(json){

//do something

})

**beforeInit**

Description: This event is triggered before initialization.

Example:

C("id").on("beforeInit",function(json){//do something})

**afterInit**

Description: This event is triggered after initialization.

Example:

C("id").on("afterInit",function(json){

//do something

})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]