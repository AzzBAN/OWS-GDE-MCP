---
title: "Describing the Deployment Capabilities"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_040.html"
depth: 4
---
# Describing the Deployment Capabilities

To ensure that developers can debug apps in a timely manner during app orchestration, the system supports triggering app deployment in the develop-state environment.

-   App deployment allows you to quickly package the current project as an app and deploy the app in the runtime-state environment.
-   During development and design in the develop-state environment, you can use the app deployment function to quickly deploy an app. After the app is deployed, you can debug services in the develop-state environment.
-   If the configuration in the development state is updated and needs to be debugged again, you need to deploy it again to debug the updated content.

You can trigger app deployment in the develop-state environment in either of the following ways:

-   One-click deployment: Apps can be quickly deployed to the runtime-state environment corresponding to the current develop-state environment based on the current configuration.
-   Customized deployment: You can customize deployment information, such as the running environment for deployment.
-   Hot deployment: After the hot deployment mode is enabled, when the configuration in the develop-state environment changes, the deployment is automatically initiated. The deployment can be completed without being perceived by developers, optimizing developers' debugging experience.

**Parent topic:** [[App Deployment Through a Develop-State Menu Entry|App Deployment Through a Develop-State Menu Entry]]