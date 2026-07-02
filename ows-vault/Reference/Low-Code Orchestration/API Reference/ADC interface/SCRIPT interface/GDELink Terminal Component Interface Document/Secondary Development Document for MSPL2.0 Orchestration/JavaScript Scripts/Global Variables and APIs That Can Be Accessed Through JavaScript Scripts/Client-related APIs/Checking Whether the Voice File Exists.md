---
title: "Checking Whether the Voice File Exists"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406477708.html"
depth: 9
---
#### U.isFileExist(path, callback) ⇒ boolean

Used to check whether the file exists in the provided path.

  
| Parameter | Type | Description |
| :-- | :-- | :-- |
| path | String | Path, which is a full path and does not support short URLs, for example, appname/pagename. |
| callback | Function | Callback function | Example:

U.isFileExist("file:///storage/.../test.jpg", function (result){
 // result: true,false
})