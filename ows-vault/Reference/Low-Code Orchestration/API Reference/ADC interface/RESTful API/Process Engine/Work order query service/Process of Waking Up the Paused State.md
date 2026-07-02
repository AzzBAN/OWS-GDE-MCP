---
title: "Process of Waking Up the Paused State"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ApiOrderApiService_api-order_app_name_module_name_process_name_signalPOST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. Interface script invoked by the instance:

var request = {

"operator": "test\_user",

"execution\_id": "test\_execution\_01",

"activity\_id": "TT10",

"form\_data": {}

};

var url = "/adc-bpm/rest/v1/order/api-order/test\_app/test\_module/test\_process/signal";

var response = ServiceInvoker.post(url, request);