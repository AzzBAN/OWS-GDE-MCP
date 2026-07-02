---
title: "Update a process rule."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546364575.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance: var request = {"proc\_rule\_id":"2c928036964bf85e01964bfc09ae0008","action\_parameters": "{"messageType":"Email,SMS","messageRecipient":"creator,last\_updater","specifiedRecipient":"","emailCcRecipient":"","emailBccRecipient":"","cycle":"no","recursion":"no","messageTitle":"test11","messageSimpleContent":"test11","messageRichContent":"","contentType":"simple","delay":"no","delayMinutes":"","autoEscalate":"no","repeatInterval":"","repeatCount":"","escalateLevel":"","recordToWorkLog":"","emailServerId":"","smsGatewayId":"","smsSrc":""}","module\_name": "abc","active": false,"project\_name": "abc","activity\_id": "TT10","rule\_name": "test3","process\_key": "flow1"}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/process-rule/update", request);.