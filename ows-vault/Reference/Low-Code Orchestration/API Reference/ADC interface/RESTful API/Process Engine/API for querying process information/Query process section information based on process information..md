---
title: "Query process section information based on process information."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_activity_app_name_module_name_process_name_listPOST.html"
depth: 6
---
#### Function Description

This API starts from GDE 24.2. It is used to query process phase information based on the process name (such as the activity ID or activity name) and return the activity ID, activity name, page name, and mobile page name.

var request = {

"activity\_id": "TT10",

"activity\_name": "CreateTask",

"first\_task": "yes"

};

var url = "/adc-bpm/rest/v1/order/api-order/test\_app/test\_module/test\_process/list";

var response = ServiceInvoker.post(url, request);