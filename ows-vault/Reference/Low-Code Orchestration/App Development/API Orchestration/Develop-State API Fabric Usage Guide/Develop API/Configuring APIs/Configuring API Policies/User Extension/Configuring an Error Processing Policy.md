---
title: "Configuring an Error Processing Policy"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_067.html"
depth: 8
---
#### Procedure

1.  Choose **User Extensions** > **Error Handling**.
2.  Configure error codes.
    
    -   **Gateway error code mapping**
        
        The API Fabric error code is used to preset the error code in the runtime state for error code mapping when an internal error occurs in the API Builder.
        
        1.  In the **Error Code Mapping Rule** column, select the defined error code mapping name from the drop-down list.
        2.  In the **Error Code Returned When No Mapping Is Found** column, select the list return code from the drop-down list. The information in the drop-down list is automatically displayed in the text box.
        
    -   **Endpoint error code mapping**
        
        If only the service name is entered, the error code is mapped for the entire service. If both the service name and method are entered, the error code is mapped to the method.
        
        1.  On the **Error Handling Strategy** tab page, enter the endpoint error code mapping.
            
            Click **Add** and configure the endpoint error code mapping. [[Configuring an Error Processing Policy|Table 1]] describes the parameters.
            
        2.  Select the service name and method of the endpoint and define the path of the error code.
        3.  In the **Error Code Group** column, click the text box and select an existing common error code group.
        4.  In the **Error Code Mapping Rule** column, click the text box and select an existing common error code mapping rule.
        5.  In the **Error Code Returned When No Mapping Is Found** column, select the defined return code for the endpoint error code mapping.
            
            **Table 1** Endpoint error code parameters  
            | Parameter | Description |
            | :-- | :-- |
            | Service Name | (Mandatory) Endpoint name. |
            | Method | Name of the method called by the endpoint. |
            | Error Code Path | (Mandatory) Error code path. The parameter is specified by the JSONPath and needs to be extended. |
            | Error Code Description Path | Path for storing error code information. The parameter is specified by the JSONPath and needs to be extended. |
            | Code Details Path | Path for storing error code details. The parameter is specified by the JSONPath and needs to be extended. |
            | Error Code Group | Error code group. |
            | Error Code Mapping Rule | Error code mapping rule. |
            | Error Code Returned When No Mapping Is Found | Information defined and returned if no error code is returned. | -   **API error response**
        
        The API error code structure can be configured for the API error response.
        
        1.  In the **Error Code Path** column, enter the error code path.
        2.  In the **Error Code Description Path** column, enter the error code description path.
        3.  In the **Code Details Path** column, enter the error code details path.
    
3.  Click **Save**.