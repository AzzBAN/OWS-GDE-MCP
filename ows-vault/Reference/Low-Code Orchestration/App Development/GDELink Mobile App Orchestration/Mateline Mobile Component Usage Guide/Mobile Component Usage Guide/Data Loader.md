---
title: "Data Loader"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001781237497.html"
depth: 5
---
# Data Loader

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Cache | Whether to use the cache |
| Parameters | Service input parameter |
| Service Id | Service that returns the data required by the form | **APIs**

**reload**

Input parameter: **(param,callback)**

Output parameters: none

Description: Reload the table data and execute the callback function.

Example:

C("loader").reload({start:0,limit:5});

**dataloader\_id** is the ID of the Data Loader component.

Nf.PageReady(function(){

C("refresh\_btn").on("click", function(){

C("dataloader\_id").reload({"user":"aty"},function(data){

C("target").setValue(data.reload\_response);

});

});

C("refresh\_btn2").on("click", function(){

C("dataloader\_id").reload();

})

})

**Events**

**dataLoaded**

Description: This event indicates that the data loading is complete.

Example:

C("id").on("dataLoaded",function(json){

//do something

})

**FAQs**

Scenarios

1\. Dynamically obtain form data through services.

2\. Reload form data.

3\. Listen to the loading completion event of the form data and execute the custom method after the form loading is complete.

**Precautions**

The reload of the form data depends on the reload event of the Data Loader component. To update the form data, you are advised to configure the corresponding data loading service. Currently, the form reload event without a data loading service is not supported.

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]