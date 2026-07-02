---
title: "Query process form information based on specified conditions."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_process-form_getPOST.html"
depth: 6
---
#### Function Description

This API starts with GDE 24.2 and is used to query the process form information based on specified conditions, that is, the page form corresponding to the specified phase of the process.

var request = {

"app\_name": "test",

"module\_name": "test",

"process\_key": "test",

"activity\_id": "test",

"activity\_name": "test",

"type": "test"

}

var url = "/adc-bpm/rest/v1/process/process-form/get";

var response = ServiceInvoker.post(url, request);