---
title: "Header Format in a Northbound Request Must Be the Same As That Defined in the WSDL File"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662165088.html"
depth: 6
---
#### Overview

In some scenarios, the SOAP header defined in the WSDL file contains multiple nodes. In this case, when the client sends a request to the API Fabric, if the node names and node quantity of the SOAP header in the request packet are different from those defined in the WSDL file, the Apache Axis2/Java open-source framework determines that the verification fails.