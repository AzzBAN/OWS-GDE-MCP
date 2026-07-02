---
title: "Introduction to Remote Deployment"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_046.html"
depth: 4
---
# Introduction to Remote Deployment

Apps must be developed in the develop-state environment of ADC and debugged and run in the runtime state. ADC allows you to deploy apps developed in a develop-state environment in multiple runtime-state environments.

For example, after developing an app in the develop-state environment, you can deploy it in runtime-state environment 1 for testing. After the test is complete, you can deploy the app in runtime-state environment 2 for production.

This way ensures normal running of the production environment and ensured and improves app release efficiency.

![[en-us_image_0000001560813705.png]]

This feature requires multiple environments to interwork. You need to configure this feature in the involved runtime-state environments and develop-state environment before using it.

**Parent topic:** [[Configuring Remote Deployment|Configuring Remote Deployment]]