---
title: "Merge PDF"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480585.html"
depth: 7
---
# Merge PDF

**mergePdf**

**Description:**

Merge PDF; To use this command, you need to install the pikepdf third-party software.

Installation procedure:

1\. Go to the Python directory from the Studio installation directory.

2\. On the road Enter cmd and press Enter.

3\. In the CLI, run the Python.exe -m pip install pikepdf command to install the software.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480585__table136471mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480585__row136480mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552480585__row136499mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">pdf_file_list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">List of absolute paths to PDF files to be combined. Separate multiple paths with a single quotation mark ';' separate.</td></tr><tr id="EN-US_TOPIC_0000002552480585__row136513mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">output-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">dir</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Path for storing the PDF files generated after the combination.</td></tr><tr id="EN-US_TOPIC_0000002552480585__row136527mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">output-name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">PdfFile.pdf</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Indicates the name of the file generated after PDF combination. The file name must end with pdf.</td></tr><tr id="EN-US_TOPIC_0000002552480585__row136541mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552480585__row136555mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Combine the PDF files D:\\AntRobot\\test1.pdf and D:\\AntRobot\\test2.pdf to generate a new file merge.pdf.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480585__table136574mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480585__row136579mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480585__row136586mcpsimp"><td class="cellrowborder" valign="top" width="50%">pdf_file_list</td><td class="cellrowborder" valign="top" width="50%">D:\AntRobot\test1.pdf;D:\AntRobot\test2.pdf</td></tr><tr id="EN-US_TOPIC_0000002552480585__row136592mcpsimp"><td class="cellrowborder" valign="top" width="50%">output-path</td><td class="cellrowborder" valign="top" width="50%">D:\project\pdf_case\test_pdf_case\Output</td></tr><tr id="EN-US_TOPIC_0000002552480585__row136598mcpsimp"><td class="cellrowborder" valign="top" width="50%">output-name</td><td class="cellrowborder" valign="top" width="50%">merge.pdf</td></tr></tbody></table>

The usage example is as follows:

![[en-us_image_0000002552560919.png]]

**Parent topic:** [[File|File]]