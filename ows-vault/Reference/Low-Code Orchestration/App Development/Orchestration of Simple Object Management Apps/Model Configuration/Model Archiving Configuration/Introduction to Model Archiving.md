---
title: "Introduction to Model Archiving"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/datamodel_008.html"
depth: 5
---
#### Model Archiving

Data models, elastic models, and data source models where default data sources are used support the archiving capability. Data source models where extra data sources are used do not support the archiving capability.

Model archiving supports the following archiving objectives:

-   **Delete**: Data is deleted. If the archived data contains files or file list, files will be deleted.
-   **Dump Elastic Model**: Data is archived to the configured elastic model.
-   **Dump File Server**: Files are archived using the file service.
-   **Dump SFTP Server**: Data is archived to the SFTP server.

**Table 1** Archiving capabilities of different models     
| Model Type | Archiving Target: Delete | Archiving Target: Dump Elastic Model | Archiving Target: Dump File Server | Archiving Target: Dump SFTP Server |
| :-- | :-- | :-- | :-- | :-- |
| Data model | Supported | Supported | Supported | Supported |
| Elastic model | Supported | Not supported | Supported | Supported |
| Data source model (default data sources) | Supported | Supported | Supported | Supported | Models can be archived in either of the following methods:

-   **Independent**: Used to archive a single model or as the root node model of the dependency tree.
-   **Associated**: Used to archive associated models based on other models.

As shown in the following figure, models B and C depend on model A. If only model A is archived, an error occurs when you query the data of model B and C depended on archived model A. Therefore, you need to configure associated archiving for models B and C. When model A is archived independently, models B and C need to be archived together. Because model D does not depend on other models, archive it independently.

**Figure 1** Model diagram  
![[en-us_image_0000001092916044.png]]

If the model uses the database sharding function and the current model is a data model in the model archiving scenario, dependency relationships can be configured only between only data models, data source models, and proxy models in the same schema of the same database.