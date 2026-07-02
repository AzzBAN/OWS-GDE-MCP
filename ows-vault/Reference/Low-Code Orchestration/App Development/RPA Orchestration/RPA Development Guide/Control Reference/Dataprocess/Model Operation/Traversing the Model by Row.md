---
title: "Traversing the Model by Row"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560717.html"
depth: 7
---
# Traversing the Model by Row

**traverseModelData**

**Description:**

Traverse the model by row:

1.Traverse the model two-dimensional table by row. Any other control can be nested in the subprocess.

2.The 2D table to be traversed can be referenced only by variables.

3.The control also supports the normal use of break and continue, that is, stop traversing the 2D table and continue traversing the 2D table.

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560717__table139515mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560717__row139521mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560717__row139531mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">for_each</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">The name of the variable that stores the row data. Use numbers, letters, and underscores.</td></tr><tr id="EN-US_TOPIC_0000002552560717__row139539mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">of</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">References of Table object to traverse</td></tr><tr id="EN-US_TOPIC_0000002552560717__row139547mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">index_name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Index variable name.Leave blank and use the default variable name index</td></tr><tr id="EN-US_TOPIC_0000002552560717__row139555mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">is_parallel</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Concurrently execute the sub-processes that traverse the table. Note: 1. After Parallel Mode is enabled, an independent scope will be used in the sub-process, and modifications to parameters will not affect the values in the context (except for some reference variables that cannot be deep copied); 2. Concurrent use of system-level resources (physical mouse, keyboard, etc.) may cause conflicts. Please ensure that system-level resources are not used in the sub-process;</td></tr><tr id="EN-US_TOPIC_0000002552560717__row139566mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">parallel_max_num</td><td class="cellrowborder" valign="top" width="33.33333333333333%">number</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Maximum number of concurrent threads, which prevents system resources from being insufficient due to excessive threads(The default maximum number of concurrencies is the number of physical CPU cores of the computer * 2)</td></tr></tbody></table>

**Sample**

traverse\_model\_data

Create a model object in advance, 'model'：

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560717__table139578mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560717__row139584mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">id</td><td class="cellrowborder" valign="top" width="33.33333333333333%">filed 1</td><td class="cellrowborder" valign="top" width="33.33333333333333%">filed 2</td></tr><tr id="EN-US_TOPIC_0000002552560717__row139594mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">1</td><td class="cellrowborder" valign="top" width="33.33333333333333%">a1</td><td class="cellrowborder" valign="top" width="33.33333333333333%">a2</td></tr><tr id="EN-US_TOPIC_0000002552560717__row139602mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">2</td><td class="cellrowborder" valign="top" width="33.33333333333333%">b1</td><td class="cellrowborder" valign="top" width="33.33333333333333%">b2</td></tr></tbody></table>

row\_data stores the data of each row.

Traverse the model object by row and obtain the 'id' in each row.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560717__table139612mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560717__row139617mcpsimp"><td class="cellrowborder" valign="top" width="50%">Parameter Name</td><td class="cellrowborder" valign="top" width="50%">Parameter value transfer</td></tr><tr id="EN-US_TOPIC_0000002552560717__row139624mcpsimp"><td class="cellrowborder" valign="top" width="50%">for_each</td><td class="cellrowborder" valign="top" width="50%">row_data</td></tr><tr id="EN-US_TOPIC_0000002552560717__row139630mcpsimp"><td class="cellrowborder" valign="top" width="50%">of</td><td class="cellrowborder" valign="top" width="50%">modelName</td></tr></tbody></table>

row\_data stores the data of each row.

1\. Invoke Python and use @{row\_item}\['id'\] to obtain the ID of each line, corresponding to '1' and '2'.

**Parent topic:** [[Model Operation|Model Operation]]