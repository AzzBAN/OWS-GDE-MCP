---
title: "Inserting Data into the Database"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406957420.html"
depth: 9
---
#### U.insertInDatabase(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| tableName | Table name | best |
| data | Data | {"id":1,"name":"best","age":100,"phone":"13333333333"} | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| result | Returned the data insertion result | 1 |
| errorMessage | Error information | Failed to insert data into the database. | Example:

//Insert a single data record.
 let params = {
    "tableName": "best",
    "data": {
      "id": 1,
      "name": "best",
      "age": 100,
      "phone": "13333333333"
    }
 }
 U.insertInDatabase(params, function(result){})
 
//Insert multiple data records.
 let params2 = {
    "tableName": "best",
    "data": \[{
      "id": 1,
      "name": "best",
      "age": 100,
      "phone": "13333333333"
    },{
      "id": 2,
      "name": "best2",
      "age": 20,
      "phone": "13344444444"
    }\]
 }
 U.insertInDatabase(params2, function(result){})