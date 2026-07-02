---
title: "Dual Gauge Chart"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/gaugeDoubleChart.html"
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
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001606706341.png]]

**Table 2** Common properties  
| Name | Description |
| :-- | :-- |
| Animation | Whether to start the initial animation of a chart. |
| Animation Duration | Duration of the initial animation, in milliseconds. |
| Animation Easing | Slow-moving effect of the initial animation. For details about different slow-moving effects, see https://www.echartsjs.com/gallery/editor.html?c=line-easing. | ![[en-us_image_0000001557056514.png]]

**Table 3** Tooltip  
| Name | Description |
| :-- | :-- |
| Show | Whether to show the prompt. |
| Background Color | Background color of the floating layer of the prompt. |
| Text Style | Text style of the floating layer of the prompt. | ![[en-us_image_0000001556897082.png]]

**Table 4** Series  
| Name | Description |
| :-- | :-- |
| Name | Series name, which is used to show prompts and filter legends. |
| Radius | Inner and outer radius of a ring. |
| Min | Minimum value of the gauge scale. |
| Max | Maximum value of the gauge scale. |
| Split Number | Number of segments of the gauge scale. |
| Width | Axis width of the gauge. |
| Color(0–100) | Axis color of different scale values on the gauge. The value indicates the percentage. |
| Progress | Whether to display the current progress. You can click to control. |
| Split Line | Split line on the scale. You can click to determine whether to display the split line. |
| Axis Tick | Axis scale configurations. You can click to determine whether to display the scale line. |
| Axis Label | Configurations about the scale label of the axis. You can click to determine whether to display the scale label. |
| Pointer | Style of the gauge pointer. You can click to determine whether to display the pointer. |
| Detail | Gauge details, which are used to display data. You can click to determine whether to display details. |
| Title | Title of the gauge. You can click to determine whether to display the title. | ![[en-us_image_0000001606937133.png]]

**Table 5** Progress  
| Name | Description |
| :-- | :-- |
| Round Cap | Whether to display the two ends of the progress bar in a circle. |
| Color | Color of the progress bar. |
| Width | Width of the progress bar. | ![[en-us_image_0000001607216845.png]]

**Table 6** Split Line  
| Name | Description |
| :-- | :-- |
| Length | Length of the split line on the scale. |
| Line Style | Style of a split line. | ![[en-us_image_0000001557057058.png]]

**Table 7** Axis Tick  
| Name | Description |
| :-- | :-- |
| Split Number | Number of scales divided between split lines. |
| Length | Length of the scale line. |
| Line Style | Style of the scale line. |
| Axis Label | Text of the label on the scale. You can click to determine whether to display the scale label. | ![[en-us_image_0000001607297433.png]]

**Table 8** Axis Label  
| Name | Description |
| :-- | :-- |
| Text Style | Text style of the scale label. | ![[en-us_image_0000001557177074.png]]

**Table 9** Pointer  
| Name | Description |
| :-- | :-- |
| Length | Pointer length. |
| Width | Pointer width. |
| Offset Center | Offset position relative to the gauge center. The first item in the array is the horizontal offset, and the second item is the vertical offset. | ![[en-us_image_0000001556738354.png]]

**Table 10** Details  
| Name | Description |
| :-- | :-- |
| Offset Center | Offset position relative to the gauge center. The first item in the array is the horizontal offset, and the second item is the vertical offset. |
| Text Style | Text style of the content in Detail. |
| Unit | Unit of the value displayed in Detail. | ![[en-us_image_0000001607297577.png]]

**Table 11** Title  
| Name | Description |
| :-- | :-- |
| Offset Center | Offset position relative to the gauge center. The first item in the array is the horizontal offset, and the second item is the vertical offset. |
| Line Style | Text style of the title. |