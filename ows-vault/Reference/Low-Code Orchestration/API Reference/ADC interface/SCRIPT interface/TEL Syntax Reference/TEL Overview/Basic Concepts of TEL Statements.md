---
title: "Basic Concepts of TEL Statements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_tel_003.html"
depth: 6
---
#### Identifier

An identifier is used to refer to a specific object that is determined by the specific scenario and its position in the TEL statement.

Identifiers are case sensitive. In most cases, an identifier must start with a letter followed by letters, digits, and underscores (\_). If special characters such as spaces are required in an identifier, enclose the special characters with double quotation marks (""). For details, see [Quotation Mark](#EN-US_TOPIC_0000001102487668__section367673233216).

An identifier can be separated by dots (.), which is commonly used in the scenario where a field in a table is referenced by a table name or alias. A maximum of two dots can be used in an identifier, that is, the identifier is divided into three parts. When a dot (.) is used to separate identifiers, if double quotation marks ("") are required, write the dot (.) outside the double quotation marks(""), for example, "book"."author".