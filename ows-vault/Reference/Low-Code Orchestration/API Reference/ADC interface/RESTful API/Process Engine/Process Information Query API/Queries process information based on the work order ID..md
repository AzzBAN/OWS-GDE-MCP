---
title: "Queries process information based on the work order ID."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_UnifiedProcessDefinitionQueryApiService_query-by-orderidPOST.html"
depth: 6
---
#### Function

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"order\_id": "test-order-id"

};

var url = "/adc-bpm/rest/v1/process/definition/query-by-order-id";

var response = ServiceInvoker.post(url, request);