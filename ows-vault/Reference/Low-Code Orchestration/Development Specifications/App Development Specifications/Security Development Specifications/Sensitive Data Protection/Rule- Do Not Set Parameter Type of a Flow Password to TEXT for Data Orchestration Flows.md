---
title: "Rule: Do Not Set Parameter Type of a Flow Password to TEXT for Data Orchestration Flows"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404131093.html"
depth: 5
---
# Rule: Do Not Set Parameter Type of a Flow Password to TEXT for Data Orchestration Flows

**Description**: When defining flow parameters, if a field is of the password type, **Parameter Type** must be set to **PASSWORD**. Otherwise, the password parameter will be displayed and stored in plaintext in the runtime-state environment, causing improper password disclosure.

**Check guide**: Check whether a flow parameter is sensitive. If yes, set **Parameter Type** to **PASSWORD**.

**Positive example**: If a flow parameter is sensitive, **Parameter Type** is set to **PASSWORD**.

![[en-us_image_0000001721675957.png]]

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_Not\_Flow\_Param\_StoreByPasswordType

**Category**: non-bottom-line check item

**Severity**: critical

**Orchestration scenario**: data orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]