---
title: "File Input"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_020.html"
depth: 4
---
#### Orchestration Procedure

1.  Prepare a basic form in advance to update and display model data. The form contains the components shown in the following figure.
    
    ![[en-us_image_0000001630888860.png]]
    
    ![[notice_3.0-en-us.png]]
    
    For details about how to orchestrate basic forms, see [[Basic Form Orchestration|Basic Form Orchestration]].
    
2.  Confirm that the model of the form contains the **File List** property.
    
    ![[en-us_image_0000001630728920.png]]
    
    Configure constraints, such as **File Type**, **File Size**, and **Max. Number**, on model properties.
    
    ![[en-us_image_0000001630728928.png]]
    
3.  Drag a **File Input** component under **Data Fields**.
    
    ![[en-us_image_0000001679008653.png]]
    
4.  Set **Name** to **more**, which corresponds to the field returned by the GET service.
    
    ![[en-us_image_0000001630568996.png]]
    
    The following figure shows the data transfer process.
    
    ![[en-us_image_0000001679008657.png]]
    
5.  Set **Label** to **File Input**.
    
    ![[en-us_image_0000001679208821.png]]
    
6.  Set **Maximum Number** to **5**, which cannot be greater than the value of **Max. Number** configured in [2](#EN-US_TOPIC_0000001400558456__en-us_topic_0000001400122442_li15593155135814).
    
    ![[en-us_image_0000001679008649.png]]
    
7.  Set **File Type Extension** to **png,xlsx,docx,jpg**, which must be a value included in the value range of **File Type** configured in [2](#EN-US_TOPIC_0000001400558456__en-us_topic_0000001400122442_li15593155135814).
    
    ![[en-us_image_0000001532340809.png]]
    
8.  Set **File Size Limit** to **1024**, which cannot be greater than the value of **File Size** configured in [2](#EN-US_TOPIC_0000001400558456__en-us_topic_0000001400122442_li15593155135814).
    
    ![[en-us_image_0000001532020905.png]]
    
9.  After the preceding configurations are complete, preview the page.
    
    ![[en-us_image_0000001630569000.png]]
    
10.  Click the plus icon (+), select a file to upload, and click **Update**.
     
     ![[en-us_image_0000001679208825.png]]
     
     ![[en-us_image_0000001679328713.png]]
     
11.  Preview the page again and click **Data Loader**. The file is displayed.
     
     ![[en-us_image_0000001679208829.png]]