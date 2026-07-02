---
title: "Selecting Images"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406477712.html"
depth: 7
---
#### U.chooseImage(params, callback)

Used to display the page for selecting original images.

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| total | Maximum number of options. | 3 |
| selectPaths | (Optional) Path of the selected image. Multiple images are separated by commas (,). | /storage/.../pic.png | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| filename | File name | 1612964724381.jpg |
| mimeType | MimeType of a file | image/jpg |
| fileSize | File size, in bytes | 1024 |
| fileUri | File access path, which starts with file:// | file:///storage/xxx/pic.png |
| filePath | File path | /storage/xxx/pic.png |
| width | Image width | 800 |
| height | Image height | 600 | Error information

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| errorCode | Error code | 1001 |
| errorMessage | Error description | You can not set total value <= 0 | Example:

  const params = {
    "total": "5",
    "selectPaths": "/storage/emulated/0/Pictures/1612964724381.jpg"
  };
  U.chooseImage(params,function(result){})