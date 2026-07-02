---
title: "Complete TQL Statement Syntax"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_tql_007.html"
depth: 6
---
#### SELECT Clause

A SELECT clause is used to describe the content to be provided in the query result. The SELECT clause syntax is as follows:

SELECT \[ DISTINCT \] { \* | { _expression_ \[ \[ AS \] _alias_ \] \[ , ... \] } }

-   DISTINCT
    
    If the **DISTINCT** keyword is specified, only one record is retained in the query result, that is, duplicate records are deleted. Note that duplication is for an entire record not for a single field.
    
-   \*
    
    An asterisk (\*) indicates that if no GROUP BY clause is used in the TQL statement, all fields in the model or subquery (for details about subquery, see [FROM Clause](#EN-US_TOPIC_0000001149607153__section138111127141611)) specified by the FROM clause are queried. Otherwise, all grouping result fields are queried.
    
-   expression
    
    The results of the expression specified by _expression_ in the clause are returned in the query results. The results can consist of property names, functions, operators, and other expressions. For details, see [[Operators and Expressions|Operators and Expressions]]. The expression is subject to the GROUP BY... HAVING clause. For details, see [GROUP BY... HAVING Clause](#EN-US_TOPIC_0000001149607153__section1579340121613).
    
-   AS
    
    **AS** indicates the keyword that separates the expression and alias, and can be omitted.
    
-   alias
    
    _alias_ indicates the alias of the expression in the clause. The field name in the query result set indicates the alias. Its format is the same as that of an identifier.
    

Example:

To query the title and author from the book model, run the following statement:

select title, author from book

To query unique categories and authors from the book model, run the following statement:

select distinct category, author from book