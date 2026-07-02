---
title: "Rule: Proper Length Must Be Defined for the Text Type Property of a Rule Model"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123584.html"
depth: 6
---
# Rule: Proper Length Must Be Defined for the Text Type Property of a Rule Model

**Description**: Text properties include the text type parameter and maximum length parameter. These parameters directly affect the types of database fields. However, once the field type is determined, the field type cannot be modified when there is data in the table or the modification costs a lot. Therefore, when setting these parameters, you need to fully understand the meanings of these parameters and consider the current and future requirements for these properties. Consider at least the following aspects:

-   The length of the text property is not the long the better. For example, if the number of characters exceeds 250 but does not exceed 1000, indexes can be created. However, the database does not support long indexes. Prefix indexes may be used to replace full indexes. As a result, indexes cannot be used in queries such as **distinct**, **group by**, and **order by**.
-   For a property that is not used as a query condition and that the **distinct**, **group by**, or **order by** operation is not performed on (such as description), it is unnecessary to define the text type as short text. The short text type occupies the line length, which may cause the line length to exceed the limit of the database.

**Check guide**: In the develop-state environment, open the property list of the corresponding model and check whether the property length of the text type is proper in the service scenario. For a property of the text type that contains more than 250 characters, check whether the length can be cut and whether an index needs to be created for the property. Texts are classified into the following types based on the text length:

-   Short text: a text property that contains a maximum of 250 characters. It is usually used to store short content such as IDs and categories, and is often used as a query condition or a grouping condition. When independent indexes (non-joint indexes) are created for such text properties, complete indexes (non-prefix indexes) can be created. In **distinct**, **group by**, and **order by** query operations, indexes can be used to improve performance.
-   Common text: a text property contains a maximum of 1000 characters. It is usually used to store content that is slightly longer than a short text, such as a name. It is used as a query condition, but is not often used as a grouping condition. Although indexes can be created for such text properties, only prefix indexes can be created. In **distinct**, **group by**, and **order by** queries, prefix indexes cannot be used to improve performance.
-   Long text: a text property that contains more than 1000 characters. It is usually used to store large segments of text such as description and details, and is seldom used as a query condition. This type of text properties cannot be indexed and cannot be used for **distinct**, **group by**, or **order by**.

As shown in the following figure, the properties of the three text types from top to bottom are short text (200 characters), common text (500 characters), and long text (256 KB).

![[en-us_image_0000001718874112.png]]

**Negative example**: Define the maximum length of a text property as 1000 characters or a larger value, even if the property contains only dozens of characters.

**Exception scenario**: When the model data volume is small (for example, less than 1000 records) and the service requirements are met, the performance of the corresponding scenario can be accepted by the service after the test of each type of database. Long text properties can be used but indexes or indexes in **distinct**, **group by**, and **order by** queries are unavailable.

**Tool supported or not**: no

**Specification name**: General\_Model\_Proper\_Text\_Property\_Size

**Severity**: minor

**Parent topic:** [[Model|Model]]