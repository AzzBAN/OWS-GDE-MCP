---
title: "Creating a Service (Based on a Preset Template)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_042.html"
depth: 4
children: ["Creating a Service (Create Template)", "Creating a Service (Get List Template)"]
---
# Creating a Service (Based on a Preset Template)

When you use a template to create a service, the system automatically generates corresponding operation nodes based on the selected template type and imports the model data to the service parameters based on the associated model.

**Table 1** Template types  
| Template Name | Template Description |
| :-- | :-- |
| Create | Service template for creating a model instance. The Create model operation node is automatically added, and fields of the associated model are used as the input and output parameters of the service. |
| Update | Service template for updating a model instance. The Update model operation node is automatically added, and fields of the associated model are used as the input and output parameters of the service. |
| Delete | Service template for deleting a model instance. The Delete operation node is automatically added, and the primary key and ID of the associated model are used as the input parameters for query. The deletion result is provided. |
| Get | Service template for querying a single data record. The Get operation node is automatically added, and the primary key and ID of the associated model are used as the input parameters for query. The model instance is used as the output. |
| Get List | Service template for querying the list. The GetList operation node is automatically added. The start, limit, sort, and active fields and model fields are used as the input parameters, and the start, limit, and total fields and model instance are used as the output parameters. There can be multiple model instances. |
| Batch Create | Service template for creating model instances in batches. The BatchCreate model operation node is automatically added. |
| Batch Update | Service template for updating model instances in batches. The BatchUpdate model operation node is automatically added. |
| Batch Delete | Service template for deleting model instances in batches. The BatchDelete model operation node is automatically added. |
| Batch Upsert | Service template for adding model instances in batches. The Batch Upsert model operation node is automatically added. |
| TQL Query | Service template for querying data using TQL. The TQL Query node is automatically added. The data query TQL statements are automatically generated based on the selected model. | -   **[[Creating a Service (Create Template)|Creating a Service (Create Template)]]**  
    The **Create** template is used to configure the service used for creating data. When you use the template to create a service, the system automatically imports model data to the service parameters based on the associated model.
-   **[[Creating a Service (Get List Template)|Creating a Service (Get List Template)]]**  
    The **Get List** template is used to configure the service used for querying the list. When you use the template to create a service, the system automatically imports model data to the service parameters based on the associated model.

**Parent topic:** [[Configuring Services|Configuring Services]]

## Sub-topics

- [[Creating a Service (Create Template)]]
- [[Creating a Service (Get List Template)]]
