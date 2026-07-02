---
title: "Rule: Do Not Use Standard Components of the Platform for Customized Page Components"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283600.html"
depth: 6
---
# Rule: Do Not Use Standard Components of the Platform for Customized Page Components

**Description**: In the development scenario of new customized page components, standard components of the platform cannot be used, but APIs provided by the platform can be used. The main reason is that the current standard components cannot be fully compatible with the subsequent evolution in terms of technical means. Therefore, the foolproof function is restricted and the API document will be released with the version, obtain the help document from the online secondary development guide.

**Check guide**: Add verification during the packaging and compilation of the CLI of customized page components. If the requirements are not met, a message is displayed.

**Positive example**:

None

**Negative example**:

![[en-us_image_0000001311775237.png]]

**Tool supported or not**: yes

**Specification name**: General\_Customize\_Page\_Components\_Forbidden\_Use\_Standard\_Component

**Involved orchestration elements**: pages and data visualization screens

**Severity**: major

**Parent topic:** [[Page|Page]]