---
title: "Rule: Dangerous Functions Cannot Be Used When JavaScript Script Is Compiled in Develop-State API Fabric"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363625.html"
depth: 5
---
# Rule: Dangerous Functions Cannot Be Used When JavaScript Script Is Compiled in Develop-State API Fabric

**Description**: In the develop-state API Fabric, developers can customize extension capabilities through JavaScript scripts, and the following scenarios are involved: data mapping, diagram element orchestration logic, user name and password authentication, and error code mapping. The conventions are as follows:

Dangerous functions, infinite loops, and application of a large amount of memory are not allowed in JavaScript scripts.

**Check guide**: Go to the develop-state API Fabric page, check all JavaScript scripts customized by developers, and check whether a large amount of memory is applied for, whether the following functions are used: System.exit in JDK, quit, and exit.

**Tool supported or not**: yes

**Specification name**: Security\_DOS\_APIFabric\_Script\_Forbid\_DangerousFunctions

**Severity**: major

**Orchestration scenarios**: API orchestration - integration and openness API orchestration

**Parent topic:** [[Anti-DoS|Anti-DoS]]