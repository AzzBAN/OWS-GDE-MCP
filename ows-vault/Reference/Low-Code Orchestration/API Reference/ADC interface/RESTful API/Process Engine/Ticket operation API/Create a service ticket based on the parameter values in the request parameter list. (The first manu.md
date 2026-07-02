---
title: "Create a service ticket based on the parameter values in the request parameter list. (The first manual task node of the ticket is not automatically transferred.)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_startPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"title":"test\_123",

"process\_name":"test\_process",

"parent\_order\_id":"abbre-20230101-00001",

"app\_name":"test\_app",

"module\_name":"test\_module",

"text\_input":"form\_data\_example\_1"

}

var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/start";

var response = ServiceInvoker.post(url, request);