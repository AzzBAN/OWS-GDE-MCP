---
title: "Execute the high-level query service."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_OrderQueryRpcService_advance-queryPOST.html"
depth: 6
---
#### Function Description

Start with GDE 24.2, Interface script invoked by the instance:

var request = {

"start":0,

"limit":10,

"title": "a"

};

var response = ServiceInvoker.post("/adc-bpm/rest/v1/bpm/query/advance-query?app\_name=CompatibilityProject&module\_name=PreTestApp&process\_name=ID\_698\_1565921678364&data\_model\_name=prea\_pretype", request);

var response = {

"start": 0,

"total": 1,

"results": \[

{

"active": "1",

"allsubticketclose": "",

"assign\_to\_fme: "",

...

}

\]

}