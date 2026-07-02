---
title: "Rule: Do Not Develop or Upload Malicious Code or Files"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404051253.html"
depth: 5
---
# Rule: Do Not Develop or Upload Malicious Code or Files

**Description**:

1\. Jupyterlab provides an open model development environment. Malicious files and scripts may be used by other users to steal user privacy or data. It is prohibited to upload malicious files and scripts to the platform.

2\. Algorithm codes cannot contain attack behaviors, such as network scanning, malicious data operations, and violent query.

**List of high-risk libraries**: subprocess, os.popen, requests, urllib3, os.system, pty.spawan, \_posixsubprocess, nmap, PyHook, and others

**Check guide**:

1\. Check the Python script uploaded to the system to ensure that the Python script contains only proper and correct service processing logic.

2\. In the develop-state environment, click **Project Quality Assessment** on the **Project Management** page to check the project quality.

**Tool supported or not**: yes

**Specification name**: Security\_AI\_Coding

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: all

**Parent topic:** [[Protection Against Malicious Operations|Protection Against Malicious Operations]]