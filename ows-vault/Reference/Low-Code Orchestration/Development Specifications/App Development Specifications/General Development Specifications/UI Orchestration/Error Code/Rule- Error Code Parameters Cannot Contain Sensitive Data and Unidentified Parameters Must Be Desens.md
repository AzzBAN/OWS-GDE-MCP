---
title: "Rule: Error Code Parameters Cannot Contain Sensitive Data and Unidentified Parameters Must Be Desensitized"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963740.html"
depth: 6
---
# Rule: Error Code Parameters Cannot Contain Sensitive Data and Unidentified Parameters Must Be Desensitized

**Description**: The parameter information in the error code cause and solution cannot contain sensitive data.

**Check guide**: In the develop-state environment, check whether the transferred parameter contains sensitive data when the error code is referenced. If the sensitive data cannot be identified, desensitize the parameter in the reference position.

**Tool supported or not**: no

**Specification name**: General\_ErrorCode\_ErrorCode\_Not\_Contains\_Sensitive\_Info

**Severity**: major

**Orchestration scenario**: all

**Parent topic:** [[Error Code|Error Code]]