---
title: "Suggestion: Customized Assets Should Not Contain a Large Amount of Built-in Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523489.html"
depth: 6
---
# Suggestion: Customized Assets Should Not Contain a Large Amount of Built-in Data

**Description**: If a large amount of data is embedded during app initialization using customized assets, app installation will take a long time. It is recommended that such data be processed as configurations after app installation.

**Check guide**: Check whether the customized asset file contains a large number of built-in files and whether the file size is too large, especially for assets imported from an Excel file. It is recommended that the number of data rows be less than or equal to 1,000.

**Positive example**: The size of the customized asset file is less than 10 MB, and the number of data rows in the asset file (in XLSX format) imported from an Excel file is less than 1,000.

**Negative example**: The number of data rows in the asset file (in XLSX format) imported from an Excel file exceeds 1,000.

**Tool supported or not**: no

**Specification name**: General\_Custom\_Forbidden\_Contain\_Large\_Amounts\_of\_Builtin\_Data

**Severity**: suggestion

**Parent topic:** [[Customized Asset|Customized Asset]]