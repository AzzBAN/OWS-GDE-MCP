---
title: "Traversing the Table by Column"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560732.html"
depth: 7
---
# Traversing the Table by Column

**pandasForEachColumn**

**Description:**

Traverse the pandas 2D table by column:

1.Traverse the DataFrame table by column. Any other control can be nested in the subprocess.

2.The 2D table to be traversed can be referenced only by variables.

3.The control also supports the normal use of break and continue, that is, stop or continue traversing the table.

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560732__table88002mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560732__row88008mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521560732__row88018mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">for_each</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">The name of the variable that stores the column data. Use numbers, letters, and underscores.</td></tr><tr id="EN-US_TOPIC_0000002521560732__row88026mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">of</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">References to table object to traverse</td></tr><tr id="EN-US_TOPIC_0000002521560732__row88034mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">index_name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Index variable name.Leave blank and use the default variable name index</td></tr></tbody></table>

**samples**

Traverse the reference variables of a dataframe by column. The data name of each row is column\_item

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560732__table88045mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560732__row88050mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560732__row88057mcpsimp"><td class="cellrowborder" valign="top" width="50%">for_each</td><td class="cellrowborder" valign="top" width="50%">column_item</td></tr><tr id="EN-US_TOPIC_0000002521560732__row88063mcpsimp"><td class="cellrowborder" valign="top" width="50%">of</td><td class="cellrowborder" valign="top" width="50%">@{dataframe_ret}</td></tr></tbody></table>

**Parent topic:** [[Table Data Processing|Table Data Processing]]