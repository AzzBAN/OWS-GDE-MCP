---
title: "Data Filtering TQL Statement Syntax"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_tql_008.html"
depth: 6
---
# Data Filtering TQL Statement Syntax

As a subset of the complete TQL statements, the data filtering TQL statements support only the data filtering of a single model, that is, only the WHERE clause (without the WHERE keyword), ORDER BY clause, and START... LIMIT clause are supported. The syntax of a complete data filtering TQL statement is as follows:

_condition\_expression_
  \[ ORDER BY { _expression_ } \[ ASC | DESC \] \[ , ... \] \]
  \[ \[ START _start_ \] LIMIT _limit_ \]

For details about the syntax, see the description of the corresponding clause in [[Data Filtering TQL Statement Syntax|Data Filtering TQL Statement Syntax]].

![[note_3.0-en-us.png]]

-   Whether the ORDER BY and START... LIMIT clauses are supported depends on the application scenarios.

Example:

-   To query English scientific books and sort them by title in ascending order, run the following statement:
    
    category = 'science' and language = 'English' order by title
    
-   To query the person whose name is Tom and age is older than 20 and the person whose name is Jim and age is older than 30, run the following statements:
    
    name = 'Tom'
    (name = 'Tom' and age > 20) or (name = 'Jim' and age > 30)
    

This type of TQL statements can be used to query a single data record and query lists in service orchestration.

**Parent topic:** [[TQL Statements Used for Model Data Query|TQL Statements Used for Model Data Query]]