---
title: "Introducing a Project Template"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_004.html"
depth: 3
---
# Introducing a Project Template

Multiple project templates are preset in the system. After a project is created using a project template, the menus of different orchestration elements are displayed by default.

**Table 1** Template description    
| Scenario | Template | Applicable Scenario | Preset Orchestration Menu |
| :-- | :-- | :-- | :-- |
| Common | 
-   General job orchestration template
-   Data visualization template

 | Used to create data models, and add, delete, modify, and query data on a page. | After a project is created using this template, the following menus are displayed by default when the first module is created:

-   Model
-   Service
-   Page
-   Data Visualization
-   Trigger
-   Data Import
-   Data Export
-   Menu
-   I18n
-   Permission
-   Model Archiving

 |
| Process | Process template | Used in the scenario where a business object requires a set of processes that are operated by different roles in different phases. | After a project is created using this template, the following menus are displayed by default when the first module is created:

-   Business Process
-   Model
-   Service
-   Page
-   Permission
-   I18n
-   Menu
-   Model Archiving

 |
| Network operation automation | Network automation template | Used to develop commands and scripts, change network configurations, and deliver scripts to the network through devices or EMS clients for the scripts to take effect. | After a project is created using this template, the following menus are displayed by default when the first module is created:

-   Command
-   Script

 |
| RPA | RPA template | Used to create an asset for automating a robotic process automation (RPA) process. | After a project is created using this template, the following menus are displayed by default when the first module is created:

-   RPA Script
-   RPA Plugin

Related orchestration elements need to be used together with local RPA tools. |
| Data orchestration | Data orchestration template | Used during data modeling and data process design and orchestration. It implements one-stop data development during the data life cycle using the metadata management, data computing engine, graphical operators, and operator computing logic. | After a project is created using this template, the following menus are displayed by default when the first module is created:

-   DataFactory Homepage
-   Data Model
-   Data Process
-   Data Exploration
-   Data Source
-   Data Integration
-   Debug Task Management
-   Extended Functions
-   Data Quality

 | In a project, after a module is created and the menu is adjusted, if you create a second module, the system creates the second module based on the menu of the current module by default. For example, if a card menu is added to the first module, the card menu is also displayed by default when the second module is created. If multiple modules have been created and different menus have been adjusted, the system creates menus for the new modules based on the menus of the current modules.

**Parent topic:** [[Setting Up a Project|Setting Up a Project]]