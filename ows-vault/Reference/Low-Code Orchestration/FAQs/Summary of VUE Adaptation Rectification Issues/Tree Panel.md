---
title: "Tree Panel"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365340988.html"
depth: 3
---
# Tree Panel

You need to perform the following adaptation rectification in the versions using VUE:

-   Create an API:
    
    S("Component ID").setAutoExpand(true); //true indicates that the component is expanded automatically, and false indicates that the component is expanded manually.
    S("Component ID").setParams(params);   //Set tree panel service parameters.
    S("Component ID").loadData(params);   //Reload the tree panel.
    
-   Events:
    
    Spl.EventBus.register("Component ID", "nodeLoaded", function(){}); //An event is triggered when a node is loaded.
    Spl.EventBus.register("Component ID", "nodeClick", function(){}); //An event is triggered when a node is clicked.
    Spl.EventBus.register("Component ID", "dblClick", function(){}); //An event is triggered when a node is double-clicked.
    Spl.EventBus.register("Component ID", "nodeExpand", function(){}); //An event is triggered when a node is expanded.
    Spl.EventBus.register("Component ID", "expand", function(){});Spl.EventBus.register("Component ID", "expand", function(){}); //An event is triggered when a node is expanded.
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]