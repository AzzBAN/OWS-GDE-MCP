---
title: "Component Methods and Events Called Through JavaScript Scripts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001316319092.html"
depth: 7
---
# Component Methods and Events Called Through JavaScript Scripts

MSPL2.0 provides 103 components. For details about the methods and events provided by each component, see the help document provided by the designer.

For details about how to view a component, move the cursor to the component and click the **API Doc** link in the lower left corner of the floating box.

![[en-us_image_0000001508302101.png]]

The following uses the on method displayed for all components under **Form** > **Data Field** as an example.

 
| Parameter | Description |
| :-- | :-- |
| event | Mandatory. Indicates the registration event to be added from the selected element. |
| function | Mandatory. Indicates the function that runs when an event occurs. | The following parameters are received: One is the name of the event to be registered, and the other is the callback function to be triggered after the event occurs. If the parameters are used in JavaScript code, refer to the following information.

//Use the C() method to transfer the component ID to obtain the component instance. Use the .on method to transfer the event name **click** and callback function **function**. When the component is clicked, the callback function is executed to record **aaa**.
C("id").on("click",function(){
  console.log('aaa')
})
C("id").on("change",function(){
  console.log('bbb')
})

**Parent topic:** [[JavaScript Scripts|JavaScript Scripts]]