---
title: "Migration Map"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/migrationMap.html"
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
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001557257148.png]]

**Table 2** Global configuration  
| Name | Description |
| :-- | :-- |
| Map Scope | Map display scope. The options are Preset and Custom.
-   Preset You can select a value from the drop-down list. Map data at the city level can be configured.
-   Custom
    -   **Title**: Map title, which is used to distinguish different maps on the same page. Therefore, when entering a custom map title, do not name multiple maps on the same page repeatedly.
    -   **JSON Map Data**: You can directly enter data or upload the JSON map data to the JSLib and enter the JSLib link. After data is uploaded to JSLib, copy the link **${staticContextPath}/${jslibPrefix}/${tenant\_id}/**_\[projectName\]_/_\[moduleName\]_**/echartmap/0.0.4/test.json** in **View List** and enter it.

 |
| Zoom | Zoom ratio of the map size. | ![[en-us_image_0000001557257552.png]]

**Table 3** Geo  
| Name | Description |
| :-- | :-- |
| Area Color | Color of a map area. |
| Border Color | Border color of each area on the map. |
| Border Width | Width of the border line in a map area, in px. |
| Label | In the map area, you can set the font, width, size, and color for the text label of each map. | ![[en-us_image_0000001557097756.png]]

**Table 4** Series  
| Name | Description |
| :-- | :-- |
| Color | Color of a migration line. |
| Width | Width of the migration line. |
| Type | Type of the migration line. |
| Curveness | Curvature of the migration line. |
| Start Symbol | Start marker of the migration line. |
| End Symbol | End marker of the migration line. |
| Symbol Size | Size of the migration line marker. | ![[en-us_image_0000001557257668.png]]

**Table 5** Tooltip  
| Name | Description |
| :-- | :-- |
| Show | Whether to show the prompt. |
| Background Color | Background color of the floating layer of the prompt. |
| Text Style | Text style of the floating layer of the prompt. You can set Font Family, Font Weight, Font Size, and Font Color. |