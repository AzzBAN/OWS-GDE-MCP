---
title: "Suggestion: Do Not Return Redundant Columns During the Execution of the Export Service"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123620.html"
depth: 6
---
# Suggestion: Do Not Return Redundant Columns During the Execution of the Export Service

**Description**: If too many redundant columns are returned during the execution of the export service, too many system resources, especially the memory, are occupied. If too many concurrent operations are performed, the memory usage is high and the system responds slowly.

**Check guide**: Check whether the fields returned by the export service differ greatly from those in the export template. For example, do not use **select \*** and **getList** to return all fields during the TQL query of the service. Generally, this fault occurs only when the number of returned fields corresponding to the service is greater than 50 and the difference between the number of returned fields and the number of fields configured in the export template is greater than 50.

**Positive example**: The fields in the exported template match those returned by the service.

**Negative example**: The service directly uses **select \*** to return all data.

**Tool supported or not**: no

**Specification name**: General\_Export\_Avoid\_Return\_Redundant\_Columns

**Severity**: suggestion

**Parent topic:** [[Data Export|Data Export]]