---
title: "Querying Data in the Database"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406477720.html"
depth: 9
---
#### U.queryInDatabase(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| tableName | Table name | best |
| columns | Table field | \["id","name","age","phone"\] or \[\] |
| whereClause | Search criteria | id=? and name=? |
| whereArgs | Value corresponding to the placeholder of the query condition | \["1","best"\] or \[":id",":name"\] |
| groupBy | Aggregate function (an empty string indicates that the function is not used) | name |
| having | Data of each group after filtering and grouping (an empty character string indicates that the data is not used) | sum(age)>100 |
| orderBy | Sorting of the result set by one or more columns (an empty string indicates that the result set is not used) | age desc or nameasc,age desc |
| offset | Paging offset | 0 |
| limit | Number of pages | 100 | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| result | Returned the data query result | \[{"phone":"13333333333","name":"best","id":"1","age":"100"}\] |
| errorMessage | Error information | Query failed. | Example:

 const params = {
   "appName": "best",
    "tableName": "best",
    "columns": \[
      "id",
      "name",
      "age",
      "phone"
    \],
    "whereClause": "id=?",
    "whereArgs": \["1"\],
    "groupBy": "name",
    "having": "sum(age)<100",
    "orderBy": "name asc,age desc",
    "offset": 0,
    "limit": 100
 }
 U.queryInDatabase(params, function(result){})