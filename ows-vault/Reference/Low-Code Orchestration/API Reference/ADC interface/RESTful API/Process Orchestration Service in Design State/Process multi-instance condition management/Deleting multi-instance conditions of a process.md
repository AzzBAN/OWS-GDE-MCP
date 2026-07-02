---
title: "Deleting multi-instance conditions of a process"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002546364571.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance: var url\_params = {"id": "2c9280299647a3fd019647ab49700000"}; var response = ServiceInvoker.delete("/adc-studio-bpm/rest/v1/multitask-condition/delete/2c9280299647a3fd019647ab49700000", url\_params);. This API is used to delete a process multi-instance condition with a specified ID. It applies to process configuration management scenarios. Ensure that the ID parameter meets the format requirements.