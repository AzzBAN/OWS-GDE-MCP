---
title: "Configuring Models to Automatically Generate Services and Pages"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/datamodel_006.html"
depth: 5
---
#### Context

Services and pages can be automatically generated based on models. After the generation, if the model is updated, the updates will not be automatically synchronized to the generated services and pages. You need to manually adjust the pages and services or automatically generate the pages and services again.

If you have decided to generate services and pages during the model creation, skip this section when the model is not modified.

Services and pages can be generated in either of the following modes:

-   Generating services automatically: The services, pages, and mobile pages can be automatically generated. To add, delete, modify, or query data on the page, you can call the corresponding service.
    
    The services have the logic orchestration capability and can translate and convert input and output parameters. For details about the services, see [[Configuring Services|Configuring Services]].
    
    When a service is called on the page, the parameters transferred from the page are used as the input parameters for data addition, deletion, modification, or query.
    
-   Using built-in model services: Only pages are generated. Data operations are not performed using the independent addition, deletion, modification, or query service but by calling the built-in addition, deletion, modification, or query service of a model on the WebUI.
    
    When built-in model services are used, complex processing, such as translation and conversion of input and output parameters, is not required when you add, delete, modify, or query data in the model.
    
    When a built-in model service is called on the page, the parameters transferred from the page are used as the input parameters of the built-in service for data addition, deletion, modification, or query.
    
    [Table 1](#EN-US_TOPIC_0000001093075692__table1928584635310) lists the core differences between the two modes.
    
    **Table 1** Differences   
    | Difference Analysis Item | Service | Built-in Model Service |
    | :-- | :-- | :-- |
    | Acceptable to data orchestration and modification | For automatically generated services, the input and output parameters and logic of the services can be adjusted and modified. | For built-in model services, the addition, deletion, modification, or query service cannot be modified again. |
    | Address format | Format: /adc-service/rest/v1/services/{project}/{module}/{service} Example: /adc-service/rest/v1/services/equipment/equipment/equipment\_baseinfo\_get\_list | Format: /adc-model/web/rest/v1/model-services/{project}/{module}/{model}/{operation} Example: /adc-model/web/rest/v1/model-services/equipment/equipment/equipment\_baseinfo/get\_list |
    | Microservice that is depended | adc-service | adc-model |
    | Permission control | You can set the permission control mode and permission items during automatic service generation. The permission items can be modified one by one in the service. | You can set the frontend access permission items during model configuration. |