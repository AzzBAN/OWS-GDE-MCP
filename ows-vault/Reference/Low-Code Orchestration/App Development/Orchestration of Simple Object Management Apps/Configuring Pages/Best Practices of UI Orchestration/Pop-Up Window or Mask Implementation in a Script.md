---
title: "Pop-Up Window or Mask Implementation in a Script"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adcui/promptConfig.html"
depth: 5
---
#### Showing the Page Mask

let config={
   body:true,
   fullscreen:true,
   lock:true,
   spinner:"customSpinner",
   text:"Test",
   background:"red",
   customClass:"customClass"}
U.showMask(config)