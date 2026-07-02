---
title: "Suggestion: Exercise Caution When Using Cron Timers"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001471545938.html"
depth: 6
---
# Suggestion: Exercise Caution When Using Cron Timers

**Description**: Cron timers are triggered as scheduled. If too many Cron timers are configured, a large number of cron jobs are triggered at the same time, which increases the system pressure.

**Check guide**: 1. Check the configuration time of the Cron timer. Do not run the Cron timer and other timers at the same time.

**Tool supported or not**: no

**Specification name**: General\_Timer\_Avoid\_Use\_Cron\_Scheduled\_Tasks

**Severity**: suggestion

**Parent topic:** [[Timer|Timer]]