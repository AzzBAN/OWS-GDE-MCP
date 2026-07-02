---
title: "Rule: Operation Logs Must Be Recorded for Non-Query Services Opened to the Frontend"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208200529.html"
depth: 5
---
# Rule: Operation Logs Must Be Recorded for Non-Query Services Opened to the Frontend

**Description**: Security events include login, logout, user creation, deletion and modification, authorization, authorization releasing, authentication, and password changes. Operation events include service system configuration parameter modification and important service data creation, deletion, modification and query. No matter whether these events are successful or failed, logs are required.

**Check guide**: Check whether the services that can be accessed by the frontend contain non-query operations.

**Positive example**: If the operation is performed on frontend services and is a non-query operation, you need to enable **Operation log**.

![[en-us_image_0000001522029253.png]]

**Note**: Record only necessary operation logs for services that are called only by the backend to prevent operation log flooding.

**Tool supported or not**: yes

**Specification name**: Security\_Log\_ShouldRecordOperationLog

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: UI orchestration

**Parent topic:** [[Logs|Logs]]