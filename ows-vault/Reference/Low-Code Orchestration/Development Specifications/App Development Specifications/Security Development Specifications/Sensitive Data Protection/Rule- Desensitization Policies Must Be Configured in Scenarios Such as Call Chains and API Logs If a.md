---
title: "Rule: Desensitization Policies Must Be Configured in Scenarios Such as Call Chains and API Logs If an API Contains Sensitive Fields"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643477.html"
depth: 5
---
# Rule: Desensitization Policies Must Be Configured in Scenarios Such as Call Chains and API Logs If an API Contains Sensitive Fields

**Description**: Requests and responses are recorded or reported using a call chain or the API log capability. If any sensitive field is included, security problems may occur.

**Check guide**: Check whether the API log policy is enabled for all APIs on the develop-state API Fabric page. If yes, check with R&D engineers whether the API contains sensitive fields, such as passwords and mobile numbers. If sensitive data is contained, enable the sensitive log policy of the API on the develop-state page and configure all sensitive fields and corresponding data desensitization policies.

![[en-us_image_0000001944863156.png]]

Positive example:

1.  Check whether the API log function is enabled.
    
    The following figure shows the page with API log function enabled.
    
    ![[en-us_image_0000001944703872.png]]
    
2.  If this function is enabled, configure a method-level desensitization policy.
    
    Select the corresponding parameters to configure desensitization rules, as shown in the following figure.
    
    ![[en-us_image_0000001972062037.png]]
    

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_APIFabric\_MustConfigDesensitization

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: API orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]