---
title: "Rule: Do Not Use Connector Integration in Ultra-Large Object Transmission Scenarios"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002343654245.html"
depth: 6
---
# Rule: Do Not Use Connector Integration in Ultra-Large Object Transmission Scenarios

**Description**: API Fabric limits the size of each API packet (2 MB by default). If the size of an interface packet exceeds the limit, the packet is rejected. Transmission of ultra-large objects may lead to a lack of system resources and DoS attacks.

**Check guide**: Check APIs whose media type is **FormData** or **application/octet-stream** and ensure that connectors do not transmit ultra-large objects (that is, each object is no larger than 10 MB).

**Tool supported or not**: no

**Specification name**: General\_Connector\_Avoid\_Invoke\_File\_Transfer\_Interfaces\_Through\_Connectors

**Severity**: major

**Parent topic:** [[Connector Development|Connector Development]]