---
title: "Expressions for Dynamically Accessing Component Property Values"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001316479068.html"
depth: 7
children: ["#Get", "#Row", "#Sys", "#Form", "#ListForm"]
---
# Expressions for Dynamically Accessing Component Property Values

Dynamic variable parameters are used in scenarios where dynamic parameters need to be transferred during page orchestration. For example, if the initialization of a list page needs to call a service to query data and the service input parameter needs to transfer an ID contained in the page URL, you can use **#Get**_\[id\]_ during service configuration to dynamically obtain the ID in the URL.

 
| Variable | Description |
| :-- | :-- |
| #Get\[xxx\] | Obtained the parameter value transferred from the source page, for example, Nf.PageManager.open ("/demo/test/PersonSelect," { "task\_id": "001"}). Use #Get\[task\_id\] to return 001. |
| #Row\[xxx\] | Available in the list view component, indicating that the field data, for example, #Row\[leavel\_id\], corresponding to the row list is obtained. |
| #Sys\[xxx\] | Obtained the values of variables including #Sys\[utc\]: provided by the system, or obtained the current UTC time. #Sys\[now\]: Obtained the current time. #Sys\[localtime\]: Obtained current local time. #Sys\[username\]: Obtained the current user name. #Sys\[userinfo\]: Obtained the information about the current user. #Sys\[url\]: Obtained the URL of the current page. #Sys\[locale\]: Obtained the language of the current system. #Sys\[location\]: Obtained the longitude and latitude of the current system. |
| #Form\[xxx\] | Obtained value of a component in a form. For example, #Form\[formPanel1.textInput\],formPanel1 indicates the ID of the formPanel component, and textInput indicates the ID of the dataField component. |
| #ListForm\[xxx\] | Obtained value of a component in a list form. For example, #ListForm\[listForm1.template1.row1.text\],listForm1 indicates the ID of the listForm component in the list form, and template1 indicates the form view template. row1 indicates the ID of the row component in the row layout, and text indicates the ID of the dataField component. |
| #Encode\[xxx\] | Returned empty string when the value of a parameter is null. | -   **[[#Get|#Get]]**  
    
-   **[[#Row|#Row]]**  
    
-   **[[#Sys|#Sys]]**  
    
-   **[[#Form|#Form]]**  
    
-   **[[#ListForm|#ListForm]]**  
    

**Parent topic:** [[Component Property Configuration|Component Property Configuration]]

## Sub-topics

- [[#Get]]
- [[#Row]]
- [[#Sys]]
- [[#Form]]
- [[#ListForm]]
