---
title: "Querying TT Operation Rights"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderOperationValidateApiService_operation-permission_verifyPOST.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2.

The following is an example of the interface invoking script:

var request = 
  {    
    "control\_id": "cancel",
    "parameters": {"order\_id":"hjwa-20230109-00000003"},
  }
var url = "/adc-bpm/rest/v1/order/batch-access-check";
var response = ServiceInvoker.post(url, request);