---
title: "Suggestion: Use a Data Job Scheduling Control Flow Instead of a Batch Processing Control Flow or a Lightweight ETL Control Flow"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001236784721.html"
depth: 6
---
# Suggestion: Use a Data Job Scheduling Control Flow Instead of a Batch Processing Control Flow or a Lightweight ETL Control Flow

**Specification name**: General\_DataFactory\_Unified\_Schedule\_Control\_By\_Unified\_Schedule

**Description**: You are advised to use a general computing task of Data Job Schedule as the control flow to control the scheduling source by flow and control the scheduling sequence and relationship among flows.

-   Batch processing control flows and lightweight ETL control flows can control the scheduling of only one type of data flows, while Data Job Schedule can control the scheduling of different types of data flows.
-   Batch processing control flows and lightweight ETL control flows can schedule only data flows and control flows in the current app (project), while Data Job Schedule can schedule them across projects through the Dependency and Trigger operators.

**Check guide**: Check whether a data job scheduling flow is used to reference a batch processing flow or a lightweight ETL flow.

**Positive example**: The general\_schedule flow of Data Job Schedule uses the **Control Flow** parameter of the Batch or LightETL operator to reference the batch processing or lightweight ETL flow to be scheduled.

**Parent topic:** [[Data Job Schedule|Data Job Schedule]]