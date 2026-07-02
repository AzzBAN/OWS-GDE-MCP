---
title: "Suggestion: Use Class to Customize the HTML Template and Reduce HTML Code Changes Caused by Style Changes"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123628.html"
depth: 6
---
# Suggestion: Use Class to Customize the HTML Template and Reduce HTML Code Changes Caused by Style Changes

**Description**: You are advised to use class instead of style in the scenario where a customized HTML template is used to facilitate future extension.

**Check guide**: Check whether the HTML template uses the style property.

**Negative example**: For example, you are advised to use the class property in the div label and configure the CSSLIB component compilation style to control the style for HTML template property of the CardGrid component, row template property of the ListView component, and code property of the HTMLPanel component. The style property of div in the following figure is not recommended, because if style is used, you need to modify the HTML template configuration once style is changed.

![[en-us_image_0000001103346650.png]]

**Tool supported or not**: no

**Specification name**: General\_Page\_Use\_Class\_for\_Custom\_HTML\_Templates

**Severity**: suggestion

**Parent topic:** [[Page|Page]]