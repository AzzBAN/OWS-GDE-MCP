---
title: "Rule: Efficient TQL Statements Must Be Used for Query"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162958928.html"
depth: 6
---
# Rule: Efficient TQL Statements Must Be Used for Query

**Description**: For ADC model data stored in relational databases, to ensure query performance and system stability, TQL statements must comply with the following best practices:

1\. **Efficient use of indexes**: Ensure that indexes have been created for the fields involved in operations such as query conditions ("WHERE"), aggregation ("GROUP BY"), and sorting ("ORDER BY"), and SARGable (indexable query) methods such as exact match ("=" and "IN") or prefix match ("LIKE 'value%'") are used to maximize index efficiency.

2\. **Avoid full table scan**: Do not use full table scan queries, such as postfix fuzzy match ("LIKE '%value'"), non-equality operations ("!="), or functions used on indexed columns. These operations may bypass indexes and trigger full table scan.

3\. **Minimize data transmission**: Use explicit column names for query (column projection) and do not use **SELECT \***, reducing network I/O and database memory consumption.

Following the preceding principles can significantly reduce the database load and prevent the database from initiating system performance and reliability risks due to low query efficiency.

**Check guide**:

Recommendation 1: Preferentially use the exact query mode in which indexes can be hit. For example, use **is**, **\>**, **<**, **\>=**, **<=**, **between**, or **in**. Do not use unnecessary fuzzy match conditions in which indexes cannot be hit, such as **contains**, **not contains**, **like**, and **not like**.

**Positive example**:

select address from model\_user where name is 'XXX%';

**Negative example**:

select address from model\_user where name like '%XXX%';

Recommendation 2: Do not use the reverse match conditions in which indexes cannot be hit, such as **is not**, **is empty**, **is not empty**, and **not in**. You are advised to set the default values of the fields and use the exact match conditions in which indexes can be hit.

**Positive example**:

Set the default value of **phone** to **0000** for the **model\_user** model.
select name from model\_user where phone is '0000';

**Negative example**:

Do not set the default value of phone for the **model\_user** model.
select name from model\_user where phone is empty;

Recommendation 3: Hit indexes during aggregation operations, such as **order by**, **group by**, **max**, **min**, and **distinct**.

**Positive example**:

The **region\_name** field of the **trouble\_ticket** model has an index which can be used for efficient calculation.
select count(region\_name ) c,region\_name from trouble\_ticket group by region\_name order by c desc limit 1000;

**Negative example**:

If no index is used for aggregation operations, data in the entire table is calculated and a large amount of temporary data is generated. As a result, the database is heavily loaded and the query efficiency is low.

Recommendation 4: Select only necessary fields because too many fields may consume many resources for data processing.

**Positive example**: Select only the fields required by the context to reduce the resources to be processed.

**Negative example**: Without considering the TQL statements and context, use **select \*** to query all fields.

Recommendation 5: After compiling a TQL statement, use the TQL debugging interpretation plan to determine whether indexes are hit during the TQL statement execution and whether the TQL statement execution is efficient.

**Positive example**: Check the interpretation plan and ensure that the number of scanned rows is as small as possible, indexes are hit, and that the execution duration meets the expectation (less than 1s). If the TQL statement is incorrectly compiled, adjust it in a timely manner. If the index is missing or does not meet the expectations, adjust the index in a timely manner.

**Negative example**: The TQL execution process is unpredictable because the interpretation plan and execution efficiency are not checked.

**Tool supported or not**: no

**Specification name**: General\_Service\_Use\_High\_Efficiency\_TQL\_to\_Query\_Tables

**Severity**: major

**Parent topic:** [[Service|Service]]