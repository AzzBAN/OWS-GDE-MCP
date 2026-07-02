---
title: "Make a PDF with an image"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480593.html"
depth: 7
---
# Make a PDF with an image

**imageToPdf**

**Description:**

Make a PDF document with an image.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480593__table75615mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480593__row75624mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552480593__row75643mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">image_dir</td><td class="cellrowborder" valign="top" width="16.666666666666664%">dir</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Path for storing images to be converted to PDF files, images that can be converted to PDF files include .png, .jpg, .jpeg, .tif, .tiff, .bmp, and .gif;Note: Only images can be stored in the path specified by this parameter.</td></tr><tr id="EN-US_TOPIC_0000002552480593__row75657mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">output-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">dir</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Path for storing PDF files converted from images.</td></tr><tr id="EN-US_TOPIC_0000002552480593__row75671mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">output-name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">PdfFile.pdf</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Indicates the name of the PDF file after the image is converted. The file name must end with .pdf.</td></tr><tr id="EN-US_TOPIC_0000002552480593__row75685mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552480593__row75699mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Run the following commands to convert the images in D:\\AntRobot\\image to a .pdf file and save the files in D:\\xx\\xx\\test\_pdf\_case:

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480593__table75718mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480593__row75723mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480593__row75730mcpsimp"><td class="cellrowborder" valign="top" width="50%">image_dir</td><td class="cellrowborder" valign="top" width="50%">D:\AntRobot\image</td></tr><tr id="EN-US_TOPIC_0000002552480593__row75736mcpsimp"><td class="cellrowborder" valign="top" width="50%">output-path</td><td class="cellrowborder" valign="top" width="50%">D:\xx\xx\test_pdf_case</td></tr><tr id="EN-US_TOPIC_0000002552480593__row75742mcpsimp"><td class="cellrowborder" valign="top" width="50%">output-name</td><td class="cellrowborder" valign="top" width="50%">image.pdf</td></tr></tbody></table>

The usage example is as follows:

![[en-us_image_0000002552560927.png]]

**Parent topic:** [[File|File]]