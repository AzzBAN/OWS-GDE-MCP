---
title: "Rule: Record Only Key and Necessary Debug Logs in the Orchestration Script"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123664.html"
depth: 6
---
# Rule: Record Only Key and Necessary Debug Logs in the Orchestration Script

**Description**: Do not use too many and non-key debug logs. Too many or non-key debug logs in the orchestration script affect the performance and affect problem demarcation and analysis.

**Check guide**:

1\. On the API development or process orchestration page, open all Service and Task diagram elements.

![[en-us_image_0000001475438616.png]]

2\. Check all log.error statements contained in the orchestration scripts of all diagram elements to determine whether the statements are necessary in the production environment.

![[en-us_image_0000001521063869.png]]

**Positive example**: Key logs at the error level are recorded only in specific error code scenarios.

![[en-us_image_0000001344945869.png]]

**Negative example**: Error-level logs are printed without determining whether the scenario is abnormal. As a result, junk logs are generated for each calling.

![[en-us_image_0000001344946129.png]]

**Tool supported or not**: no

**Specification name**: General\_API\_Avoid\_Too\_Many\_DEBUG\_LOG\_During\_Java\_Script

**Severity**: major

**Parent topic:** [[Openness Integration|Openness Integration]]