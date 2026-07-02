---
title: "Rule: Proper Indexes Must Be Configured for a Common Model Query Property"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523349.html"
depth: 6
---
# Rule: Proper Indexes Must Be Configured for a Common Model Query Property

**Description**: Proper indexes need to be configured for properties that are frequently used as query conditions (including filter criteria and aggregation operations) to improve query performance. The following aspects must be considered for proper indexes:

-   Determine whether to configure common indexes (non-unique indexes), unique indexes, single-property indexes, or combined indexes based on data distribution and query scenarios.
-   For properties that are frequently queried together, combined indexes can be configured. However, redundant indexes need to be avoided. For details, see the next rule.
-   You are advised not to create indexes for properties that are rarely used. For example, if a property can only be set to **Male** or **Female**, independent indexes are not suitable for this property.
-   The property sequence of a combined index should be arranged according to the property use frequency and property value priority in descending order.
-   After writing a TQL statement, you need to debug and view the interpretation plan to ensure that the index is hit.

**Check guide**: Log in to the develop-state environment, choose **Model**, and go to the model management page. The **Property Index** tab page is displayed. Check whether the configured index can be used in some scenarios.

As shown in the following figure, the model has two indexes: unique index **text1** and common index **text2**.

![[en-us_image_0000002192573369.png]]

**Positive example**: When the key has been defined as the primary key property for a dictionary model, if reverse query is frequently used (querying the key based on the value), you can define the value property as an index.

**Tool supported or not**: no

**Specification name**: General\_Model\_Proper\_Query\_Index

**Severity**: minor

**Parent topic:** [[Model|Model]]