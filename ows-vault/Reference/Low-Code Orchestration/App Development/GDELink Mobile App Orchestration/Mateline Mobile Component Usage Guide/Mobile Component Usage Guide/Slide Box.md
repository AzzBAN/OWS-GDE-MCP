---
title: "Slide Box"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731723342.html"
depth: 5
---
# Slide Box

**Functions**

This component is an image rotation component. You can configure services to obtain image information or configure static image components.

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001731723342__table4221mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:31%"> <col style="width:69%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001731723342__row4226mcpsimp"><td class="cellrowborder" valign="top" width="31%">Property Name</td><td class="cellrowborder" valign="top" width="69%">Description</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4231mcpsimp"><td class="cellrowborder" valign="top" width="31%">Auto Play</td><td class="cellrowborder" valign="top" width="69%">Whether to enable automatic play</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4236mcpsimp"><td class="cellrowborder" valign="top" width="31%">Use Cache Data</td><td class="cellrowborder" valign="top" width="69%">Whether to use cached data</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4241mcpsimp"><td class="cellrowborder" valign="top" width="31%">Image Description Field</td><td class="cellrowborder" valign="top" width="69%">When an image is dynamically configured, a field of the service is specified as an image description field.</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4246mcpsimp"><td class="cellrowborder" valign="top" width="31%">Image Label Field</td><td class="cellrowborder" valign="top" width="69%">When an image is dynamically configured, a field of the service is specified as an image label field.</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4251mcpsimp"><td class="cellrowborder" valign="top" width="31%">Image Link Parameters Field</td><td class="cellrowborder" valign="top" width="69%">When an image is dynamically configured, a field of the service is specified as the parameter field carried during image switching.</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4256mcpsimp"><td class="cellrowborder" valign="top" width="31%">Image Location Field</td><td class="cellrowborder" valign="top" width="69%">When an image is dynamically configured, a field of the service is specified as the redirection location field carried during image switching.</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4261mcpsimp"><td class="cellrowborder" valign="top" width="31%">Image URL Field</td><td class="cellrowborder" valign="top" width="69%">Field configured as the image direction URL field, which is returned by the service.</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4266mcpsimp"><td class="cellrowborder" valign="top" width="31%">Label</td><td class="cellrowborder" valign="top" width="69%">Component label</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4271mcpsimp"><td class="cellrowborder" valign="top" width="31%">Name</td><td class="cellrowborder" valign="top" width="69%">Component name</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4276mcpsimp"><td class="cellrowborder" valign="top" width="31%">Service ID</td><td class="cellrowborder" valign="top" width="69%">ID of the service that dynamically obtains image information</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4281mcpsimp"><td class="cellrowborder" valign="top" width="31%">Service Parameters</td><td class="cellrowborder" valign="top" width="69%">Service input parameter</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4286mcpsimp"><td class="cellrowborder" valign="top" width="31%">Show Pager</td><td class="cellrowborder" valign="top" width="69%">Whether to display the bottom tab</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4291mcpsimp"><td class="cellrowborder" valign="top" width="31%">Visible</td><td class="cellrowborder" valign="top" width="69%">Component visibility condition</td></tr><tr id="EN-US_TOPIC_0000001731723342__row4296mcpsimp"><td class="cellrowborder" valign="top" width="31%">Style</td><td class="cellrowborder" valign="top" width="69%">Custom component style. name corresponds to the property, and value corresponds to the property value.</td></tr></tbody></table>

**APIs**

N/A

**Events**

**dataLoaded**

Description: The event is triggered after data loading is complete.

Example:

C("id").on("dataLoaded",function(json){

//do something

})

**FAQs**

Scenarios

1\. Configure static images. The sub component of Slide Box is image. You can drag the image component to **images** of the slide box.

Example: link to mobile\_sample

2\. Configure a service to obtain images.

Example: link to mobile\_sample

**Precautions**

If the static images and service are configured at the same time, the images returned by the service are used.

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]