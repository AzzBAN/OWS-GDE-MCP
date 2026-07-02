---
title: "Download Shared File"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400784.html"
depth: 7
---
# Download Shared File

**mc.downloadFile**

**Description:**

Download file from shared files in the management center.Downloading all files or one file in a folder on the cloud

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400784__table30778mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400784__row30787mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400784__row30806mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">file-name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">One file name(required file type). If this parameter is not specified, all files in the cloud folder will be downloaded.</td></tr><tr id="EN-US_TOPIC_0000002521400784__row30820mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">folder</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Directory for storing uploaded files in the management center</td></tr><tr id="EN-US_TOPIC_0000002521400784__row30834mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">save-to</td><td class="cellrowborder" valign="top" width="16.666666666666664%">dir</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">File save path. Ensure that the local disk space is sufficient.</td></tr><tr id="EN-US_TOPIC_0000002521400784__row30848mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521400784__row30862mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Download file

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400784__table30881mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400784__row30886mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400784__row30893mcpsimp"><td class="cellrowborder" valign="top" width="50%">file-name</td><td class="cellrowborder" valign="top" width="50%">test</td></tr><tr id="EN-US_TOPIC_0000002521400784__row30899mcpsimp"><td class="cellrowborder" valign="top" width="50%">folder</td><td class="cellrowborder" valign="top" width="50%">test</td></tr><tr id="EN-US_TOPIC_0000002521400784__row30905mcpsimp"><td class="cellrowborder" valign="top" width="50%">save-to</td><td class="cellrowborder" valign="top" width="50%">D:\eSpace_transfer_files\test</td></tr></tbody></table>

**Parent topic:** [[File Share|File Share]]