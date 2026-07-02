---
title: "Rule: Using CallScript Instead of Sub-process to Call Sub-scripts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283652.html"
depth: 6
---
# Rule: Using CallScript Instead of Sub-process to Call Sub-scripts

**Description**: Both the **CallScript** and **Subprocess** controls can call a subscript. However, when **Subprocess** calls a subscript, the called subscript and the current script are in the same scope. That is, the variable in the subscript directly overwrites the variable with the same name in the current script, resulting in unexpected results. When **CallScript** calls a subscript, variables in a subscript do not affect the values of variables with the same name in the current script.

**Check guide**: Check whether the **Subprocess** control is used in the process script.

**Tool supported or not**: no

**Specification name**: General\_RPA\_Forbidden\_Use\_Subprocess

**Severity**: major

**Parent topic:** [[Robot|Robot]]