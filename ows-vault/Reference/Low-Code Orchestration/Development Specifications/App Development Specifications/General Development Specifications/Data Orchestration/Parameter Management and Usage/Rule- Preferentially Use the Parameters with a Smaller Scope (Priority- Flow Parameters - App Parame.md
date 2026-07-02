---
title: "Rule: Preferentially Use the Parameters with a Smaller Scope (Priority: Flow Parameters > App Parameters > Tenant Parameters)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001192464724.html"
depth: 6
---
# Rule: Preferentially Use the Parameters with a Smaller Scope (Priority: Flow Parameters > App Parameters > Tenant Parameters)

**Specification name**: General\_DataFactory\_Parameter\_Priority

**Description**: Preferentially use parameters with a smaller scope. The priority is as follows: flow parameters > app parameters > tenant parameters. This simplifies the dependencies and reduces mutual impact between flows or between apps, facilitating development and maintenance.

**Check guide**: Check whether the tenant parameters used during orchestration need to be used by multiple apps. If not, you are advised to define them as app parameters. Check whether the app parameters used during orchestration need to be used by multiple flows. If not, you are advised to define them as flow parameters.

**Positive example**: Reference flow parameters in a flow, and reference app parameters in an app.

**Impact**: Cross-app parameter reference leads to dependency between apps, increasing management complexity.

**Parent topic:** [[Parameter Management and Usage|Parameter Management and Usage]]