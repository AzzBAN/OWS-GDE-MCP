---
title: "Column Hiding/Showing in Grid Is Incompatible"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399060777.html"
depth: 3
---
# Column Hiding/Showing in Grid Is Incompatible

-   For versions using EXT:
    
    var columnModel \= S("webServiceGrid").getGrid().getColumnModel();
        columnModel.setHidden(2, false);
        columnModel.setHidden(3, true);
    
-   For versions using VUE:
    
    S("webServiceGrid").setHiddens(\[{
                     index: 2,
                     hidden: false
                 }, {
                     index: 3,
                     hidden: true
                 }
             \]);
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]