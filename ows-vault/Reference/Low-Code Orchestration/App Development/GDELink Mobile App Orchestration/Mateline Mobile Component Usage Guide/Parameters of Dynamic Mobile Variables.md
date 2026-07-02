---
title: "Parameters of Dynamic Mobile Variables"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001733877034.html"
depth: 4
---
# Parameters of Dynamic Mobile Variables

 
| Variable | Description |
| :-- | :-- |
| #Get\[xxx\] | Obtains the parameter value transferred from the URL of the current page. |
| #Sys\[xxx\] | Obtains the values of system variables provided by the system. For example, #Sys\["utc"\] is used to obtain the current UTC time. #Sys\["now"\] is used to obtain the current time. #Sys\["localtime"\] is used to obtain the current local time. #Sys\["username"\] is used to obtain the current user name. #Sys\["userinfo"\] is used to obtain the information about the current user. #Sys\["url"\] is used to obtain the URL of the current page. #Sys\["locale"\] is used to obtain the language of the current system. #Sys\["location"\]is used to obtain the longitude and latitude of the current system. |
| #Form\[xxx\] | Obtains the value of a component in a form. For example, #Form\[formPanel1.textInput\],formPanel1 indicates the ID of the formPanel component, and textInput indicates the ID of the dataField component. | **Parent topic:** [[Mateline Mobile Component Usage Guide|Mateline Mobile Component Usage Guide]]