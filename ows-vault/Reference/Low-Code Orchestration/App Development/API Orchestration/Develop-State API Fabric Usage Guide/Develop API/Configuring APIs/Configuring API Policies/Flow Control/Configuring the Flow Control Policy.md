---
title: "Configuring the Flow Control Policy"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_054.html"
depth: 8
---
#### Procedure

1.  Choose **Flow Control** > **Flow control Policy**, set **Traffic Control Speed** and **Duration**.
    
    Based on the configuration granularity, set information on the **Flow control Policy** tab page under **API-Level Policy** or **API Method-Level Policy**.
    
    **Table 1** Flow control parameters  
    | Parameter | Description |
    | :-- | :-- |
    | Threshold | Number of calls on APIs in a period. This configuration applies to all Access nodes or Access pods in the system. For example, if this parameter is set to 100, the total number of times that APIs can be called by all API Access nodes or API Access pods in the system is 100. NOTE: If this parameter is set to 0, the flow control is not performed. |
    | Duration | Period during which APIs can be called. The Redis is used to implement flow control. You are advised to select a larger time granularity, for example, Minute, to improve the performance and collect statistics on the number of access requests. If the time granularity is too small, the number of accesses may be inaccurate, affecting the flow control effect. For example, if Cycle is set to 1 Second, data is continuously updated to the Redis every second, affecting the overall performance. |
    | Degradation Policy | If the Redis service is interconnected and is unavailable, Degradation Policy can be configured.
    -   **No Flow Control**: The flow control policy is invalid.
    -   **Single Machine Flow Control**: If two nodes exist in the Access cluster and **Threshold** is set to **100**, after **Single Machine Flow Control** is selected, the number of calls in a period changes to 200.
    -   **Single Machine Share**: If two nodes exist in the Access cluster and **Threshold** is set to **100**, after **Single Machine Share** is selected, the number of calls of a single node in a period is **50**.
    
     | 2.  Click **Save**.