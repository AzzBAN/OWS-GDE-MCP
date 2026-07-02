---
title: "Proxy Mode"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001582721449.html"
depth: 7
---
#### Procedure (Outbound API/Inbound API)

1.  Choose **Development State Studio** > **Inbound API/Outbound API** > **Develop API**.
2.  Add an API.
    
    1.  Choose **Create** > **Create API**. The **Basic Information** page is displayed.
    2.  On the **Basic Information** page, select a creation mode as required.
        -   **File Upload**
            
            Import the definition file as prompted.
            
            After the import, **API Name** and **Protocol** are automatically set.
            
        -   **WEBSOCKET**
            
            After **WEBSOCKET** is selected, **Protocol** is automatically set. You do not need to upload the definition file. The WebSocket protocol does not support orchestration.
            
            The maximum length of a single frame in a WebSocket packet is 65535 bytes.
            
    3.  Select the API file to be uploaded, and click **Proxy Mode** in **Orchestration Mode**.
        
        ![[note_3.0-en-us.png]]
        
        -   You can select **Proxy Mode** only after uploading the definition file.
        -   If you select **Proxy Mode** when adding an API, an endpoint is automatically generated after the file is uploaded. The endpoint belongs only to the API and is not displayed on the **Endpoint Management** page.
        -   You need to modify the endpoint URL in the API editing menu, or modify the endpoint URL in the governance state after deploying the API.
        
    4.  Click **Confirm**.
    
3.  Configure the proxy.
    
    1.  On the **Develop API** page, click the imported API. The **Proxy Configuration** tab page is displayed.
    2.  Perform the configuration by referring to [[Orchestration|Orchestration]] only after you disable **Bypass**, as shown in [Figure 1](#EN-US_TOPIC_0000001582721449__en-us_topic_0000001143049513_en-us_topic_0000001143049513_fig16568731115619).
        
        **Figure 1** Proxy configuration
        
        ![[en-us_image_0000002450613094.png]]
        
    
    ![[note_3.0-en-us.png]]
    
    For an outbound API, only the **Post** method can be selected. The method path is in the format of _Protocol type_ + _Project name_ + _Module name_ + _API name_, for example, **/rest/XXX/xxx/API**.
    
    3.  After the configuration is complete, click **Save**.