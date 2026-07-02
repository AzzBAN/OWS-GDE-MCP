---
title: "Create Redfish Session"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400648.html"
depth: 7
---
# Create Redfish Session

**ibmc\_login**

**Description:**

Create Redfish Session.

Using this command requires users to install the redfish plugin

Installation steps:

1\. Click Advanced -> Project Configuration -> Python Module Management in the top menu of the studio design interface;

2\. In the opened Python Module Management page Install new module redfish

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400648__table11668mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400648__row11677mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400648__row11696mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">ibmc_ip</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Server BMC IP address</td></tr><tr id="EN-US_TOPIC_0000002521400648__row11710mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">username</td><td class="cellrowborder" valign="top" width="16.666666666666664%">String</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">UserName</td></tr><tr id="EN-US_TOPIC_0000002521400648__row11724mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">password</td><td class="cellrowborder" valign="top" width="16.666666666666664%">password</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Password</td></tr><tr id="EN-US_TOPIC_0000002521400648__row11738mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521400648__row11752mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400648__table11768mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400648__row11776mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521400648__row11792mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">IbmcObject</td><td class="cellrowborder" valign="top" width="20%">redfish_session</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">IBMC login session</td></tr></tbody></table>

**Samples**

Log in to the server with IP address xxx.xx.xx.xx, user name: root, password: xxxxx

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400648__table11807mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400648__row11812mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400648__row11819mcpsimp"><td class="cellrowborder" valign="top" width="50%">ibmc_ip</td><td class="cellrowborder" valign="top" width="50%">xxx.xx.xx.xx</td></tr><tr id="EN-US_TOPIC_0000002521400648__row11825mcpsimp"><td class="cellrowborder" valign="top" width="50%">username</td><td class="cellrowborder" valign="top" width="50%">root</td></tr><tr id="EN-US_TOPIC_0000002521400648__row11831mcpsimp"><td class="cellrowborder" valign="top" width="50%">password</td><td class="cellrowborder" valign="top" width="50%">xxxxx</td></tr></tbody></table>

**Parent topic:** [[Redfish Operation|Redfish Operation]]