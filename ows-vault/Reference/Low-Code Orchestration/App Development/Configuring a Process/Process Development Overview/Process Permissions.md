---
title: "Process Permissions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_052.html"
depth: 4
---
# Process Permissions

After a process is created, ticket permission items are automatically created. Permission elements are deployed and installed together with the project package in the runtime state environment.

All processes under the default role are bound to the default operation permission. For details, see [Table 1](#EN-US_TOPIC_0000001139919059__te70ab13540724366912f9da3da2aa145). Each role in the system has different permissions. If a function or role is added, the administrator needs to assign operation permissions and menu permissions to the role.

**Table 1** Default roles in processes   
| Role | Default Permission | Description |
| :-- | :-- | :-- |
| TicketCreator | Cancels tickets, displays process status diagrams, urges tickets, views ticket operation details, copies tickets, supplements suspension and resumption records, associates tickets, deletes ticket association relationships, queries ticket association relationships, handles associated tickets in batches, re-dispatches tickets, creates work logs, updates work logs, and queries the process list, attachments, rule logs, SLA details, and work logs. | Role preconfigured in the process orchestration service. This role is used in process orchestration. NOTE: You can log in to the Role Management page in the runtime-state environment as the current tenant administrator to customize the permission items. |
| TicketProcessor | Cancels tickets, displays process status diagrams, escalates tickets, handles tickets, creates sub-tickets, associates tickets, transfers tickets, urges tickets, modifies tickets, suspends tickets, resumes tickets, exempts tickets, views ticket operation details, queries attachments, views SLA details, re-assigns tickets, creates work logs, queries work logs, and updates work logs. | **Parent topic:** [[Process Development Overview|Process Development Overview]]