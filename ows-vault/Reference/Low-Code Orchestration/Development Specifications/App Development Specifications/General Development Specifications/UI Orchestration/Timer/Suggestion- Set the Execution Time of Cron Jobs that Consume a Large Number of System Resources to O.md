---
title: "Suggestion: Set the Execution Time of Cron Jobs that Consume a Large Number of System Resources to Off-Peak Hours"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804072.html"
depth: 6
---
# Suggestion: Set the Execution Time of Cron Jobs that Consume a Large Number of System Resources to Off-Peak Hours

**Description**: If a cron job consumes a large number of system resources, execute the cron job during off-peak hours (for example, at night) to avoid affecting service experience.

**Check guide**: 1. View the scheduled task configuration in the develop-state environment and check the task execution duration; 2. Check the code for registering a scheduled task and the execution duration; 3. Query the execution duration of the custom task in the runtime-state environment and check whether the task execution duration is proper.

**Tool supported or not**: no

**Specification name**: General\_Timer\_High\_Load\_Task\_Executed\_in\_Off\_Peak\_Hours

**Severity**: suggestion

**Parent topic:** [[Timer|Timer]]