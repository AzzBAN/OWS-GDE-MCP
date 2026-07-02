---
title: "Transferring a Work Order to Another Work Order Handler"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_transferPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"order\_id": "test1-20201215-00000007",

"transfer\_to": "user:test",

"task\_id": "0000000021f0f11a03-3f6b-e330-fd41-af0bb1705e71",

"reason": "test",

"operator": "test",

"message\_type": \["SMS"\]

};

var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/transfer";

var response = ServiceInvoker.post(url, request);

You can use the /adc-bpm/rest/v1/order/{app\_name}/{module\_name}/{process\_name}/{order\_id}/processing-task-info API to obtain the task ID.