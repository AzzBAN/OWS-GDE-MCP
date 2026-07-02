---
title: "Rule: Do Not Configure a Large Number of Translators During Data Export to an Excel File"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804060.html"
depth: 6
---
# Rule: Do Not Configure a Large Number of Translators During Data Export to an Excel File

**Description**: No more than 10 translators are used by the configured GetList service exported in an Excel file.

**Check guide**:

-   Check the number of translators used in the configured service exported in an Excel file.
-   If there are more than 10 translators, the efficiency will be reduced. Reduce the number of translators.

**Positive example**: The number of translators cannot exceed 10.

**Tool supported or not**: yes

**Specification name**: General\_Export\_Avoid\_Bulk\_Queries\_and\_Translations

**Severity**: major

**Parent topic:** [[Data Export|Data Export]]