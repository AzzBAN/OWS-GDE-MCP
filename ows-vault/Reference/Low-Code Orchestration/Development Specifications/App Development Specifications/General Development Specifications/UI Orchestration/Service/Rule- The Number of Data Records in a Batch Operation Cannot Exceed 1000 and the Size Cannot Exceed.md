---
title: "Rule: The Number of Data Records in a Batch Operation Cannot Exceed 1000 and the Size Cannot Exceed 1 MB"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001491702322.html"
depth: 6
---
# Rule: The Number of Data Records in a Batch Operation Cannot Exceed 1000 and the Size Cannot Exceed 1 MB

**Description**: If a large amount of data is received by the batch operation service at a time, a large amount of memory is occupied. In high-frequency service call scenarios, microservice memory overflow may occur. To avoid that issue, the batch operation service needs to limit the data volume in a single request.

**Check guide**: Check the amount of data transmitted during a single call of the batch operation service at the service calling client. Batch operation types include **BatchCreate**, **BatchUpdate**, **BatchDelete**, **BatchOperation**, and **Batch Supplement**.

**Positive example**: The number of data records in a batch operation cannot exceed 1000, and the size cannot exceed 1 MB.

**Tool supported or not**: no

**Specification name**: General\_Service\_Batch\_Operation\_Disallow\_Too\_Many\_Data

**Severity**: minor

**Parent topic:** [[Service|Service]]