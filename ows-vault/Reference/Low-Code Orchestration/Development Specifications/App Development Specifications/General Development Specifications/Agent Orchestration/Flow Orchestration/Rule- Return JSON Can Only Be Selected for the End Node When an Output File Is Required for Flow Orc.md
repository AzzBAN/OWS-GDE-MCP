---
title: "Rule: Return JSON Can Only Be Selected for the End Node When an Output File Is Required for Flow Orchestration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002343774101.html"
depth: 6
---
# Rule: Return JSON Can Only Be Selected for the End Node When an Output File Is Required for Flow Orchestration

**Description**: The agent flow provides the file upload and download capabilities. If files need to be downloaded in an agent session, **Message Return Type** of the End node must be set to **Return JSON**.

**Check guide**: Check the agent workflow orchestration canvas and check whether the selected process service involves file download. If so, **Message Return Type** of the End node can only be set to **Return JSON**.

![[en-us_image_0000002403721433.png]]

**Tool supported or not**: no

**Specification name**: General\_Agent\_WorkFlow\_File\_DownLoad

**Severity**: minor

**Parent topic:** [[Flow Orchestration|Flow Orchestration]]