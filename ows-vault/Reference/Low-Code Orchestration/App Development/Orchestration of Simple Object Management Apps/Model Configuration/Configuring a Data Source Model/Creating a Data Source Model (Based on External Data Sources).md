---
title: "Creating a Data Source Model (Based on External Data Sources)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/datamodel_031.html"
depth: 5
---
#### Context

In the data visualization screen scenario or a scenario where a large amount of data exists, developers have to process complex existing data. By using external data sources, developers can effectively manage data in the ADC system at a low cost and develop apps based on the data.

Developers can manage data sources on the **Products and Services** > **Administration** > **Model Management** > **Model External Data Source Management** page in the runtime-state environment.

After a model consisting of external data sources is created, developers can select the automatic generation of services and pages based on the model and add, delete, modify, and query data in the external data sources.

The restrictions on using external data sources are as follows:

-   Data model archiving is not supported.
-   Indexes cannot be configured.
-   Data synchronization configuration is not supported.
-   Currently, only GaussDB, MySQL, and PostgreSQL data sources are supported.