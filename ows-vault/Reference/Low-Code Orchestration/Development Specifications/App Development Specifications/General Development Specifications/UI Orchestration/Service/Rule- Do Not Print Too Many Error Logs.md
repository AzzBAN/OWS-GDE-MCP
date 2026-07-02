---
title: "Rule: Do Not Print Too Many Error Logs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283572.html"
depth: 6
---
# Rule: Do Not Print Too Many Error Logs

**Description**: Printing too many invalid error logs affects fault locating.

**Check guide**: Check all the places where logs are printed.

-   An error log can be generated only when an error occurs.
-   For common logs, use the information level.
-   Delete debug logs after commissioning.

Check the customized scripts of services, rules, translators, and validators of the run script type. Locate code in the scripts where console is used to generate logs. For example:

console.error("Create Entity Failed.");

**Negative example**:

var uuid = UUID.randomUUID();
console.error("debug request.uuid:"+uuid);//It is meaningless to print logs for each request.

**Tool supported or not**: no

**Specification name**: General\_Service\_Forbidden\_Abuse\_the\_Error\_Level

**Severity**: minor

**Parent topic:** [[Service|Service]]