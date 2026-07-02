---
title: "Updating the Work Logs of a Specified Ticket Operation"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_WorkLogApiService_updatePOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, // Interface script invoked by the instance:

var request = {

"type\_id": "WorkLogTypeCheckStatus",

"synchronize\_id": "false",

"description": "quxw",

"operation\_type": "Manual",

"attachment": "eyJleHBpcmVUaW1lIjoxNjY5Nj==",

"order\_id": "quxw-20221128-00000001",

"app\_name": "quxw",

"module\_name": "bpm",

"rich\_description": "quxw",

"attachment\_id": "install-log.zip",

"work\_log\_id": "453c64d7-6f86-11ed-8487-0255ac1200a8"

}

var url = "/adc-bpm/rest/v1/order/worklog/update";

var response = ServiceInvoker.post(url, request);