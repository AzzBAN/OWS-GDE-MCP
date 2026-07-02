---
title: "Rule: Variables Instead of Hard-coded Ones Must Be Configured for Environment-related Information During Interface Interworking"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804108.html"
depth: 6
---
# Rule: Variables Instead of Hard-coded Ones Must Be Configured for Environment-related Information During Interface Interworking

**Description**: The integration service has environment-related configurations, such as the IP address and port number, which are configured using variables.

**Check guide**: During integration service orchestration, define and reference variables in the format of "${variable name}".

**Positive example**:

Define variables in the develop-state environment: In the project list, click ![[en-us_image_0000001474960252.png]] on the project card. On the displayed project details page, click the **Common Parameter Settings** tab to define parameters.

![[en-us_image_0000001475280320.png]]

Use variables in the develop-state environment: Use **${}** to reference URLs or ports that are related to the environment or need to be dynamically replaced.

![[en-us_image_0000001474961180.png]]

Configure variables in runtime state: Configuration parameters on the app management page.

![[en-us_image_0000001526201897.png]]

**Negative example**: The service address is set to a fixed IP address and port number. As a result, the interface package is not universal.

**Tool supported or not**: no

**Specification name**: General\_Integrate\_Environment\_Related\_Information\_Cannot\_Be\_Hard\_Coded

**Severity**: major

**Parent topic:** [[Interface Integration|Interface Integration]]