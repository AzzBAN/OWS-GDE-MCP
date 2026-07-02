---
title: "Basic Concepts of a Process"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_074.html"
depth: 4
---
# Basic Concepts of a Process

Before using a process, you are advised to understand the basic concepts of the process.

A process is a set of business operation rules and mechanisms designed under specific conditions to create value for customers or achieve business objectives. On a graphical process orchestration engine. In addition to traditional user interaction processes, API processes orchestrated based on app services, service catalogs, and JavaScript nodes are supported. You can quickly develop and deploy processes through online orchestration.

ADC supports the following processes:

-   Non-automated process: applies to various manual tasks. Forms are used as data interaction interfaces between users and the system.
-   Automated process: applies to automatic tasks. No form is required as human-machine interaction interfaces.

The ADC process consists of the following parts:

-   Diagram: defines the logical sequence to be followed and the organizations or individuals involved in completing a business in a diagram
-   Form: includes PC forms, mobile forms, and GDELink forms that support data interaction between users and the system. Users can enter information and perform operations on the designed page.
-   Rule: refers to rules and mechanisms that support the effective operation of the process.

![[note_3.0-en-us.png]]

To better be compatible with historical assets, you can import the SEP process package orchestrated in ADC 1.0 to 2.0 through the legacy assets.

-   When importing historical assets, you can import customized service task, intermediate events, and nodes that call sub-processes.
-   Historical asset process packages can be converted to the new asset package format when being exported in 2.0.
-   The properties (class fields) of SEP customized components can be modified online.
-   The properties of the time event component can be modified.
-   The properties of the component that calls a sub-process can be modified.

**Parent topic:** [[Process Development Overview|Process Development Overview]]