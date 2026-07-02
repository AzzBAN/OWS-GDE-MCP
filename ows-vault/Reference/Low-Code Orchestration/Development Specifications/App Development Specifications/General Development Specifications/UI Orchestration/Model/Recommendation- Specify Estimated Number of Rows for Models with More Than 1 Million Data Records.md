---
title: "Recommendation: Specify Estimated Number of Rows for Models with More Than 1 Million Data Records"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001200321492.html"
depth: 6
---
# Recommendation: Specify Estimated Number of Rows for Models with More Than 1 Million Data Records

**Description**: If the orchestrated model stores a large amount of data, specify **Estimated Number of Rows**. Based on the configured value, the system automatically analyzes slow query processing to remind users of developing apps with better performance. Currently, the platform considers a model with more than 1 million data records as a large table.

**Check guide**: In the develop-state environment, open the property list of the model and click **Edit** to check whether the estimated number of rows is configured for a large table.

**Positive example**: For a model with a large table, if the data volume exceeds 10 million, set **Estimated Number of Rows** to **10000000**.

![[en-us_image_0000001693374633.png]]

**Negative example**: The estimated number of rows is not configured for a large table or the configuration is incorrect.

**Tool supported or not**: no

**Specification name**: General\_Model\_Huge\_Model\_Config\_Estimated\_Row\_Count

**Severity**: suggestion

**Parent topic:** [[Model|Model]]