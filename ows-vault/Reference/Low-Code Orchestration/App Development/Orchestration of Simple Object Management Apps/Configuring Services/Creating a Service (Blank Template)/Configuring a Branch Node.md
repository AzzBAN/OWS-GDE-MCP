---
title: "Configuring a Branch Node"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_050.html"
depth: 5
---
#### Context

A branch node is a condition branch. By configuring a condition branch, you can perform different operations under different conditions. For example, when service A is successfully executed, event B is triggered; when service A fails to be executed, event C is triggered.

In a branch node, the branch node carries the parameter values of the previous node to the next node. If parameter **a** exists in front of a branch node, you can use **$.a** to obtain this parameter after the branch node.