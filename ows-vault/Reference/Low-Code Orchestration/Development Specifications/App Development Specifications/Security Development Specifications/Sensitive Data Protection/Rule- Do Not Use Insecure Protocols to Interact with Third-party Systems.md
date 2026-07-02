---
title: "Rule: Do Not Use Insecure Protocols to Interact with Third-party Systems"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403965.html"
depth: 5
---
# Rule: Do Not Use Insecure Protocols to Interact with Third-party Systems

**Description**: During RPA script orchestration, scenarios where the system interacts with external systems through network protocols exist. Insecure protocols, such as Telnet, HTTP, POP3, and SMTP, cannot be used, and secure protocols, such as SSH V2, HTTPS, TLS 1.2, and TLS 1.3, should be preferentially used.

**Check guide**: Check whether insecure protocols are used in controls such as Console.login, smtp.sendemail, pop.getemail, and database.connect.

**Positive example**:

![[en-us_image_0000001816750085.png]]

**Negative example**:

![[en-us_image_0000001769916480.png]]

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_RPA\_InsecureProtocol

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: RPA orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]