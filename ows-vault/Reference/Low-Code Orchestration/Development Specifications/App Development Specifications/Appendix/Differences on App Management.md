---
title: "Differences on App Management"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001891434237.html"
depth: 4
---
# Differences on App Management

**Table 1** Differences between GDE App Manager and ADC App Management   
| Item | GDE App Manager | ADC App Management |
| :-- | :-- | :-- |
| Menu path | Products and Services > Administration > Assets > GDE App Manager | Products and Services > Administration > Assets > App Management |
| Orchestration element | The following orchestration elements are supported:
-   ADC orchestration elements. For details, see [Table 2](#EN-US_TOPIC_0000001891434237__en-us_topic_0000001891316025_table1786541417185).
-   Other orchestration elements of non-ADC services, such as API Fabric, AI, and DataFactory.

 | ADC orchestration elements are supported only. For details, see Table 2. NOTICE: If an app deployed in one-click mode in the develop-state environment contains orchestration elements of non-ADC services, the files in the installation log list on the ADC app management page are not full files and contain only content related to ADC orchestration elements. |
| Incremental deployment | -   The upgrade packages installation is not supported, but the page does not forcibly verify whether an upgrade package is installed or not.
-   If an upgrade package is forcibly installed, the app uninstallation process on the ADC app management page may be triggered.

 | The upgrade packages can be installed. |
| Asset retention or archiving | -   The automatic asset archiving function is not supported. By default, only asset packages with up to three versions can be uploaded.
-   If the number of asset package versions to be uploaded exceeds the upper limit, determine whether to select **Overwrite Old Version** based on site requirements.

 | Based on the archiving configuration on the Products and Services > Administration > Archiving Configuration page, the system triggers asset archiving at a specified time every day. By default, only the latest four asset packages and their corresponding upgrade packages are retained. |
| Asset package version management | -   Asset packages of multiple versions can be concurrently uploaded. The number of versions can be changed by setting the system function parameter **number\_retained\_uninstalled\_versions** on the **GDE App Manager** page.
-   Asset packages of earlier versions cannot be installed.

 | -   Asset packages of multiple versions cannot be concurrently uploaded. The asset package download function is only available in the installation log list.
-   By default, assets of earlier versions cannot be installed. To install such assets, set the tenant-level parameter **allow\_lower\_version\_app**.

 | **Table 2** ADC orchestration elements  
| Orchestration Element Information in Logs | Orchestration Element Menu Entry in the Develop-State Environment |
| :-- | :-- |
| MODEL | Model |
| SERVICE | Service |
| EVENT | Event |
| EVENT\_LISTENER | Event Listener |
| DATA\_EXPORT | Data Export |
| DATA\_IMPORT | Data Import |
| PAGE | Page |
| I18N | Internationalization |
| JOB | Timer |
| DATAV | Data Visualization |
| DOCUMENT | Document |
| MENU | Menu |
| PERMISSION | Permission |
| ERROR\_CODE | Error Code |
| WORKFLOW | Business Process |
| CARD | Card |
| TRIGGER | Trigger |
| MOBILE\_PAGE | Mobile Page |
| MODEL\_DUMP | Model Dump |
| MODEL\_LOAD | Model Load |
| FAAS | Function Service |
| MODEL\_ARCHIVE | Model Archiving |
| MODEL\_DATA\_ACCESS | Model Data Permission |
| MODEL\_FLOW | Model Flow |
| COMMAND\_MANAGEMENT | Command |
| SCRIPT\_MANAGEMENT | Script |
| DATA\_PACKAGE | Customized Asset |
| INBOUND\_REST | Inbound REST |
| OUTBOUND\_REST | Outbound REST |
| INBOUND\_SOAP | Inbound SOAP |
| OUTBOUND\_SOAP | Outbound SOAP |
| RPA\_SCRIPT | RPA Script |
| RPA\_PLUGIN | RPA Plugin | **Parent topic:** [[Appendix|Appendix]]