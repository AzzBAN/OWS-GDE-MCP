---
title: "Invoke C#"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400670.html"
depth: 7
---
# Invoke C#

**exec.Csharp**

**Description:**

C# function invoking:

input:

function: sting type, mandatory,Space name.Class name.Method name in c#, which are separated

file-name: file type,mandatory, c# dll name, It is placed under Robot/cfg/plugin/,which does not need to be suffixed with .dll. or the absolute path of the dll file to be executed

class-args: string type,optionalParameter of class in c#. Separate multiple parameters with commas (,)

function-args: string type, optional, C # method parameters, separated by semicolons multiple parameters. Supported Python data types include: int/float /bool/str/list/tuple/ dict/set. When the parameter is str type, you must add double quotes. When the parameter is all types except str(including the form of introducing variables), you do not need to add double quotes. When the parameter is a path string, in order to prevent it from being escaped, please prefix it with r, such as r "path".

output:

execCsharp\_ret: Call c # function to return the result

need to install .NET Framework 4.0 or higher.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400670__table70266mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400670__row70275mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70294mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">function</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Space name.Class name.Method name in c#, which are separated by a dot (.).</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70308mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">file-name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">c# dll name, It is placed under Robot/cfg/plugin/,which does not need to be suffixed with .dll or the absolute path of the dll file to be executed</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70322mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">class-args</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Parameter of class in c#. Separate multiple parameters with commas (,).</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70336mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">function-args</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">'C # method parameters, separated by semicolons multiple parameters. Supported Python data types include: int/float /bool/str/list/tuple/ dict/set. When the parameter is str type, you must add double quotes. When the parameter is all types except str(including the form of introducing variables), you do not need to add double quotes. When the parameter is a path string, in order to prevent it from being escaped, please prefix it with r, such as r "path".'</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70350mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70364mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400670__table70380mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400670__row70388mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70404mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">Object</td><td class="cellrowborder" valign="top" width="20%">execCsharp_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Call c # function to return the result</td></tr></tbody></table>

**Samples**

Call the C# function of the calculate.dll file under Robot/cfg/plugin;

Method name: ConsoleApp3.calculate.Sub;

class parameters: para1, para2

Method parameters: @{a};111

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400670__table70422mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400670__row70427mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70434mcpsimp"><td class="cellrowborder" valign="top" width="50%">file-name</td><td class="cellrowborder" valign="top" width="50%">calculate</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70440mcpsimp"><td class="cellrowborder" valign="top" width="50%">class-args</td><td class="cellrowborder" valign="top" width="50%">para1,para2</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70446mcpsimp"><td class="cellrowborder" valign="top" width="50%">function</td><td class="cellrowborder" valign="top" width="50%">ConsoleApp3.calculate.Sub</td></tr><tr id="EN-US_TOPIC_0000002521400670__row70452mcpsimp"><td class="cellrowborder" valign="top" width="50%">function-args</td><td class="cellrowborder" valign="top" width="50%">@{a};111</td></tr></tbody></table>

**Parent topic:** [[Invoke|Invoke]]