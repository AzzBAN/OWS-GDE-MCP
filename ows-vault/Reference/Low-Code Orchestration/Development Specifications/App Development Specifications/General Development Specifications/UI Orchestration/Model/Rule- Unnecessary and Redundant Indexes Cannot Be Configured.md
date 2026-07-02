---
title: "Rule: Unnecessary and Redundant Indexes Cannot Be Configured"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804028.html"
depth: 6
---
# Rule: Unnecessary and Redundant Indexes Cannot Be Configured

**Description**: Index storage occupies space, and index update also consumes resources. Too many indexes deteriorate database modification performance and waste storage space. To prevent unnecessary performance overhead, do not create redundant indexes. When you configure an index, determine whether the index is necessary in terms of the following aspects:

-   The index must be created for a specific purpose. Do not create indexes that are not used as search criteria. Exercise caution when creating indexes that are rarely used as search criteria.
-   A combined index consisting of multiple properties can replace a **non-uniquely-combined** index consisting of such properties. For example, the index formed by properties **a**, **b**, and **c** can replace the non-unique index formed by properties **a** and **b** in sequence. The non-unique index formed by properties **a** and **b** is redundant. This is because relational databases also try to use the index when few properties before the index are used as query conditions.
-   A combined index consisting of multiple properties can be replaced by a uniquely combined index consisting of such properties. For example, the index formed by properties **a**, **b**, and **c** can replace the unique index formed by properties **a** and **b** in sequence. The unique index formed by properties **a** and **b** is redundant. Because the uniqueness of the data with few properties can be determined, it is futile to add more properties to the index.

For a single primary key property model, the primary key property is the unique index. For multiple primary key property models, a composite unique index is created for these primary key properties. The property sequence in the index is the ASCII code sequence of the property name. The preceding rules also apply to an index consisting of primary key properties.

**Check guide**: Log in to the develop-state environment and go to the model details page. The **Property Index** tab page is displayed. Check whether the indexes are necessary from the preceding aspects.

**Negative example**: An index defined by properties **a**, **b**, and **c** and an index defined by properties **a** and **b** exist. According to the preceding description, there must be a redundant index.

As shown in the following figure, **text1** is the unique index, and the common index consisting of **text1** and **text2** is redundant.

![[en-us_image_0000002157018628.png]]

**Tool supported or not**: no

**Specification name**: General\_Model\_Disallow\_Redundant\_Index

**Severity**: minor

**Parent topic:** [[Model|Model]]