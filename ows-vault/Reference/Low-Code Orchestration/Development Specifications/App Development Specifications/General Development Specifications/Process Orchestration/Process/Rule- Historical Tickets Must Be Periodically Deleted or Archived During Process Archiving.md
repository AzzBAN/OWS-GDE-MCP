---
title: "Rule: Historical Tickets Must Be Periodically Deleted or Archived During Process Archiving"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963752.html"
depth: 6
---
# Rule: Historical Tickets Must Be Periodically Deleted or Archived During Process Archiving

**Description**: If historical tickets are stacked, the ticket execution and query efficiency are affected. Therefore, historical tickets must be deleted or archived periodically to reduce the system pressure.

**Check guide**:

1\. Check whether the archiving function is enabled for each process.

![[en-us_image_0000002193313825.png]]

2\. Set the number of days for storing tickets in a business process and API process to a value less than or equal to 180 (recommended) and a value less than or equal to 7 (recommended), respectively.

![[en-us_image_0000002157905872.png]]

**Tool supported or not**: no

**Specification name**: General\_Process\_Periodically\_Delete\_or\_Archive\_Historical\_Work\_Orders

**Severity**: major

**Parent topic:** [[Process|Process]]