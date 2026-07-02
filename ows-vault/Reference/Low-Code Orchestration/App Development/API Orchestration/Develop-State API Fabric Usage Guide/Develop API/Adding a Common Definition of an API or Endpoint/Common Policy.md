---
title: "Common Policy"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_157.html"
depth: 6
---
#### Procedure

1.  Select **Inbound API** or **Outbound API** as required and click **Develop APIs**.
2.  Go to the **Public Definition** tab page.
    
    Click **Public Definition** on the API Builder page. The **Variable Definition** page is displayed by default.
    
    **Figure 1** Accessing the Common Definition page  
    ![[en-us_image_0000001584969464.png]]
    

3.  Configure a policy as required.
    
    -   **Authentication**
        1.  In the navigation pane, choose **Common Policy > Authentication Mode**.
        2.  Click **Add**, enter the policy name and description, and select an authentication mode.
            
            OAuth 2.0, and username and password can be configured. For details about the authentication mode, see [[Authentication|Procedure]].
            
            Enable **Endpoint Authentication**. You can configure only the OAuth 2.0 authentication of the endpoint.
            
            ![[note_3.0-en-us.png]]
            
            On the **Endpoint Management** page, you can reference the configured southbound OAuth 2.0 authentication policy when editing an endpoint.
            
        3.  Click **Confirm**.
    
    -   **Flow control**
        1.  In the navigation pane, choose **Common Policy > Traffic Policy**.
        2.  Click **Add**, and enter the policy name, description, and flow control information.
            
            For details about flow control information, see [[Configuring the Flow Control Policy|Configuring the Flow Control Policy]].
            
        3.  Click **Confirm**.
    -   **Blacklist and whitelist**
        1.  In the navigation pane, choose **Common Policy > Black/White List**.
        2.  Click **Add** and enter the policy name and description to add one or more blacklists or whitelists.
            
            For details about IP addresses, see [[Blacklist and Whitelist|Blacklist and Whitelist]].
            
        3.  Click **Confirm**.
    -   **Dynamic parameters**
        
        Dynamic parameters are used to adjust request parameters sent to the southbound system, for example, adding parameters to the header of a request.
        
        1.  In the navigation pane, choose **Common Policy** > **Dynamic Parameters**.
        2.  Click **Add**. In the **Add Dynamic Parameters** dialog box, set parameters such as **Policy Name** and **Description**.
        3.  Click **Add** and set **Parameter Name**, **Position**, **Type**, and **Field Value**. The following table describes related parameters.
            
            ![[note_3.0-en-us.png]]
            
            If **type** is set to **Variable** or **PRESETPARAM**, the parameter is not transferred if no parameter value is obtained during calling, and the dynamic parameter content is not recorded in logs.
            
            Modifying or deleting standard HTTP headers has the following risks:
            
            -   The request may fail.
            -   Field values may fail to be modified or deleted due to the restrictions of HTTP specifications.
            
            **Table 1** Parameters  
            | Parameter | Description |
            | :-- | :-- |
            | Policy Name | Unique name of a custom dynamic parameter policy. |
            | Add |
            | Param Name | Name of a southbound parameter. |
            | Param Location | Location for storing southbound parameters after obtaining northbound parameters. The options are as follows:
            -   header
            -   query
            -   cse\_context
            
             |
            | type | Type of a northbound parameter. The options are as follows:
            
            -   **CONSTANT**
            -   **Variable**
            -   **PRESETPARAM**
            
             |
            | value | Value of a northbound parameter, which can be customized.
            
            -   If **type** is set to **Variable**, **value** can be set to **$.header.abc** or **$.query.abc**, indicating that the value named **abc** of the northbound parameter **header** or **query** is used as the value of the parameter sent to the southbound.
            -   If **type** is set to **PRESETPARAM**, **value** can be set to any of the following values:
                -   app\_key
                -   app\_name
                -   tenant\_id
                -   tenant\_name
                -   client\_ip
                -   gam\_username
            
             |
            | Delete |
            | Param Name | Name of the parameter to be deleted from the request packet sent to the southbound. |
            | Param Location | Location of the parameter to be deleted from the request packet sent to the southbound. | 4.  (Optional) Modify the policy.
    
    After a policy is configured, click **Edit** to modify the policy name or parameters.
    
5.  (Optional) Bind an API.
    
    After the policy is configured, click **Setting** and bind the policy to an API, as shown in [Figure 2](#EN-US_TOPIC_0000001569346957__en-us_topic_0132150659_fig1552017236143). After the binding is successful, you can reference the policy in the API-level policy of the API, as shown in [Figure 3](#EN-US_TOPIC_0000001569346957__en-us_topic_0132150659_fig16348159141418).
    
    **Figure 2** Binding a policy to an API  
    ![[en-us_image_0000001438935705.png]]
    
    **Figure 3** Policy reference example  
    ![[en-us_image_0000001438815893.png]]