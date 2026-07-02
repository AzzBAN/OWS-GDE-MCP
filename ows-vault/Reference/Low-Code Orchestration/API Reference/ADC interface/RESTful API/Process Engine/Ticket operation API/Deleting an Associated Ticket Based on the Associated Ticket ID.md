---
title: "Deleting an Associated Ticket Based on the Associated Ticket ID"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_dissociatePOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, // Interface script invoked by the instance:

var request = {

"ids": "03894a427e4ac884d583c19e01a1f8,03894a427e4ac884d583c19e01a1f9"

}

var url = "/adc-bpm/rest/v1/order/dissociate";

var response = ServiceInvoker.post(url, request);