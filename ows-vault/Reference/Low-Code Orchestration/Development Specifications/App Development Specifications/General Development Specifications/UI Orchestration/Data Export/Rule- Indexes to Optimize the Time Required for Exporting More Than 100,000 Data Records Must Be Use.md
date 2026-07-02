---
title: "Rule: Indexes to Optimize the Time Required for Exporting More Than 100,000 Data Records Must Be Used"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963708.html"
depth: 6
---
# Rule: Indexes to Optimize the Time Required for Exporting More Than 100,000 Data Records Must Be Used

**Description**: When a large amount of data is exported, if no index is configured for the query model during service execution, the export is time-consuming. As a result, end users may wait for a long time, affecting user experience. If the export duration exceeds the platform specifications, the export fails.

**Check guide**: Check whether the filter criteria use indexes when the export service involves model query.

**Positive example**: Proper indexes are configured for the search criteria of the model. For example, indexes are added for the time field based on the time condition.

**Negative example**: No index is configured for the model search criteria.

**Tool supported or not**: no

**Specification name**: General\_Export\_Use\_Indexes\_to\_Optimize\_the\_Export\_Performance

**Severity**: major

**Parent topic:** [[Data Export|Data Export]]