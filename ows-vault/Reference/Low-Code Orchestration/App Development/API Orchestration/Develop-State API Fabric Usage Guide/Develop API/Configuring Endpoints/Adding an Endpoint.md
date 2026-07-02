---
title: "Adding an Endpoint"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_131.html"
depth: 6
---
#### Context

![[note_3.0-en-us.png]]

-   Endpoints associated with the APIs cannot be deleted.
-   Choose **More** > **Associated APIs** next to an endpoint to view the APIs associated with the endpoint. In the dialog box that is displayed, click an API name to go to the **Basic Information** page of the API.

Endpoints can be imported and exported separately or be imported in batches. Endpoints are exported based on the catalog level and placed in the corresponding catalogs. [Figure 1](#EN-US_TOPIC_0000001569107017__en-us_topic_0122469099_fig129284175419) shows the ZIP package structure.

-   **endpoint**: common service definition. **Default** indicates the name of the catalog where the endpoint is located.
-   **config**: common configuration.
-   **.mf**: asset signature list file, including the file directory and hash value corresponding to the file.
-   **.cms**: signature file generated after the .mf file is digitally signed.
-   **.package**: description file used to identify the package types when importing packages to the API Governance portal.

**Figure 1** Endpoint package structure  
![[en-us_image_0295071961.png]]