---
title: "Configuring the Common Project Information"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_013.html"
depth: 4
---
#### Procedure

1.  Choose **Project Management**.
2.  On the **Project Management** page, click ![[en-us_image_0000001443517813.png]] in the **Operation** column of the created project.
3.  On the displayed page, click the **Project Settings** tab and click **Edit** on the right of **Project Information** to modify project parameters.
    
    For details about the parameters, see [[Creating a Project|Table 2]].
    
4.  Configure the project dependency. A maximum of 20 unique dependencies can be added. If a dependency is configured, the dependency will be verified in the runtime-state environment when the project is released to the runtime-state environment.
    
    ![[en-us_image_0000001510655105.png]]
    
5.  Configure an app trigger.
    
    Currently, you can specify the service to be triggered before app uninstallation. For example, an interface can be triggered to clear data. The service selected in the trigger must be at the project or public level. The service path starts with **/** or **cse://**.
    
    ![[en-us_image_0000001510655177.png]]
    
    -   Service path: **/adc-service/rest/v1/services/**_{project name}_**/**_{module name}_**/**_{service name}_, for example, **/adc-service/rest/v1/services/f\_test/OWS4ALoginService/serviceValidatea**. You can click ![[en-us_image_0000001267019856.png]] and select a service.
    -   CSE path: **cse://**_xxxx/xxxx_
    
    ![[note_3.0-en-us.png]]
    
    App triggers can be triggered only when apps are uninstalled on the **GDE App Manager** page. If you need to use the app trigger function, ensure that the trigger has been deployed on the **GDE App Manager** page in the develop-state environment. For details, see [[Configuring the Deployment Distribution Mode|Configuring the Deployment Distribution Mode]]. In the runtime-state environment, you can install and uninstall apps on the **Products and Services** > **Administration** > **Assets** > **GDE App Manager** page.
    
6.  After the configuration is complete, click **Save**.