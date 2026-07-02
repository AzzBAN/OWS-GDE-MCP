---
title: "Converting the File to the Base64 Format"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001709593680.html"
depth: 9
---
#### U.fileToBase64(params, callback) ⇒ String

 
| Parameter | Type |
| :-- | :-- |
| params | String |
| callback | Function | Example:

let url = "http://xxx.xxx.xxx/1.jpg" 
let base64 = U.fileToBase64(url) 
document.getElementById("img").src = "data:image/jpeg;base64," + base64 
 
let url2 = "file:///xxx/xxx/2.jpg" 
function toBaseFun (result) { 
  document.getElementById("img").src = "data:image/jpeg;base64," + result 
} 
U.fileToBase64(url2, toBaseFun)