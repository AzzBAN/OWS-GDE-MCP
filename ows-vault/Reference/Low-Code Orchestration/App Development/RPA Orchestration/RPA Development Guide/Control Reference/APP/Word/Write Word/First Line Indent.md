---
title: "First Line Indent"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400522.html"
depth: 8
---
# First Line Indent

**word.setFirstLineIndent**

**Description:**

Set the indentation of the first line of a document paragraph:

1\. If the page number and paragraph number are left blank, the indentation of the first line of all paragraphs is set.

2\. Only the page number table sets the first line indentation of all paragraphs on the specified page.

3\. Only the paragraph number indicates the first indentation of the specified paragraph on page 1.

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400522__table84064mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400522__row84070mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84080mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">DocObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Specify the document object to be operated</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400522__table84090mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400522__row84099mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84118mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">indent</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">22</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Length of first line indent.The unit is point and a character is 11 points</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84132mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">page-num</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Document page number</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84146mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">para-num</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Document paragraph numbering</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84160mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84174mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**samples**

Sets the first line indentation of all paragraphs in the document by 22 points, that is 2 characters

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400522__table84193mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400522__row84198mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84205mcpsimp"><td class="cellrowborder" valign="top" width="50%">indent</td><td class="cellrowborder" valign="top" width="50%">22</td></tr></tbody></table>

Set the indentation of the first line of the first paragraph of the first page of the document to 22 points, that is, 2 characters

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400522__table84212mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400522__row84217mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84224mcpsimp"><td class="cellrowborder" valign="top" width="50%">indent</td><td class="cellrowborder" valign="top" width="50%">22</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84230mcpsimp"><td class="cellrowborder" valign="top" width="50%">para-num</td><td class="cellrowborder" valign="top" width="50%">1</td></tr></tbody></table>

Set the indentation of the first line of the first line of the first paragraph of the second page of the document to 22 points, that is, 2 characters

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400522__table84237mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400522__row84242mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84249mcpsimp"><td class="cellrowborder" valign="top" width="50%">indent</td><td class="cellrowborder" valign="top" width="50%">22</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84255mcpsimp"><td class="cellrowborder" valign="top" width="50%">page-num</td><td class="cellrowborder" valign="top" width="50%">2</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84261mcpsimp"><td class="cellrowborder" valign="top" width="50%">para-num</td><td class="cellrowborder" valign="top" width="50%">1</td></tr></tbody></table>

Set the indentation of the first line of all paragraphs on page 2 of the document to 22 points, that is, 2 characters

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400522__table84268mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400522__row84273mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84280mcpsimp"><td class="cellrowborder" valign="top" width="50%">indent</td><td class="cellrowborder" valign="top" width="50%">22</td></tr><tr id="EN-US_TOPIC_0000002521400522__row84286mcpsimp"><td class="cellrowborder" valign="top" width="50%">page-num</td><td class="cellrowborder" valign="top" width="50%">2</td></tr></tbody></table>

**Parent topic:** [[Write Word|Write Word]]