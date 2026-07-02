---
title: "Deploying and Commissioning APIs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_159.html"
depth: 5
---
#### Restrictions and Description

-   The commissioning function applies only to APIs whose processes have been orchestrated.
-   Only the SOAP and REST protocols are supported.
-   The commissioning function supports the following authentication modes: OAuth 2.0, GAM authentication, and username and password.
-   The API Fabric limits the size of a request body to 10 KB. If the size of the request body of an API exceeds 10 KB, the page performance may be abnormal and frame freezing may occur. Therefore, you are advised not to use the commissioning function to call the API.
-   You can enable or disable the deployment commissioning function as required. The procedure is as follows:
    1.  Log in to the GDE data zone as the **admin** user.
    2.  Choose **Products and Services** > **Administration** > **Common Setting** > **Config Management**.
    3.  On the **Config Center** page, enable **Display All Configurations** in the upper right corner.
    4.  Search for the keyword **gde.apifabric.builder.test.active** in the search box and click the search icon.
    5.  Click ![[en-us_image_0000002302651281.png]] next to **gde.apifabric.builder.test.active** and modify the **gde.apifabric.builder.test.active** configuration based on site requirements.
        
        The options are as follows:
        
        -   If this parameter is set to **true**, the deployment and commissioning function is enabled.
        -   If the parameter is set to **false**, the deployment and commissioning function is disabled.