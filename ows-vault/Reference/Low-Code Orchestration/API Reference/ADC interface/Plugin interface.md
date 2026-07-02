---
title: "Plugin interface"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001120735552.html"
depth: 3
---
# Plugin interface

Plug-in interfaces provided by the ADC are used to customize the development mode. For details about how to use the plug-in interfaces, see the development guide for each scenario.

**Table 1** Plugin interface   
| Scenario | Name | Description |
| :-- | :-- | :-- |
| RPA customized extension | python3.8.3 system interface | See Python 3.8.5 System Library API |
| logger.info(msg) | Debug Log Interface |
| logger.warn(msg) | Debug Log Interface |
| logger.error(msg) | Debug Log Interface |
| console\_logger.info(msg) | Console Log Interface |
| console\_logger.warn(msg) | Console Log Interface |
| console\_logger.error(msg) | Console Log Interface |
| order | Action execution entry, which does not need to be invoked by users. |
| Customizing Web Page Components | index.vue | Definition file of the customized component. The definition of the vue component must be returned. |
| adcui.json | Defines the type of a user-defined component. |
| package.json | Name and version definition file of a user-defined component |
| en\_US.md | Customize the description document of the customized component in the page designer. |
| zh\_CN.md | Customize the description document of the customized component in the page designer. |
| icon.png | Displaying Icons in the Page Designer |
| adcui.json | Defines the type of a customized page. |
| package.json | Name and version definition file of the customized page |
| Customizing mobile page components | index.vue | Definition file of the customized component. The definition of the vue component must be returned. |
| adcui.json | Defines the type of a user-defined component. |
| package.json | Name and version definition file of a user-defined component |
| en\_US.md | Customize the description document of the customized component in the page designer. |
| zh\_CN.md | Customize the description document of the customized component in the page designer. |
| icon.png | Displaying Icons in the Page Designer |
| adcui.json | Defines the type of a customized page. |
| package.json | Name and version definition file of the customized page | **Parent topic:** [[ADC interface|ADC interface]]