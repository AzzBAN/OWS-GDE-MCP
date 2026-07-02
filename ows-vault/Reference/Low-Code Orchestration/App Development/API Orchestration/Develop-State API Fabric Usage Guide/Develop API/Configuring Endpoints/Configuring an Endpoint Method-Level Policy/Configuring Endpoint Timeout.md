---
title: "Configuring Endpoint Timeout"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001831754425.html"
depth: 7
---
#### Context

When the client calls the endpoint service through the API Fabric gateway and the gateway processes the calling request, the timeout interval configuration affects the entire communication process. If the default timeout period cannot meet service requirements, you can customize it by referring to this section.

If no method-level connection policy is configured, the endpoint-level connection policy is used by default. Only the SOAP and REST protocols are supported.