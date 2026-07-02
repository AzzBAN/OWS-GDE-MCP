---
title: "List Filter Item"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731723362.html"
depth: 5
---
# List Filter Item

Used to set the filtering item.

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001731723362__table6418mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:15%"> <col style="width:85%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001731723362__row6423mcpsimp"><td class="cellrowborder" valign="top" width="15%">Property Name</td><td class="cellrowborder" valign="top" width="85%">Description</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6428mcpsimp"><td class="cellrowborder" valign="top" width="15%">Default Value</td><td class="cellrowborder" valign="top" width="85%">Default value of the filtering item</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6433mcpsimp"><td class="cellrowborder" valign="top" width="15%">Id</td><td class="cellrowborder" valign="top" width="85%">Component ID</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6438mcpsimp"><td class="cellrowborder" valign="top" width="15%">Label</td><td class="cellrowborder" valign="top" width="85%">Filtering item label</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6443mcpsimp"><td class="cellrowborder" valign="top" width="15%">Model Key</td><td class="cellrowborder" valign="top" width="85%">Model field to be used for filtering</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6448mcpsimp"><td class="cellrowborder" valign="top" width="15%">Operator</td><td class="cellrowborder" valign="top" width="85%">Operator. The options are &gt;, &lt;, &gt;=, and &lt;=. This property takes effect when Type is set to select. To use an operator, the filter value must be in the {{xx}} format.</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6453mcpsimp"><td class="cellrowborder" valign="top" width="15%">Options</td><td class="cellrowborder" valign="top" width="85%">Static option. This property takes effect only when Type is set to select or multiSelect.</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6458mcpsimp"><td class="cellrowborder" valign="top" width="15%">Output</td><td class="cellrowborder" valign="top" width="85%">Used to convert the loaded data of the query service to the value displayed in the drop-down list. Each option in the drop-down list has two field values: one displayed value and one hidden value. This property takes effect only when Type is set to select or multiSelect. For example: {"text":"label","value":"name","parse_expr":"results"} indicates that the label field returned by the service is converted to the value displayed in the drop-down list and that the value of the name field is converted to the value in the drop-down list. parse_expr indicates that the data in the results node of the service is converted. If Output is not set, the value of the text field is displayed by default and that of the value field is hidden by default. The default value of parse_expr is results.</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6464mcpsimp"><td class="cellrowborder" valign="top" width="15%">Parameters</td><td class="cellrowborder" valign="top" width="85%">This property is used with Service Id and functions as service input parameters.</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6469mcpsimp"><td class="cellrowborder" valign="top" width="15%">Parent Id</td><td class="cellrowborder" valign="top" width="85%">Used for filtering. The usage of this property is the same as that of the Simple Select component.</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6474mcpsimp"><td class="cellrowborder" valign="top" width="15%">Parent Key</td><td class="cellrowborder" valign="top" width="85%">Used for filtering. The usage of this property is the same as that of the Simple Select component.</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6479mcpsimp"><td class="cellrowborder" valign="top" width="15%">Service Id</td><td class="cellrowborder" valign="top" width="85%">This property takes effect only when Type is set to select or multiSelect. It is used to load the filter item data source.</td></tr><tr id="EN-US_TOPIC_0000001731723362__row6484mcpsimp"><td class="cellrowborder" valign="top" width="15%">Type</td><td class="cellrowborder" valign="top" width="85%">The options are input, datetime, select, and multiSelect. This property is used to configure different types of filtering items.</td></tr></tbody></table>

**Events**

**selectFilterChanged**

Description: This vent is triggered when a filtering item is selected.

Example:

C("id").on("selectFilterChanged",function(option){

//do something

})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]