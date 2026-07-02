---
title: "Move Cursor"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400528.html"
depth: 8
---
# Move Cursor

**word.moveCursor**

**Description:**

Move position of cursor

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400528__table136797mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400528__row136803mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136813mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">DocObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Specify the document object to be operated</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400528__table136823mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400528__row136832mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136851mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">unit</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">character</td><td class="cellrowborder" valign="top" width="16.666666666666664%">character|word|sentence|paragraph|line|story|table|row|column</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Unit of cursor movement.character indicates the character, word indicates the word, sentence indicates the sentence, paragraph indicates the paragraph, line indicates the row, story indicates the entire document, table indicates the table, row indicates the row of the table, and column indicates the column of the table</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136865mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">count</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">1</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Count of cursor movement. Negative numbers indicate backward movement</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136879mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136893mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Move the cursor to the right by 3 characters

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400528__table136912mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400528__row136917mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136924mcpsimp"><td class="cellrowborder" valign="top" width="50%">unit</td><td class="cellrowborder" valign="top" width="50%">character</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136930mcpsimp"><td class="cellrowborder" valign="top" width="50%">count</td><td class="cellrowborder" valign="top" width="50%">3</td></tr></tbody></table>

Move the cursor 3 words to the right

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400528__table136937mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400528__row136942mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136949mcpsimp"><td class="cellrowborder" valign="top" width="50%">unit</td><td class="cellrowborder" valign="top" width="50%">word</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136955mcpsimp"><td class="cellrowborder" valign="top" width="50%">count</td><td class="cellrowborder" valign="top" width="50%">3</td></tr></tbody></table>

Move the cursor three sentences to the right

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400528__table136962mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400528__row136967mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136974mcpsimp"><td class="cellrowborder" valign="top" width="50%">unit</td><td class="cellrowborder" valign="top" width="50%">sentence</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136980mcpsimp"><td class="cellrowborder" valign="top" width="50%">count</td><td class="cellrowborder" valign="top" width="50%">3</td></tr></tbody></table>

Move the cursor down 3 lines

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400528__table136987mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400528__row136992mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400528__row136999mcpsimp"><td class="cellrowborder" valign="top" width="50%">unit</td><td class="cellrowborder" valign="top" width="50%">line</td></tr><tr id="EN-US_TOPIC_0000002521400528__row137005mcpsimp"><td class="cellrowborder" valign="top" width="50%">count</td><td class="cellrowborder" valign="top" width="50%">3</td></tr></tbody></table>

Move the cursor down 3 segments

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400528__table137012mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400528__row137017mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400528__row137024mcpsimp"><td class="cellrowborder" valign="top" width="50%">unit</td><td class="cellrowborder" valign="top" width="50%">paragraph</td></tr><tr id="EN-US_TOPIC_0000002521400528__row137030mcpsimp"><td class="cellrowborder" valign="top" width="50%">count</td><td class="cellrowborder" valign="top" width="50%">3</td></tr></tbody></table>

Move cursor to end of document

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400528__table137037mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400528__row137042mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400528__row137049mcpsimp"><td class="cellrowborder" valign="top" width="50%">unit</td><td class="cellrowborder" valign="top" width="50%">story</td></tr><tr id="EN-US_TOPIC_0000002521400528__row137055mcpsimp"><td class="cellrowborder" valign="top" width="50%">count</td><td class="cellrowborder" valign="top" width="50%">1</td></tr></tbody></table>

**Parent topic:** [[Common|Common]]