---
title: "If"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560659.html"
depth: 7
---
# If

**If**

**Description:**

If statement:

1.This control has two branches: do and else. If the conditions are met, the do branch is executed. Otherwise, the else branch is executed.

2.Edit the condition expression in the condition area.

3.The variable (@{name}) can be referenced in a condition expression.

4.Variables cannot be nested, that is, @{@{a}}).

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560659__table60408mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560659__row60414mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560659__row60424mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">fail_on_error</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Whether to exit the robot when the action fails</td></tr><tr id="EN-US_TOPIC_0000002552560659__row60432mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">condition</td><td class="cellrowborder" valign="top" width="33.33333333333333%">python</td><td class="cellrowborder" valign="top" width="33.33333333333333%">If conditional expression which supports the Python expressions and can reference variables in the context</td></tr></tbody></table>

**Samples**

Check whether the variable var contains the character string .pdf

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560659__table60443mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560659__row60448mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560659__row60455mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">".pdf" in @{var}</td></tr></tbody></table>

Check whether the variable var is 100

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560659__table60462mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560659__row60467mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560659__row60474mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">@{var}==100</td></tr></tbody></table>

Determine whether the variable var is neither 100 nor 200

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560659__table60481mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560659__row60486mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560659__row60493mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">@{var}!=100 and @{var}!=200</td></tr></tbody></table>

**Parent topic:** [[Flow Control|Flow Control]]