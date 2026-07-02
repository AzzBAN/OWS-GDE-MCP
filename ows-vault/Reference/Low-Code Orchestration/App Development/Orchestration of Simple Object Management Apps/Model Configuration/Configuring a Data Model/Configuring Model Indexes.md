---
title: "Configuring Model Indexes"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/datamodel_005.html"
depth: 5
---
#### Context

Restrictions on model index configuration:

-   Indexes can be created only for data models and workflow agent models. Indexes cannot be created for data source models and elastic models.
-   Composite indexes are supported. A maximum of five properties can be added to a single index.
-   Indexes cannot be created for the following properties: password, user list, user group list, file list, reference list, and enumeration list.
-   Indexes cannot be created for primary keys and default fields.
-   The model index name must be unique in a single model.