---
title: "Value Return Mode of the validate Attribute of formPanel Is Changed to Asynchronous"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365500892.html"
depth: 3
---
# Value Return Mode of the validate Attribute of formPanel Is Changed to Asynchronous

-   For versions using EXT:
    
    var result = S("form1").validate() // The value return mode in the VUE framework is changed to asynchronous, and the return value is empty.
    if(result){
        console.log("validate success");
    }else{
        console.log("validate failed");
    }
    
-   For versions using VUE:
    
    S("form1").validate(function(result){
        if(result){
            console.log("validate success");
        }else{
            console.log("validate failed");
        }
    })
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]