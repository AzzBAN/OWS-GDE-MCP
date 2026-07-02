---
title: "Rule: Robot Process Package Cannot Carry Malicious or Low-Quality Code or Binary Programs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523529.html"
depth: 5
---
# Rule: Robot Process Package Cannot Carry Malicious or Low-Quality Code or Binary Programs

**Description**: The robot process can call functional units that are compiled using the languages, such as python, Java, C#, C++, and VBS. The untrusted functional units may cause serious consequences.

**Check guide**: Check whether the asset package contains files suffixed with **\*.vbs**, **\*.bat**, **\*.js**, **\*.py**, **\*.pyc**, **\*.exe**, **\*.dll**, **\*.jar**, **\*.class**, **\*.sh**, or **\*.msi**.

**Positive example**: The robot process package does not contain files with the preceding suffix or related files have passed security inspection.

**Negative example**: none

**Tool supported or not**: yes

**Specification name**: Security\_Others\_RPA\_Forbid\_MaliciousLow-qualityCode

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: RPA orchestration

**Parent topic:** [[Others|Others]]