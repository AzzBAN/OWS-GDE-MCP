---
title: "API Fabric Contract Asset Format "
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001542287769.html"
depth: 3
---
# API Fabric Contract Asset Format

-   **Schema file naming specifications**
    
    **Table 1** Schema file naming specifications   
    | Protocol | Schema File Naming Specification | Description |
    | :-- | :-- | :-- |
    | SOAP | {API name}\_{API version}.wsdl | Place the WSDL file and all XSD files used by the WSDL file in the same folder, and compress the folder and the .package file into a ZIP package. The following figure shows the ZIP package structure. |
    | REST | 
    -   **Cloud Service Engine (CSE) scenario**
        -   In the common CSE scenario, the name format is _{Microservice name}_**\_**_{Module ID}_**.yaml**, for example, **my\_swagger\_schemaId.yaml**.
        -   In the scenario where CSE is invoked across apps, the file name must contain _App ID_. The naming format is _\[App ID\]__{Microservice name}_**\_**_{Module ID}_**.yaml**, for example, **\[appid\]microServiceName\_schemaId.yaml**.
    -   **Non-CSE scenario** The YAML file name must comply with the API naming specifications. The value can contain letters, digits, and underscores (\_), and must start with letters. The value can contain 4 to 100 characters.
    
     | The REST protocol supports the upload of a single YAML or ZIP package. The ZIP package must contain .package. The following figure shows the ZIP package structure. | -   The **type** field in the **.package** file is mandatory and must be set to **schema**.
    
    The following is an example of the **.package** file:
    
    spec: "2.0"
    packageInfo:
      type: schema
      owner: zhangsan
      timestamp: YYYYMMDD
      tag: first
    

**Parent topic:** [[Asset Package Specifications|Asset Package Specifications]]