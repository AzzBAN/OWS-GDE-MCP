---
title: "Rule: Do Not Save Sensitive Data Such as User Names and Passwords of the Production System in the RPA Process Script"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404131097.html"
depth: 5
---
# Rule: Do Not Save Sensitive Data Such as User Names and Passwords of the Production System in the RPA Process Script

Do not save any sensitive data such as user names and passwords of the production system in RPA robot assets.

**Description**: When a robot operates the service system, information such as the IP address, account, and password of the target system will inevitably be involved. Do not store sensitive data of the production system in plaintext in the parameter or variable template of RPA Studio.

Sensitive data needs to be extracted as sensitive parameters and variables, which need to be manually entered by users during task creation.

**Check guide**: Check the main script, parameters, and variables of the asset of RPA Studio to ensure that no sensitive data such as accounts and passwords is contained.

**Positive example**: Use external parameters for definition. Callers provide related data during program execution.

**Negative example**: When the database.connect control is used to connect to the database, the IP address, port number, account, and password of the target system are saved in the process asset.

**Tool supported or not**: no

**Specification name**: General\_RPA\_Forbidden\_Keep\_Sensitive\_Info\_in\_Project

**Severity**: major

**Orchestration scenario**: RPA orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]