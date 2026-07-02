---
title: "Querying the Status of All Work Orders"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_parameter_order-status_listPOST.html"
depth: 6
---
#### Function Description

This API starts from GDE 24.2 and is used to query the status of all tickets. The returned status can be running, paused, or canceled.

var request = {};

var url = "/adc-bpm/rest/v1/process/parameter/order-status/list";

var response = ServiceInvoker.post(url, request);