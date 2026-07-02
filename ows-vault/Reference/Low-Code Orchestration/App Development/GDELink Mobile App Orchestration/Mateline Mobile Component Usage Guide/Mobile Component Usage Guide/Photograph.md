---
title: "Photograph"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001733925888.html"
depth: 5
---
# Photograph

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| ID | Component ID |
| Label | Component label |
| Name | Component name |
| NeedSubmit | Whether the component can be submitted with the form. The value can be true or false. |
| Parameters | Service request parameter in JSON format. The default parameters are task\_id, group, and module. task\_id and group are mandatory. |
| Quality | The options are 1024 \* 768, 640 \* 480, 320 \* 240, and 160 \* 120. The default value is null. |
| Read Only | Whether the component is read-only. The value can be true or false. |
| EnableSystemPhotoSelection | Whether the system album can be selected. true indicates that the system album can be selected, and false indicates that the system album cannot be selected. |
| Value | Default |
| Visible | Whether the control is visible. A TQL expression is supported. You can determine whether to display the control based on the values of other controls. |
| Watermark | Watermark display condition, which is a TQL statement text box. For example, to display the current geographic information, set this parameter to location:#Sys\[location\]. To display the current time, set this parameter to time:#Sys\[localtime\]. To display geographical locations, set location\_gather\_enable to true on the mobilemarket\_config\_grid page in the mobilemarket.app file to allow location information collection. |
| WaterMarkText bold | Whether the watermark text is bold. The value is true or false. |
| WaterMarkColor | Watermark color |
| WaterMarkText Size | Watermark text font size |
| Cache Key | After the configuration, photos can be displayed based on the cache key. You can use #Get to set dynamic parameters, for example, #Get\[orderid\]. In this way, the caches of different photographing components can be distinguished. | APIs

**isRequired**

Input parameters: none

Output parameters: Boolean

Description: Determine whether the component is mandatory.

Example:

C("id").isRequired();

**setParameters**

Input parameters: **taskId**, **group**, and **item**

Output parameters: none

Description: Set the **taskId**, **group**, and **item** parameters of the component.

Example:

C("id").setParameters(taskId,group,item);

**getValue**

Input parameters: **taskId**, **group**, and **item** of the component to be obtained

Output parameters: **taskId**, **group**, and **item**

Description: Set the **taskId**, **group**, and **item** parameters of the component.

**getPictureNum**

Input parameters: none

Output parameters: Number

Description: Obtain the number of photos.

**setReadonly**

Input parameters: Boolean

Output parameters: none

Description: Set the component status to read-only.

**getPhotoDetail**

Input parameters: Function

Output parameters: none

Description: Call the callback function after obtaining the component details.

**FAQs**

Scenarios

1\. Take photos with watermarks, including the current location information and time.

Example: link to mobile\_sample

2\. Users can select photos from the system album.

Example: link to mobile\_sample

**Precautions**

When the location information needs to be displayed, you need to configure the parameter to specify whether the mobile allows the location information collection.

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]