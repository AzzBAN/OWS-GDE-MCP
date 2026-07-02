---
title: "APIs Related to Data Acquisition and Submission"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001316159588.html"
depth: 9
---
# APIs Related to Data Acquisition and Submission

The Spl.MessageProcessor. loadData API is used to obtain service data. (Ensure that you have obtained related permissions.)

  
| Property | Type | Description |
| :-- | :-- | :-- |
| serviceId | String | Service ID |
| data | Object | Indicates the submitted parameter. |
| canUseWhenOffline | Boolean | Indicates whether offline data submission is allowed. The default value is true. |
| showErrorMesisage | Boolean | Indicates whether to display error information. The default value is true. |
| silent | Boolean | Indicates whether to submit data in silent mode. The value true indicates that data is submitted in silent mode and loading is not displayed. The default value is false. |
| success | Function | Indicates that the callback is successful. |
| error | Function | Indicates that the callback fails. | Example:

Spl.MessageProcessor.loadData({
The serviceId: '/adc-service/web/rest/v1/services/project\_test/test/test\_contact\_tel\_create', // Service ID exists.
  data: {
    contact\_id: "wu\_id",
    telephone: "119"
  },
  success:function(res){
    console.log(res)
  },
  error: function(error) { 
    console.log(error)
  },
  silent: true,
  showErrorMessage: true,
});

The functions of the parameters of Spl.MessageProcessor. submitData used to submit service data are the same as those of the parameters of Spl.MessageProcessor. loadData.

**Parent topic:** [[APIs Related to Request Services and Event Registration|APIs Related to Request Services and Event Registration]]