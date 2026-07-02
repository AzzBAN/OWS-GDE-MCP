---
title: "Queries process information based on the process ID."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_UnifiedProcessDefinitionQueryApiService_query-by-processkeyPOST.html"
depth: 6
---
#### Function

It starts from GDE 24.2, Interface script invoked by the instance:var request = {"process\_key": "test-process\_key"};var url = "/adc-bpm/rest/v1/process/definition/query-by-processkey";var response = ServiceInvoker.post(url, request).