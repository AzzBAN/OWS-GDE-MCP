---
title: "Threshold Radar Chart"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/radarThresholdChart.html"
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
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001607340201.png]]

**Table 2** Common properties  
| Name | Description |
| :-- | :-- |
| Color | Several color schemes provided by the system by default. Developers can select a proper color as the chart color. |
| Animation | Whether to start the initial animation of a chart. |
| Animation Duration | Duration of the initial animation, in milliseconds. |
| Animation Easing | Slow-moving effect of the initial animation. For details about different slow-moving effects, see https://www.echartsjs.com/gallery/editor.html?c=line-easing. | ![[en-us_image_0000001557260568.png]]

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
| Text Style | Common text style of the legend. You can set Font Family, Font Weight, Font Size, and Font Color. | ![[en-us_image_0000001607380309.png]]

**Table 4** Radar coordinate system  
| Name | Description |
| :-- | :-- |
| Shape | Shape of the gradient ring line, which can be set to Circle or Polygon. |
| Split Number | Number of gradient ring lines. |
| Show | Whether to set the gap between two gradient ring lines to different colors for easy viewing. |
| Color | Two colors for the split area. |
| Axis Name | Whether to display the indication text of each data point on the radar chart. You can customize the text format and font style. |
| Series | Multiple data series can be added. | ![[en-us_image_0000001557260200.png]]

**Table 5** Series  
| Name | Description |
| :-- | :-- |
| Width | Line width of each linked data point. |
| Opacity | Transparency of the connection area of two data points. The value ranges from 0 (excluded) to 1. A smaller value indicates higher transparency. |
| Label | Text style of the data point. You can set Font Family, Font Weight, Font Size, and Font Color. | ![[en-us_image_0000001449300946.png]]![[en-us_image_0000001556781332.png]]

**Table 6** Threshold  
| Name | Description |
| :-- | :-- |
| Show | When this function is enabled, the threshold line is displayed. When this function is disabled, the threshold area is displayed. |
| Name | Threshold name. |
| Value | Equal-height threshold, that is, the same threshold is generated for all data points. The area formed by threshold lines is a regular polygon. The threshold setting takes effect only when the threshold data is not configured in data sources of the components in Data. |
| Line Style | Color, width, line type, and transparency of the threshold line when the threshold is displayed in line style. |
| Text Style | Text style of the threshold line. You can set Font Family, Font Weight, Font Size, and Font Color. | ![[en-us_image_0000001607499977.png]]

**Table 7** Tooltip  
| Name | Description |
| :-- | :-- |
| Show | Whether to show the prompt. |
| Background Color | Background color of the floating layer of the prompt. |
| Text Style | Text style of the floating layer of the prompt. |