---
title: "Querying Associated Attachments"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderAttachmentApiService_queryPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. The following is an example of the interface invoking script:

var request = {
    "start": 0,
    "limit": 10,
    "sort": "",
    "dir": "DESC",
    "condition": {
    "order\_id": "quxw-20221128-00000001",
    "is\_archived": false
    }
}
var url = "/adc-bpm/rest/v1/order/attachment/query";
var response = ServiceInvoker.post(url, request);