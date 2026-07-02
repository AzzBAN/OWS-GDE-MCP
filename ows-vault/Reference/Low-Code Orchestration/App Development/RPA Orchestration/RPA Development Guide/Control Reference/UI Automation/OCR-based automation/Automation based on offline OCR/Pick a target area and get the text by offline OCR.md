---
title: "Pick a target area and get the text by offline OCR"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560614.html"
depth: 8
---
# Pick a target area and get the text by offline OCR

**offlineGetOcrText**

**Description:**

Pick a target area and get the text by OCR.

\[Paddle\]

For details about the environment configuration, see https://bbs.huaweicloud.com/forum/thread-194071-1-1.html

Decompress the downloaded model file (e.g. ch\_PP-OCRv3\_det\_infer) and place it in public/paddleOcrModel in the Studio or Assistant installation directory.

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

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560614__table56503mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560614__row56512mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56531mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">ocr-engine</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Paddle</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Paddle|Tesseract</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Offline OCR engine</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56545mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">window-type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">control</td><td class="cellrowborder" valign="top" width="16.666666666666664%">control|image</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Window type</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56559mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">control</td><td class="cellrowborder" valign="top" width="16.666666666666664%">json</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Control Information</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56573mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">image</td><td class="cellrowborder" valign="top" width="16.666666666666664%">file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">File absolute path or file name (when filling in the file name, the picture must be in the Pic folder of the project directory. The picture format must be png|jpg)</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56587mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">language-type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">ch</td><td class="cellrowborder" valign="top" width="16.666666666666664%">ch|chinese_cht|en|korean|japan|ta|te|ka|latin|arabic|cyrillic|devanagari</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Simplified Chinese, English, and digits are recognized by default.</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56601mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56615mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560614__table56631mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560614__row56639mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56655mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">Array</td><td class="cellrowborder" valign="top" width="20%">offlinegetocrtext_ret</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">offline ocr model object</td></tr></tbody></table>

**Samples**

Use the Tesseract engine to obtain the text in the Onebox window and save it to offlinegetocrtext\_ret

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560614__table56670mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560614__row56675mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56682mcpsimp"><td class="cellrowborder" valign="top" width="50%">ocr-engine</td><td class="cellrowborder" valign="top" width="50%">Tesseract</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56688mcpsimp"><td class="cellrowborder" valign="top" width="50%">control</td><td class="cellrowborder" valign="top" width="50%">{"driver_type": "uiautomation","appName": "Onebox Mate.exe","title": "Onebox Mate","offset-x": "638","offset-y": "510","target": [{"ClassName": "OneboxUIFrame","x": "5","width": "1100","y": "3","ControlType": "WindowControl","Name": "Onebox Mate","height": "650"}]}</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56694mcpsimp"><td class="cellrowborder" valign="top" width="50%">language-type</td><td class="cellrowborder" valign="top" width="50%">chi_sim+eng</td></tr></tbody></table>

Use the Paddle engine to obtain the text in image 1.png.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560614__table56701mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560614__row56706mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56713mcpsimp"><td class="cellrowborder" valign="top" width="50%">ocr-engine</td><td class="cellrowborder" valign="top" width="50%">Paddle</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56719mcpsimp"><td class="cellrowborder" valign="top" width="50%">language-type</td><td class="cellrowborder" valign="top" width="50%">cn</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56725mcpsimp"><td class="cellrowborder" valign="top" width="50%">window-type</td><td class="cellrowborder" valign="top" width="50%">image</td></tr><tr id="EN-US_TOPIC_0000002521560614__row56731mcpsimp"><td class="cellrowborder" valign="top" width="50%">image</td><td class="cellrowborder" valign="top" width="50%">1.png</td></tr></tbody></table>

**Parent topic:** [[Automation based on offline OCR|Automation based on offline OCR]]