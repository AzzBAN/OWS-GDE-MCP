---
title: "Suggestion: Use No More Than 100 Fields for a Single Batch Operation"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963720.html"
depth: 6
---
# Suggestion: Use No More Than 100 Fields for a Single Batch Operation

**Description**: When you add or modify a model instance in an Excel file, ensure that each data record contains a maximum of 100 model fields at a time. If there are too many data records and fields, the performance loss increases.

**Check guide**: Check the number of fields used for batch update and Excel operations. Try to keep the number of fields within 100.

**Positive example**: The number of corresponding fields is less than or equal to 100.

**Negative example**: The number of corresponding fields is greater than 100.

**Tool supported or not**: no

**Specification name**: General\_Export\_Avoid\_Exceed\_100\_Data\_Records\_or\_100\_Data\_Fields\_in\_Single\_Operation

**Severity**: suggestion

**Parent topic:** [[Data Import|Data Import]]