---
title: "Toggle"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001734752202.html"
depth: 5
---
# Toggle

Note: The sub component option needs to be configured.

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Label | Component label |
| Name | Component name |
| Read Only | Whether a value can be entered |
| Value | Initial value |
| Width | Component width |
| Required | Whether the component is mandatory | **APIs**

**getValue**

Input parameters: none

Output parameters: String

Description: Obtain the initial value.

**getBeforeValue**

Input parameters: none

Output parameters: String

Description: Obtain the current value of toggle.

**setReadonly**

Input parameters: Boolean

Output parameters: none

Description: Set the component status to read-only.

Example:

C("MToggle1").setReadonly(true);

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]