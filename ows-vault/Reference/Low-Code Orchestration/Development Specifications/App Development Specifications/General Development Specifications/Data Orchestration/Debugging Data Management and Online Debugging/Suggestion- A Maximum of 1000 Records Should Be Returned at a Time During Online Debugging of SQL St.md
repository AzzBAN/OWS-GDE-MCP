---
title: "Suggestion: A Maximum of 1000 Records Should Be Returned at a Time During Online Debugging of SQL Statements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662131921.html"
depth: 6
---
# Suggestion: A Maximum of 1000 Records Should Be Returned at a Time During Online Debugging of SQL Statements

**Specification name**: General\_DataFactory\_Online\_Debug\_Select\_Limit\_1000

**Description**: The SQL online debugging function can be interworked with the big data platform to query data. Therefore, the amount of returned data needs to be limited to accelerate the response and improve the debugging efficiency. After the debugging is complete, delete the limit condition and save the settings.

**Check guide**: Check whether the limit condition is explicitly specified in the query SQL statement during debugging to limit the amount of data to be returned.

**Positive example**: select \* from #table where name = $name and age > $age limit 1000

**Version**: Functions such as online debugging of SQL statements are supported in 24.1.0 and later versions.

**Parent topic:** [[Debugging Data Management and Online Debugging|Debugging Data Management and Online Debugging]]