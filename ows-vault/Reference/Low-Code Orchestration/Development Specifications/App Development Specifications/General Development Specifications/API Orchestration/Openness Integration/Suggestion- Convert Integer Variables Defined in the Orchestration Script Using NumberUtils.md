---
title: "Suggestion: Convert Integer Variables Defined in the Orchestration Script Using NumberUtils"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363533.html"
depth: 6
---
# Suggestion: Convert Integer Variables Defined in the Orchestration Script Using NumberUtils

**Description**: Values in JS scripts do not have types. After being mapped to Java, the values are automatically converted to floating-point values. If integers are required, you are advised to use NumberUtils.toInt to convert the integers before using them.

**Check guide**:

1\. On the API development or process orchestration page, open all Service and Task diagram elements.

![[en-us_image_0000001475278796.png]]

2\. Check the value assignment statement for integer parameters in the orchestration script.

![[en-us_image_0000001345067401.png]]

**Positive example**:

![[en-us_image_0000001344747969.png]]

**Negative example**:

![[en-us_image_0000001292148320.png]]

**Tool supported or not**: no

**Specification name**: General\_API\_Number\_Type\_Convert\_Before\_Use\_IN\_Java\_Script

**Severity**: suggestion

**Parent topic:** [[Openness Integration|Openness Integration]]