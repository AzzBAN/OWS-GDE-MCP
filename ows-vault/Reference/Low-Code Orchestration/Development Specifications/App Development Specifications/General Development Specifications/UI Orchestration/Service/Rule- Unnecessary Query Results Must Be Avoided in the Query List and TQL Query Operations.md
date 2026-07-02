---
title: "Rule: Unnecessary Query Results Must Be Avoided in the Query List and TQL Query Operations"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804036.html"
depth: 6
---
# Rule: Unnecessary Query Results Must Be Avoided in the Query List and TQL Query Operations

**Description**: By default, the GetList service of the system returns the total number of model instances. The **SELECT COUNT (id) FROM** _XXX_**;** statement is executed at the bottom layer. For tables with a large amount of data, this operation may be slow. Therefore, you can disable the COUNT query to improve performance. If you do not need to query the total number of results, disable the COUNT query.

**Check guide**: Check based on the actual service situation.

If the count does not need to be summarized, ignore the count query according to the example and attach the default value **0** to **total**. **total** is not queried during query.

**Positive example**:

If summary is not required in the query list, do not select **Total**.

![[en-us_image_0000001468852890.png]]

Deselect **Total number of query results** if the total number of statistical and query results for the TQL Query service is not required.

![[en-us_image_0000001519652741.png]]

**Tool supported or not**: no

**Specification name**: General\_Service\_Disallow\_Unnecessary\_Query\_Count

**Severity**: minor

**Parent topic:** [[Service|Service]]