---
title: "Function Overview"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_054.html"
depth: 5
---
# Function Overview

A process supports the following condition types: TQL condition, Script condition (JUEL), and Script Condition (TEL). TEL is a new condition added in 2.1.

![[note_3.0-en-us.png]]

-   Only TQL and TEL can be used by new processes.
-   TQL, JUEL, and TEL can be used by historical processes.

During process configuration, condition expressions are used in the following scenarios:

-   Configure the input parameters of **Start Event**.
-   Configure the output parameters of **End Event**.
-   Configure the skip expression of **User Task**.
-   Configure the conditions of **Sequence Flow**.
    
    In the process diagram, components of **Event**, **Activity**, and **Gateway** can be connected to one or multiple **Sequence Flow**. After the flow conditions are configured for **Sequence Flow**, the process is executed based on **Sequence Flow** that meets conditions.
    
-   Configure **API Input**, **API Output**, and **Fault Handling Policy** (**Customize Exception**) of **Service Task**.
-   Configure the input and output parameters of **Call Subprocess**.

The following topics mainly describe how to use the Script condition expressions.

**Parent topic:** [[Guidance for the Conditional Expressions|Guidance for the Conditional Expressions]]