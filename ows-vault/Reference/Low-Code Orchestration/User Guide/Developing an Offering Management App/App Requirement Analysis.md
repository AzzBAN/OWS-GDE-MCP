---
title: "App Requirement Analysis"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/demo_004.html"
depth: 3
---
# App Requirement Analysis

This section describes how to analyze app requirements.

**Table 1** Requirement analysis    
| Category | Item | Implementation Analysis | Orchestration Elements |
| :-- | :-- | :-- | :-- |
| App description | An offering management app is developed to manage offering information. | As a typical information development app, the offering management app can be implemented through the general job orchestration capability of ADC. ADC app orchestration is implemented through the Integrated Orchestration module in the develop-state environment. All orchestration resources need to be managed using specific projects and modules. Therefore, you need to create a project and module first. | 
-   Project

 |
| Basic functions | An offering consists of name, price, image, category, and description. The category can be managed separately. | To manage offerings, you need to create data models and tables for offering information. The following tables are involved:

-   Category information table:
    -   Category ID: unique ID for each offering category.
    -   Category name: name corresponding to the category ID. For example, **DRINK** indicates drinks, and **FOOD** indicates food. The value can be of the text type.

-   Offering information table:
    -   ID: offering ID, which is used to uniquely identify and query an offering.
    -   Name: offering name, which is usually a character string, that is, of the text type.
    -   Price: offering price. The value can be of the float type, because the value may contain decimal points.
    -   Image: offering image, which can be managed through file attachments. The value is of the file type.
    -   Category: Offering categories, for example, food and drinks, can be managed separately. The category information needs to be selected during offering management. Therefore, you need to set the value type of **Category** to **Reference** to reference the category information table.
    -   Description: offering description, which is usually of the text or long text type.

 | -   Model

 |
| The offering list can be filtered by category and sorted by price. | During offering list query, offerings can be filtered by category and sorted by price. In ADC, the offering list query function needs to be implemented through services. Services can be automatically generated through models or modified based on the GetList services. Offerings can be filtered by category and sorted by price. | -   Service
-   Page

 |
| Offering operation information, including the operator, operation time, change type, and offering name, is recorded. | When creating a model, you can select the preset operator and time. Offering addition, deletion, and modification are implemented through services. In services, operation logs can be recorded. | -   Service

 |
| Offering information can be imported from and exported to an Excel file (excluding images). | The system supports the import and export of Excel files. When services and pages are automatically generated based on models, the corresponding data import and export capabilities are also automatically generated. You can directly use the default capabilities. | -   Data Import
-   Data Export

 |
| Security requirements | Managers and common employees can query, create, and delete offerings. | The system supports permission control on app resources such as pages, services, and URLs. | -   Menu
-   Permission

 |
| Only managers can manage offering category information. Only managers can import and export offering information and offering category information. | You can configure the offering management manager role and assign permission items to the role. | -   Permission
-   Role

 |
| Necessary parameter verification is required before an offering is saved. | In the services used for adding, deleting, and modifying offering information, the parameter validation function needs to be added, which can be implemented through a validator. | -   Service (Service > Validator)

 | **Parent topic:** [[Developing an Offering Management App|Developing an Offering Management App]]