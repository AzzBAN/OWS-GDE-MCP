---
title: "Suggestion: Preferentially Use the Asynchronous Mode for Trigger Activities"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363509.html"
depth: 6
---
# Suggestion: Preferentially Use the Asynchronous Mode for Trigger Activities

**Description**: If a trigger activity in synchronous mode fails to be executed, the execution of activities with lower priorities is affected.

**Check guide**: On the develop-state page, check whether the synchronous mode of each trigger can be changed to asynchronous mode. If the effect of a rule activity is not depended on by subsequent activities (for example, the activity with a lower priority or triggered later) and the current model does not need to be written back, you can configure the synchronization mode for the rule activity to the asynchronous mode.

**Positive example**: If a trigger activity does not need to be synchronized, configure it as an asynchronous activity.

![[en-us_image_0000001520531901.png]]

**Exception scenario**: Activities that must be executed in synchronous mode (activities that need to block subsequent activities and activities that have strict requirements on the execution sequence) are excluded.

**Tool supported or not**: no

**Specification name**: General\_Trigger\_Use\_Asynchronous\_Mode

**Severity**: suggestion

**Parent topic:** [[Trigger|Trigger]]