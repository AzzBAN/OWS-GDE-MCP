---
title: "Format Number"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560666.html"
depth: 7
---
# Format Number

**string.number\_format**

**Description:**

Format number, and return a new number. For example, if set \[Format Expression\] to '{:.2f}', and \[Source Number\] to '3.1415926', you will get 3.14

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560666__table64412mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560666__row64421mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64440mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">value</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The source number to format</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64454mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">format_expr</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Formatting expression.'{:.2f}' means keep two decimal places.</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64468mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560666__table64484mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560666__row64492mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64508mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">String</td><td class="cellrowborder" valign="top" width="20%">new_number</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Number after format</td></tr></tbody></table>

**Samples**

format 0.25 to 25.00%

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560666__table64523mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560666__row64528mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64535mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">0.25</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64541mcpsimp"><td class="cellrowborder" valign="top" width="50%">format_expr</td><td class="cellrowborder" valign="top" width="50%">{:.2%}</td></tr></tbody></table>

format 3.1415926 to +3.14

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560666__table64548mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560666__row64553mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64560mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">3.1415926</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64566mcpsimp"><td class="cellrowborder" valign="top" width="50%">format_expr</td><td class="cellrowborder" valign="top" width="50%">{:+.2f}</td></tr></tbody></table>

format 11 to binary 1011(In the format, b, d, o, and x are binary, decimal, octal, and hexadecimal, respectively.)

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560666__table64573mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560666__row64578mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64585mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">11</td></tr><tr id="EN-US_TOPIC_0000002521560666__row64591mcpsimp"><td class="cellrowborder" valign="top" width="50%">format_expr</td><td class="cellrowborder" valign="top" width="50%">{:b}</td></tr></tbody></table>

**Parent topic:** [[Text Processing|Text Processing]]