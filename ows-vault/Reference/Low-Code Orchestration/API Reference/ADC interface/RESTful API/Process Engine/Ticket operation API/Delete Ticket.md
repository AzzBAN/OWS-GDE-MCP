---
title: "Delete Ticket"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_deletePOST.html"
depth: 6
---
#### Function

Starts with GDE 24.2, Interface permission verification is implemented by the permission items bound to the invoking service in asset orchestration mode.. Interface script invoked by the instance:var request = { "order\_id": "test1-20201215-00000007", "reason": "test"};var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/delete";var response = ServiceInvoker.post(url, request);