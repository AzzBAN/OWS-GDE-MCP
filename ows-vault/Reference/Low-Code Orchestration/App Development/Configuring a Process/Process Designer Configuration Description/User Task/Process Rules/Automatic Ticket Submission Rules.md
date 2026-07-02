---
title: "Automatic Ticket Submission Rules"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_116.html"
depth: 6
---
#### Context

When a ticket needs to be automatically submitted in a phase, you can configure automatic ticket submission rules.

Before configuring rules, plan the required rule events and rule activities by referring to [[Rule Design|Rule Design]]. The actual scenario is subject to the actual plan.

![[note_3.0-en-us.png]]

-   Automatic ticket submission rules can be configured only when the rule event is **Subticket Updated** or **Task Started**.
-   Custom ticket submission rules are used only for ticket transfer. If there are multiple custom ticket submission rules that meet the conditions, only the custom ticket submission rule with the highest priority can be executed.