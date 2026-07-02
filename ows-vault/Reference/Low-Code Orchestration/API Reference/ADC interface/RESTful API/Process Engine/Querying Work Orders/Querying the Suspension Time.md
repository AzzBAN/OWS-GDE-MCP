---
title: "Querying the Suspension Time"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiProtectedService_sla-pause-time_queryPOST.html"
depth: 6
---
#### Function

Query the SLA suspension and resumption time of a ticket based on the specified ticket ID on GDE 24.2.

Interface script invoked by the instance: var request = { "order\_id": "test1-20201215-00000007",};var url = "/adc-bpm/rest/v1/order/sla-pause-time/query";var response = ServiceInvoker.post(url, request);