---
title: "Download File"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560627.html"
depth: 7
---
# Download File

**sftp.download**

**Description:**

Download file or folder from remote server.

1.Action supports downloading file or folder.

2.Action doesn't support file overwriting, target with the same name should not exist in local target directory.

3.Action must used together with sftp.connect and it executed after sftp.connect.

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560627__table118830mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560627__row118836mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560627__row118846mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">FtpObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Server connection session</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560627__table118856mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560627__row118865mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560627__row118884mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">local-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">dir</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Local save path for downloaded target</td></tr><tr id="EN-US_TOPIC_0000002552560627__row118898mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">remote-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Remote target path to be downloaded, Cannot be the root directory(/).</td></tr><tr id="EN-US_TOPIC_0000002552560627__row118912mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">overwrite</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True|False</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Whether to cover. Whether to overwrite a path with the same name when it exists locally. True means overwriting, and the local path will be deleted and then downloaded again; False means not overwriting, cancel download (no error will be reported).</td></tr><tr id="EN-US_TOPIC_0000002552560627__row118926mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552560627__row118940mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Download the test\_doc.docx file in /root/output/ dir on the remote server to the download folder in the project directory.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560627__table118959mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560627__row118964mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560627__row118971mcpsimp"><td class="cellrowborder" valign="top" width="50%">local-path</td><td class="cellrowborder" valign="top" width="50%">@{WORK_DIR}\download</td></tr><tr id="EN-US_TOPIC_0000002552560627__row118977mcpsimp"><td class="cellrowborder" valign="top" width="50%">remote-path</td><td class="cellrowborder" valign="top" width="50%">/root/output/test_doc.docx</td></tr></tbody></table>

Download the /root/output/ folder on the remote server to the download folder in the project directory.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560627__table118984mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560627__row118989mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560627__row118996mcpsimp"><td class="cellrowborder" valign="top" width="50%">local-path</td><td class="cellrowborder" valign="top" width="50%">@{WORK_DIR}\download</td></tr><tr id="EN-US_TOPIC_0000002552560627__row119002mcpsimp"><td class="cellrowborder" valign="top" width="50%">remote-path</td><td class="cellrowborder" valign="top" width="50%">/root/output</td></tr></tbody></table>

The usage example is as follows:

![[en-us_image_0000002521400958.png]]

**Parent topic:** [[Sftp|Sftp]]