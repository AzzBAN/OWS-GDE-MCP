---
title: "Jump from the current execution phase to the specified target phase."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ApiOrderApiService_api-order_app_name_module_name_process_name_jump-activityPOST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. Interface script invoked by the instance:

var request = {

"execution\_id": "0000123-123456-00000001",

"target\_act\_id": "TT12",

"jump\_variables": {}

};

var url = "/adc-bpm/rest/v1/order/api-order/test\_app/test\_module/test\_process/jump-activity";

var response = ServiceInvoker.post(url, request);