---
title: "Create a service ticket based on the parameter values in the request parameter list. (If the first phase is a manual task, the ticket is automatically transferred to this phase.)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_createPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"title":"test\_123",

"creator":"user:admin",

"task\_id":"000123-abcd-00012345",

"process\_id":"1234-2345-3456",

"ticket\_id":"0000-1234-2345",

"create\_date":"2022-10-01 04:12:59",

"parent\_order\_id":"id-00000-00000",

"order\_status":"running",

"process\_type":"",

"next\_tasks":\[

{

"task\_id":"12505"

},

\],

"form\_data":{},

"results":{

"results":true

}

};

var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/create";

var response = ServiceInvoker.post(url, request);