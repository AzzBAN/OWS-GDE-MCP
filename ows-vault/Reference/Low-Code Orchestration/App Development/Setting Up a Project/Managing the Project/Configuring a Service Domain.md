---
title: "Configuring a Service Domain"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_051.html"
depth: 4
---
#### Context

Service domains to which projects belong are used in the following scenarios:

-   Database sharding. The service database is matched based on the configured service domain.
    
    For example, if **Service Domain** is set to **FM** and a secondary database is configured for the FM service domain, the database instance of the project can be created in the secondary database to optimize the performance of the service domain.
    
-   Fine-grained public API control. If an API is set to be public, a public domain whitelist is also set. Only domains in the whitelist can access the API.
    
    For example, if **Service Domain** is set to **CEAE** and the public domain is CEAE for public services of asset domain A, the project can call the corresponding public services.
    
    For details about how to configure a whitelist for a public API, see [[Creating a Service (Blank Template)|Table 1]].