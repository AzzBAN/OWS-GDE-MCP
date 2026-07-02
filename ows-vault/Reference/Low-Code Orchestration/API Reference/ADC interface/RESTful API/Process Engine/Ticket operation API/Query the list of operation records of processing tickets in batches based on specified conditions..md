---
title: "Query the list of operation records of processing tickets in batches based on specified conditions."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_batch-process-log_listPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, // Interface script invoked by the instance:

var request = {

"start": 0,

"limit": 10,

"sort": "",

"dir": "DESC",

"condition": {

"batch\_operate\_id": "test",

"order\_id": "test",

"operate\_result": "Success"

}

}

var url = "/adc-bpm/rest/v1/order/batch-process-log/list";

var response = ServiceInvoker.post(url, request);