---
title: "Suggestion: Properly Protect the Data When the Tool Calls a Third-Party System"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404037545.html"
depth: 6
---
# Suggestion: Properly Protect the Data When the Tool Calls a Third-Party System

**Description**: During agent orchestration, users can use tools to call third-party interfaces. Currently, when the tool calls third-party systems through the API gateway, the platform provides certain protection capabilities, such as content risk control and theme fence. However, the rationality of some content still needs to be guaranteed manually.

**Check guide**:

1\. Go to the tool definition page. Based on the provided translator capabilities, you can use the translator to process input parameters.

2\. If the content returned by the tool may contain uncertain information returned by the foundation model, you are advised to use a script to preprocess the information and then return the information to the next processing process or page.

3\. When sensitive data is called and transferred, a secure encryption channel must be configured on the API gateway for transmission.

4\. The openness level of the tool must be properly configured. Interfaces that may involve sensitive data transmission or high-risk operations must not be opened.

![[en-us_image_0000002470790840.png]]

**Tool supported or not**: no

**Specification name**: General\_Ctx\_Data\_Protection

**Severity**: suggestion

**Parent topic:** [[Intelligent Component Orchestration|Intelligent Component Orchestration]]