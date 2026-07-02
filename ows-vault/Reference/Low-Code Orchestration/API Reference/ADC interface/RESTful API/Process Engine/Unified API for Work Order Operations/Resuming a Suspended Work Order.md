---
title: "Resuming a Suspended Work Order"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_UnifiedOrderOperationApiService_app_name_module_name_process_name_resumePOST.html"
depth: 6
---
#### Function

Starting from GDE 24.2, Interface script invoked by the instance:

var request = {

"order\_id": "test1-20201215-00000007",

"resume\_time": "2021-02-24 09:43:22",

"description": "test description",

"operator": "admin"

};

var url = "/adc-bpm/rest/v1/unified/order/test\_app/test\_module/test\_process/resume";

var response = ServiceInvoker.post(url, request);