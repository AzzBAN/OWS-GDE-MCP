---
title: "Rule: Desensitize Any Sensitive Field in Connector Input Parameters in Logs. Encrypted Transmission Is Recommended"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002370571436.html"
depth: 5
---
# Rule: Desensitize Any Sensitive Field in Connector Input Parameters in Logs. Encrypted Transmission Is Recommended

**Description**: Log desensitization policies cannot be configured for connectors.

![[en-us_image_0000002325883570.png]]

**Check guide**: Check whether all fields of a connector need to be desensitized during log printing. For fields that need to be desensitized, you are advised to encrypt them for transmission and decrypt them upon receiving.

**Tool supported or not**: no

**Specification name**: Security\_Connector\_Parameters\_Anonymization

**Severity**: major

**Orchestration scenario**: API orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]