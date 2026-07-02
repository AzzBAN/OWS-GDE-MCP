---
title: "Hot Deployment"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_035.html"
depth: 4
---
#### Context

Currently, the develop state is separated from the runtime state. After development, you need to package the elements and deploy them to the runtime state for debugging. Currently, the deployment of 50 element instances is completed within 1 minute. Some services have thousands of element instances. The deployment duration may reach 5 minutes, which is inconvenient for development and debugging.

Hot deployment is to incrementally deploy elements orchestrated in the develop-state environment to the runtime-state environment in real time. Developers do not need to manually perform one-click deployment, which facilitates quick debugging.

![[note_3.0-en-us.png]]

During process orchestration, only the hot deployment setting of process charts and process definitions (including creating, modifying, deleting, copying, enabling, and disabling processes) can be saved.

When creating a project, you can determine whether to enable hot deployment. If you need to modify the configuration after the project creation, change the parameter value through deployment configuration.