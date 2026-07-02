---
title: "Confirmation Dialog Box"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001316479060.html"
depth: 9
---
#### Nf.promptConfirm

**OK** and **Cancel** buttons are displayed in the dialog box.

  
| Property | Type | Description |
| :-- | :-- | :-- |
| title | String | (Optional) Title |
| message | String | Message body |
| okText | String | Text of the confirm button Default value: OK |
| cancelText | String | Text of the cancel button Default value: Cancel |
| yes | Function | Callback of the confirm button |
| no | Function | Callback of the cancel button |
| autoCloseTime | Number | (Optional) Waiting time (unit: ms) after which the dialog box is automatically closed | Style example:

![[en-us_image_0000001457788350.png]]

Example:

Nf.promptConfirm({
  title:"prompt title",
  message:"prompt message",
  okText:"confirm",
  cancelText:"exit",
  yes: function () {
    console.log ("confirm is clicked");
  },
  no:function(){
    console.log("exit is clicked");
  }
});