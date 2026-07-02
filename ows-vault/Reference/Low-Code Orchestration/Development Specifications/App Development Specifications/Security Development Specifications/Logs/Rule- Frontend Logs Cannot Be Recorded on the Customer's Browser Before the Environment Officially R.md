---
title: "Rule: Frontend Logs Cannot Be Recorded on the Customer's Browser Before the Environment Officially Runs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523513.html"
depth: 5
---
# Rule: Frontend Logs Cannot Be Recorded on the Customer's Browser Before the Environment Officially Runs

**Description**: The impact of debug logs on the system performance and log storage space is large. In addition, the amount of the information recorded in debug logs is increased, which may cause improper information disclosure. Therefore, do not record logs at the frontend in the official running environment.

**Check guide**: Search for JavaScript files in the release package and check whether the **console.log** file exists. If the file exists, delete it. This file can be used only for development and debugging.

**Code example**:

console.log("Important and sensitive information. ");
console.log("pwd"+pwd);

**Tool supported or not**: yes

**Specification name**: Security\_Log\_DoNotPrint\_Frontend

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: UI orchestration

**Parent topic:** [[Logs|Logs]]