---
title: "Deleting a Flow from a Specified Flow List"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessManageApiService_instances_project_name_module_name_process_name_POST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. Interface script invoked by the instance:

var request = {
"project\_name": "test\_project",
"module\_name": "test\_module",
"process\_name": \["test\_process\_a", "test\_process\_b"\]
};
var url = "/adc-studio-bpm/rest/v1/process-manage/instances/test\_project/test\_module/test\_process\_a";
var response = ServiceInvoker.post(url, request);