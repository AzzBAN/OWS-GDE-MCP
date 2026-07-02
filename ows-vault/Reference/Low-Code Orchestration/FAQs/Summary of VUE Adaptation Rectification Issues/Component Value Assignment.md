---
title: "Component Value Assignment"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365340984.html"
depth: 3
---
# Component Value Assignment

-   **Issue:** The following assignment method invalidates bidirectional binding. The value obtained by the getValue interface is null.
    
    $("#collector\_id").val(id\_html); 
    $("#collector\_alias").val(alias\_html);
    
-   **Solution:** You are advised to use the setValue interface of the component.
    
    S("componentId").setValue("content");
    

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]