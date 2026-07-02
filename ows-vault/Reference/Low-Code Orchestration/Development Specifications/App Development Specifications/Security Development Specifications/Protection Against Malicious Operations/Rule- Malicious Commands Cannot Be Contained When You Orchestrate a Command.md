---
title: "Rule: Malicious Commands Cannot Be Contained When You Orchestrate a Command"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162959142.html"
depth: 5
---
# Rule: Malicious Commands Cannot Be Contained When You Orchestrate a Command

**Description**: When you create a command set, do not use malicious commands, regardless of whether the command set is created using a script or is directly created. Otherwise, an alarm will be generated. When an alarm is generated, the developer needs to confirm the alarm and modify the command set.

**Malicious command source**: A malicious command is one that contains preset data, such as reboot, reset, delete, remove, del, rmv, rst, deactive, or dact. In addition, a malicious command can be customized by the service team.

**Check guide**: In the develop-state environment, click **Project Quality Assessment** on the **Project Management** page to check the project quality.

**Tool supported or not**: yes

**Specification name**: Security\_MaliciousOperations\_Forbid\_MCP\_DaggerCommand

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: network automation orchestration

**Parent topic:** [[Protection Against Malicious Operations|Protection Against Malicious Operations]]