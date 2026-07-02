---
title: "Loading an App"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001709426344.html"
depth: 7
---
#### U.applicationLoaded(module, page, callback)

Used to allow users to perform certain operations when a light app is opened for the first time or when the app is installed and opened for upgrade.

  
| Parameter | Type | Description |
| :-- | :-- | :-- |
| module | String | Light app module |
| page | String | Light app orchestration page |
| callback | Function | Execution initialization method | Example:

function init() { 
 // Execution initialization method
} 
U.applicationLoaded("mobile", "index", init)