---
title: "Openness Policies"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643305.html"
depth: 4
---
# Openness Policies

The following table lists the openness policies for the orchestration capability opened by GDE. Different asset developers need to pay attention to different policies.

  
| Policy Orchestration Capability | Ecosystem openness: provides basic low-code orchestration and development capabilities, clear openness boundaries, and mature technical control mechanisms, maintains the long-term compatibility, opens to ecosystem developers, and supports customer development through commercial sales. | Restricted openness: is the new orchestration development feature. Because the API design/technical mechanism may evolve and have compatibility risks, this feature is defined as a preview capability that can be compatible with as much as possible. It will be fully open after it becomes mature. |
| :-- | :-- | :-- |
| General Job Orchestration (model, service, trigger, and others) | 
-   No Code

Graphical orchestration CSE REST API Web REST API

-   Low Code

TQL (data query language) TEL (expression language) Service JS API | -   Pro Code

FaaS Python SDK |
| UI Orchestration: (page, mobile page, cards, menu, and i18n) | -   No Code

Graphical orchestration CSE REST API

-   Low Code

Web UI JS API (component/framework) Mobile UI JS API (component/framework) | -   Pro Code

Web UI Component Plugin Web UI Page Plugin Mobile UI Component Plugin Mobile UI Page Plugin Mobile Native SDK Mobile Native Plugin Web UI CSS API (restricted) Mobile UI CSS API (restricted) |
| Business Process | -   No Code

Graphical orchestration CSE REST API Web REST API

-   Low Code

BPM JS API BPM JUEL API | N/A |
| MCP | -   No Code

Graphical orchestration CSE REST API Open REST API

-   Low Code

MCP Python API | N/A |
| RPA Orchestration | -   No Code

Graphical orchestration

-   Low Code

RPA Python API (expression and code snippet) | -   Pro Code

RPA Action Plugin |
| API Fabric | -   No Code

Graphical orchestration CSE REST API

-   Low Code

Back-end low-code JS | N/A |
| Data Orchestration | -   No Code

Operator dragging, connection, and property configuration Operator expression editing

-   Low Code

Batch processing: using the Extract JDBC, Extract Hive, Extract Oracle, Extract Spark Sql, and Extract Impala operators Stream processing: using the Extract/Load GaussDB and Extract/Load Carbon operators | -   Pro Code

Data job scheduling: using the Inject(Stream) and External Engine operators Control flow: using the External Program, User-Defined Node, Stored Procedure, SQL Executor, and Hadoop SQL Executor operators Data flow: using the SQL Inject operator Stream processing: using the Inject and Extract/Load Custom operators AIP: using the script, SSH, and database operators DBUS: using the script operators Custom functions Custom programs Custom operators | **Parent topic:** [[Overview|Overview]]