---
title: "Offline OCR Auto Form"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560612.html"
depth: 8
---
# Offline OCR Auto Form

**OfflineOcrAutoForm**

**Description:**

Offline OCR Auto Form

\[Paddle\]

For details about the environment configuration, see https://bbs.huaweicloud.com/forum/thread-194071-1-1.html

\[Tesseract\]

Firstly, before configuring the OCR engine, perform the following steps:

1\. Download the Tesseract-OCR installation package from https://digi.bib.uni-mannheim.de/tesseract/?C=M;O=D, which is similar to tesseract-ocr-w64-setup-v5.1.0.20220510.exe.

2\. Set environment variables for the installation directory. For example, add D:/Tesseract-OCR to Path.

3\. Set the system variable name TESSDATA\_PREFIX and the variable value to D:/Tesseract-OCR/tessdata.

4\. By default, only the English package is available. Therefore, download the required language package to the directory in step 3. The language package download address is https://github.com/tesseract-ocr/tessdata. For example, chi\_sim.traineddata is the Chinese language package.

5\. If "no module named'pytesseract" is displayed, go to the python folder in the studio installation directory, open the cmd command line black window, and enter python -m pip install pytesseract.

Secondly, for details about how to train the OCR recognition model, visit https://bbs.huaweicloud.com/forum/thread-191969-1-1.html.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560612__table101072mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560612__row101081mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101100mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">ocr-engine</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Paddle</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Paddle|Tesseract</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Offline OCR engine</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101114mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">control</td><td class="cellrowborder" valign="top" width="16.666666666666664%">json</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Control Information</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101128mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">language-type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">ch</td><td class="cellrowborder" valign="top" width="16.666666666666664%">ch|chinese_cht|en|korean|japan|ta|te|ka|latin|arabic|cyrillic|devanagari</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Simplified Chinese, English, and digits are recognized by default.</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101142mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">form-content</td><td class="cellrowborder" valign="top" width="16.666666666666664%">autoForm</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">content to type into the form</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101156mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101170mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Use the Paddle engine to log in to Onebox based on the form input information.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560612__table101189mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560612__row101194mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101201mcpsimp"><td class="cellrowborder" valign="top" width="50%">ocr-engine</td><td class="cellrowborder" valign="top" width="50%">Paddle</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101207mcpsimp"><td class="cellrowborder" valign="top" width="50%">control</td><td class="cellrowborder" valign="top" width="50%">{"driver_type": "uiautomation","appName": "Onebox Mate.exe","title": "Onebox Mate","offset-x": "638","offset-y": "510","target": [{"ClassName": "OneboxUIFrame","x": "5","width": "1100","y": "3","ControlType": "WindowControl","Name": "Onebox Mate","height": "650"}]}</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101213mcpsimp"><td class="cellrowborder" valign="top" width="50%">language-type</td><td class="cellrowborder" valign="top" width="50%">ch</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101219mcpsimp"><td class="cellrowborder" valign="top" width="50%">form-content</td><td class="cellrowborder" valign="top" width="50%">[{"name":"Account/ID","find-text-rule":"contain","optype":"input","value":"xxxx","offset-x":"0","offset-y":0},{"name":"Password","find-text-rule":"contain","optype":"input","value":"xxx","offset-x":"0","offset-y":0},{"name":"Login","find-text-rule":"equals","optype":"click","value":"","offset-x":"","offset-y":0}]</td></tr><tr id="EN-US_TOPIC_0000002521560612__row101225mcpsimp"><td class="cellrowborder" valign="top" width="50%">return</td><td class="cellrowborder" valign="top" width="50%">offlineocrwindow_ret</td></tr></tbody></table>

Operation on the form items as shown below:

![[en-us_image_0000002521400936.png]]

**Parent topic:** [[Automation based on offline OCR|Automation based on offline OCR]]