---
title: "Set Line Spacing"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560505.html"
depth: 8
---
# Set Line Spacing

**word.setLineSpacing**

**Description:**

Set the line spacing of a document paragraph:

1\. If the page number and paragraph number are left blank, the line spacing of all paragraphs is set.

2\. Only the page number table sets the line spacing of all paragraphs on the specified page.

3\. Only the paragraph number indicates setting the leading of the specified paragraph on page 1.

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560505__table68851mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560505__row68857mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560505__row68867mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">DocObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Specify the document object to be operated</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560505__table68877mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560505__row68886mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560505__row68905mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">line-spacing</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">12</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Length of line spacing.The unit is point and Single spacing is 12 pounds</td></tr><tr id="EN-US_TOPIC_0000002552560505__row68919mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">page-num</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Document page number</td></tr><tr id="EN-US_TOPIC_0000002552560505__row68933mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">para-num</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Document paragraph numbering</td></tr><tr id="EN-US_TOPIC_0000002552560505__row68947mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552560505__row68961mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Set the document line spacing to 12 points, that is single line spacing

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560505__table68980mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560505__row68985mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560505__row68992mcpsimp"><td class="cellrowborder" valign="top" width="50%">line-spacing</td><td class="cellrowborder" valign="top" width="50%">12</td></tr></tbody></table>

Set the paragraph 2 on page 1 of the document to 12 points, that is single line spacing

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560505__table68999mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560505__row69004mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560505__row69011mcpsimp"><td class="cellrowborder" valign="top" width="50%">line-spacing</td><td class="cellrowborder" valign="top" width="50%">12</td></tr><tr id="EN-US_TOPIC_0000002552560505__row69017mcpsimp"><td class="cellrowborder" valign="top" width="50%">para-num</td><td class="cellrowborder" valign="top" width="50%">2</td></tr></tbody></table>

Set the paragraph 2 on page 2 of the document to 12 points, that is single line spacing

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560505__table69024mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560505__row69029mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560505__row69036mcpsimp"><td class="cellrowborder" valign="top" width="50%">line-spacing</td><td class="cellrowborder" valign="top" width="50%">12</td></tr><tr id="EN-US_TOPIC_0000002552560505__row69042mcpsimp"><td class="cellrowborder" valign="top" width="50%">page-num</td><td class="cellrowborder" valign="top" width="50%">2</td></tr><tr id="EN-US_TOPIC_0000002552560505__row69048mcpsimp"><td class="cellrowborder" valign="top" width="50%">para-num</td><td class="cellrowborder" valign="top" width="50%">2</td></tr></tbody></table>

Set all paragraphs on page 2 of the document to 12 points, that is single line spacing

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560505__table69055mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560505__row69060mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560505__row69067mcpsimp"><td class="cellrowborder" valign="top" width="50%">line-spacing</td><td class="cellrowborder" valign="top" width="50%">12</td></tr><tr id="EN-US_TOPIC_0000002552560505__row69073mcpsimp"><td class="cellrowborder" valign="top" width="50%">page-num</td><td class="cellrowborder" valign="top" width="50%">2</td></tr></tbody></table>

**Parent topic:** [[Write Word|Write Word]]