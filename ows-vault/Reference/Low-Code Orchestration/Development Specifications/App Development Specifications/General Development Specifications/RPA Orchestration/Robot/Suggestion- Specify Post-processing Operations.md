---
title: "Suggestion: Specify Post-processing Operations"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001767985428.html"
depth: 6
---
# Suggestion: Specify Post-processing Operations

**Description**: Post-processing operations refers to the operations that are executed (no matter whether the script execution result is successful or not) to clear the intermediate data during script running and ensure that the script can be executed repeatedly. You need to check whether the robot script contains specific post-processing operations.

**Check guide**: For example, close the browser, close desktop applications, and delete data. Note: If some service systems provide the temporary storage function, you need to clear the intermediate data after a script execution failure. Otherwise, the execution at the next time may fail.

**Positive example**:

-   If the post-processing operations of the normal process are different from those of the abnormal process, the Try-Catch statements can be used. The post-operations are added to both the Try and Catch parts.
    
    ![[en-us_image_0000001746840214.png]]
    
-   If the post-processing operations of the normal process are the same as those of the abnormal process, the Try-Catch-Finally statements can be used. The common post-processing operations are stored in the Finally part, which will be executed no matter whether the script is executed successfully.
    
    ![[en-us_image_0000001793799349.png]]
    

**Tool supported or not**: no

**Specification name**: General\_RPA\_Use\_Less\_Custom\_Command

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]