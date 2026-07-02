---
title: "Function Service Call"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_faas_012.html"
depth: 4
---
# Function Service Call

After a function service is developed, you can call the function through the **ServiceInvoke** or **RunScript** node.

-   In a service, you can call a function service through the **ServiceInvoke** node. For details, see [[Configuring the Node for Calling a Service|Configuring the Node for Calling a Service]]. To call an API, switch to the **Function** tab page to select a function service.

-   In the service, you can call the function service through the **RunScript** node. For details, see [[Configuring the Node for Executing a Script|Configuring the Node for Executing a Script]]. [Table 1](#EN-US_TOPIC_0000001487225846__table711619565012) describes the APIs.
    
    **Table 1** **Function Service APIs**  
    | API Name | Example |
    | :-- | :-- |
    | FaaS Invoke API | var request = {}; // Input parameter for executing the function var response = ServiceInvoker.post("/adc-faas/rest/v1/functions/project\_xx/module\_xx/function\_xx", request); Returned results:
    {"response": { "result": true, "request\_id": "xxxx-xxxx-xxxx-xxxx-xxxxxxxxx" }}
    
     |
    | Synchronous Call of Function Service API | var request = {}; // Input parameter for executing the function var response = ServiceInvoker.post("/adc-faas/rest/v1/functions/sync/project\_xx/module\_xx/function\_xx", request); Returned results:
    
    { "response": "\*\*\*\*\*\*","status": "succeeded"}
    
     |
    | FaaS Log Query API | var response = ServiceInvoker.post("/adc-faas/rest/v1/functions/task-log/xxxx-xxxx-xxxx-xxxx-xxxxxxxxx",{}); Returned results:
    
    { "start\_time": "2022-01-01T00:00:01.000+00:00",
    "function\_log": "\*\*\*\*\*\*\*",
    "function\_parameters": "{}",
    "user\_name": "user\_name\_xxxx",
    "function\_name": "function\_xxxx",
    "end\_time": "2022-01-01T00:00:01.000+00:00",
    "task\_id": "xxxx-xxxx-xxxx-xxxx-xxxxxxxxx",
    "module\_name": "module\_name",
    "project\_name": "project\_name",
    "status": "succeeded"}
    
     | **Parent topic:** [[Pro Code SDK APIs|Pro Code SDK APIs]]