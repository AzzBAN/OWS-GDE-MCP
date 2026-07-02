---
title: "Rule: Time-consuming Logic, Such as Infinite Loop and Simulated Sleep, Cannot Be Found in Orchestration Scripts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643489.html"
depth: 5
---
# Rule: Time-consuming Logic, Such as Infinite Loop and Simulated Sleep, Cannot Be Found in Orchestration Scripts

**Description**: The logic such as infinite loop and simulated sleep occupies system resources for a long time, which may cause DoS attacks.

**Check guide**:

1\. On the API development or process orchestration page, open all Service and Task diagram elements.

![[en-us_image_0000001521798905.png]]

2\. Check all while and for statements in the orchestration script to determine whether time-consuming scenarios exist.

![[en-us_image_0000001291992484.png]]

**Negative example**: A sleep function is developed and called in the orchestration script to implement the wait operation.

![[en-us_image_0000001296848742.png]]

**Tool supported or not**: yes

**Specification name**: Security\_DOS\_API\_Avoid\_Long\_Time\_Loop\_During\_Java\_Script

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: API orchestration

**Parent topic:** [[Anti-DoS|Anti-DoS]]