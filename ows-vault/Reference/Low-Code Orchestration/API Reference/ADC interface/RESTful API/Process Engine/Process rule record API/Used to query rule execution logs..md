---
title: "Used to query rule execution logs."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessRuleRecordApiService_app_name_module_name_process_name_process-rule-log_listPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, // Interface script invoked by the instance:

var request = {

"order\_id": "quxw-20221128-00000001",

"is\_archived": false

}

var url = "/adc-bpm/rest/v1/order/{app\_name}/{module\_name}/{process\_name}/process-rule-log/list ";

var response = ServiceInvoker.post(url, request);