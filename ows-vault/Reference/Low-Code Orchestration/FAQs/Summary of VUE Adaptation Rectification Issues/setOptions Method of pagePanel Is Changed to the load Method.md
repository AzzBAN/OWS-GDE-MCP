---
title: "setOptions Method of pagePanel Is Changed to the load Method"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365340996.html"
depth: 3
---
# setOptions Method of pagePanel Is Changed to the load Method

-   For versions using EXT:
    
    S("inOutSiteRecordFrame").setOptions({
        id:"inOutSiteRecordFrame",
        url:"/app/" + tenantId + "/spl/in\_out\_site\_record\_detail.spl"
    });
    
-   For versions using VUE:
    
    S("xxpagepanelid").load({url:"xxx",location:"xx",parameters:"xx"})   (Use either **url** or **location**.)
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]