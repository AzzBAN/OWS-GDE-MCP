---
title: "Try"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552480649.html"
depth: 7
---
# Try

**Try**

**Description:**

Try exception handling statement:

1.The exception handling logic is used together with catch and finally.

2.Exceptions that can be handled by the control.

3.When a control in the subprocess of the control fails to run, a specific exception is thrown. You can set the exception attribute of try to capture the exception.

4.If an exception is captured, execute the corresponding logic in the catch.

5.redo\_times indicates the number of times that the try logic is executed after catch processing if an exception occurs.

6.from\_error\_node indicates whether to execute the control that fails to be executed during retry.

7.redone\_times indicates that if an exception occurs during operation, the try logic will be re-executed after catch processing, and the current number of retries.

**Attributes**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480649__table153187mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480649__row153193mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552480649__row153203mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">redo_times</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">When the redo_times attribute is specified, after the catch processes the exception, it starts from the try tag again, and execute the failed action until there is no error or redo_times value is executed.</td></tr><tr id="EN-US_TOPIC_0000002552480649__row153211mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">redone_times</td><td class="cellrowborder" valign="top" width="33.33333333333333%">string</td><td class="cellrowborder" valign="top" width="33.33333333333333%">When there is the redo_times attribute, catch handles the exception and then returns to try to continue execution from the failed action position, displaying the current number of retries.</td></tr><tr id="EN-US_TOPIC_0000002552480649__row153219mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">from_error_node</td><td class="cellrowborder" valign="top" width="33.33333333333333%">list</td><td class="cellrowborder" valign="top" width="33.33333333333333%">Indicates whether to start execution from an incorrect action during retry upon an error. The default value is True.</td></tr></tbody></table>

**Samples**

Error retry five times, starting from the first control of the try subflow

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552480649__table153230mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552480649__row153235mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552480649__row153242mcpsimp"><td class="cellrowborder" valign="top" width="50%">redo_times</td><td class="cellrowborder" valign="top" width="50%">5</td></tr><tr id="EN-US_TOPIC_0000002552480649__row153248mcpsimp"><td class="cellrowborder" valign="top" width="50%">from\_error\_node</td><td class="cellrowborder" valign="top" width="50%">False</td></tr></tbody></table>

Capture custom exception ValidateError

![[en-us_image_0000002552560945.png]]

![[en-us_image_0000002552480929.png]]

**Parent topic:** [[Exception|Exception]]