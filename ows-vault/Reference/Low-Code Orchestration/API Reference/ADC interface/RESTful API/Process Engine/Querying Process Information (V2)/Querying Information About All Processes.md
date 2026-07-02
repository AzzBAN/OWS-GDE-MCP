---
title: "Querying Information About All Processes"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546607807.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance: var request = {"start": 0,"limit": 10,"sort": "","dir": "","condition": {"app\_name": "test\_app","module\_name": "test\_module"}}; var url = "/adc-bpm/rest/v2/process/definition/list"; var response = ServiceInvoker.post(url, request);.