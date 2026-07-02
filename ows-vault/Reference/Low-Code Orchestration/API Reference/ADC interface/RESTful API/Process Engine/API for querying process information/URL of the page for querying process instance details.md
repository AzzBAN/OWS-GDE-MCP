---
title: "URL of the page for querying process instance details"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_app_name_module_name_process_name_page-urlGET.html"
depth: 6
---
#### Function Description

Query the URL of the process instance details page based on the app name, module name, and process name on GDE 24.2.

var request = {};

var url = "/adc-bpm/rest/v1/process/my\_app/my\_module/my\_process/page-url";

var response = ServiceInvoker.get(url, request);