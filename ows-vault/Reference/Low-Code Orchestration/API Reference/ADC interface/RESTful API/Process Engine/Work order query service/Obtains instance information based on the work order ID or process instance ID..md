---
title: "Obtains instance information based on the work order ID or process instance ID."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ApiOrderApiService_api-order_app_name_module_name_process_name_get-processing-activitiesPOST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. Obtains the execution phase ID and process instance execution ID based on the work order ID or process instance ID.

Interface script invoked by the instance:

var request = {

"order\_id": "id-20220922-00000001"

};

var url = "/adc-bpm/rest/v1/order/api-order/test\_app/test\_module/test\_process/get-processing-activities";

var response = ServiceInvoker.post(url, request);