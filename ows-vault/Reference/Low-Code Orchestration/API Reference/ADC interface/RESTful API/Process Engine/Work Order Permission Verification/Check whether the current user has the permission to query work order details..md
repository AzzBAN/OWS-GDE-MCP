---
title: "Check whether the current user has the permission to query work order details."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_CustomizedOrcValidateService_order-detail-queryPOST.html"
depth: 6
---
#### Function description

It starts with GDE24.2. Interface script invoked by the instance:

var request = {};
var url = "/adc-bpm/rest/v1/order/orc-service-control/access-check/order-detail-query";
var response = ServiceInvoker.post(url, request);