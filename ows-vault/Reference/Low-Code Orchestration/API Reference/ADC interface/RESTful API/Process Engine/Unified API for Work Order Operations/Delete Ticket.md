---
title: "Delete Ticket"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_UnifiedOrderOperationApiService_app_name_module_name_process_name_deletePOST.html"
depth: 6
---
#### Function Description

The following is an example of API calling when GDE 24.2 is used:

var request = {

"order\_id": "test1-20201215-00000007",

"reason": "test"};var url = "/adc-bpm/rest/v1/unified/order/test\_app/test\_module/test\_process/delete";

var response = ServiceInvoker.post(url, request);