---
title: "Rule: Do Not Overwrite the Internal Style of a Component During Style Customization"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804064.html"
depth: 6
---
# Rule: Do Not Overwrite the Internal Style of a Component During Style Customization

**Description**: When new pages are involved, the boundary of customized CSS is controlled on the frontend page to prevent the internal style of the component from being overwritten. The main reason is as follows: Due to the continuous evolvement of platform components, if the internal DOM structure is used, the platform does not promise compatibility. Currently, only the ID selector can be used to customize styles.

**Check guide**: Check whether the preceding rules are met when a developer saves a style. If the rules are not met, a message is displayed.

**Positive example**:

![[en-us_image_0000001311654473.png]]

**Negative example**:

![[en-us_image_0000001264014398.png]]

**Exception scenario**: In scenarios where the HTML template is configured, the class can be customized to improve the developer experience. The class must start with the **custom-** prefix.

**Tool supported or not**: no

**Specification name**: General\_Page\_Forbidden\_Overwrite\_The\_Internal\_Style

**Involved orchestration elements**: pages and data visualization screens

**Severity**: major

**Parent topic:** [[Page|Page]]