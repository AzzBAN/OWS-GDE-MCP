---
title: "Appendix 3: Three Normal Forms for Data Modeling"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804212.html"
depth: 5
---
# Appendix 3: Three Normal Forms for Data Modeling

**First normal form (1NF):**

Each specific relationship r in the relational pattern R must have a primary key, and each attribute value is the minimum data unit that is indivisible. In this case, relationship R belongs to the first normal form.

-   The attribute values displayed in each column are indivisible to ensure the column atomicity.
-   For two columns with similar or same attribute values, merge the columns if possible to prevent redundant data.

**Second normal form (2NF):**

If all non-key attributes in relational schema R are completely dependent on the primary key, relationship R belongs to the second normal form.

Each row of data can be related to only one column. That is, a row of data can be used for one purpose only. The table needs to be split as long as duplicate data is found in a data column.

**Third normal form (3NF):**

Non-primary keys in the relational schema R cannot depend on other non-primary keys. That is, there is no function (transfer) dependency among non-primary keys. In this case, relationship R belongs to the third normal form.

**Parent topic:** [[Data Category|Data Category]]