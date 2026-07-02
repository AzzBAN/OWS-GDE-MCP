---
title: "Authentication"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_050.html"
depth: 8
---
#### Procedure

1.  Choose **Access Control** > **Authentication Mode** and select an authentication mode.
    
    Choose **API-Level Policy** or **API Method-Level Policy** based on the configuration granularity. The following authentication modes are supported:
    
    ![[note_3.0-en-us.png]]
    
    -   If no authentication mode is selected, authentication is not required.
    -   If multiple authentication modes are selected, you can use one of them.
    
    -   OAuth 2.0
    -   HIS API
    -   GTS API
    -   GAM Authentication
    -   Username and password
        -   If **Pattern** is set to **APP**, subscribe to the API through an app in the runtime-state API Fabric and use the AK/SK for username and password authentication.
        -   If **Pattern** is set to **Basic Authentication**, select a user group based on site requirements.
        -   If **Pattern** is set to **Customize**, configure user information in the **Attribute Variables of Extension Policies** dialog box. For details, see [Configuring Attribute Variables of Extension Policies](#EN-US_TOPIC_0000001760274661__en-us_topic_0122469024_section0568131103814).
    -   OpenID
    -   AK/SK signature
        
        If this authentication mode is selected, you need to configure **Expiration Time** and **Whether the signature contains the message body**.
        
    
2.  Click **Save**.