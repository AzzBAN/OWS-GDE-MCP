---
title: "Get Runtime Info"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560778.html"
depth: 7
---
# Get Runtime Info

**getRuntimeInfo**

**Description:**

Get Runtime Info,Including project name (projectName), project version (projectVersion), project start time(startTime), job name(jobName), task tag(taskTag), job mode(jobMode), queue name(queueName), agent name(agentName) , cluster name(clusterName) and agent type(agentType);

1\. When the designer is executed, the return value includes the project name, project version, project startup time, agent name and agent type; the executor name here is the name in the designer management center when it is online, and the name of the designer in the management center when it was online last time when it is offline;

2\. When the executor executes, the return value adds the job name, task tag, and job mode;

3\. The queue name is added to the return value when the management center schedules the queue to start, and the cluster name is added to the return value when the cluster task is started.

Part of the field return value enumeration value:

The trigger mode return value includes once (single), repeat (repeat), cron (timing), agentTrigger (client trigger), queueTrigger (queue trigger) and manualTriger (manual trigger);

Executor types include Executor (executor) and Studio (designer).

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560778__table74660mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560778__row74669mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560778__row74688mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">info</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">all</td><td class="cellrowborder" valign="top" width="16.666666666666664%">all|projectName|projectVersion|startTime|jobName|taskTag|jobMode|queueName|agentName|clusterName|agentType</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The running information that needs to be obtained</td></tr><tr id="EN-US_TOPIC_0000002521560778__row74702mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560778__row74716mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560778__table74732mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560778__row74740mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521560778__row74756mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">Object</td><td class="cellrowborder" valign="top" width="20%">get_runtime_info_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Obtained running information, see the help information of the control for detailed key values.</td></tr></tbody></table>

**Samples**

Querying the Version Information of the Current Task

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560778__table74771mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560778__row74776mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560778__row74783mcpsimp"><td class="cellrowborder" valign="top" width="50%">info</td><td class="cellrowborder" valign="top" width="50%">projectVersion</td></tr></tbody></table>

Return value example {'projectVersion': '1.0.2'}

Queries all information about the current task.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560778__table74791mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560778__row74796mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560778__row74803mcpsimp"><td class="cellrowborder" valign="top" width="50%">info</td><td class="cellrowborder" valign="top" width="50%">all</td></tr></tbody></table>

Return value example {'projectName': 'aaa-132295', 'projectVersion': '1.0.3', 'startTime': '2023-02-13 17:04:00', 'jobName': 'aaa', 'taskTag': 'aaa\_1676278731515', 'jobMode': 'once', 'agentName': 'lxs', 'agentType': 'executor'}

**Parent topic:** [[Basic Functions|Basic Functions]]