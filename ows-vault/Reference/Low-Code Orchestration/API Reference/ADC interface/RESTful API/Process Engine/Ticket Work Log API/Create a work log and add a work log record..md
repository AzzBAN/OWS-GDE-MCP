---
title: "Create a work log and add a work log record."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_WorkLogApiService_createPOST.html"
depth: 6
---
#### Function

Start with GDE 24.2, // Interface script invoked by the instance:

var request = {

"type\_id": "WorkLogTypeCheckStatus",

"synchronize\_id": "false",

"description": "quxw",

"operation\_type": "Manual",

"attachment": "eyJleHBpcmVUaW1lIjoxNjY5N==",

"order\_id": "quxw-20221128-00000001",

"app\_name": "quxw",

"module\_name": "bpm",

"rich\_description": "quxw",

"attachment\_id": "install-log.zip"

}

var url = "/adc-bpm/rest/v1/order/worklog/create";

var response = ServiceInvoker.post(url, request);