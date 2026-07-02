---
title: "Create an automatic process ticket based on parameters such as the ticket title and creator."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_UnifiedOrderOperationApiService_app_name_module_name_process_name_api-order_createPOST.html"
depth: 6
---
#### Function Description

Start with GDE 25.0, Interface script invoked by the instance:

var request = {

"title":"test",

"parent\_order\_id":"id-00000-00000",

"form\_data":{}

};

var url = /adc-bpm/rest/v1/unified/order/{app\_name}/{module\_name}/{process\_name}/api-order/create";

var response = ServiceInvoker.post(url, request);