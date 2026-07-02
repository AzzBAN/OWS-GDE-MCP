---
title: "Modifying process definition information"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002514924656.html"
depth: 6
---
#### Function Description

This script starts from GDE 24.2. The interface script is invoked by the instance: var request = {"open\_level": "protected","data\_model\_name": "test1\_flow1","process\_name": "flow1","module\_name": "test1","process\_key": "flow1","auto\_process": "no","project\_name": "test1"}; var url = "/adc-studio-bpm/cse/rest/v1/process-designer/create-by-template"; var response = ServiceInvoker.post(url, request);.