---
title: "Packaging the Offering Management App"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/demo_021.html"
depth: 4
---
#### Procedure

1.  Open the created project, click ![[en-us_image_0000001591696293.png]], and select **App** from the **Packaged Into** list.
2.  In the displayed dialog box, set basic packaging information.
    
    ![[en-us_image_0000001618525913.png]]
    
    **Table 1** Parameter description  
    | Parameter | Description |
    | :-- | :-- |
    | Version | The version format is fixed to n.n.n, where n is a digit. Other version formats are invalid. By default, the version starts from 0.0.1. Each time a packaging task is executed, the version increases. You can manually change the version of an app package and package the app package of an earlier version. For example, if you package apps of 0.0.1 and 0.0.2 and then package the app of 0.0.1, the assets in the local asset library are updated to the newly packaged assets of 0.0.1. |
    | Version Type | You can set this parameter to Beta Version or Official Version for distinguishing. |
    | Asset Catalog | Category of a service. Available values are asset catalogs in the asset library. For details about how to add an asset catalog, see Managing Labels. | 3.  Click **Pack**.
4.  After the system displays a message indicating that the packaging is successful, click **Download** to obtain the application package file.