---
title: "Differences Between TQL and TEL Statements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_tql_005.html"
depth: 6
---
# Differences Between TQL and TEL Statements

The main functions and application scenarios of TQL and TEL statements are different. In a specific scenario, only either of them is used. For details, see the development guide for the specific scenario. For example, TQL statements instead of TEL statements are used for model data query.

-   TQL statements are used for query.
    
    TQL statements are used to query data that meets the specified conditions from the existing data based on the criteria specified in TQL statements. A typical scenario is as follows: During model data query, TQL statements are used to specify query conditions and further calculate the query result (such as grouping and aggregation).
    
-   TEL statements are used for the expression calculation.
    
    TEL statements are used to calculate the given data based on the expressions specified in TEL statements to obtain the calculation result.
    

Other differences are as follows:

-   Variables can be used in TQL statements but cannot be used in TEL statements.
    
    TQL statements are used in the scenario where a trigger is triggered by a business logic (for example, the business side calls a service or an API of a model). You can use a variable as a placeholder in a TQL statement, and the calling party transfers a specific value to obtain a complete TQL statement for execution.
    
    However, TEL statements are generally used when data is changed (for example, the model data is changed). Therefore, a parameter (that is, an identifier in a TEL statement) calculated by a TEL statement comes from the context of the TEL statements (for example, model data that is actually changed). Additional values don not need to and cannot be transferred through mechanisms, such as variables.
    

TQL statement examples in the model data query scenario:

author = 'Tom' -- Data filtering TQL statement, which is used to query the data whose author is Tom
select title from book where author = 'Tom' and nationality = $nationality -- Complete TQL statement, which is used to query the book whose author is Tom and the author's nationality is transferred by a variable
select author, count(1) as count from book group by author -- Complete TQL statement, which is used to collect statistics on the number of works of each author

**Parent topic:** [[TQL Overview|TQL Overview]]