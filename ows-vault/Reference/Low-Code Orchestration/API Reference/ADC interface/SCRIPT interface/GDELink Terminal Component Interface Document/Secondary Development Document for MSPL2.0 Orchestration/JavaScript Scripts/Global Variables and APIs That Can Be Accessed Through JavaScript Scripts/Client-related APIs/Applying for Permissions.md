---
title: "Applying for Permissions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457397213.html"
depth: 9
---
#### U.requestPermissions(params, callback)

![[notice_3.0-en-us.png]]

Android and Harmony versions are supported.

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameter of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| permissions | Camera: camera; document read/write: file; dial: call\_phone | \['camera','file','call\_phone'\] | Example:

 U.requestPermissions({
   permissions: \['camera','file','call\_phone'\],
 },function(){})