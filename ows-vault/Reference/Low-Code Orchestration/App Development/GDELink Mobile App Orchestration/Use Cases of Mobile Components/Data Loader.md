---
title: "Data Loader"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_018.html"
depth: 4
---
#### Orchestration Procedure

1.  Drag a **Data Loader** component under **Form Panel**.
    
    ![[en-us_image_0000001630744962.png]]
    
2.  Set **Interface** to a GET service.
    
    ![[en-us_image_0000001679024929.png]]
    
3.  Set **Parameters** to values in the following figures.
    
    ![[en-us_image_0000001679024805.png]]
    
    ![[en-us_image_0000001630745154.png]]
    
    Configured parameters are transferred as service input parameters.
    
    ![[en-us_image_0000001630585030.png]]
    
4.  In most cases, service input parameters are dynamically obtained. Set parameters as shown in the following figure.
    
    ![[en-us_image_0000001679024897.png]]
    
5.  After the preceding configurations are complete, click **Preview**. The service is called and the data is displayed in the form.
    
    ![[en-us_image_0000001630744970.png]]
    
    ![[en-us_image_0000001630585274.png]]
    
6.  Note that the key of the service output parameter must match the value of **Name** for the form element component so that the data can be displayed. For example, the value of the service output parameter **name** can be displayed only when **Name** of the **Text Input** component is **name**.
    
    ![[en-us_image_0000001679144749.png]]