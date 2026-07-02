---
title: "Rule: Do Not Overwrite the Internal Style of a Component During Style Customization"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001663787229.html"
depth: 6
---
# Rule: Do Not Overwrite the Internal Style of a Component During Style Customization

**Description**: For a new page, boundary control is performed on the custom CSS on the front-end page to prevent the internal style of the component from being overwritten. The main reasons are as follows: Platform components will continuously evolve. If the platform depends on the internal DOM structure, the platform side does not promise compatibility. Currently, the system allows style customization only in ID selector mode. There are exceptions. In the scenario where HTML templates are configured, classes can be customized but they must be prefixed with **custom-**, to improve the developer experience.

**Check guide**: Check whether the preceding rules are met when a developer saves a style. If the rules are not met, a message is displayed.

**Positive example**:

![[en-us_image_0000001608967504.png]]

**Negative example**:

![[en-us_image_0000001609127488.png]]

**Tool supported or not**: no

**Specification name**: General\_Page\_Forbidden\_Overwrite\_The\_Internal\_Style

**Severity**: major

**Parent topic:** [[Mobile Page|Mobile Page]]