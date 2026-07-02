---
title: "Updating Data in the Database"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406637632.html"
depth: 9
---
#### U.updateInDatabase(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| tableName | Table name | best |
| data | Data | {"id":1,"name":"best","age":100,"phone":"13333333333"} |
| whereClause | Update condition | id=? and name=? |
| whereArgs | Value corresponding to the placeholder of the update condition | \["1","best"\] or \[":id",":name"\] | Example:

//Update a single data record.
  const param = {
    "appName": "best",
    "tableName": "best",
    "data": {
      "name": "huawei",
      "age": 90,
      "phone": "15555555555"
    },
    "whereClause": "id=? and name=?",
    "whereArgs": \["1", "best"\]
  }
  U.updateInDatabase(param, function(result){});
 
  //Update data in batches.
  const param2 = {
    "appName": "best",
    "tableName": "best",
    "data": \[{
      "name": "huawei",
      "age": 90,
      "phone": "15555555555"
    },{
      "name": "huawei2",
      "age": 91,
      "phone": "15555555556"
    }\],
    "whereClause": "id=? and name=?",
    "whereArgs": \[":id", ":name"\]
  }
  U.updateInDatabase(param2, function(result){})