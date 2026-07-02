---
title: "Rule: Do Not Perform Time-Consuming Translation Operations on the Service for Exporting More Than 100,000 Data Records"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403825.html"
depth: 6
---
# Rule: Do Not Perform Time-Consuming Translation Operations on the Service for Exporting More Than 100,000 Data Records

**Description**: If time-consuming (longer than or equal to 1s) translation operations are performed on the service for exporting more than 100,000 data records during service execution, the export is time-consuming. As a result, end users wait for a long time and user experience is poor. If the export duration exceeds the platform specifications, the export fails.

**Check guide**: Locate the target service, check the output parameter settings of its end node, and determine whether time-consuming translators, especially some associated translators for data acquisition and transformation through service calling, are configured under the results element subnode.

**Positive example**: Configure a translator on the results node or perform redundancy processing on the data to be translated during data generation.

![[en-us_image_0000001469122364.png]]

**Negative example**: Configure a translator for querying data from another service or model under the results node.

![[en-us_image_0000001469441872.png]]

**Tool supported or not**: no

**Specification name**: General\_Export\_Avoid\_Time\_Consuming\_Translation\_Operations

**Severity**: major

**Parent topic:** [[Data Export|Data Export]]