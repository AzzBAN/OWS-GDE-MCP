---
title: "Rule: Create Only One Management Object for One Data Source Instance on the Data Source Configuration Page"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001192304720.html"
depth: 6
---
# Rule: Create Only One Management Object for One Data Source Instance on the Data Source Configuration Page

**Specification name**: General\_DataFactory\_Datasource\_Management\_Principle

**Description**: The data source information used by businesses, such as the name, schema, and path, must be properly planned to avoid conflicts between businesses. Create only one management object for each data source instance. This prevents a logical data source from being mapped to multiple physical data sources in the runtime-state environment, reduces system redundancy, and improves maintainability.

**Check guide**: When adding a management object for a data source instance on the **Data Source Configuration** page, check whether there is an existing record for the instance.

**Impact**: If multiple management objects are created for one data source instance, the configuration may be inconsistent. As a result, the calculation tasks fail, and errors occur.

**Parent topic:** [[Data Sources|Data Sources]]