---
title: "Rule: Do Not Use Non-Open APIs During Page Customization"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363493.html"
depth: 6
---
# Rule: Do Not Use Non-Open APIs During Page Customization

**Description**: In new customized page development scenarios, do not use APIs that are not open in the standard component library of the platform. You can use APIs and standard components provided by the platform. Currently, foolproof restrictions are added to the command line interface (CLI) of customized pages. The API document will be released with the version, obtain the document from the online secondary development guide. Currently, only files in the **@adc/vigour-ui/lib/style/index.css** and **@adc/vigour-ui/lib** directories can be accessed. Files in other directories and their subdirectories cannot be accessed.

**Check guide**: Add verification during the packaging and compilation of the CLI on the customized page. If the requirements are not met, a message is displayed.

**Description**: In new customized page development scenarios, do not use APIs that are not open in the standard component library of the platform. You can use APIs and standard components provided by the platform. Currently, foolproof restrictions are added to the CLI of customized pages. The API document will be released with the version, obtain the document from the online secondary development guide. Currently, only files in the **@adc/vigour-ui/lib/style/index.css** and **@adc/vigour-ui/lib** directories can be accessed. Files in other directories and their subdirectories cannot be accessed.

**Check guide**: Add verification during the packaging and compilation of the CLI on the customized page. If the requirements are not met, a message is displayed.

![[en-us_image_0000002354051073.png]]

**Positive example**:

None

**Negative example**:

![[en-us_image_0000002320133350.png]]

**Tool supported or not**: The current CLI has been verified by default. No tool is required.

**Specification name**: General\_Customize\_Page\_Forbidden\_Use\_Private\_API

**Severity**: major

**Positive example**:

None

**Negative example**:

![[en-us_image_0000002320126810.png]]

**Tool supported or not**: yes

**Specification name**: General\_Customize\_Page\_Forbidden\_Use\_Private\_API

**Severity**: major

**Parent topic:** [[Page|Page]]