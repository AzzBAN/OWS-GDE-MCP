---
title: "Contacts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_006.html"
depth: 4
---
#### Orchestration Procedure

1.  Drag a **Form Panel** component, and drag a **Contacts** component under **Data Fields**.
    
    ![[en-us_image_0000001614112914.png]]
    
2.  Configure the interface.
    
    ![[en-us_image_0000002159388542.png]]
    
    The following figure shows the data returned by the interface.
    
    ![[en-us_image_0000001662632845.png]]
    
    The fields include **fullname**, **im\_count**, **telephone**, and **contact\_state**. However, these fields are not required by the component. You need to use the **Configure Service Output** property to map the service output fields with the fields required by the component.
    
    The default fields are displayed on the left, and the interface-created fields are displayed on the right.
    
    ![[en-us_image_0000001613953010.png]]
    
3.  Configure the phone number of a contact in the phone number property area. The primary key **contact\_id** is used to associate with a single contact and obtain the phone number of the contact.
    
    ![[en-us_image_0000001662513017.png]]
    
    ![[en-us_image_0000001613952982.png]]