---
title: "Recall Process"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ApiOrderApiService_api-order_app_name_module_name_process_name_recallPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. In the recall process, some phases are canceled based on the activity ID and the specified target phases are executed.

Interface script invoked by the instance:

var request = {

"order\_id": "id-20220922-00000001",

"target\_act\_ids": "TT12",

"cancel\_act\_ids": TT11"

};

var url = "/adc-bpm/rest/v1/order/api-order/test\_app/test\_module/test\_process/recall";

var response = ServiceInvoker.post(url, request);