---
title: "Rule: Placeholders Must Be Used to Configure User Names and Passwords in Device Login Commands"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283720.html"
depth: 5
---
# Rule: Placeholders Must Be Used to Configure User Names and Passwords in Device Login Commands

**Description**: The user name and password in plaintext cannot be configured in the device login command.

**Check guide**: Check whether the login command contains the plaintext user name and password.

**Positive example**:

![[en-us_image_0000001816748573.png]]

**Negative example**:

![[en-us_image_0000001816628085.png]]

**Tool supported or not**: yes

**Specification name**: General\_MCP\_Device\_Login\_Command\_Forbidden\_Plaintext\_Username\_And\_Password

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: network automation orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]