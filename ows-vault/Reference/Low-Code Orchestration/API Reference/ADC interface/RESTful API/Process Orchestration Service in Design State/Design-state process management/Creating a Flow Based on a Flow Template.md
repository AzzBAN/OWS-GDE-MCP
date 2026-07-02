---
title: "Creating a Flow Based on a Flow Template"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546444587.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance: var request = {"process\_name": "test2","process\_key": "test2", "module\_name": "test1", "abbreviation": "test2","data\_model\_name": "test1\_test2", "project\_name": "test1", "auto\_process": "","page\_customizable": true, "template\_name": "default-process-template","open\_level": "public", "order\_seq\_format": "{YYYY}{MM}{DD}-{00000000}"}; var url = "/adc-studio-bpm/cse/rest/v1/process-designer/create-by-template";var response = ServiceInvoker.post(url, request);.