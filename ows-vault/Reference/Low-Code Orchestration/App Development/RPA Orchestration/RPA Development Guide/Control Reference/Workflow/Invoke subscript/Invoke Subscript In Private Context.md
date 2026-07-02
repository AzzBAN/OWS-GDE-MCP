---
title: "Invoke Subscript In Private Context"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560688.html"
depth: 7
---
# Invoke Subscript In Private Context

**CallScript**

**Description:**

Invoke subscript with local scope. The parameters and variables defined in the current script are invisible and cannot be modified in the invoked script. If a subscript requires the parameters or variables defined in the current script, you need to define parameters of the "in" type in the subscript and transfer the parameters or variables as input parameters in the current script.

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560688__table39767mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560688__row39773mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521560688__row39783mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">fail_on_error</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Whether to exit the robot when the action fails</td></tr><tr id="EN-US_TOPIC_0000002521560688__row39791mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">callScript</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Subscript file name</td></tr></tbody></table>

**Samples**

Invoke the subscript script01.xml in the directory as a relative path

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560688__table39802mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560688__row39807mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560688__row39814mcpsimp"><td class="cellrowborder" valign="top" width="50%">callScript</td><td class="cellrowborder" valign="top" width="50%">script01.xml</td></tr></tbody></table>

Invoke the subscript script02.xml in the subdirectory as a relative path

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560688__table39821mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560688__row39826mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560688__row39833mcpsimp"><td class="cellrowborder" valign="top" width="50%">callScript</td><td class="cellrowborder" valign="top" width="50%">sub/script01.xml</td></tr></tbody></table>

**Parent topic:** [[Invoke subscript|Invoke subscript]]