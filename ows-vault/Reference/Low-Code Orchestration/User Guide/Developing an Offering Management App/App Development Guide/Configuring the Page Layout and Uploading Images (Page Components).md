---
title: "Configuring the Page Layout and Uploading Images (Page Components)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/demo_009.html"
depth: 4
---
#### Scenario Description

According to the description in [[Configuring Data Models (Offering Category Table and Information Table)|Configuring Data Models (Offering Category Table and Information Table)]], the **info\_goods\_create**, **info\_goods\_grid**, and **info\_goods\_update** pages are automatically generated.

The **info\_goods\_create** page is adjusted. After you click **info\_goods\_create** and access the page designer, the automatically generated page is shown in the following figure.

![[en-us_image_0000001535717570.png]]

The automatically generated pages do not fully meet service requirements and need to be adjusted as follows:

-   The **goods\_id** field is automatically generated and its value does not need to be entered. This field can be deleted from the input parameter. That is, this field is not displayed and its value does not need to be transferred.
-   The format and size of the file to be uploaded must be set for **goods\_picture**. In addition, this field is displayed as **Offering Image**.
-   The field sequence is adjusted. The **goods\_type** and **goods\_name** fields are placed in the first row, and the **goods\_description** field is moved to the last row.
-   **goods\_price** is displayed as **Offering Price**. **goods\_name** is displayed as **Offering Name**. **goods\_description** is displayed as **Offering Introduction**. **goods\_type** is displayed as **Offering Category**.