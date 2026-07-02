---
title: "Method for Verifying a Single Field in the Form"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399180701.html"
depth: 3
---
# Method for Verifying a Single Field in the Form

-   For versions using EXT:
    
    S("copyForm").getValidator().get("name").allCheck();
    
-   For versions using VUE:
    
    S("copyForm").validateSingleField("name")
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]