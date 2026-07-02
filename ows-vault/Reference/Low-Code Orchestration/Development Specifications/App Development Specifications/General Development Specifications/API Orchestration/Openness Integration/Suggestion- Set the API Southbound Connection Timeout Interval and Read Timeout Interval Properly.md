---
title: "Suggestion: Set the API Southbound Connection Timeout Interval and Read Timeout Interval Properly"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523421.html"
depth: 6
---
# Suggestion: Set the API Southbound Connection Timeout Interval and Read Timeout Interval Properly

**Description**:

1\. It is recommended that the southbound API timeout period be less than or equal to the API consumer timeout period. If the southbound API timeout period exceeds the API consumer timeout period, the API thread may wait for a long time, causing a waste of system resources.

2\. It is recommended that the connection timeout interval be less than or equal to the read timeout interval. It is recommended that the timeout interval be less than or equal to 5 seconds. If the timeout interval is too long, system requests may be stacked, causing DoS attacks.

**Check guide**: Check whether the connection timeout interval and read timeout interval of the API endpoint are properly set. For example, check whether the timeout interval does not exceed the timeout interval of the API consumer.

![[en-us_image_0000001469964274.png]]

**Positive example**: The backend service is in the same LAN. The read timeout is set to 3 seconds, and the connection timeout is set to 1 second.

![[en-us_image_0000001469966438.png]]

**Negative example**: To ensure that the backend service can receive responses even when the processing is slow, set the timeout interval of all endpoints to the maximum value. The read timeout interval is five minutes, and the connection timeout interval is one minute.

![[en-us_image_0000001521045473.png]]

**Tool supported or not**: no

**Specification name**: General\_API\_Avoid\_Endpoint\_TimeOut\_Not\_Reasonable

**Severity**: suggestion

**Parent topic:** [[Openness Integration|Openness Integration]]