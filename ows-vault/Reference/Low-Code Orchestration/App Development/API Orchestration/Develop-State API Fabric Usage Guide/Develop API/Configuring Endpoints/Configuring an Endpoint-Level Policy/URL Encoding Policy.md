---
title: "URL Encoding Policy"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002331389046.html"
depth: 7
---
#### Constraints

-   The API Fabric supports two encoding modes: RFC and W3C.
    
    RFC and W3C escape special characters in URLs to the %HH format. The following table describes the escape rules in the API Fabric.
    
    **Table 1** Special character escape rules   
    | Encoding Mode | Special Character in the URL | After Being Escaped |
    | :-- | :-- | :-- |
    | RFC | Space | %20 |
    | W3C | Space | + | -   This policy supports only the RESTful protocol and can be configured only in the develop-state API Fabric.
-   The default encoding mode of existing endpoints created in versions earlier than API Fabric V600R025C00 is W3C. If no encoding mode is configured for a new endpoint in API Fabric V600R025C00 or later, the RFC encoding mode is used by default. The scenarios for adding an endpoint are as follows:
    -   When an API is added on the **Design API** tab page, you need to click **Generate a public endpoint** or **One-click transparent transmission API** to generate an endpoint.
    -   When an API is added on the **Develop API** tab page, you need to set **Orchestration Mode** to **Transparent Transmission Mode** to add an endpoint.
    -   In **Endpoint Management**, add an endpoint.