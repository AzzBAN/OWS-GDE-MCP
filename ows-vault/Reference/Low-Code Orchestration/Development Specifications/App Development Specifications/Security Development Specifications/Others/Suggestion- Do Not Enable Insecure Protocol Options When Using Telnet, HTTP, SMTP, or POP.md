---
title: "Suggestion: Do Not Enable Insecure Protocol Options When Using Telnet, HTTP, SMTP, or POP"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002370571444.html"
depth: 5
---
# Suggestion: Do Not Enable Insecure Protocol Options When Using Telnet, HTTP, SMTP, or POP

**Description**: During RPA script orchestration, scenarios where the system interacts with external systems through network protocols exist. Insecure protocols such as Telnet and HTTP cannot be used, and secure protocols such as SSH and HTTPS should be preferentially used.

**Check guide**: Check whether insecure protocols are used in controls such as Console.login, smtp.sendemail, pop.getemail, and database.connect.

**Positive example**: none

**Tool supported or not**: no

**Specification name**: General\_RPA\_Use\_Secure\_Connection\_Protocol

**Severity**: suggestion

**Orchestration scenario**: RPA orchestration

**Parent topic:** [[Others|Others]]