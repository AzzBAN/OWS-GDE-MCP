---
title: "Returns the flowchart information based on the process name."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_editor_modelPOST.html"
depth: 6
---
#### Function Description

Returns the flowchart information based on the process name, including the nodes in the flowchart and the connections between nodes. This function starts with GDE 24.2.

var request = {

"app\_name": "test\_app",

"module\_name": "test\_module",

"process\_name": "test\_process"

};

var url = "/adc-bpm/rest/v1/process/editor/model";

var response = ServiceInvoker.post(url, request);