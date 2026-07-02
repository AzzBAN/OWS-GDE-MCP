---
title: "Take Photo"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560734.html"
depth: 7
---
# Take Photo

**takepicture**

**Description:**

Taken by camera:

1\. The camera control saves the current content of the camera as a local image,Ensure privacy and information security by yourself.

Input parameters:

1\. index, int type, optional, and camera ID (0 indicates the built-in camera; 1, 2, ... indicates the external camera through the USB port). The default value is 0.

2\. save-to or new\_file type. This parameter is optional. If the image path and image name are customized, the path must exist. By default, images are stored in the Pic folder in the project directory. Currently, only images in .jpg and .png formats can be saved.

Output parameter:

picture\_ret: path for storing images.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560734__table120401mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560734__row120410mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560734__row120429mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">index</td><td class="cellrowborder" valign="top" width="16.666666666666664%">int</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Camera number (0 means built-in camera, 1,2...... means USB external camera)</td></tr><tr id="EN-US_TOPIC_0000002521560734__row120443mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">save-to</td><td class="cellrowborder" valign="top" width="16.666666666666664%">new_file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">jpg|png</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Optional. If you customize the storage path and name of the picture, the path directory must already exist; the default path of the picture is in the Pic folder of the project directory.</td></tr><tr id="EN-US_TOPIC_0000002521560734__row120457mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560734__row120471mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560734__table120487mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560734__row120495mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521560734__row120511mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">String</td><td class="cellrowborder" valign="top" width="20%">picture_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">The path of the picture</td></tr></tbody></table>

**Samples**

Take a photo with the camera and save it

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560734__table120526mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560734__row120531mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560734__row120538mcpsimp"><td class="cellrowborder" valign="top" width="50%">index</td><td class="cellrowborder" valign="top" width="50%">0</td></tr><tr id="EN-US_TOPIC_0000002521560734__row120544mcpsimp"><td class="cellrowborder" valign="top" width="50%">save-to</td><td class="cellrowborder" valign="top" width="50%">@{WORK_DIR}\Pic</td></tr></tbody></table>

**Parent topic:** [[QR Code Processing|QR Code Processing]]