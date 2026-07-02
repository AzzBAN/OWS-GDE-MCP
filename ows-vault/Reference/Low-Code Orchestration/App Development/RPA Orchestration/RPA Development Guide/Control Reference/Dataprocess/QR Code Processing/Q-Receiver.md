---
title: "Q-Receiver"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560711.html"
depth: 7
---
# Q-Receiver

**receiveQrData**

**Description:**

Receives data in the QR code transmission scheme:

1\. This command is used only in specific scenarios. The sendQrData command is used at the other end of the transmission. Used to transfer files or data volume when a single QR code cannot be transferred.

2\. This command involves camera shooting. The camera image is not displayed. Align the camera with the receiver screen to adjust the camera.

Input parameters:

1\. index: int type, mandatory, camera ID (0 indicates the built-in camera, 1, 2, ...)

2\. file\_name: string type, optional, new file name (new by default) when the received file is a file).

3\. img\_size: int type, image size for display, the length and width are consistent. If the value is greater than the resolution of the local computer, the screen is adaptive.

4\. position: position of the image to be displayed. The value type is list. The default value is middle.

Output parameter:

receive\_qrdata\_ret: indicates the received data or file. (If the received data is a file, the return value is the file storage path. If the received data is data, the return value is the received data.)

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560711__table113462mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560711__row113471mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113490mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">index</td><td class="cellrowborder" valign="top" width="16.666666666666664%">int</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Camera number (0 means built-in camera, 1,2...... means USB external camera)</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113504mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">file_name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">new</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">New file name (new by default) when the received file is a file.</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113518mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">img_size</td><td class="cellrowborder" valign="top" width="16.666666666666664%">int</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">300</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The size of the picture when displayed, the length and width are the same;If the set value is greater than the local computer resolution, it will adapt to the screen</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113532mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">position</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">center</td><td class="cellrowborder" valign="top" width="16.666666666666664%">upper left|lower left|upper right|lower right|center</td><td class="cellrowborder" valign="top" width="16.666666666666664%">display pictures: upper left|lower left|upper right|lower right|center</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113546mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113560mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560711__table113576mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560711__row113584mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113600mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">String</td><td class="cellrowborder" valign="top" width="20%">receive_qrdata_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Received data or file (If the received data is a file, the returned value is the file storage path. If the received data is data, the returned value is the received data.)</td></tr></tbody></table>

**Samples**

Receive data in the QR code transmission scheme

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560711__table113615mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560711__row113620mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113627mcpsimp"><td class="cellrowborder" valign="top" width="50%">index</td><td class="cellrowborder" valign="top" width="50%">0</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113633mcpsimp"><td class="cellrowborder" valign="top" width="50%">image_size</td><td class="cellrowborder" valign="top" width="50%">300</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113639mcpsimp"><td class="cellrowborder" valign="top" width="50%">position</td><td class="cellrowborder" valign="top" width="50%">center</td></tr><tr id="EN-US_TOPIC_0000002552560711__row113645mcpsimp"><td class="cellrowborder" valign="top" width="50%">file_name</td><td class="cellrowborder" valign="top" width="50%">new</td></tr></tbody></table>

**Parent topic:** [[QR Code Processing|QR Code Processing]]