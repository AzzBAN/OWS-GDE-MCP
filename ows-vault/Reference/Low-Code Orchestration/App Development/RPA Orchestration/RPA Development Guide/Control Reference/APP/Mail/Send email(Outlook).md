---
title: "Send email(Outlook)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560435.html"
depth: 7
---
# Send email(Outlook)

**outlook.sendEmail**

**Description:**

1.Use local Outlook to send mail. Using this command will require the user to interact with the system. Click on the window that pops up mid-way, or you can set it up in Options-Trust Center-Trust Center Settings-Programmatic Access-No warning will be issued; otherwise it will block this command.

2.The frequent sending is limited. It is recommended that the sending interval be greater than 500 ms.

3.For details, see the usage of each parameter.

4\. Please ensure that the network is unblocked before sending emails.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560435__table124620mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560435__row124629mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124648mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">content settings</td><td class="cellrowborder" valign="top" width="16.666666666666664%">kv_group</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Email Body Template;Mail body variable;Email Subject;Image in the Email Body;Email Attachment,Click the More button on the right to view the edits</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124662mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">send settings</td><td class="cellrowborder" valign="top" width="16.666666666666664%">kv_group</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Email Recipient;Recipients in CC;Recipients in BCC,Click the More button on the right to view the edits</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124676mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124690mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

To send a message using the Outlook Mailbox app:

1\. The subject of the email is "Test11 outlook.sendEmail."

2\. The sender is from, the recipient is to, and the cc is copied to, and the cc is secretly copied to the bcc.

3\. The body image is an image, and the attachment is D:\\test\\msc.png.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560435__table124712mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560435__row124717mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124724mcpsimp"><td class="cellrowborder" valign="top" width="50%">template</td><td class="cellrowborder" valign="top" width="50%">Test test:@{url}&lt;br&gt;@{image}</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124730mcpsimp"><td class="cellrowborder" valign="top" width="50%">template-params</td><td class="cellrowborder" valign="top" width="50%">url:http://xxx/xxx/xxx/</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124736mcpsimp"><td class="cellrowborder" valign="top" width="50%">subject</td><td class="cellrowborder" valign="top" width="50%">Test11 outlook.sendEmail</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124742mcpsimp"><td class="cellrowborder" valign="top" width="50%">to</td><td class="cellrowborder" valign="top" width="50%">@{to}</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124748mcpsimp"><td class="cellrowborder" valign="top" width="50%">cc</td><td class="cellrowborder" valign="top" width="50%">@{cc}</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124754mcpsimp"><td class="cellrowborder" valign="top" width="50%">bcc</td><td class="cellrowborder" valign="top" width="50%">@{bcc}</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124760mcpsimp"><td class="cellrowborder" valign="top" width="50%">image</td><td class="cellrowborder" valign="top" width="50%">@{image}</td></tr><tr id="EN-US_TOPIC_0000002552560435__row124766mcpsimp"><td class="cellrowborder" valign="top" width="50%">attach</td><td class="cellrowborder" valign="top" width="50%">D:\test\msc.png</td></tr></tbody></table>

**Parent topic:** [[Mail|Mail]]