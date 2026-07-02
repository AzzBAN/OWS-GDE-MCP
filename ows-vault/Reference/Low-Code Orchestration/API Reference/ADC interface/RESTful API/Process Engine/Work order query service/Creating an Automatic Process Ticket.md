---
title: "Creating an Automatic Process Ticket"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ApiOrderApiService_api-order_app_name_module_name_process_name_startPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. Create an automatic process ticket based on parameters such as the ticket title and creator.

Interface script invoked by the instance:

var request = {

"creator": "test\_user",

"title": "test",

"form\_data": {}

};

var url = "/adc-bpm/rest/v1/order/api-order/test\_app/test\_module/test\_process/start";

var response = ServiceInvoker.post(url, request);