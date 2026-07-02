---
title: "Create a ticket operation log based on the log information in the request parameter list."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_operation-log_createPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"operation\_type": "accept",

"order\_id": "test1-20201215-00000007",

"operator": "test\_operator"

"log\_detail": "",

};

var url = "/adc-bpm/rest/v1/order/operation-log/create";

var response = ServiceInvoker.post(url, request);