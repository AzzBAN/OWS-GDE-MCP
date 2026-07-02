---
title: "Suggestion: Use Less Than 20 API Service Calling Phases in a Single Process"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523413.html"
depth: 6
---
# Suggestion: Use Less Than 20 API Service Calling Phases in a Single Process

**Description**: If there are too many API service calling phases in a process, errors may occur and cannot be located, and subsequent process maintenance is inconvenient. In addition, the process may have too many mixed responsibilities. Therefore, it is necessary to combine phases or split the process into multiple subprocesses.

**Check guide**:

Open the process chart and view the number of API service calling phases.

![[en-us_image_0000001166257125.png]]

**Positive example**:

The number of API service calling phases in the process is less than the recommended value, and the process chart is clear.

**Negative example**:

The number of API service calling phases in the process is greater than the recommended value, and the process chart is complex.

**Tool supported or not**: no

**Specification name**: General\_Process\_The\_Number\_of\_API\_Service \_Invoking\_Phases\_in\_Single\_Process\_Less\_Than\_20

**Severity**: suggestion

**Parent topic:** [[Process|Process]]