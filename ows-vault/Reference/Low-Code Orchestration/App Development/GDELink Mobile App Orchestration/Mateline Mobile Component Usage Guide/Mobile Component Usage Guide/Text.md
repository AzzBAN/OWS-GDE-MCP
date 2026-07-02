---
title: "Text"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001782309261.html"
depth: 5
---
# Text

This component can be used to display the link type, phone number type, time type, and text type.

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Label | Component label |
| Link Parameters | Parameters carried in the click-to-redirect request |
| Link To | Page that is redirected to |
| Name | Component name |
| Text | Display text content |
| UTC To Local | Whether to convert the local time if the value is of the time type |
| Visible | Visibility condition |
| Align | Alignment mode |
| Icon | Icon in front of the text |
| Icon Color | Icon color |
| Size | Font size |
| Width | Component width | **APIs**

**setValue(value)**

Input parameters: String

Output parameters: none

Description: Set the value.

Example:

C("compId").setValue("aaa");

**getValue()**

Input parameters: none

Output parameters: String

Description: Set the value.

Example:

C("compId").getValue();

**Events**

**click**

Description: click event

Example:

C("id").on("click",function(){

//do something

})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]