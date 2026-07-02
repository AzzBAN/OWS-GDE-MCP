---
title: "How Does the System Dynamically Transfers Parameters in an Outbound API URL?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_back_api_026.html"
depth: 5
---
#### Context

The system supports the function of referencing variables in the service URL of an outbound API to dynamically transfer parameters. The variables that can be referenced are classified into the following types:

-   Common parameters: common project parameters obtained from the service URL. The format is ${_Parameter name_}.
-   Path parameters: API input parameters whose **Parameter Location** is **Path** in the service URL. The format is {_Parameter name_}.