---
title: "Transfer Output Text To Dict"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560648.html"
depth: 7
---
# Transfer Output Text To Dict

**console.outputTextToDict**

**Description:**

Converts tabular output text to a dict.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560648__table137699mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560648__row137708mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137727mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">terminal_output_text</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The text output from executing a terminal command.</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137741mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">ignore_empty_value</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">False</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True|False</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Whether to skip when the key value recognized in the current row is empty</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137755mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">selected_keys</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specifies the list of keys to be extracted. Multiple keys should be separated by semicolons. If this parameter is left blank, all valid data will be extracted.</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137769mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">separator</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">:</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Separator of a key-value pair. The default value is a ":".</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137783mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137797mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay before the current operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560648__table137813mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560648__row137821mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137837mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">Object</td><td class="cellrowborder" valign="top" width="20%">outputTextToDict_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Dict converted from output text</td></tr></tbody></table>

**samples**

Convert the terminal output text into a dict (ignore the blank lines and select only the key-value A B. The key-value pair separator is:)

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560648__table137852mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560648__row137857mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137864mcpsimp"><td class="cellrowborder" valign="top" width="50%">terminal_output_text</td><td class="cellrowborder" valign="top" width="50%">A:a1<br><br>B:b1<br>C:c1<br></td></tr><tr id="EN-US_TOPIC_0000002521560648__row137870mcpsimp"><td class="cellrowborder" valign="top" width="50%">ignore_empty_value</td><td class="cellrowborder" valign="top" width="50%">True</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137876mcpsimp"><td class="cellrowborder" valign="top" width="50%">selected_keys</td><td class="cellrowborder" valign="top" width="50%">A;B</td></tr><tr id="EN-US_TOPIC_0000002521560648__row137882mcpsimp"><td class="cellrowborder" valign="top" width="50%">separator</td><td class="cellrowborder" valign="top" width="50%">:</td></tr></tbody></table>

Expected Result:

\`\`\`

{"A": "a1", "B": "b1"}

\`\`\`

The usage example is as follows:

![[en-us_image_0000002521560962.png]]

**Parent topic:** [[Terminal|Terminal]]