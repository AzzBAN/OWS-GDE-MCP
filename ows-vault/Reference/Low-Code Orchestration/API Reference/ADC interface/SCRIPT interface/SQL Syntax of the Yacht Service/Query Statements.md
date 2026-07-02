---
title: "Query Statements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001628913285.html"
depth: 5
---
#### Syntax

1.  Query syntax
    
    **SELECT** /\* Query statements \*/
    
    \[ **DISTINCT** \] /\* Uniquely identifies a row in the result set \*/
    
    column\_expr \[, column\_expr \] ... /\* Column expression \*/
    
    \[**FROM** table\_references\] /\* Table expression \*/
    
    \[**WHERE** condition\_expr \[, condition\_expr \] ... /\* Condition expression \*/\]
    
    \[**GROUP BY** column\_expr \[, column\_expr \] ... /\* Column expression \*/\]
    
    \[**HAVING** condition\_expr \[, condition\_expr \] ... /\* Condition expression \*/\]
    
    \[**ORDER BY** column\_expr \[**ASC** | **DESC**\] \[, column\_expr \[**ASC** | **DESC**\]\] ... /\* Column expression \*/\]
    
    \[**LIMIT** row\_count \[ **OFFSET** offset \]\] /\* Constraint on the number of returned rows \*/
    
    ![[note_3.0-en-us.png]]
    
    -   If the output column selected by the SELECT statement contains the sensitive attribute, Dynamic Data Masking (DDM) is performed. DDM only affects the data finally obtained and does not affect the condition judgment, sorting, and aggregation.
    -   DDM is used to retain the characters at both ends and mask the characters in the middle with masking characters, that is, the asterisk (\*) by default. Due to database function differences, the length of the characters used for masking may differ from that of the actual data in some scenarios.
    -   The values of **row\_count** and **offset** are non-negative integers.
    -   When an escape character is used by **table\_references** for escaping, verification rules are strictly matched based on letter cases during SQL parsing. As a result, letter cases of the schema and table names in the SQL statement written by a user must be the same as those of metadata in the database.
    -   By default, parameters in **column\_expr** and **condition\_expr** are case insensitive.
    
2.  Union operation syntax
    
    **SELECT** ... /\* Query statements \*/
    
    **UNION** \[ **ALL** \] /\* When UNION expression is used without ALL, lines are deduplicated. \*/
    
    **SELECT** ... /\* Query statements \*/
    
    ![[caution_3.0-en-us.png]]
    
    If the number of query records is not specified (namely, the LIMIT clause is not used), a maximum of 10,000,000 cells can be exported by default. (The number of records specified by the LIMIT clause can be obtained through dividing 10,000,000 by the number of columns.) **10000000** is the value of **Default Cells in the Result Set** configured on the **Result Set Data Volume Configuration** page.
    
3.  Syntax of common table expression (CTE statements)
    
    **WITH** alias **AS** ( select\_expr /\* Query statements \*/ )
    
    **SELECT** ... /\* Query statements. The table name can be the alias of WITH \*/
    
    ![[note_3.0-en-us.png]]
    
    -   **\[ ... \]** in the preceding statement indicates an optional statement.
    -   In the ClickHouse database, conditions following **WITH** can only be a single value. The WITH syntax is parsed into a syntax for the sub-query.