---
title: "Nested Pie Chart"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/pieNestedChart.html"
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
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001556673138.png]]

**Table 2** Common properties  
| Name | Description |
| :-- | :-- |
| Color | Several color schemes provided by the system by default. Developers can select a proper color as the chart color. |
| Animation | Whether to start the initial animation of a chart. |
| Animation Duration | Duration of the initial animation, in milliseconds. |
| Animation Easing | Slow-moving effect of the initial animation. For details about different slow-moving effects, see https://www.echartsjs.com/gallery/editor.html?c=line-easing. |
| Carousel | Rotation effect of a chart. |
| Interval | Dwell duration on a single piece of data during play. | ![[en-us_image_0000001556569084.png]]

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
| Text Style | Common text style of legends. | ![[en-us_image_0000001556407864.png]]

**Table 4** Series  
| Name | Description |
| :-- | :-- |
| Name | Series name, which is used to show prompts and filter legends. |
| Center | Center coordinate. The first item of the array is the horizontal coordinate, and the second item is the vertical coordinate. |
| Radius | Inner and outer radius of a ring. |
| Color | Color of each data item in a ring. |
| Border Width | Border width of each sector. |
| Border Radius | Radius of the rounded corner of the sector. | ![[en-us_image_0000001556567824.png]]

**Table 5** Highlighted text style  
| Name | Description |
| :-- | :-- |
| Wrap | Whether to start a new line. |
| Data Name | Data name. You can click to determine whether to display the data name. |
| Data Value | Text of the data value. You can click to determine whether to display the data text. |
| Formatter | You can set the data display format. The options are Percentage, Data, and None. If None is selected, no data is displayed. |
| Text Style | Text style of the data text. |
| Description | Data description. You can click to determine whether to display the description. |
| Text | Content of the description text. |
| Text Style | Style of the description text. | ![[en-us_image_0000001556248996.png]]

**Table 6** Halo Effect  
| Name | Description |
| :-- | :-- |
| Show | Whether to enable the halo effect at the edge. |
| Color | Fill color at the edge of the ring. | ![[en-us_image_0000001607288237.png]]

**Table 7** Tooltip  
| Name | Description |
| :-- | :-- |
| Show | Whether to show the prompt. |
| Background Color | Background color of the floating layer of a prompt. |
| Text Style | Text style of the floating layer of a prompt. |