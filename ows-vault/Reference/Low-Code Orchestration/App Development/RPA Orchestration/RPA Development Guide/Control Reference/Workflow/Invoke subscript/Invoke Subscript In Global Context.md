---
title: "Invoke Subscript In Global Context"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480647.html"
depth: 7
---
# Invoke Subscript In Global Context

**Subprocess**

**Description:**

Invoke subscript within a global context.All parameters and variables defined before invoking are visible in the subscript and can be modified,it's not recommended

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480647__table3363mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480647__row3369mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552480647__row3379mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">fail_on_error</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Whether to exit the robot when the action fails</td></tr><tr id="EN-US_TOPIC_0000002552480647__row3387mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">subScript</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Subscript file name</td></tr></tbody></table>

**Samples**

Invoke the subscript script01.xml in the directory as a relative path

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480647__table3398mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480647__row3403mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480647__row3410mcpsimp"><td class="cellrowborder" valign="top" width="50%">subScript</td><td class="cellrowborder" valign="top" width="50%">script01.xml</td></tr></tbody></table>

Invoke the subscript script02.xml in the subdirectory as a relative path

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480647__table3417mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480647__row3422mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480647__row3429mcpsimp"><td class="cellrowborder" valign="top" width="50%">subScript</td><td class="cellrowborder" valign="top" width="50%">sub/script01.xml</td></tr></tbody></table>

**Parent topic:** [[Invoke subscript|Invoke subscript]]