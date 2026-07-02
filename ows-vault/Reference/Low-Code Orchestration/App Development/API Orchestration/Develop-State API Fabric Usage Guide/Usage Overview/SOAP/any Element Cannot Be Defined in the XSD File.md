---
title: "any Element Cannot Be Defined in the XSD File"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662324768.html"
depth: 6
---
#### Overview

The following figure shows an example of the packet segment in the XSD file, in which the **any** element is defined and two simple elements **balance** and **type** are defined in the **extension** complex structure.

![[en-us_image_0000001670077901.png]]

The Axis2 does not support the use of the **any** element in the class file compiled by the WSDL. As a result, the API Fabric cannot obtain the content of the **any** element during object conversion based on the aar, and the **balance** and **type** elements are lost after the XSD is parsed into the MessageObject.