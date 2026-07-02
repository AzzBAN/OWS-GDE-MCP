---
title: "Rule: A Log Interface Cannot Be Frequently Called to Write Information or Large Objects"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123756.html"
depth: 5
---
# Rule: A Log Interface Cannot Be Frequently Called to Write Information or Large Objects

**Description**: If the log API in a frequently executed statement is called to write logs or write large objects, the disk space may be exhausted.

**Check guide**:

1.  Check whether **console.log** is called in the loop statement to write logs. If the interface does not need to be called, do not call the log interface in the loop statement to write logs. Only necessary information is recorded.
2.  Do not record logs of large objects, such as messages and customized complex objects. Record only logs that are clear and facilitate locating.

**Involved scenarios**: Service script compiled using JavaScript, Python, and Ruby.

**Negative JS example**:

for(i=0;i<10000000;i++) { 
    console.error("I am " + i); 
}

**Positive example**:

for(i=0;i<10000000;i++) { 
    if(i == 10000000){ 
      console.info("All things done."); 
     } 
}

In the negative example, useless information is recorded and a large amount of information is recorded in the loop body. In the positive example, logs are recorded only once when an exception that requires log recording occurs.

**Tool supported or not**: yes

**Note**: Only JavaScript script check is supported. Python or Ruby script check is not supported.

**Specification name**: Security\_DOS\_Script\_PrintHugeObject

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: all

**Parent topic:** [[Anti-DoS|Anti-DoS]]