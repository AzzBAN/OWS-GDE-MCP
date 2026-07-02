---
title: "Data Grid"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_022.html"
depth: 4
---
#### Orchestration Procedure

1.  Drag a **Data Grid** component to the component tree.
    
    ![[en-us_image_0000001679123057.png]]
    
2.  Set **Interface** to a GetList service.
    
    ![[en-us_image_0000001630883364.png]]
    
    The service return results are as shown in the following figure.
    
    ![[en-us_image_0000001679003185.png]]
    
3.  Set **Parameters** to values in the following figures.
    
    ![[en-us_image_0000001630883360.png]]
    
    ![[en-us_image_0000001679203341.png]]
    
    Configured parameters are transferred as service input parameters.
    
    ![[en-us_image_0000001630723448.png]]
    
4.  Set **Direction** to **vertical**.
    
    ![[en-us_image_0000001679123045.png]]
    
    **Direction** specifies the sorting direction of table columns. The options are **vertical** and **horizontal**.
    
    ![[en-us_image_0000001630563520.png]]
    
    ![[en-us_image_0000001679203349.png]]
    
5.  Set **Align** to **Left**.
    
    ![[en-us_image_0000001481444912.png]]
    
    **Align** specifies whether the text in the table column is left-aligned, centered, or right-aligned.
    
    ![[en-us_image_0000001679003189.png]]
    
    ![[en-us_image_0000001630403696.png]]
    
    ![[en-us_image_0000001679203337.png]]
    
6.  Drag a **Column** component to the **Column** component and set **Data Index** to the name returned by the service to view the actual table configuration effect.
    
    ![[en-us_image_0000001630563524.png]]
    
7.  After the preceding configurations are complete, click **Preview**. The list data is vertically aligned to the left.
    
    ![[en-us_image_0000001630883376.png]]