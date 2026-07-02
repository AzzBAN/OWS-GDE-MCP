---
title: "Photograph"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_021.html"
depth: 4
---
#### Orchestration Procedure

1.  Prepare a basic form in advance to update and display model data. The form contains the components shown in the following figure.
    
    ![[en-us_image_0000001630406332.png]]
    
    ![[notice_3.0-en-us.png]]
    
    For details about how to orchestrate basic forms, see [[Basic Form Orchestration|Basic Form Orchestration]].
    
2.  Confirm that the model of the form contains the **File List** property.
    
    ![[en-us_image_0000001630886044.png]]
    
    Configure constraints, such as **File Type**, **File Size**, and **Max. Number**, on model properties.
    
    ![[en-us_image_0000001630886012.png]]
    
3.  Drag a **Photograph** component under **Data Fields**.
    
    ![[en-us_image_0000001630566152.png]]
    
4.  Set **Name** to **more**, which corresponds to the field returned by the GET service.
    
    ![[en-us_image_0000001679325873.png]]
    
    The following figure shows the data transfer process.
    
    ![[en-us_image_0000001630726108.png]]
    
    ![[en-us_image_0000001630566180.png]]
    
5.  Set **Photo Title** to **Photo**.
    
    ![[en-us_image_0000001679125733.png]]
    
6.  Set **Total** to **5**, which cannot be greater than the value in model constraints.
    
    ![[en-us_image_0000001630886016.png]]
    
7.  Set **Require Submission** to **Yes** to allow component data to be submitted to the back end.
    
    ![[en-us_image_0000001481592096.png]]
    
8.  Set **Select System Photograph** to **Yes**. Photos in the album can be selected on the mobile.
    
    ![[en-us_image_0000001532191853.png]]
    
9.  After the preceding configurations are complete, preview the page.
    
    ![[en-us_image_0000001679125717.png]]
    
10.  Click the photo icon, select an image to upload, and click **Update**.
     
     ![[en-us_image_0000001630726116.png]]
     
     ![[en-us_image_0000001679205981.png]]
     
11.  Preview the page again and click **Data Loader**. The image is displayed.
     
     ![[en-us_image_0000001679206009.png]]