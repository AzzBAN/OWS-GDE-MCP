---
title: "Check whether the current user has the permission to create tickets."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_CustomizedOrcValidateService_createPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. Interface script invoked by the instance:

var request = {};
var url = "/adc-bpm/rest/v1/order/orc-service-control/access-check/create";
var response = ServiceInvoker.post(url, request);