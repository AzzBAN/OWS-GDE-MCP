---
title: "Configuring a Multi-Node Service"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_049.html"
depth: 5
---
#### Context

When orchestrating services on multiple nodes, pay attention to the different parameter settings, that is, context parameters. **$** is equivalent to a JSON object.

-   **$xxx** is the parameter value of the context variable.
-   **$.xxx** is the result of the previous node.
-   **$$.stepName.xxx** is the variable whose value has been obtained across nodes. In this scenario, you are advised to use the **assign** node to define global variables.