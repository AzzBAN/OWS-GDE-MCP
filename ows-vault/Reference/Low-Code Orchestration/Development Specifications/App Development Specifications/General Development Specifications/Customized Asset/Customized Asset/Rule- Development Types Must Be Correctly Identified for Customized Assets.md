---
title: "Rule: Development Types Must Be Correctly Identified for Customized Assets"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123728.html"
depth: 6
---
# Rule: Development Types Must Be Correctly Identified for Customized Assets

**Description**: ADC cannot identify metadata and code types of customized assets because they are not orchestrated by ADC. The asset management and control feature mapped to ADC is closely related to the development types. Incorrect development type configuration may cause quality defects. The following table defines the currently supported development types.

 
| Development Type | Description |
| :-- | :-- |
| No Code | Assets are developed through drag-and-drop operations and attribute configurations, for example, model ER diagram design and page development through drag and drop. |
| Low Code | Assets are developed by compiling scripts (usually using JavaScript and Python languages encapsulated by the platform) to customize services within the system restrictions. For example, if service development cannot be completed by drag-and-drop operations, simple JS scripts need to be compiled. |
| Pro Code | Resources, engineering capabilities, and the running environment provided by the system are used to develop complex service logic with the native coding language to implement asset development. Assets developed in Pro Code mode are used to start independent processes or are directly executed based on the OS or container. Assets developed in No Code/Low Code mode usually exist in the main process of the ADC system. The following has been determined to use the Pro Code development mode:
1.  Custom frontend pages and components (implemented based on UI Pro Code CLI)
2.  Python tool Note: Currently, the Python tool does not provide full-function capabilities. It restricts local resource access, network access, and system API calling, and is started through the main process during execution. Before full-function capabilities are provided, the Low Code development mode is used.
3.  Code snippets based on the FaaS technology
4.  Microservices developed based on CommonSDK

 | **Check guide**: Check whether the development types of the customized assets are the same as those of the uploaded asset files.

**Positive example**: A proper development type is configured for the customized asset type.

**Negative example**: No proper development type is configured for the customized asset or the configuration is incorrect.

**Tool supported or not**: no

**Specification name**: General\_Custom\_Correctly\_Identify\_the\_Code\_Type

**Severity**: major

**Parent topic:** [[Customized Asset|Customized Asset]]