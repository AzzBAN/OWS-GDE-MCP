---
title: "Rule: Do Not Transfer Oversized Objects in the Process Orchestration Mode of API Integration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403881.html"
depth: 6
---
# Rule: Do Not Transfer Oversized Objects in the Process Orchestration Mode of API Integration

**Description**: The system has a limit on the packet size (2 MB by default) in the process orchestration mode. If the size of an interface packet exceeds the limit, the packet is rejected. Transmission of large packets may cause insufficient system resources. As a result, DoS attacks may occur.

**Check guide**: Check the APIs whose media type is **FormData** or **application/octet-stream** and ensure that the APIs related to the process orchestration mode do not transmit ultra-large objects (greater than 10 MB).

![[en-us_image_0000001469785942.png]]

![[en-us_image_0000002283745184.png]]

**Tool supported or not**: no

**Specification name**: General\_API\_Avoid\_Invoke\_File\_Transfer\_Interfaces\_Through\_APIs

**Severity**: major

**Parent topic:** [[Openness Integration|Openness Integration]]