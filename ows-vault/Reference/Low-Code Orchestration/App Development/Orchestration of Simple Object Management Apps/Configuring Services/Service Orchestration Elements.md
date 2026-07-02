---
title: "Service Orchestration Elements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_002.html"
depth: 4
---
# Service Orchestration Elements

This topic describes the orchestration elements involved in services.

The service orchestration page consists of the element area on the left, canvas area in the middle, configuration area on the right, and debugging area at the bottom.

You can click ![[en-us_image_0000001093235654.png]] in the configuration area on the right to display more parameters.

You can expand the debugging area at the bottom to debug the service.

**Table 1** Description of service information  
| Service Element | Description |
| :-- | :-- |
| Service Property | Properties, such as input parameters, output parameters, and public levels, can be configured for each service. These properties are service properties. |
| Service Node | Nodes contained in services. You can drag and drop nodes to orchestrate them. Properties can be configured for each node, such as associating models, calling APIs, and setting input and output parameters. Parameters can be transferred between service nodes. | **Table 2** Model operations  
| Orchestration Element | Element Description |
| :-- | :-- |
| Create | The Create operation is used to create data of specified models. After you configure the mapping between service input parameters and model data, the system can create model data using the input parameters. |
| Update | The Update operation is used to update data of specified models. After you configure the mapping between service input parameters and model data, the system can find the corresponding existing model data and update the model data. |
| Delete | The Delete operation is used to delete the corresponding model data based on the input primary key. |
| Supplement | The system checks whether the entered data exists. If no, the system creates the data. If yes, the system updates the data. |
| Get | The Get operation is used to query a unique model data record based on input parameter conditions and return the data. |
| GetList | The GetList operation is used to query model data based on input parameter conditions and return all model data that meets the conditions. |
| BatchCreate | The BatchCreate operation is used to create data in batches. |
| BatchUpdate | The BatchUpdate operation is used to update data in batches. That is, calling a service once can change multiple model data records to the same value in a unified manner. |
| BatchDelete | The BatchDelete operation is used to delete data in batches. That is, calling a service once can delete multiple data records at a time. |
| Batch Supplement | The Batch Supplement operation is provided for data provided in batches. If a record does not exist in the data table, the operation inserts the record. If the record exists in the data table, the operation updates the record. |
| TQLQuery | The TQLQuery operation provides a service for querying complete TQL configurations so that you can configure complex reports or query operations. | **Table 3** Common Operations  
| Orchestration Element | Element Description |
| :-- | :-- |
| ServiceInvoke | Call other APIs. Specifically, you can configure the mapping between input parameters of the current service and those of the called service to call another service, including translating or validating some fields. |
| RunScript | The RunScript operation is used when a single service cannot meet requirements. For example, when a submit button on a page applies to two models, or when the operation execution logic is complex, you can configure services using RunScript. |
| FireEvent | The FireEvent operation provides the function of triggering events. You can configure events and decision-making rules to complete a series of actions after an event is triggered. |
| BatchOperation | The BatchOperation operation provides the function of performing operations in batches on a service. |
| Mapping | Parameter processing node, which does not contain any operations and is used only for parameter mapping. For example, if the input and output parameters of the last two operations do not match, you can add a mapping node to process parameters. |
| assign | The assign operation is used to define a global context variable and assigns a value to the variable. | **Table 4** Logical Node  
| Orchestration Element | Element Description |
| :-- | :-- |
| Switch | Condition branch. By configuring a condition branch, you can perform different operations under different conditions. For example, when service A is successfully executed, event B is triggered; when service A fails to be executed, event C is triggered. |
| ErrorInput | Exception handling start node, which is a service-level exception handling entrance. A service can have only one exception handling start node. |
| Output | End node | **Table 5** Platform services  
| Orchestration Element | Element Description |
| :-- | :-- |
| DataService Query | Developers can orchestrate SQL statements to query data services. In fact, the query is implemented by enabling the interworking between the Yacht service and data source of the data service. This node is used to implement the data communication based on Data Cube. This node is available only when the Yacht account exists in the system. | **Table 6** Component  
| Orchestration Element | Element Description |
| :-- | :-- |
| Text Annotation | Users can add annotation to the service, which is similar to code comments. | **Parent topic:** [[Configuring Services|Configuring Services]]