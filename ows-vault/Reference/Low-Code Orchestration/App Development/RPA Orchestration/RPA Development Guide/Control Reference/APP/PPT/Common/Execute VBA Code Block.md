---
title: "Execute VBA Code Block"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521560510.html"
depth: 8
---
# Execute VBA Code Block

**pptExecuteVBA**

**Description:**

Execute VBA code block.Some VBA code can be successfully run only in visual conditions. If it fails to run in the background, open the document in the foreground visual mode.You need to select the access permission for VBProject:

1\. Select Development Tools: File > Options > Custom Ribbon > Development Tools.

2\. PPT: Development Tools > Macro Security > Macro Settings > Trust Access to VBA Project Object Model.

3\. WPS: Development Tools > Macro Security > Reliable Publishers > Trust Access to Visual Basic Projects

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560510__table46422mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560510__row46428mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521560510__row46438mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">PPTObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Specify the PPT object to be operated</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560510__table46448mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560510__row46457mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521560510__row46476mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">vba-code</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">VBA code block. Such as: With ActivePresentation.Slides.Add(Index:=1, Layout:=ppLayoutTitle).Shapes .Title.TextFrame.TextRange = "This is the title text" .Placeholders(2).TextFrame.TextRange = "This is subtitle text" End With</td></tr><tr id="EN-US_TOPIC_0000002521560510__row46493mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521560510__row46507mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Run the vba code block: <br/>With ActivePresentation.Slides.Add(Index:=1, Layout:=ppLayoutTitle).Shapes<br/> .Title.TextFrame.TextRange = "This is the title text"<br/> .Placeholders(2).TextFrame.TextRange = "This is subtitle text"<br/>End With

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521560510__table46526mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521560510__row46531mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521560510__row46538mcpsimp"><td class="cellrowborder" valign="top" width="50%">vba-code</td><td class="cellrowborder" valign="top" width="50%">With ActivePresentation.Slides.Add(Index:=1, Layout:=ppLayoutTitle).Shapes<br>.Title.TextFrame.TextRange = "This is the title text"<br>.Placeholders(2).TextFrame.TextRange = "This is subtitle text"<br>End With</td></tr></tbody></table>

**Parent topic:** [[Common|Common]]