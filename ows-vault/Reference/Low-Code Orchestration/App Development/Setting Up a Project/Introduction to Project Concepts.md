---
title: "Introduction to Project Concepts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_002.html"
depth: 3
---
# Introduction to Project Concepts

**Figure 1** Project concepts  
![[en-us_image_0000001489269005.png]]

**Table 1** Concept description  
| Concept | Description |
| :-- | :-- |
| Develop state | The develop state, also called the design state, is used for app development (including APIs, data orchestration, UI orchestration, and processes). The assets developed in this state are equivalent to a source package that does not have running instances. |
| Runtime state | The runtime-state system instantiates and runs the assets developed in the develop state and bears the permission control, flow control, and security issues during program running. |
| Project | In the develop state, you can manage multiple types of assets in a unified manner through projects. A project can contain multiple assets, for example, multiple modules. A project in the develop state corresponds to an app in the runtime state. |
| Module | A module is an independent unit in a project. Different modules can be divided based on different orchestration element types. |
| Orchestration element | Elements used to form a module, for example, pages and APIs. | In the current version, a developer can access the projects and modules created by other developers to collaboratively develop orchestration elements.

For example, when creating a product management app, you need to create a project and a module, and then develop orchestration elements in this module.

**Figure 2** Typical project diagram  
![[en-us_image_0000001170171809.png]]

**Parent topic:** [[Setting Up a Project|Setting Up a Project]]