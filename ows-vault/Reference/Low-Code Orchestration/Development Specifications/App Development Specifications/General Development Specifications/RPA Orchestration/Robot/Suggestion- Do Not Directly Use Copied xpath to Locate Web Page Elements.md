---
title: "Suggestion: Do Not Directly Use Copied xpath to Locate Web Page Elements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001814865229.html"
depth: 6
---
# Suggestion: Do Not Directly Use Copied xpath to Locate Web Page Elements

**Description**: During service data operations, the operation object must be determined based on the unique service ID. Variable conditions such as line number are not allowed. In addition, do not use absolute paths or relative paths with pure hierarchical relationships (xpath) to locate elements. To prevent element position changes caused by minor adjustment of the page structure, use text or other properties to locate elements.

**Check guide**: none

**Positive example**

![[en-us_image_0000001793887057.png]]

![[note_3.0-en-us.png]]

xpath logic of the current Studio element picker: The matching starts from the first one in sequence. Once successful, the matching stops. It is recommended that the first xpath be located using text or element properties or only one xpath be retained. The content in the red box in the preceding figure must be retained. Other fields can be left empty. If there is an iframe, the content also needs to be retained.

**Tool supported or not**: no

**Specification name**: General\_RPA\_Forbidden\_Use\_Copied\_XPath

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]