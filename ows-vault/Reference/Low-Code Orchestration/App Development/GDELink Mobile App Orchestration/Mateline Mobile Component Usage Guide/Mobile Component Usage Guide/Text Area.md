---
title: "Text Area"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001778803353.html"
depth: 5
---
# Text Area

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001778803353__table4128mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:26%"> <col style="width:74%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001778803353__row4133mcpsimp"><td class="cellrowborder" valign="top" width="26%">Property Name</td><td class="cellrowborder" valign="top" width="74%">Description</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4138mcpsimp"><td class="cellrowborder" valign="top" width="26%">Allow Copy</td><td class="cellrowborder" valign="top" width="74%">Whether to allow replication</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4143mcpsimp"><td class="cellrowborder" valign="top" width="26%">Fixed Line</td><td class="cellrowborder" valign="top" width="74%">Component height, in text lines</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4148mcpsimp"><td class="cellrowborder" valign="top" width="26%">Open History</td><td class="cellrowborder" valign="top" width="74%">Whether to open the historical record. If the value is true, the historical record entered last time is displayed when the text box is clicked.</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4153mcpsimp"><td class="cellrowborder" valign="top" width="26%">Name</td><td class="cellrowborder" valign="top" width="74%">Component name</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4158mcpsimp"><td class="cellrowborder" valign="top" width="26%">Label</td><td class="cellrowborder" valign="top" width="74%">Component label</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4163mcpsimp"><td class="cellrowborder" valign="top" width="26%">Place Holder</td><td class="cellrowborder" valign="top" width="74%">Placeholder</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4168mcpsimp"><td class="cellrowborder" valign="top" width="26%">Read Only</td><td class="cellrowborder" valign="top" width="74%">Whether the component is read-only</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4173mcpsimp"><td class="cellrowborder" valign="top" width="26%">Tooltip</td><td class="cellrowborder" valign="top" width="74%">Pop-up message. After the configuration, a small icon is displayed in the upper right corner of the component. When you click the icon, a message is displayed.</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4178mcpsimp"><td class="cellrowborder" valign="top" width="26%">Value</td><td class="cellrowborder" valign="top" width="74%">Initial value of the component</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4183mcpsimp"><td class="cellrowborder" valign="top" width="26%">Visible</td><td class="cellrowborder" valign="top" width="74%">Visibility condition</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4188mcpsimp"><td class="cellrowborder" valign="top" width="26%">Width</td><td class="cellrowborder" valign="top" width="74%">Component width</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4193mcpsimp"><td class="cellrowborder" valign="top" width="26%">Avoid Special Chars</td><td class="cellrowborder" valign="top" width="74%">Whether special characters are not allowed</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4198mcpsimp"><td class="cellrowborder" valign="top" width="26%">Max Length</td><td class="cellrowborder" valign="top" width="74%">Maximum length</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4203mcpsimp"><td class="cellrowborder" valign="top" width="26%">Min Length</td><td class="cellrowborder" valign="top" width="74%">Minimum length</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4208mcpsimp"><td class="cellrowborder" valign="top" width="26%">Required</td><td class="cellrowborder" valign="top" width="74%">Whether the component is mandatory</td></tr><tr id="EN-US_TOPIC_0000001778803353__row4213mcpsimp"><td class="cellrowborder" valign="top" width="26%">Special Chars</td><td class="cellrowborder" valign="top" width="74%">Special characters that are not allowed. This property is used together with Avoid Special Chars.</td></tr></tbody></table>

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

**setConfig()**

Input parameters: String

Output parameters: none

Description: Set the verification mode of the component value length.

Example:

const currentPage = Nf.PageManager.getCurrentPage();

// Set the verification mode to character.

currentPage.setConfig("lengthValidation", "char");

// Set the verification mode to byte.

currentPage.setConfig("lengthValidation", "byte");

**Events**

**click**

Description: click event

Example:

C("id").on("click",function(){

//do something

})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]