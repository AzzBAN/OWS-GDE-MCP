---
title: "Suggestion: Do Not Create More Than 1000 Cron Jobs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283608.html"
depth: 6
---
# Suggestion: Do Not Create More Than 1000 Cron Jobs

**Description**: Too many cron jobs cause great pressure on the system, especially when the tasks are executed concurrently. You are advised to plan the number of cron jobs based on service scenarios. If you need to periodically delete data generated before a certain time point, use one cron job instead of creating cron jobs for each data record.

**Check guide**: 1. Check the code for registering cron jobs and check whether the task registration is proper. 2. Query the execution period of the cron job in the runtime-state environment and check whether the job execution frequency is proper. 3. Check whether the JavaScript script contains the code for cyclically creating cron jobs.

**Tool supported or not**: no

**Specification name**: General\_Timer\_Avoid\_Create\_Too\_Many\_Scheduled\_Tasks

**Severity**: suggestion

**Parent topic:** [[Timer|Timer]]