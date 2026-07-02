---
title: "Rule: Do Not Use the Log Operator of DataFactory to Print Personal Information or Sensitive Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404131101.html"
depth: 5
---
# Rule: Do Not Use the Log Operator of DataFactory to Print Personal Information or Sensitive Data

**Description**: To prevent improper information disclosure, do not use the Log operator to print personal information or sensitive data.

**Check guide**: Check whether the configuration of the Log operator contains sensitive data, such as mobile numbers, email addresses, passwords, or variables that contain sensitive data. If so, remove the configuration immediately.

**Impact**: Improper sensitive data disclosure may occur.

**Specification name**: Security\_Log\_DataFactory\_AIP\_Avoiding\_Sensitive\_Info

**Severity**: minor

**Orchestration scenario**: data orchestration

**Parent topic:** [[Logs|Logs]]