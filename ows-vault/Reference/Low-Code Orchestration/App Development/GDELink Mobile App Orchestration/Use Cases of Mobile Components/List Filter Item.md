---
title: "List Filter Item"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_009.html"
depth: 4
---
#### Orchestration Procedure

1.  Configure the data filtering function based on text input.
    
    1.  Drag the **List Filter Item** component under **Filter Items**.
        
        ![[en-us_image_0000001679225077.png]]
        
    2.  Set **Label** to **Input Filter**.
        
        ![[en-us_image_0000001630745042.png]]
        
    3.  Set **Type** to **input**.
        
        ![[en-us_image_0000001679344909.png]]
        
        **Type** specifies the type of the filtering item. **input** indicates an input text box.
        
        ![[en-us_image_0000001630745090.png]]
        
    4.  Set **Model Key** to **name**.
        
        ![[en-us_image_0000001679344941.png]]
        
        The value of **Model Key** is transferred to the service as a parameter.
        
        ![[en-us_image_0000001679024745.png]]
        
        ![[en-us_image_0000001630585122.png]]
        
    
2.  Configure the data filtering function in the option selection mode.
    
    1.  Drag the **List Filter Item** component under **Filter Items**.
        
        ![[en-us_image_0000001480416534.png]]
        
    2.  Set **Label** to **Select Filter**.
        
        ![[en-us_image_0000001679224897.png]]
        
    3.  Set **Type** to **select**.
        
        ![[en-us_image_0000001630904906.png]]
        
        Set options for a filter whose **Type** is **select**.
        
        ![[en-us_image_0000001630904898.png]]
        
    4.  Set **Options** to values in the following figure.
        
        ![[en-us_image_0000001679144793.png]]
        
        ![[en-us_image_0000001630425458.png]]
        
    5.  Set **Model Key** to **sex**.
        
        ![[en-us_image_0000001679024717.png]]
        
        The value of **Model Key** is transferred to the service as a parameter.
        
        ![[en-us_image_0000001679344729.png]]
        
        ![[en-us_image_0000001679225101.png]]
        
    6.  The configuration items can also be obtained through a service.
        
        ![[en-us_image_0000001630905130.png]]
        
        -   The format of the data returned by the service is as follows:
            
            ![[en-us_image_0000001679344945.png]]
            
        -   Configure **Output** to complete the mapping as shown in the following figures.
            
            ![[en-us_image_0000001630744990.png]]
            
            ![[en-us_image_0000001630425426.png]]
            
        -   The configuration items obtained through services are different from the manual configuration items on the page.
            
            ![[en-us_image_0000001630745106.png]]
            
            ![[en-us_image_0000001630425398.png]]
            
    
3.  Configure the data filtering function in the multi-option selection mode.
    
    1.  Drag the **List Filter Item** component under **Filter Items**.
        
        ![[en-us_image_0000001679224869.png]]
        
    2.  Set **Label** to **Multiselect Filter**.
        
        ![[en-us_image_0000001630585126.png]]
        
    3.  Set **Type** to **multiSelect**.
        
        ![[en-us_image_0000001679024925.png]]
        
        **multiSelect** indicates the multi-option selection box.
        
        ![[en-us_image_0000001679344861.png]]
        
    4.  Set **Options** to values in the following figure.
        
        ![[en-us_image_0000001679144801.png]]
        
        ![[en-us_image_0000001630585306.png]]
        
    5.  Set **Model Key** to **sex**.
        
        ![[en-us_image_0000001679024697.png]]
        
        The value of **Model Key** is transferred to the service as a parameter.
        
        ![[en-us_image_0000001679344957.png]]
        
        ![[en-us_image_0000001630585098.png]]
        
    6.  The configuration items can also be obtained through a service or configurations in [2](#EN-US_TOPIC_0000001400238620__en-us_topic_0000001400121904_li64381734132713).
    
4.  Associate filtering items by configuring **Parent Id** and **Parent Key**.
    
    1.  Set **Id** of the filtering item in the option filtering list to **singleSelect**.
        
        ![[en-us_image_0000002194718025.png]]
        
    2.  Set **Parent Id** of the filtering item in the multi-selection filtering list to **singleSelect**. Set **Parent Key** to **single**, which is used as the request parameter name.
        
        ![[en-us_image_0000001679225089.png]]
        
        In this way, the two values are associated. If a value is selected under **Select Filter**, the value is transferred to **Multiselect Filter**.
        
        ![[en-us_image_0000001630585290.png]]
        
        ![[en-us_image_0000001679225085.png]]