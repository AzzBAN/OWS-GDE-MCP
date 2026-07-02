---
title: "Date"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001734962852.html"
depth: 5
---
# Date

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Format | Date format, for example, yyyy/MM/dd. The format character string must contain yyyy,MM,dd. |
| Label | Component label |
| Name | Component name |
| Read Only | Whether the component is read-only |
| Show Current Time | Whether to display the current date during initialization |
| Value | Initial value of the component |
| Visible | Visibility condition |
| Width | Component width |
| Required | Whether the component is mandatory | **APIs**

**setValue()**

Input parameters: String. The value must be in the format of "yyyy-mm-dd".

Output parameters: none

Description: Set the value.

Example:

C("a").setValue("2018-06-13")

**getValue()**

Input parameters: none

Output parameters: String

Description: Obtain the value.

Example:

C("a").getValue()

**getFormatValue()**

Input parameters: none

Output parameters: String

Description: Obtain a value in the format of "yyyy-mm-dd".

Example:

C("a").getFormatValue()

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]