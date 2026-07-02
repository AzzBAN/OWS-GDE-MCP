---
title: "Updating the Process Archiving Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546364583.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance: var request = { "id":"2c92802b967b218d01967b8995690000", "project\_name": "test1", "module\_name": "test1", "process\_name": "flow1", "retention\_days": 151, "retention\_rows": 10000000, "archiving\_type": "ES", "auto\_process": false, "second\_archive\_config": { "retention\_days": 151, "archiving\_type": "DEL"}, "create\_replica\_model": false}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/archive-config/update", request);.