---
title: "Rule: When a Prompt Template References a Context Variable, the Variable Name Must Be Enclosed in Double Braces and Only Variables of the String, Array, and Object Types Can Be Referenced"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404117377.html"
depth: 6
---
# Rule: When a Prompt Template References a Context Variable, the Variable Name Must Be Enclosed in Double Braces and Only Variables of the String, Array, and Object Types Can Be Referenced

**Description**: The agent orchestration feature allows you to customize prompts. You can use preset placeholders to reference the content of context variables. Variables can be replaced only by names enclosed in double braces {{}}, for example, _{{Variable}}_. Currently, only variables of the string, array, and object types can be referenced, that is, _{{Variable}}_, _{{Variable\[N\]}_}, and _{{Variable.Value}}_.

**Check guide**: Access the agent prompt management page and create a prompt template.

**Positive example**:

![[en-us_image_0000002403723253.png]]

**Tool supported or not**: no

**Specification name**: General\_Prompts\_Variable\_Standardization

**Severity**: minor

**Parent topic:** [[Intelligent Component Orchestration|Intelligent Component Orchestration]]