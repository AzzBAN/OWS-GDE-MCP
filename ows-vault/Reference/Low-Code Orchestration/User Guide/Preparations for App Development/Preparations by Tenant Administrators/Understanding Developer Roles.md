---
title: "Understanding Developer Roles"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_dev_prepare_002.html"
depth: 4
---
# Understanding Developer Roles

A role is a group of users with the same responsibilities. Users complete their specified work based on their roles.

[Table 1](#EN-US_TOPIC_0000001539379729__en-us_topic_0000001135645954_table372525510286) lists the default roles provided in the develop-state system. The roles and their responsibilities specified in this document are for reference only.

The system administrator and developer permissions must be separated for users. You are advised not to assign the administrator and developer roles to the same user.

The tenant administrator, as an administrator, should not participate in application development. If high-risk operations arise from improper application development by the administrator, the administrator shall bear full responsibility for such operations.

**Table 1** Default roles in the develop-state system   
| Role | Description | Default Operation Permission |
| :-- | :-- | :-- |
| StudioFaaSTenantAdmin | Tenant dependency package administrator in the develop state. Users with this role can query and edit tenant-level dependency packages. | This role has permissions on Tenant Function Dependency Managing and Tenant Function Dependency Query menus. |
| StudioDeveloper | Developers. They have the permissions to develop and customize apps and integrate the apps to the system in the develop state. They can only maintain and manage assets such as apps developed only by themselves. | This role has permissions on the following pages:
-   Menu permissions (runtime state):
    -   **Model Management**: **Model Property Manage**, **Shard Policy**, **Data Load Log**, **Data Dump Log**, and **Cache Configuration**
    -   **Integration Service**: **FTP Management**, **Inbound REST Management**, **Inbound SOAP Management**, **Inbound Strategy Management**, **Certificate Management**, **Outbound REST Management**, **Outbound SOAP Management**, **Outbound Strategy Management**, and **WSSE Signature Management**
    -   **Log Management**: **FaaS Task Run Log** (Log query)
    -   **Integration Log**: **REST Receive Log**, **REST Send Log**, **SOAP Receive Log**, and **SOAP Send Log**
    -   **Development State Studio**
-   Shortcut permissions (Portal configuration):
    -   **App Shortcuts**: **Development State Studio**
    -   **App Shortcut Category**: **Common Management**
-   API permissions (develop state):
    -   **Asset Management**: **Category Management**, **Modify Asset**, **Import Asset**, **Delete Asset**, and **View Asset**
    -   **Common operation rights**: **get user information**
    -   **Studio Develop** > **Common**: **Develop-State Asset Initialization Logs**, **Developer Certificate**, **Menu Unify Func**, and **Query User info**
    -   **Studio Develop** > **Release Asset**: **Save asset registration configuration** and **Viewing asset registration configurations**
    -   **Studio Develop** > **Project Management**: **Query Remote Deploy Environment**, **Query Business Field**, **Create Business Field**, **Update Business Field**, **Delete Business Field**, **Hot Deploy Configuration**, **Modify personal project members**, **List Project**, **Delete Project**, **Export Project**, **Import Project**, **Modify Project**, and **Create Project**
    -   **Studio Develop** > **Asset Developing**: **Intg Developing**, **Workflow Development**, **Model Develop**, **Mobile Page Develop**, **Menu Develop**, **I18n Develop**, **Card Develop**, **Page Develop**, **Document**, **PermissionResource**, **TimerTask**, **ErrorCode**, **RolePermission**, **Permission**, **Quality evaluation**, **Custom asset** (**Import custom asset**, **Delete custom asset**, **Query custom asset**, **update custom asset**, **Create custom asset**, and **Export custom asset**), **Data Import**, **Data Export**, **Service Developing**, and **Network Operation** (**Command Management**, **Route Management**, **Resource Management**, **Resource Type Management**, **General Setting**, and **Script Management**)
    -   **Studio Mateline Editor**
    -   **Studio UI Editor**
    -   **Studio Mateline Editor**
    -   **Model Foundry Template Orchestration**

 |
| StudioFaasDeveloper | Preset role of the FaaS service. Users with this role can query and edit project-level dependency packages. | This role has permissions on Tenant Function Dependency Managing and Tenant Function Dependency Query, and Function Developing menus. |
| AssetDeveloper | Asset developer, a preset role of the asset services. This role is responsible for asset management operations. | This role can be used only when the StudioDeveloper role is assigned first. This role has the following operation permissions:

-   Menus and operations under **Asset Management** in the develop-state environment:
    -   Asset Vulnerabilities
    -   Asset viewing
    -   Asset deletion
    -   Asset import
    -   Asset modification
    -   Service type management
    -   Asset deployment
    -   Deployment environment viewing
    -   Asset Library
    -   Asset Approval (only for viewing and no approval-related operation permission)
    -   Asset Production Environment (only for viewing and using, and no permission to add, delete, or modify the asset production environment)
-   Operations under **API Catalog** in the runtime-state environment:
    -   API deletion
    -   API import
    -   API modification
    -   API viewing

 |
| AssetOperationsAdmin | Asset operations administrator, a preset role of the asset service. Users with this role can approve the asset putaway and remove assets. | This role has permissions to approve and reject asset putaway and remove assets. |
| AssetMaintenanceAdmin | Asset O&M administrator, a preset role of the asset service. Users with this role can approve the asset putaway and configure the asset production environment. | This role has permissions to approve and reject asset putaway and add, modify, and delete the asset production environment. |
| StudioAssetAnalyst | Develop-state asset analyst, a preset role of the asset service. Users with this role can analyze tenant-level asset dependency and provide analysis suggestions for asset rectification, consolidation, and sunsetting. This role must be used together with the StudioDeveloper role. That is, users must be bound to both the StudioDeveloper and StudioAssetAnalyst roles to have the asset dependency analysis permissions. The StudioAssetAnalyst role alone is not enough. | This role has the permission to access the Asset Management > Asset Dependency Analysis menu in the develop state. Users with this role can view the element distribution, element dependency chain, inter-project dependency, and inter-project element dependency of all assets of a tenant. | **Parent topic:** [[Preparations by Tenant Administrators|Preparations by Tenant Administrators]]