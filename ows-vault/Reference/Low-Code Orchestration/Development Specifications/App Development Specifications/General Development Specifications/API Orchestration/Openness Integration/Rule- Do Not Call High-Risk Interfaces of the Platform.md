---
title: "Rule: Do Not Call High-Risk Interfaces of the Platform"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002309655172.html"
depth: 6
---
# Rule: Do Not Call High-Risk Interfaces of the Platform

**Description**: Calling high-risk interfaces (which will cause business loss or interruption) of the platform through a gateway may maliciously attack internal components of the platform, for example, user privilege escalation and service RCE.

**Check guide**:

1\. On the API development or endpoint configuration page, check whether the endpoint address calls high-risk interfaces of the platform.

![[en-us_image_0000002285286984.png]]

**Tool supported or not**: no

**Specification name**: General\_API\_Avoid\_Calling\_High-risk\_Interfaces

**Severity**: major

**Parent topic:** [[Openness Integration|Openness Integration]]