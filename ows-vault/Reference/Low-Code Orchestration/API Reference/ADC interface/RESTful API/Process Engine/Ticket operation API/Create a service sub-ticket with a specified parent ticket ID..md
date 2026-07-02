---
title: "Create a service sub-ticket with a specified parent ticket ID."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_create-sub-orderPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"title":"test\_123",

"operator":"test\_operator",

"sub\_order\_app\_name":"test\_sub\_app",

"sub\_order\_module\_name":"test\_sub\_module",

"sub\_order\_process\_name":"test\_sub\_process",

"parent\_order\_id":"par-20230725-00000001",

"app\_name":"test\_parent\_app",

"module\_name":"test\_parent\_module",

"process\_name":"test\_parent\_process",

"create\_date":"2022-08-12 12:04:34"

};

var url = "/adc-bpm/rest/v1/order/test\_parent\_app/test\_parent\_module/test\_parent\_process/create-sub-order";

var response = ServiceInvoker.post(url, request);