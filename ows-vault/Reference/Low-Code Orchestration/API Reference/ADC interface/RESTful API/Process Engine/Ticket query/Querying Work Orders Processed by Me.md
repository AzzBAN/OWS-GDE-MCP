---
title: "Querying Work Orders Processed by Me"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_CommonQueryPublicService_processed-by-mePOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. This interface is used to query processed work orders. You can search for work orders based on specified conditions. If no condition is specified, all processed work orders are returned.

Interface script invoked by the instance:

var request = {
"start":0,
"limit":10,
"condition":{
"current\_user":"test",
"order\_id":""
}
};
var url = "/adc-bpm/rest/v1/order/processed-by-me";
var response = ServiceInvoker.post(url, request);