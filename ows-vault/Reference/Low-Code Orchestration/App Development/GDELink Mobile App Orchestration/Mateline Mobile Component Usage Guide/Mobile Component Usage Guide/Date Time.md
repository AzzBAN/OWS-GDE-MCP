---
title: "Date Time"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001781868997.html"
depth: 5
---
# Date Time

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Format | Date format, for example, hh:mm:ss yyyy/MM/dd. The value must contain hh,mm,ss,yyyy,MM,dd. |
| Label | Component label |
| Local To Utc | Whether to convert the return value of getValue to UTC time |
| Minute Step | Interval for increasing or decreasing a minute when you click the up or down button on the time selection page |
| Name | Component name |
| Read Only | Whether the component is read-only |
| Second Step | Interval for increasing or decreasing a second when you click the up or down button on the time selection page |
| Show CurrentTime | Whether to display the current date during initialization |
| Show Second | Time display accuracy to second |
| Value | Initial value of the component |
| Visible | Visibility condition |
| Width | Component width |
| Required | Whether the component is mandatory | **APIs**

**setValue()**

Input parameters: String. The value must be in the format of "yyyy-mm-dd _xx_:_xx_:_xx_".

Output parameters: none

Description: Set the value.

Example:

C("a").setValue("2018-06-13 10:54:13")

**getValue()**

Input parameters: none

Output parameters: String

Description: Obtain the value. If **localToUtc** is set to **true**, a UTC time is obtained.

Example:

C("a").getValue()

**getText()**

Input parameters: none

Output parameters: String

Description: Obtain the display value.

Example:

C("a").getText()

**getFormatValue()**

Input parameters: none

Output parameters: String

Description: Obtain a value in the format of "yyyy-mm-dd hh:mm:ss".

Example:

C("a").getFormatValue()

**isVisible()**

Input parameters: none

Output parameters: Boolean

Description: Determine whether a component is visible.

Example:

C("a").isVisible()

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]