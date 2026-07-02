---
title: "Used to re-assign a ticket to another ticket handler."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationApiService_app_name_module_name_process_name_reassignPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"order\_id": "test1-20201215-00000007",

"assign\_to": "user:test", "reason": "test", "operator": "test", "target\_node": "process", "target\_node\_name": "process", "message\_type": \["SMS"\]

};

var url = "/adc-bpm/rest/v1/order/test\_app/test\_module/test\_process/reassign";var response = ServiceInvoker.post(url, request);