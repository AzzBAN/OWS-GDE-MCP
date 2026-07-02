---
title: "Send a message based on the specified message type to urge the processor to process the work order."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_UnifiedOrderOperationApiService_app_name_module_name_process_name_urgePOST.html"
depth: 6
---
#### Function Description

Starting from GDE 24.2, Interface script invoked by the instance:

var request = {

"order\_id": "ID\_456\_1594175397300",

"description": "test",

"message\_type": \["SMS"\]

};

var url = "/adc-bpm/rest/v1/unified/order/test\_app/test\_module/test\_process/urge";

var response = ServiceInvoker.post(url, request);