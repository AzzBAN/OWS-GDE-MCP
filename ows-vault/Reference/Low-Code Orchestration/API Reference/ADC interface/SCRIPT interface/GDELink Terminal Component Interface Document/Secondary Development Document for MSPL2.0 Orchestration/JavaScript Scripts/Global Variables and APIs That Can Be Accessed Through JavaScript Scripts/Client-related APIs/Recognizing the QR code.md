---
title: "Recognizing the QR code"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406957416.html"
depth: 9
---
#### U.scanCode(params, callback)

Used to recognize the Base64 code of an image or the QR code in the image path.

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameter of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| params | base64 data or file:///Address | file:///storage/emulated/0/Pictures/1612964724381.jpg | Example:

  const params = {
    params: "file:///storage/emulated/0/Pictures/1612964724381.jpg"
  }
  U.scanCode(params,function(result){
//result: QR code information, which is of the String type
  })