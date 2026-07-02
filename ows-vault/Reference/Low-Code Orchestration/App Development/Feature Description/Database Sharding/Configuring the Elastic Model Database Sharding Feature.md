---
title: "Configuring the Elastic Model Database Sharding Feature"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_sharding_006.html"
depth: 4
---
#### Context

After the configuration is complete based on [[Configuring a Data Source for Database Sharding (Management Zone)|Configuring a Data Source for Database Sharding (Management Zone)]] and [[Configuring Project Database Sharding (Develop State)|Configuring Project Database Sharding (Develop State)]], the basic sharding feature of data models can be implemented.

In the current service scenario, after a data model is created in the schema of database sharding, the data model needs to synchronize the elastic model data. For example, in the FM service domain, after the database sharding feature is configured, data model A created in the database sharding schema needs to be synchronized to elastic model B.

-   In the MySQL database, this feature can be used by default. No additional configuration is required.
-   In the GaussDB database, you need to modify the configuration of the corresponding data source node.

The elastic model–based database sharding feature has the following restrictions:

-   Currently, only GaussDB and MySQL databases are supported.
-   The GaussDB database sharding supports only database nodes installed using GKit as external data sources.
-   The newly connected database must communicate with the system network to which ADC is to be connected.
-   The version of the newly connected external GaussDB database must be Gauss100 OLTP 1.3.0 or later.
-   A maximum of 10 external database sources can be configured. Only the scenarios where both the master and slave databases are GaussDB or MySQL databases are supported.
-   Before you install adc-zenith-trigger on the server where the external GaussDB database is located, install third-party components, for example, ADC-rhm and adc-mgt-init jre1.8 or later.