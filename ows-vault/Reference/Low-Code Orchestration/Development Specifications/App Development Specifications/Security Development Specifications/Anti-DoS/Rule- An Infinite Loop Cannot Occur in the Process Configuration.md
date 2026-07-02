---
title: "Rule: An Infinite Loop Cannot Occur in the Process Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963856.html"
depth: 5
---
# Rule: An Infinite Loop Cannot Occur in the Process Configuration

**Description**: In scenarios such as automatic processing rules or service calling in workflow configuration, cyclic dependency or repeated calling may occur. As a result, an infinite loop occurs, a large number of system resources are occupied, and the system may even be unavailable.

**Check guide**:

1.  Avoid cyclical calling of subprocesses.
2.  During API service calling, do not call the process used for releasing a process to avoid infinite loops.
3.  When the gateway is used to implement cyclic execution, check whether there are loop ending conditions to avoid infinite loops.
4.  Avoid infinite loops during automatic processing of process rules.
5.  Configure data rules on the model used by the process to avoid infinite loops. You are advised not to use model data rules.

**Negative example**: The process is automatically rejected to the previous phase and is submitted to the current phase again.

**Positive example**: As shown in the following figure, when the loopback logic is configured for mutually exclusive gateways, there must be exit conditions to prevent infinite loops during process execution.

![[en-us_image_0000001735314129.png]]

**Tool supported or not**: yes

**Specification name**: Security\_DOS\_BPM\_ServiceConfig\_ProhibitInfiniteLoop

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: process orchestration

**Parent topic:** [[Anti-DoS|Anti-DoS]]