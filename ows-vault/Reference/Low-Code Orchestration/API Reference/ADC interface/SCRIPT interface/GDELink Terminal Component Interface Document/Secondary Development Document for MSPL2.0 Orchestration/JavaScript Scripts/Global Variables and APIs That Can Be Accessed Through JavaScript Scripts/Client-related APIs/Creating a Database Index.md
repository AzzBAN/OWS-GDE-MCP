---
title: "Creating a Database Index"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406797452.html"
depth: 9
---
#### U.createTableIndex(params, callback)

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameters of the **params** parameter

   
| Parameter | Sub-parameter | Description | Example Value |
| :-- | :-- | :-- | :-- |
| tableName | \- | Table name | best |
| indexName | \- | Field index name | idx\_name |
| tableField | \- | Field | "tableField":{"tableFields":\["name","age","phone"\]} |
| tabileFields | Table field | "tableFields":\["name","age","phone"\] | Callback parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| result | Returned result, which can be true or false | true |
| errorMessage | Error information | Failed to create an index. | Example:

  const params = {
    "tableName": "best",
    "indexName": "idx\_name",
    "tableField": {
      "tableFields": \[
        "name",
        "age",
        "phone"
      \]
    }
  }
  U.createTableIndex(params,function(res){});