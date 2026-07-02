---
title: "Configuring Page-based Data Export"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/excel_009.html"
depth: 4
---
#### Context

Data can be exported based on page. In actual application scenarios, data may be frequently added. As a result, duplicate data may be exported. This problem can be resolved through the pagination configurations.

This section describes how to modify the configurations of the data list query service and data export service automatically generated after the model creation.

Assume that the data model **info\_goods** has been created and services and pages are automatically generated. The following elements are automatically generated:

-   **info\_goods\_get\_list**
-   **info\_goods\_export**: The data export service **info\_goods\_export** calls the data list query service **info\_goods\_get\_list**.
-   **info\_goods\_grid**: Click **Export** on the page to call the data export service **info\_goods\_export** to export data.