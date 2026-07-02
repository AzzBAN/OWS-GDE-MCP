---
title: "Query the corresponding advanced query service based on the application name, module name, and process name."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_app_name_module_name_process_name_query_serviceGET.html"
depth: 6
---
#### Function Description

This API starts from GDE 24.2. It is used to query the corresponding advanced query service based on the application name, module name, and process name.

var url = "/adc-bpm/rest/v1/order/{app\_name}/{module\_name}/{process\_name}/query\_service"; var response = ServiceInvoker.get(url);