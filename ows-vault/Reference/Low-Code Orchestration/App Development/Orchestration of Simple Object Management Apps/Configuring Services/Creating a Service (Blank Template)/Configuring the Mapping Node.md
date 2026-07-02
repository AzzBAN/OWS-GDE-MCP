---
title: "Configuring the Mapping Node"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_052.html"
depth: 5
---
#### Context

Parameter processing node, which does not contain any operations. It is used only for mapping a parameter, processing the output of the previous node, and sending the processing result to the next node.

For example, interface A needs to be called to query the **aa** field, and interface B needs to be called to use the queried field **aa** as the input parameter of interface B.

For example, if the input and output parameters of the last two operations do not match, you can add a mapping node to process parameters.