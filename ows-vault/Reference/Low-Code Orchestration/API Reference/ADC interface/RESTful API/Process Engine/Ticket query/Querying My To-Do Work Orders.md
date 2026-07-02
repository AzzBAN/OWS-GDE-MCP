---
title: "Querying My To-Do Work Orders"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_CommonQueryPublicService_pending-for-mePOST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. This interface is used to query tickets in My To-Dos. You can search for tickets based on specified conditions. If no condition is specified, all tickets to be processed are returned.

Interface script invoked by the instance:

var request = {
"start":0,
"limit":10,
"condition":{
"current\_user":"test",
"order\_id":""
}
};
var url = "/adc-bpm/rest/v1/order/pending-for-me";
var response = ServiceInvoker.post(url, request);