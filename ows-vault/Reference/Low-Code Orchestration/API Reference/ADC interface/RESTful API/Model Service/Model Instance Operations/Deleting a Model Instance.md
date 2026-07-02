---
title: "Deleting a Model Instance"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_BaseInstanceApiService_batch-delete-tqlPOST.html"
depth: 6
---
#### Function

It starts with GDE24.2. This API is used to delete model instances in batches based on the model URI. For compatibility, use the V2 API. When data model instances are deleted in batches, a maximum of 10,000 data records can be processed. If the number of data records exceeds 10,000, the interface needs to be invoked for multiple times. When elastic model instances are deleted in batches, a maximum of 10,000 data records can be processed by default. You can adjust the upper limit by setting the tenant-level system parameter max-elastic-model-delete-limit. If the number of data records exceeds the upper limit, the interface needs to be invoked for multiple times.