---
title: "Suggestion: Exercise Caution When Proactively Throwing Exceptions in the Orchestration Script"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804104.html"
depth: 6
---
# Suggestion: Exercise Caution When Proactively Throwing Exceptions in the Orchestration Script

**Description**: The proactive exception throwing behavior in the orchestration script should be used only to interrupt the process in abnormal scenarios. Otherwise, the execution performance will be severely affected.

**Check guide**:

1\. On the API development or process orchestration page, open all Service and Task diagram elements.

![[en-us_image_0000001475118808.png]]

2\. Check all throw error statements in the orchestration script and check whether the statements can be executed only in specific exception scenarios.

![[en-us_image_0000001470132046.png]]

**Positive example**:

![[en-us_image_0000001292306920.png]]

**Negative example**: An exception is thrown and the normal response is transferred through the exception.

![[en-us_image_0000001291987468.png]]

**Tool supported or not**: no

**Specification name**: General\_API\_Avoid\_Throw\_Exception\_During\_Java\_Script\_IN\_Normal\_Process

**Severity**: suggestion

**Parent topic:** [[Openness Integration|Openness Integration]]