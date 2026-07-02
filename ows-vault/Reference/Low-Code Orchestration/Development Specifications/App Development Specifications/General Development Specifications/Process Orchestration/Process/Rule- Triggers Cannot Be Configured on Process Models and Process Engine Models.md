---
title: "Rule: Triggers Cannot Be Configured on Process Models and Process Engine Models"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162800434.html"
depth: 6
---
# Rule: Triggers Cannot Be Configured on Process Models and Process Engine Models

**Description**: If synchronized rules are configured, the ticket execution efficiency may be affected, and problems, such as blocking and timeout, may occur.

**Check guide**:

On the **Model Management** page of the process, query the trigger list. Do not configure triggers in the model, and do not configure synchronized rules.

![[en-us_image_0000001469764796.png]]

**Positive example**:

1\. No model trigger is configured.

**Negative example**:

1\. A model trigger is configured, and synchronization is used.

**Tool supported or not**: no

**Specification name**: General\_Process\_Avoid\_Configure\_Triggers\_on\_the\_Process\_Model\_Forbidden\_Configure\_Synchronous\_Triggers

**Severity**: major

**Parent topic:** [[Process|Process]]