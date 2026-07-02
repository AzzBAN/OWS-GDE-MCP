---
title: "Suspending a ticket"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationV2ApiService_app_name_module_name_process_name_suspendPOST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. This interface is used to suspend a ticket. The difference between this interface and the interface of the V1 version is that the interface of the V2 version verifies the permission.

Interface script invoked by the instance:

var request = {
"order\_id": "test1-20201215-00000007",
"suspend\_time": "2021-02-22 09:43:22",
"resume\_time": "2021-02-24 09:43:22",
"reason": "test reason",
"description": "test description",
"operator": "admin"
};
var url = "/adc-bpm/rest/v2/order/test\_app/test\_module/test\_process/suspend";
var response = ServiceInvoker.post(url, request);