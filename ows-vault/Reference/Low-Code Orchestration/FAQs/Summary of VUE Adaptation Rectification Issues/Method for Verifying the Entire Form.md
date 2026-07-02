---
title: "Method for Verifying the Entire Form"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399060789.html"
depth: 3
---
# Method for Verifying the Entire Form

-   For versions using EXT:
    
    var validateResult \= Spl.form.FormPanelManager.get("copyForm").getValidation(); 
    if(!validateResult.doCheck())
     {
         return;
     }
    
-   For versions using VUE:
    
    S("copyForm").validate(function(result){
         if(result){
             //The verification is successful.
         }else{
             //The verification failed.
         }
     })
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]