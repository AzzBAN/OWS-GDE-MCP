---
title: "Introduction to the Elastic Model TQL Statements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_tql_009.html"
depth: 6
---
# Introduction to the Elastic Model TQL Statements

TQL statement query capabilities supported by elastic models are a subset of statements described in [[Complete TQL Statement Syntax|Complete TQL Statement Syntax]] and [[Data Filtering TQL Statement Syntax|Data Filtering TQL Statement Syntax]]. However, the elastic model TQL statements also have some unique functions. The differences are as follows:

-   The elastic model does not support associated query. That is, the JOIN ... ON and UNION clauses, and the FROM clause that contains multiple models are not supported.
-   The elastic model does not support subqueries. That is, subqueries cannot be used in the FROM clause, and operators, such as in, that support subqueries do not support subqueries.
-   Elastic models and common data models support different TQL functions. For details, see [[TQL Functions|TQL Functions]].
-   Elastic models and common data models support different expression operators and operands. For details, see [[Operators and Expressions|Operators and Expressions]].

**Parent topic:** [[TQL Statements Used for Model Data Query|TQL Statements Used for Model Data Query]]