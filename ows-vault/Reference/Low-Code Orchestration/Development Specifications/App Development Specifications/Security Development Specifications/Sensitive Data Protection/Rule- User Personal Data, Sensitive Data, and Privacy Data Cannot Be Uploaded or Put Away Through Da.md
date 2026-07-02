---
title: "Rule: User Personal Data, Sensitive Data, and Privacy Data Cannot Be Uploaded or Put Away Through DataFactory"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404051249.html"
depth: 5
---
# Rule: User Personal Data, Sensitive Data, and Privacy Data Cannot Be Uploaded or Put Away Through DataFactory

**Description**: Personal data, sensitive data, and privacy data should not be pushed by the engine operators of DataFactory. Custom functions, custom operators, and custom programs should not contain any personal data, sensitive data, or privacy data.

**Check guide**: Check whether the uploaded data contains personal data, sensitive data, or privacy data. Sensitive and privacy data mainly refers to passwords, certificate numbers, bank accounts, original communication content (emails and SMS messages), keys, session IDs, verification codes (including SMS verification codes), session tokens, and passwords (such as voucher passwords). Check whether the uploaded custom functions, custom operators, and custom program assets contain personal sensitive data and privacy data. Such data includes numbers that can identify natural persons, bank accounts, original communications content (emails and SMS messages), keys, session IDs, verification codes (including SMS verification codes), session tokens, and passwords (such as voucher passwords).

**Impact**: If the engine operators, custom functions, custom operators, and custom programs used by DataFactory use users' personal data, sensitive data, and privacy data, laws may be violated, which may affect the company's reputation, finance, or operations, and have adverse impacts on personal data subjects.

**Specification name**: Security\_DataFactory\_ Custom\_Function\_Upload\_No\_Sensitive\_Data

**Severity**: major

**Orchestration scenario**: data orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]