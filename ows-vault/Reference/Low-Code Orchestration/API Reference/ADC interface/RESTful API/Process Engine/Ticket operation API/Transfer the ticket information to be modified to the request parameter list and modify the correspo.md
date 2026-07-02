---
title: "Transfer the ticket information to be modified to the request parameter list and modify the corresponding items in the ticket information."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_modifyPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"order\_id":"id-1234-4567",

"task\_id":"12354-abcd-efgh",

"operator":"test\_operator",

"order\_status":"running",

"form\_data":{

"title":"test\_456"

},

"results":{

"results":true

}

};

var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/modify";

var response = ServiceInvoker.post(url, request);