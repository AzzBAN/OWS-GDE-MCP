---
title: "Configuring the Deployment Distribution Mode"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_055.html"
depth: 4
---
#### Context

The deployment distribution mode is used by the backend during app deployment. The selected distribution mode takes effect during app deployment.

-   **ADC App Manager** is usually used to develop app distribution modes in ADC. It can also be used to orchestrate elements such as external access, API integration, common settings, network services, processes, robot automation, and network automation.
-   **GDE App Manager** calls AppManager in the backend to install apps. It can also be used when orchestration elements including data orchestration and API integration are involved.
-   **Auto**: If the orchestration elements of data orchestration and API integration are included and AppManager has been deployed in the current system, the asset is deployed based on the process of **GDE App Manager**. If the orchestration elements (for example, external access, API integration, common settings, network service, robot automation, and network automation) in ADC are detected, **ADC App Manager** can be used. This mode is not supported for remote deployment.