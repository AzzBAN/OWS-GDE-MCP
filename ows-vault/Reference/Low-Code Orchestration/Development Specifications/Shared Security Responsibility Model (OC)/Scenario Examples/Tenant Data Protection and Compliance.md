---
title: "Tenant Data Protection and Compliance"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001104369704.html"
depth: 4
---
# Tenant Data Protection and Compliance

1\. GDE allows the tenant administrator to configure the anonymization policy to meet data protection and compliance requirements.

Scenario 1: The tenant administrator does not configure the anonymization policy or the configuration is incorrect. Personal data is not anonymized, leading to privacy violations.

In this case, the tenant administrator should analyze privacy compliance risks and configure the anonymization policy based on local compliance requirements. Otherwise, the tenant administrator takes full responsibility for the issue that occurred.

Scenario 2: The tenant administrator correctly configures the anonymization policy, but personal data is still stored or displayed in plaintext, leading to privacy violations.

In this case, GDE is responsible for not properly implementing system functions.

2\. GDE allows the tenant administrator to configure the data access permission to meet data protection and compliance requirements.

Scenario 1: The tenant administrator does not properly configure the data access permission. Common users have excessive data access permissions, leading to data leakage.

The tenant takes the responsibility and the tenant administrator should configure the permission based on the minimum permission principle. The tenant is responsible for the issue caused by improper configuration.

Scenario 2: The tenant administrator correctly configures the data access permission, and the common user role and permission are correctly configured. However, the user accesses unauthorized data, leading to data leakage.

In this case, GDE takes the full responsibility for the issue that occurs after the tenant administrator correctly configures the permission.

**Parent topic:** [[Scenario Examples|Scenario Examples]]