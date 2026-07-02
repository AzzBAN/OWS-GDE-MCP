---
title: "Traversing the Table by Row"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480691.html"
depth: 7
---
# Traversing the Table by Row

**pandasForEachRow**

**Description:**

Traverse the table by row:

1.Traverse the DataFrame two-dimensional table by row. Any other control can be nested in the subprocess.

2.The 2D table to be traversed can be referenced only by variables.

3.The control also supports the normal use of break and continue, that is, stop traversing the 2D table and continue traversing the 2D table.

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480691__table154068mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480691__row154074mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552480691__row154084mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">for_each</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">The name of the variable that stores the row data. Use numbers, letters, and underscores.</td></tr><tr id="EN-US_TOPIC_0000002552480691__row154092mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">of</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">References of Table object to traverse</td></tr><tr id="EN-US_TOPIC_0000002552480691__row154100mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">index_name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Index variable name.Leave blank and use the default variable name index</td></tr><tr id="EN-US_TOPIC_0000002552480691__row154108mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">is_parallel</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Concurrently execute the sub-processes that traverse the table. Note: 1. After Parallel Mode is enabled, an independent scope will be used in the sub-process, and modifications to parameters will not affect the values in the context (except for some reference variables that cannot be deep copied); 2. Concurrent use of system-level resources (physical mouse, keyboard, etc.) may cause conflicts. Please ensure that system-level resources are not used in the sub-process;</td></tr><tr id="EN-US_TOPIC_0000002552480691__row154119mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">parallel_max_num</td><td class="cellrowborder" valign="top" width="33.33333333333333%">number</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Maximum number of concurrent threads, which prevents system resources from being insufficient due to excessive threads(The default maximum number of concurrencies is the number of physical CPU cores of the computer * 2)</td></tr></tbody></table>

**samples**

Create a DataFrame named 'df\_demo':

![[en-us_image_0000002521560986.png]]

Traversing 'df\_demo' by row to get 'name' in each row

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480691__table154132mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480691__row154137mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480691__row154144mcpsimp"><td class="cellrowborder" valign="top" width="50%">for_each</td><td class="cellrowborder" valign="top" width="50%">row_item</td></tr><tr id="EN-US_TOPIC_0000002552480691__row154150mcpsimp"><td class="cellrowborder" valign="top" width="50%">of</td><td class="cellrowborder" valign="top" width="50%">@{df_demo}</td></tr></tbody></table>

The 'row\_item' stores the data of each row.

1\. use @{row\_item}\['name'\] to obtain the value of 'name' of each row, which corresponds to 'Joe','Ken','Su'

2\. use Action 'series2list' translate 'row\_item' to list

**Parent topic:** [[Table Data Processing|Table Data Processing]]