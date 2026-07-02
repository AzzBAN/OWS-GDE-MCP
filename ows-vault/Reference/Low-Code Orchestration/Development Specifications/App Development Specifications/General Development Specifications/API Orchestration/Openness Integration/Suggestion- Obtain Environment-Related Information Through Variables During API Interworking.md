---
title: "Suggestion: Obtain Environment-Related Information Through Variables During API Interworking"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283640.html"
depth: 6
---
# Suggestion: Obtain Environment-Related Information Through Variables During API Interworking

**Description**: Environment-related configurations, such as the third-party service address, are set as public variables for the running engine to dynamically modify.

**Check guide**: Check whether the endpoint service URL is in **$**_{Variable name}_ format.

![[en-us_image_0000001469805510.png]]

**Positive example**:

![[en-us_image_0000001469965466.png]]

**Negative example**:

![[en-us_image_0000001526038645.png]]

**Tool supported or not**: no

**Specification name**: General\_API\_Avoid\_Runtime\_About\_Config\_Hard\_Code

**Severity**: suggestion

**Parent topic:** [[Openness Integration|Openness Integration]]