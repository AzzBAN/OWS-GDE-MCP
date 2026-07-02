---
title: "duration Data Type Cannot Be Defined in the XSD File of the Southbound Service"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001710244677.html"
depth: 6
---
#### Overview

In the API Fabric, the **duration** data type is processed by the **org.apache.xmlbeans.GDuration** open-source class. In the class, the **field** attribute is inconsistent with the names of the corresponding **get** and **set** methods. As a result, data is lost when the API Fabric receives southbound packets and converts them into MO messages, and the constructor of **org.apache.xmlbeans.GDuration** is called to generate a value of **PT0S** when the value is sent back to the northbound service.