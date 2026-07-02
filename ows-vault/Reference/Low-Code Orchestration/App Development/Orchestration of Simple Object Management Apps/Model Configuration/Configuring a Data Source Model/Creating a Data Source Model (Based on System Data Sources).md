---
title: "Creating a Data Source Model (Based on System Data Sources)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/datamodel_030.html"
depth: 5
---
#### Context

-   The table of a data source model is not created by ADC but by external systems or services. The table structure is not defined by ADC. Therefore, the data source model does not support index configuration.
    
-   The table location of the data source model is as follows:
    
    -   The table can be in the default data source of the tenant, but the table name must start with **t\_rt\_app\_ds\_** or **t\_rt\_mod\_ds\_**. Such models correspond to fixed table models of the historical version.
        
    -   The table can be in the data source configured by the tenant administrator but the data source cannot be the same as that configured by the system administrator. The table name is not limited. Such models correspond to data source models of the historical version.
        
-   The table data corresponding to the data source model can be directly operated in the database by external systems or services. For example, when an external system or a service directly operates the data in the database:
    
    -   If the model data cache is enabled for the model, the cached data may be inconsistent with the data in the database.
        
    -   The trigger is not triggered. In the future, the interface for triggering triggers will be opened to external systems. External systems or services need to call this interface to trigger triggers.
        
-   The table name of the data source model and the field name corresponding to the property can be specified during development.
    

-   Currently, fields of the binary type are not supported.