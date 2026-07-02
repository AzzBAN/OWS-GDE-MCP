---
title: "Orchestration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001532041506.html"
depth: 7
---
#### Procedure

An API method can call one or more southbound services.

The process orchestration complies with [BPMN 2.0 specifications](https://www.omg.org/spec/BPMN/2.0/). For details about the diagram elements, see [[Diagram Elements|Diagram Elements]].

1.  Select the method to be orchestrated in the **Method** column on the left.
2.  Add a diagram element.
    
    Drag diagram elements from the diagram element panel to the editing area based on the process design requirements.
    
    For example, if the method to be orchestrated needs to call a SOAP southbound service and then a REST southbound service, drag the SOAP diagram element and then drag the REST diagram element.
    
    ![[note_3.0-en-us.png]]
    
    To delete an added diagram element, select the diagram element and press **Delete**.
    
3.  Connect a diagram element.
    
    Select a connection line based on the process design requirements.
    
    ![[note_3.0-en-us.png]]
    
    To delete an added connection, select the line and press **Delete**.
    
    1.  Click the connection line in the diagram element panel.
    2.  Move the pointer to the start diagram element to be connected in the diagram element orchestration area.
        
        When the cursor changes to **+**, many connection points are displayed on the diagram element.
        
    3.  Click any connection point.
    4.  Drag to any connection point of the target diagram element, and click the connection point.
    
4.  Create a mapping between services and data.
    
    1.  Double-click the diagram element to be orchestrated and select the service and method to be called.
        
        ![[note_3.0-en-us.png]]
        
        In the integrated orchestration scenario, when selecting the service to be called for the REST protocol, you can click **Select service**. In the **Search Service** window, search for and select a service in **Service** or **API Catalog** as prompted.
        
        The logic flow corresponds to **Service** on the menu, and the API catalog is the API on the page displayed after you choose **Asset Management** > **Service Category**.
        
    2.  Click the **Request** tab in the **Advanced Parameters** area, map the data based on the actual relationship, and click **Save**.
    3.  Click the **Response** tab in the **Advanced Parameters** area, map the data based on the actual relationship, and click **Save**.
        
        Response parameters of the endpoint are displayed on the left. Response parameters of the API are displayed on the right.
        
    
    ![[note_3.0-en-us.png]]
    
    -   You can name diagram elements to understand the entire service process on the process orchestration page.
    -   Click the automatic matching button. When the parameters in the source and target objects are consistent, the parameters are automatically associated.
    -   If you move the cursor to ![[en-us_image_0129694032.png]], a message is displayed. You can view the displayed data mapping.
        
        The API Fabric displays the message based on the parameter type in the definition file, but does not perform any logic processing. JavaScript is a loosely-typed language. You can use the auxiliary function Numbertils for type conversion based on site requirements.
        
        For example, if the called API performs strong verification for the parameter type, special processing is mandatory. If the input parameters do not affect the status, no special processing is required.
        
    -   You can click ![[en-us_image_0122469046.png]] of the target parameter to set the function.
    -   After the configuration is complete, you can click the non-configuration area of the diagram element to return to the **Process Orchestration** page.
    -   The response parameters of the previous diagram element are displayed on the request parameter page of the next diagram element. If multi-level connected diagram elements exist, the response parameters of all upper-level diagram elements are displayed on the request parameter page of the current diagram element.