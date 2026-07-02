---
title: "Rule: Select Parameter Types Based on the Parameter Usage When Editing Parameters for Data Integration Flows"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001653873181.html"
depth: 6
---
# Rule: Select Parameter Types Based on the Parameter Usage When Editing Parameters for Data Integration Flows

**Specification name**: General\_DataFactory\_AIP\_Match\_Parameter\_Type

**Description**: When editing parameters for data integration flows, select parameter types based on the actual usage of the parameters to avoid data security risks.

**Check guide**:

Select parameter types based on actual meanings:

-   If the value of a parameter is a password, set **Parameter Type** to **PASSWORD**. Then, the parameter is anonymized when it is displayed on the WebUI.
-   If the value of a parameter is personal data (such as an email address and mobile number), set **Parameter Type** to **ANONYMOUS**. Then, the parameter is anonymized when it is displayed on the WebUI.
-   If the value of a parameter contains more than 1024 characters, set **Parameter Type** to **TEXTAREA**. Then, the parameter can be easily viewed and edited.
-   If the value of a parameter is an IP address, set **Parameter Type** to **IP**.
-   If a parameter is of another type, set **Parameter Type** to **TEXT**.

**Impact**: Improper data type may cause data security risks.

**Parent topic:** [[Data Integration|Data Integration]]