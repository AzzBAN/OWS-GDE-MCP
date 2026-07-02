---
title: "Generating a QR Code"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457277253.html"
depth: 7
---
#### U.generateQRcode(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | String |
| callback | Function | Example:

U.generateQRcode("xxx",function(res){
// xxx: Content of the QR code to be generated; res: Base64 format of the QR code image
})