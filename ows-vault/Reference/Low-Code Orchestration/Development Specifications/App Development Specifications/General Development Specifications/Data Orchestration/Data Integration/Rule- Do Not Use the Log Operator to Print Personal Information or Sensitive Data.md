---
title: "Rule: Do Not Use the Log Operator to Print Personal Information or Sensitive Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001604033252.html"
depth: 6
---
# Rule: Do Not Use the Log Operator to Print Personal Information or Sensitive Data

**Specification name**: General\_DataFactory\_AIP\_Avoiding\_Sensitive\_Info

**Description**: To prevent information leakage, do not use the Log operator to print personal information or sensitive data.

**Check guide**: Check whether the configuration of the Log operator contains sensitive data, such as mobile numbers, email addresses, passwords, or variables that contain sensitive data. If yes, remove the sensitive data information immediately.

**Impact**: Serious sensitive data leakage may occur.

**Parent topic:** [[Data Integration|Data Integration]]