---
title: "Creating a Process Archiving Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002514924662.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance: var request = { "project\_name": "StudioBPM\_HotDeploy6", "module\_name": "SHD1", "process\_name": "test1", "retention\_rows": 10000000, "archiving\_type": "ES", "auto\_process": false, "second\_archive\_config": { "retention\_days": 151, "archiving\_type": "DEL"}, "create\_replica\_model": true}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/archive-config/create", request);.