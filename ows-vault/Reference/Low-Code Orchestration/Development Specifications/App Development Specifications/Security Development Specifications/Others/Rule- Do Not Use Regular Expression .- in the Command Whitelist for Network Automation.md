---
title: "Rule: Do Not Use Regular Expression .* in the Command Whitelist for Network Automation"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404131105.html"
depth: 5
---
# Rule: Do Not Use Regular Expression .\* in the Command Whitelist for Network Automation

**Description**: The regular expression in the command whitelist configuration is **.\***, which is too extensive and insecure.

**Check guide**: Check whether the regular expression in the whitelist command configuration is **.\***.

![[en-us_image_0000002352848661.png]]

**Tool supported or not**: no

**Specification name**: General\_MCP\_Command\_Whitelist\_Config\_Regular\_Expression\_Not\_Used\_.\*

**Severity**: minor

**Orchestration scenario**: RPA orchestration

**Parent topic:** [[Others|Others]]