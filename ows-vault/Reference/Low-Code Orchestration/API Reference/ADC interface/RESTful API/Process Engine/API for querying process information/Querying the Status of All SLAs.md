---
title: "Querying the Status of All SLAs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_parameter_sla-status_listPOST.html"
depth: 6
---
#### Function Description

Query the status of all SLAs starting from GDE 24.2. The status includes normal, timeout, and milestone-exceeding.

var request = {};

var url = "/adc-bpm/rest/v1/process/parameter/sla-status/list";

var response = ServiceInvoker.post(url, request);