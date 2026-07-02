---
title: "Infinite Loop Is Displayed During Model Trigger Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001328251580.html"
depth: 3
---
#### Symptom

When a rule (trigger) configuration is submitted or a rule is imported on the develop-state page, if the system detects that the trigger operates on its own model, no trigger condition is configured, and the operation type is the same as the model operation, an infinite loop is definitely triggered. This scenario is detected during rule metadata configuration. Therefore, rules cannot be updated or imported.

![[en-us_image_0000001406258958.png]]