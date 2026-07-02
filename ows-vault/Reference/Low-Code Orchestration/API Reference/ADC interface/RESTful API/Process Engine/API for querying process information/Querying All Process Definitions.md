---
title: "Querying All Process Definitions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_definition_listPOST.html"
depth: 6
---
#### Function Description

This API starts with GDE 24.2 and is used to query the process definition list. The process name, activation status, service type, process abbreviation, and whether the process is an automated process are returned.

var request = {

"start": 0,

"limit": 10,

"sort": "",

"dir": "",

"condition": {

"app\_name": "test\_app",

"module\_name": "test\_module"

}

};

var url = "/adc-bpm/rest/v1/process/definition/list";

var response = ServiceInvoker.post(url, request);