---
title: "Creating a Process Connection Condition"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546364569.html"
depth: 6
---
#### Function

It starts with GDE 24.2, Interface script invoked by the instance: var request = {"condition\_content": "order\_id = '11'","module\_name": "test1","condition\_type": "Tql","process\_key": "flow1","activity\_id": "AQT3","project\_name": "test1"}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/flow-condition/create", request);. This interface is used to create a process connection condition. Complete condition configuration parameters must be provided.