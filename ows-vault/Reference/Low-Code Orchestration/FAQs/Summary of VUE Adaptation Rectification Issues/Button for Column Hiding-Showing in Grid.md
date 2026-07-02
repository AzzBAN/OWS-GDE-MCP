---
title: "Button for Column Hiding/Showing in Grid"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399180697.html"
depth: 3
---
# Button for Column Hiding/Showing in Grid

-   For versions using EXT:
    
    $(".icon\_column.icon\_edit\[btid=modifyServiceBT\]").hide();
    
-   For versions using VUE:
    
    Spl.EventBus.register("modifyBT", "visibleCondition", function (data) {
            data.button.visible = false;
        });
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]