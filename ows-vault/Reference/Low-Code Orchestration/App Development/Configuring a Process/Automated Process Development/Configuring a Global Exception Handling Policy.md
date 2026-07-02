---
title: "Configuring a Global Exception Handling Policy"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_122.html"
depth: 4
---
#### Context

-   A global exception handling policy can be configured for automated processes. The global exception handling policy supports only **Terminate Exception**.

-   The global exception handling policy takes effect in the following scenarios:
    -   Service call fails on the **Service Task** node.
    -   After the policy is executed, the wakeup API carries exception information. (Currently, only the private API carries exception information during wakeup.)
    -   An exception occurs on the **Script Task** node.
    -   The operations cannot be continued because sequence flow conditions cannot be matched.
    -   The operations cannot be continued because conditions of an exclusive gateway cannot be matched.

![[note_3.0-en-us.png]]

The exception handling policy at the process node level has a higher priority than that at the global level.