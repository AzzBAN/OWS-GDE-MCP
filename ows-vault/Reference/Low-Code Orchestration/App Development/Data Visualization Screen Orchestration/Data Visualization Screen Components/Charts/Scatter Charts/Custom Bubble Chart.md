---
title: "Custom Bubble Chart"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/customBubbleChart.html"
depth: 6
---
#### Properties

**Table 1** Fundamental properties  
| Name | Description |
| :-- | :-- |
| Hidden | Whether to hide a component. If a component is hidden by default, components in the group can no longer use unified data sources. |
| Id | Component ID, which can be changed to a required value. |
| Size | The value includes width and height of the component. The unit is px. |
| Position | The value includes the horizontal coordinate and vertical coordinate of the component. The unit is px. The horizontal coordinate indicates the pixel distance between the upper left corner of the component and the left boundary of the page, and the vertical coordinate indicates the pixel distance between the upper left corner of the component and the upper boundary of the page. |
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001557101276.png]]

**Table 2** Common properties  
| Name | Description |
| :-- | :-- |
| Color | Several color schemes provided by the system by default. Developers can select a proper color as the chart color. |
| Animation | Whether to start the initial animation of a chart. |
| Animation Duration | Duration of the initial animation, in milliseconds. |
| Animation Easing | Slow-moving effect of the initial animation. For details about different slow-moving effects, see https://www.echartsjs.com/gallery/editor.html?c=line-easing. | ![[en-us_image_0000001556782392.png]]

-   **Label**: controls the display of text in the bubble. You can control the font style of the data name and text, and whether the data name and text are displayed in the same line or in different lines.
-   **Border Width**: width of a bubble border, in px.
-   **Max Bubble Size**: maximum diameter of a bubble, in px.
-   **Min Bubble Size**: minimum diameter of a bubble, in px.
-   **Bubble Color**: You can set different colors for different bubbles.
-   **Display Decorative Bubble**: whether to display decorative bubbles.