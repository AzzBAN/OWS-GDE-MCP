---
title: "Upload File"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400644.html"
depth: 7
---
# Upload File

**sftp.upload**

**Description:**

Upload file or folder to the remote server.

1.Action supports uploading file or folder.

2.Action support file overwriting, overwrite target with the same name exist in the remote target directory by default.

3.Action must used together with sftp.connect and it executed after sftp.connect.

4.Action execute succeed requires the server to open relevant permissions.

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400644__table17431mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400644__row17437mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17447mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">FtpObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Server connection session</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400644__table17457mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400644__row17466mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17485mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">local-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Local target path to be uploaded</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17499mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">remote-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Remote save path for uploaded target, cannot be "\"</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17513mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">overwrite</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True|False</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Whether to cover. Whether to overwrite a path with the same name on the remote end. True means overwriting, and the remote path will be deleted and uploaded again; False means not overwriting, cancel upload (no error will be reported).</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17527mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17541mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Upload the test\_doc.docx file in the upload folder in the project directory to the /root/recv/ directory on the remote server.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400644__table17560mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400644__row17565mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17572mcpsimp"><td class="cellrowborder" valign="top" width="50%">local-path</td><td class="cellrowborder" valign="top" width="50%">@{WORK_DIR}\upload\test_doc.docx</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17578mcpsimp"><td class="cellrowborder" valign="top" width="50%">remote-path</td><td class="cellrowborder" valign="top" width="50%">/root/recv</td></tr></tbody></table>

Upload the upload file in the project directory to the /root/recv/ directory on the remote server.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400644__table17585mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400644__row17590mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17597mcpsimp"><td class="cellrowborder" valign="top" width="50%">local-path</td><td class="cellrowborder" valign="top" width="50%">@{WORK_DIR}\upload</td></tr><tr id="EN-US_TOPIC_0000002521400644__row17603mcpsimp"><td class="cellrowborder" valign="top" width="50%">remote-path</td><td class="cellrowborder" valign="top" width="50%">/root/recv</td></tr></tbody></table>

The usage example is as follows:

![[en-us_image_0000002521560964.png]]

**Parent topic:** [[Sftp|Sftp]]