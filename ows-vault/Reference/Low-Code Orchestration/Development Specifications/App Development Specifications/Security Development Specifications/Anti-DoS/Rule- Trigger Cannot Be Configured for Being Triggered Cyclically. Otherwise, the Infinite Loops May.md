---
title: "Rule: Trigger Cannot Be Configured for Being Triggered Cyclically. Otherwise, the Infinite Loops May Occur"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208360491.html"
depth: 5
---
# Rule: Trigger Cannot Be Configured for Being Triggered Cyclically. Otherwise, the Infinite Loops May Occur

**Description**: The trigger that is triggered cyclically means that data changes of a model trigger some triggers that may directly or indirectly change data in the model. The trigger that is triggered cyclically causes the execution of a large number of rule activities, consuming a large number of performances resources. The performance impact lasts a period of time.

**Check guide**: When a trigger that is configured on the develop-state page is cyclically triggered, a prompt is displayed. For example, an unconditional trigger triggered by the update operation of a model updates the data of the model.

However, the system does not display a message for a trigger that is indirectly triggered or a conditional trigger in the develop-state environment. Manually check whether the triggers configured in the model of the model data operation activity operation may directly or indirectly form a loop.

In the runtime-state environment, if too many loops are triggered on the WebUI, the error code is displayed on the WebUI. If such a message is displayed, the rule that cyclically triggers other rules described in the message exists.

Although ADC has a certain infinite loop detection mechanism, it can detect infinite loops only in some known scenarios. Due to the flexibility of configuration calling, the system cannot detect infinite loops in all scenarios. Developers need to pay attention to whether logic calling may enter an infinite loop in their own triggers.

**Negative example**: A trigger activity directly or indirectly changes the model that triggers the trigger, and those changes directly or indirectly trigger the trigger activity.

For example, the following figure shows that the model where the model data operation is performed on the trigger is the one that triggers the trigger. Therefore, a loop is formed.

![[en-us_image_0000001120142252.png]]

When such trigger is saved, ADC detects the loop and reports an error as shown in the following figure.

![[en-us_image_0000001119982340.png]]

**Positive example**:

![[en-us_image_0000001817203713.png]]

**Tool supported or not**: yes

**Specification name**: Security\_DOS\_Trigger\_ProhibitInfiniteLoop

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: general job orchestration

**Parent topic:** [[Anti-DoS|Anti-DoS]]