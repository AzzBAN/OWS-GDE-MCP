---
title: "Definition of Basic Function Information"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_faas_005.html"
depth: 4
---
# Definition of Basic Function Information

The basic function information is obtained from the entry function **index.handler**. For details, see [Table 1](#EN-US_TOPIC_0000001538105765__table19813412135715).

**Table 1** Description of the Context property    
| Property | Name | Type | Description |
| :-- | :-- | :-- | :-- |
| function\_uri | Function URI | str | The format is /Project name/Module name/Function name. |
| tracker\_id | Message monitoring ID | str | Random ID, which is unique in a process that is called independently. |
| username | User name | str | Login user name for executing the function. |
| timeout | Timeout duration | int | The unit is second. The value must be the same as that configured in the function service. |
| memory | Memory | int | The unit is MB. The value must be the same as that configured in the function service. | **index.py** provides a default function example, as shown in [Figure 1](#EN-US_TOPIC_0000001538105765__fig15595103444213).

**Figure 1** index.py file  
![[en-us_image_0000001487385778.png]]

**Parent topic:** [[Pro Code SDK APIs|Pro Code SDK APIs]]