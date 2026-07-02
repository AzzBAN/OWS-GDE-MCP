---
title: "Rule: Exception Messages Returned by APIs Cannot Be Directly Recorded and Only General Error Messages Can Be Recorded"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643481.html"
depth: 5
---
# Rule: Exception Messages Returned by APIs Cannot Be Directly Recorded and Only General Error Messages Can Be Recorded

**Description**: The scope of sensitive data should be determined based on application scenarios and product threat analysis results. Typical sensitive data includes passwords, bank accounts, personal information, communication records, and keys. If sensitive data is not processed during exception transmission, improper information disclosure always occurs, which may result in further attacks by the attackers. Attackers can construct malicious input parameters to discover the internal data structure and execution logic of apps. Data may be improperly disclosed through either the text messages in exceptions or the types of exceptions.

**Check guide**: Check whether the exception information returned by the interface contains unnecessary information, such as the passwords, bank accounts, personal information, communication records, keys, container and version information, and database and version information. Check whether the exception information returned by the interface is directly recorded and whether the exception description that may contain sensitive data is exposed to the frontend.

**Positive example**:

var logger = JsLogger.logger();
var bankAccount = readBankAccount();
try{
abc(bankAccount);
}catch(err){
logger.log("the input is not correct !");
}

Only general error messages are displayed.

**Negative example**:

var logger = JsLogger.logger();
var bankAccount = readBankAccount();
try{
abc(bankAccount);
}catch(err){
logger.log(err);
}

All exception information is recorded. However, the running environment does not allow such information.

**Tool supported or not**: yes

**Specification name**: Security\_Exception\_OnlyPrintNecessary

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: all

**Parent topic:** [[Exception Handling|Exception Handling]]