---
title: "Deleting a Database Table"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457117593.html"
depth: 9
---
#### U.dropTable(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameter of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| tableName | Table name | best | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| result | Returned result, which can be true or false | true |
| errorMessage | Error information | Failed to delete the table. | Example:

    const params = {
      "tableName": "best"
    };
    U.dropTable(params, function(result){});