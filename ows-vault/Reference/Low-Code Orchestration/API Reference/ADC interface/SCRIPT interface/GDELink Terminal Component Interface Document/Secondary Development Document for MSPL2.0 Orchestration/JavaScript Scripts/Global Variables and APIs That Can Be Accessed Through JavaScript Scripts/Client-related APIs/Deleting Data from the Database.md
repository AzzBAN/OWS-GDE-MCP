---
title: "Deleting Data from the Database"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457197409.html"
depth: 9
---
#### U.deleteInDatabase(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| tableName | Table name | best |
| whereClause | Deletion condition | id=? and name=? |
| whereArgs | Value corresponding to the placeholder of the deletion condition | \["1","best"\] | Example:

  const params = {
    "tableName": "best",
    "whereClause": "id=?",
    "whereArgs": \["1"\]
  }
  U.deleteInDatabase(params,function(result){});