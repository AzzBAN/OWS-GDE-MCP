---
title: "Insert into Mongodb"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400758.html"
depth: 8
---
# Insert into Mongodb

**mongodb.insert**

**Description:**

Insert data into mongodb database.The current instruction will add data to the production environment, please use it with caution.

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400758__table97636mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400758__row97642mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521400758__row97652mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">DBObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Database connection session</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400758__table97662mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400758__row97671mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400758__row97690mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">collection</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Select the database collection to operate</td></tr><tr id="EN-US_TOPIC_0000002521400758__row97704mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">document</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Data to insert in json format</td></tr><tr id="EN-US_TOPIC_0000002521400758__row97718mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521400758__row97732mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Insert a piece of data into the score collection of the database {"id":1, "name":"xiaoyun"}

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400758__table97751mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400758__row97756mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400758__row97763mcpsimp"><td class="cellrowborder" valign="top" width="50%">collection</td><td class="cellrowborder" valign="top" width="50%">score</td></tr><tr id="EN-US_TOPIC_0000002521400758__row97769mcpsimp"><td class="cellrowborder" valign="top" width="50%">document</td><td class="cellrowborder" valign="top" width="50%">{"id":1, "name":"xiaoyun"}</td></tr></tbody></table>

Insert 2 pieces of data into the score collection of the database \[{"id":2, "name":"xiaoyun"},{"id":3, "name":"xiaohua"}\]

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400758__table97776mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400758__row97781mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400758__row97788mcpsimp"><td class="cellrowborder" valign="top" width="50%">collection</td><td class="cellrowborder" valign="top" width="50%">score</td></tr><tr id="EN-US_TOPIC_0000002521400758__row97794mcpsimp"><td class="cellrowborder" valign="top" width="50%">document</td><td class="cellrowborder" valign="top" width="50%">[{"id":2, "name":"xiaoyun"},{"id":3, "name":"xiaohua"}]</td></tr></tbody></table>

**Parent topic:** [[NoSQL|NoSQL]]