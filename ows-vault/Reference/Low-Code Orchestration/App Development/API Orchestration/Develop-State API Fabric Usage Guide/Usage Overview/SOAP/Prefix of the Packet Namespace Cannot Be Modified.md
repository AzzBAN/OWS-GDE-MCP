---
title: "Prefix of the Packet Namespace Cannot Be Modified"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662165084.html"
depth: 6
---
#### Overview

The prefix of the namespace in the packet is calculated using an algorithm based on the URL of the namespace defined in the WSDL file. The API Fabric cannot intervene and can pass the packet only based on the prefix calculated using the algorithm.

For example, in the following packet segment, **http://www.aa.com/servers/samples/javaclass** is the complete namespace address, and **jav** is the namespace prefix computed by the algorithm and cannot be modified.

<jav:aa xmlns:jav="http://www.aa.com/servers/samples/javaclass">