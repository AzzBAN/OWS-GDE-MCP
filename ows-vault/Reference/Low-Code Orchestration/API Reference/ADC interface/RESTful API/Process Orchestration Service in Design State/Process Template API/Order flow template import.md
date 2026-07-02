---
title: "Order flow template import"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessTemplateApiService_importPOST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. Interface script invoked by the instance:

var request = {"batchId": "xx","name": "yy"};
var url = "/adc-studio-bpm/rest/v1/process-template/import";
var response = ServiceInvoker.post(url, request);