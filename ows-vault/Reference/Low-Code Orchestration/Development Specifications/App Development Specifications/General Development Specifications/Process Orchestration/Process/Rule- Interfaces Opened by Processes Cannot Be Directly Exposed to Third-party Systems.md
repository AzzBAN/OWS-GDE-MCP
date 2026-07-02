---
title: "Rule: Interfaces Opened by Processes Cannot Be Directly Exposed to Third-party Systems"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403873.html"
depth: 6
---
# Rule: Interfaces Opened by Processes Cannot Be Directly Exposed to Third-party Systems

**Description**:

The interfaces opened by processes can be used only during process orchestration and cannot be directly exposed to third-party systems. If related capabilities need to be provided for third-party systems, service developers need to package the capabilities and expose them to external systems based on the integration services or the API Fabric setting.

**Check guide**:

Check whether the interfaces opened by processes are directly called when a third-party system is integrated.

**Tool supported or not**: no

**Specification name**: General\_Process\_interface\_Is\_InvokeByThirdParty

**Severity**: minor

**Parent topic:** [[Process|Process]]