---
title: "Scatter Map"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/scatterMap.html"
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
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001607375861.png]]

**Table 2** Global configuration  
| Name | Description |
| :-- | :-- |
| Map Scope | Map display scope. The options are Preset and Custom.
-   Preset You can select a value from the drop-down list. Map data at the city level can be configured.
-   Custom
    -   **Title**: Map title, which is used to distinguish different maps on the same page. Therefore, when entering a custom map title, do not name multiple maps on the same page repeatedly.
    -   **JSON Map Data**: You can directly enter data or upload the JSON map data to the JSLib and enter the JSLib link. After data is uploaded to JSLib, copy the link **${staticContextPath}/${jslibPrefix}/${tenant\_id}/**_\[projectName\]_/_\[moduleName\]_**/echartmap/0.0.4/test.json** in **View List** and enter it.

 |
| Zoom | Zoom ratio of the map size. | ![[en-us_image_0000001557096668.png]]

**Table 3** Visual Map  
| Name | Description |
| :-- | :-- |
| Show | Whether to display the legend. |
| Type | Legend type, which can be set to Continuous or Precisewise. |
| Horizontal Position | Horizontal position of the legend, that is, whether the legend is placed on the left or right. |
| Vertical Position | Vertical position of the legend, that is, whether the legend is placed on the top or at the bottom. After setting both Horizontal Position and Vertical Position, you can determine whether the legend is displayed in the upper left corner, lower left corner, upper right corner, or lower right corner. |
| Item Width | Width of the legend. |
| Item Height | Height of the legend. |
| Top Text | Text corresponding to the maximum value of the legend. |
| Bottom Text | Text corresponding to the minimum value of the legend. |
| Min | Minimum value in a legend. |
| Max | Maximum value in a legend. |
| Min Color | Color of the minimum value. |
| Max Color | Color of the maximum value. |
| Text Style | Text style of the legend. You can set Font Family, Font Weight, Font Size, and Font Color. | ![[en-us_image_0000001556937216.png]]

**Table 4** Geo  
| Name | Description |
| :-- | :-- |
| Area Color | Color of a map area. |
| Border Color | Border color of each area on the map. |
| Border Width | Width of the border line in a map area. The unit is px. |
| Label | In the map area, you can set the font, width, size, and color for the text label of each map. | ![[en-us_image_0000001556778036.png]]

**Table 5** Series  
| Name | Description |
| :-- | :-- |
| Name | Scatter data series name, which can be displayed in the tooltip after you hover a mouse over a scatter. |
| Symbol | Scatter shape. |
| Symbol Size | Size of the scatter marker. |
| Ripple Effect Color | Color of the dynamic ripple effect around the data scatter. |
| Brush Type | Drawing mode of the dynamic ripple effect around the data scatter. Its value can be Fill or Stroke. |
| Period | Rendering speed of the ripple animation. The smaller the data, the faster the rendering speed. |
| Scale | Maximum zoom ratio of the ripple animation. |
| Label | Text label of the data value corresponding to the scatter. By default, the switch is disabled. After the switch is enabled, you can set Font Family, Font Weight, Font Size, and Font Color. | **Table 6** Tooltip  
| Name | Description |
| :-- | :-- |
| Show | Whether to show the prompt. |
| Background Color | Background color of the floating layer of the prompt. |
| Text Style | Text style of the floating layer of the prompt. You can set Font Family, Font Weight, Font Size, and Font Color. |