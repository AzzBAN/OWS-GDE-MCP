---
title: "Downloading Files"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406637620.html"
depth: 7
---
#### U.downloadFile(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

   
| params | Sub-parameter | Description | Example Value |
| :-- | :-- | :-- | :-- |
| url | \- | Download URL | http://xxx.xxx |
| id | \- | Download task ID | UUID |
| method | \- | (Optional) Request method | GET/POST (GET by default) |
| headers | \- | (Optional) Request header | \- |
| params | \- | (Optional) Request parameter | { "id": "123"} |
| path | \- | Storage path, which needs to be transferred when a single file is downloaded | \- |
| files | \- | Parameter required for downloading multiple files, which is an array | \- |
| id | ID of the downloaded file | \- |
| params | Request parameter | \- |
| path | Storage path | \- | Callback parameters

   
| Parameter | Sub-parameter | Description | Example Value |
| :-- | :-- | :-- | :-- |
| id | \- | Download task ID | UUID |
| success | \- | Whether the file is successfully downloaded | true/false |
| msg | \- | Error information | Download timed out |
| responses | \- | Response body | \- |
| id | File ID | 1 |
| response | If the value is an empty string, the download is successful. Otherwise, the download is abnormal. | \- | Example:

//Download a single file.
  const param = {
    "url": "xxx.xxx",
    "params": {
      "id": "123"
    },
    "path": "/storage/emulated/0/Android/data/com.huawei.gdelink/files/best",
    "id": "1408631227837067266"
  }
  U.downloadFile(param,function(result){})
 
//Download multiple files.
  const param2 = {
    "id": "12345",
    "url": "xxx.xxx",
    "files": \[
      {
        "id": "1",
        "params": {
          "id": "1406117530287747073",
        },
        "path": "/storage/emulated/0/Android/data/com.huawei.gdelink/files/best"
      },
      {
        "id": "2",
        "params": {
          "id": "1405713899638063106",
        },
        "path": "/storage/emulated/0/Android/data/com.huawei.gdelink/files/best"
      }
    \]
  }
  U.downloadFile(param2,function(result){})