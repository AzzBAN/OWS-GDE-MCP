---
title: "Query multi-instance condition information."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546444581.html"
depth: 6
---
#### Function

Starts with GDE 24.2, Interface script invoked by the instance:var request = { "start":0, "limit":10, "sort":"title", "dir":"DESC", "condition":{ "project\_name":"aaa", "module\_name":"aaa", "process\_key":"flow1", "activity\_id":"TT10", "active":true, "title":"test"}}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/multitask-condition/query", request).