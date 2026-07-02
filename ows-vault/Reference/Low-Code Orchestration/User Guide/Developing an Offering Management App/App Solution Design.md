---
title: "App Solution Design"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/demo_005.html"
depth: 3
---
# App Solution Design

Developers need to analyze service requirements to determine the functions to be developed in the system and the orchestration elements to be used.

The following figure shows the orchestration elements of the offering management app.

![[en-us_image_0000001425158670.png]]

During the detailed solution design, consider the development specifications to avoid specification non-compliance problems. For details about the development specifications, see [[App Development Specifications|App Development Specifications]]. The following table lists the rules related to the scenario.

**Table 1** Solution design   
| Item | Planning | Related Development Specifications |
| :-- | :-- | :-- |
| Project and module | 
-   Project: info
-   Module: info

 | -   Rule: Asset Names Must Be Properly Set
-   Rule: Apps Must Be Properly Divided

 |
| Model | -   Category information table **info\_category**:
    -   **type\_id**: category ID
    -   **type\_name**: category name

-   Offering information table **info\_goods**:
    -   **goods\_id**: This field functions as the primary key and its value is of the sequence type.
    -   **goods\_name**: This field indicates the offering name and its value is of the text type.
    -   **goods\_picture**: image file type. PNG and JPG files are supported. The maximum size of a single file is 1000 KB.
    -   **goods\_price**: The value is of the decimal type.
    -   **goods\_type**: The value is of the reference type and the **info\_category** table is referenced.
    -   **goods\_description**: The value is of the text type.

 | -   Rule: To Open Access to the Frontend, Orchestration Models Must Be Associated with Permission Items
-   Rule: Proper Length Must Be Defined for the Text Type Property of a Rule Model
-   Suggestion: Properties of Decimal Type Must Be Used with Caution

 |
| Service | -   Automatically generated addition, deletion, modification, and query services
-   Permission item restrictions for services
-   Input parameter verification in services

 | -   Rule: To Open Access to the Frontend, Orchestration Services Must Be Associated with Permission Items
-   Rule: Use a Validator to Verify Service Input Parameters
-   Rule: The Parameter Validation on the Front-end Page Must Be Consistent with That on the Back-end Service Page and the Final Validation Must Be Performed on the Server

 |
| Page | -   Offering information query page
-   Page verification

 |
| Menu | Two menu entries are planned:

-   Offering category management. Only managers have the permission to view the **Goods Category Management** menu.
-   Offering information management. Common employees and managers have the permission to view the **Goods Information Management** menu.

 | N/A |
| Import service | Permission items are configured based on the automatically generated import service. | -   Rule: To Open Access to the Frontend, Data Import and Export Elements Must Be Associated with Permission Items
-   Rule: The Frontend Access Callback Policy Must Be Set to Restricted Callback in the Rule Import Template

 |
| Export service | Permission items are configured based on the automatically generated export service. |
| Roles and permissions | The following permission items are planned:

-   **menu\_goods\_info**: permission items on the offering information management page
-   **menu\_category**: permission items on the offering category page
-   **manageCategory**: permission items for adding, deleting, modifying, and querying offering categories
-   **manageGoodsinfo**: permission items for adding, deleting, modifying, and querying offering information
-   **importGoods**: permission item for importing offering information
-   **exportGoods**: permission item for exporting offering information

The following roles are planned:

-   **staff**: has the **menu\_goods\_info** and **manageGoodsinfo** permission items.
-   **manager**: has all the preceding permission items.

 | N/A | **Parent topic:** [[Developing an Offering Management App|Developing an Offering Management App]]