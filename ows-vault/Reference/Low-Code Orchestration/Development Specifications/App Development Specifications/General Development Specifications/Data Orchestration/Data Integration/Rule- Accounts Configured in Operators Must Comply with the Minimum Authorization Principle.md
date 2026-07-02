---
title: "Rule: Accounts Configured in Operators Must Comply with the Minimum Authorization Principle"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001603713496.html"
depth: 6
---
# Rule: Accounts Configured in Operators Must Comply with the Minimum Authorization Principle

**Specification name**: General\_DataFactory\_AIP\_Follow\_Authorized\_Minimize

**Description**: Accounts configured in the HDFS, FTPClient, SFTP, Database, CollectorReceiver(S), LdapClient, KafkaConsumer(S), KafkaProducer, WMQSender, WMQReceiver(S), SMPPClient, SNMPReceiver(S), and SSH operators must comply with the minimum authorization principle, preventing security risks such as data leakage and loss.

**Check guide**: Check whether the accounts configured in the HDFS, FTPClient, SFTP, Database, CollectorReceiver(S), LdapClient, KafkaConsumer(S), KafkaProducer, WMQSender, WMQReceiver(S), SMPPClient, SNMPReceiver(S), and SSH operators are the administrator account or accounts with excessive permission.

**Impact**: Serious data leakage may occur.

**Parent topic:** [[Data Integration|Data Integration]]