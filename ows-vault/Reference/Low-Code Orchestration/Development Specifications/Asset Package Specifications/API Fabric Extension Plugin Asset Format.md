---
title: "API Fabric Extension Plugin Asset Format "
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001491447684.html"
depth: 3
---
#### Extension Plug-in Asset Package Description

The following table lists an example of the aspect plugin package.

**Table 1** Extension Plugin Asset Package Format  
| Directory | Description |
| :-- | :-- |
| plugin.zip | Overall software package |
| |-lib | Stores the Jar compiled by the extended protocol Adaptor. The name of lib can be changed based on service habits. If there are two or more JAR packages, compress them into a ZIP package and put the ZIP package to the lib directory. |
| |-definition.yaml | Definition file. Describes information about the extended aspect, such as the name, version number, aspect name, API policy, and endpoint policy of the extended aspect plug-in. |
| |-Package.mf.cms | Signature File | The format and description of the definition.yaml file are as follows:

**Table 2** Extension policy file class **definition.yaml**     
| Key Field | Description |
| :-- | :-- |
| name | Plug-in name, which must be unique together with version. |
| version | Plugin version. |
| visible | (Optional) Visibility of the plug-in package after being archived to Catalog. The default value is public, indicating that the plug-in is visible to all tenants. Currently, other values cannot be set. |
| type | Specifies the type of an extended package.
-   adaptor: protocol adapter
-   aspect: aspect

 |
| image | Optional. This parameter is used only for the display image of the plug-in on the catalog. |
| description | Description of the plug-in, which is displayed only on the GUI. A configuration example is as follows.

description:
  zh: ""
  en: ""

 |
| dependency | Version of API Fabric that the plugin depends on, which is the same as that in the pom.xml file of the project during aspect development. |
| aspect | \- | Asset information about the plugin. |
| metadata | Server protocol type, which is the same as that declared in com.huawei.fabric.access.adaptor.server.TcpServer. |
| config | \- | Describes information about user-extended aspects in the JAR package, including the API policy, endpoint policy, and interceptor. One or more of them can be included during development. |
| chains | \- | Describe the responsibility chain. The YAML file can contain both api and endpoint, or only one of them. |
| api | Information about the API aspect. Multiple API aspects can be configured.

-   **name** Aspect name, which is the same as the annotation name in the aspect implementation class.
-   **description** Aspect description in Chinese and English.
-   **properties** The following is an example of the aspect configuration. After the configuration, the value of value can be changed on the API Portal or API Development Tool.
    
    properties:
                - key: "key1"
                  value: "value1"
                - key: "phoneNumber"
    
    //If sensitive information is contained, add the following configuration. The value of **value** is displayed as **\*** on the GUI. If this parameter is not set, the information is not sensitive by default.
                  allowShow: false  
                  value: ""
    
-   **tables** The aspect configured in the table format has the same function as the properties.
    
    tables:
            **#table name**
            tb1:
             ** #table column information**
              columns:
                - column: "username"
                - column: "age"
                - column: "sex"
                - column: "pass"
                  allowShow: false
              **#table row information**
              rows:
                - username: "aaa"
                  age: 18
                  sex: "male"
                - username: "bbb"
                  age: 22
                  sex: "femal"  
    
-   **pre** Location of the aspect in the API responsibility chain.
    -   owner Aspect owner, including sys (API Fabric preset aspect) and user (user extended aspect).
    -   phase Phase to which an aspect belongs, including access, mediation, and forward.
    -   category Preset aspect category. For details, see Data Zone Configuration > Data Zone Configuration (default Tenant) > API Integration (API Fabric) > Common Definition > Importing Extension Policies in GDE x.x.x Product Documentation.
-   **scope** Application scope of the aspect:
    -   global: global application, that is, the application is applied to all published APIs.
    -   partial: Only the APIs configured with this aspect are applied. APIs of the application aspect are configured using the API development tool.

 |
| endpoint | Information about the endpoint aspect. The fields and meanings are the same as those of api, but the value of the pre/phase field must be mediation. |
| interceptors | (Optional, not recommended) Endpoint interceptor, which is customized for historical versions and is used to be compatible with historical versions. This item can be deleted in other versions. |