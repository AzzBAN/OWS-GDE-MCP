---
title: "Text Input Button"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731723326.html"
depth: 5
---
# Text Input Button

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001731723326__table5337mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:21%"> <col style="width:79%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001731723326__row5342mcpsimp"><td class="cellrowborder" valign="top" width="21%">Property Name</td><td class="cellrowborder" valign="top" width="79%">Description</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5347mcpsimp"><td class="cellrowborder" valign="top" width="21%">ColorRGB</td><td class="cellrowborder" valign="top" width="79%">Button text color</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5352mcpsimp"><td class="cellrowborder" valign="top" width="21%">Font Size</td><td class="cellrowborder" valign="top" width="79%">Font size</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5357mcpsimp"><td class="cellrowborder" valign="top" width="21%">Icon</td><td class="cellrowborder" valign="top" width="79%">Icon type</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5362mcpsimp"><td class="cellrowborder" valign="top" width="21%">Name</td><td class="cellrowborder" valign="top" width="79%">Component name</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5367mcpsimp"><td class="cellrowborder" valign="top" width="21%">Label</td><td class="cellrowborder" valign="top" width="79%">Component label</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5372mcpsimp"><td class="cellrowborder" valign="top" width="21%">Padding</td><td class="cellrowborder" valign="top" width="79%">Padding</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5377mcpsimp"><td class="cellrowborder" valign="top" width="21%">Visible</td><td class="cellrowborder" valign="top" width="79%">Visibility condition</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5382mcpsimp"><td class="cellrowborder" valign="top" width="21%">Color</td><td class="cellrowborder" valign="top" width="79%">Button text color. This parameter is available only when ColorRGB is not set.</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5387mcpsimp"><td class="cellrowborder" valign="top" width="21%">ComponentStyle</td><td class="cellrowborder" valign="top" width="79%">Style of a custom component</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5392mcpsimp"><td class="cellrowborder" valign="top" width="21%">Icon Position</td><td class="cellrowborder" valign="top" width="79%">Icon position, which can be placed on the left or right of the text.</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5397mcpsimp"><td class="cellrowborder" valign="top" width="21%">Width</td><td class="cellrowborder" valign="top" width="79%">Component width</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5402mcpsimp"><td class="cellrowborder" valign="top" width="21%">Size</td><td class="cellrowborder" valign="top" width="79%">Optional. The options include button-small (14 px) and button-large (16 px).</td></tr><tr id="EN-US_TOPIC_0000001731723326__row5407mcpsimp"><td class="cellrowborder" valign="top" width="21%">Style</td><td class="cellrowborder" valign="top" width="79%">Button style. For example, determine whether there is a border, whether the background is filled, and whether only the icon is displayed.</td></tr></tbody></table>

**APIs**

**setValue(value)**

Input parameters: String

Output parameters: none

Description: Set the value.

Example:

C("compId").setValue("aaa");

**Events**

**Click**

Example:

C("compId").on("click",function(){

console.log("aa");

});

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]