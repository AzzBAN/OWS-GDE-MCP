---
title: "Fault Element Can Be Returned to the Northbound Client"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662324772.html"
depth: 6
---
#### Overview

When the values of the subelements such as **faultcode**, **faultstring**, and **detail** in **Fault** are returned to the northbound client, JavaScript must be compiled in the exception diagram element and the subelement values cannot be bypassed.

When the values of **faultcode** and **faultstring** are empty, the value of **detail** can be returned.