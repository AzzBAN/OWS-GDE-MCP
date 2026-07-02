---
title: "Save as workbook"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480457.html"
depth: 8
---
# Save as workbook

**excelSaveAsWorkbook**

**Description:**

Save as a workbook

Note:

1.Changing the file type may fail because format conversion is not supported

2.if the excelsaveasworkbook command is executed without subsequent operations, execute the excelcloseworkbook command to close the saved excel workbook

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480457__table83672mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480457__row83678mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552480457__row83688mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">ExcelObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Enter an Excel object opened using the ExcelApplicationScope control</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480457__table83698mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480457__row83707mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552480457__row83726mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">file-name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">new_file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">xlsx|xlsm|xls|xlsb|et</td><td class="cellrowborder" valign="top" width="16.666666666666664%">the path of Saving as workbook</td></tr><tr id="EN-US_TOPIC_0000002552480457__row83740mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">is-replace</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">False</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True|False</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The path saved as a workbook has the same name, whether to overwrite files with the same name: True means to overwrite files with the same name, False means not to overwrite files with the same name, default is False</td></tr><tr id="EN-US_TOPIC_0000002552480457__row83754mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">password</td><td class="cellrowborder" valign="top" width="16.666666666666664%">password</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Read-only permission password for Excel files</td></tr><tr id="EN-US_TOPIC_0000002552480457__row83768mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">write-password</td><td class="cellrowborder" valign="top" width="16.666666666666664%">password</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Writing permission password for Excel files</td></tr><tr id="EN-US_TOPIC_0000002552480457__row83782mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552480457__row83796mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Configure the following configuration to write the test.xlsx workbook and save it as a new table

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480457__table83815mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480457__row83820mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480457__row83827mcpsimp"><td class="cellrowborder" valign="top" width="50%">file-name</td><td class="cellrowborder" valign="top" width="50%">@{WORK_DIR}\\test3.xlsx</td></tr></tbody></table>

**Parent topic:** [[Common|Common]]