---
title: "Suggestion: Use Parameters to Manage Configuration Items in a Unified Manner During Orchestration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001590958769.html"
depth: 6
---
# Suggestion: Use Parameters to Manage Configuration Items in a Unified Manner During Orchestration

**Specification name**: Parameter\_Centralized\_Management\_For\_Configurations

**Description**: If the default values of multiple configuration items of multiple operators are the same during orchestration, you are advised to use the same parameter to manage these configuration items for easier maintenance.

**Check guide**: Check whether the default values of multiple configuration items of multiple operators are the same.

**Example**: If the file directories extracted by multiple Extract Text operators are the same and need to be changed frequently, you can set the file directory as a parameter and change the default value of this parameter for batch modification in subsequent operations.

1.  Add the file directory as a flow parameter and set the default value.
    
    ![[en-us_image_0000001744265938.png]]
    
2.  On the configuration page of the Extract Text operators, enter the directory parameter specified by the flow parameter.
    
    ![[en-us_image_0000001607727313.png]]
    

For details about how to use the parameters, see [Parameter Description](../nottoctopics/en-us_topic_0000001439663728.html).

**Parent topic:** [[Parameter Management and Usage|Parameter Management and Usage]]