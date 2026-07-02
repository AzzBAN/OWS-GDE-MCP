---
title: "Rule: All APIs Have Been Developed Before Apps That Are Deployed in the Runtime State Environment Are Packaged"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643389.html"
depth: 6
---
# Rule: All APIs Have Been Developed Before Apps That Are Deployed in the Runtime State Environment Are Packaged

**Description**: APIs in the develop state will be ignored when being imported to the running engine. APIs that are not completely developed may fail to be released or fail to be called when being imported to the running engine.

**Check guide**: Click the **Develop API** tab and check whether the app to be packaged contains APIs that are being designed or developed.

![[en-us_image_0000001520989613.png]]

**Negative example**: The API is in the develop state.

![[en-us_image_0000001474959168.png]]

**Tool supported or not**: no

**Specification name**: General\_API\_Avoid\_API\_In\_Design\_Status\_Before\_Pack

**Severity**: major

**Parent topic:** [[Openness Integration|Openness Integration]]