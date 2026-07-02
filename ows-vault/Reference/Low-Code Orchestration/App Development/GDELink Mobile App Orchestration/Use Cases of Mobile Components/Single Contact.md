---
title: "Single Contact"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_005.html"
depth: 4
---
#### Orchestration Procedure

1.  Drag a **Form Panel** component, and drag a **Single Contact** component under **Data Fields**.
    
    ![[en-us_image_0000001613771128.png]]
    
    ![[note_3.0-en-us.png]]
    
    Set **Primary Key**, **fullName**, **role**, **telephone**, and **state** to the fields corresponding to the data returned by the interface. If **fullName** is empty, the component is not displayed.
    
2.  Configure the component properties.
    
    ![[en-us_image_0000002159350332.png]]
    
    -   The configured test interface is **test\_single\_contact\_get**.
    
    ![[en-us_image_0000001614112834.png]]
    
    -   The input parameters of the interface are as follows:
        
        ![[en-us_image_0000002159353856.png]]
        
    -   The actual result returned by the service is as follows:
        
        ![[en-us_image_0000001613792898.png]]
        
        ![[notice_3.0-en-us.png]]
        
        The keys of the parameters returned by the service match those in the property configuration.
        
    
3.  **Phone API** is provided for making calls. Click the dial button. This interface is called to obtain the phone number of the corresponding contact based on the primary key.
    
    -   Use the preceding service as an example:
        
        ![[en-us_image_0000002194555401.png]]
        
        ![[en-us_image_0000001662672761.png]]
        
    
    After you click the phone icon, the preceding service is called to obtain the returned information. Then, the phone information is found based on the value of **contact\_id** for number dialing.