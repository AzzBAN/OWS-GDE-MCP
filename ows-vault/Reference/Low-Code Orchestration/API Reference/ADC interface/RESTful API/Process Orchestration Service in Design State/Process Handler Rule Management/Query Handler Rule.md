---
title: "Query Handler Rule"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546444589.html"
depth: 6
---
#### Function

It starts with GDE 24.2, Interface script invoked by the instance:var request = { "start":0, "limit":10, "sort":"title", "dir":"DESC", "condition":{ "project\_name":"test1", "module\_name":"test1", "process\_key":"flow1", "activity\_id":"TT10", "active":true, "title":""}}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/assignee-rule/query", request);.