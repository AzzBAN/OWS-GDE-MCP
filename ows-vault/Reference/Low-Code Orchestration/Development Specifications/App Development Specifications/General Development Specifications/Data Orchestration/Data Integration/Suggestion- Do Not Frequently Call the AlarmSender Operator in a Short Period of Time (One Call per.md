---
title: "Suggestion: Do Not Frequently Call the AlarmSender Operator in a Short Period of Time (One Call per Minute)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001604632956.html"
depth: 6
---
# Suggestion: Do Not Frequently Call the AlarmSender Operator in a Short Period of Time (One Call per Minute)

**Specification name**: General\_DataFactory\_AIP\_Avoiding\_Send\_alarms

**Description**: During app orchestration, do not frequently call the AlarmSender operator to send alarms. You are advised to send alarms properly based on service scenarios to prevent a large number of alarms from being generated in the GDE management zone.

**Check guide**: Check whether the AlarmSender operator is frequently called in the app.

**Negative example**:

-   The AlarmSender operator is called in the Foreach operator.
-   After the Scheduler(S) operator is triggered frequently, the AlarmSender operator is called to send alarms without any restrictions.

**Impact**: A large number of alarms are generated in the GDE management zone, affecting service experience.

**Parent topic:** [[Data Integration|Data Integration]]