---
title: "Count Down"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001734747286.html"
depth: 5
---
# Count Down

Note: The countdown is displayed.

Used to display the countdown value.

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Label | Component label |
| Name | Component name |
| Timeup Callback | Callback function to be executed after the countdown is complete |
| Value | Initial value of the timer |
| Visible | Element display condition |
| Align | Element alignment mode |
| Size | Component text display size | **APIs**

**getValue**

Input parameters: none

Output parameters: String

Description: Obtain the value.

Example:

C("MCountDown1").getValue()

**setValue**

Input parameters: String

Output parameters: none

Description: Set the value.

Example:

C("MCountDown1").setValue("0:0:30")

**reset**

Input parameters: none

Output parameters: none

Description: Reset the timer.

Example:

C("MCountDown1").reset()

**setCallback**

Input parameters: Function

Output parameters: none

Description: Reset the callback function.

Example:

C("MCountDown1").setCallback(function(){console.log("aaa")})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]