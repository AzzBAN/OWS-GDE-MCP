---
title: "Suggestion: Handle Less Than Five Rules in Each Phase by Less Than Two Handlers or Groups"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283632.html"
depth: 6
---
# Suggestion: Handle Less Than Five Rules in Each Phase by Less Than Two Handlers or Groups

**Description**: If too many assignment rules are configured for a single phase, the execution efficiency is affected, errors may occur and cannot be easily located, making the subsequent process maintenance inconvenient. You are advised to extract and combine assignment rules based on conditions.

**Check guide**:

1.  Select a phase in the process diagram, select **Handler** from the shortcut menu or click the **Handler** text box.
    
    ![[en-us_image_0000002194367157.png]]
    
2.  On the displayed page, query the total number of rules.
    
    ![[en-us_image_0000002159069694.png]]
    

**Positive example**:

1\. The number of assignment rules configured for a single phase in the process is less than the recommended value.

2\. The number of handlers configured for a single phase in the process is less than the recommended value.

**Negative example**:

1\. The number of assignment rules configured for a single phase in the process is greater than the recommended value.

2\. The number of handlers configured for a single phase in the process is greater than the recommended value.

**Tool supported or not**: no

**Specification name**: General\_Process\_Handler\_Rules\_Less\_Than\_5\_and\_Handlers\_or\_Groups\_Less\_Than\_2

**Severity**: suggestion

**Parent topic:** [[Process|Process]]