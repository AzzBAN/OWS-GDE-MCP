---
title: "Corner Mark Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_002.html"
depth: 4
---
#### Orchestration Procedure

1.  In addition to directly setting the text value to configure a corner mark, you can also obtain the data by calling a service. The following configuration items are related to the service:
    
    -   **Parameters**: input parameter transferred to the called service
    -   **Service ID**: service to be called
        
        ![[en-us_image_0000001679144589.png]]
        
    
2.  After parameters are set, they are transferred to the service when the service is called.
    
    **Figure 1** Setting parameters
    
    ![[en-us_image_0000001679144817.png]]
    
    **Figure 2** Service input parameters
    
    ![[en-us_image_0000001679224885.png]]
    
3.  There are specific requirements on service output parameters. Data must be returned in **result.cornerValue**.
    
    1.  Create the getCornerValue service.
        
        ![[en-us_image_0000001630425262.png]]
        
    2.  Generate simulation data by running scripts.
        
        ![[en-us_image_0000001630985722.png]]
        
        ![[en-us_image_0000001481780138.png]]
        
    3.  Configure the script content by referring to the following figure. The information under **return** is output data.
        
        ![[en-us_image_0000001630745182.png]]
        
        **Figure 3** Actual page display after data is returned
        
        ![[en-us_image_0000001481621086.png]]