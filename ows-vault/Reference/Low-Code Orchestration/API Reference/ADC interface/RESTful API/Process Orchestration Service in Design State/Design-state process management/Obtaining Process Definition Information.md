---
title: "Obtaining Process Definition Information"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546364577.html"
depth: 6
---
#### Function

It starts with GDE 24.2, Interface script invoked by the instance: var url = "/adc-studio-bpm/cse/rest/v1/process-designer/get?project\_name = test1&module\_name = test1&name = flow1"; var response = ServiceInvoker.post(url, request);. This API is used to query process definition information based on the project name, module name, and process name. It is applicable to process configuration management scenarios.