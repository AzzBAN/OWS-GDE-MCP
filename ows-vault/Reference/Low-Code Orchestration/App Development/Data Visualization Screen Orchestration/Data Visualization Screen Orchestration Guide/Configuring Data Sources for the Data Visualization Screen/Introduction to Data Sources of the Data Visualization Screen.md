---
title: "Introduction to Data Sources of the Data Visualization Screen"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_largescreen_011.html"
depth: 5
---
# Introduction to Data Sources of the Data Visualization Screen

You need to import data to the components displayed on the data visualization screen for visualized display.

-   Unified data sources: data sources that can be used by all orchestration components on the data visualization screen. After a unified data source is added, you can apply it to any component.
-   Independent data sources: data sources configured for a single component and cannot be shared by other components.

Currently, the following data source access modes are supported:

-   Static data: Fixed values are displayed. This mode applies to the scenario where data is displayed in static mode and does not need to be updated.
-   Service: Values are obtained and displayed by calling the orchestration service. This mode applies to the data display in the system.
-   API: Values are obtained and displayed by calling APIs. This mode applies to the data display from external systems.
-   TQL expression: Model data is obtained using TQL expressions.
-   Custom data source: user-defined data sources
-   Model: model created based on the current system, which is used as the data source of the data visualization screen.

**Parent topic:** [[Configuring Data Sources for the Data Visualization Screen|Configuring Data Sources for the Data Visualization Screen]]