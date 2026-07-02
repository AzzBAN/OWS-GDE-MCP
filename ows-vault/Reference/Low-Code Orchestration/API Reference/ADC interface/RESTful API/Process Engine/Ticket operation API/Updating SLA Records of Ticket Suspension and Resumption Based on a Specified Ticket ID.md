---
title: "Updating SLA Records of Ticket Suspension and Resumption Based on a Specified Ticket ID"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_sla_supend-pause-record_updatePOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, // Interface script invoked by the instance:

var request = {

"order\_id": "",

"record\_id": "",

"operate\_type": "",

"operated\_by": "",

"new\_operated\_by": ""

};

var url = "/adc-bpm/rest/v1/order/sla/supend-pause-record/update";

var response = ServiceInvoker.post(url, request);