---
title: "Suggestion: Do Not Use the O(n) Complex Command When Redis Is Used In Orchestration Scripts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001615027380.html"
depth: 6
---
# Suggestion: Do Not Use the O(n) Complex Command When Redis Is Used In Orchestration Scripts

**Description**: Exercise caution when using range query commands and commands for which the time complexity is greater than O(n). When the data volume is large, running these commands may cause service jitter, slow query, or congestion.

**Check guide**:

Check whether the following Redis usage is included in all JS scripts in the API package:

redis.GLOBAL.lget(key, start, end)
redis.forName("redisServiceName").lget(key, start, end)

If the usage cannot be avoided, specify the values of **start** and **end**.

**Negative example**:

redis.GLOBAL.lget(key, 0, -1)
redis.forName("redisServiceName").lget(key, 0, -1)

**Tool supported or not**: no

**Specification name**: General\_API\_Redis\_Avoid\_Range\_Operation\_In\_JsScript

**Severity**: suggestion

**Parent topic:** [[Openness Integration|Openness Integration]]