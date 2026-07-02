---
title: "Health Check"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_081.html"
depth: 7
---
#### Procedure

1.  Click the name of the endpoint to be configured, and choose **Endpoint-Level Policy** > **Health Detection**.
2.  In the navigation pane, choose **Health Check**.
3.  Click to enable **Health Check** and set related parameters. The parameters are described as follows.
    
    **Table 1** Health check parameters  
    | Parameter | Description |
    | :-- | :-- |
    | Detection Cycle | Interval for executing the health check URL. The value ranges from 1 to 3000000. |
    | Health Check URL | Health API of an endpoint. You can add a maximum of 500 health check URLs. The URL format can be https://xxxx or ${xxxx}. | 4.  Click **Save**.