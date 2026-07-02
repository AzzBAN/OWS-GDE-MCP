---
title: "Service Task Parameter"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_120.html"
depth: 5
---
#### Context

Service tasks are used in the service phase in the automated ticket handling scenario and are not used in the non-automated process. **Service Task Parameter** is used to call a service in an API catalog or app.

-   The **Service Task** node allows you to set input and output parameters, and exception handling policies of phases. When a phase starts, the API calls a required service using the input parameters, and generates output parameters using the returned result from the service.
-   The **Service Task** node supports the following configuration switches: **Record Calling Log**, **Asynchronize**, **Pause Before Execution**, **Automatic Execution Period**, **Wait After Execution**, and **Job Support Retry**.
-   The service task node supports dynamic API name configuration. The API name can contain dynamic variables. The format of the variables is the same as that of the default variables in the API expression, for example, _{title}_ and _{app\_name}_. The variable name must exist in the process context. For example, **/adc-service/rest/v1/services/my\_project/my\_module/**_{service\_name}_, in which _service\_name_ indicates the variable name in the process context.