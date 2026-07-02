---
title: "Querying Work Order Details by Work Order ID"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_CommonQueryPublicService_order-detailPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. Query ticket details based on order\_id or order\_id and my\_task\_id. The creation time, creator, ticket level, and update time are returned.

Interface script invoked by the instance:

var request = {
"order\_id":"id-20220922-00000001",
"my\_task\_id":"000000000603edb4f5-8e30-5898-ccf9-b774595c5e47"
};
var url = "/adc-bpm/rest/v1/order/order-detail";
var response = ServiceInvoker.post(url, request);