---
title: "Querying the User List of a Project Team"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_ProjectConfigPublicService_project_users_query_POST.html"
depth: 6
---
#### Function

It starts with GDE24.2. This API is used to query the user list of a project team based on the project name. The names of all users in the list are returned.

Interface script invoked by the instance:

var request = {
"project\_name":"test\_project"
};
var url = "/adc-bpm/rest/v1/order/project/users/query/";
var response = ServiceInvoker.post(url, request);