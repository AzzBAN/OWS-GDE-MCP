---
title: "Rule: Proper Filter Criteria Must Be Used for the Data Export Service That Contains More Than 100,000 Data Records"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523377.html"
depth: 6
---
# Rule: Proper Filter Criteria Must Be Used for the Data Export Service That Contains More Than 100,000 Data Records

**Description**: If the export service does not use proper filter criteria, the export may be time-consuming. As a result, end users may wait for a long time, affecting user experience. If the export duration exceeds the platform specifications, the export fails.

**Check guide**: Determine whether to filter data and how to design filter criteria from the service perspective. Generally, a large number of order logs in time sequence are filtered by time range.

**Positive example**: Filter ticket operation logs by time range.

**Negative example**: The service directly uses **select \*** to return all data and no filter criteria are configured.

**Tool supported or not**: no

**Specification name**: General\_Export\_Use\_Reasonable\_Filter\_for\_Export\_Data

**Severity**: minor

**Parent topic:** [[Data Export|Data Export]]