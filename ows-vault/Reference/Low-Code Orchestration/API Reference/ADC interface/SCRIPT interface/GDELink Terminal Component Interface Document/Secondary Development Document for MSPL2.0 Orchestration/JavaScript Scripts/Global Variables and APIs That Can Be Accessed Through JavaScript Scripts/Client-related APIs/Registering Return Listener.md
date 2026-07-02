---
title: "Registering Return Listener"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406637628.html"
depth: 9
---
#### U.registerBackPressListener(callback)

![[notice_3.0-en-us.png]]

Android and Harmony versions are supported.

 
| Parameter | Type |
| :-- | :-- |
| callback | Function | Example:

  U.registerBackPressListener(function(){
    // to do something
    if(window.onBackPressed){
      window.onBackPressed();
    }
  })