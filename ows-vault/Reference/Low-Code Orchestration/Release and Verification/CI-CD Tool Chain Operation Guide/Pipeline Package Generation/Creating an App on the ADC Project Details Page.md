---
title: "Creating an App on the ADC Project Details Page"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mate_pipeline_new.html"
depth: 4
---
# Creating an App on the ADC Project Details Page

1.  Click **CI/CD Tool Chain** in the lower left corner, and click **Pipeline** in the displayed window.
    
    **Figure 1** Accessing the **Pipeline** page from the **CI/CD Tool Chain** menu
    
    ![[en-us_image_0000001782515294.png]]
    
2.  On the displayed page, click **Deliver** to create an app.
    
    **Figure 2** Deliver button  
    ![[en-us_image_0000001829195081.png]]
    
    After you click **Deliver**, the **Configure Login Info** dialog box is displayed. The login information is used to test the related task on the pipeline.
    
    **Figure 3** Configuring the login information  
    ![[en-us_image_0000001829075037.png]]
    
    Select an environment as required, enter the user name and password, and click **Deliver**.
    
    **Figure 4** Packed into an app  
    ![[en-us_image_0000001782355622.png]]
    
    **Table 1** Parameter description  
    | Name | Description |
    | :-- | :-- |
    | App Name | Same as the project name and cannot be modified. |
    | Version | The version number is incremented by 1 by default. The version number must be later than the previous one, for example, 0.0.1. |
    | Version Type | You can select Beta Version or Official Version. |
    | Asset Catalog | You can select the node where the asset is stored. | Click **Pack** to start the pipeline.
    
3.  Start the pipeline, and tasks are started in sequence and the page is refreshed to the latest status.
    
    **Figure 5** Pipeline details (Executing)  
    ![[en-us_image_0000001782515286.png]]
    
    **Figure 6** Pipeline details (Executed and the package delivered)  
    ![[en-us_image_0000001782355606.png]]
    
4.  View the task logs.
    
    You can click ![[en-us_image_0000001829195041.png]] in the lower left corner to view the pipeline execution logs. You can click the task status, such as ![[en-us_image_0000001829195069.png]], ![[en-us_image_0000001782515278.png]], or ![[en-us_image_0000001829075013.png]] to go to the log page of the corresponding task and quickly locate the fault.
    
    **Figure 7** Viewing logs  
    ![[en-us_image_0000001829195065.png]]
    
5.  Click the package name to download the asset package.
    
    **Figure 8** Packaging task  
    ![[en-us_image_0000001782355626.png]]
    

**Parent topic:** [[Pipeline Package Generation|Pipeline Package Generation]]