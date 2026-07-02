---
title: "Success Dialog Box"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001367647825.html"
depth: 7
---
#### Nf.promptSuccess

  
| Property | Type | Description |
| :-- | :-- | :-- |
| title | String | (Optional) Title |
| message | String | Message body |
| okText | String | (Optional) Text of the confirm button (no default value) |
| cancelText | String | (Optional) Text of the cancel button (no default value) |
| yes | Function | Callback of the confirm button |
| no | Function | Callback of the cancel button |
| autoCloseTime | Number | (Optional) Waiting time (unit: ms) after which the dialog box is automatically closed | Style example 1:

![[en-us_image_0000001507669853.png]]

Example 1:

Nf.promptSuccess({
  title:"success title",
  message:"success message",
  cancelText: "cancel",
  okText:"close",
  yes:function(){
    console.log("confirm is clicked");
  },
  no: function() {
    console.log("cancel is clicked")
  }
});

Only the message body is displayed. The button is omitted.

Style example 2:

![[en-us_image_0000001457789206.png]]

Example 2:

Nf.promptSuccess({
  title:"success title",
  message:"success message"
});