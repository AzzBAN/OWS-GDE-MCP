---
title: "Rule: Do Not Upload Users' Personal Data, Sensitive Data, or Privacy Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001237104695.html"
depth: 6
---
# Rule: Do Not Upload Users' Personal Data, Sensitive Data, or Privacy Data

**Specification name**: General\_DataFactory\_Upload\_No\_Sensitive\_Data

**Description**: The debugging data is the experimental one constructed by simulating the actual running scenario during the debugging. The debugging data cannot contain any personal data, sensitive data, or privacy data.

**Check guide**: Check whether the uploaded data contains personal data, sensitive data, or privacy data. Such data includes numbers that can identify natural persons, bank accounts, original communication content (emails and SMS messages), keys, session IDs, verification codes (including SMS verification codes), session tokens, and passwords (such as voucher passwords).

**Impact**: Utilizing users' personal, sensitive, or privacy data for debugging purposes may lead to data leaks, potential legal violations, harms to Huawei's reputation, financial standing, and operations, as well as adverse impact on personal data subjects to different degrees

**Parent topic:** [[Debugging Data Management and Online Debugging|Debugging Data Management and Online Debugging]]