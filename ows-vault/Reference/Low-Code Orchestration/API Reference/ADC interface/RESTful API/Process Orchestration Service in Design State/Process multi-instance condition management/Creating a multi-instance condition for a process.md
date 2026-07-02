---
title: "Creating a multi-instance condition for a process"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002514924650.html"
depth: 6
---
#### Function

Starts with GDE 24.2, Interface script invoked by the instance: var request = { "active": true, "activity\_id": "TT10", "module\_name": "test1", "process\_key": "flow1", "title": "test", "rule\_trigger\_condition": "app\_name = '222'", "project\_name": "test1", "task\_condition\_operation": ">", "task\_condition\_threshold": "10", "task\_condition\_type": "Percent", "property\_id": "operation\_mode", "property\_value": "11"}; return ServiceInvoker.post("/adc-studio-bpm/rest/v1/multitask-condition/query", request).