---
title: "Concept Dictionary"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_dev_overview_006.html"
depth: 3
---
# Concept Dictionary

**Table 1** Concept dictionary  
| Concept | Description |
| :-- | :-- |
| ADC | Application Development Center (ADC) is a low-code and multi-experience development platform. |
| GDE | General Digital Engine (GDE) is a digital operation platform. It separates service units with common attributes from front-end applications to form public resources and capabilities that can be shared. It uses the "cloud service + online application development" mode to meet flexible and scalable service requirements of enterprises, decoupling services from platforms and applications from data. |
| Tenant | Different tenants can share one environment, in which each tenant is independent and does not affect by others. It is similar to the game Arena of Valor, when you activate account A in a service zone, account A can be used in different service zones. The level and hero of each service are different. |
| Develop State | Used to develop apps (including APIs, data orchestration elements, UIs, and processes). The assets developed in the develop-state environment are equivalent to a source program package that does not have running instances. It is also called Studio in develop state (design state). |
| Runtime State | The system instantiates and runs the assets developed in the develop-state environment and performs permission control, flow control, and security control during program running. |
| Project | In the develop-state environment, you can manage multiple types of assets in a unified manner through projects. A project can contain multiple assets, for example, multiple modules. A project in the develop-state environment corresponds to an app in the runtime-state environment. |
| Module | A module is an independent unit in a project. Different modules can be divided based on different orchestration element types. |
| Orchestration Element | Elements that are used to form modules, such as models, pages, and services. |
| Project Name | Used to isolate project identifiers from orchestration elements. The value can contain 3 to 64 characters, including letters, digits, underscores (\_), hyphens (-), and periods (.). It cannot end with \[..\] and must be globally unique. The project name cannot be changed after submission. |
| Module Prefix | Distinguish different modules for easy search. The value can contain lowercase letters, digits, and underscores (\_). The value is obtained from the Name value by default. A maximum of the first 10 characters can be retained. |
| Display Name | The display name is the app name displayed to end users. You can set it to a name that is easy to identify. The value can contain 1 to 100 characters. You can change the value in Settings after submitting the modification. |
| One-Click Deployment | Currently, the develop-state environment is separated from the runtime-state environment. After development, a project needs to be packaged and deployed to the runtime-state environment for debugging. The project can be directly packaged as an app and installed in the runtime-state environment. If the configuration in the develop-state environment is updated and needs to be debugged again, you need to deploy it again to debug the updates. |
| Hot Deployment | Used to deploy the elements orchestrated in the develop-state environment to the runtime-state environment in real time. The hot deployment function is disabled by default. To use this function, you need to manually enable it. After this function is enabled, you do not need to manually perform one-click deployment when debugging is required. |
| Model | Used to store data and provide data APIs. Models are classified into common data models, data source models (used to access external data), and elastic models (used to store and manage a large amount of data). |
| Service | Operations on data (also called logic flow). |
| Page | Used to design the pages used by users. |
| Trigger | Used to configure the triggering action upon data change. |
| Data Export | Used to define the capability of exporting data in Excel and CSV formats. |
| Data Import | Used to define the capability of importing data in Excel and CSV formats. |
| Menu | Pages developed in the develop-state environment can be released as menus for users. |
| I18n | Used to configure the multi-language internationalization. The system provides Chinese and English by default. |
| Permission | Used to configure permissions for orchestration elements. |
| Business Process | Page for managing business processes (also called workflow). |
| Inbound REST | Inbound REST API configuration, which is used to configure REST APIs provided for third parties. |
| Outbound REST | Outbound REST API configuration, which is used to configure REST APIs for calling third parties. |
| Inbound SOAP | Inbound SOAP API configuration, which is used to configure SOAP APIs for third parties. |
| Outbound SOAP | Outbound SOAP API configuration, which is used to configure SOAP APIs for calling third parties. |
| Asset | Content provided by developers after creation on ADC, such as develop-state projects, runtime-state apps, page templates, and project templates. Such content is accumulated based on developers' wisdom and service experience and has extensive values. | **Parent topic:** [[Application Development Overview|Application Development Overview]]