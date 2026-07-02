---
title: "Suggestion: Manage Variables in a Unified Manner"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001814745269.html"
depth: 6
---
# Suggestion: Manage Variables in a Unified Manner

**Description**: The default variables during script running should be maintained in a unified manner. For example, the default variables are put in global variables or global parameters. Do not hardcode these variables in scripts.

**Check guide**: Global variables are invisible to external systems and are used to define parameters that do not change. The sensitive information entered by users must be of the sensitive type. Create sensitive information that does not change frequently on the parameter configuration page of RPA Orchestrator and reference them during task creation. In addition, parameters are generated in the output of some controls for subsequent call, and variables are defined for the tooltip control.

**Positive example**: The variables in the current script are called in the format of "@_{Variable name}_". Traverse all variables that meet the call mode and compare them with the variables defined in the preceding mode. If there are variables that are not defined in the preceding range, check whether the variables are directly referenced in the script.

![[en-us_image_0000001793881045.png]]

**Tool supported or not**: no

**Specification name**: General\_RPA\_Unified\_Variable\_Management

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]