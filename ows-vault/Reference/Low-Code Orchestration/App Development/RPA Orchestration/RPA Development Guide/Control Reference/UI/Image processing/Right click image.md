---
title: "Right click image"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560915.html"
depth: 7
---
# Right click image

**citrix.rclickPicScreen**

**Description:**

Right click the image

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560915__table95046mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560915__row95055mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560915__row95074mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">image</td><td class="cellrowborder" valign="top" width="16.666666666666664%">file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The path is the image name.(The format of the image path is ***.png, which must end with .png|.jpg)</td></tr><tr id="EN-US_TOPIC_0000002552560915__row95088mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">offset-x</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">x axis offset</td></tr><tr id="EN-US_TOPIC_0000002552560915__row95102mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">offset-y</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">y axis offset</td></tr><tr id="EN-US_TOPIC_0000002552560915__row95116mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552560915__row95130mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Right-click the wei.png image, and click the coordinates of the upper left corner of the image (20,20)

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560915__table95149mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560915__row95154mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560915__row95161mcpsimp"><td class="cellrowborder" valign="top" width="50%">image</td><td class="cellrowborder" valign="top" width="50%">wei.png</td></tr><tr id="EN-US_TOPIC_0000002552560915__row95167mcpsimp"><td class="cellrowborder" valign="top" width="50%">offset-x</td><td class="cellrowborder" valign="top" width="50%">20</td></tr><tr id="EN-US_TOPIC_0000002552560915__row95173mcpsimp"><td class="cellrowborder" valign="top" width="50%">offset-y</td><td class="cellrowborder" valign="top" width="50%">20</td></tr></tbody></table>

**Parent topic:** [[Image processing|Image processing]]