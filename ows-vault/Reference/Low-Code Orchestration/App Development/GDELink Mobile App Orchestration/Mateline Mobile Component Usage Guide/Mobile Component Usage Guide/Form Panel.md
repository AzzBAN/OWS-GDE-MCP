---
title: "Form Panel"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001734125838.html"
depth: 5
---
# Form Panel

**Properties**

N/A

**APIs**

**get**

Input parameter: sid

Output parameters: component objects

Description: Obtain component objects in a form based on the component ID.

Example:

C("form").get("defaultTextInput")

// Same as C("defaultTextInput")

**getFieldValue**

Input parameter: sid

Output parameters: component values

Description: Obtain values of the component objects in a form based on the component ID.

Example:

C("form").getFieldValue("defaultTextInput")

// Same as C("defaultTextInput").getValue()

**getInputData**

Input parameters: none

Output parameters: component name-value pairs

Description: Obtain the input data of a form.

Example:

C("form").getInputData()

**getSubmitData**

Input parameters: none

Output parameters: component name-value pairs

Description: Obtain the form data that can be submitted.

Example:

C("form").getSubmitData()

**setInputData**

Input parameters: component name-value pairs

Output parameters: none

Description: Set the form data.

Example:

C("form").setInputData({defaultTextInput:"A"})

**getWidgets**

Input parameters: none

Output parameters: component objects

Description: Obtain all component objects of a form.

Example:

C("form").getWidgets()

**getUploadData**

Input parameters: none

Output parameters: data to be uploaded

Description: Obtain the data to be uploaded, such as signatures and images.

Example:

C("form").getUploadData()

**Events**

**before\_validate**

Description: pre-verification event

Example:

C("id").on("before\_validate",function(validator){

//do something

})

**after\_validate**

Description: This event is triggered after verification. If the value of **result** is **false**, the logic stops the execution.

Example:

C("id").on("after\_validate",function(result){

//do something

})

**FAQs**

Scenarios

1\. Dynamically obtain form data through services.

2\. Reload form data.

3\. Listen to the loading completion event of the form data and execute the custom method after the form loading is complete.

**Precautions**

Configure the dataField component. The component can be used with service buttons to submit data to services.

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]