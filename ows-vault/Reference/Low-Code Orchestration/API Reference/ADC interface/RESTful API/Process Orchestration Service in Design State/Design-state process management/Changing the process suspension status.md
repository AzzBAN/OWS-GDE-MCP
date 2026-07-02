---
title: "Changing the process suspension status"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002514764724.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance: var request = {}; var url\_params = { "project\_name": "test1",

"module\_name": "test1",

The "name": "flow1"}; return ServiceInvoker.put("/adc-studio-bpm/rest/v1/process-designer/change-status/test1/test1/flow1", request, url\_params); API is used to modify the process status of a specified project or module. The process status can be enabled or disabled. The complete project name, module name, and process name must be provided.