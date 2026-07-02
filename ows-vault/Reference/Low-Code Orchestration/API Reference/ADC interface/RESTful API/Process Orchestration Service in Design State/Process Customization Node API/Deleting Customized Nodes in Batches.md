---
title: "Deleting Customized Nodes in Batches"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessCustomNodeApiService_batch-deletePOST.html"
depth: 6
---
#### Function description

It starts with GDE24.2. Deletes activities in the customized activity ID list in batches. The IDs of the activities that are successfully deleted are returned.

Interface script invoked by the instance:

var request = {
"activity\_ids": \["TT10", "TT11"\]
};
var url = "/adc-studio-bpm/rest/v1/custom-nodes/batch-delete";
var response = ServiceInvoker.post(url, request);