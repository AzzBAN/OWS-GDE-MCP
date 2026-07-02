---
title: "Transferring a Work Order to Another Work Order Processor"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_UnifiedOrderOperationApiService_app_name_module_name_process_name_transferPOST.html"
depth: 6
---
#### Function Description

This API starts from GDE 24.2 and is used to query basic ticket information based on the app name, module name, process name, and ticket ID.

var request = {

"assign\_to": "user:test",

"task\_id": "0000000021f0f11a03-3f6b-e330-fd41-af0bb1705e71",

"reason": "test",

"message\_type": \["SMS"\]

};

var url = "/adc-bpm/rest/v1/unified/order/test\_app/test\_module/test\_process/transfer";

var response = ServiceInvoker.post(url, request);

You can use the /adc-bpm/rest/v1/unified/order/{app\_name}/{module\_name}/{process\_name}/{order\_id}/processing-task-info API to obtain the task ID.