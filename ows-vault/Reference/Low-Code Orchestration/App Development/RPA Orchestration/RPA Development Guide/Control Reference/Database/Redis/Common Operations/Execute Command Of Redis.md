---
title: "Execute Command Of Redis"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560747.html"
depth: 8
---
# Execute Command Of Redis

**redis.executeCommand**

**Description:**

Execute the redis client command, please refer to the redis command manual: https://www.redis.net.cn/order/

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560747__table143235mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560747__row143241mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143251mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">RedisConnect</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Database connection session</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560747__table143261mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560747__row143270mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143289mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">redis-command</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Redis client command. Example setting string: SET name Tom NX</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143303mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143317mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560747__table143333mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560747__row143341mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143357mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">Object</td><td class="cellrowborder" valign="top" width="20%">result_command</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Return of Executing Redis Command.Different redis commands return different types of values.</td></tr></tbody></table>

**Samples**

Execute the command: GET name, get the value of the key name

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560747__table143372mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560747__row143377mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143384mcpsimp"><td class="cellrowborder" valign="top" width="50%">redis-command</td><td class="cellrowborder" valign="top" width="50%">GET name</td></tr></tbody></table>

Execute the command: SET words "I'm a Chinese people" EX 60, set the value of words to "I'm a Chinese people", and the expiration time is 60 seconds

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560747__table143391mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560747__row143396mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143403mcpsimp"><td class="cellrowborder" valign="top" width="50%">redis-command</td><td class="cellrowborder" valign="top" width="50%">SET words "I'm a Chinese people" EX 60</td></tr></tbody></table>

Execute the command: SET age 20 XX, set its value to 20 when age exists

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560747__table143410mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560747__row143415mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143422mcpsimp"><td class="cellrowborder" valign="top" width="50%">redis-command</td><td class="cellrowborder" valign="top" width="50%">SET age 20 XX</td></tr></tbody></table>

Execute the command: DEL name age score, delete the key name, age, score

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560747__table143429mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560747__row143434mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143441mcpsimp"><td class="cellrowborder" valign="top" width="50%">redis-command</td><td class="cellrowborder" valign="top" width="50%">DEL name age score</td></tr></tbody></table>

Execute the command: LPUSH db redis mysql mongodb, insert redis, mysql, mongodb into the head of the db list

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560747__table143448mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560747__row143453mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143460mcpsimp"><td class="cellrowborder" valign="top" width="50%">redis-command</td><td class="cellrowborder" valign="top" width="50%">LPUSH db redis mysql mongodb</td></tr></tbody></table>

Execute the command: LLEN list, get the length of the list list

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560747__table143467mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560747__row143472mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560747__row143479mcpsimp"><td class="cellrowborder" valign="top" width="50%">redis-command</td><td class="cellrowborder" valign="top" width="50%">LLEN list</td></tr></tbody></table>

**Parent topic:** [[Common Operations|Common Operations]]