---
title: "Rule: Ensuring the Compatibility of External APIs During Asset Development"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283560.html"
depth: 6
---
# Rule: Ensuring the Compatibility of External APIs During Asset Development

**Description**: Open APIs must be compatible with external systems to prevent upper-layer apps from being unavailable. External compatibility is reflected in the following aspects:

1\. Input and output parameters cannot be deleted or modified. New parameters are optional by default.

2\. The behavior of the API should not be changed when the input parameters remain unchanged.

3\. If business requirements change and are incompatible, notify asset users in advance.

4\. Do not expose all APIs to external systems.

**Tool supported or not**: no

**Specification name**: General\_Basic\_Interface\_Compatibility

**Severity**: major

**Parent topic:** [[Principles|Principles]]