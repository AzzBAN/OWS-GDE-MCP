---
title: "Suggestion: Do Not Set Protocol to HTTP During Operator Configuration in Data Orchestration Flows"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002370411572.html"
depth: 5
---
# Suggestion: Do Not Set Protocol to HTTP During Operator Configuration in Data Orchestration Flows

**Description**: When using HTTP-related operators, you are advised to set **Protocol** to **HTTPS** because HTTP is an insecure protocol and may cause improper information disclosure.

**Check guide**: When setting parameters of HTTP-related operators, check whether **Protocol** is set to **HTTPS**.

**Positive example**:

![[en-us_image_0000001673793422.png]]

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_Not\_Use\_HTTP\_InsecureProtocol

**Category**: non-bottom-line check item

**Severity**: suggestion

**Orchestration scenario**: data orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]