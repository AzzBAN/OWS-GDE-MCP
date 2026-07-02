---
title: "Scanning the QR code"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457397221.html"
depth: 9
---
#### U.qrscan(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Example:

U.qrscan({
autoOpenLink: true //Automatically open the link page.
})
 
U.qrscan(null,function(res){
// res: Scanning result
})