---
title: "Cancels a work order and sends an SMS or email to the processor. (Only work orders in the running state can be canceled.)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_UnifiedOrderOperationApiService_app_name_module_name_process_name_cancelPOST.html"
depth: 6
---
#### Function Description

Starting from GDE 24.2, Interface script invoked by the instance:

var request = {

"operator": "test",

"creator": "userName",

"reason": "reason",

"order\_id": "ID\_456\_1594175397300",

"reason": "test",

"description": "test",

"operator": "test"

};

var url = "/adc-bpm/rest/v1/unified/order/test\_app/test\_module/test\_process/cancel";

var response = ServiceInvoker.post(url, request);