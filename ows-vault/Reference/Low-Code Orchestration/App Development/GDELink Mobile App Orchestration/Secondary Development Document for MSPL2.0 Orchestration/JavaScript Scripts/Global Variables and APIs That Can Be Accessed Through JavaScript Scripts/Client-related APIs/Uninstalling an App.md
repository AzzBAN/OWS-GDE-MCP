---
title: "Uninstalling an App"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001709585808.html"
depth: 7
---
#### U.applicationUnloaded(module, page, callback)

Used to allow users to perform certain operations during light app uninstallation.

  
| Parameter | Type | Description |
| :-- | :-- | :-- |
| module | String | Light app module |
| page | String | Light app orchestration page |
| callback | Function | Callback method | Example:

function destroy() { 
 // Callback method
} 
U.applicationUnloaded("mobile", "index", destroy)