---
title: "Hidden"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001734969792.html"
depth: 5
---
# Hidden

Note: Data that does not need to be displayed to users. The Hidden component supports **#Get\[task\_id\]** and **#Sys** expressions, but does not support **#Form**.

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Id | Component ID |
| Name | Name |
| Need Submit | Whether submission is required. The value is of the Boolean type. The default value is false. |
| Value | Value to be hidden. You can enter the default value of the component. | **APIs**

**getValue**

Input parameters: none

Output parameters: String

Description: Obtain the hidden value.

Example:

C("hidden1").getValue(); // **hidden1** indicates the component ID.

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]