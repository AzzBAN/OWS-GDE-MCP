---
title: "Suggestion: Select HTTPS When You Configure the Outbound SOAP/REST Service"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523509.html"
depth: 5
---
# Suggestion: Select HTTPS When You Configure the Outbound SOAP/REST Service

**Description**: GDE provides integration service capabilities. The outbound SOAP/REST service functions as a client to connect to third-party APIs. Secure transmission channels must be used during the connection. Insecure channels may cause improper data disclosure.

**Check guide**: Log in to the develop-state environment, select the app to be checked, and check whether the service URL of the API under **Outbound SOAP** or **Outbound REST** is prefixed with **https://**.

**Positive example**: outbound SOAP configuration example

![[en-us_image_0000001470271002.png]]

**Exception scenarios**:

1: The server does not support HTTPS. When GDE functions as a client to access the server, if the server does not support HTTPS, the service URL does not need to be prefixed with **https://**.

2: In the DMC Nginx transition scenario, the WS server does not interwork with the third-party server but is transited by DMC Nginx in the following OWS historical networking scenarios: The transmission is divided into two parts: The first part is plaintext transmission from WS to DMC Nginx, and the second part is encrypted transmission from DMC Nginx to Internet and then to a third-party system.

This suggestion aims to prevent improper data disclosure or tampering during transmission between untrusted networks (such as Internet), that is, the transmission risk of the second part. Protection has been provided for the current scenario.

The first transmission part belongs to the VPC internal network domain, which has low security risks. In compatibility scenarios, this specification is not violated.

![[en-us_image_0000001147292621.png]]

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_Interface\_ShouldUseHttps

**Category**: non-bottom-line check item

**Severity**: suggestion

**Orchestration scenario**: API orchestration - API integration and orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]