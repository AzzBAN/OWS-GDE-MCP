---
title: "Adding a Common Definition of an API or Endpoint"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_147.html"
depth: 5
children: ["Variable Definition", "Dictionary Value Mapping", "Key Management", "User Group Management", "Common Function", "Common Structures", "Common Process", "Common Error Handling Policy", "Error Codes", "Common Policy", "Importing or Exporting Common Assets"]
---
#### Overview

The configuration items defined on the **Public Definition** page are global variables. [Table 1](#EN-US_TOPIC_0000001569107025__en-us_topic_0122468685_table1455284514574) describes the configuration items.

**Table 1** Configuration items on **Public Definition**  
| Configuration Item | Description |
| :-- | :-- |
| Variable Definition | Used for centralized configuration and management of project-level common variables (shared with all APIs in a project), obtaining environment information and cross-API shared configuration during the API development. After common variables are set, you can enter ${ to associate them when defining APIs or adding southbound endpoints. |
| KV Mapping | Used to manage mappings at different sites to meet the requirements. After being set, the configuration item can be used during API development. |
| Key Management | Used to obtain a decrypted field of a service during API orchestration. After being set, the configuration item can be used during API definition. |
| User Management | Used to manage users and passwords by a user group in a unified manner. After the configuration item is set, user groups can be associated during API development. If authentication is configured in the API test or application, the system searches for the corresponding username and password from the associated user group. If the matching is successful, the authentication is successful. Otherwise, the authentication fails and invalid users are intercepted. |
| Public Function | JavaScript function used in the policy such as the process orchestration or responsibility chain (such as flow control, authentication, and data mapping). Common functions can be defined to prevent repeated definition of functions. The common functions defined here are global functions and are used by all APIs of a project. |
| Public Structure | The configuration item is used to centrally manage the parameter structures that are referenced across APIs in the northbound API definition. The common structures defined in the Investigator tool and Builder tool can be shared. A common structure is included when the API that references the common structure is exported. Currently, the Builder tool supports only the common structure of the REST protocol. After the definition, for REST APIs, common structures can be directly referenced in the API definition to meet users' requirements for reusing common structures across APIs. |
| Public Process | You can define the southbound service orchestration process of an endpoint as a common process to implement process reuse. The process nesting is not supported currently. |
| Public Error Handling Strategy | The configuration item is used to define a common error response so that the service side can notify the tool platform of the error response structure for the platform to obtain and construct error objects. When handling an exception message, the API running engine constructs an exception message based on the exception message format defined in the API policy and returns the message. |
| Error Code | The configuration item is used to set the common error code for multiple APIs. |
| Public Policy | The configuration item is used to configure a common policy for multiple APIs. Currently, only the API-level common policy can be referenced. | The configuration on the **Common Definition** tab page can be used for common asset import or export. The structure of the import or export package is shown in [Figure 1](#EN-US_TOPIC_0000001569107025__en-us_topic_0122468685_fig1916254873615).

-   **source\\config**: stores the common definition file.
-   **js**: stores the common script.
-   **.mf**: asset signature list file, including the file directory and hash value corresponding to the file.
-   **.cms**: signature file generated after the .mf file is digitally signed.
-   **.package**: description file, which is used to identify the package type when a package is imported to the Governance portal.

**Figure 1** Common asset package structure  
![[en-us_image_0295071646.png]]

![[note_3.0-en-us.png]]

-   For information security, **Key Management** and **User Management** in the exported asset package are unavailable. You need to set them again after the API is deployed.
-   The exported asset package does not contain common structure information. The common structure information needs to be exported separately.

## Sub-topics

- [[Variable Definition]]
- [[Dictionary Value Mapping]]
- [[Key Management]]
- [[User Group Management]]
- [[Common Function]]
- [[Common Structures]]
- [[Common Process]]
- [[Common Error Handling Policy]]
- [[Error Codes]]
- [[Common Policy]]
- [[Importing or Exporting Common Assets]]
