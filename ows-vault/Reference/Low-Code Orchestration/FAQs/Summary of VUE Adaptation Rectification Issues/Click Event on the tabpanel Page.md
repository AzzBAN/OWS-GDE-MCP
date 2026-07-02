---
title: "Click Event on the tabpanel Page"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399180685.html"
depth: 3
---
# Click Event on the tabpanel Page

You need to perform the following adaptation rectification in the versions using VUE:

-   Method 1:
    
    Spl.EventBus.register("xxtabPanelId","click",function(tabName){
         //Determine which tab is clicked based on the value of tabName.
    })
    
-   Method 2:
    
    Spl.EventBus.register("xxtabPanelId","active",function(param){
          //var tabName = param.activeTabId
    })
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]