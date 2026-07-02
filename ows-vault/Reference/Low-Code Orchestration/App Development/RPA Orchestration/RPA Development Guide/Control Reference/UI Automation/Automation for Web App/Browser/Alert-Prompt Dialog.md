---
title: "Alert/Prompt Dialog"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560572.html"
depth: 8
---
# Alert/Prompt Dialog

**clickOnAlertDialog**

**Description:**

Click OK/Cancel in the alert/prompt box.

Note:

1.When prompted to find the control timeout exception information, you need to start the studio as an administrator to run the script.

2.This control does not support 360 browser

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560572__table46002mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560572__row46011mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46030mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">target</td><td class="cellrowborder" valign="top" width="16.666666666666664%">json</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Recorded or picked page information</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46044mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">accept</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True|False</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Accept or Not</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46058mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">input-value</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Enter a value in the Prompt text box.</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46072mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">tab-status</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">loading</td><td class="cellrowborder" valign="top" width="16.666666666666664%">complete|loading</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specifies the page loading policy before an operation is performed. Complete indicates that page loading needs to be completed. Loading indicates that page loading does not need to be completed. If this parameter is left empty, the default value Loading is used. This parameter does not apply to asynchronous AJAX requests.</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46086mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46100mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

The following configuration will click the "confirm" button in the alert box

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560572__table46119mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560572__row46124mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46131mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">**The json containing page element information**</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46137mcpsimp"><td class="cellrowborder" valign="top" width="50%">accept</td><td class="cellrowborder" valign="top" width="50%">True</td></tr></tbody></table>

The following configuration will click the "Confirm" button of the confirmation box with the input box, Fill in the input box with id\*\*\*\*\*

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560572__table46144mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560572__row46149mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46156mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">**json containing page element information**</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46162mcpsimp"><td class="cellrowborder" valign="top" width="50%">accept</td><td class="cellrowborder" valign="top" width="50%">True</td></tr><tr id="EN-US_TOPIC_0000002521560572__row46168mcpsimp"><td class="cellrowborder" valign="top" width="50%">input-value</td><td class="cellrowborder" valign="top" width="50%">id*****</td></tr></tbody></table>

**Parent topic:** [[Browser|Browser]]