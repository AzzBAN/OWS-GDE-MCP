---
title: "Suggestion: Properly Add a Timeout Interval for API Calls"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001767985508.html"
depth: 6
---
# Suggestion: Properly Add a Timeout Interval for API Calls

**Description**: For example, if the timeout interval is not added for the requestApi control, an error is reported every time the control fails to be executed due to unstable network. After the timeout interval is added, the system retries within the specified timeout interval to improve the API call success rate. The timeout interval cannot be less than the actual response timeout interval of the API. Otherwise, the control fails to be executed before the API gives a response.

**Check guide**: Check whether the requestApi control is used in the process script.

**Tool supported or not**: no

**Specification name**: General\_RPA\_Use\_Timeout\_For\_API

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]