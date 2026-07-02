---
title: "Frame Panel"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/framePanel.html"
depth: 5
---
#### Properties

-   **Id**: Component ID, which can be changed to a required value.
-   **Size**: The value includes width and height of the component. The unit is px.
-   **Position**: The value includes the horizontal coordinate and vertical coordinate of the component. The unit is px. The horizontal coordinate indicates the pixel distance between the upper left corner of the component and the left boundary of the page, and the vertical coordinate indicates the pixel distance between the upper left corner of the component and the upper boundary of the page.
-   **Rotate**: Rotation angle of the component with the center as the center point. The unit is degree (°).
-   Basic Properties
    
    ![[en-us_image_0000001607166545.png]]
    
    -   **Resource Address**: Resource address, which is the address of the page loaded by the panel. Its priority is lower than that of **Position**. That is, if both **Position** and **Resource Address** are configured, **Position** takes effect.
    -   **Interface Input Parameter**: Dynamic parameter values combined to the URL for specifying the page to which a URL redirects.