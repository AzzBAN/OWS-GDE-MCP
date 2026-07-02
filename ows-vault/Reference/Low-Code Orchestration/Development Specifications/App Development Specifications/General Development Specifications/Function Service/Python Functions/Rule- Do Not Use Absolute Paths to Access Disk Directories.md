---
title: "Rule: Do Not Use Absolute Paths to Access Disk Directories"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001663787233.html"
depth: 6
---
# Rule: Do Not Use Absolute Paths to Access Disk Directories

**Description**: Due to the security mechanism, absolute paths cannot be used to access disk directories. The **FileInvoker.get\_tmp\_file** method is used to create temporary files, and the **FileInvoker.read\_code\_file** method is used to read code and configuration information.

**Tool supported or not**: no

**Specification name**: General\_FaaS\_Forbidden\_Use\_Absolute\_Path

**Severity**: minor

**Parent topic:** [[Python Functions|Python Functions]]