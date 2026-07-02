---
title: "Rule: Enter Verification Rules Based on the Parameter Usage When Editing Parameters for Data Integration Flows"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001653753249.html"
depth: 6
---
# Rule: Enter Verification Rules Based on the Parameter Usage When Editing Parameters for Data Integration Flows

**Specification name**: General\_DataFactory\_AIP\_Match\_Parameter\_Rule

**Description**: When editing parameters for data integration flows, you need to enter verification rules based on the actual usage to prevent app running issues or security risks caused by invalid input during parameter modification in the production environment.

**Check guide**: Check whether the regular expressions for added parameters comply with the specifications based on the actual usage of the parameters. The regular expression range must be minimized to avoid invalid verification rules such as (.\*) or regular expressions that are vulnerable to ReDoS attacks.

**Impact**: Inappropriate data verification rules may affect app running or cause security risks.

**Parent topic:** [[Data Integration|Data Integration]]