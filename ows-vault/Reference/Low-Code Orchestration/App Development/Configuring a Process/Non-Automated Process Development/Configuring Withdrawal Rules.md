---
title: "Configuring Withdrawal Rules"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_129.html"
depth: 4
---
#### Context

After withdrawal rules are configured, the withdrawal operation has the following restrictions by default:

-   Only the ticket creator can withdraw a ticket to the ticket creation phase. After the withdrawal, the current handler of the task is the ticket creator.
-   If a ticket has been withdrawn once, it cannot be withdrawn again after being submitted again.
-   Tickets that have been approved cannot be withdrawn.
-   Tickets cannot be withdrawn if an automatic node such as service node exist after the creation phase and tickets are transferred.
-   If the approval phase after the ticket creation phase contain multiple instances and some tasks have been approved in the approval phase, the ticket cannot be withdrawn.
-   Historical data is retained after the withdrawal, and the withdrawal operation is recorded in work logs.
-   After a ticket is withdrawn, the SLA/OLA calculation continues. If the ticket is submitted again, the SLA/OLA recalculation is not automatically started.