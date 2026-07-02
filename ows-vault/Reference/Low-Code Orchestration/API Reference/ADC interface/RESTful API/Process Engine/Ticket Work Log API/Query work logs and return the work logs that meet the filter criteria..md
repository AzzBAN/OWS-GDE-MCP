---
title: "Query work logs and return the work logs that meet the filter criteria."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_WorkLogApiService_queryPOST.html"
depth: 6
---
#### Function Description

This API starts with GDE 24.2 and is used to query work logs. Work logs that meet the filter criteria are returned.

var request = {

"start": 0,

"limit": 10,

"sort": "",

"dir": "DESC",

"condition": {

"order\_id": "quxw-20221128-00000001",

"is\_archived": false,

"work\_log\_id": "dc037176-6f85-11ed-8487-0255ac1200a8",

"description": "quxw",

"creator\_name": \["admin"\],

"record\_time\_start": "2022-11-29 09:42:01",

"record\_time\_end": "2022-11-29 09:42:10",

"operation\_type": "Manual"

}

}

var url = "/adc-bpm/rest/v1/order/worklog/query";

var response = ServiceInvoker.post(url, request);