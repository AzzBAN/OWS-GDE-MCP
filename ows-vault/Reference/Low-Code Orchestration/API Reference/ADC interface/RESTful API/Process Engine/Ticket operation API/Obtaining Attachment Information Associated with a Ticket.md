---
title: "Obtaining Attachment Information Associated with a Ticket"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_attachment_listPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"start": 0,

"limit": 10,

"order\_id": "test\_order\_01",

"expire\_time": 10000

};

var url = "/adc-bpm/rest/v1/order/attachment/list";

var response = ServiceInvoker.post(url, request);