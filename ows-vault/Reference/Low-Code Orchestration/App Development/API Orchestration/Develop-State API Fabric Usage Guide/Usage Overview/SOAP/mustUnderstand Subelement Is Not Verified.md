---
title: "mustUnderstand Subelement Is Not Verified"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662165080.html"
depth: 6
---
#### Overview

The optional subelement **mustUnderstand** in the SOAP header indicates whether the server verifies the SOAP header. The API Fabric functions as the gateway only to process and forward requests or impacts. Therefore, the API Fabric does not identify **mustUnderstand**. That is, the API Fabric processes the request normally no matter whether the SOAP header contains **mustUnderstand**.