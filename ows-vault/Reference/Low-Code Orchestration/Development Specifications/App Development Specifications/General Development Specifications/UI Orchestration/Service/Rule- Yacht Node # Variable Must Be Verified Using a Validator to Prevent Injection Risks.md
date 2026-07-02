---
title: "Rule: Yacht Node # Variable Must Be Verified Using a Validator to Prevent Injection Risks"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523361.html"
depth: 6
---
# Rule: Yacht Node # Variable Must Be Verified Using a Validator to Prevent Injection Risks

**Description**: The yacht node provides flexible parameter settings. In scenarios such as table names, the # variable is used as placeholder, which may cause injection risks.

**Check guide**: Configure a validator for the # variable in the input parameter to specify the parameter range and prevent SQL injection risks.

**Positive example**: Use # to replace variables in the table. The SQL statement needs to be validated in the input parameter validator.

![[en-us_image_0000001468544160.png]]

**Negative example**: The start and limit variables are replaced with # but are not verified in the input parameter validator.

**Tool supported or not**: no

**Specification name**: General\_Service\_Start\_Value\_Cannot\_Exceed\_10000

**Severity**: minor

**Orchestration scenario**: data orchestration

**Parent topic:** [[Service|Service]]