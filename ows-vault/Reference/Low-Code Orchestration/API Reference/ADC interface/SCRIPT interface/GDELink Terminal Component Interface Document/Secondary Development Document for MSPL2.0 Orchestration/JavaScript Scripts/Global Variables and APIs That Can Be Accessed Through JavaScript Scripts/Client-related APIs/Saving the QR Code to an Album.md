---
title: "Saving the QR Code to an Album"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406797448.html"
depth: 9
---
#### U.saveAlbum(params, callback)

Used to upload the image data encoded in Base64 format and save the image to the album of the mobile phone.

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameter of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| params | Data encoded in Base64 format | Data encoded in Base64 format | Example:

 const params = {
params: "Data encoded in Base64 format"
 }
 U.saveAlbum(params, function(result){
// result: Success or failed
 })