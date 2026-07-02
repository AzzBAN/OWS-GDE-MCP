---
title: "Obtaining the Light App List and Plugin List of Light Apps"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457397225.html"
depth: 7
---
#### U.getAppPluginList(appType, callBack)

  
| Parameter | Type | Description |
| :-- | :-- | :-- |
| appType | String | "ALL", "SPL", "H5", "PLUGIN" |
| callBack | Function | Callback function | Example:

U.getAppPluginList("ALL", function(res) {
   //do something
})