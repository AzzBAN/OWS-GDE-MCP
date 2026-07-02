---
title: "Rule: Do Not Return Sensitive Data to the Frontend in Any Way"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403961.html"
depth: 5
---
# Rule: Do Not Return Sensitive Data to the Frontend in Any Way

**Description**: The storage, transmission, and processing of sensitive data must comply with applicable local laws and regulations, and data security must be guaranteed during these operations.

For details about sensitive data types, see Appendix 1.

**Check guide**: Log in to the develop-state environment, select the app to be checked, and check the page and backend code one by one to ensure that no plaintext sensitive data is received by the frontend and displayed on the page.

**Typical error scenarios**:

-   During human-machine API calling, if the API output configuration is set with the AESDecrypt() decryption translator, the API automatically decrypts and returns plaintext sensitive data (such as database and system passwords).
-   During runtime-state service debugging, if no anonymization policy is configured for sensitive fields of the service, plaintext sensitive data is returned during service debugging. For details about the development guide, see [Rule: Anonymization Policy Must Be Configured for Service Output Parameters That Contain Sensitive Information](../nottoctopics/en-us_topic_0000002404034349.html).

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_Response\_Message

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: all

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]