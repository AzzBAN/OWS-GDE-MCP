---
title: "Threshold Chart"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/thresholdChart.html"
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
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001556513138.png]]

**Table 2** Common  
| Name | Description |
| :-- | :-- |
| Color | Several sets of colors provided by the system by default. Select a proper one as the chart color. |
| Animation | Whether to start the initial animation of a chart. |
| Animation Duration | Duration of the initial animation, in milliseconds. |
| Animation Easing | Slow-moving effect of the initial animation. For details about different slow-moving effects, see https://www.echartsjs.com/gallery/editor.html?c=line-easing. |
| Padding | Drawing grid margin in the rectangular coordinate system. | Legend

![[en-us_image_0000001607045273.png]]

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
| Text Style | Common text style of legends. | ![[en-us_image_0000001556551388.png]]

![[en-us_image_0000001556232720.png]]

**Table 4** X axis  
| Name | Description |
| :-- | :-- |
| Show | Whether to display the X axis. |
| Type | Axis type. |
| Position | Location of the X axis. |
| Min | Minimum scale of the coordinate axis. You can set this parameter to Data Min. In this case, the minimum value of the data on the axis is used as the minimum scale. If this parameter is not set, the minimum value is automatically calculated to ensure even distribution of axis scales. |
| Max | Maximum value of the axis scale. You can set this parameter to Data Max. In this case, the maximum value of the data on the axis is used as the maximum scale. If this parameter is not set, the maximum value is automatically calculated to ensure even distribution of axis scales. |
| Name | Axis name. |
| Name Location | Display position of an axis name. |
| Name Text Style | Text style of the axis name. |
| Name Gap | Distance between the axis name and axis line. |
| Name Rotate | Rotation angle of an axis name. |
| Axis Line | Axis line configurations. You can click to determine whether to display the axis line. |
| Axis Tick | Axis scale configurations. You can click to determine whether to display the scale. |
| Axis Label | Configurations about the scale label of the axis. You can click to determine whether to display the scale label. |
| Split Line | Split line of the axis in the grid area. You can click to determine whether to display the split line. | ![[en-us_image_0000001606912177.png]]

**Table 5** Axis Tick  
| Name | Description |
| :-- | :-- |
| Inside | Whether the axis scale faces inwards. By default, the axis scale faces outwards. |
| Length | Length of the coordinate axis scale. |
| Line Style | Style settings of the scale line. | ![[en-us_image_0000001556552796.png]]

**Table 6** Scale label  
| Name | Description |
| :-- | :-- |
| Inside | Whether the scale label faces inwards. By default, the scale label faces outwards. |
| Rotate | Rotation angle of the scale label. When the category label of the category axis cannot be displayed, you can rotate the scale label to prevent the labels from overlapping. The rotation angle ranges from -90 degrees to 90 degrees. |
| Margin | Distance between the scale label and the axis line. |
| Text Style | Text font style. | ![[en-us_image_0000001556393572.png]]

![[en-us_image_0000001556553368.png]]

**Table 7** Y axis  
| Name | Description |
| :-- | :-- |
| Show | Whether to display the Y axis. |
| Type | Axis type. |
| Split Number | Number of segments on the coordinate axis. Note that the number of segments is only an estimated value. The actual value is adjusted based on the readability of the scale on the coordinate axis after splitting. |
| Min | Minimum scale of the coordinate axis. You can set this parameter to Data Min. In this case, the minimum value of the data on the axis is used as the minimum scale. If this parameter is not set, the minimum value is automatically calculated to ensure even distribution of axis scales. |
| Max | Maximum value of the axis scale. You can set this parameter to Data Max. In this case, the maximum value of the data on the axis is used as the maximum scale. If this parameter is not set, the maximum value is automatically calculated to ensure even distribution of axis scales. |
| Name | Axis name. |
| Name Location | Display position of an axis name. |
| Name Text Style | Text style of the axis name. |
| Name Gap | Distance between the axis name and axis line. |
| Name Rotate | Rotation angle of an axis name. |
| Axis Line | Axis line configurations. You can click to determine whether to display the axis line. |
| Axis Tick | Axis scale configurations. For details, see Table 5. |
| Axis Label | Configurations about the scale label of the axis. For details, see Table 6. |
| Split Line | Split line of the axis in the grid area. You can click to determine whether to display the split line. | ![[en-us_image_0000001556713452.png]]

**Table 8** Tooltip  
| Name | Description |
| :-- | :-- |
| Show | Whether to show the prompt. |
| Background Color | Background color of the floating layer of a prompt. |
| Text Style | Text style of the floating layer of a prompt. |
| Line Style | Style of the axis indicator line. | ![[en-us_image_0000001607073473.png]]

**Table 9** Series  
| Name | Description |
| :-- | :-- |
| Name | Series name, which is used to show prompts and filter legends. |
| Color | Chart color. |
| Show Symbol | Whether to display the marker icon. |
| Symbol Size | Size of a symbol. |
| Step | Configurations of a step line. The options are Close, Start, Middle, and End. |
| Smooth | Whether to display data using the smooth curve. |
| Area Style | Area filling style. After the setting, the area chart is displayed. When Opacity is 0, the chart is not drawn. |
| Stack | Data stacking. |
| Line Style | Line style. Note: Changing the color does not affect the legend color. If you want that the legend color is the same as the line chart color, change the chart color. The line color is changed accordingly by default. |
| Label | Text label on a chart, which can be used to describe some data information of the chart, such as the value and name. You can click to determine whether to display the text label. | ![[en-us_image_0000001607193625.png]]

**Table 10** Label  
| Name | Description |
| :-- | :-- |
| Position | Label position. |
| Distance | Distance between text labels and chart elements. |
| Rotate | Label rotation angle, which ranges from -90 degrees to 90 degrees. The positive value indicates a counter-clockwise rotation. |
| Color | Text color. | ![[en-us_image_0000001556553820.png]]

**Table 11** Marking line  
| Name | Description |
| :-- | :-- |
| Show | Whether to display the marking line, which is displayed by default. |
| Symbol | Marker types at both ends. |
| Data | Value at a marking line. |
| Color Lower Then Mark Line | Color of the line below the marking line. |
| Color Higher Then Mark Line | Color of the line above the marking line. |
| Color | Color of the marking line. |
| Width | Width of the marking line. |
| Type | Type of the marking line. |
| Show | Whether to display the label on the marking line. By default, the label is not displayed. |
| Label Style | Label style. |