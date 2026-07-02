---
title: "Command API Execution"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_CommandExecApiService_command-exec_appName_modelName_dictateType_dictateKey_POST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. This API is used to issue commands to probes for execution. This interface is an asynchronous interface. After the execution is complete, the callback service specified in the input parameter is invoked with the instruction execution result. This parameter specifies the address of the API used by each command to register with the API directory. It is often used together with the process.