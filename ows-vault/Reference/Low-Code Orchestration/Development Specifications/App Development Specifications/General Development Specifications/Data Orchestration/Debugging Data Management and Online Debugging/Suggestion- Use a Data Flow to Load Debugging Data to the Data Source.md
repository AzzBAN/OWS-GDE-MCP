---
title: "Suggestion: Use a Data Flow to Load Debugging Data to the Data Source"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001192144748.html"
depth: 6
---
# Suggestion: Use a Data Flow to Load Debugging Data to the Data Source

**Specification name**: General\_DataFactory\_Load\_Test\_Data\_Efficiently

**Description**: The extraction operators provided by DataFactory can extract data from diverse data sources. The process of manually uploading data to a data source is complex. For example, to write data to the Oracle database, you need to connect to the database and run SQL statements to insert debugging data. You can refer to this suggestion to load debugging data more efficiently.

For example, use the debugging data upload function on the DataFactory page to upload the debugging data to HDFS. Then, use the Extract HDFS operator and Load JDBC operator to automatically save the debugging data to the Oracle database. Later, use the Extract JDBC operator to extract debugging data and debug the flow.

**Parent topic:** [[Debugging Data Management and Online Debugging|Debugging Data Management and Online Debugging]]