---
title: "Event Bus and Event"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_024.html"
depth: 4
---
#### Orchestration Procedure

1.  Drag an **Event Bus** component under **Includes**.
    
    ![[en-us_image_0000001613955906.png]]
    
2.  Drag an **Event** component under **Event Bus** and set **Name** to **event**.
    
    ![[en-us_image_0000001613796066.png]]
    
3.  The following figure shows the relationship between the **Event Bus** and **Event** components.
    
    ![[en-us_image_0000001662235989.png]]
    
    -   Multiple **Event** components can be configured under the **Event Bus** component. Each event consists of a trigger and an action.
    -   When a user behavior meets the trigger condition, all actions under the current event are executed.
    -   By default, triggers and actions are executed from top to bottom. The component itself also supports priority configuration.