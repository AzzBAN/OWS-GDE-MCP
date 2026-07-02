---
title: "Rule: Property Type of the Model That Contains Sensitive Data Must Be Set to Password"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208519051.html"
depth: 5
---
# Rule: Property Type of the Model That Contains Sensitive Data Must Be Set to Password

**Description**: Sensitive data such as passwords entered in text boxes cannot be displayed in plaintext or copied. In addition, sensitive data such as keys or passwords must be encrypted for storage. Otherwise, passwords may be disclosed improperly.

**Check guide**: If the model contains sensitive data, check that **Property Type** of that model has been set to **Password**. For details about sensitive data types, see Appendix 1.

**Positive example**:

If the property information is sensitive, set **Property Type** to **Password** and select a password policy based on service requirements. In reversible scenarios, select **AES** for **Password Policy**. In irreversible scenarios, select **SHA256** for **Password Policy**.

![[en-us_image_0000001522394125.png]]

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_Not\_StoreByPasswordType

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: UI orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]