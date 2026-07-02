---
title: "Form Panel"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_017.html"
depth: 4
---
#### Orchestration Procedure

1.  Drag a **Form Panel** component to the component tree and set **Id** to **formpanel**.
    
    ![[en-us_image_0000001614115266.png]]
    
2.  The **Form Panel** component is mainly used as a form container and needs to be used with the **Validations** and **Button** components and form elements.
    
    -   Verifications
        
        ![[en-us_image_0000001662675101.png]]
        
    -   Form elements
        
        ![[en-us_image_0000001662635133.png]]
        
    -   Button
        
        ![[en-us_image_0000001662515269.png]]
        
    
3.  Drag a **Text** component under **Data Fields** and set the parameters as shown in the following figures.
    
    ![[en-us_image_0000001613955274.png]]
    
    ![[en-us_image_0000002194733981.png]]
    
4.  Drag a **Text Input** component under **Data Fields** and set the parameters as shown in the following figures.
    
    ![[en-us_image_0000001613955278.png]]
    
    ![[en-us_image_0000002194733893.png]]
    
5.  Drag a **Service Button** component under **Button** and set the parameters as shown in the following figures.
    
    ![[en-us_image_0000001614115346.png]]
    
    ![[en-us_image_0000001662675197.png]]
    
6.  After the preceding configurations are complete, view an initial form on the preview page. Text display, text input, and form data submission functions are provided on the page.
    
    ![[en-us_image_0000001614527890.png]]
    
    -   Enter some text and click **Submit**. The interaction between the form and back-end services is displayed.
        
        ![[en-us_image_0000001663087805.png]]
        
    -   Note that the key of the form data is obtained from the value of **Name** in the component configuration item.
        
        ![[en-us_image_0000001614275370.png]]