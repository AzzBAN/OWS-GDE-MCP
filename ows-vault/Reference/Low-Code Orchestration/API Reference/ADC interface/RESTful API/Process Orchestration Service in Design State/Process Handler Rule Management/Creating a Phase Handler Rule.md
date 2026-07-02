---
title: "Creating a Phase Handler Rule"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546364581.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance: var request = {"activity\_id": "TT11", "active": true, "process\_key": "flow1", "module\_name": "test1", "project\_name": "test1", "rule\_condition": "", "processor": "creator", "specified\_cc\_processor": "user:admin", "specified\_processor": "user:admin", "title": "test1", "cc\_processor": "creator"}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/assignee-rule/create", request);.