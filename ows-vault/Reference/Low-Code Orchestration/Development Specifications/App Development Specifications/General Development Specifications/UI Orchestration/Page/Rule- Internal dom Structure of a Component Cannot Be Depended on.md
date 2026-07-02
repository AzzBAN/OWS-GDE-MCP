---
title: "Rule: Internal dom Structure of a Component Cannot Be Depended on"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162640394.html"
depth: 6
---
# Rule: Internal dom Structure of a Component Cannot Be Depended on

**Description**: The service orchestration page cannot be customized based on the internal dom structure of the component. Since GDE 2.2, new assets are protected in the framework code in the scenario where dom is operated in JQuery mode. The internal dom structure of the HTML Panel component is not restricted. In scenarios where other components are used, error logs are recorded on the console to notify developers. The error logs on the console are as follows:

![[en-us_image_0000001277908221.png]] dom is operated to solve style problems. It is recommended that the dom be implemented based on the open style configuration of the component or the API developed for a single component.

**Check guide**: Check whether the dom structure in the component is used in the customized JS code.

**Negative example**:

![[en-us_image_0000001103025456.png]]

Obtain the orchestration configuration ID through **S**("id").

**Tool supported or not**: yes

**Specification name**: General\_Page\_Forbidden\_Depend\_on\_The\_Internal\_DOM

**Involved orchestration elements**: pages and data visualization screens

**Severity**: major

**Parent topic:** [[Page|Page]]