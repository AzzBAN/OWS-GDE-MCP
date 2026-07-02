---
title: "Cancels a ticket and sends an SMS message or email to the handler. (Only tickets in the running state can be canceled.)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_cancelPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"operator": "test",

"creator": "userName",

"reason": "reason",

"order\_id": "orderID",

"description": "test",

};

var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/cancel";

var response = ServiceInvoker.post(url, request);