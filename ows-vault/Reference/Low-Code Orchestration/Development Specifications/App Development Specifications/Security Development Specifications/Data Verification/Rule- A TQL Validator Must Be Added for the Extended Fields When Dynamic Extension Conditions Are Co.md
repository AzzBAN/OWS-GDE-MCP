---
title: "Rule: A TQL Validator Must Be Added for the Extended Fields When Dynamic Extension Conditions Are Configured for a Frontend Service"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403957.html"
depth: 5
---
# Rule: A TQL Validator Must Be Added for the Extended Fields When Dynamic Extension Conditions Are Configured for a Frontend Service

**Description**: GDE provides the extended condition query capability for the GetList service. If the TQL validator is not configured for the extended conditions, TQL injection risks may occur.

**Check guide:** Check whether extended fields are set in the GetList service of the app service list. If extended fields are set, check whether the validator whose field type is TQL is configured and whether the left value is set.

**Positive example**:

1\. Configure service parameters in the extended conditions and add a validator.

![[en-us_image_0000001524510305.png]]

2\. Select TQL as the field type for the validator and configure the left value model corresponding to the fields in the TQL.

![[en-us_image_0000001473190540.png]]

**Tool supported or not**: yes

**Specification name**: Security\_DataCheck\_LogicFlow\_ExtendTQL\_InjectionRisk

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: UI orchestration

**Parent topic:** [[Data Verification|Data Verification]]