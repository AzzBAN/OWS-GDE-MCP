---
title: "Query details about the batch processing logs of associated tickets based on the log ID."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_batch-process-log_logId_GET.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, // Interface script invoked by the instance:

var request = {}

var url = "/adc-bpm/rest/v1/order/batch-process-log/{logId}";

var response = ServiceInvoker.post(url, request);