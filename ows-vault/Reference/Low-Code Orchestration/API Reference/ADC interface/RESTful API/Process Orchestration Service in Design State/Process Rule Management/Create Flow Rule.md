---
title: "Create Flow Rule"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002514764722.html"
depth: 6
---
#### Function Description

Create a process rule to define the triggering conditions and actions during process execution. Starts with GDE 24.2, Interface script invoked by the instance: var request = { "action\_parameters": "{"messageType":"Email,SMS","messageRecipient":"creator,last\_updater","specifiedRecipient":"","emailCcRecipient":"","emailBccRecipient":"","cycle":"no","recursion":"no","messageTitle":"test11","messageSimpleContent":"test11","messageRichContent":"","contentType":"simple","delay":"no","delayMinutes":"","autoEscalate":"no","repeatInterval":"","repeatCount":"","escalateLevel":"","recordToWorkLog":"","emailServerId":"","smsGatewayId":"","smsSrc":""}", "module\_name": "test1", "active": true, "project\_name": "test1", "activity\_id": "TT10", "rule\_name": "test3", "process\_key": "flow1"}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/process-rule/create", request).