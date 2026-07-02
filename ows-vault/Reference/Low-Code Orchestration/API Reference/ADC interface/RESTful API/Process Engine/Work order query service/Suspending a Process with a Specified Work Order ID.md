---
title: "Suspending a Process with a Specified Work Order ID"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ApiOrderApiService_api-order_app_name_module_name_process_name_suspendPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. Interface script invoked by the instance:

var request = {

"operator": "test\_user",

"order\_id": "test\_order\_01"

};

var url = "/adc-bpm/rest/v1/order/api-order/test\_app/test\_module/test\_process/suspend";

var response = ServiceInvoker.post(url, request);