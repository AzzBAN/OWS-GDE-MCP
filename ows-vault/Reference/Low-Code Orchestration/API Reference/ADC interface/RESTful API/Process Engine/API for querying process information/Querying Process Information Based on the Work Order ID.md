---
title: "Querying Process Information Based on the Work Order ID"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProcessQueryApiService_definition_order_id_GET.html"
depth: 6
---
#### Function Description

This API starts from GDE 24.2. It queries process information based on the ticket ID and returns the activation status, service type, process abbreviation, and whether the process is an automatic process.

var request = {};var url = "/adc-bpm/rest/v1/process/definition/{order\_id}";var response = ServiceInvoker.post(url, request);