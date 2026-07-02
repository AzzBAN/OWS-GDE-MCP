---
title: "Error Codes"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_156.html"
depth: 6
---
#### Procedure (Error Code Definition)

1.  Select **Inbound API** or **Outbound API** as required and click **Develop APIs**.
2.  Go to the **Public Definition** tab page.
    
    Click **Public Definition** on the API Builder page. The **Variable Definition** page is displayed by default.
    
    **Figure 1** Accessing the Common Definition page  
    ![[en-us_image_0000001584969464.png]]
    

3.  Go to the **Error Code Definition** page.
    
    In the navigation pane, choose **Error Code > Error Code Definition**.
    
4.  Add a source error code category.
    
    ![[note_3.0-en-us.png]]
    
    The source error code is used for error code information returned by the API Fabric or third-party system.
    
    The error code group **GatewayInner** of the API Fabric in O&M state is embedded in the tool.
    
    Choose **Source** and click ![[en-us_image_0313201870.png]] next to the catalog. In the dialog box that is displayed, enter the source name and click **Confirm**.
    
5.  Add a source error code.
    
    1.  Select the category to which the source error code belongs and click **Add**.
        
        Enter the error code name, description, and error details as prompted.
        
    2.  Click **Confirm**.
    
6.  Add a target error code category.
    
    ![[note_3.0-en-us.png]]
    
    The target error code is defined by the service side and is an error code that can be identified by the service side.
    
    Choose **Target** and click ![[en-us_image_0313203774.png]] next to the catalog. In the dialog box that is displayed, enter the target name and click **Confirm**.
    
7.  Add a target error code.
    
    1.  Select the category to which the target error code belongs and click **Add**.
        
        Enter the error code name, description, and error details as prompted.
        
    2.  Click **Confirm**.