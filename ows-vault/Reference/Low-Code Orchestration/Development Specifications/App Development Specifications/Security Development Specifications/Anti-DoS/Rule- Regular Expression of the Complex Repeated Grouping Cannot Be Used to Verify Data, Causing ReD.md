---
title: "Rule: Regular Expression of the Complex Repeated Grouping Cannot Be Used to Verify Data, Causing ReDoS Attacks"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523517.html"
depth: 5
---
# Rule: Regular Expression of the Complex Repeated Grouping Cannot Be Used to Verify Data, Causing ReDoS Attacks

**Description**: The Regular expression Denial of Service (ReDoS) is a Denial of Service attack. If developers use regular expressions to verify the validity of data entered by users, and the regular expressions have defects or are not precise, attackers can construct special character strings to consume a large number of system resources on the server, causing service interruption or termination on the server.

Do not provide the function of executing regular expressions using untrusted frontend input. Do not use regular expressions that may cause ReDoS attacks in scripts and command parsing expressions.

**Check guide**:

SDL Regex Fuzzer is a free tool released by Microsoft to help test personnel check whether the regular expression in the program has the ReDoS vulnerability. Users need to sort out the regular expressions in the code and use the tool to check the regular expression. If the check result "Passed successfully" is displayed, the current expression is normal.

**Positive example**:

var longReg = new RegExp("^-?(1\[0-7\]\[0-9\]|\[1-9\]?\\\\d{1})(\\\\.{1}\\\\d{1,15})?$|-?180(\\\\.{1}0{1,15})?$"); if(longReg.exec(fieldValue)){ return new ValidateResult(); }

**Negative example**:

var longReg = new RegExp("^(https:\\/\\/\[\\w\\-\_\]+(\\.\[\\w\\-\_\]+)+(\[\\w\\-\\.,@?^=%&:/~\\+#\]\*\[\\w\\-\\@?^=%&/~\\+#\])?){1,100}$"); if(longReg.exec(fieldValue)){ return new ValidateResult(); }

**Tool supported or not**: yes

**Specification name**: Security\_DOS\_ShouldCheckRedos

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: all

**Parent topic:** [[Anti-DoS|Anti-DoS]]