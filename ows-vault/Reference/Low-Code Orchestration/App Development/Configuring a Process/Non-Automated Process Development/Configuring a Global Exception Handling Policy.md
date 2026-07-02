---
title: "Configuring a Global Exception Handling Policy"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_126.html"
depth: 4
---
#### Context

A global exception handling policy can be configured for non-automated processes. If an exception occurs in the **Service Task** or **Script Task** node in a non-automated process, you can configure a global exception handling policy, including the following options:

-   **Terminate Exception**: The process ticket of the current service task or script task is terminated unexpectedly, and the ticket status changes to **Completed**.
-   **Abort Exception**: The process ticket of the current service task or script task is stopped unexpectedly, and the ticket status changes to **Running**.
-   **Ignore Exception**: The process ticket of the current service task or script task ignores the exception and the ticket continues to be transferred.

![[note_3.0-en-us.png]]

The exception handling policy at the process node level has a higher priority than that at the global level.