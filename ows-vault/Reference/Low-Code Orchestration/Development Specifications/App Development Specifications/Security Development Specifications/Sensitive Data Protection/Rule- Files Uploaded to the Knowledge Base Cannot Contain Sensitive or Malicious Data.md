---
title: "Rule: Files Uploaded to the Knowledge Base Cannot Contain Sensitive or Malicious Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002370411576.html"
depth: 5
---
# Rule: Files Uploaded to the Knowledge Base Cannot Contain Sensitive or Malicious Data

**Description**: The knowledge base may contain the following information:

1\. High-value service data (such as customer network data)

2\. Copyright data

3\. KIA (Huawei internal data)

4\. Network security sensitive data such as passwords and keys

5\. Personal data

6\. Misleading data (data related to pornography, terrorism, violence, politics, and racial discrimination)

7\. Malicious code (viruses, Trojan horses, worms, and vulnerability exploitation code)

8\. Insecure configuration

Developers need to identify, scan, and clean the preceding data before uploading the data to the knowledge base. Do not upload the preceding data to the knowledge base.

**Tool supported or not**: yes

**Note**: Currently, the tool supports the following sensitive data: Huawei employee ID, mobile phone number, fixed-line phone number, session ID, email address, ID card number, IP address, and password. Other sensitive data is to be supported in the future.

**Specification name**: Security\_Knowledge Base\_Document

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: agent orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]