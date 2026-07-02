---
title: "MultiIf"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480643.html"
depth: 7
---
# MultiIf

**MultiIf**

**Description:**

MultiIf statement:

1.The control is divided into multiple branches. Which branch is executed when the condition of the branch is met. Otherwise, the else branch is executed.

2.Edit the condition expression in the condition area.

3.The variable (@{name}) can be referenced in a condition expression.

4.Variables cannot be nested, that is, @{@{a}}).

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480643__table136093mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480643__row136099mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552480643__row136109mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">fail_on_error</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Whether to exit the robot when the action fails</td></tr></tbody></table>

**Samples**

Check whether the variable var contains the character string .pdf

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480643__table136120mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480643__row136125mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480643__row136132mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">".pdf" in @{var}</td></tr></tbody></table>

Check whether the variable var is 100

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480643__table136139mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480643__row136144mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480643__row136151mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">@{var}==100</td></tr></tbody></table>

Determine whether the variable var is neither 100 nor 200

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480643__table136158mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480643__row136163mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480643__row136170mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">@{var}!=100 and @{var}!=200</td></tr></tbody></table>

**Parent topic:** [[Flow Control|Flow Control]]