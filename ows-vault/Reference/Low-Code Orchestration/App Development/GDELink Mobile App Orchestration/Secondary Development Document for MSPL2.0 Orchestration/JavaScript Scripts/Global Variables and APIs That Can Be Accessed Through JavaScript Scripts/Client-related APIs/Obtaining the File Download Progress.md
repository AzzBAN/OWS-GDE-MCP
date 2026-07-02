---
title: "Obtaining the File Download Progress"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457197397.html"
depth: 7
---
#### U.downloadFileStatus(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| id | File ID | 12345 | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| id | File ID | 12345 |
| success | Whether the API is successfully executed | true |
| msg | Information about the downloaded file | download successful |
| status | File download status. -1 indicates that the file fails to be downloaded, 0 indicates that the file is downloading, and 1 indicates that the file is downloaded successfully. | 1 |
| progress | Download progress | 100 | Example:

const params = {
 id: "1408631227837067266"
}
U.downloadFileStatus(params,function(result){})