---
title: "Rule: Files Uploaded to Notebook Cannot Carry Malicious or Low-Quality Code or Binary Programs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804208.html"
depth: 5
---
# Rule: Files Uploaded to Notebook Cannot Carry Malicious or Low-Quality Code or Binary Programs

**Description**: By default, the system supports the following file formats: .py, .txt, .xml, .json, .yaml, .ipynb, .csv, and .ini. Ensure that the uploaded files to be uploaded do not incur security risks, such as viruses or Trojan horses.

**Check guide**: Check the file type, ensure that the file format is supported by the system, and upload the file.

**Negative example**:

![[en-us_image_0000001166872977.png]]

**Exception scenarios**: If you want to upload a file not in the default format, contact the administrator to customize the file format.

**Tool supported or not**: yes

**Specification name**: Security\_Others\_Notebook\_Forbid\_MaliciousLow-qualityCode

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenarios**: AI orchestration - integration and openness API orchestration

**Parent topic:** [[Others|Others]]