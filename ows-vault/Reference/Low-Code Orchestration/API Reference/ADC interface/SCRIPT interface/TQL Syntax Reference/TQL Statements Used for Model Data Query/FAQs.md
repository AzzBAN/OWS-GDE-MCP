---
title: "FAQs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_tql_013.html"
depth: 6
---
#### In the TQL Statement with GROUP BY Clauses, the SELECT Clause Queries the Original Property and the Property Is Not in the Aggregate Function

For example, the following statement is incorrect:

select title, category from book group by category

The preceding statement is used to perform grouping based on **category**. However, the original title property is queried using the SELECT clause. A category may contain different titles. Therefore, it is inappropriate to use any title as the title of the category. Therefore, this query is invalid. Even if this query can be performed, the results are uncertain.

If the GROUP BY clause is used, the SELECT and ORDER BY clauses cannot be used to directly query the original data. Only the following content can be used:

-   Expression in the GROUP BY clause
-   Aggregation operation performed on the original query results