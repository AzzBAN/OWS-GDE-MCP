---
title: "Query basic ticket information based on the application name, module name, process name, and ticket ID."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002515918522.html"
depth: 6
---
#### Function description

It starts with GDE 24.2, Interface script invoked by the instance: var request = {}; var url = "/adc-bpm/rest/v1/order/my\_app/my\_module/my\_process\_key/1234-abcd-0000/processing-task-info"; var response = ServiceInvoker.get(url, request);.