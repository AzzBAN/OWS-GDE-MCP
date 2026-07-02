---
title: "General Query of Work Orders"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_CommonQueryPublicService_common-queryPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. You can search for tickets based on specified conditions. If no condition is specified, parameters such as the ticket ID, creator, and creation time of all tickets are returned.

Interface script invoked by the instance:

var request = {
"start":0,
"limit":10,
"condition":{
"order\_id":""
}
};
var url = "/adc-bpm/rest/v1/order/common-query";
var response = ServiceInvoker.post(url, request);