---
title: "Updating a Process Connection Condition"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002514924648.html"
depth: 6
---
#### Function

This API starts from GDE 24.2, Interface script invoked by the instance: { "flow\_condition\_id":"2c928029967f627d01967f68091f0007", "condition\_content": "order\_id = '11'", "module\_name": "test1", "condition\_type": "Tql", "process\_key": "flow1", "activity\_id": "AQT3", "project\_name": "test1"}; var response = ServiceInvoker.post("/adc-studio-bpm/rest/v1/flow-condition/create", request); and is used to update the process connection condition configuration. A complete parameter set must be provided, including key information such as the process condition ID, condition content, and module name.