---
title: "Multi Select"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001778643621.html"
depth: 5
---
# Multi Select

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001778643621__table6113mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:14.000000000000002%"> <col style="width:86%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001778643621__row6118mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Property Name</td><td class="cellrowborder" valign="top" width="86%">Description</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6123mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Label</td><td class="cellrowborder" valign="top" width="86%">Component label</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6128mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Name</td><td class="cellrowborder" valign="top" width="86%">Component name</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6133mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Output</td><td class="cellrowborder" valign="top" width="86%">Used to convert the loaded data of the query service to the value displayed in the drop-down list. Each option in the drop-down list has two field values: one displayed value and one hidden value. For example: {"text":"label","value":"name","parse_expr":"results"} indicates that the label field returned by the service is converted to the value displayed in the drop-down list and that the value of the name field is converted to the value in the drop-down list. parse_expr indicates that the data in the results node of the service is converted. If Output is not set, the value of the text field is displayed by default and that of the value field is hidden by default. The default value of parse_expr is results.</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6139mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Parameters</td><td class="cellrowborder" valign="top" width="86%">Service input parameter</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6144mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Place Holder</td><td class="cellrowborder" valign="top" width="86%">Component placeholder. This parameter is displayed when the value is empty.</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6149mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Read Only</td><td class="cellrowborder" valign="top" width="86%">Whether the component is read-only</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6154mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Service Id</td><td class="cellrowborder" valign="top" width="86%">Data source of the drop-down list</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6159mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Value</td><td class="cellrowborder" valign="top" width="86%">Initial value</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6164mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Value Delimiter</td><td class="cellrowborder" valign="top" width="86%">Value separator</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6169mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Visible</td><td class="cellrowborder" valign="top" width="86%">Visibility condition</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6174mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Width</td><td class="cellrowborder" valign="top" width="86%">Component width</td></tr><tr id="EN-US_TOPIC_0000001778643621__row6179mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%">Required</td><td class="cellrowborder" valign="top" width="86%">Whether the component is mandatory</td></tr></tbody></table>

**APIs**

**setReadonly**

Input parameters: Boolean

Output parameters: none

Description: The component status is set to read-only.

Example:

C("compId").setReadonly(true);

**getValue**

Input parameters: none

Output parameters: String

Description: Obtain the value.

Example:

C("compId").getValue();

**setValue**

Input parameters: String

Output parameters: none

Description: Set the value.

Example:

C("compId").setValue("value1;value2");

**reload**

Input parameter: **params**

Output parameters: none

Description: Reload the data source.

Example:

C("compId").reload({name:"level1"});

**addOptions**

Input parameters: Array or JSON

Output parameters: none

Description: Add static options.

Example:

C("compId").addOptions(\[{text:"option1",value:"option1"},{text:"option2",value:"option2"}\]);

**clearOptions**

Input parameters: Boolean. The value can be **true** or **false** and these parameters are optional.

Output parameters: none

Description: whether a specified multi-choice option is cleared. A Boolean value is transferred and the default value is **false**.

Example:

C("compId").clearOptions();

**Events**

**change**

Description: event triggered when the value changes

Example:

C("id").on("change",function(json){

//do something

})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]