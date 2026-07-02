---
title: "Creating Database Tables"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457277257.html"
depth: 7
---
#### U.createTable(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

   
| Parameter | Sub-parameter | Description | Example Value |
| :-- | :-- | :-- | :-- |
| tableName | \- | Table name | best |
| tableField | \- | Field | Object |
| tableId | Table primary key | id |
| tabileFields | Table field | "tableFields": \["name","age","phone"\] |
| tableFieldTypes | Table field type. Only text character strings, integers, and double-precision decimals are supported. | The value is an array. | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| result | true/false | true |
| errorMessage | Error information | Failed to create the table. | Example:

  const params = {
    "tableName": "best",
    "tableField": {
      "tableId": "id",
        "tableFields": \[
        "name",
        "age",
        "phone"
      \],
      "tableFieldTypes":\[
        "text",
        "integer",
        "text"
      \]
    }
  }
  U.createTable(params,function(result){})