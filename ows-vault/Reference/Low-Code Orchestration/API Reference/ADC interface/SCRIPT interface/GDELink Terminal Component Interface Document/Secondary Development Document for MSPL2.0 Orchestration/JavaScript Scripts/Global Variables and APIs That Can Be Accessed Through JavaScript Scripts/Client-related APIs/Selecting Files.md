---
title: "Selecting Files"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406797444.html"
depth: 9
---
#### U.chooseFile(params, callback)

Used to display the page for selecting original files.

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| multiSelect | Whether to select multiple files | true |
| fileNumberLimit | Maximum size of a single file, in KB | 1024 | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| filename | File name | 1.txt |
| mimeType | MimeType of a file | text/plain |
| fileSize | File size, in bytes | 1024 |
| fileUri | File access path, which starts with file:// and is used to display images | file:///storage/.../pic.png |
| filePath | File path | /storage/.../pic.png | Example:

  const params = {
    "fileTypeExts": ".jpg,.png,.bmp,.jpeg,.flv,.f4v,.mp4",
    "singleSizeLimit": 102400
  }
  U.chooseFile(params,function(result){});