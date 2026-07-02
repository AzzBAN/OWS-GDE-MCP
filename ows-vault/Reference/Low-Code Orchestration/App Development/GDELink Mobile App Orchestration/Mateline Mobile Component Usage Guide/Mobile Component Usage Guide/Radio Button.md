---
title: "Radio Button"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001781847569.html"
depth: 5
---
# Radio Button

Note: The sub component option needs to be configured.

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Label | Component label |
| Name | Component name |
| Read Only | Whether the component is read-only |
| Value | Initial value |
| Visible | Component display condition |
| Width | Component width |
| Required | Whether the component is mandatory | **APIs**

**getValue**

Input parameters: none

Output parameters: String

Description: Obtain the value.

Example:

C("MRadioButton1").getValue();

**isRequired**

Input parameters: none

Output parameters: Boolean

Description: Determine whether the component is mandatory.

Example:

C("MRadioButton1").isRequired();

**getSubmitValue**

Input parameters: none

Output parameters: String

Description: Obtain the nested values of each layer of the component.

Example:

C("MRadioButton1").getSubmitValue();

**setValue**

Input parameters: String

Output parameters: none

Description: Set the value.

Example:

C("MRadioButton1").setValue("ok");

**setReadonly**

Input parameters: Boolean

Output parameters: none

Description: Set the component status to read-only.

Example:

C("MRadioButton1").setReadonly(true)

**getDirectDisplayChildDataField**

Input parameters: none

Output parameters: JSON

Description: Obtain the level-1 subcomponent of the selected item.

Example:

// Obtain the level-1 subcomponent of the selected item.

C("MRadioButton1").getDirectDisplayChildDataField();

// Obtain all subcomponents.

C("MRadioButton1").getChildDataField();

// Obtain all subcomponents of the selected item.

C("MRadioButton1").getVisibleChildDataField()

**Events**

**valueChanged**

Description: value change event

Example:

C("id").on("valueChanged",function(){

console.log("xxx")

})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]