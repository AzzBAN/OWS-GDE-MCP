---
title: "While Loop"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560684.html"
depth: 7
---
# While Loop

**While**

**Description:**

While Loop Statement:

1.This control has two attributes: condition and timeout. condition indicates the condition for executing the loop, and timeout indicates the timeout interval.

2.When the conditions are met, the subprocess in the control is executed.

3.End the loop when the condition is not met or the timeout interval expires.

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560684__table18757mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560684__row18763mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521560684__row18773mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">fail_on_error</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Whether to exit the robot when the action fails</td></tr><tr id="EN-US_TOPIC_0000002521560684__row18781mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">timeout</td><td class="cellrowborder" valign="top" width="33.33333333333333%">number</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded; otherwise, the loop will not be terminated until the conditional expression does not hold.</td></tr><tr id="EN-US_TOPIC_0000002521560684__row18789mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">condition</td><td class="cellrowborder" valign="top" width="33.33333333333333%">python</td><td class="cellrowborder" valign="top" width="33.33333333333333%">While conditional expression which supports the Python expressions and can reference variables in the context</td></tr></tbody></table>

**Samples**

Loop the entry logic when the variable var<5

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560684__table18800mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560684__row18805mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560684__row18812mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">@{var}&lt;5</td></tr></tbody></table>

When the variable var is true, the entry logic is cyclically executed

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560684__table18819mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560684__row18824mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560684__row18831mcpsimp"><td class="cellrowborder" valign="top" width="50%">condition</td><td class="cellrowborder" valign="top" width="50%">@{var}</td></tr></tbody></table>

**Parent topic:** [[Flow Control|Flow Control]]