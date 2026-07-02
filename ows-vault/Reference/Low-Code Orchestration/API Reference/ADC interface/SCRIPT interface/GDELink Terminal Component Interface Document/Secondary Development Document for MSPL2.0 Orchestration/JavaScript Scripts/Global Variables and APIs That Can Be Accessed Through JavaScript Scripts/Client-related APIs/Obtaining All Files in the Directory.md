---
title: "Obtaining All Files in the Directory"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406957412.html"
depth: 9
---
#### U.getfilesList(params, callback)

Used to recursively obtain all sub-directories and files in a specified directory.

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| path | Path | /storage/.../business | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| path | Absolute file path. | /storage/.../business |
| size | File size, in bytes. This parameter exists only when the value of type is file. | 1024 |
| name | File name. | business |
| type | File type. dir and file indicate that the type is a directory or file, respectively. | dir |
| children | Subdirectory. This parameter exists only when the value of type is dir. | children: \[\] | Example:

  const params = {
    path: "/storage/emulated/0/com.huawei.gdelink/best/business"
  }
  U.getfilesList(params, function(result){});