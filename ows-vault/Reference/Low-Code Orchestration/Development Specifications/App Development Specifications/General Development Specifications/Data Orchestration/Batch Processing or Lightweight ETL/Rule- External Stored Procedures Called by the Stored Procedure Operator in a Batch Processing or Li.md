---
title: "Rule: External Stored Procedures Called by the Stored Procedure Operator in a Batch Processing or Lightweight ETL Control Flow Must Be Trustworthy"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001192304724.html"
depth: 6
---
# Rule: External Stored Procedures Called by the Stored Procedure Operator in a Batch Processing or Lightweight ETL Control Flow Must Be Trustworthy

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Stored\_Procedure\_Security\_Trustworthy

**Description**: A stored procedure is an SQL statement set used to implement specific functions. It is created after compilation and stored in a database. Users can specify the name and parameters of a stored procedure to call and execute the stored procedure. A stored procedure is the code encapsulation and reuse at the SQL language level of the database.

When you perform operations on the database, if untrustworthy data (such as external data) is used to dynamically concatenate SQL statements and an attacker enters maliciously constructed data, the execution results of the dynamically concatenated SQL statements do not meet the expectations, causing serious consequences, such as data leakage, information tampering, or malicious data clearance.

Untrustworthy data includes data transmitted across trusted domains, such as user input data, data imported from external systems, and data transferred from networks.

**Check guide**:

1.  Check whether the called external stored procedure contains external variable input data. If no external input exists, check whether the database syntax is reliable and available.
2.  If external variable input exists, whitelist-based verification must be performed on the input. Some special characters have been transcoded to ensure that the external input is controllable.

**Impact**: Calling untrustworthy external stored procedures may cause serious security and function issues.

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]