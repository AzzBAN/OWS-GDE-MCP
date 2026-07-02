---
title: "Rule: Password Box Must Be Selected for Sensitive Data During the Custom Data Source Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404051241.html"
depth: 5
---
# Rule: Password Box Must Be Selected for Sensitive Data During the Custom Data Source Configuration

**Description**: When creating a custom data source type, you need to select **Password Box** in the **Control Type** column during the configuration of sensitive data.

**Check guide**: Check all custom data source types and ensure that **Password Box** is selected in the **Control Type** column for sensitive data.

**Positive example**:

![[en-us_image_0000001721908469.png]]

**Negative example**: When a custom data source type is created, if a value other than **Password Box** is selected in the **Control Type** column for sensitive data, the password is displayed in plaintext instead of being encrypted when another parameter is added.

![[en-us_image_0000001673888670.png]]

![[en-us_image_0000001721933801.png]]

**Tool supported or not**: no

**Specification name**: Security\_SensitiveData\_Not\_StoreByPasswordType

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: data orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]