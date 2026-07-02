---
title: "Suggestion: Do Not Create a Cron Job Whose Execution Interval Is Less Than 5 Minutes"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523389.html"
depth: 6
---
# Suggestion: Do Not Create a Cron Job Whose Execution Interval Is Less Than 5 Minutes

**Description**: On the premise that service requirements are met, select the longest execution interval to reduce system resource consumption and avoid latency caused by cron job blocking. It is recommended that the execution interval be greater than or equal to 5 minutes.

**Check guide**: 1. View the cron job configuration in the develop-state environment and check the task execution interval; 2. Check the code for registering a cron job and the execution interval; 3. Query the execution interval of the customized task in the runtime-state environment and check whether the task execution frequency is proper.

**Tool supported or not**: yes

**Specification name**: General\_Timer\_Avoid\_Scheduled\_Tasks\_Period\_Less\_Than\_5\_Minutes

**Severity**: suggestion

**Parent topic:** [[Timer|Timer]]