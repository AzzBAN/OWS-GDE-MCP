---
title: "Query process rules."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546444583.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance:var request = { "start":0, "limit":10, "sort":"ruleName", "dir":"DESC", "condition":{ "project\_name":"test1", "module\_name":"test1", "process\_key":"flow1", "activity\_id":"TT10", "active":true, "rule\_name":""}}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/process-rule/query", request);.