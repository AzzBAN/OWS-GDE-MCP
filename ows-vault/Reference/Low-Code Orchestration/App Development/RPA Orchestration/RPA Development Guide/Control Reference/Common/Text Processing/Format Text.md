---
title: "Format Text"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400660.html"
depth: 7
---
# Format Text

**string.str\_format**

**Description:**

Format string, and return a new string. For example, if set \[Format Expression\] to 'hello {}', and \[Source String\] to 'world', you will get 'hello world'

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400660__table83843mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400660__row83852mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400660__row83871mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">value</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The source string to process</td></tr><tr id="EN-US_TOPIC_0000002521400660__row83885mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">format_expr</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Formatting expression.The format is one or more `{}`. See the example for details.</td></tr><tr id="EN-US_TOPIC_0000002521400660__row83899mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400660__table83915mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400660__row83923mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521400660__row83939mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">String</td><td class="cellrowborder" valign="top" width="20%">new_string</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">String after format</td></tr></tbody></table>

**Samples**

Create a string 'hello Johnny', 'Johnny' is the value of variable 'name'

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400660__table83954mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400660__row83959mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400660__row83966mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">@{name}</td></tr><tr id="EN-US_TOPIC_0000002521400660__row83972mcpsimp"><td class="cellrowborder" valign="top" width="50%">format_expr</td><td class="cellrowborder" valign="top" width="50%">hello {}</td></tr></tbody></table>

Create a string 'hello ABC ABC', ABC is the value of variable 'name'

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400660__table83979mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400660__row83984mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400660__row83991mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">@{name}</td></tr><tr id="EN-US_TOPIC_0000002521400660__row83997mcpsimp"><td class="cellrowborder" valign="top" width="50%">format_expr</td><td class="cellrowborder" valign="top" width="50%">hello {0} {0}</td></tr></tbody></table>

Create a string 'hello ABC', 'A','B','C' are the values of a list

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400660__table84004mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400660__row84009mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400660__row84016mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">['A','B','C']</td></tr><tr id="EN-US_TOPIC_0000002521400660__row84022mcpsimp"><td class="cellrowborder" valign="top" width="50%">format_expr</td><td class="cellrowborder" valign="top" width="50%">hello {0[0]} {0[1]} {0[2]}</td></tr></tbody></table>

Create a string 'Hello weautomate,welcome','weautomate' and 'welcome' are the values of a dict

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400660__table84029mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400660__row84034mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400660__row84041mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">{'name':'weautomate','msg':'welcome'}</td></tr><tr id="EN-US_TOPIC_0000002521400660__row84047mcpsimp"><td class="cellrowborder" valign="top" width="50%">format_expr</td><td class="cellrowborder" valign="top" width="50%">hello {name} {msg}</td></tr></tbody></table>

**Parent topic:** [[Text Processing|Text Processing]]