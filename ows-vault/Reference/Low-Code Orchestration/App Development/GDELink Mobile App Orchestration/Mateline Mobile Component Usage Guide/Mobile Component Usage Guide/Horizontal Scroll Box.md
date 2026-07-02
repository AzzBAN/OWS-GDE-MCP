---
title: "Horizontal Scroll Box"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731723346.html"
depth: 5
---
# Horizontal Scroll Box

This component is a horizontal scroll box. Users can flick left or right to display images.

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001731723346__table5736mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:39%"> <col style="width:61%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001731723346__row5741mcpsimp"><td class="cellrowborder" valign="top" width="39%">Property Name</td><td class="cellrowborder" valign="top" width="61%">Description</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5746mcpsimp"><td class="cellrowborder" valign="top" width="39%">Use Cache Data</td><td class="cellrowborder" valign="top" width="61%">Whether to use cached data</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5751mcpsimp"><td class="cellrowborder" valign="top" width="39%">Image Description Field</td><td class="cellrowborder" valign="top" width="61%">Field configured as the image description field, which is returned by the service.</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5756mcpsimp"><td class="cellrowborder" valign="top" width="39%">Image Label Field</td><td class="cellrowborder" valign="top" width="61%">Field configured as the image label field, which is returned by the service.</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5761mcpsimp"><td class="cellrowborder" valign="top" width="39%">Image Link Parameters Field</td><td class="cellrowborder" valign="top" width="61%">Field configured as the image direction parameter field, which is returned by the service.</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5766mcpsimp"><td class="cellrowborder" valign="top" width="39%">Image Location Field</td><td class="cellrowborder" valign="top" width="61%">Field configured as the image direction location field, which is returned by the service.</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5771mcpsimp"><td class="cellrowborder" valign="top" width="39%">Image URL Field</td><td class="cellrowborder" valign="top" width="61%">Field configured as the image direction URL field, which is returned by the service.</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5776mcpsimp"><td class="cellrowborder" valign="top" width="39%">Label</td><td class="cellrowborder" valign="top" width="61%">Component label</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5781mcpsimp"><td class="cellrowborder" valign="top" width="39%">Name</td><td class="cellrowborder" valign="top" width="61%">Component name</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5786mcpsimp"><td class="cellrowborder" valign="top" width="39%">Service ID</td><td class="cellrowborder" valign="top" width="61%">ID of the service that dynamically obtains image information</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5791mcpsimp"><td class="cellrowborder" valign="top" width="39%">Service Parameters</td><td class="cellrowborder" valign="top" width="61%">Service input parameter</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5796mcpsimp"><td class="cellrowborder" valign="top" width="39%">Visible</td><td class="cellrowborder" valign="top" width="61%">Component visibility condition</td></tr><tr id="EN-US_TOPIC_0000001731723346__row5801mcpsimp"><td class="cellrowborder" valign="top" width="39%">LabelStyle</td><td class="cellrowborder" valign="top" width="61%">Label style</td></tr></tbody></table>

**APIs**

N/A

**Events**

**dataLoaded**

Description: The event is triggered after data loading is complete.

Example:

C("id").on("dataLoaded",function(json){

//do something

})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]