---
title: "Floating Notification Bar"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001367767701.html"
depth: 9
---
#### Nf.promptNotification

  
| Property | Type | Description |
| :-- | :-- | :-- |
| message | String | Message body |
| autoCloseTime | Number | Waiting time after which the floating notification bar is automatically closed. The unit is ms and the default value is 5000. | Style example:

![[en-us_image_0000001507549149.png]]

Example:

Nf.promptNotification({
  message:"The task module has changed, you needtextneedtextneedtext",
})