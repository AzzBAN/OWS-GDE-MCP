---
title: "Uploading Files"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457117581.html"
depth: 7
---
#### U.uploadFile(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

   
| Parameter | Sub-parameter | Description | Example Value |
| :-- | :-- | :-- | :-- |
| url | \- | Upload URL | https://xxx.xxx |
| id | \- | Upload task ID | 12345 |
| headers | \- | Request header | \- |
| params | \- | Request parameter | { "id": "1405713899638063106"} |
| path | \- | Storage path, which is required for uploading a single file | \- |
| files | \- | Parameter required for uploading multiple files, which is an array | \- |
| id | ID of the uploaded file | \- |
| params | Request parameter | \- |
| path | Storage path | \- | Callback parameters

   
| Parameter | Sub-parameter | Description | Example Value |
| :-- | :-- | :-- | :-- |
| id | \- | Upload task ID | 12345 |
| success | \- | Whether the file is successfully uploaded | true/false |
| msg | \- | Error information | Upload timed out |
| responses | \- | Response body | \- |
| id | File ID | 1 |
| response | If the value is an empty string, the upload is successful. Otherwise, the upload is abnormal. | \- | Example:

//Upload a single file.
  const params = {
    "url": "xxx.xxx",
    "headers": {
      "Content-Type": "multipart/form-data"
    },
    "params": {
      "id": "1408631227837067266"
    },
    "path": "/storage/emulated/0/Android/data/com.huawei.gdelink/files/best/66.jpg",
    "id": "1408631227837067266"
  };
  U.uploadFile(params,function(result){});
 
//Upload multiple files.
  const params2 = {
    "id": "1408631227837067266",
    "url": "xxx.xxx",
    "files": \[
      {
        "id": "1",
        "params": {
          "id": "1406117530287747073",
        },
        "path": "/storage/emulated/0/Android/data/com.huawei.gdelink/files/best/1.jpg"
      },
      {
        "id": "2",
        "params": {
          "id": "1405713899638063106",
        },
        "path": "/storage/emulated/0/Android/data/com.huawei.gdelink/files/best/2.jpg"
      }
    \]
  };
  U.uploadFile(params2,function(result){});