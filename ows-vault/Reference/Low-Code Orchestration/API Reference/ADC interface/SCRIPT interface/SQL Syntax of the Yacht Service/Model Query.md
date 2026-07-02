---
title: "Model Query"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001578554144.html"
depth: 5
---
#### Modeling

A physical model is a catalog, schema, table, or column defined by the database so that users can use SQL statements to query the physical model.

**Table 1** Model creating rules   
| Catalog | Schema | Physical Model Mapping |
| :-- | :-- | :-- |
| physical-MetaOne | Name of the service type in the logical model, for example, xdr and sdr.
-   If **Service Type** is **global** or the service type does not exist, the schema name is fixed at **general**.
-   A schema whose name is **metadata** provides metadata tables corresponding to physical models. For details, see [Metadata](../nottoctopics/en-us_topic_0000001584281893.html).

 | When the physical model name is used as a table name, the mapping priority of physical models whose names are the same is as follows:

1.  The physical model on which the user does not have permission is excluded.
2.  The physical model that cannot be queried by JDBC, such as HDFS, is excluded.
3.  The physical model that is obtained from the **Products and Services** > **Data Cube** > **System Management** > **Data Source Management** > **Data Source Configuration** > **Hadoop Cluster Configuration** page and has the smallest ASCII code of the data source ID is preferred.
4.  The physical model that is obtained from the **Products and Services** > **Data Cube** > **System Management** > **Data Source Management** > **Data Source Configuration** > **Database** page and has the smallest ASCII code of the data source ID is preferred.

 |
| physical-Data source name | Database name of a physical model (the value of OWNER of metadata.tables). For details, see Metadata. | One logical schema maps only one physical schema (table creation schema). For details, see Table 2. | **Table 2** Data source mapping   
| Name | Mapping | Configuration Method |
| :-- | :-- | :-- |
| Data source | Logical data sources correspond to values in the Data Source column on the Physical Model page of Products and Services > Data Cube > Data Governance > Metadata Management > Model Management. The default name of a catalog is in the format of "physical-Data source name." | Choose Products and Services > Data Cube > System Management > Data Source Management > Data Source Configuration, click the Data Source Mapping tab, and click Create. NOTE: If the name of a physical data source and the ID of a logical data source do not match, the data source mapping is required. |
| Schema | When a logical schema and a physical schema do not match, the mapping between the logical schema and the physical schema (table creation schema) must be configured. | Choose Products and Services > Data Cube > System Management > Data Source Management > Data Source Configuration, click Hadoop Cluster Configuration or Database, and click Configure Mapping. NOTE: If the mapping between logical schemas and physical schemas is not configured for a preconfigured data source, the error 42P01 UNDEFINED\_TABLE may be reported during model query. For details about error codes, see Error Codes. |