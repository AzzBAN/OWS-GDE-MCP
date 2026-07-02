---
title: "Configuring the Policy for Handling Service Task Exceptions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_121.html"
depth: 5
---
#### Context

When an exception occurs in a service task, you can configure an exception handling policy including the following information:

-   **Terminate Exception**: The process instance of the current service task is terminated unexpectedly, and the ticket status changes to **Completed**.
-   **Abort Exception**: The process instance of the current service task is stopped unexpectedly, and the ticket status changes to **Running**.
-   **Ignore Exception**: The process instance of the current service task ignores the exception and the ticket continues to be transferred.
-   **Customize Exception**: custom exception. You can define a new exception handling policy based on the context of the current process instance.