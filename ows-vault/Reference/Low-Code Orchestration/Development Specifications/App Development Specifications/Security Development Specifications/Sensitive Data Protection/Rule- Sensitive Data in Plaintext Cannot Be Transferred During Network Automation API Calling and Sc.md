---
title: "Rule: Sensitive Data in Plaintext Cannot Be Transferred During Network Automation API Calling and Script Execution"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804184.html"
depth: 5
---
# Rule: Sensitive Data in Plaintext Cannot Be Transferred During Network Automation API Calling and Script Execution

**Description**: The network automation module records logs for received command requests and command outputs. The logs are stored in plaintext. Therefore, plaintext sensitive data cannot be transferred during network automation API calling, and commands involving sensitive data cannot be executed based on the network automation module.

**Check guide**: Check whether the parameters for calling network automation APIs contain sensitive data. For example, check whether the parameters contain sensitive fields when the API process calls the network automation command.

![[en-us_image_0000001470283158.png]]

Check whether the command output contains sensitive data.

![[en-us_image_0000001147372531.png]]

**Tool supported or not**: no

**Specification name**: Security\_SensitiveData\_MCP\_NotTransferByInterface

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: network automation orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]