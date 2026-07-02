---
title: "Dynamic Routing"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_078.html"
depth: 8
---
#### Procedure

1.  Click the name of the endpoint to be configured, and choose **Endpoint-Level Policy** > **Routing Policy**.
2.  Configure a dynamic route.
    
    1.  Set **Choose Type** to **Dynamic Routing**.
    2.  Configure the route type and path expression by referring to [Table 1](#EN-US_TOPIC_0000001712315768__en-us_topic_0000001259099905_table8822154601716).
        
        **Table 1** Parameters  
        | Parameter | Description |
        | :-- | :-- |
        | Route Type | (Mandatory) When the type is jsonpath, select the corresponding packet field. Currently, $.header, $.body, and $.query are supported. |
        | Routing Expression | Set this parameter based on the selected route type. For example, the format of jsonpath is $.header.addr. |
        | URL Address | URL set based on Path Expression. For example, if URL Address is set to https://${servicename}:port, ${servicename} is automatically replaced by the URL in the request. NOTE: When the dynamic route is used, the system replaces the path expression with the corresponding URL in the request message. The following two situations exist: If URL Address is set to https://${addr}/service, ${addr} is replaced by the corresponding part of the URL in the request. If URL Address is set to ${addr}, the complete URL in the request is used. | 3.  Click **Save**.