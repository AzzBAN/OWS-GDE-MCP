---
title: "Decompressing Files"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457397217.html"
depth: 9
---
#### U.unzipFile(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| source | Source file path | /storage/.../assets.zip |
| path | Decompression path | /storage/.../business |
| id | Task ID | \- | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| id | Task ID | 123 |
| success | Whether the file is decompressed successfully | true |
| msg | Callback information. If the value of success is false, the callback information is error information. | The file is successfully decompressed. | Example:

  const params = {
    source: "/storage/emulated/0/com.huawei.gdelink/best/download/assets.zip",
    path: "/storage/emulated/0/com.huawei.gdelink/best/business",
    id: "123"
  }
  U.unzipFile(params,function(result){});