---
title: "Rule: Translators Must Be Used to Encrypt Service Input Parameters That Contain Sensitive Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208599067.html"
depth: 5
---
# Rule: Translators Must Be Used to Encrypt Service Input Parameters That Contain Sensitive Data

**Description**: Plaintext storage of sensitive data may lead to improper data disclosure and customer doubts. Plaintext storage of sensitive personal data may even lead to regulatory penalties. GDE provides translators to encrypt and decrypt data using AESEncrypt and AESDecrpt, ensuring that sensitive data is stored in ciphertext.

Note: You are advised to use the **Password** field to define properties. Translators are not recommended.

**Check guide**: Go to the develop-state environment, select the app to be checked, select the corresponding service, and check whether the translator that contains sensitive data is configured in the **Input Configuration** area.

**Positive example**:

The page for creating or editing a service is displayed. You can select a service that contains sensitive data in the **Input Configuration** or **Output Configuration** area, and click the plus sign (+) in the **Translator** column to select a translator.

![[en-us_image_0000001522078705.png]]

Set **Translation Mode** to **General Configuration**, **Mapping Type** to **Common functions**, and **Name** to **aesEncrypt()** or **aesDecrypt()**, as shown in the following figure.

![[en-us_image_0000001522397829.png]]

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_Not\_UsePasswordTranslate

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: UI orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]