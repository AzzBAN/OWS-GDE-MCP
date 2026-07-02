---
title: "Obtaining the GDELink Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457197405.html"
depth: 9
---
#### U.getViewConfig(params, callback)

Used to obtain the client display configuration.

![[notice_3.0-en-us.png]]

Android and Harmony versions are supported.

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | Input parameter of the **params** parameter

   
| Parameter | Description | Value | Description |
| :-- | :-- | :-- | :-- |
| key | Configuration information | allow\_screenshot | Whether to allow screenshot | Example:

  U.getViewConfig({
    key: "allow\_screenshot"
  })