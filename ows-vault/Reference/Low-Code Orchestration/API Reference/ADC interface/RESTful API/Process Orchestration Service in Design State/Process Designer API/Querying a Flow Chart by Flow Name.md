---
title: "Querying a Flow Chart by Flow Name"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessDesignerApiService_editor_modelPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. Returns the flowchart information based on the process name, including the nodes in the flowchart and the connection relationships between nodes.

Interface script invoked by the instance:

var request = {
"project\_name": "test\_project",
"module\_name": "test\_module",
"process\_name": "test\_process"
};
var url = "/adc-studio-bpm/rest/v1/process-designer/editor/model";
var response = ServiceInvoker.post(url, request);