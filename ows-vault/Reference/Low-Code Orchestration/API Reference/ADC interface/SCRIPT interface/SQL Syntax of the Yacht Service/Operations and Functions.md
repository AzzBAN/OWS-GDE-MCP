---
title: "Operations and Functions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001628553533.html"
depth: 5
---
#### Operator

   
| Type | Operator | Example | SQL Compatibility |
| :-- | :-- | :-- | :-- |
| Unary logical operation | 
-   expr IS NULL: indicates whether expr is empty.

-   expr IS NOT NULL: indicates whether expre is not empty.
-   **expr** is of the Boolean type.

 | select 1 IS NULL;
select 1 IS NOT NULL;
select NOT TRUE;

 | \- |
| Fuzzy matching | -   **LIKE** 'reg'
-   **NOT LIKE** 'reg'

NOTE: reg indicates a character string. %: Match zero or multiple % characters. \_: Match one \_ character. | SELECT 'abc' LIKE 'a%';
SELECT 'abc' NOT LIKE 'a%';

 | \- |
| Binary mathematical operation | -   expr **+** expr
-   expr **\-** expr
-   expr **\*** expr
-   expr **/** expr
-   expr **%** expr
-   If **expr** is of the numeric type, the calculation result is of the numeric type.

 | select 1 + 1;
select 1 - 1;
select 1 \* 1;
select 1 / 1;
select 1 % 1;

 | 1.  **expr / expr**: This function is not supported by PostgreSQL.
2.  **expr % expr**: This function is not supported by SparkSQL.

 |
| Binary comparison operation | -   expr **\=** expr
-   expr **!=** expr
-   expr **<>** expr
-   expr **<** expr
-   expr **<=** exp
-   rexpr **\>** expr
-   expr **\>=** expr
-   If **expr** is a number or a character string, the result is of the Boolean type.

 | select 1 = 1;
select 1 != 1;
select 1 <> 1;
select 1 < 1;
select 1 <= 1;
select 1 > 1;
select 1 >= 1;
select 'a' = 'a';
select 'a' != 'a';
select 'a' <> 'a';
select 'a' < 'a';
select 'a' <= 'a';
select 'a' > 'a';
select 'a' >= 'a';

 | \- |
| Binary logic operation | -   expr **OR** expr
-   expr **AND** expr
-   If **expr** is of the Boolean type, the result is of the Boolean type.

 | select TRUE OR TRUE;
select TRUE AND TRUE;

 | The following scenarios are not supported:

1.  **expr OR expr**: This function is not supported by PostgreSQL and SparkSQL.
2.  **expr || expr**: expr OR expr is changed to expr || expr in PostgreSQL. expr OR expr is not supported by SparkSQL.
3.  **expr && expr**: This function is not supported by PostgreSQL and SparkSQL.
4.  **TRUE/true, FALSE/false**: This function is not supported by ClickHouse.

 |
| Unary bit operation | ~: Bitwise exclusive for integers. | select ~1;

 | This function is not supported by SQL Editor. |
| Binary bit operation | -   expr **|** expr
-   expr **&** expr
-   expr **^** expr
-   If **expr** is an integer, the result is an integer.

 | select 1 | 1;
select 1 & 1;
select 1 ^ 1;

 | 1.  **expr << expr**: This function is not supported by SparkSQL.
2.  **expr >> expr**: This function is not supported by SparkSQL.
3.  **expr | expr**, **expr & expr**, and **expr ^ expr** is not supported by ClickHouse.

 |
| Interval judgment | -   **expr BETWEEN min AND max** is equivalent to **min <= expr AND expr <= max**.
-   expr **NOT BETWEEN** min **AND** max
-   **expr** is a number or a character string.

 | select 5 BETWEEN 3 AND 5;
select 5 NOT BETWEEN 3 AND 5;

 | \- |
| Branch | -   \[**WHEN** ...\] **ELSE** \[result\] **END** :
    -   **CASE** **WHEN** condition **THEN** result
    -   **CASE** expr **WHEN** value **THEN** result
-   **condition** is of the Boolean type.
-   **expr** is a number or a character string.
-   **COALESCE(value \[, ...\])** returns the value of the first parameter that is not empty.
-   **NULLIF(value1, value2)**: If **value1** is equal to **value2**, **NULL** is returned. Otherwise, **value1** is returned.
-   **IFNULL****(value1, value2)** returns the value of the first parameter that is not empty. If **value1** is not empty, **value1** is returned. If it is empty, **value2** is returned. **value1** and **value2** must be of the same type.

 | select case when 1 then 1 else 0 end;
select case 1 when 1 then 1 else 0 end;
select COALESCE(null,1,2);
select NULLIF(1,2);
select IFNULL(null, 3);

 | \- |
| List judgment | -   IN(expr \[, expr\] ...)

-   NOT IN(expr \[, expr\] ...)
-   **expr** is a number or a character string.
-   **NOT IN** cannot be used for query in the SQL statement editing pane of **Module**.

 | select 0 IN(1,2,3,4,5);
select 0 NOT IN(1,2,3,4,5);

 | \- |