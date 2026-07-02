---
title: "Spl.MessageProcessor.submitData"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731564086.html"
depth: 6
---
# Spl.MessageProcessor.submitData

Used to submit service data.

Input parameters:

**options** (object): Parameters related to submitted service options

  
| Property | Type | Meaning |
| :-- | :-- | :-- |
| serviceId | String | Service ID |
| data | Object | Submitted parameter |
| canUseWhenOffline | Boolean | Whether offline data submission is allowed. The default value is true. |
| showErrorMessage | Boolean | Whether to display error information. The default value is true. |
| silent | Boolean | Whether silent submission is enabled. The default value is false. |
| actionType | String | Submission type. The default value is Update, indicating that the page form will be reloaded after the service request is completed. If the form does not need to be reloaded, you can manually set the value to Delete. |
| pageBackWhenError | Boolean | Whether to return to the previous page when an error message is displayed. The default value is true. |
| success | Function | Successful callback |
| error | Function | Failed callback |
| searchConfig | Object | Filter condition |
| \--contains | Array | Key value array for fuzzy match |
| \--or | Array | Key value array of the OR relationship |
| \--orderBy | Object | Sorting field in {"key":"asc"}. The value can be asc or desc. |
| \--range | Array | Key value array of the range filtering relationship | Example:

Spl.MessageProcessor.submitData({
serviceId: 'task\_work\_update',
data: {taskId:"CM-001"},
success:function(){
C("depart\_btn").beSubmit=false;},
silent: true
});

If **canUseWhenOffline** is set to **false**, the offline status is unavailable. If the value of this property is **true** (default or specified), the offline service must be configured as well. Otherwise, the obtained data is inaccurate. The configuration method is as follows: Open the **mobilemarket\_service\_config\_grid** page in **mobilemarket.app**, and configure a service with the same name as **serviceId** and set the type to **UPDATE**. In addition, when the model field changes, data needs to be submitted to the cache. Otherwise, the GetList service is used to update fields during scheduled synchronization, with certain delay.

**Parent topic:** [[APIs Related to Data Acquisition and Submission|APIs Related to Data Acquisition and Submission]]