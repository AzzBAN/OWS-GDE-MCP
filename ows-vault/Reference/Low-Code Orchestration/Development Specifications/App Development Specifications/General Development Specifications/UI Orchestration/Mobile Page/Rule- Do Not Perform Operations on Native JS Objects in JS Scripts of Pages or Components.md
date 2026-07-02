---
title: "Rule: Do Not Perform Operations on Native JS Objects in JS Scripts of Pages or Components"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001615347204.html"
depth: 6
---
# Rule: Do Not Perform Operations on Native JS Objects in JS Scripts of Pages or Components

**Description**: The internal implementation logic of platform components keeps evolving. If native JS objects are used to perform operations on elements such as DOM, compatibility issues will occur after the platform is upgraded and the compatibility is not promised by the platform side. Therefore, when editing the scripts of a page or component, do not access native JS objects. Use the APIs provided by the platform to process the service logic. (The API document is released with the version. You can obtain the document from the online secondary development guide.)

**Check guide**: Do not perform operations using methods such as $, document, window, and Vue on native JS objects. Use the UI capabilities (such as Spl, C, and U) provided by the platform.

**Positive example**:

![[en-us_image_0000001609007406.png]]

**Negative example**:

![[en-us_image_0000001608687926.png]]

**Tool supported or not**: no

**Specification name**: General\_Page\_Forbidden\_Use\_Native\_JavaScript\_or\_Private\_APIs

**Severity**: major

**Parent topic:** [[Mobile Page|Mobile Page]]