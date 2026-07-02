---
title: "Basic TQL Concepts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_tql_003.html"
depth: 6
---
#### Identifier

An identifier is used to refer to a specific object. The object is determined by the specific scenario and its position in the TQL statement. For example, in the model data query scenario, the identifiers may be the model name and property name, which correspond to the table name and field name in the SQL statement, respectively.

Identifiers are case sensitive. In most cases, an identifier must start with a letter which can be followed by letters, digits, and underscores (\_). If special characters such as spaces are required in an identifier, enclose the special characters with double quotation marks (""). For details, see [Quotation Mark](#EN-US_TOPIC_0000001102487468__section367673233216).

An identifier can be separated by dots (.), which is commonly used in scenarios where a field in a table is referenced by a table name or alias. A maximum of two dots are supported, that is, the identifier is divided into three parts. When you use a dot (.) to separate an identifier, if you need to use double quotation marks (""), place the dot (.) outside the double quotation marks (""), for example, "book"."author".