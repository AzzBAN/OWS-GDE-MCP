---
title: "Rule: distinct, group by, or order by Query Operations Cannot Be Performed on Long or Non-indexed Text Properties in Models with a Large Amount of Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363457.html"
depth: 6
---
# Rule: distinct, group by, or order by Query Operations Cannot Be Performed on Long or Non-indexed Text Properties in Models with a Large Amount of Data

**Description**: If the **distinct**, **group by**, or **order by** query operation is performed on properties without indexes in a model with a large amount of data, the query takes a long time and the performance overhead is high.

For a text property that contains more than 250 characters, indexes can be created for the corresponding fields. However, some databases do not support the function of creating indexes for long complete content. Therefore, only the first several characters are used as the index content (prefix index). In this case, the **distinct**, **group by**, and **order by** queries do not use these indexes. If the data volume of a model to be queried is large, the query takes a long time and the performance decreases.

**Check guide**: In the develop-state environment, check each service that contains the TQL query type and running script type. If there are **distinct**, **group by**, and **order by** queries, check whether the corresponding properties of the queried model have proper indexes. The length of the corresponding text property cannot exceed 250 characters.

**Positive example**: Based on actual query scenarios, define proper indexes for queries that are frequently used such as **distinct**, **group by**, and **order by**, and fully verify the indexes in multiple databases to ensure that the indexes take effect in these scenarios.

**Tool supported or not**: no

**Specification name**: General\_Model\_Avoid\_Complex\_Queries\_on\_Unindexed\_Attributes\_in\_a\_Large\_Data\_Volume\_Model

**Severity**: major

**Parent topic:** [[Model|Model]]