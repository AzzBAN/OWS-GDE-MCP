---
title: "Spl.MessageProcessor.loadData"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001778643529.html"
depth: 6
---
# Spl.MessageProcessor.loadData

Used to load service data.

Input parameters:

**options** (object): Parameters related to loaded service options

  
| Property | Type | Meaning |
| :-- | :-- | :-- |
| serviceId | String | Service ID |
| data | Object | Service parameter |
| canUseWhenOffline | Boolean | Whether offline data loading is allowed. The default value is true. |
| silent | Boolean | Whether silent loading is enabled. The default value is false. |
| success | Function | Successful callback. The callback parameter is the return value of the service. |
| error | Function | Failed callback | Example:

Spl.MessageProcessor.loadData({
serviceId: 'task\_work\_get',
data: {taskId:"CM-001"},
success:function(json){
console.log(json);
}
});

If **canUseWhenOffline** is set to **false**, the offline status is unavailable. If the value of this property is **true** (default or specified), the offline service must be configured as well. Otherwise, the obtained data is inaccurate. The configuration method is as follows: In **mobilemarket.app**, open the **mobilemarket\_service\_config\_grid** page, configure a service with the same name as **serviceId** and the service type **GETLIST** and **GET**. The GetList service is used to periodically synchronize mobile cache data and server data; therefore, it must be configured as well.

**Parent topic:** [[APIs Related to Data Acquisition and Submission|APIs Related to Data Acquisition and Submission]]