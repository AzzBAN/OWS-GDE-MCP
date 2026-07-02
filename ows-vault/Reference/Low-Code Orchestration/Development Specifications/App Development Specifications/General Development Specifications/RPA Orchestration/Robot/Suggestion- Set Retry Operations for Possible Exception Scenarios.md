---
title: "Suggestion: Set Retry Operations for Possible Exception Scenarios"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001814745301.html"
depth: 6
---
# Suggestion: Set Retry Operations for Possible Exception Scenarios

**Description**: During the script execution, if the operation result of an object does not meet the expectations, retry the script for several times. If the operation is successful after several retries, no error is reported. Otherwise, an error is reported.

**Check guide**: none

**Positive example**:

-   The for loop is used to set the number of retry times, which is generally used in a metering loop.
    
    ![[en-us_image_0000001746847630.png]]
    
-   In the Try-Catch statement, the error retry mode of Try is set to **True** and the number of retry times is set. After the Catch part processes the exception, the statement is returned to the Try part because the error retry mode is **True** by default (which is an incorrect mode) and is executed from the location of the failed action until no error occurs or the number of retry times becomes 0.
    
    ![[en-us_image_0000001747006834.png]]
    
-   The While or Do-While cyclic statement applies to the scenarios where the number of retry times is not fixed, such as verification code input scenarios.
    
    ![[en-us_image_0000001747006982.png]]
    
-   Set the control timeout interval. The current control will be retried within the timeout interval.
    
    ![[en-us_image_0000001793806877.png]]
    
-   When using loops, pay attention to the nesting depth. The following figure shows the standards.
    
    ![[en-us_image_0000001747007018.png]]
    

**Tool supported or not**: no

**Specification name**: General\_RPA\_Retry\_In\_Abnormal\_Scenarios

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]