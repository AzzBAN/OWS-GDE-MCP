---
title: "Region Map"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/regionMap.html"
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
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001607332701.png]]

**Table 2** Global configuration  
| Name | Description |
| :-- | :-- |
| Map Scope | Map display scope. The options are Preset and Custom.
-   Preset You can select a value from the drop-down list. Map data at the city level can be configured.
-   Custom
    -   **Title**: Map title, which is used to distinguish different maps on the same page. Therefore, when entering a custom map title, do not name multiple maps on the same page repeatedly.
    -   **JSON Map Data**: You can directly enter data or upload the JSON map data to the JSLib and enter the JSLib link. After data is uploaded to JSLib, copy the link **${staticContextPath}/${jslibPrefix}/${tenant\_id}/**_\[projectName\]_/_\[moduleName\]_**/echartmap/0.0.4/test.json** in **View List** and enter it.

 |
| Zoom | Zoom ratio of the map size. | ![[en-us_image_0000001607375317.png]]

**Table 3** Series  
| Name | Description |
| :-- | :-- |
| Name | Name of a data series, which is displayed when a tooltip is displayed after you hover a pointer over a data area. |
| Area Color | Default color of the map area before the data series is covered. |
| Border Color | Border color of each area on the map. |
| Border Width | Width of the border line of each area on the map. |
| Label | Area description text marked on each area of the map. You can set the font, width, size, and color. The text label switch is enabled by default. When the switch is disabled, Label is not displayed. | ![[en-us_image_0000001557255436.png]]

**Table 4** Visual Map  
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
| Text Style | Text style of the legend. You can set Font Family, Font Weight, Font Size, and Font Color. | ![[en-us_image_0000001556776688.png]]

**Table 5** Tooltip  
| Name | Description |
| :-- | :-- |
| Show | Whether to show the prompt. |
| Background Color | Background color of the floating layer of the prompt. |
| Text Style | Text style of the floating layer of the prompt. You can set Font Family, Font Weight, Font Size, and Font Color. |