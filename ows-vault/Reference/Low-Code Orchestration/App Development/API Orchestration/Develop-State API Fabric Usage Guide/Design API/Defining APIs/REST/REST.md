---
title: "REST"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_095.html"
depth: 6
children: ["Swagger 2.0", "OpenAPI 3.0"]
---
#### Restrictions

-   Currently, the API Fabric supports the following media types configured for the REST protocol. The application/octet-stream type does not support commissioning or mocker.
    
    ![[note_3.0-en-us.png]]
    
    -   When the media type application/octet-stream is used to download files, you can change the file size by configuring **access\_max\_req\_size** and **access\_max\_resq\_size** during installation.
    -   After the installation, text/event-stream can be used only after **sse\_switch** is set to **YES** by upgrading the stack. If **sse\_switch** is not set, text/event-stream is disabled by default. The streaming API function can be used only when the APIF LB service is interconnected.
    
    -   application/json
    -   application/xml
    -   application/x-www-form-urlencoded
    -   multipart/form-data
    -   application/octet-stream
    
    -   text/event-stream (selected only when the REST Swagger 2.0 response type is configured)

## Sub-topics

- [[Swagger 2.0]]
- [[OpenAPI 3.0]]
