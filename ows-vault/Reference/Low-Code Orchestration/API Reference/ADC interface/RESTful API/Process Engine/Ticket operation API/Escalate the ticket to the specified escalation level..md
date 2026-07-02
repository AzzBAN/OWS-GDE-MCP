---
title: "Escalate the ticket to the specified escalation level."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_escalatePOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

{

"order\_id": "ID\_456\_1594175397300",

"escalate\_level": "nnn",

"escalate\_to": "",

"reason": "test",

"description": "test",

"operator": "test",

"message\_type": \["SMS"\]

}

};

var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/escalate";

var response = ServiceInvoker.post(url, request);