---
title: "Rule: Unauthorized Operations Cannot Be Performed in Python Scripts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162800590.html"
depth: 5
---
# Rule: Unauthorized Operations Cannot Be Performed in Python Scripts

**Description**: In Python activities of technical jobs, you can customize Python scripts and encapsulate them into activities. The Python scripts can be used to parse and determine command activity results. You can only write normal service logic in Python scripts. Do not execute invalid logic that is mainly targeted at attacks in Python scripts, for example, CPU and memory resources are consumed by infinite loops or invalid logic, and disk space resources are consumed by writing invalid files.

Do not use high-risk libraries. Otherwise, an alarm is generated. When an alarm is generated, developers need to confirm the alarm and modify it.

**List of high-risk libraries**: subprocess, os.popen, requests, urllib3, os.system, pty.spawan, \_posixsubprocess, os.execv, os.execp, os.exece, os.spawnv, os.spawnve,

os.kill, os.execl, os.execle, os.execlp, os.execvp, os.edecvpe, os.spawnl, os.spwanle, os.popen2(/3/4), pty.fork, exec, and eval

**Check guide**:

1\. Check the Python script uploaded to the system to ensure that the Python script contains only proper and correct service processing logic.

2\. Click **Project Quality Assessment** on the **Project Management** page to check the project quality.

**Positive example**: none

**Negative example**:

1.  Invalid service logic. The system CPU resources are consumed by infinite loop or invalid logic.
2.  Invalid memory operations. Excessive memory resources are requested, consuming system memory resources.
3.  Invalid file operations. For example, deleting files in the underlying running environment or generating junk files consumes the disk space.
4.  The script contains more than 1000 consecutive character strings (without spaces).

**Exception scenarios**: none

**Tool supported or not**: yes

**Specification name**: Security\_MaliciousOperations\_Forbid\_Python\_DaggerCommand

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: all

**Parent topic:** [[Protection Against Malicious Operations|Protection Against Malicious Operations]]