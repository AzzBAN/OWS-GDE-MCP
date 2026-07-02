---
title: "Rule: The Frontend Access Callback Policy Must Be Set to Restricted Callback in the Rule Import Template"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283596.html"
depth: 6
---
# Rule: The Frontend Access Callback Policy Must Be Set to Restricted Callback in the Rule Import Template

**Description**: After the frontend access function is enabled for the Excel import configuration, the template can be directly accessed on the page and the callback service can be configured. The frontend access callback policy in the import configuration must be set to restricted callback, and the list of services that can be called back must be specified to prevent security issues caused by the callback of any service.

**Check guide**:

-   Check whether the frontend access function is enabled in the Excel import configuration.
-   Check whether the frontend access callback policy in the Excel file is restricted.

**Positive example**: Set the callback policy to restricted callback in the frontend access scenario.

![[en-us_image_0000001469283820.png]]

**Tool supported or not**: yes

**Specification name**: General\_Export\_Avoid\_Bulk\_Queries\_and\_Translations

**Severity**: major

**Parent topic:** [[Data Import|Data Import]]