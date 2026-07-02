---
title: "Conditional Routing"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_079.html"
depth: 8
---
#### Procedure

1.  Click the name of the endpoint to be configured, and choose **Endpoint-Level Policy** > **Routing Policy**.
2.  Configure a conditional route.
    
    1.  Choose **Choose Type** > **Conditional Routing**.
    2.  Set **Default URL** and **Route URL**.
    3.  Click **Add Parameters** next to **Route URL**, and set parameters as required. For details about the parameters, see [Table 1](#EN-US_TOPIC_0000001760154869__en-us_topic_0000001259019839_en-us_topic_0000001188041237_table16882161035517).
        
        **Table 1** Parameters for configuring conditional routing  
        | Parameter | Description |
        | :-- | :-- |
        | Condition | Condition name. The default value is Condition1. If multiple conditions exist, the conditions are indexed in ascending order, for example, Condition1 and Condition2. |
        | Route URL | User-defined routing URL. |
        | Parameter Name | Parameter name in a request message. |
        | Parameter Position | Location of a parameter in a request packet. The value must be in the JSONPath format. |
        | Match Type | The options are as follows:
        -   **Exact Match**: If one or more parameters exist, the matching is successful only when all parameters are met.
        -   **Fuzzy Match**: If multiple parameters exist, the matching is successful when one of the parameters is met.
        
         |
        | Parameter Value List | Preset parameter information. When the information in a request message matches a parameter in the parameter value list, the corresponding route URL is called. | ![[note_3.0-en-us.png]]
        
        You can add multiple conditions. When two or more conditions are met, the first condition that is met is used for routing by default.
        
    
3.  Click **Save**.