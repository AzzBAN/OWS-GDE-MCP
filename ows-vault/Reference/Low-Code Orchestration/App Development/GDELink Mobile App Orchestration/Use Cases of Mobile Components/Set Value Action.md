---
title: "Set Value Action"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_026.html"
depth: 4
---
#### Orchestration Procedure

1.  Drag a **Set Value Action** component under **Actions**.
    
    ![[en-us_image_0000001679319517.png]]
    
2.  Set **Data Field** to **name2**.
    
    ![[en-us_image_0000001532053361.png]]
    
    **name2** corresponds to the value of **Id** (that is, **name2**) for the **Text Input** component in the form.
    
    ![[en-us_image_0000001630879672.png]]
    
    ![[en-us_image_0000001630719752.png]]
    
3.  Set **Value** to **#Form\[formpanel.name\]**.
    
    ![[en-us_image_0000001679199645.png]]
    
    ![[en-us_image_0000001679119365.png]]
    
    **#Form\[formpanel.name\]** indicates that the value of the **name2 Text Input** component comes from the **name Text Input** component of the formpanel form.
    
    ![[en-us_image_0000001679199637.png]]
    
4.  After the preceding configurations are complete, click **Preview**. Information as shown in the following figure is displayed.
    
    ![[en-us_image_0000001679119369.png]]
    
    Change the value in the preceding text box to **Tom111**. The value in the following text box is automatically changed to **Tom111**.
    
    ![[en-us_image_0000001630559808.png]]