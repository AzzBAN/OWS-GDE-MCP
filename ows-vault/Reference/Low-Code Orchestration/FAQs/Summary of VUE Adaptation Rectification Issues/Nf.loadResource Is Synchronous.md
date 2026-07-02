---
title: "Nf.loadResource Is Synchronous"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399180669.html"
depth: 3
---
# Nf.loadResource Is Synchronous

-   **Issue:** Nf.loadResource is synchronous, but loadResource is asynchronous. Therefore, no value cannot be obtained by Nf.res.
    
    Nf.loadResource("com/huawei/mateinfo/portal/action/LoadPortalAction"); 
    ... 
    Nf.res("mateinfo.userSetting.model")
    

-   **Solution:** Place Nf.loadResource outside Nf.ready().

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]