---
title: "Convert PDF to Image"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560634.html"
depth: 7
---
# Convert PDF to Image

**pdfToImage**

**Description:**

Convert PDF to image;

There are two ways to use this command (we recommend the first method because the first method covers more scenarios than the second method):

Method 1: Configure the third-party software according to the RPA forum, forum address: https://bbs.huaweicloud.com/forum/thread-186377-1-1.html;

Method 2: Install PyMupdf>=1.18.14 version tripartite;

installation steps:

1\. Enter the Python directory under the studio installation directory;

3\. Windows system enter the command in the cmd window: Python.exe -m pip install pymupdf to install; Linux system enter the command in the terminal: ./python3 -m pip install pymupdf

Method 2: Download the conversion tool poppler;

installation steps:

1\. Download link http://blog.alivate.com.au/poppler-windows/,

2\. After downloading, unzip the serial bin/folder and add it to the environment variable;

3\. Restart the computer.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560634__table90783mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560634__row90792mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90811mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">pdf-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">pdf</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Absolute path of the pdf file to be parsed</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90825mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">output-path</td><td class="cellrowborder" valign="top" width="16.666666666666664%">dir</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Path for storing converted PDF images.</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90839mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">output-name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">image.png</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Name of the image converted from the PDF file,The file name used must end with a valid image extension. The supported file names include .png, .jpg, .jpeg, .tif, .tiff, .bmp, and .gif.</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90853mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">filter-page</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">1-2</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Specifies the number of pages to be converted to images. You can specify a page or a range of pages to be converted to images. If you want to convert all PDF pages to images, enter all. (Note: If the file size is too large, system freezing may occur.) e.g.:1-2 Note: The number of pages can only be a positive integer, and the start page cannot be greater than the end page when specifying the range of pages</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90868mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90882mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560634__table90898mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560634__row90906mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90922mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">Array</td><td class="cellrowborder" valign="top" width="20%">pdfToImage_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">Path Array of images generated by running the control</td></tr></tbody></table>

**Samples**

Change pages 1 to 2 in the D:\\AntRobot\\test.pdf file to images.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560634__table90937mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560634__row90942mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90949mcpsimp"><td class="cellrowborder" valign="top" width="50%">pdf-path</td><td class="cellrowborder" valign="top" width="50%">D:\AntRobot\test.pdf</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90955mcpsimp"><td class="cellrowborder" valign="top" width="50%">output-path</td><td class="cellrowborder" valign="top" width="50%">D:\AntRobot\test</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90961mcpsimp"><td class="cellrowborder" valign="top" width="50%">output-name</td><td class="cellrowborder" valign="top" width="50%">test.png</td></tr><tr id="EN-US_TOPIC_0000002521560634__row90967mcpsimp"><td class="cellrowborder" valign="top" width="50%">filter-page</td><td class="cellrowborder" valign="top" width="50%">1-2</td></tr></tbody></table>

The usage example is as follows:

![[en-us_image_0000002552480911.png]]

**Parent topic:** [[File|File]]