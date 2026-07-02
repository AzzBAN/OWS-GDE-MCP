---
title: "Suggestion: Error Code Should Contain Sufficient Parameters to Help Users Quickly Locate Faults"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403857.html"
depth: 6
---
# Suggestion: Error Code Should Contain Sufficient Parameters to Help Users Quickly Locate Faults

**Description**: The cause and solution of an error code must contain parameter information. Use placeholders _{0}, {1}..._ to write the parameters. The rest can be deduced by analogy. You can also write internationalization **bundle.key**. Placeholders are written in internationalization.

**Check guide**: Check whether the error code definition is reasonable in the develop-state environment and whether the key parameters for locating the fault are correct.

**Positive example**:

![[en-us_image_0000002353627601.png]]

**Tool supported or not**: no

**Specification name**: General\_ErrorCode\_ErrorCode\_Contains\_Args

**Severity**: suggestion

**Parent topic:** [[Error Code|Error Code]]