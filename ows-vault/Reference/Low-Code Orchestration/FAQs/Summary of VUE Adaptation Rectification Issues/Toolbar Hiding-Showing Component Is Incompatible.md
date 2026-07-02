---
title: "Toolbar Hiding/Showing Component Is Incompatible"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365340992.html"
depth: 3
---
# Toolbar Hiding/Showing Component Is Incompatible

The SPL2.0 Data Field component provides the hide() and show() APIs for hiding or showing toolbars.

-   For versions using EXT:
    
    $("#"+inputIds\[i\]).parents(".toolbar\_each ").show(); 
    $("#"+inputIds\[i\]).parents(".toolbar\_each ").hide();
    
-   For versions using VUE:
    
    S(inputIds\[i\]).show(); 
    S(inputIds\[i\]).hide();
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]