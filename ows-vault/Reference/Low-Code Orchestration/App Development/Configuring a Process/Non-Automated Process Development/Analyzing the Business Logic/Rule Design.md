---
title: "Rule Design"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_studio_guide_workflow_0013.html"
depth: 5
---
#### Event

**Table 1** Rule event description   
| Rule Event | Whether the Event Is Related to the Process Phase | Event Trigger Condition |
| :-- | :-- | :-- |
| Ticket Deleted | Irrelevant to process phases. This event can be selected when Process Phase is set to All. | This event is triggered when a ticket is deleted. |
| Ticket Completed | This event is triggered when a ticket is handled. |
| Ticket Canceled | This event is triggered when a ticket is canceled. |
| Ticket Modified | This event is triggered when a ticket is modified. |
| Ticket Participant | This event is triggered when a ticket handler is modified. |
| Ticket Recalled | This event is triggered when a ticket is withdrawn. |
| Ticket Resume | This event is triggered when an SLA resumes a ticket. |
| Ticket Suspend | This event is triggered when an SLA suspends a ticket. |
| Before Task Completed | Relevant to process phases. This event can be selected when a specific process phase is selected. | This event is triggered before a task is handled. |
| Subticket Updated | This event is triggered when a sub-ticket is updated. |
| Task Completed | This event is triggered when a task is handled. |
| Task Reassigned | This event is triggered when a task needs to be reassigned. |
| Task Started | This event is triggered after a task starts. |
| Task Transferred | This event is triggered when a task is transferred. |