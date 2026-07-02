---
title: "About Integration Services"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_back_api_002.html"
depth: 4
---
#### Architecture and Functions

![[en-us_image_0000001140222267.png]]

ADC can interact with third-party systems through integration services. The core functions are as follows:

-   The client of the third-party system calls the inbound SOAP/REST API of ADC to implement service functions.
-   ADC calls the outbound SOAP or REST API provided by the third-party system server to implement service functions.

The ADC integration service architecture consists of the following modules:

-   SOAP API management: provides unified management of inbound and outbound SOAP APIs, including creating, modifying, querying, and debugging SOAP APIs.
-   Log management: provides the function of querying logs of inbound and outbound SOAP or REST APIs, including querying received and sent logs and retrying upon an API sending failure.
-   Authentication management: provides authentication for inbound and outbound SOAP or REST APIs and supports multiple authentication modes, such as basic authentication, OAuth 2.0, WSSE, and Keystore.
-   REST API management: provides unified management of inbound and outbound REST APIs, including creating, modifying, querying, and debugging REST APIs.