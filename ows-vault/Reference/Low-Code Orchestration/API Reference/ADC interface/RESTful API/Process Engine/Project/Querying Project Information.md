---
title: "Querying Project Information"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProjectConfigPublicService_project_queryPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. This API is used to query project information based on the project name or project ID. Information such as the creator and creation time of a project is returned.

Interface script invoked by the instance:

var request = {
"start":0,
"limit":10,
"condition":{
"project\_name":"test\_project",
"user\_name":"admin"
}
};
var url = "/adc-bpm/rest/v1/order/project/query";
var response = ServiceInvoker.post(url, request);