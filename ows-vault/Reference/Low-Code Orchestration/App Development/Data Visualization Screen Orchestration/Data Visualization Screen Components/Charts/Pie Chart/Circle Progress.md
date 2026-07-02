---
title: "Circle Progress"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/circleProgress.html"
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
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001556466116.png]]

**Table 2** Common properties  
| Name | Description |
| :-- | :-- |
| Color | Several color schemes provided by the system by default. Developers can select a proper color as the chart color. |
| Animation | Whether to start the initial animation of a chart. |
| Animation Duration | Duration of the initial animation, in milliseconds. |
| Animation Easing | Slow-moving effect of the initial animation. For details about different slow-moving effects, see https://www.echartsjs.com/gallery/editor.html?c=line-easing. | ![[en-us_image_0000001607291041.png]]

**Table 3** Legend properties  
| Name | Description |
| :-- | :-- |
| Show | Whether to show a legend. |
| Position | Legend display position. |
| Icon | Icon of a legend item. ECharts provides the following icon types:
-   Circle
-   Rect
-   RoundRect
-   Triangle
-   Diamond
-   Pin
-   Arrow
-   None

 |
| Item Gap | Interval between items in the legend. Horizontal spacing is used for horizontal layout, and vertical spacing is used for vertical layout. |
| Item Width | Width of the legend marker. |
| Item Height | Height of the legend marker. |
| Text Style | Common text style of legends. | ![[en-us_image_0000001607090753.png]]

**Table 4** Tooltip  
| Name | Description |
| :-- | :-- |
| Show | Whether to show the prompt. |
| Background Color | Background color of the floating layer of a prompt. |
| Text Style | Text style of the floating layer of a prompt. | ![[en-us_image_0000001556411268.png]]

**Table 5** Series  
| Name | Description |
| :-- | :-- |
| Name | Series name, which is used to show prompts and filter legends. |
| Center | Center coordinate. The first item of the array is the horizontal coordinate, and the second item is the vertical coordinate. |
| Radius | Inner and outer radius of a ring. |
| Radius Difference Between Rings | Radius difference between rings. |
| Width | Width of a ring. | ![[en-us_image_0000001556411352.png]]

**Table 6** Text Config  
| Name | Description |
| :-- | :-- |
| Show | Whether to display the text in the middle. |
| Title Style | Text settings of the title. |
| Top | Ratio of the distance between the text and the top of the parent element to the overall height of the parent element. |
| Text | Text content of the subtitle. |
| Text Style | Text style of the subtitle. |