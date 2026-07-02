---
title: "Suggestion: Check Whether Document Operation Result Meets the Expectations"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001814745317.html"
depth: 6
---
# Suggestion: Check Whether Document Operation Result Meets the Expectations

**Description**: The implementation logic of the current document robot is to replace document fields with template fields. After the execution is complete, check whether the replacement is successful and whether there are fields that are not replaced. If some fields fail to be replaced, delete the data and execute the operation again.

**Check guide**: Check based on the robot script design. For example, check whether the words to be replaced exist in the new document, for example, **\[F012\]**.

**Positive example**:

-   You can search for data in an Excel file. If the returned result is not \[\], the data is found.
    
    ![[en-us_image_0000001793888569.png]]
    
-   You can obtain the Word document content by using the word.readText control, and then determine whether the keywords are in the text content to be read by using the IN statement or regular expressions.
    
    ![[en-us_image_0000001793809125.png]]
    

**Tool supported or not**: no

**Specification name**: General\_RPA\_Check\_Document\_Operation\_Result

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]