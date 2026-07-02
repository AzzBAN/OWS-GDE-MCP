---
title: "Configuring a Customized Authentication Service"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_060.html"
depth: 4
---
#### Context

Different authentication modes can be defined for each service. In addition to authorization configuration based on permission items, the system also allows users to define flexible authentication modes based on a customized service.

Developers need to understand basic operations in [[Creating a Service (Blank Template)|Creating a Service (Blank Template)]] and [[Configuring the Node for Executing a Script|Configuring the Node for Executing a Script]]. This topic uses a simple customized service as an example to describe how to configure the customized authentication service.

Assume that you have configured the info\_category\_create service by referring to the preceding topics. The service can be accessed after login by default. This topic describes how to enable the service to be called only by specific users whose user names start with **demo**.