---
title: "Rule: Do Not Upload Users' Personal Data, Sensitive Data, or Privacy Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001889179373.html"
depth: 6
---
# Rule: Do Not Upload Users' Personal Data, Sensitive Data, or Privacy Data

**Specification name**: General\_DataFactory\_Data\_Bus\_Upload\_No\_Sensitive\_Data

**Description**: The data uploaded to the object storage operators of the data bus should not contain any personal data, sensitive data, or privacy data.

**Check guide**: Check whether the uploaded data contains personal data, sensitive data, or privacy data. Such data includes numbers that can identify natural persons, bank accounts, original communications content (emails and SMS messages), keys, session IDs, verification codes (including SMS verification codes), session tokens, and passwords (such as voucher passwords).

**Impact**: If the data uploaded to the object storage operators contains any personal data, sensitive data, or privacy data of users, data leakage may occur or even laws may be violated, damaging Huawei's reputation, affecting Huawei's finance or operations, and causing different levels of damage to personal data subjects.

**Parent topic:** [[Data Bus|Data Bus]]