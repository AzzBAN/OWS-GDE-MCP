---
title: "Registering Customized Nodes in Batches"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessCustomNodeApiService_batch-registerPOST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. Registers activities in the customized activity ID list in batches. The IDs of the activities that are successfully registered are returned.

Interface script invoked by the instance:

var request = {
"activity\_ids": \["TT10", "TT11"\]
};
var url = "/adc-studio-bpm/rest/v1/custom-nodes/batch-register";
var response = ServiceInvoker.post(url, request);