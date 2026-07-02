---
title: "This interface is used to obtain details about tickets that meet the filter criteria and can be associated with the current ticket based on the ticket number, project, module, and ticket creation time."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001945507604.html"
depth: 6
---
#### Function description

This API starts from GDE 24.2. It is used to query the list of associated tickets based on the specified ticket ID and whether the ticket is archived.

var request = {

"start":0,

"limit":10,

"order\_id":"INC-20221111-00000001",

"condition":{

"create\_time\_start":"2022-01-01 00:00:00",

"create\_time\_end":"2022-02-28 00:00:00"

}

};

var url = /adc-bpm/rest/v1/order/INC-20221111-00000001/to-associate-order/query/";

var response = ServiceInvoker.post(url, request);