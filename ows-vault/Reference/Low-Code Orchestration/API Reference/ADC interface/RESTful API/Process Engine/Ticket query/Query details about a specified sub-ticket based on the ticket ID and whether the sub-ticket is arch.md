---
title: "Query details about a specified sub-ticket based on the ticket ID and whether the sub-ticket is archived."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_CommonQueryPublicService_sub-order_queryPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. Query details about a specified sub-ticket based on the ticket ID and whether the sub-ticket is archived.

Interface script invoked by the instance:

var request = 
{
	"order\_id":"INC-20221111-00000003"
};
var url = "/adc-bpm/rest/v1/order/sub-order/query";
var response = ServiceInvoker.post(url, request);