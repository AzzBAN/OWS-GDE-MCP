---
title: "Sequence Flow Configuration Description"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_111.html"
depth: 4
---
# Sequence Flow Configuration Description

A sequence flow is used to identify the process execution direction. When a gateway is used together, you can configure conditions and default flows to implement multi-branch scenarios.

-   **Condition**: This parameter needs to be configured only for the sequence flows behind the gateway component. A process supports the following condition types: TQL condition, script condition (JUEL), and script condition (TEL). TEL is a new condition added in 2.1. JUEL and TEL on the page are adapted and displayed based on the old and new processes.
    -   Only TQL and TEL can be used by new processes. JUEL cannot be used.
    -   TQL, JUEL, and TEL can be used by historical processes.
-   **Default Process**: indicates whether the process is a default branch. Only one default process can be configured for a phase.
    -   **Exclusive Gateway**: If the sequence flow conditions of the exclusive gateway exit are not met, the default process is executed.
    -   **Inclusive Gateway**: If the sequence flow conditions of the inclusive gateway exit are not met, the default process is executed. If any of the sequence flow conditions of the inclusive gateway exit is met, the default process is not executed.

**Parent topic:** [[Process Designer Configuration Description|Process Designer Configuration Description]]