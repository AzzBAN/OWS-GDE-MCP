---
title: "Querying Process Information by Process Name"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_definition_app_name_module_name_process_name_getPOST.html"
depth: 6
---
#### Function Description

This API starts with GDE 24.2. It queries process information based on the process name and returns the activation status, service type, process abbreviation, and whether the process is an automated process.

var request = {};

var url = "/adc-bpm/rest/v1/process/definition/test\_app/test\_module/test\_process/get";

var response = ServiceInvoker.post(url, request);