---
title: "Rule: Processing a Large Amount of Data or Time-Consuming Requests Is Disallowed on the Script Node"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403869.html"
depth: 6
---
# Rule: Processing a Large Amount of Data or Time-Consuming Requests Is Disallowed on the Script Node

**Description**: When the script processes a large amount of data or time-consuming requests, the execution efficiency is affected. In addition, the script may block and occupy too many resources, which may affect the performance of the entire system.

**Check guide**:

Open the script and check the script logic. Do not use the logic that includes but is not limited to the following:

1\. Logic that processes a large amount of data, for example, more than 1000 data records.

2\. Entire script logic that takes a long time to process. It is recommended that the time be less than or equal to 2 seconds.

3\. Script logic that calls a synchronization interface requiring third-party system interworking, causing blocked requests.

**Tool supported or not**: no

**Specification name**: General\_Process\_Avoid\_Large\_Scale\_Data\_Processing\_or\_Time\_Consuming\_Processing\_in\_Script\_Node

**Severity**: major

**Parent topic:** [[Process|Process]]