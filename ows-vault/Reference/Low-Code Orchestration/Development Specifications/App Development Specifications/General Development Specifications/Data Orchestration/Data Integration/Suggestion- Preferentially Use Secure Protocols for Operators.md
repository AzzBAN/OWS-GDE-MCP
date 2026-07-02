---
title: "Suggestion: Preferentially Use Secure Protocols for Operators"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001653992957.html"
depth: 6
---
# Suggestion: Preferentially Use Secure Protocols for Operators

**Specification name**: General\_DataFactory\_AIP\_Prioritize\_Use\_Security\_Protocols

**Description**: For the HttpListener(S), HttpRequest, SocketsListener(S), SocketsSender, KafkaConsumer(S), KafkaProducer, WMQSender, WMQReceiver(S), LdapClient, SNMPReceiver(S), SFTP, and FTPClient operators, preferentially use a secure protocol or a secure algorithm of the protocol to avoid security risks during data transmission. For details, see the risk prompt in the operator.

**Check guide**: Check whether an insecure protocol is used for the HttpListener(S), HttpRequest, SocketsListener(S), SocketsSender, KafkaConsumer(S), KafkaProducer, WMQSender, WMQReceiver(S), LdapClient, SNMPReceiver(S), SFTP, or FTPClient operator in the app.

**Positive example**: An insecure protocol, such as HTTP, FTP, or LDAP, is used in the operator. You are advised to replace it with a secure protocol.

**Impact**: Serious data leakage may occur during app running.

**Parent topic:** [[Data Integration|Data Integration]]