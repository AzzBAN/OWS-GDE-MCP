---
title: "Rule: Do Not Directly Operate Data Sources in the Production Environment During Online Debugging of SQL Statements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662451761.html"
depth: 6
---
# Rule: Do Not Directly Operate Data Sources in the Production Environment During Online Debugging of SQL Statements

**Specification name**: General\_DataFactory\_Online\_Debug\_Data\_Source\_Operation

**Description**: DataFactory provides the online debugging function when SQL statements are compiled in operators. During online debugging of SQL statements, data in the database will be added, deleted, modified, or queried. Therefore, do not directly operate data sources in the production environment.

**Impact**: If you directly perform operations on data sources in the production environment, data may be deleted or modified by mistake, causing production data errors.

**Version**: Functions such as online debugging of SQL statements are supported in 24.1.0 and later versions.

**Parent topic:** [[Debugging Data Management and Online Debugging|Debugging Data Management and Online Debugging]]