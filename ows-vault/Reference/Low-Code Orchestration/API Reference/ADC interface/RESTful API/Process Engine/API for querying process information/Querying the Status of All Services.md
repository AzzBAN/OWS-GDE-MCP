---
title: "Querying the Status of All Services"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_parameter_business-status_listPOST.html"
depth: 6
---
#### Function Description

This API starts from GDE 24.2 and is used to query the status of all services, including completed, canceled, submitted, to-be-processed, to-be-confirmed, to-do, and termination exception.

var request = {};

var url = "/adc-bpm/rest/v1/process/parameter/business-status/list";

var response = ServiceInvoker.post(url, request);