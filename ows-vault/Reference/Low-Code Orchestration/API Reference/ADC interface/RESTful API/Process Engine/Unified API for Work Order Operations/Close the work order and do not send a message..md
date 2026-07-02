---
title: "Close the work order and do not send a message."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_UnifiedOrderOperationApiService_app_name_module_name_process_name_closePOST.html"
depth: 6
---
#### Function Description

Starting from GDE 24.2, Interface script invoked by the instance:

var request = {

"order\_id": "test1-20201215-00000007",

"reason": "test",

"operator": "test\_operator"

};

var url = "/adc-bpm/rest/v1/unified/order/test\_app/test\_module/test\_process/close";

var response = ServiceInvoker.post(url, request);