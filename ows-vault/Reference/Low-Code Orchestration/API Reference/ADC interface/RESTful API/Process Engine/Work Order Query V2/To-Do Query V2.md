---
title: "To-Do Query V2"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_CommonQueryPublicV2Service_pending-for-mePOST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. To-do query, which is used to extend the to-do query interface of the v1 version. To-do information can be queried based on the process list.

Interface script invoked by the instance:

var request = {
"start":0,
"limit":10,
"condition":{
"current\_user":"test",
"order\_id":""
}
};
var url = "/adc-bpm/rest/v2/order/pending-for-me";
var response = ServiceInvoker.post(url, request);