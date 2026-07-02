---
title: "Rule: Do Not Upload Users' Personal Data, Sensitive Data, or Privacy Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001891919340.html"
depth: 6
---
# Rule: Do Not Upload Users' Personal Data, Sensitive Data, or Privacy Data

**Specification name**: General\_DataFactory\_Stream\_Upload\_No\_Sensitive\_Data

**Description**: The object storage operators of stream processing should not contain any personal data, sensitive data, or privacy data.

**Check guide**: Check whether the uploaded data contains personal data, sensitive data, or privacy data. Such data includes numbers that can identify natural persons, bank accounts, original communications content (emails and SMS messages), keys, session IDs, verification codes (including SMS verification codes), session tokens, and passwords (such as voucher passwords).

**Impact**: If the object storage operators use any personal data, sensitive data, or privacy data of users, data leakage may occur or even laws may be violated, damaging Huawei's reputation, affecting Huawei's finance or operations, and causing different levels of damage to personal data subjects.

**Parent topic:** [[Stream Processing|Stream Processing]]