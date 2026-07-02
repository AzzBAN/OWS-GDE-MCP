---
title: "Resuming a Work Order (V2)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationV2ApiService_app_name_module_name_process_name_resumePOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. This interface is used to resume a work order. The difference between the V2 interface and the V1 interface is that the V2 interface verifies the permission.

Interface script invoked by the instance:

var request = {
"order\_id": "test1-20201215-00000007",
"resume\_time": "2021-02-24 09:43:22",
"description": "test description",
"operator": "admin"
};
var url = "/adc-bpm/rest/v2/order/test\_app/test\_module/test\_process/resume";
var response = ServiceInvoker.post(url, request);