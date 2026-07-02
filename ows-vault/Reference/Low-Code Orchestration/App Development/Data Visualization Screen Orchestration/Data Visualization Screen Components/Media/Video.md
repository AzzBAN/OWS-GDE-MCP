---
title: "Video"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/video.html"
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
| Rotate | Rotation angle of the component with the center as the center point. The unit is degree (°). | ![[en-us_image_0000001771030657.png]]

**Table 2** Basic Properties  
| Name | Description |
| :-- | :-- |
| Resource Address | URL of the video to be embedded into the page. |
| Autoplay | After this property is configured, the video automatically will start playing as soon as possible and do not wait until all data to be loaded. |
| Control Panel | After this property is configured, the browser provides a control panel at the bottom of the video, allowing users to control the video playing, including volume, cross-frame, and suspension/resumption. |
| Cycle | After this function is enabled, the system automatically returns to the position where the video starts when the video play ends and continues playing the video. |
| Poster Frame Image | URL of the poster frame image, which is displayed when the video is being downloaded. If this property is not configured, no content is displayed before the first frame of the video is available, and then the first frame of the video is displayed as a poster frame. |