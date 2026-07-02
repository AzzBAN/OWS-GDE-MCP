---
title: "Common Dialog Box"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001316319084.html"
depth: 7
---
#### Nf.prompt

There is only one close button in the dialog box.

  
| Property | Type | Description |
| :-- | :-- | :-- |
| title | String | (Optional) Title |
| message | String | Message body |
| okText | String | Text of the close button (default value: close) |
| yes | Function | Callback of the confirm button |
| autoCloseTime | Number | (Optional) Waiting time (unit: ms) after which the dialog box is automatically closed | Style example:

![[en-us_image_0000001508181897.png]]

Example:

Nf.prompt({
  title:"prompt",
  message:"prompt message",
  okText:"close"
})