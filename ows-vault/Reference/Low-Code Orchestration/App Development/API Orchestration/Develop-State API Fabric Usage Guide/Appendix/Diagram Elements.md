---
title: "Diagram Elements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_083.html"
depth: 5
---
#### Branch Diagram Elements

Branches connect diagram elements in a process.

Events influence the execution of a process. Usually, each event has a cause and impact.

**Table 1** Branch diagram elements   
| Name | Icon | Description |
| :-- | :-- | :-- |
| Sequence branch |  | Sequence flow. After a node using a sequence flow is accessed, the process is executed based on the sequence flow direction. A node can have one or more sequence flows. |
| Condition branch |  | Conditional flow. A process using conditional flows can be executed only when required conditions are met. A node can have one or more conditional flows. Double-click a connection line to add a determination function. |
| Default branch |  | Default flow. When no condition is met for the conditional flows on a node, the default flow is used to execute the process. A node can have only one default flow. |
| Mutually exclusive branch |  | Exclusive gateway, which is used to determine the output flow in the process (the calculation result of the output flow without any condition is true). When multiple output flows exist, only the first flow that meets the conditions is executed.
-   A conditional flow can be defined for the exclusive gateway diagram element. If the calculation result of the conditional flow is **true**, the process is executed properly.
-   Multiple conditional flows can be defined for the exclusive gateway diagram element. If the calculation results of all conditional flows are **false** and the default flow is not defined, an error is reported, and the process ends.

 |