---
title: "Split PDF"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400620.html"
depth: 7
---
# Split PDF

**splitPdf**

**Description:**

Split PDF; To use this command, you need to install the third-party pikepdf component.

Installation procedure:

1\. Go to the Python directory from the Studio installation directory.

2\. Enter cmd in the path bar and press Enter.

3\. Enter the following command in the cmd window:Python.exe -m pip install pikepdf.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400620__table111801mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400620__row111810mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111829mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">pdf-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">pdf</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Absolute path of the pdf file to be parsed</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111843mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">output-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">dir</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Path for storing the split PDF file.</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111857mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">output-name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">PdfFile.pdf</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specifies the name of the split PDF file. The file name must end with pdf.</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111871mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">split-page</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">1-2</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specifies the number of pages to be split into PDF files. You can specify a single page, start page, and end page. eg:1-2 Note:The number of pages must be a positive integer. The start page cannot be greater than the end page when the page number range is specified.</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111886mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111900mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Split pages 2 to 4 in the D:\\AntRobot\\test.pdf file to form a pdf file.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400620__table111919mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400620__row111924mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111931mcpsimp"><td class="cellrowborder" valign="top" width="50%">pdf-path</td><td class="cellrowborder" valign="top" width="50%">D:\AntRobot\test.pdf</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111937mcpsimp"><td class="cellrowborder" valign="top" width="50%">output-path</td><td class="cellrowborder" valign="top" width="50%">D:\AntRobot\output</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111943mcpsimp"><td class="cellrowborder" valign="top" width="50%">output-name</td><td class="cellrowborder" valign="top" width="50%">split.pdf</td></tr><tr id="EN-US_TOPIC_0000002521400620__row111949mcpsimp"><td class="cellrowborder" valign="top" width="50%">split-page</td><td class="cellrowborder" valign="top" width="50%">2-4</td></tr></tbody></table>

The usage example is as follows:

![[en-us_image_0000002521560944.png]]

**Parent topic:** [[File|File]]