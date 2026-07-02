---
title: "Data Field Value Change Trigger"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_025.html"
depth: 4
---
#### Orchestration Procedure

1.  Drag a **Data Field Value Change Trigger** component under **Triggers**.
    
    ![[en-us_image_0000001679320149.png]]
    
2.  Set **Data Field** to **name**.
    
    ![[en-us_image_0000001481291896.png]]
    
    **name** corresponds to the value of **Id** (that is, **name**) for the **Text Input** component in the form.
    
    ![[en-us_image_0000001630720384.png]]
    
    ![[en-us_image_0000001679120009.png]]
    
3.  Drag a **Set Value Action** component under **Action** and update the value of **name** to **name2**.
    
    ![[en-us_image_0000001679120013.png]]
    
4.  After the preceding configurations are complete, click **Preview**. Information as shown in the following figure is displayed.
    
    ![[en-us_image_0000001630560448.png]]
    
    Change the value in the preceding text box to **Tom111**. The value in the following text box is automatically changed to **Tom111**.
    
    ![[en-us_image_0000001679200285.png]]