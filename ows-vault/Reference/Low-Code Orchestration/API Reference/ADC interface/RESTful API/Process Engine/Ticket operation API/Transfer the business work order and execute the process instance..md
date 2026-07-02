---
title: "Transfer the business work order and execute the process instance."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_processPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"task\_id":"1234-3456-qwer",

"order\_id":"id-1234-edff",

"operator":"test\_operator",

"title":"test\_123",

"form\_data":{}

};

var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/process";

var response = ServiceInvoker.post(url, request);