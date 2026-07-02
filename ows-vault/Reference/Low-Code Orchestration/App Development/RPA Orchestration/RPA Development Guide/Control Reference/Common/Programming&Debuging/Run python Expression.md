---
title: "Run python Expression"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400664.html"
depth: 7
---
# Run python Expression

**eval**

**Description:**

Run a python expression, and get the result, it will get None, if no result after running the expression

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400664__table97201mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400664__row97210mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97229mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">target</td><td class="cellrowborder" valign="top" width="16.666666666666664%">python</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Optional. When a built-in function is invoked in an expression, the corresponding package needs to be imported. Multiple packages can be imported at the same time, such as: import sys,os;import math.</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97243mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">value</td><td class="cellrowborder" valign="top" width="16.666666666666664%">python</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The single python expression.The value assignment statement is not supported. The operation on the object type does not return a value. Instead, the object itself is changed, for example, the `append` to the list.</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97257mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400664__table97273mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400664__row97281mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97297mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">Object</td><td class="cellrowborder" valign="top" width="20%">eval_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Save result to a variable, some expression will return None,such as operation to list,dict and so forth.</td></tr></tbody></table>

**Samples**

Evaluates the value of an expression. Create a variable named \`number\` and set value to 2,

The result is True

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400664__table97313mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400664__row97318mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97325mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">@{number}&gt;0</td></tr></tbody></table>

Concat path,create a variable 'folder' with value '/abc/',

and create variable 'iNum' with value 1, The result is

'/abc/file1.jpg'

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400664__table97334mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400664__row97339mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97346mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">@{folder}+ "\file\"+str(@{iNum})+".jpg"</td></tr></tbody></table>

Append a value to list,create a list type variable 'myList' with value \[1,2,3\],

The result is None, and the myList will be \[1,2,3,4\]

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400664__table97354mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400664__row97359mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97366mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">@{myList}.append(4)</td></tr></tbody></table>

Get value for a dict,create a dict type variable 'myDict' with value {"name":"joe"},

The result is 'joe'

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400664__table97374mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400664__row97379mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97386mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">@{myDict}.get('age')</td></tr></tbody></table>

Quote python's built-in library random to generate a random integer between 1 and 10

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400664__table97393mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400664__row97398mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97405mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">from random import randint</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97411mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">randint(1,10)</td></tr></tbody></table>

Kill process

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400664__table97418mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400664__row97423mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97430mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">import os</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97436mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">os.system('taskkill /IM chrome.exe /F')</td></tr></tbody></table>

Use the py file in the Lib directory (put testLib.py in the project directory/Lib)

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400664__table97443mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400664__row97448mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97455mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">import testLib</td></tr><tr id="EN-US_TOPIC_0000002521400664__row97461mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">testLib.test_print('print')</td></tr></tbody></table>

**Parent topic:** [[Programming&Debuging|Programming&Debuging]]