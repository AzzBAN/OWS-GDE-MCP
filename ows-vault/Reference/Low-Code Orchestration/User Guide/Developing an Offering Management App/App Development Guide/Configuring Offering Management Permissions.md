---
title: "Configuring Offering Management Permissions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/demo_012.html"
depth: 4
---
#### Scenario Description

ADC supports multi-layer permission management. You can configure permission items for different orchestration elements, assign permission items to specified roles, and associate roles with users during user creation to implement permission control.

**Table 1** Permission configuration analysis  
| Orchestration Element Type | Permission Control Mode |
| :-- | :-- |
| Model | When Data can be accessed by the frontend is enabled for a model, data permission access control policies need to be configured. |
| Service | By default, Authentication Type of the service is Login only, that is, the permission is not controlled. To control the permission, you need to set Authentication Type to Login and authorization, and select the desired permission item. Only the user who has this permission item can access the service. |
| Page component | To control the permission of the components on the page, such as the redirection button and window button, you need to obtain and configure the permission URI. |
| Menu | A permission item is automatically generated for each menu. The permission item needs to be assigned to a role. |
| Import and export services | For data import and export services, configured permission items need to be associated. Otherwise, permission control policies do not take effect. | You need to plan permission items based on permission control requirements.

**Table 2** Permission item planning    
| Permission Item Name | Configuration | Description | Role to Which the Permission Is Assigned |
| :-- | :-- | :-- | :-- |
| menu\_goods\_info | After a menu is created, a permission item with the same name as the menu is automatically generated. | The permission item has been automatically bound to the corresponding menu. After the permission item is assigned to a role, the menu is displayed to the role. | 
-   staff
-   manager

 |
| menu\_category | After a menu is created, a permission item with the same name as the menu is automatically generated. | The permission item has been automatically bound to the corresponding menu. After the permission item is assigned to a role, the menu is displayed to the role. | manager |
| manageCategory | Create a permission item to manage and control the service permission for creating offering categories. | The permission item needs to be bound to the following services of the offering category model:

-   info\_category\_update
-   info\_category\_get\_list
-   info\_category\_get
-   info\_category\_create
-   info\_category\_batch\_update
-   info\_category\_batch\_delete

 | manager |
| manageGoodsinfo | Create a permission item to manage and control the service permission for querying offering information. | The permission item needs to be bound to the following services of the offering information model:

-   info\_goods\_update
-   info\_goods\_get\_list
-   info\_goods\_get
-   info\_goods\_create
-   info\_goods\_batch\_update
-   info\_goods\_batch\_delete

 | -   staff
-   manager

 |
| importGoods | Create a permission item to manage and control the permission for importing offering information. | The permission item needs to be bound to the data import service info\_goods\_import for importing offering information. In addition, the permission item needs to be bound to the import button on the info\_goods\_grid page to ensure that the frontend and backend permissions are the same. | manager |
| exportGoods | Create a permission item to manage and control the permission for exporting offering information. | The permission needs to be bound to the data export service info\_goods\_export for exporting offering information. In addition, the permission item needs to be bound to the export button on the info\_goods\_grid page to ensure that the frontend and backend permissions are the same. | manager |