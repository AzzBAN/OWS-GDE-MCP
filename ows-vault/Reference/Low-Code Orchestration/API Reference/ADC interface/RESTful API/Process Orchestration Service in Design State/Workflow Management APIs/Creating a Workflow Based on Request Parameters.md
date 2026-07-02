---
title: "Creating a Workflow Based on Request Parameters"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessManageApiService_instance_createPOST.html"
depth: 6
---
#### Function description

It starts with GDE24.2. Create a workflow based on the request parameters.

Interface script invoked by the instance:

var request = {
"process\_name": "test\_process",
"auto\_process": "yes",
"display\_name": "test\_process",
"open\_level": "private",
"abbreviation": "tp",
"project\_name": "test\_project",
"data\_model\_name": "test",
"module\_name": "test\_module"
};
var url = "/adc-studio-bpm/rest/v1/process-manage/instance/create";
var response = ServiceInvoker.post(url, request);