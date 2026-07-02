---
title: "Ticker Board"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/digitalFlipper.html"
depth: 5
---
#### Properties

**Table 1** Fundamental properties  
| Name | Description |
| :-- | :-- |
| Hidden | Whether to hide a component. If a component is hidden by default, components in the group can no longer use unified data sources. |
| Id | Component ID, which can be changed to a required value. |
| Size | The value includes width and height of the component. The unit is px. |
| Position | The value includes the horizontal coordinate and vertical coordinate of the component. The unit is px. The horizontal coordinate indicates the pixel distance between the upper left corner of the component and the left boundary of the page, and the vertical coordinate indicates the pixel distance between the upper left corner of the component and the upper boundary of the page. |
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001556904486.png]]

**Table 2** Theme Configuration  
| Name | Description |
| :-- | :-- |
| Theme Style | Theme style of the ticker board. The options are None, Border, 3D, and Pure Color. |
| Theme Color | Theme color of the ticker board. | ![[en-us_image_0000001556904594.png]]

**Table 3** Text Configuration  
| Name | Description |
| :-- | :-- |
| Display Precision | Display precision of digits. The default value is two decimal places. |
| Font Configuration | Font style of digits. |
| Digit Interval | Interval between digits, in px. |
| Show Separator | Whether to display the separator between digits. |
| Separator | Separator between digits. |
| Show Separator Background | Whether to display the background of the separator between digits. If this function is enabled, the background is the same as the theme style. |
| Number of Digits for Separation | Number of digits for separation. | ![[en-us_image_0000001557186234.png]]

**Table 4** Prefix Configuration  
| Name | Description |
| :-- | :-- |
| Static Display | Whether to display the prefix statically. If this function is enabled, the prefix is displayed regardless of the conditions. If this function is disabled, you need to configure the minimum value and maximum value and the prefix is displayed only when the data falls between the two values. |
| Min Value | Minimum value for prefix display. This parameter can be configured only when the Static Display function is disabled. |
| Max Value | Maximum value for prefix display. This parameter can be configured only when the Static Display function is disabled. |
| Content Type | Type of the content displayed in the prefix. The options are None, Text, Icon, and Image. | ![[en-us_image_0000001556749990.png]]

**Table 5** Properties when Content Type is set to Text  
| Name | Description |
| :-- | :-- |
| Text Content | Text content to be displayed in the prefix. This parameter can be configured only when Content Type is set to Text. |
| Font | Text style of the prefix. This parameter can be configured only when Content Type is set to Text. | ![[en-us_image_0000001607309669.png]]

**Table 6** Properties when Content Type is set to Icon  
| Name | Description |
| :-- | :-- |
| Icon | Icon to be displayed for the prefix. This parameter can be configured only when Content Type is set to Icon. |
| Icon Color | Icon color for the prefix. This parameter can be configured only when Content Type is set to Icon. | ![[en-us_image_0000001556910118.png]]

**Table 7** Properties when Content Type is set to Image  
| Name | Description |
| :-- | :-- |
| Image | Image to be displayed for the prefix. This parameter can be configured only when Content Type is set to Image. |
| Image Width | Image width. This parameter can be configured only when Content Type is set to Image. |
| Image Height | Image height. This parameter can be configured only when Content Type is set to Image. | ![[en-us_image_0000001556751110.png]]

**Table 8** Suffix Configuration  
| Name | Description |
| :-- | :-- |
| Static Display | Whether to display the prefix statically. If this function is enabled, the suffix is displayed regardless of the conditions. If this function is disabled, you need to configure the minimum value and maximum value and the suffix is displayed only when the data falls between the minimum value and the maximum value. |
| Content Type | Type of the content to be displayed for the suffix. The options are None, Text, Icon, and Image. | ![[en-us_image_0000001556751282.png]]

**Table 9** Animation Settings  
| Name | Description |
| :-- | :-- |
| Animation Duration | Animation duration of digits in the ticker board. |
| Change Interval | Interval of digit changes in the ticker board. |