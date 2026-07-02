---
title: "Associate the original ticket with the ticket in the specified associated ticket list."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_associatePOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"order\_id": {"id-20220922-00000001", "id-20220922-00000002"},

"reason": "Service reason,"

"operator":"Operator(ConfirmTask)"

};

var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/associate";

var response = ServiceInvoker.post(url, request);