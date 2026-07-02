---
title: "Rule: Orchestration Scripts Support Only the ES6 Syntax"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643385.html"
depth: 6
---
# Rule: Orchestration Scripts Support Only the ES6 Syntax

**Description**: Orchestration and authentication during API development require customization using the JS script. However, the script supports only the ES6 syntax and does not support ES7, ES8, or ES9. Currently, the development tool supports only syntax prompt but does not support syntax check.

**Check guide**:

1\. On the API development or process orchestration page, open all Service and Task diagram elements.

![[en-us_image_0000001526198585.png]]

2\. Check whether the orchestration scripts of all diagram elements use the ES6 or later syntax.

![[en-us_image_0000001469823848.png]]

**Tool supported or not**: no

**Specification name**: General\_API\_Open\_API\_Only\_Supports\_the\_ES6\_Syntax

**Severity**: major

**Parent topic:** [[Openness Integration|Openness Integration]]