---
title: "window.location.href = \"xxx\" Adaptation"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365341000.html"
depth: 3
---
# window.location.href = "xxx" Adaptation

-   For versions using EXT:
    
    window.location.href = "/app/spl/system/system\_test.spl";
    
-   For versions using VUE:
    
    Spl.WindowManager.open({"url":"/app/spl/system/system\_test.spl"});
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]