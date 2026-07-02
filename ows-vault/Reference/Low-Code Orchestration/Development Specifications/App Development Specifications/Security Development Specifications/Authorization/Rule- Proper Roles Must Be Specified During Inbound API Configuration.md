---
title: "Rule: Proper Roles Must Be Specified During Inbound API Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963836.html"
depth: 5
---
# Rule: Proper Roles Must Be Specified During Inbound API Configuration

**Description**: The inbound APIs of the integration service support machine-machine accounts on GAM and these machine-machine accounts support permission control. If a role is configured for the inbound service, only the account of the corresponding role can access the service.

**Check guide**: Check whether the role configuration of the inbound authentication policy is proper.

**Example scenario**: Configure necessary roles for inbound authentication.

![[en-us_image_0000001470262242.png]]

**Tool supported or not**: yes

**Specification name**: Security\_Authority\_Inbound\_\_No\_Control

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: API orchestration - API integration and orchestration

**Parent topic:** [[Authorization|Authorization]]