---
title: "Rule: Sensitive Data on the Target Network Cannot Be Queried and Operated Using Ansible, MML, or SSH"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523505.html"
depth: 5
---
# Rule: Sensitive Data on the Target Network Cannot Be Queried and Operated Using Ansible, MML, or SSH

**Description**: During the execution of technical operation tasks, all commands executed through an Ansible, MML, or SSH command activity and command outputs may be stored and displayed in the system. If command parameters or outputs contain sensitive data, sensitive data may be disclosed improperly. Therefore, you cannot query and operate sensitive data in such activities.

**Check guide**: Check whether Ansible, MML, and SSH commands involve sensitive data query commands.

**Positive example**: none

**Negative example:** The executed commands include commands for querying or operating sensitive data. For example, you can run the following commands to set the password of a device user:

<HUAWEI> system-view
\[~HUAWEI\] aaa
\[~HUAWEI-aaa\] local-user test@test.net password cipher password

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_MCP\_CanNotQueryByScript

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: network automation orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]