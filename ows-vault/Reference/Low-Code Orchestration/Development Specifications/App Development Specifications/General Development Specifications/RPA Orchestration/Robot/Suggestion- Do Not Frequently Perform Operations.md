---
title: "Suggestion: Do Not Frequently Perform Operations"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001768145164.html"
depth: 6
---
# Suggestion: Do Not Frequently Perform Operations

**Description**: When an app or API is called, the operation frequency should not be too high. With regard to factors such as the actual processing speed and response time of the host, you need to adjust the call interval to a proper range to ensure performance and stability.

**Check guide**: If a control is continuously called, check whether **Delay Before Execution** of the control is set to a proper value or the delay operation is used. You are advised to set **Delay Before Execution** in the control.

**Positive example**: A proper delay time is set.

![[en-us_image_0000001746843582.png]]

**Tool supported or not**: no

**Specification name**: General\_RPA\_Operation\_Not\_Too\_Fast

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]